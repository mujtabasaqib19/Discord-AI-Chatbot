# Discord Gaming Bot README
This project consists of a Discord bot designed to assist with gaming-related inquiries. The bot can respond to various prompts related to games like Valorant and CS:GO, offering information, tips, and even jokes.

# Features
Responds to messages with pre-defined responses based on keywords.
Supports private and channel communications.
Customizable responses based on user inputs.
Logs all user messages for monitoring interactions.

# Prerequisites
Before you start, make sure you have the following installed:

Python 3.8 or higher
pip for Python package management

# Installation
Follow these steps to set up the bot:

# Step 2: Install Dependencies
Install the required Python libraries using pip:
pip install discord python-dotenv

# Step 3: Setup Discord Bot
Go to the Discord Developer Portal.
Create a new application and note the application ID.
Under the "Bot" tab, create a new bot and copy the token.
Invite the bot to your server using the OAuth2 URL generator with appropriate permissions.

# Step 4: Configure Environment Variables
Create a .env file in the root directory of the project and add your Discord bot token:
DISCORD_TOKEN=your_bot_token_here

# Step 5: Start the Bot
Run the bot using the following command:
python bot.py

# Usage
Once the bot is running and connected to your Discord server, it will listen to messages and respond based on the predefined intents. Users can interact with the bot in any channel where the bot has permissions to read and send messages.
