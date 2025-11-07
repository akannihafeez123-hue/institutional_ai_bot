from config import WALLET_ADDRESS, BANK_DETAILS, PAYPAL_EMAIL, ADMIN_ID
from datetime import datetime

pending_verifications = {}
paid_members = {}
vip_members = {}

def show_payment_options(bot, message):
    bot.send_message(message.chat.id, f"""
💼 *Subscription Plans*  
• 💎 Member: $30/month  
• 👑 VIP: $50/month  

📥 *Payment Methods*  
1. **Crypto Wallet**  
   - `{WALLET_ADDRESS}` (BEP20/ERC20)

2. **Bank Transfer (NGN)**  
   - {BANK_DETAILS['bank']}  
   - {BANK_DETAILS['account_name']}  
   - {BANK_DETAILS['account_number']}

3. **PayPal**  
   - {PAYPAL_EMAIL}

📨 After payment, send `/confirm <transaction_id>` to activate.
""", parse_mode="Markdown")

def confirm_payment(bot, message):
    user_id = message.from_user.id
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Include transaction ID. Example: /confirm 0xabc123")
        return
    tx_id = parts[1]
    pending_verifications[user_id] = tx_id
    bot.send_message(user_id, "🕵️ Awaiting verification.")
    bot.send_message(ADMIN_ID, f"🔔 Payment confirmation from {user_id}:\nTX: {tx_id}")

def approve_payment(bot, user_id, tier):
    if tier == "vip":
        vip_members[user_id] = datetime.utcnow()
    else:
        paid_members[user_id] = datetime.utcnow()
    bot.send_message(user_id, "✅ Subscription activated!")

def reject_payment(bot, user_id):
    tx_id = pending_verifications.pop(user_id, None)
    if tx_id:
        bot.send_message(user_id, f"🚫 Payment rejected. TX {tx_id} not verified.")
