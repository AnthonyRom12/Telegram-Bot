from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class ButtonMarkup:
    def __init__(self, button_text, callback_data):
        self.button = InlineKeyboardButton(button_text, callback_data)

    def get_button(self):
        return self.button


def create_button_markup(buttons):
    """
    Create a ReplyKeyboardMarkup from a list of ButtonMarkup objects.

    Args:
        buttons (list): List of ButtonMarkup objects.

    Returns:
        ReplyKeyboardMarkup: Keyboard markup containing the buttons.
    """
    keyboard = [[button.get_button()] for button in buttons]
    return InlineKeyboardMarkup(keyboard)



