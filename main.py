import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Топ Фандинги 🔥")],
        [KeyboardButton("Разница 💵")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Добро пожаловать! Выберите действие:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text == "Топ Фандинги 🔥":
        await update.message.reply_text("Здесь будет список топ фандингов от ±0.75%")
    elif text == "Разница 💵":
        await update.message.reply_text("Здесь будет анализ разницы между биржами")
    else:
        await update.message.reply_text(f"Запрос по монете: {text} — здесь будет информация о фандинге")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7692499543:AAGn4B2M1LE0z9mNga1baA_KK_nDVsNHbdo").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
