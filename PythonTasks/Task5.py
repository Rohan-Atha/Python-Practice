#. Store five subject names in a list and display them one by one.
A=['English', 'Physics', 'Mathematics', 'Computer science', 'Chemistry']
for i in A:
    print("Subject:",i)
#• Take 5 marks as input and calculate the total, average, highest and lowest marks.
L=[]
for i in range(5):
    a= int(input("Enter a number:"))
    L.append(a)
print("Total marks is",sum(L))
print("Average marks is",sum(L)/5)
print("Highest marks :",max(L))
print("Lowest marks :", min(L))
#•Create a dictionary containing a student's name, roll number and marks.
D={}
N=int(input("Enter number of students:"))
for i in range(N):
    roll=int(input("Enter roll no.:"))
    name=input("Enter name:")
    marks=int(input("Entre marks:"))
    D[roll]=(name,marks)
for i in D:
    print(i,":",(D[i][0],D[i][1]))
#•Search for a name in a list and display whether it exists.
B=["ABC","XYZ","LMN","PQR","UVW"]
n=input("Enter for a name in a list:")
if n in B:
    print(n,"Exists in",B)
else:
    print(n,"does not exist in",B)
#•Count how many times each character appears in a string.
s=input("Enter a string:")
L=[]
for i in s:
    if i not in L:
        L.append(i)
for i in s:
    c=0
    for j in s:
        if (i is j) and (i in L):
            c=c+1
    try:
        L.remove(i)
    except:
        continue

    print(i,"presents ",c,"times in ",s)
