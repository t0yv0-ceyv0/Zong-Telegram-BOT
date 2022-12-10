import config
import telebot
import random  

from telebot import types

buffer = ''
score = 0
arr = []
curent_round_score = 0

combinations = [
    ['1 2 3 4 5 6', '1', '1 1 1', '1 1 1 1', '1 1 1 1 1', '1 1 1 1 1 1', 
    '2 2 2', '2 2 2 2', '2 2 2 2 2', '2 2 2 2 2 2', 
    '3 3 3', '3 3 3 3', '3 3 3 3 3', '3 3 3 3 3 3', 
    '4 4 4', '4 4 4 4', '4 4 4 4 4', '4 4 4 4 4 4', 
    '5', '5 5 5', '5 5 5 5', '5 5 5 5 5', '5 5 5 5 5 5', 
    '6 6 6', '6 6 6 6', '6 6 6 6 6', '6 6 6 6 6 6'], 
    [1500, '100', 1000, 2000, 3000, 4000, 
    200, 400, 600, 800, 
    300, 600, 900, 1200, 
    400, 800, 1200, 1600, 
    50, 500, 1000, 1500, 2000, 
    600, 1200, 1800, 2400] ]

def game_results(message, n):
    arr.clear()
    for i in range(n):
        a = random.randrange(1, 7)
        arr.append(a)
        stik_path = 'stik\dice_' + str(a) + '.tgs'
        stik = open(stik_path, 'rb')
        bot.send_sticker(message.chat.id, stik)
    
    result_markup = check_combinations(arr, False)
    buffer = 'Результат раунду:' + ' '.join(map(str, arr)) + "\n Можливі комбінації: "
    bot.send_message(message.chat.id, buffer, reply_markup=result_markup)

def check_combinations(arr, bool):
    inline_keyboard_arr = []
    result_markup = types.InlineKeyboardMarkup(row_width=2)
    arr.sort()
    str_arr = ' '.join(map(str, arr))

    for i in range(len(combinations[0])):
        count = 0
        pos = 0
        while str_arr.find(combinations[0][i], pos) != -1:
            count += 1

            pos = (str_arr.find(combinations[0][i], pos) + len(combinations[0][i]))
        
        if count > 0:
            for j in range(count):
                txt = combinations[0][i] + " - " + str(combinations[1][i])
                item = types.InlineKeyboardButton(txt, callback_data=combinations[1][i])
                inline_keyboard_arr.append(item)

    if bool:
        if len(inline_keyboard_arr) > 0:
            for i in inline_keyboard_arr:
                result_markup.add(i)
            result_markup.add(types.InlineKeyboardButton('Наступние підкидання',callback_data='next'))
            return result_markup
        else:
            kkk = 0
    else:
        if len(inline_keyboard_arr) > 0:
            for i in inline_keyboard_arr:
                result_markup.add(i)
            result_markup.add(types.InlineKeyboardButton('Наступние підкидання',callback_data='next'))
            return result_markup
        else:
            curent_round_score = 0
            result_markup.add(types.InlineKeyboardButton('Наступние підкидання',callback_data='next'))
            return result_markup


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

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '100':
                print(arr)
                arr.remove(1)
                result_markup = check_combinations(arr, True)
                buffer = 'Результат раунду:' + ' '.join(map(str, arr)) + "\n Можливі комбінації: "
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=buffer, reply_markup=result_markup)

    except Exception as e:
        print(repr(e))

bot.infinity_polling()