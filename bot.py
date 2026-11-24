import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["🛒 Buy Proxy", "📧 Email Products"],
    ["💰 Deposit", "📜 Deposit History"],
    ["👥 Referral", "🎧 Support"],
]

TEXTS = {
    "🛒 Buy Proxy": (
        "🛒 Proxy Store\n\n"
        "Proxy packages will appear here after the admin adds products."
    ),
    "📧 Email Products": (
        "📧 Email Products\n\n"
        "Only authorized email products and services will be listed here."
    ),
    "💰 Deposit": (
        "💰 Deposit\n\n"
        "Manual deposit will be set up next. You will see the payment "
        "instructions and submit a transaction ID here."
    ),
    "📜 Deposit History": (
        "📜 Deposit History\n\n"
        "Your deposit records will appear here after the database is connected."
    ),
    "👥 Referral": (
        "👥 Referral\n\n"
        "Your personal referral link will be available after referral setup."
    ),
    "🎧 Support": (
        "🎧 Support\n\n"
        "Please contact the store administrator for help."
    ),
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    await update.effective_message.reply_text(
        "🌐 Welcome to PROXYHUB!\n\nChoose a service from the menu.",
        reply_markup=keyboard,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text(
        "Use /start to open the PROXYHUB menu."
    )


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None or message.text is None:
        return

    response = TEXTS.get(
        message.text,
        "Please choose an option from the menu or send /start.",
    )
    await message.reply_text(response)


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. Add it as an environment variable / secret."
        )

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    logger.info("PROXYHUB bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()
