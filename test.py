dict = { 
    "yêu": "❤️",
    "thích": "👍",
    "ghét": "💀",
    "buồn cười": "😆",
    "buồn": "😭",
    "tức giận": "😡",
    "chán": "🥱",
    "đang ngủ": "😴",
    "hào hứng": "🤩",
    "ngạc nhiên": "😲",
    "khóc": "😢",
    # Food
    "pizza": "🍕",
    "burger": "🍔",
    "khoai tây chiên": "🍟",
    "cà phê": "☕",
    "trà": "🫖",
    "bánh": "🍰",
    "socola": "🍫",
    "kem": "🍦",
    # Animals
    "mèo": "🐱",
    "chó": "🐶",
    "khỉ": "🙈",
    "gấu trúc": "🐼",
    "rùa": "🐢",
    "cá": "🐠",
    # People & reactions
    "tôi": "🙋",
    "bạn": "👉",
    "họ": "👥",
    "bạn": "🫶",
    "bro": "👊",
    "con gái": "💁‍♀️",
    "con trai": "🧑",
    "giáo viên": "👩‍🏫",
    "học sinh": "🎓",
    # Objects & fun stuff
    "máy tính": "💻",
    "điện thoại": "📱",
    "game": "🎮",
    "nhạc": "🎶",
    "nhảy": "💃",
    "ngủ": "🛌",
    "học": "📚",
    "tiền": "💸",
    "cháy": "🔥",
    "party": "🎉",
    # Random funny slang
    "wow": "🤯",
    "oops": "😅",
    "cool": "😎",
    "ok": "👌",
    "no": "🚫",
    "yes": "✅",
    "cứu": "🆘",
    "chạy": "🏃‍♂️",
    "lol": "😂",
    "bruh": "🤦‍♂️",
    "omg": "😱",
    "ma": "👻",
    "sus": "🕵️"}

sentence=input("Type sth: ")
for key in dict.keys():
    if key in sentence:
        sentence = sentence.replace(key, dict[key])
print(sentence)

