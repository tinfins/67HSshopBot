import logging
import logging.config
import datetime as dt
import pytz
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class KnowledgeBase(commands.Cog, name='Knowledge Base'):
    """Shop Knowledge Base"""

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    '''
    @commands.command(name='intro', aliases=['introduction', 'info'])
    async def intro(self, ctx):
        """Shop 67HS Information."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="Welcome to shop 67HS.", 
                              colour=discord.Colour(0x1dc327), 
                              description="We conduct scheduled and emergent repairs all masts and antennas on submarines.\nWe are the highest production shop at NNSY FMB.\nThis is an I-level maintenance facility and a fast-paced environment.\n")

        embed.set_image(url="https://cdn.glitch.com/0d022b8f-6258-470b-a559-0bf7d70c9c99%2Fsemper_gumby.png?v=1601089383124")
        embed.add_field(name='Semper Gumby', value='Semper Flexibilis')
        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")

        await ctx.author.send(content="**Shop 67HS Introduction**", embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()
        # Log entry for command execution
        print(f"{ts} EST: {ctx.author} executed '/intro'\n")


    @commands.command(name='schedule', aliases=['sked', 'daily'])
    async def schedule(self, ctx):
        """Shop 67HS daily schedule."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="Schedule for 67HS.", colour=discord.Colour(0x1dc327), description="The daily schedule is always subject to change based on work, training, and discretion of your supervisor.")

        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")

        embed.add_field(name="Daily Schedule", value="------------------")
        embed.add_field(name="0730", value="   - Muster on Station.\n   - Morning Quarters.\n   - Shop PT")
        embed.add_field(name="0930", value="   - Muster after Shop PT.\n   - Quarters.\n   - Clean Up (Field Days on Friday).\n   - Go to Work.\n\n\n")

        await ctx.author.send(content="**Shop 67HS Daily Schedule**", embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()
        # Log entry for command execution
        print(f"{ts} EST: {ctx.author} executed '/schedule'\n")


    @commands.command(name='appt', aliases=['appointments', 'mustering'])
    async def appts(self, ctx):
        """Appointments."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="Appointments and Remote Mustering.", colour=discord.Colour(0x1dc327), description="Inform your supervisor or LPO of your appointment. \nEnter all of your appointments in the Calendar on the admin desk.\nIf you will not be present for morning muster, you will muster by phone, text message, or in this app. \n\nThe image below demonstrates how to use this app to muster.")

        embed.set_image(url="https://cdn.glitch.com/0d022b8f-6258-470b-a559-0bf7d70c9c99%2Fmuster_tutorial.gif?v=1601092655128")
        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")

        await ctx.author.send(content="**Shop 67HS Appointments**", embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()
        # Log entry for command execution
        print(f"{ts} EST: {ctx.author} executed '/appt'\n")


    @commands.command(name='quals', aliases=['qualifications', 'watch'])
    async def quals(self, ctx):
        """Qualifications Information."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="Qualifications and Watchstanding.", colour=discord.Colour(0x1dc327), description="While at NNSY FMB, you will qualify at least one watch station in your first two months on board.")

        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/", icon_url="http://i.imgur.com/5BFecvA.png")

        embed.add_field(name="Qualifications", value="-------------------")
        embed.add_field(name="DPO (Duty Petty Officer)", value="E-5 are required to qualify. E-4 and below are highly encouraged to qualify.\n\nThis watch is stood at the NNSY Duty Office.")
        embed.add_field(name="PDO (Production Duty Officer)", value="E-5 and above may qualify this watch if recommended by the command.\n\nThis watch is stood on Norfolk Naval Base at FMB.")
        embed.add_field(name="IRP (Installation Roving Patrol)", value="E-6 and above are required to qualify.\n\nThis watch is stood at NNSY as a Roving Watch.")
        embed.add_field(name="SDO (Shipyard Duty Officer)", value="E-6 and above may qualify this watch. E-5 who have qualified DPO may qualify this watch.\n\nThis watch is stood at the NNSY Duty Office.\n\n")

        await ctx.author.send(content="**Shop 67HS Qualifications**", embed=embed)

        if not isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.delete()
        # Log entry for command execution
        print(f"{ts} EST: {ctx.author} executed '/quals'\n")
    '''

    @cog_ext.cog_slash(name="college", description="College Information")
    async def college(self, ctx: SlashContext):
        """College/TA Information."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        embed = discord.Embed(title="College and Tuition Assistance.", colour=discord.Colour(0x29afba),
                              description="Higher education and use of Tuition Assistance is highly encouraged at NNSY. \n\nThe [collegeSmart](https://collegesmart.herokuapp.com/) is a good starting point to gain eligibility to use TA and help you select a college that is right for you.\n\nThe site is informational only and has no affiliation with the U.S. Navy or Department of Defense.")

        embed.set_image(
            url="https://cdn.glitch.com/0d022b8f-6258-470b-a559-0bf7d70c9c99%2FCS_logo_wht_stacked.png?v=1601094460835")
        embed.set_footer(text="Made in Python with discord.py@rewrite | https://github.com/tinfins/",
                         icon_url="http://i.imgur.com/5BFecvA.png")
        self.logger.info(f"{ts} EST: {ctx.author} executed '/college'\n")
        return await ctx.send(content="College and Tuition Assistance", embed=embed, hidden=True)

    @college.error
    async def college_error(self, ctx: SlashContext, error):
        """
        Error catcher for college command
        :param ctx:
        :param error:
        """
        msg = f'college error: {error}'
        await ctx.send(msg, hidden=True)


def setup(bot):
    bot.add_cog(KnowledgeBase(bot))
