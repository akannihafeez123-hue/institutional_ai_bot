from payment_handler import paid_members, vip_members

def broadcast_signal(bot, message, tier="member"):
    targets = vip_members if tier == "vip" else paid_members
    for user_id in targets:
        bot.send_message(user_id, message)
