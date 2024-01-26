# f1 = open("data.txt")

# output= f1.read()
# print(output)

# f1 = open("data.txt", mode="w") #over write the previous data
# f1.write("\n The text is has overwritten")
# f1 = open("data.txt")
# output= f1.read()
# print(output)

# f2= open("data.txt", mode="a") #add the new text files to the data.txt file
# f2.write("\nhello anjal")
# f2= open("data.txt")
# output= f2.read()
# print(output)
# f2.close()

# with open("data.txt")as f: #automatically close the opened file
#     f.read()
b=[]
name=input("enter the data: ")
b.append(name)
print(b)

with open("class/name.txt","a") as f:
    f.write(f"\n{name}")
# f1= open("data.txt", mode="a")
# f1.writelines(b)

# f2=open("data.txt")
# output = f2.read()
# print(output)

