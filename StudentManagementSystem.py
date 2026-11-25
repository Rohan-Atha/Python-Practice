#Create a menu-driven Python program that allows a user to manage student records
#Your program should display a menu similar to this:
# 1. Add student
# 2. View all students
# 3. Search student by roll number
# 4. Calculate average marks
# 5. Exit
import csv
print("Welcome to Student Management System")
def menu():
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        try:
            roll=int(input("Enter roll number:"))
            name=input("Enter student name:")
            marks=int(input("Enter marks:"))
            L.append([roll,name,marks])
            f=open("student.xls","a")
            a=csv.writer(f)
            a.writerow(([roll,name,marks]))
            f.close()
            print("Student successfully added !!")
            menu()
        except:
            print("Invalid Input! Please try again:")
            menu()
    elif choice==2:
        print("Students details are:")
        f=open("student.xls","r")
        d=csv.reader(f)
        for i in d:
            if len(i)>1:
                print(i)
            else:
                continue
        f.close()
        menu()
    elif choice==3:
        s=0
        t=[]
        roll=int(input("Enter roll number:"))
        f=open("student.xls","r")
        d=csv.reader(f)
        for i in d:
            try:
                if roll==int(i[0]):
                    s=1
                    t=i
            except:
                continue
        if s==1:
            print("The Student Exists in the list ")
            print("Student Details:",t)
        else:
            print("The Student Doesn't Exist")
        f.close()
        menu()
    elif choice==4:
        try:
            s=0
            n=0
            f=open("student.xls","r")
            d=csv.reader(f)
            for i in d:
                try:
                    s=s+int(i[2])
                    n=n+1
                except:
                    continue
            print("Average marks are:",s/n)
            f.close()
            menu()
        except:
            print("Syntax Error! Please try again:")
            menu()
    elif choice==5:
        print("Thank you for using Student Management System")
        exit()
    else:
        print("Invalid Choice")
        menu()
L=[]
menu()