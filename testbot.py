import telebot
from telebot import types

bot = telebot.TeleBot('2025117473:AAGyIAcJ-ta7GjLCzaYNx9EscN5JMXiZSKM')

def first(m):
    if m.text == 'О компании':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Сертификаты']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'инфа о компании',
            reply_markup=keyboard)
    elif m.text == 'Прайс-лист':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Общий', 'Одиночный']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Выберите прайс который нужен.',
            reply_markup=keyboard)
    elif m.text == 'Акции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
            reply_markup=keyboard)


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['О компании', 'Прайс-лист']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Акции', 'Контакты']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, first)





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "comproxy":
        comproxy_keyboard = types.InlineKeyboardMarkup()
        call_button_comproxy_restart = types.InlineKeyboardButton(text="Restart", callback_data="comproxy_restart")
        call_button_comproxy_status = types.InlineKeyboardButton(text="Status", callback_data="comproxy_status")
        call_button_comproxy_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_comproxy_restart, call_button_comproxy_status)
        comproxy_keyboard.add(call_button_comproxy_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите:",
                              reply_markup=comproxy_keyboard)

    elif call.data == "back":
        back_keyboard = types.InlineKeyboardMarkup()
        call_button_back_comproxy = types.InlineKeyboardButton(text="Comproxy", callback_data="comproxy")
        call_button_back_ser2net = types.InlineKeyboardButton(text="Ser2net", callback_data="ser2net")
        call_button_back_cups = types.InlineKeyboardButton(text="Cups", callback_data="cups")
        back_keyboard.add(call_button_back_comproxy, call_button_back_ser2net)
        back_keyboard.add(call_button_back_cups)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Чего изволите, господин?', reply_markup=back_keyboard)

bot.polling(none_stop=True)
