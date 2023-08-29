# TODO: OOP Button
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class MyInlineButton:
    def __init__(self, text, callbackData):
        self.text = text
        self.callbackData = callbackData

    def get_button(self):
        return InlineKeyboardButton(self.text, callback_data=self.callbackData)


class MyInlineKeyBoard:
    def __init__(self, *button_rows):
        self.button_rows = button_rows

    def get_keyboard(self):
        keyboard = []
        for row in self.button_rows:
            buttons = []
            for button in row:
                buttons.append(button.get_button())
            keyboard.append(buttons)
        return InlineKeyboardMarkup(keyboard)

