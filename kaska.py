import telebot
from telebot import types

api = '1937537260:AAGTXrgwd5_V7hbds3f9NBOqYgMJmdReMSc'

greetings = """Добрый день!
Вы находитесь чат-боте Kaska.
Нажмите на нужную кнопку снизу"""

answers = '''1.Сколько стоит вызов замерщика?
    Это бесплатная услуга
2.У вашей компании есть реквизиты, счет фактуры?
    Да, подробнее об этом вы можете узнать в разделе «Документы». 
3.Мщжет ли заказчик сам предоставить материалы?
    Конечно. Об этом нужно будет сказать замерщику или нашему менеджеру по телефону до начала составления договора
4.Сколько времени длится заказ?
    Это зависит от типа работ и размера площади.'''

bot = telebot.TeleBot(api)

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='http://kaska.kg/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    kbrd = types.InlineKeyboardMarkup()
    kbrd1 = types.InlineKeyboardButton(text='Наши услуги', callback_data='service')
    kbrd2 = types.InlineKeyboardButton(text='Контакты', callback_data='contact')
    kbrd3 = types.InlineKeyboardButton(text='Отзывы наших клиентов', callback_data='client')
    kbrd4 = types.InlineKeyboardButton(text='Наши работы', callback_data='work')
    kbrd5 = types.InlineKeyboardButton(text='Самые важные вопросы и ответы на них', callback_data='ansque')
    kbrd.add(kbrd1, kbrd2, kbrd3, kbrd4, kbrd5)
    bot.send_message(message.chat.id, greetings, reply_markup=kbrd)


@bot.callback_query_handler(func=lambda ans: True)
def ans(call):
    if call.data == 'service':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reklama = types.KeyboardButton('Наружная реклама')
        svarochnye = types.KeyboardButton('Сварочные работы')
        mebel = types.KeyboardButton('Мебель под заказ')
        reshetki = types.KeyboardButton('Декоративные решетки')
        home = types.KeyboardButton('Назад')
        markup_reply.add(reklama, svarochnye, mebel, reshetki, home)
        bot.send_message(call.message.chat.id, 'Нажмите на нужную кнопку снизу', reply_markup=markup_reply)
    elif call.data == 'contact':
        bot.send_message(call.message.chat.id, text='Номера обслуживания: +996700441644\n +996706121122\n'
            'Наш сайт: http://kaska.kg/\n'
            'Эл. почта: kaskakg18@gmail.com')
    elif call.data == 'work':
        bot.send_photo(chat_id=call.message.chat.id, photo='http://kaska.kg/static/media/img1.013049d7.jpg')
        bot.send_photo(call.message.chat.id, photo='http://kaska.kg/static/media/img8.526f3e93.jpg')
        bot.send_message(call.message.chat.id, 'Примеры выполненных работ, которыми гордится наша команда')
    elif call.data == 'ansque':
        bot.send_message(call.message.chat.id, answers)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'наружная реклама':
        bot.send_photo(message.chat.id, photo='http://inoutprint.ru/wp-content/uploads/konstruktsii-naruzhnoy-reklamy.jpg')
    elif message.text.lower() == 'сварочные работы':
        bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDXJIA0RCrnvSlbaOD9OcdIss2To7cWqJiTw&usqp=CAU')
    elif message.text.lower() == 'мебель под заказ':
        bot.send_photo(message.chat.id, photo='http://kaska.kg/static/media/img7.581b11bf.jpg')
    elif message.text.lower() == 'декоративные решетки':
        bot.send_photo(message.chat.id, photo='http://kaska.kg/static/media/img8.526f3e93.jpg')
    elif message.text.lower() == 'назад':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Я Вас не понимаю, может Вам поможет /start')


@bot.message_handler(content_types=['text'])
def go_txt(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Здраствуйте!')

bot.polling(none_stop=True, interval=0)
