from flask import Flask, request
import stripe
from config import STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
from payment_handler import paid_members, vip_members
from datetime import datetime

app = Flask(__name__)
stripe.api_key = STRIPE_SECRET_KEY

@app.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    event = stripe.Webhook.construct_event(request.data, request.headers.get("Stripe-Signature"), STRIPE_WEBHOOK_SECRET)
    session = event["data"]["object"]
    user_id = int(session["client_reference_id"])
    amount = session["amount_total"] / 100
    if amount == 30:
        paid_members[user_id] = datetime.utcnow()
    elif amount == 50:
        vip_members[user_id] = datetime.utcnow()
    return "OK", 200
