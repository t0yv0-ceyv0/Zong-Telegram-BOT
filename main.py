import config
import telebot

from random import randrange
from telebot import types

arr = []
score = 0
curent_round_score = 0
max_score = 100
can = True
redy = True
game_end = True

combinations = {
    '1 2 3 4 5 6' : 1500, '1' : 100, '1 1 1' : 1000, '1 1 1 1' : 2000, '1 1 1 1 1' : 3000, '1 1 1 1 1 1' : 4000, 
    '2 2 2' : 200, '2 2 2 2' : 400, '2 2 2 2 2' : 600, '2 2 2 2 2 2' : 800, 
    '3 3 3' : 300, '3 3 3 3' : 600, '3 3 3 3 3' : 900, '3 3 3 3 3 3' : 1200, 
    '4 4 4' : 400, '4 4 4 4' : 800, '4 4 4 4 4' : 1200, '4 4 4 4 4 4' : 1600, 
    '5' : 50, '5 5 5' : 500, '5 5 5 5' : 1000, '5 5 5 5 5' : 1500, '5 5 5 5 5 5' : 2000, 
    '6 6 6' : 600, '6 6 6 6' : 1200, '6 6 6 6 6' : 1800, '6 6 6 6 6 6' : 2400}

def round_random(n):

    arr.clear()
    for i in range(n):
        arr.append(randrange(1,7))
    
    txt = 'Результат раунду:' + ' '.join(map(str, arr)) + "\n Поточна кількість очків:" + str(curent_round_score) + "\n Можливі комбінації: "
    
    return txt

def check_combinations(bool):
    inline_keyboard_arr = []
    result_markup = types.InlineKeyboardMarkup(row_width=2)
    arr.sort()
    str_arr = ' '.join(map(str, arr))

    for i in combinations:
        global curent_round_score
        count = 0
        pos = 0
        while str_arr.find(i, pos) != -1:
            count += 1

            pos = (str_arr.find(i, pos) + len(i))
        
        if count > 0:
            for j in range(count):
                txt = i + " - " + str(combinations[i])
                item = types.InlineKeyboardButton(txt, callback_data=i)
                inline_keyboard_arr.append(item)
    for i in inline_keyboard_arr:
            result_markup.add(i)
    
    if bool:
        return result_markup
    else:
        if len(inline_keyboard_arr) == 0:
            curent_round_score = 0
            global can
            can = False
        return result_markup

def send_message(message, txt, result_markup):
    bot.send_message(message.chat.id, txt, reply_markup=result_markup)

def send_stikers(message):

    for i in arr:
        stik = open('stik\dice_' + str(i) + '.tgs', 'rb')
        bot.send_sticker(message.chat.id, stik)

bot=telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("Нова гра")
  item2 = types.KeyboardButton("Наступне підкидання")
  item3 = types.KeyboardButton("Продовжити раунд")
  item4 = types.KeyboardButton("Преглянути кількість очків")
  markup.add(item1, item2, item3, item4)

  bot.send_message(message.chat.id, config.Greeting, reply_markup=markup)
  
@bot.message_handler(content_types=['text'])
def check_text(message):

    global game_end, can, redy, score, curent_round_score

    txt = ''

    if message.chat.type == 'private':

        if message.text == 'Преглянути кількість очків':
            send_message(message, "Кількість очок до перемоги: " + str(max_score) + "\n Ваша кількість очок: " + str(score), None)

        if message.text == 'Нова гра' and game_end:
            game_end = False
            can = True
            score = 0
            curent_round_score = 0
            txt = round_random(6)

            send_stikers(message)
            send_message(message, txt, check_combinations(False))
        
        if message.text == 'Наступне підкидання':
            score = score + curent_round_score
            curent_round_score = 0

            if max_score > score:
                can = True
                txt = round_random(6)
                send_stikers(message)
                send_message(message, txt, check_combinations(False))


            else:
                send_message(message, "Ви набрали потрібну кількість очків \n Ваша кількість очків: " + str(score), None )
                game_end = True
                can = True
                score = 0
                curent_round_score = 0

        if message.text == 'Продовжити раунд':
            
            if len(arr) > 0 and can and redy:
                redy = False
                txt = round_random(len(arr))
                send_stikers(message)
                send_message(message, txt, check_combinations(False))

            elif len(arr) == 0:
                send_message(message, 'Більше не залишилось кубиків' + str(score), None )

            else:
                send_message(message, 'Ви не обрали жодної комбінації' + str(score), None )                     

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data in combinations:

                global redy, curent_round_score

                redy = True
                curent_round_score = curent_round_score + combinations[call.data]
                x = list(map(int, call.data.split()))

                for i in x:
                    arr.remove(i)

                result_markup = check_combinations(True)

                buffer = 'Результат раунду:' + ' '.join(map(str, arr)) + "\n Поточна кількість очків:" + str(curent_round_score) + "\n Можливі комбінації: "

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=buffer, reply_markup=result_markup)

    except Exception as e:
        print(repr(e))

bot.infinity_polling()