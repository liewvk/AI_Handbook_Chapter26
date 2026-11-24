def classify_message(message):
    text = message.lower()
    if "refund" in text or "return" in text:
        return "Returns"
    if "delivery" in text or "shipping" in text:
        return "Delivery"
    return "General"

messages = [
    "Where is my delivery?",
    "I would like a refund.",
    "Do you have the blue model?"
]
for item in messages:
    print(classify_message(item))

