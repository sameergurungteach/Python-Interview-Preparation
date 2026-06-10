# a = int(input("Enter the number of rows for Floyd's triangle: "))
# b = 1
# for i in range(1,a+1):
#     for j in range(b,i):
#         print(j)
#         b = i


a = int(input("Enter number of rows: "))
num = 1

for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()