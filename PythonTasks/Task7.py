#•  Write text to a file and then read it back.
f=open("student.txt","w")
N=int(input("Enter number of lines:"))
for i in range(N):
    s=input("Enter a line:")
    s=s+"\n"
    f.write(s)
f.close()
f=open("student.txt","r")
a= f.readlines()
for i in a:
    print(i)
f.close()
#•  Save a student's name and marks in a file, then display the saved data.
#•  Use try-except to handle invalid numeric input without crashing.
#•  Make sure your program handles a missing or empty data file.
D={}
N=int(input("Enter number of students:"))
for i in range(N):
    try:
        name=input("Enter student name:")
        marks=int(input("Enter student marks:"))
        D[name]=marks
    except:
        continue
f=open("std.txt","a")
for i in D:
    f.write(i)
    f.write(" : ")
    f.write(str(D[i]))
    f.write("\n")
f=open("std.txt","r")
a= f.readlines()
for i in a:
    print(i)
f.close()



