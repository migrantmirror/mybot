from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your real bot token
BOT_TOKEN = "7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ"

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"🆔 Your chat ID is: {chat_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("id", get_chat_id))

print("✅ Bot is running... Type /id to get your chat ID")
app.run_polling()
