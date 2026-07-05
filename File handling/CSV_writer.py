import csv
rows = [
    ["Name","age","address"],
    ["sameer",21,"Changunarayan"],
    ["Nikesh",21,"Ramhiti"]
]
with open("profile.csv","w",newline="") as f:
 writer = csv.writer(f)
 writer.writerows(rows)
with open("profile.csv") as f:
  reader = csv.reader(f)
  for row in reader:
   print(row)

   