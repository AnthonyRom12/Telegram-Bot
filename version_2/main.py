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
             "/Python - \U0001F40DLearn Python\n"
             "/Java - \U0001F525Learn Java\n"
             "/Cpp - \U0001F5A5Learn C++\n"
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
        [InlineKeyboardButton("while", callback_data='topic_while'),
         InlineKeyboardButton("for", callback_data='topic_for')],
        [InlineKeyboardButton("function", callback_data='topic_function'),
         InlineKeyboardButton("bool", callback_data='topic_bool'),
         InlineKeyboardButton("array", callback_data='topic_array')],
        [InlineKeyboardButton("class", callback_data='topic_class'),
         InlineKeyboardButton("polymorphism", callback_data='topic_polymorphism'),
         InlineKeyboardButton("inheritance", callback_data='topic_inheritance')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #  -------------------
    chosen_topic = update.message.text[1:]
    context.user_data['chosen_topic'] = chosen_topic
    print(f"chosen_topic in handle_language: {chosen_topic}")
    await update.message.reply_text('Choose a topic:', reply_markup=reply_markup)


# Define the callback query handler for topic buttons
async def handle_topic(update: Update, context: CallbackContext):
    query = update.callback_query
    try:
        chosen_topic: str = context.user_data.get('chosen_topic')
        topic: str = query.data.replace('topic_', '')
        # chosen_language = context.user_data.get('chosen_language')
        print(f"chosen_topic in handle_topic: {chosen_topic}")
        # print(f"chosen_topic in handle_topic: {chosen_language}")
        print(f"chosen_topic in handle_topic: {topic}")

        # Retrieve information from the PostgreSQL database
        cursor.execute("SELECT explanation FROM info_table WHERE language = %s AND topic = %s", (chosen_topic, topic))
        result = cursor.fetchone()

        if result:
            explanation = result[0]
            # await query.answer(explanation)
            await query.edit_message_text(text=explanation, reply_markup=back_button(chosen_topic))
    except:
        await query.answer("Topic not found.")

# TODO: BACK BUTTON
# async def bact_to_topic_selection(update: Update, context: CallbackContext):
#     query = update.callback_query
#     chosen_language = context.user_data.get('chosen_language')
#     await query.edit_message_text(text='Choose a topic: ', reply_markup=handle_language(chosen_language))


def back_button(chosen_topic):
    keyboard = [[InlineKeyboardButton("Back\U0001F519", callback_data=f'topic_{chosen_topic}')]]
    return InlineKeyboardMarkup(keyboard)


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

    # back_handler = CallbackQueryHandler(bact_to_topic_selection)
    # application.add_handler(back_handler)

    topics_handler = CallbackQueryHandler(handle_topic)
    application.add_handler(topics_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

