import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, \
    CallbackQueryHandler
from access import API_TOKEN
from hash_table import python_hash_table
from Button import *

# Enable logging
logging.basicConfig(filename='bot.log',
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

    python_button = MyInlineKeyBoard(
        [
            MyInlineButton("for", callbackData='for'),
            MyInlineButton("while", callbackData='while'),
            MyInlineButton("def", callbackData='def'),
            MyInlineButton("generator", callbackData='generator'),
            MyInlineButton('Numbers', callbackData='Numbers')
        ],
        [
            MyInlineButton("tuple", callbackData='tuple'),
            MyInlineButton("dictionary", callbackData='dictionary'),
            MyInlineButton("lambda", callbackData='lambda')
        ],
        [
            MyInlineButton("array", callbackData='array'),
            MyInlineButton("str", callbackData='str'),
            MyInlineButton("bool", callbackData='bool')
        ],
        [
            MyInlineButton("class", callbackData='class'),
            MyInlineButton("polymorphism", callbackData='polymorphism'),
            MyInlineButton("inheritance", callbackData='inheritance')
        ]
    )

    markup_button = python_button.get_keyboard()

    if data == 'Python':
        await query.edit_message_text(text='Python', reply_markup=markup_button)
    elif data == 'for':
        info = python_hash_table.get(data)
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'while':
        info = python_hash_table.get('while')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'def':
        info = python_hash_table.get('def')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'array':
        info = python_hash_table.get('array')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'list':
        info = python_hash_table.get('list')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'tuple':
        info = python_hash_table.get('tuple')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'generator':
        info = python_hash_table.get('generator')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'dictionary':
        info = python_hash_table.get('dictionary')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'lambda':
        info = python_hash_table.get('lambda')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'str':
        info = python_hash_table.get('str')
        info = python_hash_table.get('inheritance')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'bool':
        info = python_hash_table.get('bool')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'class':
        info = python_hash_table.get('class')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'polymorphism':
        info = python_hash_table.get('polymorphism')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'inheritance':
        info = python_hash_table.get('inheritance')
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        # await query.answer(text=info, show_alert=True)
        await query.edit_message_text(text=info, reply_markup=back_button)
    elif data == 'back':
        await query.edit_message_text(text='Python', reply_markup=markup_button)

    if data == 'Java':
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress!"
                                           f" "f"Try other commands! ", reply_markup=back_button)

    if data == 'C++':
        back = [
            [InlineKeyboardButton("back", callback_data="back")]
        ]
        back_button = InlineKeyboardMarkup(back)
        await query.edit_message_text(text=f"Selected option: {query.data},\n Sorry, but updating still in progress! "
                                           f"Try other commands! ", reply_markup=back_button)


async def help_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    await updater.message.reply_text("Hi! We have few different ways of working our bot: Use one of the follow "
                                     "command to get more information: (Without asteriks)\n "
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
                                     "* inheritance\n"
                                     "or you can use Inline Buttons! Good luck!")


async def message_(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = updater.message.text
    # print(msg)
    ans = python_hash_table.get(msg)
    if ans:
        await updater.message.reply_text(ans)  # python_hash_table.get(msg)
    else:
        await updater.message.reply_text("Oops something went wrong, try again!")


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_)
    button_handler = CallbackQueryHandler(button)

    application.add_handler(button_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.add_handler(MessageHandler(filters.TEXT, message_))

    application.run_polling()
