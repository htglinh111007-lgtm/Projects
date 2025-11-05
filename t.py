dict = { 
    "máy tính": "💻",
    "điện thoại": "📱",
    "game": "🎮",
    "nhạc": "🎶",
    "nhảy": "💃",
    "ngủ": "🛌",
    "học": "📚",
    "tiền": "💸",
    "cháy": "🔥",
    "party": "🎉",}

sentence=input("Type sth: ")
if sentence in dict.keys():
    result = dict.get(sentence)
    print(result)
        
