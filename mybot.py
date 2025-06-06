import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ"  # Replace this with your bot token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is working perfectly.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running. Press Ctrl+C to stop.")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Run forever
    await asyncio.Event().wait()

# 👇 This handles both normal and already-running event loops (Windows safe)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "cannot be called from a running event loop" in str(e).lower() or "already running" in str(e).lower():
            print("⚠️ Detected running event loop, switching to alternative start...")
            import nest_asyncio
            nest_asyncio.apply()
            loop = asyncio.get_event_loop()
            loop.create_task(main())
        else:
            raise
