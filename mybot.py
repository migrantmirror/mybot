import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()  # allow nested event loops

BOT_TOKEN = "7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is running.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("Bot started. Press Ctrl+C to stop.")
    await asyncio.Event().wait()  # run forever

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
