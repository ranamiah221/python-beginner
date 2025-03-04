marks=int(input("Enter your marks: "))
if(marks >= 90):
    Grade= "A"
elif(marks >= 80 and marks < 90):
    Grade= "B"
elif(marks >= 70 and marks < 80):
    Grade= "C"
elif(marks < 70):
    Grade= "D"
print("grade of the student -> ", Grade)