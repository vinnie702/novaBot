import discord
from discord.ext import commands
import discord.errors
from mail.mailer import send_auth_code
from models.nova_user import link_discord


class Register:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def link(self, ctx, user_id: int):
        # Generates the  code
        generated_code = send_auth_code(user_id)
        await self.bot.send_message(ctx.message.channel, 'Email sent with verification code!')
        # Waits for the code
        member = ctx.message.author
        code = await self.bot.wait_for_message(author=member, timeout=120, content=generated_code)
        # Code expired
        if code is None:
            await self.bot.send_message(member, 'You are taking too much time! Code expired. Use the command again!')
            return
        # Links the user discord in the DB
        link_discord(user_id, member.id)
        await self.bot.send_message(member, 'Your account has been successfully linked!'
                                            'Type !promote to get your rank')


# Adds these features to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Register(bot))
