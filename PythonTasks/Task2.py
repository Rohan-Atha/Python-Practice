#•  Create examples of int, float, string and boolean variables.
a=21
b=21.7
name="Rohan"
c= True
print("a is",type(a),"b is ",type(b),"name is",type(name),"c is",type(c))
#•  Convert a temperature from Celsius to Fahrenheit.
temp=float(input("enter temp in Celsius:"))
print("temp in celsius is",temp)
fahrenheit= (9/5)*temp + 32
print("temp in fahrenheit is",fahrenheit)
#•  Calculate the area and perimeter of a rectangle using user input.
print("Give inputs for rectangle length and width")
length= float(input("enter length in cm:"))
width= float(input("enter width in cm:"))
perimeter= 2*(length+width)
print("perimeter is ",perimeter)
area= length*width
print("area is ",area)
#•  Explore comparison and logical operators with simple examples.
A=int(input("Enter a number:"))
B=int(input("Enter another number:"))
print(A>B)
print(A<B)
print(A==B)
print(A!=B)
print(A and B)
print(A or B)
print(not A)
print(not B)