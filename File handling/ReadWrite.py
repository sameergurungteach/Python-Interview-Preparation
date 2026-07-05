def Write(FileName,data):
    with open(FileName,"a") as f:
        f.write(data)
def Read(FileName):
    try:
        with open(FileName,"r") as f:
            return f.readlines()
    except FileNotFoundError:
       return []
Write("hello.txt","this a practice")
print(Read("hello.txt"))