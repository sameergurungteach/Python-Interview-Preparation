en = []
with open("hello.txt","rb") as f:
    data = f.read()
print(data)
print(data.decode())
print(data.decode().encode())
for i in data:
    en.append(chr(i+1))
print(en)
print(type(en))
dn = "".join(en)
print(dn.split())
print(type(dn))