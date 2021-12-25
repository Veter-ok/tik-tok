import telebot

TOKEN = "1709159871:AAH-YG-rXNU3IBMB_q7LoXjpOFDwEWvCOPk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Бот запущен")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()