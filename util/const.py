import re
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
    'deadily stares at {0}',
    'uses a trebuchet to shoot a 95kg projectile over 300 meters at {0}',
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
weird_faces = [
    "'~~~__***=***__~~~'",
    '''```──────────▄▄▄▄▄▄▄▄▄▄▄──────────
─────▄▄▀▀▀▀──────────▀▀▄▄──────
───▄▀───────────────────▀▀▄────
──█────────────────────────█───
─█─────────────────────▄▀▀▀▀▀█▄
█▀────────────────────█────▄███
█─────────────────────█────▀███
█─────▄▀▀██▀▄─────────█───────█
█────█──████─█─────────▀▄▄▄▄▄█─
█────█──▀██▀─█───────────────█─
█────█───────█──────────────▄▀─
█────▀▄─────▄▀──▄▄▄▄▄▄▄▄▄───█──
█──────▀▀▀▀▀────█─█─█─█─█──▄▀──
─█──────────────▀▄█▄█▄█▀──▄▀───
──█──────────────────────▄▀────
───▀▀▀▄──────────▄▄▄▄▄▄▀▀──────
────▄▀─────────▀▀──▄▀──────────
──▄▀───────────────█───────────
─▄▀────────────────█──▄▀▀▀█▀▀▄─
─█────█──█▀▀▀▄─────█▀▀────█──█─
▄█────▀▀▀────█─────█────▀▀───█─
█▀▄──────────█─────█▄────────█─
█──▀▀▀▀▀█▄▄▄▄▀─────▀█▀▀▀▄▄▄▄▀──
█───────────────────▀▄─────────```''',
    '''```░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░```''',
    '''```▒▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█
▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄
▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█
▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█
▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█
▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█
▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█
▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█
▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█```''',
    '''```▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░```''',
'''```░░░░░░░░░░░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░▀▄░░░░░░▄░░░░░░░░░░
░░░░░░░░░░█░░▀░░▀░░░░░▀▄▄░░█░█░░░░░░░░░
░░░░░░░░░░█░▄░█▀░▄░░░░░░░▀▀░░█░░░░░░░░░
░░░░░░░░░░█░░▀▀▀▀░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░░░░█░░▄▄░░▄▄▄▄░░▄▄░░█░░░░░░░░░░
░░░░░░░░░░░█░▄▀█░▄▀░░█░▄▀█░▄▀░░░░░░░░░░
░░░░░░░░░░░░▀░░░▀░░░░░▀░░░▀░░░░░░░░░░░░
╔═════════════════════════════════════╗
║ * You feel like you're going to     ║
║ have a ruff time.                   ║
║                                     ║
╚═════════════════════════════════════╝
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│/ FIGHT│ │)  PET | |6 ITEM | |x MERCY|
└───────┘ └───────┘ └───────┘ └───────┘```''',
    '¯\\_(ツ)_/¯',
    '(╯°□°）╯︵ ┻━┻',
    '┬─┬﻿ ノ( ゜-゜ノ)',
    '''```     (`)
   / /
  / /
 / /
(_)_)```''',
    r'''```...................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
```''',
    r'''``` ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ________
||` |||1 |||2 |||3 |||4 |||5 |||6 |||7 |||8 |||9 |||0 |||- |||= |||BS    ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||______||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/______\|
 ________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
||TAB   |||Q |||W |||E |||R |||T |||Y |||U |||I |||O |||P |||[ |||] |||\ ||
||______|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ________
||CAPS   |||A |||S |||D |||F |||G |||H |||J |||K |||L |||; |||' |||ENTER ||
||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||______||
|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/______\|
 ___________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ___________
||SHIFT    |||Z |||X |||C |||V |||B |||N |||M |||, |||. |||/ |||SHIFT    ||
||_________|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_________||
|/_________\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_________\|```''',
    '''```███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████```''',
    '''▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░█▒▒▄▀▀▀▀▀▄▄▒▒▒▒▒▒▒▒▒▄▄▀▀▀▀▀▀▄
░░▄▀▒▒▒▄█████▄▒█▒▒▒▒▒▒▒█▒▄█████▄▒█
░█▒▒▒▒▐██▄████▌▒█▒▒▒▒▒█▒▐██▄████▌▒█
▀▒▒▒▒▒▒▀█████▀▒▒█▒░▄▒▄█▒▒▀█████▀▒▒▒█
▒▒▐▒▒▒░░░░▒▒▒▒▒█▒░▒▒▀▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█
▒▌▒▒▒░░░▒▒▒▒▒▄▀▒░▒▄█▄█▄▒▀▄▒▒▒▒▒▒▒▒▒▒▒▌
▒▌▒▒▒▒░▒▒▒▒▒▒▀▄▒▒█▌▌▌▌▌█▄▀▒▒▒▒▒▒▒▒▒▒▒▐
▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▀███▀▒▌▒▒▒▒▒▒▒▒▒▒▒▒▌
▀▀▄▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒█
▀▄▒▀▄▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▄▄▀
▒▒▀▄▒▀▄▀▀▀▄▀▀▀▀▄▄▄▄▄▄▄▀░░░░▀▀▀▀▀▀
▒▒▒▒▀▄▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐
▒█▀▀▄ █▀▀█ █▀▀█ █▀▀█ 　 ▀▀█▀▀ █░░█ █▀▀ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀
▒█░▒█ █▄▄▀ █░░█ █░░█ 　 ░▒█░░ █▀▀█ █▀▀ 　 ▒█▀▀▄ █▄▄█ ▀▀█ ▀▀█
▒█▄▄▀ ▀░▀▀ ▀▀▀▀ █▀▀▀ 　 ░▒█░░ ▀░░▀ ▀▀▀ 　 ▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀
║████║░░║████║████╠═══╦═════╗
╚╗██╔╝░░╚╗██╔╩╗██╠╝███║█████║
░║██║░░░░║██║╔╝██║███╔╣██══╦╝
░║██║╔══╗║██║║██████═╣║████║
╔╝██╚╝██╠╝██╚╬═██║███╚╣██══╩╗
║███████║████║████║███║█████║
▀▀█▀▀ ▒█▀▀▀█ ▒█░▒█ ▒█▄░▒█ ░█▀▀█ ▒█▀▄▀█ ▀█▀  █ █ █
░▒█░░ ░▀▀▀▄▄ ▒█░▒█ ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█░  ▀ ▀ ▀
░▒█░░ ▒█▄▄▄█ ░▀▄▄▀ ▒█░░▀█ ▒█░▒█ ▒█░░▒█ ▄█▄  ▄ ▄ ▄
'''
]
emojis = '😀😬😁😂😃😄😅😆😇😉😊🙂🙃☺️😋😌😍😘😗😙😚😜😝😛🤑🤓😎🤗😏😶😐😑😒🙄🤔😳😞😟😠😡😔😕🙁☹️😣😖😫😩😤😮😱😨😰😯😦😧😢😥😪😓😭😵😲🤐😷🤒🤕😴💤💩😈👿👹👺💀👻👽🤖😺😸😹😻😼😽🙀😿😾🙌👏👋👍👊✊✌️👌✋💪🙏☝️👆👇👈👉🖕🤘🖖✍️💅👄👅👂👃👁👀👤🗣👶👦👧👨👩👱👴👵👲👳👮👷💂🕵🎅👼👸👰🚶🏃💃👯👫👬👭🙇💁🙅🙆🙋🙎🙍💇💆💑👩‍❤️‍👩👨‍❤️‍👨💏👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👪👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👚👕👖👔👗👙👘💄💋👣👠👡👢👞👟👒🎩⛑🎓👑🎒👝👛👜💼👓🕶💍🌂👦🏻👧🏻👨🏻👩🏻👴🏻👵🏻👶🏻👱🏻👮🏻👲🏻👳🏻👷🏻👸🏻💂🏻🎅🏻👼🏻💆🏻💇🏻👰🏻🙍🏻🙎🏻🙅🏻🙆🏻💁🏻🙋🏻🙇🏻🙌🏻🙏🏻🚶🏻🏃🏻💃🏻💪🏻👈🏻👉🏻☝️🏻👆🏻🖕🏻👇🏻✌️🏻🖖🏻🤘🏻🖐🏻✊🏻✋🏻👊🏻👌🏻👍🏻👎🏻👋🏻👏🏻👐🏻✍🏻💅🏻👂🏻👃🏻🚣🏻🛀🏻🏄🏻🏇🏻🏊🏻⛹🏻🏋🏻🚴🏻🚵🏻👦🏼👧🏼👨🏼👩🏼👴🏼👵🏼👶🏼👱🏼👮🏼👲🏼👳🏼👷🏼👸🏼💂🏼🎅🏼👼🏼💆🏼💇🏼👰🏼🙍🏼🙎🏼🙅🏼🙆🏼💁🏼🙋🏼🙇🏼🙌🏼🙏🏼🚶🏼🏃🏼💃🏼💪🏼👈🏼👉🏼☝️🏼👆🏼🖕🏼👇🏼✌️🏼🖖🏼🤘🏼🖐🏼✊🏼✋🏼👊🏼👌🏼👍🏼👎🏼👋🏼👏🏼👐🏼✍🏼💅🏼👂🏼👃🏼🚣🏼🛀🏼🏄🏼🏇🏼🏊🏼⛹🏼🏋🏼🚴🏼🚵🏼👦🏽👧🏽👨🏽👩🏽👴🏽👵🏽👶🏽👱🏽👮🏽👲🏽👳🏽👷🏽👸🏽💂🏽🎅🏽👼🏽💆🏽💇🏽👰🏽🙍🏽🙎🏽🙅🏽🙆🏽💁🏽🙋🏽🙇🏽🙌🏽🙏🏽🚶🏽🏃🏽💃🏽💪🏽👈🏽👉🏽☝️🏽👆🏽🖕🏽👇🏽✌️🏽🖖🏽🤘🏽🖐🏽✊🏽✋🏽👊🏽👌🏽👍🏽👎🏽👋🏽👏🏽👐🏽✍🏽💅🏽👂🏽👃🏽🚣🏽🛀🏽🏄🏽🏇🏽🏊🏽⛹🏽🏋🏽🚴🏽🚵🏽👦🏾👧🏾👨🏾👩🏾👴🏾👵🏾👶🏾👱🏾👮🏾👲🏾👳🏾👷🏾👸🏾💂🏾🎅🏾👼🏾💆🏾💇🏾👰🏾🙍🏾🙎🏾🙅🏾🙆🏾💁🏾🙋🏾🙇🏾🙌🏾🙏🏾🚶🏾🏃🏾💃🏾💪🏾👈🏾👉🏾☝️🏾👆🏾🖕🏾👇🏾✌️🏾🖖🏾🤘🏾🖐🏾✊🏾✋🏾👊🏾👌🏾👍🏾👎🏾👋🏾👏🏾👐🏾✍🏾💅🏾👂🏾👃🏾🚣🏾🛀🏾🏄🏾🏇🏾🏊🏾⛹🏾🏋🏾🚴🏾🚵🏾👦🏿👧🏿👨🏿👩🏿👴🏿👵🏿👶🏿👱🏿👮🏿👲🏿👳🏿👷🏿👸🏿💂🏿🎅🏿👼🏿💆🏿💇🏿👰🏿🙍🏿🙎🏿🙅🏿🙆🏿💁🏿🙋🏿🙇🏿🙌🏿🙏🏿🚶🏿🏃🏿💃🏿💪🏿👈🏿👉🏿☝️🏿👆🏿🖕🏿👇🏿✌️🏿🖖🏿🤘🏿🖐🏿✊🏿✋🏿👊🏿👌🏿👍🏿👎🏿👋🏿👏🏿👐🏿✍🏿💅🏿👂🏿👃🏿🚣🏿🛀🏿🏄🏿🏇🏿🏊🏿⛹🏿🏋🏿🚴🏿🚵🏿🐶🐱🐭🐹🐰🐻🐼🐨🐯🦁🐮🐷🐽🐸🐙🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🐺🐗🐴🦄🐝🐛🐌🐞🐜🕷🦂🦀🐍🐢🐠🐟🐡🐬🐳🐋🐊🐆🐅🐃🐂🐄🐪🐫🐘🐐🐏🐑🐎🐖🐀🐁🐓🦃🕊🐕🐩🐈🐇🐿🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘🍀🎍🎋🍃🍂🍁🌾🌺🌻🌹🌷🌼🌸💐🍄🌰🎃🐚🕸🌎🌍🌏🌕🌖🌗🌘🌑🌒🌓🌔🌚🌝🌛🌜🌞🌙⭐️🌟💫✨☄☀️🌤⛅️🌥🌦☁️🌧⛈🌩⚡️🔥💥❄️🌨🔥💥❄️🌨☃️⛄️🌬💨🌪🌫☂️☔️💧💦🌊🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🍅🍆🌶🌽🍠🍯🍞🧀🍗🍖🍤🍳🍔🍟🌭🍕🍝🌮🌯🍜🍲🍥🍣🍱🍛🍙🍚🍘🍢🍡🍧🍨🍦🍰🎂🍮🍬🍭🍫🍿🍩🍪🍺🍻🍷🍸🍹🍾🍶🍵☕️🍼🍴🍽⚽️🏀🏈⚾️🎾🏐🏉🎱⛳️🏌🏓🏸🏒🏑🏏🎿⛷🏂⛸🏹🎣🚣🏊🏄🛀⛹🏋🚴🚵🏇🕴🏆🎽🏅🎖🎗🏵🎫🎟🎭🎨🎪🎤🎧🎼🎹🎷🎺🎸🎻🎬🎮👾🎯🎲🎰🎳🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐🚚🚛🚜🏍🚲🚨🚔🚍🚘🚖🚡🚠🚟🚃🚋🚝🚄🚅🚈🚞🚂🚆🚇🚊🚉🚁🛩✈️🛫🛬⛵️🛥🚤⛴🛳🚀🛰💺⚓️🚧⛽️🚏🚦🚥🏁🚢🎡🎢🎠🏗🌁🗼🏭⛲️🎑⛰🏔🗻🌋🗾🏕⛺️🏞🛣🛤🌅🌄🏜🏖🏝🌇🌆🏙🌃🌉🌌🌠🎇🎆🌈🏘🏰🏯🏟🗽🏠🏡🏚🏢🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛⛪️🕌🕍🕋⛩⌚️📱📲💻⌨🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹🎥📽🎞📞☎️📟📠📺📻🎙🎚🎛⏱⏲⏰🕰⏳⌛️📡🔋🔌💡🔦🕯🗑🛢💸💵💴💶💷💰💳💎⚖🔧🔨⚒🛠⛏🔩⚙⛓🔫💣🔪🗡⚔🛡🚬☠⚰⚱🏺🔮📿💈⚗🔭🔬🕳💊💉🌡🏷🔖🚽🚿🛁🔑🗝🛋🛌🛏🚪🛎🖼🗺⛱🗿🛍🎈🎏🎀🎁🎊🎉🎎🎐🎌🏮✉️📩📨📧💌📮📪📫📬📭📦📯📥📤📜📃📑📊📈📉📄📅📆🗓📇🗃🗳🗄📋🗒📁📂🗂🗞📰📓📕📗📘📙📔📒📚📖🔗📎🖇✂️📐📏📌📍🚩🏳🏴🔐🔒🔓🔏🖊🖊🖋✒️📝✏️🖍🖌🔍🔎❤️💛💙💜💔❣️💕💞💓💗💖💘💝💟☮✝️☪🕉☸✡️🔯🕎☯️☦🛐⛎♈️♉️♊️♋️♌️♍️♎️♏️♐️♑️♒️♓️🆔⚛🈳🈹☢☣📴📳🈶🈚️🈸🈺🈷️✴️🆚🉑💮🉐㊙️㊗️🈴🈵🈲🅰️🅱️🆎🆑🅾️🆘⛔️📛🚫❌⭕️💢♨️🚷🚯🚳🚱🔞📵❗️❕❓❔‼️⁉️💯🔅🔆🔱⚜〽️⚠️🚸🔰♻️🈯️💹❇️✳️❎✅💠🌀➿🌐Ⓜ️🏧🈂️🛂🛃🛄🛅♿️🚭🚾🅿️🚰🚹🚺🚼🚻🚮🎦📶🈁🆖🆗🆙🆒🆕🆓0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟🔢▶️⏸⏯⏹⏺⏭⏮⏩⏪🔀🔁🔂◀️🔼🔽⏫⏬➡️⬅️⬆️⬇️↗️↘️↙️↖️↕️↔️🔄↪️↩️⤴️⤵️#️⃣*️⃣ℹ️🔤🔡🔠🔣🎵🎶〰️➰✔️🔃➕➖➗✖️💲💱©️®️™️🔚🔙🔛🔝🔜☑️🔘⚪️⚫️🔴🔵🔸🔹🔶🔷🔺▪️▫️⬛️⬜️🔻◼️◻️◾️◽️🔲🔳🔈🔉🔊🔇📣📢🔔🔕🃏🀄️♠️♣️♥️♦️🎴👁‍🗨💭🗯💬🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧🕺🖤🛑🛴🛵🛶🛒☺️☹☝️✌️✍️❤️❣️☠♨️✈️⌛⌚♈♉♊♋♌♍♎♏♐♑♒♓☀️☁️☂️❄️⛄️☄♠️♥️♦️♣️▶️◀️☎️⌨✉️✏️✒️✂️↗️➡️↘️↙️↖️↕️↔️↩️↪️✡️☸☯️✝️☦☪☮☢☣☑️✔️✖️✳️✴️❇️‼️©️®️™️Ⓜ️▪️▫️#⃣️*️⃣0⃣️1⃣️2⃣️3⃣️4⃣️5⃣️6⃣️7⃣️8⃣️9⃣️⁉️ℹ️⤴️⤵️♻️◻️◼️◽◾☕⚠️☔⏏⬆️⬇️⬅️⚡☘⚓♿⚒⚙⚗⚖⚔⚰⚱⚜⚛⚪⚫🀄⭐⬛⬜⛑⛰⛪⛲⛺⛽⛵⛴⛔⛅⛈⛱⛄⚽⚾️⛳⛸⛷⛹⛏⛓⛩⭕❗🅿️❦♕♛♔♖♜☾→⇒⟹⇨⇰➩➪➫➬➭➮➯➲➳➵➸➻➺➼➽☜☟➹➷↶↷✆⌘⎋⏎⏏⎈⎌⍟❥ツღ☻🇦🇫🇦🇽🇦🇱🇩🇿🇦🇸🇦🇩🇦🇴🇦🇮🇦🇶🇦🇬🇦🇷🇦🇲🇦🇼🇦🇺🇦🇹🇦🇿🇧🇸🇧🇭🇧🇩🇧🇧🇧🇾🇧🇪🇧🇿🇧🇯🇧🇲🇧🇹🇧🇴🇧🇶🇧🇦🇧🇼🇧🇷🇮🇴🇻🇬🇧🇳🇧🇬🇧🇫🇧🇮🇨🇻🇰🇭🇨🇲🇨🇦🇮🇨🇰🇾🇨🇫🇹🇩🇨🇱🇨🇳🇨🇽🇨🇨🇨🇴🇰🇲🇨🇬🇨🇩🇨🇰🇨🇷🇭🇷🇨🇺🇨🇼🇨🇾🇨🇿🇩🇰🇩🇯🇩🇲🇩🇴🇪🇨🇪🇬🇸🇻🇬🇶🇪🇷🇪🇪🇪🇹🇪🇺🇫🇰🇫🇴🇫🇯🇫🇮🇫🇷🇬🇫🇵🇫🇹🇫🇬🇦🇬🇲🇬🇪🇩🇪🇬🇭🇬🇮🇬🇷🇬🇱🇬🇩🇬🇵🇬🇺🇬🇹🇬🇬🇬🇳🇬🇼🇬🇾🇭🇹🇭🇳🇭🇰🇭🇺🇮🇸🇮🇳🇮🇩🇮🇷🇮🇶🇮🇪🇮🇲🇮🇱🇮🇹🇨🇮🇯🇲🇯🇵🇯🇪🇯🇴🇰🇿🇰🇪🇰🇮🇽🇰🇰🇼🇰🇬🇱🇦🇱🇻🇱🇧🇱🇸🇱🇷🇱🇾🇱🇮🇱🇹🇱🇺🇲🇴🇲🇰🇲🇬🇲🇼🇲🇾🇲🇻🇲🇱🇲🇹🇲🇭🇲🇶🇲🇷🇲🇺🇾🇹🇲🇽🇫🇲🇲🇩🇲🇨🇲🇳🇲🇪🇲🇸🇲🇦🇲🇿🇲🇲🇳🇦🇳🇷🇳🇵🇳🇱🇳🇨🇳🇿🇳🇮🇳🇪🇳🇬🇳🇺🇳🇫🇲🇵🇰🇵🇳🇴🇴🇲🇵🇰🇵🇼🇵🇸🇵🇦🇵🇬🇵🇾🇵🇪🇵🇭🇵🇳🇵🇱🇵🇹🇵🇷🇶🇦🇷🇪🇷🇴🇷🇺🇷🇼🇧🇱🇸🇭🇰🇳🇱🇨🇵🇲🇻🇨🇼🇸🇸🇲🇸🇹🇸🇦🇸🇳🇷🇸🇸🇨🇸🇱🇸🇬🇸🇽🇸🇰🇸🇮🇸🇧🇸🇴🇿🇦🇬🇸🇰🇷🇸🇸🇪🇸🇱🇰🇸🇩🇸🇷🇸🇿🇸🇪🇨🇭🇸🇾🇹🇼🇹🇯🇹🇿🇹🇭🇹🇱🇹🇬🇹🇰🇹🇴🇹🇹🇹🇳🇹🇷🇹🇲🇹🇨🇹🇻🇺🇬🇺🇦🇦🇪🇬🇧🇺🇸🇻🇮🇺🇾🇺🇿🇻🇺🇻🇦🇻🇪🇻🇳🇼🇫🇪🇭🇾🇪🇿🇲🇿🇼🤣🤠🤡🤥🤤🤢🤧🤴🤶🤵🤷🤦🤰🤳🤞🤙🤛🤜🤚🤝🦍🦊🦌🦏🦇🦅🦆🦉🦎🦈🦐🦑🦋🥀🥝🥑🥔🥕🥒🥜🥐🥖🥞🥓🥙🥚🥘🥗🥛🥂🥃🥄🥇🥈🥉🥊🥋🤸🤼🤽🤾🤺🥅🤹🥁'
s_emojis = '😀😬😁😂😃😄😅😆😉😊🙂🙃😋😌😗😙😚😜😝😛🤑🤓😎🤗😏😶😐😑😒🙄🤔😳😞😟😠😡😔😕🙁☹️😣😖😫😩😤😮😱😨😰😯😦😧😢😥😪😓😭😵😲🤐😷🤒🤕😴💤💩😈👿👹👺💀👻👽🤖😺😸😹😻😼😽🙀😿😾🙌👏👋👍👊✊✌️👌✋💪🙏☝️👆👇👈👉🖕🤘🖖✍️💅👄👅👂👃👂🏿👃🏿🚣🏿🛀🏿🏄🏿🏇🏿🏊🏿⛹🏿🏋🏿🚴🏿🚵🏿🐶🐱🐭🐹🐰🐻🐼🐨🐯🦁🐮🐷🐽🐸🐙🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🐺🐗🐴🦄🐝🐛🐌🐞🐜🦂🦀🐍🐢🐠🐟🐡🐬🐳🐋🐊🐆🐅🐃🐂🐄🐪🐫🐘🐐🐏🐑🐎🐖🐀🐁🐓🦃🐕🐩🐈🐇🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘🍀🎍🎋🍃🍂🍁🌾🌺🌻🌹🌷🌼🌸💐🍄🌰🎃🐚🌎🌍🌏🌕🌖🌗🌘🌑🌒🌓🌔🌚🌝🌛🌜🌞🌙⭐️🌟💫✨☀️🌤⛅️☁⚡️🔥💥❄️🔥💥❄️☃️⛄️💨☂️☔️💧💦🌊🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🍅🍆🌶🌽🍠🍯🍞🧀🍗🍖🍤🍳🍔🍟🌭🍕🍝🌮🌯🍜🍲🍥🍣🍱🍛🍙🍚🍘🍢🍡🍧🍨🍦🍰🎂🍮🍬🍭🍫🍿🍩🍪🍺🍻🍷🍸🍹🍾🍶🍵☕️🍼🍴⚽️🏀🏈⚾️🎾🏐🏉🎱⛳️🏌🏓🏸🏒🏑🏏🎿⛷🏂🏹🎣🚣🏊🏄🛀⛹🏋🚴🚵🏇🕴🏆🎽🏅🎫🎭🎨🎪🎤🎧🎼🎹🎷🎺🎸🎻🎬🎮👾🎯🎲🎰🎳🚗🚕🚙🚌🚎🚓🚑🚒🚐🚚🚛🚜🏍🚲🚨🚔🚍🚘🚖🚡🚠🚟🚃🚋🚝🚄🚅🚈🚞🚂🚆🚇🚊🚉🚁🛩✈️🛫🛬⛵️🚤🚀💺⚓️🚧⛽️🚏🚦🚥🏁🚢🎡🎢🎠🏗🌁🗼🏭⛲️🎑⛰🏔🗻🌋🗾🏕⛺️🏞🛣🛤🌅🌄🏜🏖🏝🌇🌆🏙🌃🌉🌌🌠🎇🎆🌈🏘🏰🏯🏟🗽🏠🏡🏚🏢🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛⛪️🕌🕍🕋⌚️📱📲💻💽💾💿📀📼📷📸📹🎥📞☎️📟📠📺📻⏱⏲⏰⏳⌛️📡🔋💡🔦💸💵💴💶💷💰💳💎🔧🔨🔩🔫💣🔪🚬🏺🔮📿💈🔭🔬💊💉🔖🚽🚿🛌🚪🗿🎈🎏🎀🎁🎊🎉🎎🎐🎌🏮✉️📩📨📧💌📮📪📫📬📭📦📯📥📤📜📃📑📊📈📉📄📅📆📇📋📁📂📰📓📕📗📘📙📔📒📚📖🔗📎✂️📐📏📌📍🚩🏴🔐🔒🔓🔏✒️📝✏️🔍🔎❤️💛💙💜💔❣️💕💞💓💗💖💘💝💟📴📳⛔️📛🚫❌⭕️💢♨️🚷🚯🚳🚱🔞📵❗️❕❓❔💯🔅🔆🔱〽️⚠️🚸🔰♻️💠🌀🌐🏧🔼🔽🎵🎶️➰💱🔘⚪️⚫️🔴🔵🔸🔹🔶🔷🔺⬛️⬜️🔻◼️◻️◾️◽️🔲🔳🔈🔉🔊🔇📣📢🔔🔕👁‍🗨💭🗯💬🕺🖤🛑🛴🛵🛶🛒☝️✌️✍️❤️❣️☠♨️✈️⌛⌚☀️☁☂️❄️⛄️☄☎️✉️✏️✒️✂️♻️☕⚠️☔⏏⚡⚓⚪⚫⭐⬛⬜⛪⛲⛺⛽⛵⛴⛔⛅⛄⚽⚾️⛳⛹⛓⭕❗'
description = '''Dragon5232's loyal bot, Goldmine.
A new bot for Discord that keeps things nice and snug. 
Featuring VOICE (MUSIC), NATURAL LANGUAGE, IMAGES, CUSTOM WIDGETS, RANKS, and more!
Typically cool. Try not to expose the bugs! :P
Enjoy, and leave comments for Dragon5232 please!'''
auto_convo_starters = [
    'do', 'oh',
    'are', 'you',
    'u', 'ur',
    'ready', 'begin',
    'lets',
    'go',
    'p',
    'c',
    'h',
    'w',
    'shut',
    'watch',
    'behave',
    'test',
    'testing',
    'stop',
    'stahp',
    'ask',
    'ho',
    'um',
    'uh',
    'y',
    'tell',
    'why',
    'd',
    'g'
]
q_replies = [
    'What is the answer then.',
    'Why.',
    'Yes or no.',
    'You tell me.',
    'Erare humanum est.',
    'Hi.',
    'Hello.'
]
cnf_fmt = '{0.mention} The command you tried to execute, `{2}{1}`, does not exist. Type `{2}help` for help.'
npm_fmt = '{0.mention} Sorry, the `{2}{1}` command doesn\'t work in DMs. Try a channel.'
ccd_fmt = '{0.mention} Sorry, the `{2}{1}` command is currently disabled. Try again later!'
cpe_fmt = '{0.mention} Sorry, you don\'t have enough **permissions** to execute `{2}{1}`! You need **{3}**.'
ocpe_fmt = '{0.mention} Sorry, you don\'t have enough **permissions** to execute `{2}{1}`! **{3}** will work.'
ece_fmt = '{0.mention} Hey, we don\'t have empty commands here! Try `{2}help` instead of `{2}` for help.'
emp_msg = '{0.mention} The bot tried to send an empty message for `{2}{1}`. Maybe try again?'
msg_err = '{0.mention} Something went wrong in the bot while responding to `{2}{1}`. Maybe try again? Error: `{3}`'
nam_err = '{0.mention} Something went wrong in the bot while responding to `{2}{1}`. Maybe try again? Error: internal variable `{3}` not defined.'
big_msg = '{0.mention} Something went wrong in the bot while sending the message to respond to `{2}{1}`. This usually means the message was too long. Maybe try again?'
tim_err = '{0.mention} The bot tried to respond to `{2}{1}`, but the request took too long! Maybe try again?'
arg_err = '{0.mention} You tried to execute `{2}{1}` with{4}. Type `{2}help {1}` for extra help. Here\'s the correct usage:\n`{3}`'
ast_err = '{0.mention} You tried to execute `{2}{1}` with invalid code. Maybe try again?'
ast_pow = '{0.mention} You tried to execute `{2}{1}` with a power too high. Max is `900**900`.'
coc_fmt = '{0.mention} You\'re currently on cooldown for `{2}{1}`. Try again in **{3}**.'

