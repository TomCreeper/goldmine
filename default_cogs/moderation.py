"""Small moderation cog."""
import re
import discord
import util.commands as commands
from .cog import Cog

class Moderation(Cog):
    """Some moderation at least."""
    def __init__(self, bot):
        super().__init__(bot)
        self.logger = self.logger.getChild('automod')

    async def on_not_command(self, msg):
        if self.bot.selfbot: return
        if msg.author.id == self.bot.user.id: return
        if ('_' in msg.content) or ('*' in msg.content):
            if re.search(r'[_*~]{1000,}', msg.content):
                try:
                    await self.bot.delete_message(msg)
                except discord.Forbidden:
                    self.logger.warning('Couldn\'t delete iOS crash message in ' + \
                                        msg.server.name + ', sent by ' + str(msg.author))
                    return
                await self.bot.send_message(msg.channel, msg.author.mention + \
                                            ' **:japanese_goblin: Stop crashing iOS users!**')

def setup(bot):
    bot.add_cog(Moderation(bot))
