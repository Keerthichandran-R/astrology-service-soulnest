# app.py

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Sample responses from Soul Nest
TAROT_MESSAGES = [
    "🌸 The Flowering: You are blooming, trust your unfolding.",
    "🌕 The Moon: Emotions rise, reflect and rest, my dear soul.",
    "🦋 Transformation: You’re shedding what no longer serves your spirit.",
]

PRASANAM_GUIDANCE = [
    "🌿 Your question carries the wind of karma — the answer lies in stillness.",
    "🔥 Wait 3 days before acting. The fire must cool to reveal the truth.",
    "🌊 Go near flowing water today and speak your prayer. A sign will come.",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_soul_nest():
    data = request.json
    category = data.get("category", "tarot").lower()

    if category == "tarot":
        message = random.choice(TAROT_MESSAGES)
    elif category == "prasanam":
        message = random.choice(PRASANAM_GUIDANCE)
    else:
        message = "🌟 I hear you... But I'm still learning to listen in that way. Try again with 'tarot' or 'prasanam'."

    return jsonify({"reply": message})

if __name__ == "__main__":
    app.run(debug=True)
