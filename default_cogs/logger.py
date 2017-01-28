"""The bot's chatlogger for AI training."""
import asyncio
import os
import util.commands as commands
from util.perms import echeck_perms
from .cog import Cog

class Logger(Cog):
    """Chat logger for collecting AI training data."""

    def __init__(self, bot):
        super().__init__(bot)
        self.int = 6 * 60
        self.log = {}
        self.w_task = self.loop.create_task(self.writer())
        self.active = True

    def __unload(self):
        self.w_task.cancel()
        self.bot.loop.create_task(self.write())

    async def on_message(self, msg):
        """Log messages."""
        if not self.active: return
        try:
            self.log[msg.channel.id].append(msg.content)
        except (KeyError, AttributeError):
            self.log[msg.channel.id] = [msg.content]

    async def write(self):
        """Commit logs to disk."""
        t_len = 0
        for channel in self.log:
            ct = '\n'.join(self.log[channel])
            t_len += len(ct)
            with open(os.path.join(self.bot.dir, 'data', 'logger', channel + '.log'), 'ab') as f:
                f.write(b'\n' + ct.encode('utf-8'))
        self.log = {}
        self.bot.logger.info(f'Wrote {t_len} characters of chatlogs!')
        return t_len

    async def writer(self):
        """Writer task"""
        while True:
            await asyncio.sleep(self.int)
            await self.write()

    @commands.group(pass_context=True, aliases=['chatlog', 'log'], name='logger')
    async def cmd_logger(self, ctx):
        """Control panel for the logger.
        Usage: logger {stuff}"""
        await echeck_perms(ctx, ('bot_owner',))
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @cmd_logger.command(aliases=['commit', 'save'], name='write')
    async def cmd_write(self):
        """Commit all the logs to disk.
        Usage: logger write"""
        await self.bot.say('**Writing...**')
        s = await self.write()
        await self.bot.say('**Wrote `%s` characters**' % str(s))

    @cmd_logger.command()
    async def wstart(self):
        """Start the 6-min writer task.
        Usage: logger wstart"""
        self.w_task = self.loop.create_task(self.writer())
        await self.bot.say('**Started 6-min writer task!**')

    @cmd_logger.command()
    async def wstop(self):
        """Stop the 6-min writer task.
        Usage: logger wstop"""
        self.w_task.cancel()
        await self.bot.say('**Stopped 6-min writer task!**')

    @cmd_logger.command()
    async def start(self):
        """Start logging messages.
        Usage: logger start"""
        self.active = True
        await self.bot.say('**Now logging messages!**')

    @cmd_logger.command()
    async def stop(self):
        """Stop logging messages.
        Usage: logger stop"""
        self.active = False
        await self.bot.say('**No longer logging messages!**')

    @cmd_logger.command(pass_context=True)
    async def clast(self, ctx, *count: int):
        """Get the last messages from this channel.
        Usage: logger clast {count}"""
        if not count:
            n = 12
        else:
            n = count[0]
        await self.bot.say('\n'.join(self.log[ctx.message.channel.id][-n:]))

def setup(bot):
    log_dir = os.path.join(bot.dir, 'data', 'logger')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    bot.add_cog(Logger(bot))
