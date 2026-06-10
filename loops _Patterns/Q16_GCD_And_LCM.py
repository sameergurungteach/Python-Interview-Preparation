
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

num1 = a
num2 = b

while b:
    a, b = b, a % b
# temp = b;
# b = a % b;
# a = temp;

gcd = a
lcm = (num1 * num2) // gcd

print(f"GCD = {gcd}")
print(f"LCM = {lcm}")