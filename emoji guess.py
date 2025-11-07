import random
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
quest = random.choice(list(dict.keys()))
print(quest)
ans = input("Your answer is: ")
point = 0
if ans == dict[quest]:
    print("You got it")
    point+=10
else:
    print("Incorrect answer")