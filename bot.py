from telebot import TeleBot
from config import BOT_TOKEN, ADMIN_ID
from payment_handler import show_payment_options, confirm_payment, approve_payment, reject_payment
from signal_engine import generate_elite_signal, generate_member_buy_signals
from trade_manager import log_trade, broadcast_trade_report
from broadcast import broadcast_signal
import threading
import time

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'subscribe'])
def start(message):
    show_payment_options(bot, message)

@bot.message_handler(commands=['confirm'])
def confirm(message):
    confirm_payment(bot, message)

@bot.message_handler(commands=['approve'])
def approve(message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split()
    approve_payment(bot, int(parts[1]), parts[2])

@bot.message_handler(commands=['reject'])
def reject(message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split()
    reject_payment(bot, int(parts[1]))

def daily_signal_loop():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    while True:
        elite = generate_elite_signal("BTCUSDT")
        if elite:
            broadcast_signal(bot, f"👑 ELITE SIGNAL\n{elite['commentary']}", tier="vip")
            log_trade(elite['symbol'], elite['entry'], elite['entry'] * 1.5, "vip")

        member_signals = generate_member_buy_signals(symbols)
        if member_signals:
            for s in member_signals:
                broadcast_signal(bot, f"💎 MEMBER SIGNAL\n{s['symbol']} @ ${s['entry']:.2f}", tier="member")
                log_trade(s['symbol'], s['entry'], s['entry'] * 1.5, "member")

        broadcast_trade_report(bot)
        time.sleep(3600)

if __name__ == "__main__":
    threading.Thread(target=daily_signal_loop, daemon=True).start()
    bot.polling(none_stop=True)
