#•  Print numbers from 1 to 100 using a loop.
for i in range(1,101):
    print(i)
#•  Print the multiplication table of a number entered by the user.
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"*",i,"=",i*num)
#•  Find the sum of all numbers from 1 to N.
N=int(input("Enter a number:"))
s=0
for i in range(1,N+1):
    s=s+i
print("Sum of numbers from 1 to",N,"is ",s)
#•  Count the vowels in a word entered by the user.
word=input("Enter a word:")
v=0
for i in word:
    if i in "AEIOUaeiou":
        v=v+1
print("Total vowels are:",v)
#•  Print all prime numbers between 1 and 100.
print("Prime numbers are:")
for i in range(1,101):
    f=0
    for j in range(2,i):
        if i%j==0:
            f=f+1
    if f==0:
        print(i,sep=",")