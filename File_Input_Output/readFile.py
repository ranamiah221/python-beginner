# text = input("Enter Your text: ")
# f=open("C:\projects\python beginner\File_Input_Output\demo.txt","a")
# f.write(text)
# f.close()

# file=open("C:\projects\python beginner\File_Input_Output\demo.txt","r")
# data = file.read()
# print(data)
# f.close()
with open("simple.txt","w") as f:
    f.write('Hi everyone\nwe are learning I/O \n')
    f.write('using Java\nI like programming in Java')
with open("simple.txt","r") as f:
    data=(f.read())
newData = data.replace("Java", "Python")
with open("simple.txt","w") as f:
     f.write(newData)

