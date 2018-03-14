import discord
from discord.ext import commands
import discord.errors
import data.channels as channels


class Greeter:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # This function is called when a member joins.
    async def on_member_join(self, member: discord.Member):
        # Greets the user in every greeting channel.
        server = self.bot.get_server('378653187336568834')
        recruitment_team = discord.utils.get(server.roles, name='recruitmentteam')
        for channel in channels.greet_channels:
            await self.bot.send_message(channel, 'Welcome {} to the Nova Black Discord Server! A member of our {}'
                                                 ' will be with you shortly to help you with any questions you'
                                                 'may have!!'.format(member.mention, recruitment_team.mention))
        await self.bot.send_message(member, 'Welcome to our discord server!\nIf you have already joined our website and want to be assigned your current rank as a role in discord, you need to'
                                            'link your discord account with the NovaBlack website account.')
        await self.bot.send_message(member, 'http://www.novabl4ck.org')
        await self.bot.send_message(member, 'Don\'t have an account? Register now! We are waiting for you :)\n'
                                            'Once your account is created and approved, go to **Admin** >''**Profile**\n'
                                            'There you can see your id, now write here **bot_link \'yourid\'** '
                                            'and check your email.')

    # This function is called when a member leaves.
    async def on_member_remove(self, member):
        # Notifies a user just left the server.
        for channel in channels.greet_channels:
            await self.bot.send_message(channel, 'Later homie! Come back soon :middlefinger: ... quitter.')


# Adds these features to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Greeter(bot))
