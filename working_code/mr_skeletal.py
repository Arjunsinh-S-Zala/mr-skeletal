# Mr. Skeletal is a code stripper that can and has stripped of JSON structures of Chatgpt, Claude and Gemini from Google AI Studio for now. It will simply strip the long structures of the chats so you can look at the structure and code easily around it. 
# Below is the example code that operates at smaller scale to understand the fundamental way Mr. Skeletal works. 
# import json
# with open('nested_test.json', 'r') as f:
#     data = json.load(f)
    
# print(data)
# for i in data:
#     print(i,"->",type(data[i]))
#     if isinstance(data[i], str):  
#         length = len(data[i])
#         if length > 5:
#             print(f"{i} is a long string!")

# for i in data:
#     value = data[i]
    
#     if isinstance(value, str):
#         print(f"Found string: {value}")
    
#     if isinstance(value, dict):
#         print(f"Found dict, need to go inside!")
    
#     if isinstance(value, list):
#         print(f"Found list, need to go inside!")            

import json


# 1. We DEFINE our custom tool
def mr_skeletal(thing):
    if isinstance(thing, list):
        for index, item in enumerate(thing):
        
            if isinstance(item, str):
                print(f"Found string: {item}")
                length = len(item)
                if length > 5:
                    print(f"{item} is a long string")
                    thing[index] = "[...]"
        
            if isinstance(item, dict):
                mr_skeletal(item)# recurse
        
            if isinstance(item, list):
                mr_skeletal(item)# recurse

    # If it's a dict, loop through its keys
    if isinstance(thing, dict):
        for key in thing:
            value = thing[key]
            
            if isinstance(value, str):
                print(f"Found string: {value}")
                length = len(value)
                if length > 5:
                    thing[key] = "[...]"
                    print(f"{value} is a long string")
            
            if isinstance(value, dict):
                mr_skeletal(value)
            
            if isinstance(value, list):
                mr_skeletal(value)
                # WE WILL DO SOMETHING MAGIC HERE LATER

# 2. Load the file
with open('conversations(claude).json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mr_skeletal(data)  # Strip the meat first!

with open('claudeskeleton.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Done! Check skeleton.json")  