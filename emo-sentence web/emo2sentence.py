from flask import Flask, render_template, request
app = Flask(__name__)
eng ={
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
    "🕵️": "sus",
}
viet = {
    "❤️": "yêu",
    "👍": "thích",
    "💀": "ghét",
    "😆": "buồn cười",
    "😭": "buồn",
    "😡": "tức giận",
    "🥱": "chán",
    "😴": "đang ngủ",
    "🤩": "hào hứng",
    "😲": "ngạc nhiên",
    "😢": "khóc",
    # Food
    "🍕": "pizza",
    "🍔": "burger",
    "🍟": "khoai tây chiên",
    "☕": "cà phê",
    "🫖": "trà",
    "🍰": "bánh",
    "🍫": "socola",
    "🍦": "kem",
    # Animals
    "🐱": "mèo",
    "🐶": "chó",
    "🙈": "khỉ",
    "🐼": "gấu trúc",
    "🐢": "rùa",
    "🐠": "cá",
    # People & reactions
    "🙋": "tôi",
    "👉": "bạn",
    "👥": "họ",
    "🫶": "bạn",
    "👊": "bro",
    "💁‍♀️": "con gái",
    "🧑": "con trai",
    "👩‍🏫": "giáo viên",
    "🎓": "học sinh",
    # Objects & fun stuff
    "💻": "máy tính",
    "📱": "điện thoại",
    "🎮": "game",
    "🎶": "nhạc",
    "💃": "nhảy",
    "🛌": "ngủ",
    "📚": "học",
    "💸": "tiền",
    "🔥": "cháy",
    "🎉": "party",
    # Random funny slang
    "🤯": "wow",
    "😅": "oops",
    "😎": "cool",
    "👌": "ok",
    "🚫": "no",
    "✅": "yes",
    "🆘": "cứu",
    "🏃‍♂️": "chạy",
    "😂": "lol",
    "🤦‍♂️": "bruh",
    "😱": "omg",
    "👻": "ma",
    "🕵️": "sus",
}
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        lang = request.form.get("lang").lower()
        sentence = request.form.get("sentence", "").lower()
        if lang == "english":
            result = sentence
            for key in sorted(eng.keys(), key=len, reverse=True):
                if key in result:
                    result = result.replace(key,eng[key])
            output = result
        elif lang == "vietnamese":
            result = sentence
            for key in sorted(viet.keys(), key=len, reverse=True):
                if key in result:
                    result = result.replace(key, viet[key])
            output = result
    return render_template("index.html", result=output)
if __name__ == "__main__":
    app.run(debug=True)