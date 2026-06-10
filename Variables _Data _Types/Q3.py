s = input( "Enter any string: ")
vowels = "aeiou"
a = s.lower()
for x in a:
    if x in vowels:
        print(x)
        