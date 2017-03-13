"""Where all the good stuff happens in the bot."""
from contextlib import suppress
from collections import deque
from fnmatch import filter
from datetime import datetime
from asteval import Interpreter
from .commands.bot import ProContext, StringView, CommandError, CommandNotFound
from convert_to_old_syntax import cur_dir, rc_files
from properties import storage_backend
from util.datastore import DataStore
from util.const import *
from util.func import dprint, _get_variable
from util.fake import FakeObject
from util.token import is_bot
import distutils.dir_util
import util.token as token
import util.dynaimport as di
for mod in ['asyncio', 'random', 'inspect', 'subprocess', 'os', 'sys', 'gc',
            'traceback', 're', 'shutil', 'math', 'logging', 'async_timeout',
            'discord', 'pickledb']:
    globals()[mod] = di.load(mod)
json = di.load('util.json')
commands = di.load('util.commands')
rank = di.load('util.ranks')

try:
    from ex_props import store_path
    opath = store_path
except ImportError:
    opath = None

try:
    import psutil
    have_psutil = True
except ImportError:
    have_psutil = False
    if sys.platform in ['linux', 'linux2', 'darwin']:
        import resource

class GoldBot(commands.Bot):
    """The brain of the bot, GoldBot."""

    def __init__(self, **options):
        self.logger = logging.getLogger('bot')
        self.is_restart = False
        self.loop = asyncio.get_event_loop()
        self.perm_mask = '1609825363' # 66321741 = full
        self.game = {
            'name': 'with you',
            'type': 0,
            'url': 'https://www.twitch.tv/'
        }
        self.status = 'online'
        self.presence = {}
        self.chars = 0
        self.words = 0
        self.lines = 0
        self.files = 0
        self.size_bytes = 0
        self.raw_sizes_bytes = set()
        self.size_kb = 0
        self.avg_size_bytes = 0
        self.avg_size_kb = 0
        for fn in filter(rc_files(cur_dir), '*.py'):
            with open(fn, 'rb') as f: # fix for windows unicode error
                fr = f.read().decode('utf-8') # fix for windows unicode error
                self.chars += len(fr)
                self.words += len(fr.split())
                self.lines += len(fr.split('\n'))
                self.files += 1
            self.raw_sizes_bytes.add(os.path.getsize(fn))
        self.size_bytes = sum(self.raw_sizes_bytes)
        self.avg_size_bytes = self.size_bytes / self.files
        self.size_kb = self.size_bytes / 1000
        self.avg_size_kb = self.size_kb / self.files
        self.git_rev = 'Couldn\'t fetch'
        try:
            self.git_rev = subprocess.check_output(['git', 'describe', '--always']).decode('utf-8')
        except Exception:
            pass
        self.start_time = datetime.now()
        self.dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].core_file))
        self.storepath = os.path.join(self.dir, 'storage.')
        if storage_backend not in DataStore.exts:
            self.logger.critical('Invalid storage backend specified, quitting!')
        self.version = '0.0.1'
        with open(os.path.join(cur_dir, '__init__.py')) as f:
            self.version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
        self.store = None
        if opath:
            self.store = DataStore(storage_backend, path=opath, join_path=False)
        else:
            self.store = DataStore(storage_backend)
        self.storage = None
        if storage_backend == 'leveldb':
            import plyvel
            self.storage = plyvel.load()
        elif storage_backend == 'pickledb':
            self.storage = pickledb.load(self.storepath, False)
        self.modules = sys.modules
        self.dc_ver = discord.version_info
        self.lib_version = '.'.join([str(i) for i in self.dc_ver])
        self.store_writer = self.loop.create_task(self.store.commit_task())
        self.asteval = None
        self.loop.create_task(self.reset_asteval())
        self.have_resource = False
        if sys.platform in ['linux', 'linux2', 'darwin']:
            self.have_resource = True
        self.loop.create_task(self.update_emote_data())
        self.emotes = {}
        self.dl_cogs_path = os.path.join(self.dir, 'cogs')
        self.ex_cogs_path = os.path.join(self.dir, 'cogs.txt')
        self.dis_cogs_path = os.path.join(self.dir, 'disabled_cogs.txt')
        self.init_dl_cogs_path = os.path.join(self.dir, 'cogs', '__init__.py')
        self.data_cogs_path = os.path.join(self.dir, 'data')
        self.cog_json_cogs_path = os.path.join(self.dir, 'data', 'cogs.json')
        self.cogs_cog_py_path = os.path.join(self.dir, 'cogs', 'cog.py')
        for name in ['dl', 'data']: # Dirs
            p = getattr(self, name + '_cogs_path')
            with suppress(OSError):
                if not os.path.exists(p):
                    os.makedirs(p)
        for name in ['ex', 'dis']: # Files
            p = getattr(self, name + '_cogs_path')
            with suppress(OSError):
                if not os.path.exists(p):
                    f = open(p, 'a')
                    f.close()
        with suppress(OSError):
            if not os.path.exists(self.init_dl_cogs_path):
                with open(self.init_dl_cogs_path, 'w+') as f:
                    f.write('"""Placeholder to make Python recognize this as a module."""\n')
        with suppress(IOError):
            if not os.path.exists(self.cogs_cog_py_path):
                shutil.copy2(os.path.join(self.dir, 'default_cogs', 'cog.py'), self.cogs_cog_py_path)
        self.disabled_cogs = []
        with open(self.dis_cogs_path, 'r') as f:
            self.disabled_cogs = [c.replace('\n', '').replace('\r', '') for c in f.readlines()]
        self.enabled_cogs = []
        with open(self.ex_cogs_path, 'r') as f:
            self.enabled_cogs = [c.replace('\n', '').replace('\r', '') for c in f.readlines()]
        if not os.path.exists(self.cog_json_cogs_path):
            with open(self.cog_json_cogs_path, 'a') as f:
                f.write('{}')
        self.server_map = {}
        if 'nobroadcast' not in self.store.store:
            self.store.store['nobroadcast'] = ['110373943822540800']
        if 'owner_messages' not in self.store.store:
            self.store.store['owner_messages'] = []
        self.command_calls = {}
        self.event_calls = {}
        self.app_info = None
        self.owner_user = None
        self.selfbot = not is_bot
        if 'utils_revision' not in self.store.store:
            self.store['utils_revision'] = 1
        if self.store.store['utils_revision'] < 2:
            distutils.dir_util.copy_tree(os.path.join(cur_dir, 'default_cogs', 'utils'), os.path.join(cur_dir, 'cogs', 'utils') + os.path.sep)
            self.store['utils_revision'] = 2
        super().__init__(**options)
        self.commands = {}

    async def update_presence(self):
        """Generate an updated presence and change it."""
        self.presence = dict(status=discord.Status(self.status))
        if self.game['name']:
            self.presence['game'] = discord.Game(**self.game)
        await self.change_presence(**self.presence)

    async def send(self, *apass, **kwpass):
        await self.send_message(*apass, **kwpass)
    async def msend(self, msg, *apass, **kwpass):
        await self.send_message(msg.channel, *apass, **kwpass)
    async def csend(self, ctx, *apass, **kwpass):
        await self.send_message(ctx.message.channel, *apass, **kwpass)

    async def on_ready(self):
        """On_ready event for when the bot logs into Discord."""
        self.logger.info('Bot has logged into Discord, ID ' + self.user.id)
        if self.selfbot:
            self.game['name'] = ''
            self.game['type'] = 0
            self.game['url'] = ''
        else:
            await self.update_presence()
        if self.user.bot:
            self.app_info = await self.application_info()
            self.owner_user = self.app_info.owner
            self.store.store['owner_id'] = self.owner_user.id
        else:
            self.store.store['owner_id'] = self.user.id
            self.owner_user = self.user
        self.logger.info('Owner information automatically filled.')
        if (not self.selfbot) and len(self.servers) >= 75:
            await self.send_message(self.owner_user, "I've just started up!\nThe time is **%s**." % datetime.now().strftime(absfmt))

    async def on_message(self, msg):
        try:
            myself = msg.server.me
        except AttributeError:
            myself = self.user
        bname = myself.display_name
        if self.selfbot:
            try:
                cmdfix = self.store['properties']['global']['selfbot_prefix']
            except KeyError:
                cmdfix = myself.name[0].lower() + '.'
            prefix_convo = False
            do_logic = msg.author.id == self.user.id
        else:
            cmdfix = self.store.get_cmdfix(msg)
            prefix_convo = (self.store.get_prop(msg, 'prefix_answer')) in bool_true
            do_logic = msg.author.id != self.user.id
        prefix_help = (msg.server.id if msg.server else None) != '110373943822540800' # DBots
        lbname = bname.lower()
        if do_logic:
            if msg.author.bot:
                if self.status == 'invisible': return
                if not self.selfbot:
                    self.dispatch('bot_message', msg)
            else:
                if self.selfbot:
                    if msg.content.startswith(cmdfix):
                        await self.process_commands(msg, cmdfix)
                    else:
                        self.dispatch('not_command', msg)
                    return
                if not msg.channel.is_private:
                    if not msg.content.startswith(cmdfix):
                        self.dispatch('not_command', msg)
                if self.status == 'invisible':
                    if msg.content.lower().startswith(cmdfix + 'resume'):
                        self.status = 'online'
                        await self.update_presence()
                        await self.msend(msg, 'Successfully **resumed** my features!')
                elif msg.channel.is_private:
                    if msg.content.startswith(cmdfix):
                        await self.process_commands(msg, cmdfix)
                    else:
                        self.dispatch('pm', msg)
                elif msg.content.lower().startswith(lbname + ' ') and prefix_convo:
                    self.dispatch('prefix_convo', msg, lbname)
                elif (msg.content.lower() in ['prefix', 'prefix?']) and prefix_help:
                    await self.msend(msg, '**Current server command prefix is: **`' + cmdfix + '`')
                else:
                    if msg.content.startswith(cmdfix):
                        await self.process_commands(msg, cmdfix)
                    elif myself.mentioned_in(msg) and ('@everyone' not in msg.content) and ('@here' not in msg.content):
                        self.dispatch('mention', msg)
        else:
            self.logger.debug('Didn\'t meet check for main on_message processing')

    async def on_error(self, *a, **b):
        await self.cogs['Errors'].on_error(*a, **b)

    async def on_server_join(self, server):
        """Send the bot introduction message when invited."""
        self.logger.info('New server: ' + server.name + ', yay!')
        self.update_server_map()
        if self.selfbot: return
        try:
            await self.send_message(server.default_channel, join_msg)
        except discord.Forbidden:
            satisfied = False
            c_count = 0
            try_channels = list(server.channels)
            channel_count = len(try_channels) - 1
            while not satisfied:
                with suppress(discord.Forbidden, discord.HTTPException):
                    await self.send_message(try_channels[c_count], join_msg)
                    satisfied = True
                if c_count > channel_count:
                    self.logger.warning('Couldn\'t announce join to server ' + server.name)
                    satisfied = True
                c_count += 1
    async def on_server_remove(self, server):
        """Update the stats."""
        self.logger.info('Lost a server: ' + server.name + ', aww :\\')
        self.update_server_map()

    def update_server_map(self):
        self.server_map = {s.id: s for s in self.servers}

    async def suspend(self):
        """Suspend the bot."""
        self.status = 'invisible'
        await self.update_presence()

    def dispatch(self, event, *args, **kwargs):
        commands.Bot.dispatch(self, event, *args, **kwargs)
        if event in self.event_calls:
            self.event_calls[event] += 1
        else:
            self.event_calls[event] = 1

    async def process_commands(self, message, prefix):
        """This function processes the commands that have been registered."""
        if self.status == 'invisible': return
        _internal_channel = message.channel
        _internal_author = message.author
        view = StringView(message.content)
        view.skip_string(prefix)
        cmd = view.get_word()
        tmp = {
            'bot': self,
            'invoked_with': cmd,
            'message': message,
            'view': view,
            'prefix': prefix
        }
        ctx = ProContext(**tmp)
        del tmp
        cl = cmd.lower().replace('é', 'e').replace('è', 'e') # TODO: Real accent parsing

        if cl in self.commands:
            command = self.commands[cl]
            self.dispatch('command', command, ctx)
            try:
                if command.name in self.command_calls:
                    self.command_calls[command.name] += 1
                else:
                    self.command_calls[command.name] = 1
                await command.invoke(ctx)
            except CommandError as exp:
                ctx.command.dispatch_error(exp, ctx)
            else:
                self.dispatch('command_completion', command, ctx)
        else:
            exc = CommandNotFound('Command "{}" is not found'.format(cmd))
            self.dispatch('command_error', exc, ctx)

    async def send_typing(self, destination):
        """Send a typing status to the destination. """
        if self.status == 'invisible': return
        channel_id, guild_id = await self._resolve_destination(destination)
        await self.http.send_typing(channel_id)

    async def format_uptime(self):
        """Return a human readable uptime."""
        s = lambda n: '' if n == 1 else 's'
        fmt = '{0} day{4} {1} hour{5} {2} minute{6} {3} second{7}'
        time_diff = datetime.now() - self.start_time
        time_mins = divmod(time_diff.total_seconds(), 60)
        time_hrs = divmod(time_mins[0], 60)
        time_days = divmod(time_hrs[0], 24)
        final = fmt.format(int(time_days[0]), int(time_days[1]), int(time_hrs[1]), int(time_mins[1]),
                           s(time_days[0]), s(time_days[1]), s(time_hrs[1]), s(time_mins[1]))
        return final

    async def send_message(self, destination, content=None, *, tts=False, embed=None, filter=True):
        """Sends a message to the destination given with the content given."""
        channel_id, guild_id = await self._resolve_destination(destination)
        if content:
            content = str(content)
            if len(content) > 2000:
                truncate_msg = '**... (truncated)**'
                #rmatch = len(re.findall('```', content))
                #if rmatch % 2 != 0: # odd number
                if '```' in content:
                    truncate_msg = '```' + truncate_msg
                content = content[:2000 - len(truncate_msg)] + truncate_msg
            elif len(content) <= 1999:
                if self.selfbot:
                    if filter:
                        content += '\u200b'
        if embed:
            embed = embed.to_dict()
        try:
            data = await self.http.send_message(channel_id, content, guild_id=guild_id, tts=tts, embed=embed)
            channel = self.get_channel(data.get('channel_id'))
            message = self.connection._create_message(channel=channel, **data)
            return message
        except discord.HTTPException as e:
            if embed: # let's try non embed
                def final_perms():
                    if isinstance(destination, discord.User):
                        return ('embed_links',)
                    elif isinstance(destination, discord.Server):
                        return [k[0] for k in list(destination.me.permissions_in(destination.default_channel)) if k[1]]
                    elif isinstance(destination, discord.Channel):
                        if destination.is_private:
                            return ('embed_links',)
                        else:
                            return [k[0] for k in list(destination.server.me.permissions_in(destination)) if k[1]]
                    else:
                        raise e # 244929610146381824 244929610792304640 244929610607886337
                e_text = '```md\n'
                if 'author' in embed:
                    e_text += embed['author']['name'] + '\n\n'
                for kv in embed['fields']:
                    e_text += kv['name'] + '\n-----------------------------------\n' + kv['value'] + '\n\n'
                if 'footer' in embed:
                    e_text += embed['footer']['text']
                if 'embed_links' in final_perms():
                    e_text += '```\n⚠ An error occured sending the embed. Contact the bot owner for more help.'
                else:
                    e_text += '```\n⚠ I need the **Embed Links** permission to send embeds!'
                try:
                    data = await self.http.send_message(channel_id, (content if content else '') + '\n' + e_text, guild_id=guild_id, tts=tts, embed=None)
                except discord.HTTPException:
                    raise e
                channel = self.get_channel(data.get('channel_id'))
                message = self.connection._create_message(channel=channel, **data)
                return message
            elif self.selfbot and destination.id == self.user.id:
                self.logger.warning('Sending to ourselves. what??')
                destination = _get_variable('_internal_channel')
                channel_id, guild_id = await self._resolve_destination(destination)
                data = await self.http.send_message(channel_id, content, guild_id=guild_id, tts=tts, embed=embed)
                channel = self.get_channel(data.get('channel_id'))
                message = self.connection._create_message(channel=channel, **data)
                return message
            else:
                raise e # didn't mean to catch that

    async def send_cmd_help(self, ctx):
        """Send command help for a command or subcommand."""
        if ctx.invoked_subcommand:
            pages = self.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await self.csend(ctx, page)
        else:
            pages = self.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await self.csend(ctx, page)

    async def get_ram(self):
        """Get the bot's RAM usage info."""
        if have_psutil: # yay!
            mu = psutil.Process(os.getpid()).memory_info().rss
            return (True, mu / 1_000_000, mu / 1048576)
        else: # aww
            raw_musage = 0
            got_conversion = False
            musage_dec = 0
            musage_hex = 0
            if sys.platform.startswith('linux'): # Linux & Windows report in kilobytes
                raw_musage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                got_conversion = True
                musage_dec = raw_musage / 1000
                musage_hex = raw_musage / 1024
            elif sys.platform == 'darwin': # Mac reports in bytes
                raw_musage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                got_conversion = True
                musage_dec = raw_musage / 1000000 # 1 million. 1000 * 1000
                musage_hex = raw_musage / 1048576 # 1024 * 1024
            if got_conversion:
                return (got_conversion, musage_dec, musage_hex)
            else:
                return (got_conversion,)

    async def update_emote_data(self):
        """Fetch Twitch and FrakerFaceZ emote mappings."""
        with open(os.path.join(cur_dir, 'assets', 'emotes_twitch_global.json')) as f:
            twitch_global = json.loads(f.read())['emotes']
        with open(os.path.join(cur_dir, 'assets', 'emotes_twitch_subscriber.json')) as f:
            twitch_sub = json.loads(f.read())
        twitch_subscriber = {e: {'description': '\u200b', 'image_id': twitch_sub[e], 'first_seen': None} for e in twitch_sub}
        self.emotes['twitch'] = {**twitch_global, **twitch_subscriber}
        with open(os.path.join(cur_dir, 'assets', 'emotes_ffz.json')) as f:
            self.emotes['ffz'] = json.loads(f.read())
        with open(os.path.join(cur_dir, 'assets', 'emotes_bttv.json')) as f:
            raw_json = json.loads(f.read())
            bttv_v1 = {n: 'https:' + raw_json[n] for n in raw_json}
        with open(os.path.join(cur_dir, 'assets', 'emotes_bttv_2.json')) as f:
            raw_json2 = json.loads(f.read())
            bttv_v2 = {n: 'https://cdn.betterttv.net/emote/' + str(raw_json2[n]) + '/1x' for n in raw_json2}
        self.emotes['bttv'] = {**bttv_v1, **bttv_v2}

    async def reset_asteval(self, log_reset=True, reason='upon request', note=''):
        try:
            del self.asteval
        except AttributeError:
            pass
        gc.collect()
        self.asteval = Interpreter(use_numpy=False, writer=FakeObject(value=True))
        self.asteval.symtable['print'] = dprint
        del self.asteval.symtable['dir']
        if log_reset:
            if note:
                note = ' (' + note + ')'
            self.logger.warning(f'Reset ASTEval interpreter {reason}!{note}')
    def del_command(self, *names):
        """Remove a command and its aliases."""
        for name in names:
            for a in self.commands[name].aliases:
                del self.commands[a]
            del self.commands[name]
