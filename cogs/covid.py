"""
A cog extension for the covid info functions of the bot app
"""

import logging
import logging.config
import datetime as dt
import pytz
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class CovidCog(commands.Cog, name='COVID-19 info'):
    """COVID-19 Testing Info"""

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    @cog_ext.cog_slash(name="covid", description="COVID Information")
    async def covid(self, ctx: SlashContext):
        """COVID-19 exposure checklist."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="COVID-19 Testing Information.", 
                              colour=discord.Colour(0x1dc327), 
                              description="The Navy takes COVID-19 very seriously.\nIf you feel you may have contracted COVID-19 or are experiencing symptoms of COVID-19, please do the following;.\n")

        embed.add_field(name='☑️    TRICARE Coronavirus Testing FAQ', value='Read through the [TRICARE Coronavirus Testing FAQ](https://tricare.mil/HealthWellness/HealthyLiving/Coronavirus/Coronavirus-FAQs#testing)')
        
        embed.add_field(name='☑️    DoD COVID-19 symptoms assessment', value='Complete the [DoD COVID-19 symptoms assessment](https://mysymptoms.mil/). If you feel you require testing, contact your LPO and send a screenshot of your results from the self-assessment.')
        
        embed.add_field(name='☑️    Naval Medical Center Portsmouth (NMCP) COVID-19 hotline', value='NMCP has a 24 hour COVID-19 hotline.\n\nIf directed by your chain-of-command, call the NMCP hotline (757-953-6200), answer their questions, and follow their instructions.\n\nInform your LPO of the outcome of the phone call. ')
        
        embed.add_field(name='☑️    TRICARE Online', value='If you have taken a COVID-19 test, your results can be found through [TRICARE Online](https://www.tricareonline.com/tol2/prelogin/desktopIndex.xhtml) in 2-7 days.\n\nInform your chain of command of the result as soon as it is recieved.\n\n')
        
        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")

        self.logger.info(f"{ts} EST: {ctx.author} executed '/covid'\n")
        await ctx.send(content="**COVID-19 Information**", embed=embed, hidden=True)

    @covid.error
    async def covid_error(self, ctx: SlashContext, error):
        """
        Error catcher for covid command
        :param ctx:
        :param error:
        """
        msg = f'covid error: {error}'
        await ctx.send(msg, hidden=True)


def setup(bot):
    bot.add_cog(CovidCog(bot))
