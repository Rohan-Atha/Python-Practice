#•  Take a number as input and check whether it is even or odd.
a=int(input("Enter a number:"))
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")
#•  Take marks as input and print a grade using if-elif-else. Define your own grade ranges.
marks=int(input("Enter marks:"))
if marks>=90:
    print("Your grade is A")
elif 90>marks>=80:
    print("Your grade is B")
elif 80>marks>=70:
    print("Your grade is C")
elif 70>marks>=60:
    print("Your grade is D")
elif 60>marks>=50:
    print("Your grade is E")
else:
    print("Your grade is F")
#•  Check whether a year entered by the user is a leap year.
year=int(input("Enter a year:"))
if year%4==0:
    print("Year is leap year")
else:
    print("Year is not leap year")
#•  Create a simple calculator that supports addition, subtraction, multiplication and division.
A=int(input("Enter a number:"))
B=int(input("Enter another number:"))
O=input("Enter operation(+,-,*,/)")
if O=="+":
    print("Addition of ",A," and ",B," is ",A+B)
elif O=="-":
    print("Subtraction of ",A," and ",B," is ",A-B)
elif O=="*":
    print("Multiplication of ",A," and ",B," is ",A*B)
elif O=="/":
    if B==0:
        print("Zero division not possible")
    else:
        print("Division of ",A," and ",B," is ",A/B)
else:
    print("Operation not supported")
