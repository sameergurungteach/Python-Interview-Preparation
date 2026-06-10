
# For an interview or viva, you can define a dictionary as:
# **"A dictionary is a built-in Python data type that stores data in "
# "key-value pairs. Each key is unique and is used to access its corresponding "
# "value."**

# ### Example

# ```python
# student = {
#     "name": "Sameer",
#     "age": 20,
#     "faculty": "BCA"
# }
# ```
# Here:
# * `"name"`, `"age"`, `"faculty"` are **keys**
# * `"Sameer"`, `20`, `"BCA"` are **values**

# ### Key Points

# * Stores data as **key : value** pairs.
# * Keys must be unique.
# * Dictionaries are mutable (can be changed after creation).
# * Created using curly braces `{}`.



# Frequency of characters means counting how many times each character appears in a string.
s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    print(ch, "=", freq[ch])