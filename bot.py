import sys
import traceback
import discord
import os
from discord.ext import commands


description = '''StarCitizen-Bot'''

modules = {'cogs.greeter', 'cogs.channels_config', 'cogs.cleaner', 'cogs.info', 'cogs.register', 'cogs.ranker_assigner'}

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Novablack-bot starting...')

    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='Star Citizen someday'))
    print('Loading cogs...')
    if __name__ == '__main__':
        modules_loaded = 0
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
                modules_loaded += 1
            except Exception as e:
                traceback.print_exc()
                print(f'Error loading the extension {module}', file=sys.stderr)
        print(str(modules_loaded) + '/' + str(modules.__len__()) + ' modules loaded')
        print('Systems 100%')
    print('------')


# Test bot
bot.run(os.getenv("TOKEN"))
