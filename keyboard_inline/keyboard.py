from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_game():
    keyboard_1 = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('Начать историю', callback_data='start_story')
    keyboard_1.add(button_1)
    return keyboard_1

def scene_1():
    keyboard_2 = InlineKeyboardMarkup(row_width=1)
    next_scen_1 = InlineKeyboardButton('Продолжить историю', callback_data='continue_scene_1')
    keyboard_2.add(next_scen_1)
    return keyboard_2

def scene_2():
    keyboard_3 = InlineKeyboardMarkup(row_width=1)
    next_scen_2 = InlineKeyboardButton('Продолжить историю', callback_data='continue_scene_2')
    keyboard_3.add(next_scen_2)
    return keyboard_3



