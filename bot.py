import os
from discord.ext import commands
from pathlib import Path


class BotO(commands.Bot):
    # noinspection PyMethodMayBeStatic
    async def on_ready(self):
        print('Bot is ready!')


bot = BotO(command_prefix='/')
bot.load_extension('cogs.test')

# Run Bot
bot_token = os.environ.get('DISCORD_TOKEN')
bot.run(bot_token)
