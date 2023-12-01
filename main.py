import telebot
bot = telebot.TeleBot('6942552926:AAFUoQEMTxgVENO8drJxRKNgfXzvRlfUuNY')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['love'])
def main(message):
    bot.send_message(message.chat.id, 'Очень сильно люблю!!!')

@bot.message_handler(commands=['jump'])
def main(message):
    bot.send_message(message.chat.id, 'Прыгай? \nПрыгай?')

bot.infinity_polling()