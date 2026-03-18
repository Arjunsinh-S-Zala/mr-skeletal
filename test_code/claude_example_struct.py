data = [
    {
        "name": "conversation one",
        "chat_messages": [
            {
                "sender": "human",
                "content": [
                    {
                        "text": "hello there"
                    }
                ]
            },
            {
                "sender": "assistant",
                "content": [
                    {
                        "text": "hello back"
                    }
                ]
            }
        ]
    }
]

for conversation in data:
    print(conversation["name"])    
    for message in conversation["chat_messages"]:
        print(message["sender"], message["content"][0]["text"])
        