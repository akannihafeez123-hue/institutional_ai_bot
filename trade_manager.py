from broadcast import broadcast_signal

trade_log = []

def log_trade(symbol, entry, tp, tier):
    trade_log.append({"symbol": symbol, "entry": entry, "tp": tp, "tier": tier})

def broadcast_trade_report(bot):
    for trade in trade_log:
        msg = f"📈 TRADE HIT: {trade['symbol']}\nEntry: ${trade['entry']:.2f} → TP: ${trade['tp']:.2f}\n🎉 Congrats {trade['tier'].upper()} members!"
        broadcast_signal(bot, msg, tier=trade['tier'])
    trade_log.clear()
