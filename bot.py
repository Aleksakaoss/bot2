import telebot
TOKEN = '' #Введите сюда токен бота, полученный в BotFather
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Напишите мне что-нибудь!, и я смогу тебе помочь!')
if __name__ == '__main__':
    bot.infinity_polling()