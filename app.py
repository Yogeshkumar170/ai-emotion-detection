from flask import Flask, render_template, request

app = Flask(__name__)

def detect_emotion(text):
    text_lower = text.lower()

    # Emotion words
    angry_words = ["angry", "hate", "furious", "mad", "annoyed", "upset", "frustrated"]
    fear_words = ["fear", "scared", "terrified", "afraid", "panic", "anxious", "nervous"]
    surprise_words = ["wow", "surprise", "amazing", "shocked", "unbelievable", "incredible"]
    sad_words = ["sad", "cry", "unhappy", "depressed", "miserable", "not happy", "lonely", "disappointed"]
    happy_words = ["happy", "love", "good", "fantastic", "great", "excellent", "joy", "delighted", "wonderful"]

    # Negations
    negations = ["not", "don't", "never", "no"]

    def is_negated(text, word):
        for neg in negations:
            if f"{neg} {word}" in text:
                return True
        return False

    # Check each emotion
    for word in angry_words:
        if word in text_lower:
            return "Angry 😡" if not is_negated(text_lower, word) else "Happy 😊"

    for word in fear_words:
        if word in text_lower:
            return "Fear 😨" if not is_negated(text_lower, word) else "Happy 😊"

    for word in surprise_words:
        if word in text_lower:
            return "Surprise 😲"

    for word in sad_words:
        if word in text_lower:
            return "Sad 😢" if not is_negated(text_lower, word) else "Happy 😊"

    for word in happy_words:
        if word in text_lower:
            return "Happy 😊" if not is_negated(text_lower, word) else "Sad 😢"

    # Default neutral
    return "Neutral 😐"

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = ""
    if request.method == "POST":
        text = request.form["text"]
        emotion = detect_emotion(text)
    return render_template("index.html", emotion=emotion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)