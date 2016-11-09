import asyncio
import io
import random

import discord
from discord.ext import commands


class Roleplay:
    """Commands related to roleplay.
    Examples: poking, stabbing, and color roles.
    """
    adjs = [
        'lovingly',
        'lamely',
        'limply',
        'officially',
        'for money',
        'sadly',
        'roughly',
        'angrily',
        'harshly',
        'without hesitation',
        'quickly',
        'greedily',
        'shamefully',
        'dreadfully',
        'painfully',
        'intensely',
        'digitally',
        'unofficially',
        'nervously',
        'invitingly',
        'seductively',
        'embarassingly',
        'thoroughly',
        'doubtfully',
        'proudly'
    ]
    fights = [
        'pokes {0} with a spear',
        'impales {0}',
        'stabs {0}',
        'guts {0} with a stone knife',
        'eviscerates {0} with a sharp stone',
        'decapitates {0} with a wand',
        'fires cruise missle at {0}',
        'backstabs {0}',
        'punches {0}',
        'poisons {0}',
        'opens trapdoor under {0}',
        '360 quick scopes {0}',
        'noscopes {0}',
        'normally snipes {0}',
        'uses katana to slice through {0}',
        'deadly stares at {0}',
        'uses a trebuchet to shoot a 95kb projectile over 300 meters at {0}',
        'snaps neck from {0}',
        'pours lava over {0}',
        'dumps acid above {0}',
        'shoots with a glock 17 at {0}',
        'incinerates {0}',
        'uses a tridagger to stab {0}',
        'assasinates {0}',
        'fires with a minigun at {0}',
        'fires with bazooka at {0}',
        'uses granny bomb at {0}',
        'throws bananabomb at {0}',
        'throws holy grenade at {0}'
    ]
    death = [
        '{0} dies.',
        '{0} survives.',
        'Blood pours from {0}.',
        '{0} heals themself.',
        'Fairies take {0} away.',
        'An old man carries {0} away.',
        '{0} is in shock.',
        '{0} passes out.'
    ]
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def poke(self, ctx, target: str):
        """Pokes someone... with random results!"""
        await self.bot.say('*' + ctx.message.author.display_name + '* pokes *' +
                           target + '* **' + random.choice(self.adjs) + '**.')

    @commands.command(pass_context=True)
    async def boop(self, ctx, target: str):
        """Boops someone with possibly satisfying results."""
        await self.bot.say('*' + ctx.message.author.display_name + '* boops *' +
                           target + '* **' + random.choice(self.adjs) + '**.')

    @commands.command(pass_context=True)
    async def stab(self, ctx, target: str):
        """Floran besst sssstabber! Painful, too."""
        await self.bot.say('*' + ctx.message.author.display_name + '* ' +
                           random.choice(self.fights).format(target) + '. '
                           + random.choice(self.death).format(target))

    @commands.command(pass_context=True)
    async def attack(self, ctx, target: str):
        """Hurts someone with determination in the shot."""
        await self.bot.say('*' + ctx.message.author.display_name + '* ' +
                           random.choice(self.fights).format(target) + '. '
                           + random.choice(self.death).format(target))

    @commands.command()
    async def charlie(self, *args):
        """Ask a question... Charlie Charlie are you there?"""
        await self.bot.say('*Charlie Charlie* ' + ' '.join(args) + "?\n**" +
                           random.choice(['Yes', 'No']) + '**')