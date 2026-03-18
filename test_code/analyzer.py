import json

with open('conversations.json', 'r') as f:
    data = json.load(f)

conversation = data[11]
mapping = conversation['mapping']

for key, value in mapping.items():
    if value.get('message') is not None:
        role = value["message"]["author"]["role"]
        parts = value["message"]["content"].get("parts", [])
        if parts:
            text = parts[0]
        else:
            text = "[no text content]"
    print(f"{role}: {text[:100]}")