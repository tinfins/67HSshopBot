"""
A cog extension for the personnel functions of the bot app
"""

import logging
import logging.config
import datetime as dt
import pytz
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_components import (
    create_select,
    create_select_option,
    create_actionrow,
    wait_for_component
)
import random
from os import environ
# import pendulum
import re
import io
from urllib.request import urlopen


class PersonnelCog(commands.Cog, name='Personnel'):
    """Personnel specific commands"""

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    @cog_ext.cog_slash(name="muster", description="Muster Electronically")
    async def muster(self, ctx: SlashContext):
        """
        /muster - Muster electronically.
        """
        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')
        muster_ts = dt.datetime.now(self.tz).strftime('%H:%M   %d-%b-%Y')

        """
        Change for Main Server
        """
        #muster_channel = self.bot.get_channel(758744914862669864)
        muster_channel = self.bot.get_channel(817437296353345576)
        author = ctx.author.name
        user = ctx.author.mention
        # await muster_channel.send('{} has mustered at  {}'.format(user, muster_ts))
        self.logger.info(f"{ts} EST: {ctx.author} has executed '/muster'\n")
        await muster_channel.send(f'{user} has mustered at {muster_ts}')
        await ctx.send('You have been accounted for', hidden=True)

    @muster.error
    async def muster_error(self, ctx: SlashContext, error):
        """
        Error catcher for muster command
        :param ctx:
        :param error:
        """
        msg = f'muster error: {error}'
        await ctx.send(msg, hidden=True)

    @cog_ext.cog_slash(name="navadmin", description="Link to NavAdmin Msgs")
    @commands.guild_only()
    @commands.has_any_role("announcements", "supervisors", "admin")
    async def navadmin(self, ctx: SlashContext, target_url: str):
        """
        /navadmin [url for navadmin] - NavAdmin embedded message
        :param:target_url: URL for NAVADMIN txt file (ex. https://www.mynavyhr.navy.mil/Portals/55/Messages/NAVADMIN/NAV2021/NAV21287.txt?ver=BuTcMwKS54Yyqswt9DMXuw%3d%3d)
        """
        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        # Download NAVADMIN using urllib
        navadmin_b = urlopen(target_url)
        # Decode  navadmin and stream to memory
        navadmin_mem = io.StringIO(navadmin_b.read().decode('utf-8'))
        # Convert to text and save only first 500 chars
        navadmin_text = navadmin_mem.getvalue()[:500]

        # Regex find word NAVADMIN and rest of line
        title_find = re.search(r"\bNAVADMIN \b[A-Z0-9/ ]+", navadmin_text)
        # Regex find word SUBJ and rest of line
        subj_find = re.search(r"\bSUBJ/\b[A-Z0-9-/ ]+", navadmin_text)

        # Create embed
        embed = discord.Embed(title=title_find.group(0), colour=discord.Colour(0x2783d8), url=target_url,
                              description=f"```{navadmin_text}```")

        embed.set_author(name="U.S. Navy",
                         url="https://www.public.navy.mil/bupers-npc/reference/messages/NAVADMINS/Pages/default.aspx",
                         icon_url="https://cdn.glitch.com/0d022b8f-6258-470b-a559-0bf7d70c9c99%2FDON-SEAL.png?v=1601296713844")

        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/",
                         icon_url="http://i.imgur.com/5BFecvA.png")

        self.logger.info(f"{ts} EST: {ctx.author} has executed '/navadmin'\n")
        return await ctx.send(content=subj_find.group(0), embed=embed)

    @navadmin.error
    async def navadmin_error(self, ctx: SlashContext, error):
        """
        Error catcher for navadmin command
        :param ctx:
        :param error:
        """
        msg = f'navadmin error: {error}'
        await ctx.send(msg, hidden=True)


def setup(bot):
    """
    Adds cog to bot
    """
    bot.add_cog(PersonnelCog(bot))
