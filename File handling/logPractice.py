c = 0
li = []
with open("app.log","r") as f:
   for line in f:
      if "ERROR" in line:
         c = c + 1
      elif "WARNING" in line:
         li.append(line)
print("total error is :",c)
print("warning are:")
for ili in li:
   print(ili)