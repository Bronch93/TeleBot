import telebot

bot = telebot.TeleBot("6421472079:AAEk8tT9b69EeuwA8e-ov2PEUl9kKxBQ44U")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name}",
    )


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(
        message.chat.id, "<b>Help</b> <em><u>information</u></em>", parse_mode="html"
    )


bot.polling(none_stop=True)
