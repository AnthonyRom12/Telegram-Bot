import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ContextTypes, CommandHandler, CallbackQueryHandler, ConversationHandler, \
    Application
from access import API_TOKEN
from Button_Markup import *
from dataBase import get_info_from_db
from topis import get_topics_for_language


# Enable logging
logging.basicConfig(
    filename='../bot.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# Global variables to store selected language and topic
SELECT_LANGUAGE = 1
SELECT_TOPIC = 2
selected_language = None
selected_topic = None

# Your ButtonMarkup, get_topics_for_language, and get_info_from_db functions here

async def start(update: Update, context: CallbackContext):
    """Send message on '/start'"""
    user = update.message.from_user
    logger.info("User %s started the conversation!", user.full_name, user.first_name)

    PythonButton, JavaButton, CppButton = ButtonMarkup("Python \U0001F40D"), ButtonMarkup(
        "Java \U0001F525"), ButtonMarkup("C++ \U0001F5A5")
    markup = create_button_markup([PythonButton, JavaButton, CppButton])

    await context.bot.send_message(chat_id=update.message.chat_id, reply_markup=markup, text='Choose Language')
    return SELECT_LANGUAGE

async def select_language(update: Update, context: CallbackContext):
    global selected_language
    selected_language = update.callback_query.data
    logger.info("Selected language: %s", selected_language)

    topics = get_topics_for_language(selected_language)
    buttons = [ButtonMarkup(topic) for topic in topics]
    markup = create_button_markup(buttons)
    await update.callback_query.edit_message_text("Choose a Topic: ", reply_markup=markup)
    return SELECT_TOPIC

async def select_topic(update: Update, context: CallbackContext):
    global selected_language, selected_topic
    selected_topic = update.callback_query.data

    info = get_info_from_db(selected_language, selected_topic)

    if info:
        await update.callback_query.edit_message_text(f"\U00002705Info -->{info}", reply_markup=ReplyKeyboardRemove())
    else:
        await update.callback_query.edit_message_text("Information not found\U00002757",
                                                      reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

if __name__ == '__main__':
    application = Application.builder().token(API_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_LANGUAGE: [CallbackQueryHandler(select_language, pattern='^language_.*')],
            SELECT_TOPIC: [CallbackQueryHandler(select_topic)],
        },
        fallbacks=[]
    )
    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