charsets = {
    'normal': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'fullwidth': 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９～ ｀！＠＃＄％＾＆＊（）－＿＝＋［］｛｝|；：＇＂,＜．＞/？\\',
    'circled': 'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ0①②③④⑤⑥⑦⑧⑨~ `!@#$%^&⊛()⊖_⊜⊕[]{}⦶;:\'",⧀⨀⧁⊘?⦸',
    'circled_negative': '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩⓿123456789~ `!@#$%^&⊛()⊖_⊜⊕[]{}⦶;:\'",⧀⨀⧁⊘?⦸',
    'math_bold': '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_bold_fraktur': '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_bold_italic': '𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_bold_script': '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_double': '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_mono': '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_sans': '𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_sans_bold': '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_sans_bold_italic': '𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'math_sans_italic': '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'parenthesized': '⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵0⑴⑵⑶⑷⑸⑹⑺⑻⑼~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'regional': '🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'squared': '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉0123456789~ `!@#$%^&⧆()⊟_=⊞[]{}|;:\'",<⊡>⧄?⧅',
    'squared_negative': '🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉0123456789~ `!@#$%^&*()-_=+[]{}|;:\'",<.>/?\\',
    'upside_down': 'ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86~ ,¡@#$%^⅋*)(-‾=+][}{|;:,,,\'>˙</¿'
}

