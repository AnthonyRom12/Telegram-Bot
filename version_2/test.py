import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, Application, \
    InlineQueryHandler, ContextTypes, CallbackQueryHandler
from Button_Markup import *
import psycopg2
from access import API_TOKEN, HOST, USER, PASSWORD, DB_NAME

# Enable logging
logging.basicConfig(filename='../bot.log',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
                    )
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Initialize your PostgreSQL connection
conn = psycopg2.connect(
    database=DB_NAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
)
cursor = conn.cursor()


# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send message on '/start'"""
    # Get user that sent /start and log his name
    user = update.effective_user
    logger.info("User %s started the conversation!", user.full_name, user.first_name)
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Hello {user.mention_html()}!\n"
             "Welcome to your bot. Please use the following commands:\n"
             "/Python - Learn Python\n"
             "/Java - Learn Java\n"
             "/Cpp - Learn C++\n"
             "/help - Show help",
        parse_mode="HTML",
    )


# Define the /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a help message. You can use /start, /Python, /Java, or /Cpp commands.")


# Define the /Python, /Java, and /Cpp command handlers
async def handle_language(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("str", callback_data='topic_str'),
         InlineKeyboardButton("Numbers", callback_data='topic_Numbers')],
        [InlineKeyboardButton("Functions", callback_data='topic_Functions'),
         InlineKeyboardButton("OOP", callback_data='topic_OOP')],
        [InlineKeyboardButton("More...", callback_data='topic_More')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #  -------------------
    context.user_data['chosen_language'] = update.message.text[1:]
    await update.message.reply_text('Choose a topic:', reply_markup=reply_markup)


# Define the callback query handler for topic buttons
async def handle_topic(update: Update, context: CallbackContext):
    query = update.callback_query
    topic = query.data.replace('topic_', '')

    chosen_language = context.user_data.get('chosen_language')
    # Retrieve information from the PostgreSQL database
    cursor.execute("SELECT explanation FROM info_table WHERE language = %s AND topic = %s", (chosen_language, topic))
    result = cursor.fetchone()

    if result:
        explanation = result[0]
        await query.answer(explanation)
    else:
        await query.answer("Topic not found.")


# Create the main function to run the bot
def main():
    application = Application.builder().token(API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help_command)
    application.add_handler(help_handler)

    python_handler = CommandHandler("Python", handle_language)
    application.add_handler(python_handler)

    java_handler = CommandHandler("Java", handle_language)
    application.add_handler(java_handler)

    cpp_handler = CommandHandler("Cpp", handle_language)
    application.add_handler(cpp_handler)

    topics_handler = CallbackQueryHandler(handle_topic)
    application.add_handler(topics_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
