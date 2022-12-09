import config
import telebot
import random  

from telebot import types

def game_results(message, n):
    str_arr = 'Результат раунду: '
    for i in range(n):
        a = str(random.randrange(1, 7))
        arr = arr + a + ' '
        stik_path = 'stik\dice_' + a + '.tgs'
        stik = open(stik_path, 'rb')
        bot.send_sticker(message.chat.id, stik)
    bot.send_message(message.chat.id, arr)

bot=telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("Почати")
  item2 = types.KeyboardButton("Допомога")
  markup.add(item1, item2)

  bot.send_message(message.chat.id, config.Greeting, reply_markup=markup)
  

@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.chat.type == 'private':
        if message.text == 'Почати':
            game_results(message, 6)


bot.infinity_polling()