import logging
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler
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


async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    # await query.answer()
    if data == 'Python':
        python_button = [
            [InlineKeyboardButton("for", callback_data='for'),
             InlineKeyboardButton("while", callback_data='while'),
             InlineKeyboardButton("def", callback_data='def'),
             InlineKeyboardButton("generator", callback_data='generator'),
             InlineKeyboardButton("Numbers", callback_data='Numbers')],
            [InlineKeyboardButton("tuple", callback_data='tuple'),
             InlineKeyboardButton("dictionary", callback_data='dictionary'),
             InlineKeyboardButton("lambda", callback_data='lambda')],
            [InlineKeyboardButton("array", callback_data='array'),
             InlineKeyboardButton("str", callback_data='str'),
             InlineKeyboardButton("bool", callback_data='bool')],
            [InlineKeyboardButton("class", callback_data='class'),
             InlineKeyboardButton("polymorphism", callback_data='polymorphism'),
             InlineKeyboardButton("inheritance", callback_data='inheritance')]
        ]

        markup_button = InlineKeyboardMarkup(python_button)
        await query.edit_message_text(text='Python', reply_markup=markup_button)

    elif data == 'for':  # TODO: message too long
        info = python_hash_table.get(data)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info)
    elif data == 'while':
        info = python_hash_table.get('while')
        await query.answer(text=info, show_alert=True)
    elif data == 'def':
        info = python_hash_table.get('def')
        await query.answer(text=info, show_alert=True)
    elif data == 'array':
        info = python_hash_table.get('array')
        await query.answer(text=info, show_alert=True)
    elif data == 'list':
        info = python_hash_table.get('list')
        await query.answer(text=info, show_alert=True)
    elif data == 'tuple':  # TODO: message too long
        info = python_hash_table.get('tuple')
        await query.answer(text=info, show_alert=True)
    elif data == 'generator':
        info = python_hash_table.get('generator')
        await query.answer(text=info, show_alert=True)
    elif data == 'dictionary':  # TODO: message too long
        info = python_hash_table.get('dictionary')
        await query.answer(text=info, show_alert=True)
    elif data == 'lambda':
        info = python_hash_table.get('lambda')
        await query.answer(text=info, show_alert=True)
    elif data == 'str':
        info = python_hash_table.get('str')
        await query.answer(text=info, show_alert=True)
    elif data == 'bool':  # TODO: message too long
        info = python_hash_table.get('bool')
        await query.answer(text=info, show_alert=True)
    elif data == 'class':  # TODO: message too long
        info = python_hash_table.get('class')
        await query.answer(text=info, show_alert=True)
    elif data == 'polymorphism':
        info = python_hash_table.get('polymorphism')
        await query.answer(text=info, show_alert=True)
    elif data == 'inheritance':  # TODO: message too long
        info = python_hash_table.get('inheritance')
        await query.answer(text=info, show_alert=True)

    if data == 'Java':
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress!"
                                           f" "f"Try other commands! ")

    if data == 'C++':
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress! "
                                           f"Try other commands! ")


async def help_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    await updater.message.reply_text("Hi, Use one of the follow command to get more information: (Without asteriks)\n"
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
                                     "* bool\n"
                                     "* class\n"
                                     "* polymorphism\n"
                                     "* inheritance")


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
