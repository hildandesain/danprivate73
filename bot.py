import os, telebot
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MY_ID = 7622264496
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(m):
    if m.from_user.id != MY_ID:
        bot.reply_to(m, "⛔ Private Hildan only")
        return
    bot.reply_to(m, f"Halo Dan! Kamu bilang: {m.text}")

bot.infinity_polling()
