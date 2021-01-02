import discord
from discord.ext import commands

import datetime as dt
import pytz
import random
from os import environ
#import pendulum
import re
import io
from urllib.request import urlopen

"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""

class MusterCog(commands.Cog, name='Navy'):
    """Navy specific commands"""

    def __init__(self, bot):
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    @commands.command(name='muster', aliases = ['present', 'checkin'])
    async def muster(self, ctx):
        """Muster in the app."""
        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')
        muster_ts = dt.datetime.now(self.tz).strftime('%H:%M   %d-%b-%Y')

        #time_stamp = dt.datetime.timestamp(dt.datetime.now())
        #muster_ts = pendulum.from_timestamp(time_stamp, 'US/Eastern').strftime('%H:%M %m-%d-%Y')
        muster_channel = self.bot.get_channel(758744914862669864)
        user = ctx.message.author.mention
        await muster_channel.send('{} has mustered at  {}'.format(user, muster_ts))
        await ctx.author.send('You have been accounted for')

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()

        print(f"{ts} EST: {ctx.author} has executed '/muster'\n")
        
    
    @commands.command(name='navadmin')
    @commands.guild_only()
    @commands.has_any_role("announcements", "admin")
    async def navadmin(self, ctx, *, target_url: str=None):
        """/navadmin [url for navadmin]"""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')
 
       # Download NAVADMIN using urllib
        navadmin_b = urlopen(target_url)
        # Decode  navadmin and stream to memor
        navadmin_mem = io.StringIO(navadmin_b.read().decode('utf-8'))
        # Convert to text and save only first 500 chars
        navadmin_text = navadmin_mem.getvalue()[:500]
        
        # Regex find word NAVADMIN and rest of line
        title_find = re.search(r"\bNAVADMIN \b[A-Z0-9/ ]+" ,navadmin_text)
        # Regex find word SUBJ and rest of line
        subj_find = re.search(r"\bSUBJ/\b[A-Z0-9-/ ]+", navadmin_text)
        
        # Create embed
        embed = discord.Embed(title=title_find.group(0),  colour=discord.Colour(0x2783d8), url=target_url, description=f"```{navadmin_text}```")
        
        embed.set_author(name="U.S. Navy", url="https://www.public.navy.mil/bupers-npc/reference/messages/NAVADMINS/Pages/default.aspx", icon_url="https://cdn.glitch.com/0d022b8f-6258-470b-a559-0bf7d70c9c99%2FDON-SEAL.png?v=1601296713844")
        
        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")
        
        await ctx.send(content=subj_find.group(0) , embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()

        print(f"{ts} EST: {ctx.author} has executed '/navadmin'\n")


# The setup function below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MusterCog(bot))
