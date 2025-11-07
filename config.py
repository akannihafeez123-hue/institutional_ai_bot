import os
from dotenv import load_dotenv

# 📦 Load environment variables from .env file
load_dotenv()

# 🔐 Telegram Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# 🧠 Gemini AI Integration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 💳 Stripe Payment Integration
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

# 💼 Wallet & Bank Payment Details
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
BANK_NAME = os.getenv("BANK_NAME")
BANK_ACCOUNT_NAME = os.getenv("BANK_ACCOUNT_NAME")
BANK_ACCOUNT_NUMBER = os.getenv("BANK_ACCOUNT_NUMBER")

# 🌍 PayPal Setup
PAYPAL_EMAIL = os.getenv("PAYPAL_EMAIL")

# 🏦 Exchange Configuration
EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "bitget").lower()

# 🔑 Bitget API Credentials
BITGET_API_KEY = os.getenv("BITGET_API_KEY")
BITGET_API_SECRET = os.getenv("BITGET_API_SECRET")
BITGET_API_PASSPHRASE = os.getenv("BITGET_API_PASSPHRASE")

# ✅ Utility: Check if all critical keys are loaded
def validate_config():
    missing = []
    for key, value in {
        "BOT_TOKEN": BOT_TOKEN,
        "GEMINI_API_KEY": GEMINI_API_KEY,
        "STRIPE_SECRET_KEY": STRIPE_SECRET_KEY,
        "BITGET_API_KEY": BITGET_API_KEY,
        "BITGET_API_SECRET": BITGET_API_SECRET,
        "BITGET_API_PASSPHRASE": BITGET_API_PASSPHRASE,
    }.items():
        if not value:
            missing.append(key)
    if missing:
        raise EnvironmentError(f"Missing required config keys: {', '.join(missing)}")
