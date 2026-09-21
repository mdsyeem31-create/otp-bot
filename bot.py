import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text=f"পাওয়া গেছে: {text}")

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("Token missing!")
        return
    app = ApplicationBuilder().token(token.strip()).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
