a = int(input("Enter any number: "))
count = 0
while a != 0:
    a = a//10
    count = count + 1
print("Number of digits is: ", count)