import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

ADMIN_ID = 123456789  # Replace with your Telegram ID
WALLET_ADDRESS = "0xA1B2C3D4E5F6G7H8I9J0KLMNOPQR1234567890AB"
BANK_DETAILS = {
    "bank": "Zenith Bank",
    "account_name": "Khleez Signals",
    "account_number": "1234567890"
}
PAYPAL_EMAIL = "khleezsignals@protonmail.com"
