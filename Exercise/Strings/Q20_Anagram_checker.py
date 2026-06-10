# -### One-line meaning
# **Anagram = same letters, different order**

def anagram_checker(str1,str2):
    return sorted(str1)==sorted(str2)

a=anagram_checker("LISTEN","SLIENT")
print(f"is anagram: {a}")