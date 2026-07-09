KEY = 23
#READ ORIGINAL VALUE 
with open("hello.txt","rb") as f:
    original = f.read()
# print(original)

#ENCRYPTION PROCESS
encrypted = bytes( b ^ KEY for b in original)
with open("encrypted.bin","wb") as f:
   f.write(encrypted)
# print(encrypted)
# print(list(encrypted))

#DECRYPTED PROCESS
with open("encrypted.bin","rb") as f:
    encrypted_value = f.read()
print(encrypted_value)