import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ContextTypes, CommandHandler, CallbackQueryHandler, ConversationHandler, \
    Application
from access import API_TOKEN
from Button_Markup import *
from dataBase import get_info_from_db


# Enable logging
logging.basicConfig(filename='../bot.log',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
                    )
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define conversation states
SELECT_LANGUAGE, SELECT_TOPIC = range(2)

# Global variables to store selected language and topic
selected_language = None
selected_topic = None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send message on '/start'"""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation!", user.full_name, user.first_name)

    PythonButton = InlineKeyboardButton("Python \U0001F40D", callback_data="language_python")
    JavaButton = InlineKeyboardButton("Java \U0001F525", callback_data="language_java")
    CppButton = InlineKeyboardButton("C++ \U0001F5A5", callback_data="language_cpp")
    markup = InlineKeyboardMarkup([[PythonButton], [JavaButton], [CppButton]])
    await context.bot.send_message(chat_id=update.message.chat_id, reply_markup=markup, text='Choose Language')
    return SELECT_LANGUAGE


# Define a function to handle language selection
async def select_language(update: Update, context: CallbackContext):
    global selected_language
    selected_language = update.callback_query.data
    print(selected_language)
    """
    create sub_buttons for topics related to the selected language
    """
    logger.info("Selected language: %s", selected_language)
    topics = get_topics_for_language(selected_language)  # Define a function to retrieve topics
    buttons = [ButtonMarkup(topic, f"topic_{topic}") for topic in topics]
    print(topics)
    markup = create_button_markup([buttons])
    print(markup)
    await context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                        message_id=update.callback_query.message.chat_id, text="Choose a Topic: ",
                                        reply_markup=markup)
    return SELECT_TOPIC


async def select_topic(update: Update, context: CallbackContext):
    global selected_language, selected_topic
    selected_topic = update.callback_query.data

    # Retrieve from the database based on the selected language
    info = get_info_from_db(selected_language, selected_topic)

    if info:
        await update.callback_query.edit_message_text(f"\U00002705Info -->{info}", reply_markup=ReplyKeyboardRemove())
    else:
        await update.callback_query.edit_message_text("Information not found\U00002757",
                                                      reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def help_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    await updater.message.reply_text("Welcome to Professional Bot for Programmers! This bot is easy in work. Just tap "
                                     "on any button you want!")


if __name__ == '__main__':
    application = Application.builder().token(API_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_LANGUAGE: [CallbackQueryHandler(select_language, pattern='^language_.*')],
            SELECT_TOPIC: [CallbackQueryHandler(select_topic)], }, fallbacks=[])
    help_handler = CommandHandler('help', help_)

    application.add_handler(help_handler)
    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
