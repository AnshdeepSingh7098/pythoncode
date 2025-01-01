# f=open("file.txt")
# lines=f.readlines()
# print(lines, type(lines))

# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# lines=f.readline()
# while lines!="":
#     print(lines)
#     lines=f.readline() 
#if you not write this line then it will print only one line infinte times.

#append function in file handling 
# str="hello lets start python programming\n"
# f=open('file.txt', 'a')
# f.write(str)
# f.close()


#with block in file handling 
with open('file.txt') as f:
    print(f.read())