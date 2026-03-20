import json

data = [
    {
        "name": "test conversation",
        "chat_messages": [
            {
                "sender": "human",
                "content": [
                    {
                        "start_timestamp": "2024-01-01T00:00:00",
                        "stop_timestamp": "2024-01-01T00:00:01",
                        "text": "hello there"
                    }
                ]
            }
        ]
    }
]

def extract_claude(data):
    all_conversations = []
    
    for conversation in data:
        messages = []
        for message in conversation["chat_messages"]:
            content = message["content"][0]
            clean_message = {
                "role": message["sender"],
                "text": content["text"],
                "start": content["start_timestamp"],
                "stop": content["stop_timestamp"]
            }
            messages.append(clean_message)
        
        all_conversations.append(messages)
    
    return all_conversations

result = extract_claude(data)
print(result)