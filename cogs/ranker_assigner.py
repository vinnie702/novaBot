import discord
from discord.ext import commands
import discord.errors
from models.nova_user import get_nova_user
from data.server import server_id


class Ranker:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # This function is called when a member joins.
    async def on_member_join(self, member: discord.Member):
        # Assigns the New Recruit member to new users.
        server = self.bot.get_server(server_id)
        new_recruit_role = discord.utils.get(server.roles, name='New Recruit')
        recruitment_team = discord.utils.get(server.roles, name='Recruitment Team')
        await self.bot.add_roles(member, new_recruit_role)

    @commands.command(pass_context=True)
    async def promote(self, ctx):
        server = self.bot.get_server(server_id)
        discord_member : discord.Member = ctx.message.author
        user = get_nova_user(discord_member.id)
        if user is None:
            await self.bot.say('You need to link your account first! If you have doubts, ask {}'.format(recruitment_team.mention)
            return
        user_role = discord.utils.get(server.roles, name=user.rank)
        if user_role in discord_member.roles:
            await self.bot.say('You already have your highest rank!')
            return
        await self.bot.add_roles(discord_member, user_role)
        await self.bot.say('{} \'s rank has been updated!'.format(discord_member.display_name))


# Adds these features to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Ranker(bot))
