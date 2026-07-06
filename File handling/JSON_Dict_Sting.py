import json
# student = {
#     "name": "Sameer",
#     "age": 21
# }
# print(type(student))
# json_text = json.dumps(student)
# print(type(json_text))
student = {"name": "Sameer"}

x = json.dumps(student)
print(type(x))