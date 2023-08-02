import logging
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler
from access import API_TOKEN
from hash_table import python_hash_table


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send message on '/start'"""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation!", user.full_name, user.first_name)

    keyboard = [
        [
            InlineKeyboardButton("Python", callback_data='Python', ),
            InlineKeyboardButton("Java", callback_data='Java'),
        ],
        [InlineKeyboardButton("C++", callback_data='C++')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.message.chat_id, reply_markup=reply_markup, text='Choose Language')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    if query.data == 'Python':
        pyth0n_button = [
            [InlineKeyboardButton("for", callback_data='for'),
             InlineKeyboardButton("while", callback_data='2'),
             InlineKeyboardButton("def", callback_data='3'),
             InlineKeyboardButton("generator", callback_data='4'),
             InlineKeyboardButton("Numbers", callback_data='5')],
            [InlineKeyboardButton("tuple", callback_data='6'),
             InlineKeyboardButton("dictionary", callback_data='7'),
             InlineKeyboardButton("lamda", callback_data='8')],
            [InlineKeyboardButton("array", callback_data='9'),
             InlineKeyboardButton("str", callback_data='10'),
             InlineKeyboardButton("bool", callback_data='11')],
        ]

        markup_button = InlineKeyboardMarkup(pyth0n_button)
        await query.edit_message_text(text='Python', reply_markup=markup_button)

        # await query.edit_message_text(text=f"Selected option: {query.data},\n Use follow command to get more"
        #                                    f"information: (Without asteriks)\n "
        #                                    "* for\n"
        #                                    "* for_statement_example\n"
        #                                    "* while\n"
        #                                    "* while_example\n"
        #                                    "* tuple\n"
        #                                    "* def\n"
        #                                    "* list\n"
        #                                    "* array\n"
        #                                    "* generator\n"
        #                                    "* dictionary\n"
        #                                    "* lambda\n"
        #                                    "* Numbers\n"
        #                                    "* str\n"
        #                                    "* bool")
    if query.data == 'Java':
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress!"
                                           f" "f"Try other commands! ")

    if query.data == 'C++':
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress! "
                                           f"Try other commands! ")


async def help_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    await updater.message.reply_text("Use follow command to get more information: (Without asteriks)\n"
                                     "* for\n"
                                     "* for_statement_example\n"
                                     "* while\n"
                                     "* while_example\n"
                                     "* tuple\n"
                                     "* def\n"
                                     "* list\n"
                                     "* array\n"
                                     "* generator\n"
                                     "* dictionary\n"
                                     "* lambda\n"
                                     "* Numbers\n"
                                     "* str\n"
                                     "* bool")


async def message_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = updater.message.text
    # print(msg)
    ans = python_hash_table.get(msg)
    if ans:
        await updater.message.reply_text(ans)  # python_hash_table.get(msg)
    else:
        await updater.message.reply_text("Oops something went wrong, try again!")


# Echo functions for creating echo bot
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_)
    button_handler = CallbackQueryHandler(button)

    application.add_handler(button_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    # application.add_handler(echo_handler)
    application.add_handler(MessageHandler(filters.TEXT, message_))

    application.run_polling()
