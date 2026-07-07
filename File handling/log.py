c = 0
with open("app.log","r") as f:
    # print(f.read())
  for line in f:
   if "ERROR" in line:
    c =c+1
    print("Error founded")
print("total error is ",c)