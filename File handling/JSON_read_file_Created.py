import json

student = {
    "name": "Sameer",
    "age": 21,
    "city": "Kathmandu"
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)