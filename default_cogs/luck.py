"""Definition of the bot's Luck module.'"""
import asyncio
import random

import util.commands as commands
from .cog import Cog

class Luck(Cog):
    """Commands that require some luck to use.
    Lose the coin toss for me, will you?
    """

    @commands.command(aliases=['choice', 'rand'])
    async def choose(self, *choices: str):
        """Chooses between choices given.
        Usage: choose [choice 1] [choice 2] [choice 3] [etc...]"""
        await self.bot.say(random.choice(choices))

    @commands.command(aliases=['flipcoin', 'coin', 'coinflip'])
    async def flip(self):
        """Flip a virtual coin.
        Usage: flip"""
        await self.bot.say('The coin toss revealed... ' + random.choice(['Heads', 'Tails']) + '!')

    @commands.command(aliases=['dice', 'rolldice', 'rolld', 'droll', 'diceroll'])
    async def roll(self, dice: str):
        """Rolls a virtual dice in [# of rolls]d[Range: 1-N] format.
        Usage: roll [number of rolls]d[max number, normally 6]"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(aliases=['gfight'])
    async def googlefight(self, tg1: str, tg2: str):
        """Generates a Google Fight link.
        Usage: gfight [target 1] [target 2]"""
        await self.bot.say('http://www.googlefight.com/' + tg1.title() + '-vs-' + tg2.title() + '.php')

def setup(bot):
    c = Luck(bot)
    bot.add_cog(c)
