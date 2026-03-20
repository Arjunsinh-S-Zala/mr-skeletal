import json
data = [
    {
        "title": "chat one",
        "messages": [
            {
                "from": "person",
                "body": [
                    {
                        "words": "hey how are you",
                        "sent_at": "12:00",
                        "received_at": "12:01"
                    }
                ]
            }
        ]
    }
]

def extract_claude(data):
    big_list = []
    for conversation in data:
        data_encasing_list = []
        for message in conversation["messages"]:
            content = message["body"][0]
            conversations = {
                "from": message["from"],
                "words": content["words"],
                "sent_at": content["sent_at"],
                "recieved_at": content["received_at"]
            }
            data_encasing_list.append(conversations)
    big_list.append(data_encasing_list)           
    
    return big_list

result = extract_claude(data)
print(result)
print(json.dumps(result, indent=2))