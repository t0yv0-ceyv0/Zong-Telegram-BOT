import config
import telebot
import random  

from telebot import types

combinations = ['1 2 3 4 5 6', '1', '1 1 1', '1 1 1 1', '1 1 1 1 1', '1 1 1 1 1 1', '2 2 2', '2 2 2 2', '2 2 2 2 2', '2 2 2 2 2 2', '3 3 3', '3 3 3 3', '3 3 3 3 3', '3 3 3 3 3 3', '4 4 4', '4 4 4 4', '4 4 4 4 4', '4 4 4 4 4 4', '5', '5 5 5', '5 5 5 5', '5 5 5 5 5', '5 5 5 5 5 5', '6 6 6', '6 6 6 6', '6 6 6 6 6', '6 6 6 6 6 6']

def game_results(message, n):
    arr = []
    str_arr = ''
    
    for i in range(n):
        a = random.randrange(1, 7)
        arr.append(a)
        stik_path = 'stik\dice_' + str(a) + '.tgs'
        stik = open(stik_path, 'rb')
        bot.send_sticker(message.chat.id, stik)

    
    buffer = 'Результат раунду:' + ' '.join(map(str, arr))
    bot.send_message(message.chat.id, buffer)
    bot.send_message(message.chat.id, "Можливі комбінації: ")

    arr.sort()
    str_arr = ' '.join(map(str, arr))

    for i in combinations:
        count = 0
        pos = 0
        while str_arr.find(i, pos) != -1:
            count += 1
            
            pos = (str_arr.find(i, pos) + len(i))
        
        if count > 0:
            txt = i + " - " + str(count)

            bot.send_message(message.chat.id, txt)
            
        
        


'''
    one = arr.count(1)
    two = arr.count(2)
    three = arr.count(3)
    four = arr.count(4)
    five = arr.count(5)
    six = arr.count(6)


    if (one >= 1 and two >= 1 and three >= 1 and four >= 1 and five >= 1 and six >= 1):
        bot.send_message(message.chat.id, "1 2 3 4 5 6 - 1500 очок")
    
    if (one >= 1):
        for i in range(one):
            bot.send_message(message.chat.id, "1 - 100 очок")
        if (one == 3):
            bot.send_message(message.chat.id, "1 1 1 - 1000 очок")
        elif (one == 4):
            bot.send_message(message.chat.id, "1 1 1 1 - 2000 очок")
        elif (one == 5):
            bot.send_message(message.chat.id, "1 1 1 1 1 - 3000 очок")
        elif (one == 6):
            bot.send_message(message.chat.id, "1 1 1 1 1 1 - 4000 очок")
    
    if (two >= 3):
        if (two == 3):
            bot.send_message(message.chat.id, "2 2 2 - 200 очок")
        elif (two == 4):
            bot.send_message(message.chat.id, "2 2 2 2 - 400 очок")
        elif (two == 5):
            bot.send_message(message.chat.id, "2 2 2 2 2 - 600 очок")
        elif (two == 6):
            bot.send_message(message.chat.id, "2 2 2 2 2 2 - 800 очок")
    
    if (three >= 3):
        if (three == 3):
            bot.send_message(message.chat.id, "3 3 3 - 300 очок")
        elif (three == 4):
            bot.send_message(message.chat.id, "3 3 3 3 - 600 очок")
        elif (three == 5):
            bot.send_message(message.chat.id, "3 3 3 3 3 - 900 очок")
        elif (three == 6):
            bot.send_message(message.chat.id, "3 3 3 3 3 3 - 1200 очок")

    if (four >= 3):
        if (four == 3):
            bot.send_message(message.chat.id, "4 4 4 - 400 очок")
        elif (three == 4):
            bot.send_message(message.chat.id, "4 4 4 4 - 800 очок")
        elif (four == 5):
            bot.send_message(message.chat.id, "4 4 4 4 4 - 1200 очок")
        elif (four == 6):
            bot.send_message(message.chat.id, "4 4 4 4 4 4 - 1600 очок")

    if (five >= 1):
        for i in range(five):
            bot.send_message(message.chat.id, "5 - 50 очок")
        if (five == 3):
            bot.send_message(message.chat.id, "5 5 5 - 500 очок")
        elif (five == 4):
            bot.send_message(message.chat.id, "5 5 5 5 - 1000 очок")
        elif (five == 5):
            bot.send_message(message.chat.id, "5 5 5 5 5 - 1500 очок")
        elif (five == 6):
            bot.send_message(message.chat.id, "5 5 5 5 5 5 - 2000 очок")
    
    if (six >= 3):
        if (six == 3):
            bot.send_message(message.chat.id, "6 6 6 - 600 очок")
        elif (six == 4):
            bot.send_message(message.chat.id, "6 6 6 6 - 1200 очок")
        elif (six == 5):
            bot.send_message(message.chat.id, "6 6 6 6 6 - 1800 очок")
        elif (six == 6):
            bot.send_message(message.chat.id, "6 6 6 6 6 6 - 2400 очок")
'''



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