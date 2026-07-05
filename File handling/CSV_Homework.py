import csv
total_salary = 0
employee_count = 0
rows = [
["Name","Department","Salary"],
["Alice","HR",50000],
["Bob","IT",70000],
["Charlie","Finance",65000]
]
with open("employees.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
with open("employees.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        print("Employee:", row[0])

        total_salary += int(row[2])
        employee_count += 1

average_salary = total_salary / employee_count

print("\nTotal Salary:", total_salary)
print("Average Salary:", f"{average_salary:.2f}")