em_cells = list(emojis)
sem_cells = list(s_emojis)
_mentions_transforms = {
    '@everyone': '@\u200beveryone',
    '@here': '@\u200bhere'
}
_mention_pattern = re.compile('|'.join(_mentions_transforms.keys()))
bool_true = [
    'yes',
    'yea',
    'ya',
    'yeah',
    1,
    '1',
    'true',
    'yep',
    'yeh',
    'y',
    'ye',
    't',
    'positive',
    'certainly',
    'totally',
    'definitely',
    'on',
    'uh-huh',
    'yes.',
    'yus',
    'true',
    True
]
bool_false = [
    'no',
    'nope',
    'na',
    'nah',
    0,
    '0',
    'nop',
    'never',
    'nevah',
    'no.',
    'nopes',
    'nops',
    'nu',
    'nuu',
    'false',
    False
]

spinners = [
    "|/-\\",
    "⠂-–—–-",
    "◐◓◑◒",
    "◴◷◶◵",
    "◰◳◲◱",
    "▖▘▝▗",
    "■□▪▫",
    "▌▀▐▄",
    "▉▊▋▌▍▎▏▎▍▌▋▊▉",
    "▁▃▄▅▆▇█▇▆▅▄▃",
    "←↖↑↗→↘↓↙",
    "┤┘┴└├┌┬┐",
    "◢◣◤◥",
    ".oO°Oo.",
    ".oO@*",
    "🌍🌎🌏",
    "◡◡ ⊙⊙ ◠◠",
    "☱☲☴",
    "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏",
    "⠋⠙⠚⠞⠖⠦⠴⠲⠳⠓",
    "⠄⠆⠇⠋⠙⠸⠰⠠⠰⠸⠙⠋⠇⠆",
    "⠋⠙⠚⠒⠂⠂⠒⠲⠴⠦⠖⠒⠐⠐⠒⠓⠋",
    "⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠴⠲⠒⠂⠂⠒⠚⠙⠉⠁",
    "⠈⠉⠋⠓⠒⠐⠐⠒⠖⠦⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈",
    "⠁⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈⠈",
    "⢄⢂⢁⡁⡈⡐⡠",
    "⢹⢺⢼⣸⣇⡧⡗⡏",
    "⣾⣽⣻⢿⡿⣟⣯⣷",
    "⠁⠂⠄⡀⢀⠠⠐⠈",
    "🌑🌒🌓🌔🌕🌝🌖🌗🌘🌚"
]

