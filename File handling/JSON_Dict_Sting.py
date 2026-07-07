# import json
# # student = {
# #     "name": "Sameer",
# #     "age": 21
# # }
# # print(type(student))
# # json_text = json.dumps(student)
# # print(type(json_text))
# student = {"name": "Sameer"}

# x = json.dumps(student)
# print(type(x))
import json

# Python dict → JSON string/file
data = {"name": "Alice", "age": 21, "skills": ["Python", "AI"]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# JSON file → Python dict
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["skills"])