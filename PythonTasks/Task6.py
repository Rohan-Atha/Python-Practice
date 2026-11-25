#•  Write a function that returns the largest of three numbers.
def maximum(a,b,c):
    m=0
    L=[]
    L.append(a)
    L.append(b)
    L.append(c)
    for i in L:
        cm=i
        if cm>m:
            m=cm
    return m
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter a number:"))
print("Maximum number is ",maximum(a,b,c))
#•  Write a function to check whether a number is prime.
def prime(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f=f+1
    if x==1 or x==0:
        print("The number",x,"Is neither prime nor composite")
    else:
        if f==0:
            print("The number",x,"is a prime number")
        else:
            print("The number", x, "is not a prime number")
y=int(input("Enter a number to check if it is prime:"))
prime(y)
#•  Write a function that takes a list of marks and returns the average.
def avg(L):
    s=0
    for i in L:
        s=s+i
    print("The average is",s/len(L))
L=eval(input("Enter a list of numbers:"))
avg(L)
#•  Rewrite your calculator using separate functions for each operation.
def addition(a,b):
    print("Addition is:",a+b)
def subtraction(a,b):
    print("Subtraction:",a-b)
def multiplication(a,b):
    print("Multiplication:",a*b)
def division(a,b):
    if b==0:
        print("Zero division Error")
    else:
        print("Division :",a/b)
A=int(input("Enter a number:"))
B=int(input("Enter another number:"))
O=input("Enter operation(+,-,*,/):")
if O=="+":
    addition(A,B)
elif O=="-":
    subtraction(A,B)
elif O=="*":
    multiplication(A,B)
elif O=="/":
    division(A,B)
else:
    print("Invalid operation")