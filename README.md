# PROXYHUB Telegram Bot

This is the starter project for the PROXYHUB Telegram bot.

## Files
- `bot.py` — Telegram bot code
- `requirements.txt` — Python dependency
- `.env.example` — example environment variable file (never put a real token here)

## Important security note
Never paste your Telegram bot token into `bot.py`, a public GitHub file, screenshots, or chat.
If a real token was ever committed to a public repository, open Telegram's **@BotFather**,
use `/revoke` for that bot, and store the new token only as a secret/environment variable.

## Run locally
1. Install Python 3.10 or newer.
2. Install dependencies: `pip install -r requirements.txt`
3. Set the environment variable `BOT_TOKEN` to your token.
4. Run: `python bot.py`

## Hosting
GitHub stores the source code; it does not keep a Telegram bot running by itself.
A hosting service/worker is needed to run `python bot.py` continuously. Add `BOT_TOKEN`
to that host's secret/environment-variable settings.

## Current functionality
The bot displays the PROXYHUB menu and placeholder replies. Deposit approval, user balances,
product inventory, purchases, referral tracking, and the admin dashboard are not connected yet.
Those require a database and admin/payment configuration and will be added in later steps.
