# Movie Search Bot

A simple Telegram bot that allows users to search for movies in a group. When a user sends a movie name, the bot checks a simple database and replies with the title and a download link.

## How It Works

1. User sends a message with a movie name.
2. The bot searches its database (a Python dictionary in `movies_db.py`).
3. If a match is found, the bot sends back the movie title and download link.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create your bot with BotFather and update the token in `bot.py`.
4. Run the bot: `python bot.py`

## License

MIT License
