# 67HS Python Discord Bot

[![Python latest](https://img.shields.io/static/v1?label=Python&message=latest&color=blue&style=plastic&logo=Python&logoColor=ffffff)](https://www.python.org/downloads/)

[![Commits](https://img.shields.io/github/last-commit/tinfins/67HSshopBot/main?style=plastic&logo=GitHub)](https://github.com/tinfins/67HSshopBot/commits/main)

[![Open Issues](https://img.shields.io/github/issues/tinfins/67HSshopBot?style=plastic&logo=GitHub)](https://github.com/tinfins/67HSshopBot/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed/tinfins/67HSshopBot?style=plastic&logo=GitHub)](https://github.com/tinfins/67HSshopBot/issues?q=is%3Aissue+is%3Aclosed)

67HS shop bot is currently configured for one server, but the code is provided for others to use

The bot is written in Python using the discord-py-interactions and discord.py libraries. Commands are added to the bot via cogs

## For Developers
For Developers interested in using our application as a base to building their own app or for learning purposes, please see our [LICENSE](https://github.com/tinfins/discordParkingPassBot/blob/main/LICENSE).
  
## Development Environment Setup
### Pre-requisites
Python >= 3.7
### Required dependencies
-   aiohttp==3.7.4.post0
-   async-timeout==3.0.1
-   attrs==21.2.0
-   chardet==4.0.0
-   discord==1.0.1
-   discord-py-interactions==3.0.2
-   discord.py==1.7.3
-   idna==3.2
-   multidict==5.1.0
-   python-dotenv==0.15.0
-   pytz==2021.1
-   typing-extensions==3.10.0.2
-   yarl==1.6.3
  
(See requirements.txt for most up to date dependencies)
  
### Bot Credentials
Store your discord bot token in a file titled .env in the top-level project directory
  
### Environment Setup
-   Install Python 3.7.1 or higher

-   Clone github repository
    -   All Platforms: git clone https://github.com/tinfins/discordParkingPassBot.git

-   Install sqlite3
    -   sudo apt install sqlite3 libsqlite3-dev

-   Install virtualenv
    -   All platforms: pip install virtualenv

-   Create a Python virtual environment
    -   Windows: virtualenv --python C:\Path\To\Python\python.exe venv
    -   OSX/Linux: virtualenv venv

-   Activate your virtual environment
    -   Windows: .\venv\Scripts\activate
    -   OSX/Linux: source venv/bin/activate

-   Install required dependencies
    -   All Platforms: pip3 install -r requirements.txt
    -   If updating: pip install -r requirements.txt --upgrade
  
### Running
Run the bot by starting your virtual environment and use python3 app.py in the top level directory to run the bot, then invite it to your server.

Ensure the bot has permissions to send messages in your default system channel.
  
For a 24/7 online presence of your bot, creating a systemd service file (example included) or installing supervisor (sudo apt install supervisor) to manage your processes is recommended.
  
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/tinfins/discordParkingPassBot/blob/main/LICENSE) file for details.
