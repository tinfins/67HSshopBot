import discord
from discord.ext import commands
import datetime as dt
import pytz

"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class CovidCog(commands.Cog, name='COVID-19 info'):
    """COVID-19 Testing Info"""

    def __init__(self, bot):
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    @commands.command(name='covid', aliases=['covid-19', 'covid19'])
    async def covid(self, ctx):
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

        await ctx.author.send(content="**COVID-19 Information**", embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()

        print(f"{ts} EST: {ctx.author} executed '/covid'\n")


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(CovidCog(bot))
