with open("file.txt") as f:
    c=f.read()
with open('file3.txt','w') as f:
    f.write(c)