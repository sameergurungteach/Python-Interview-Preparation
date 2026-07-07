warnings =[]
with open("app.log","r") as f:
 for check in f: 
   if "WARNING" in check:
     warnings.append(check.strip()) 
print(warnings)