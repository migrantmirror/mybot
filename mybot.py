import asyncio
import logging
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging to catch all errors
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

nest_asyncio.apply()  # fix nested loop issue on Windows

BOT_TOKEN = "7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Hello! I am alive and running 24/7!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type /start to see me respond!")

async def main():
    try:
        app = ApplicationBuilder().token(BOT_TOKEN).build()

        # Add command handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))

        await app.initialize()
        await app.start()
        await app.updater.start_polling()

        print("✅ Bot started. Running 24/7. Press Ctrl+C to stop.")
        await asyncio.Event().wait()  # Keeps bot alive forever

    except Exception as e:
        logging.error(f"❌ Bot crashed with error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
