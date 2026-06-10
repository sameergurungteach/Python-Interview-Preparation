a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))
if(a>b) and (a>c):
    print("Largest number is: ",a)
elif(b>a) and (b>c):
    print("Largest number is: ",b)
else:
    print("Largest number is: ",c)   