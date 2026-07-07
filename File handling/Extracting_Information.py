warnings =[]
with open("app.log","r") as f:
 for check in f: 
   if "WARNING" in check:
     warnings.append(check.strip()) 
for line in warnings:
  p = line.split(":")
  print(p[0])

