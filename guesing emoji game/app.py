from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "secrect_random"
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
@app.route("/")
def index():
    emoji = random.choice(list(dict.keys()))
    session["current_emoji"] = emoji
    return render_template("index.html", emoji=emoji)
from flask import request
@app.route("/check", methods=["POST"])
def check():
    user_answer = request.form["answer"].strip().lower()   
    emoji = session.get("current_emoji")                  
    correct_answer = dict.get(emoji)               
    if user_answer == correct_answer:
        result = "True ✅"
    else:
        result = f"False ❌ (Correct: {correct_answer})"

    return render_template("result.html", emoji=emoji, result=result)
if __name__ == "__main__":
    app.run(port = 5002, debug=True)
