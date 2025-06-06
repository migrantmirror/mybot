from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot.")

app = ApplicationBuilder().token("7956098574:AAFgQa4Z95yWXuHxhETsDWm_v1hs2qWCaeQ
").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
