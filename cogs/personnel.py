import discord
from discord.ext import commands
import discord.utils
import datetime as dt
import pytz

class PersonnelCog(commands.Cog, name='Teams Info'):
    """Team and Personnel info"""
    def __init__(self, bot):
        self.bot = bot
        self.tz = pytz.timezone('America/New_York')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            #print(f'{member.display_name} joined the server')
            await channel.send(f'{member.mention} has joined the server')
            await member.send("🎉 Welcome, {0.mention}! 🎉\n\nChange your server nickname so everyone knows who you are.\n\nPlease type ?help or /help for a list of commands provided by 67shopBot\n\nPlease go to #bots-playground and enter /join_team [team name] to join your assigned teams channel\n\nMute the channel #bots-playground to avoid notification spam.\n\nWelcome again!".format(member))

    
    @commands.command(name='join_team', aliases=['jointeam', 'setrole', 'join'])
    @commands.guild_only()
    async def set_role(self, ctx, role):
        """/join_team [team color]"""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        # Get role entered by user
        entered_role = discord.utils.get(ctx.guild.roles, name=role)
        member = ctx.author
        # Roles allowed to be self-assigned
        #team_list = ['green', 'blue', 'gold']
        team_list = {'green': 758504132603805726, 'gold': 758504113968775188, 'blue': 758504082393530368}
        # Make list of member role names
        member_roles = [role.name for role in member.roles]
        # Check if member already has role
        for r in member_roles:
            if entered_role in member.roles:
                await ctx.send(f'{member.mention} is already on team {str(role)}')
                return
            elif r in team_list.keys():
                await ctx.send(f'{member.mention} is already on a team.\nContact an administrator to be removed, then join a team.')
                return
        # Limit self-assigned roles to team_list
        if role not in team_list.keys():
            await ctx.send(f'The {str(role)} role can only be assigned by an Administrator')
        else:
            team_channel = self.bot.get_channel(team_list.get(role))
            await member.add_roles(entered_role)
            await ctx.send(f'{member.mention} has been added to team {str(role)}')
            await team_channel.send(f'{member.mention} has joined team {str(role)}')
        
        print(f"{ts} EST: {ctx.author} has execcuted '/join_team'\n")
    
    @set_role.error
    async def set_role_error(self, ctx, error):
        # do stuff
        msg = 'join_team Error: {}'.format(error)
        await ctx.send(msg)
    
    
    @commands.command(name='roles')
    @commands.has_any_role("announcements","admin")
    #@commands.guild_only()
    async def show_role(self, ctx, *, member: discord.Member=None):
        """Shows the members Roles."""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        if member is None:
            member = ctx.author
        member_roles = '\n'.join(role.name for role in member.roles)

        await ctx.send(f'The roles for {member.mention} are\n {member_roles}')
        print(f"{ts} EST: {ctx.author} has executed '/roles'\n")

    @commands.command(name='view_team', aliases=['team'])
    async def view_team(self, ctx, role):
        """Display Team members"""

        ts = dt.datetime.now(self.tz).strftime('%d-%b-%y %H:%M:%S')

        member_list = []
        entered_role = discord.utils.get(ctx.guild.roles, name=role)
        async for member in ctx.guild.fetch_members(limit=150):
            if entered_role in member.roles:
                member_list.append(member.mention)
        role_members = '\n'.join(member_list)
        if not role_members:
            await ctx.send('There are no members on this team')
        else:
            await ctx.send(f'The members of {role} are:\n{role_members}')
            print(f"{ts} EST: {ctx.author} has executed '/view_team'\n")


    @view_team.error
    async def view_team_error(self, ctx, error):
        msg = 'view_team Error: {}'.format(error)
        await ctx.send(msg)


# The setup function below. We give bot.add_cog() the name of the class, PersonnelCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(PersonnelCog(bot))