home_broadcast = '''**Author\'s Website**: <https://khronodragon.com>
**Forums**: <https://forums.khronodragon.com>
**GitHub**: <https://github.com/Armored-Dragon/goldmine>
**Invite Link**: <https://tiny.cc/goldbot>
**Support Guild**: https://discord.gg/dwykTHc'''

lvl_base = 100

ch_fmt = '''Total: {0}
Text: {1}
Voice: {2}'''
absfmt = '%a %b %d, %Y %I:%M:%S %p'
status_map = {
    'online': 'Online',
    'offline': 'Offline',
    'idle': 'Idle',
    'dnd': 'Do Not Disturb'
}

quote_format = '**#{0}**: {4}"{1}"{4} \u2014 `{2}` [{3}]'
default_cogs = [
    'cogs',
    'admin',
    'cosmetic',
    'luck',
    'misc',
    'roleplay',
    'utility',
    'voice',
    'repl',
    'game_night',
    'quotes',
    'pokemon',
    'custom_commands',
    'cleverbot',
    'emoji',
    'welcome',
    'google',
    'errors',
    'ranks',
    'moderation',
    'owner',
    'help'
]
essential_cogs = [
    'cogs',
    'errors',
    'owner',
    'help'
]

join_msg = '''**Thanks for inviting me!** :heart:
My default prefix is `!`, so type `!help` to learn more about me.
People with Manage permissions can change it with `!prefix [new prefix]`.
If you ever forget my prefix, just type `prefix`.
**Enjoy, and remember that I can play music!** :stuck_out_tongue:'''
muted_perms = [
    'send_messages',
    'send_tts_messages',
    'embed_links',
    'mention_everyone',
    'manage_messages',
    'attach_files',
    'external_emojis',
    'add_reactions'
]

