import discord
from discord.ext import commands
import discord.errors
import data.channels as channels


class ChannelsConfig:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def add_greeting_channel(self, ctx, channel_name: discord.Channel):
        channels.greet_channels.append(channel_name)
        await self.bot.send_message(ctx.message.channel, 'Greeting channel added!')

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def remove_greeting_channel(self, ctx, channel_name: discord.Channel):
        if channel_name not in channels.greet_channels:
            await self.bot.send_message(ctx.message.channel, 'Greeting channel not found!')
            return
        channels.greet_channels.remove(channel_name)
        await self.bot.send_message(ctx.message.channel, 'Greeting channel removed!')

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def list_greeting_channels(self, ctx):
        channels_list = 'Greeting channels:'
        for channel in channels.greet_channels:
            channels_list += '\n-' + channel.name
        await self.bot.send_message(ctx.message.channel, channels_list)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def add_info_channel(self, ctx, channel_name: discord.Channel):
        channels.info_channels.append(channel_name)
        await self.bot.send_message(ctx.message.channel, 'Info channel added!')

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def remove_info_channel(self, ctx, channel_name: discord.Channel):
        if channel_name not in channels.info_channels:
            await self.bot.send_message(ctx.message.channel, 'Greeting channel not found!')
            return
        channels.info_channels.remove(channel_name)
        await self.bot.send_message(ctx.message.channel, 'Info channel removed!')

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def list_info_channels(self, ctx):
        channels_list = 'Info channels:'
        for channel in channels.info_channels:
            channels_list += '\n-' + channel.name
        await self.bot.send_message(ctx.message.channel, channels_list)


def setup(bot: commands.Bot):
    bot.add_cog(ChannelsConfig(bot))
