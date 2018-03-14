import discord
from discord.ext import commands
import discord.errors
from models.nova_user import get_nova_user
from utils.html_cleaner import clean_html


class Info:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def bio(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        # Gets the nova DB user
        nova_user = get_nova_user(user.id)
        if nova_user is None:
            await self.bot.send_message(ctx.message.channel, 'User not found! Maybe the account is not linked yet.')
            return
        # Creates the embed
        embed = discord.Embed(title=nova_user.handle, description=clean_html(nova_user.short_bio), color=0xBA55D3)
        if nova_user.img is None or nova_user.img == '':
            # Default img
            embed.set_image(url='https://i.imgur.com/GhsS0cq.jpg')
        else:
            embed.set_image(url='http://www.novabl4ck.org' + nova_user.img)
        embed.add_field(name='Rank', value=nova_user.rank)
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
        if nova_user.position is not None:
            embed.add_field(name='Position', value=nova_user.position)
        await self.bot.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    async def ships(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.message.author

        nova_user = get_nova_user(user.id)
        nova_user.get_owned_ships()

        output = '▮▯Ships▮▯\n'
        output += '▮▯'*10 + '\n'
        for ship in nova_user.ships:
            output += '▮▯ **{}**   N: {}   Crew: {}\n'.format(ship['data'].nickname, str(ship['quantity']), str(ship['data'].crewsize))
        await self.bot.say(output)


# Adds these features to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
