from flask import Flask, render_template, request
import random
app = Flask(__name__)
dict ={
    "❤️": "love",
    "👍": "like",
    "💀": "hate",
    "😆": "funny",
    "😭": "sad",
    "😡": "angry",
    "🥱": "bored",
    "😴": "asleep",
    "🤩": "excited",
    "😲": "surprised",
    "🍕": "pizza",
    "🍔": "burger",
    "🍟": "fries",
    "☕": "coffee",
    "🫖": "tea",
    "🍰": "cake",
    "🍫": "chocolate",
    "🍦": "icecream",
    "🐱": "cat",
    "🐶": "dog",
    "🙈": "monkey",
    "🐼": "panda",
    "🐢": "turtle",
    "🐠": "fish",
    "🙋": "me",
    "👉": "you",
    "👥": "they",
    "🫶": "friend",
    "👊": "bro",
    "💁‍♀️": "girl",
    "🧑": "boy",
    "👩‍🏫": "teacher",
    "🎓": "student",
    "💻": "computer",
    "📱": "phone",
    "🎮": "game",
    "🎶": "music",
    "💃": "dance",
    "🛌": "sleep",
    "📚": "study",
    "💸": "money",
    "🔥": "fire",
    "🎉": "party",
    "🤯": "wow",
    "😅": "oops",
    "😎": "cool",
    "👌": "ok",
    "🚫": "no",
    "✅": "yes",
    "🆘": "help",
    "🏃‍♂️": "run",
    "😂": "lol",
    "🤦‍♂️": "bruh",
    "😱": "omg",
    "👻": "ghost",
    "🕵️": "sus"
}
@app.route("/", methods = ["GET","POST"])
def index():
    result = ""
    if request.method =="GET":
        emoji = random.choice(list(dict.keys()))
        answer = request.form["answer"].strip().lower()
        if answer == dict[emoji]:
            result = "Correct answer!"
        else:
            result = f"Incorrect answer, the answer must be {dict[emoji]}"
    return render_template("index.html", result = result)
if __name__ == "__main__":
    app.run(debug=True)