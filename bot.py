import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from movies_db import MOVIES  # our simple movie database

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello! I'm your movie search bot. Just type a movie name, and I'll see if I have it in my database."
    )

# Message handler: search for a movie
def search_movie(update: Update, context: CallbackContext) -> None:
    query = update.message.text.lower().strip()
    results = []
    for key, info in MOVIES.items():
        if query in key:
            results.append(info)
    if results:
        reply_lines = []
        for movie in results:
            reply_lines.append(
                f"*{movie['title']}*\nDownload: [Link]({movie['download_link']})"
            )
        reply_text = "\n\n".join(reply_lines)
        update.message.reply_text(
            reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
    else:
        update.message.reply_text("Sorry, I couldn't find that movie.")

# Error handler
def error_handler(update: object, context: CallbackContext) -> None:
    logger.error("Update %s caused error %s", update, context.error)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # Handlers for /start command and text messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search_movie))
    dispatcher.add_error_handler(error_handler)

    # Start the bot with polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
