from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import asyncio

# Replace this with your actual bot token
BOT_TOKEN = "7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ"

# Replace this with your actual Telegram user chat ID (you'll get it by sending /id)
YOUR_CHAT_ID = 123456789  # Update after running /id

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your bot.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ Send /id to get your chat ID.\nI'm also sending automatic alerts every 60 seconds.")

# ID command
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"🆔 Your chat ID is: {chat_id}")

# Auto-alert function
async def send_alerts(application):
    while True:
        try:
            await application.bot.send_message(chat_id=YOUR_CHAT_ID, text="🚨 This is an automatic alert sent every 60 seconds.")
            await asyncio.sleep(60)
        except Exception as e:
            print(f"Error sending alert: {e}")
            await asyncio.sleep(60)

# Main function
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", get_chat_id))

    # Start background alert task
    asyncio.create_task(send_alerts(app))

    print("🤖 Bot is running... Press Ctrl+C to stop.")
    await app.run_polling()

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
