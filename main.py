import telebot
bot=telebot.TeleBot('1652045021:AAFeD9evC3UMCNQqV9_4a9pmfhzIUkjaGvM')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    input_text=message.text
    bot.send_message(message.chat.id, input_text)

bot.polling(none_stop=True,interval=0)