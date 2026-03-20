import json
with open('exports/conversations(claude).json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def extract_claude(data):
    big_list = []
    for conversation in data:
        encasing__list = []
        print(conversation["name"])
        for message in conversation["chat_messages"]:
            content = message.get("content", [])
            created_at = message.get("created_at", "")
            if content:
                content_item = content[0]
                text = content_item.get("text", "")
                start_timestamp = content_item.get("start_timestamp", "")
                stop_timestamp = content_item.get("stop_timestamp", "")
            else:
                text = ""
                start_timestamp = ""
                stop_timestamp = ""
                created_at = message.get("created_at", "unknown")
            role = message.get("sender", "no_role_found")
            files = message.get("files", [])
            attachments = message.get("attachments", [])
            filtered_final_messages = {
                "created_at" : created_at,
                "role" : role,
                "text" : text,
                "start_timestamp" : start_timestamp,
                "stop_timestamp" : stop_timestamp,
                "files": files,
                "attachments": attachments
             }
            encasing__list.append(filtered_final_messages)
    big_list.append(encasing__list)        
    return big_list

result = extract_claude(data)

with open('claude_output_3.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2)

print("Done!")