import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["🛒 Buy Proxy", "📧 Email Products"],
    ["💰 Deposit", "📜 Deposit History"],
    ["👥 Referral", "🎧 Support"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        MENU,
        resize_keyboard=True
    )
    await update.message.reply_text(
        "🌐 Welcome to PROXYHUB!\n\n"
        "আপনার পছন্দের সার্ভিস নির্বাচন করুন।",
        reply_markup=keyboard
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "🛒 Buy Proxy": "🛒 Proxy Store\n\nশীঘ্রই Proxy প্যাকেজ এখানে দেখা যাবে।",
        "📧 Email Products": "📧 Email Products\n\nঅনুমোদিত ইমেইল সার্ভিস এখানে থাকবে।",
        "💰 Deposit": "💰 Deposit\n\nএখানে টাকা জমা দেওয়ার ব্যবস্থা থাকবে।",
        "📜 Deposit History": "📜 আপনার Deposit History এখানে দেখা যাবে।",
        "👥 Referral": "👥 আপনার Referral ব্যবস্থা শীঘ্রই চালু হবে।",
        "🎧 Support": "🎧 Support\n\nসাহায্যের জন্য Admin-এর সঙ্গে যোগাযোগ করুন।"
    }

    await update.message.reply_text(
        responses.get(text, "দয়া করে মেনু থেকে একটি অপশন নির্বাচন করুন।")
    )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN সেট করা হয়নি!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("PROXYHUB Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
