from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
