from tkinter import *

def Student():
    result = int(entry1.get()) + int(entry2.get()) + int(entry3.get())

    totText.set(result)

    percentage = (result/300)*100
    PerText.set(percentage)

    if (percentage > 90):
        grade = "A"
    elif(percentage<=90 and percentage>=80):
        grade = "B"
    elif(percentage<=80 and percentage>=70):
        grade = "C"
    elif(percentage<=70 and percentage>=60):
        grade = "D"
    elif(percentage<=60 and percentage>=50):
        grade = "E"
    else:
        grade="FAIL"
    gradeText.set(grade)

root = Tk()
root.title("Student Percentage Calculation System")
root.geometry("400x360")

Label(root,text="STUDENT PERCENTAGE AND GRADE CALCULATOR",font="impack 10 bold",bg="yellow").pack(fill="x")

Label(root, text="Python").place(x=10, y=30)
Label(root, text="DBMS").place(x=10, y=60)
Label(root, text="Web technology").place(x=10, y=90)
Label(root, text="Total:").place(x=10, y=120)
Label(root, text="Percentage:").place(x=10, y=150)
Label(root, text="Grade:").place(x=10, y=180)

totText = StringVar()
PerText = StringVar()
gradeText = StringVar()

entry1 = Entry(root,font="arial 15",width=15)
entry1.place(x=150, y=30)

entry2 = Entry(root,font="arial 15",width=15)
entry2.place(x=150, y=60)

entry3 = Entry(root,font="arial 15",width=15)
entry3.place(x=150, y=90)

result = Label(root, text="", textvariable=totText,font="arial 15",width=15).place(x=100, y=120)
percentage = Label(root, text="", textvariable=PerText,font="arial 15",width=15).place(x=100, y=150)
grade = Label(root, text="", textvariable=gradeText,font="arial 15",width=15).place(x=100, y=180)

Button(root, text="Calculate", command=Student ,bg="green",width=10).place(x=10, y=220)
Button(root,text="Exit",command=lambda:exit(),bg="red",width=10).place(x=250,y=220)

root.mainloop()