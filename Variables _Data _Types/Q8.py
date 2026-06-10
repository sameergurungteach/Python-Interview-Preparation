a = int(input("Enter any number: "))
b = a
total = 0
while a != 0:
   digit = a % 10
   total = total + digit*digit*digit
   a = a//10
if total == b:
  print("Armstrong number")     
else:
  print("Not an Armstrong number")