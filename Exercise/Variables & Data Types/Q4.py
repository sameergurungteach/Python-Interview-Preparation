a = int(input("Enter any number: "))
re = 0
o = a 
while a!=0:
    r = a % 10
    re = re * 10 + r
    a = a//10


if(o == re):
        print("Palindrome") 
else:
        print("Not a palindrome")         