def generate_elite_signal(symbol):
    df = fetch_kline(symbol, "15m")
    df = add_indicators(df)
    keras_signal = keras_model.predict(preprocess(df))[-1][0]
    decision = ai_select_institutional_trade(symbol)
    sentiment = get_news_sentiment(symbol)
    confidence = int((keras_signal + sentiment + decision['confidence']/100) / 3 * 100)

    if confidence >= 90 and decision['signal'] == "BUY":
        commentary = get_gemini_commentary(decision, keras_signal)
        return {
            "symbol": symbol,
            "confidence": confidence,
            "commentary": commentary,
            "entry": df['close'].iloc[-1]
        }

def generate_member_buy_signals(symbols):
    signals = []
    for symbol in symbols:
        decision = ai_select_institutional_trade(symbol)
        if decision['confidence'] >= 80 and decision['signal'] == "BUY":
            signals.append({
                "symbol": symbol,
                "confidence": decision['confidence'],
                "entry": fetch_kline(symbol, "15m")['close'].iloc[-1]
            })
        if len(signals) >= 4:
            break
    return signals
