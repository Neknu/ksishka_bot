import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ксюшка ❤")
    item2 = types.KeyboardButton("Давай пошалим?😏")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Привет, {0.username}!\nЯ - <b>{1.username}</b>, бот, которого сделал Даня для Ксюшки".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Ксюшка ❤':
            sti = open('static/rabbit.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'В моем сердечке❣')
        elif message.text == 'Давай пошалим?😏':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Дыыыыыы", callback_data='yes')
            item2 = types.InlineKeyboardButton("Не так быстро, молодой, но вживую задам тебе жару🔥", callback_data='fire')

            markup.add(item1, item2)

            sti = open('static/mur_mur.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Конечно давай🧡', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Нинаю, что на такое ответить, но Ксюшка - топ❤❤❤')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'АРРРР😍😍😍')
                sti = open('static/archer.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
            elif call.data == 'fire':
                bot.send_message(call.message.chat.id, 'Жду не дождусь😍')
                sti = open('static/kus.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)