ev_regexps = [
    r'while\s+.+:',
    r'\s*\.\s*__[a-z]{2,}__\s*\(.*\)',
    r'^\s*__[a-z]+__\s*$',
    r'\([0-9]+\)\s*.\s*\.',
    r'lambda\s+.*:',
#    r'def\s+.+\(.*\)\s*:',
    r'range\(.+\*\*.+\)',
#    r'for\s+.+in\s+.+:',
#    r'\[.+\s+for\s+.+in\s+.+\]',
#    r'if\s+.+:',
#    r'else\s*:',
    r'{.+\s*:\s*.+\s+for\s+.+in\s+.+}',
#    r'.+\s*\*=',
    r'range\(.*[0-9.]+e[0-9.]+.*\)',
    r'range\(.*[0-9._]{7,}.*\)'
]
eval_blocked = [re.compile(r) for r in ev_regexps]

v_level_map = {
    'none': 'None 👀',
    'low': 'Low',
    'medium': 'Medium',
    'high': '(╯°□°）╯︵ ┻━┻ 😮',
    'table_flip': '(╯°□°）╯︵ ┻━┻ 😮'
}
clocks = [':clock' + c + ':' for c in [
    '1',
    '130',
    '2',
    '230',
    '3',
    '330',
    '4',
    '430',
    '5',
    '530',
    '6',
    '630',
    '7',
    '730',
    '8',
    '830',
    '9',
    '930',
    '10',
    '1030',
    '11',
    '1130',
#    '12',
#    '1230',
]]
