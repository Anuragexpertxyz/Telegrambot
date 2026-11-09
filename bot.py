import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
Application,
CommandHandler,
CallbackQueryHandler,
ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
keyboard = [
[InlineKeyboardButton("Channel Management", callback_data="channel")],
[InlineKeyboardButton("Scheduled Posts", callback_data="schedule")],
[InlineKeyboardButton("Polls", callback_data="polls")],
[InlineKeyboardButton("Reactions", callback_data="reactions")],
[InlineKeyboardButton("Help", callback_data="help")]
]

await update.message.reply_text(
    "Welcome to Channel Management Bot!\n\nChoose an option:",
    reply_markup=InlineKeyboardMarkup(keyboard)
)
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
query = update.callback_query
await query.answer()

messages = {
    "channel": "Channel Management\n\nFeatures coming soon!",
    "schedule": "Scheduled Posts\n\nFeatures coming soon!",
    "polls": "Poll Management\n\nFeatures coming soon!",
    "reactions": "Reactions\n\nFeatures coming soon!",
    "help": "Commands:\n/start - Open bot menu"
}

await query.edit_message_text(
    messages.get(query.data, "Unknown option")
)
def main():
if not TOKEN:
raise RuntimeError("BOT_TOKEN is not configured!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu))

print("Bot is running...")
app.run_polling()
if name == "main":
main()
