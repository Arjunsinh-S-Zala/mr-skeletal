game = {
    "title": "Final Fantasy X",
    "platform": {
        "console": "PS2",
        "year": 2001
    },
    "characters": ["Tidus", "Yuna", "Auron"]
}
title = game["title"]
console = game["platform"]["console"]
name = game["characters"][1]

print(f"{title}\n{name}\n{console}")

chat = {
    "title": "Filter Chat",
    "messages": [
        {
            "author": {"role": "user"},
            "text": "help me with partitions"
        },
        {
            "author": {"role": "assistant"},
            "text": "show me your disk layout"
        }
    ]
}
something = chat["title"]
author = chat["messages"][0]["author"]["role"]
text = chat["messages"][1]["text"]
print(something,"\n",author,":", text)



