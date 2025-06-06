import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ'  # replace with your actual token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is working!")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    await app.run_polling()

# 👇 Universal launcher: works inside or outside event loops
try:
    asyncio.run(main())
except RuntimeError as e:
    if "already running" in str(e):
        print("🔄 Event loop already running. Using alternate startup...")
        loop = asyncio.get_event_loop()
        loop.create_task(main())
    else:
        raise
