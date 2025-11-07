from telebot import TeleBot
from config import BOT_TOKEN, ADMIN_ID
from payment_handler import show_payment_options, confirm_payment, approve_payment, reject_payment
from signal_engine import generate_elite_signal, generate_member_buy_signals
from trade_manager import log_trade, broadcast_trade_report
from broadcast import broadcast_signal
import threading
import time

bot = TeleBot(BOT_TOKEN)

# 🔐 Admin check
def is_admin(message):
    return message.from_user.id == ADMIN_ID

# 🧾 Start or Subscribe
@bot.message_handler(commands=['start', 'subscribe'])
def start(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Access denied. This bot is for admin use only.")
        return
    show_payment_options(bot, message)

# 💳 Confirm Payment
@bot.message_handler(commands=['confirm'])
def confirm(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Access denied.")
        return
    confirm_payment(bot, message)

# ✅ Approve Payment
@bot.message_handler(commands=['approve'])
def approve(message):
    if not is_admin(message):
        return
    parts = message.text.split()
    if len(parts) < 3:
        bot.reply_to(message, "❌ Usage: /approve <user_id> <tier>")
        return
    approve_payment(bot, int(parts[1]), parts[2])

# ❌ Reject Payment
@bot.message_handler(commands=['reject'])
def reject(message):
    if not is_admin(message):
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Usage: /reject <user_id>")
        return
    reject_payment(bot, int(parts[1]))

# 🔁 Daily Signal Loop
def daily_signal_loop():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    while True:
        elite = generate_elite_signal("BTCUSDT")
        if elite:
            broadcast_signal(bot, f"👑 ELITE SIGNAL\n\n📊 {elite['symbol']} ({elite['confidence']}%)\n📈 Entry: ${elite['entry']:.2f}\n\n{elite['commentary']}", tier="vip")
            log_trade(elite['symbol'], elite['entry'], elite['entry'] * 1.5, "vip")

        member_signals = generate_member_buy_signals(symbols)
        if member_signals:
            for s in member_signals:
                broadcast_signal(bot, f"💎 MEMBER SIGNAL\n\n📊 {s['symbol']} ({s['confidence']}%)\n📈 Entry: ${s['entry']:.2f}", tier="member")
                log_trade(s['symbol'], s['entry'], s['entry'] * 1.5, "member")

        broadcast_trade_report(bot)
        time.sleep(3600)  # Run every hour

# 🚀 Launch Bot
if __name__ == "__main__":
    threading.Thread(target=daily_signal_loop, daemon=True).start()
    bot.polling(none_stop=True)
