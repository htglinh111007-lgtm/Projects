# User input a string
sentence = input("Let's input a sentence: ")
string = sentence.split()
# Emoji dictionary
emoji_dict ={
    # Basic emotions
    "love": "❤️",
    "like": "👍",
    "hate": "💀",
    "funny": "😆",
    "sad": "😭",
    "angry": "😡",
    "bored": "🥱",
    "asleep": "😴",
    "excited": "🤩",
    "surprised": "😲",
    "cry": "😢",
    # Food
    "pizza": "🍕",
    "burger": "🍔",
    "fries": "🍟",
    "coffee": "☕",
    "tea": "🫖",
    "cake": "🍰",
    "chocolate": "🍫",
    "icecream": "🍦",
    # Animals
    "cat": "🐱",
    "dog": "🐶",
    "monkey": "🙈",
    "panda": "🐼",
    "turtle": "🐢",
    "fish": "🐠",
    # People & reactions
    "me": "🙋",
    "you": "👉",
    "they": "👥",
    "friend": "🫶",
    "bro": "👊",
    "girl": "💁‍♀️",
    "boy": "🧑",
    "teacher": "👩‍🏫",
    "student": "🎓",
    # Objects & fun stuff
    "computer": "💻",
    "phone": "📱",
    "game": "🎮",
    "music": "🎶",
    "dance": "💃",
    "sleep": "🛌",
    "study": "📚",
    "money": "💸",
    "fire": "🔥",
    "party": "🎉",
    # Random funny slang
    "wow": "🤯",
    "oops": "😅",
    "cool": "😎",
    "ok": "👌",
    "no": "🚫",
    "yes": "✅",
    "help": "🆘",
    "run": "🏃‍♂️",
    "lol": "😂",
    "bruh": "🤦‍♂️",
    "omg": "😱",
    "ghost": "👻",
    "sus": "🕵️",
}
a=-1
for s in string:
    a = a+1
    if a == len(string):
        break
    for d in emoji_dict:
        if s == d:
            string[a] = emoji_dict[d]
        else:
            continue
output = " ".join(string)
print(output)