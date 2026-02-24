#print("Hello, world!")
'''
name = input("Enter your name:")
age = int((input("Enter your age:")))
city = input("Enter the city:")
print(name, age, city)

x=int(input("enter a number:"))
print(x)

#Write a program to take two numbers and print them on the same line
a =int(input("Enter a number:"))
b = int(input("Enter another number:"))
print(a, end= ' ')
print(b)


#Write a program to print a number using end=" "
a = int(input("enter a number:"))
b = int(input("enter another number:"))
print(a, end=' ')
print(b)
print(type(a))
print(type(b))

#Write a program to store two numbers in variables and print their sum
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = x + y
print("THE SUM IS:", z)

#Write a program to swap two numbers using a temporary variable
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))  
temp = a
a = b
b = temp
print("After swapping:", end = ' ')
print("First number:", a)
print("Second number:", b)

#Write a program to swap two numbers without using a temporary variable
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))  
a,b = b,a
print("After swapping:")
print("First number:", a)
print("Second number:", b)

#Write a program to store your name and age and print them
name = input("Enter your name:")
age  = int(input("Enter your age:"))
print("name:",name, end=' ')
print("age:", age)

#Write a program to assign one value to multiple variables
a = b = c = d = 10
print(a, b, c, d)

#Write a program to add two numbers
#Write a program to subtract two numbers
#Write a program to multiply two numbers
#Write a program to divide two numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a/b
print(c)

#Write a program to take two numbers and print their quotient and remainder
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = x%y
q = x//y
print("Quotient:", q)
print("Remainder:", z)

#Write a program to calculate power of a number
x = int(input("enter an number:"))
y = int(input("enter the power:"))
z = x**y
print("Power of the number is:", z)

#Write a program to find area of a rectangle
l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
a = l*b
print("Area of the rectangle is:", a)

#Write a program to find area of a circle
r = float(input("Enter the radius value:"))
a = 3.14*r*r
print("Area of the circle:", a)

#Write a program to find circumference of a circle
r = float(input("Enter the radius value:"))
c = 2*3.14*r
print("Circumference of the circle:", c)

#Write a program to convert Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius:"))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

#Write a program to convert Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit:"))
c = (f - 32) * 5/9 
print("Temperature in Celsius:", c)

#Write a program to check if two numbers are equal
x = int(input("Enter the number:"))
y = int(input("Enter another number:"))
if x==y:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

#Write a program to check which number is greater
x = int(input("Enter the number:"))
y = int(input("Enter another number:"))
if x>y:
    print("First number is greater")
else:
    print("Second number is greater")


#Write a program to find the smallest of three numbers
x = int(input("Enter first number:"))   
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))
if x<y and x<z: 
    print("First number is smallest")
elif y<x and y<z:
    print("Second number is smallest")
else:
    print("Third number is smallest")

#Write a program to check if a number is less than 100
x = int(input("Enter a number:"))
if x<100:
    print("Number is less than 100")
else:
    print("Number is not less than 100")

#Write a program to check if a number is greater than or equal to 50
x = int(input("Enter a number:"))
if x>=50:
    print("Number is greater than or equal to 50")
else:
    print("Number is less than 50")

#Write a program to compare two numbers and print the result
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
if x > y :
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("x and y are equal:")

#Write a program to check if a number is between 10 and 50
x = int(input("Enter a number:"))
if 10 < x < 50:
    print("Number is between 10 and 50")
else:
    print("Number is not between 10 and 50")

#Write a program to check if a number is positive and even
x = int(input("enter a number:"))
if x % 2 == 0 and x>0:
    print("Even and positive")
else :
    print("Not even and positive")

#Write a program to check if a number is negative or odd
x = int(input("Enter a number:"))
if x < 0 or x % 2 != 0:
    print("Number is negative or odd")
else:
    print("Number is not negative and not odd")
    
 #Write a program to use the not operator
a,b = 10,20
print(not(a>b))

a = int(input("Enter a number:"))
if not(a>0):
    print("Number is not positive")
else:
    print("Number is positive")
    
#divisible by 3 and 5
x = int(input("enter a value:"))
if x%3==0 and x%5==0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")
    
#Write a program to demonstrate += operator
#Write a program to demonstrate -= operator
#Write a program to demonstrate *= operator
#Write a program to demonstrate /= operator
a = 10
a += 5  
print(a)
a = 10
a -=5
print(a)
a = 10
a *= 5
print(a)
a = 10
a /= 5
print(a)
#Write a program to demonstrate %= operator
a = 10
a %= 3
print(a)

#Write a program to perform bitwise AND operation
x = 20
y = 15
z = x&y
print(f"{z}")
print((bin(z)))

#Write a program to perform bitwise OR
x = 20 
y = 15
print(x|y) 
print(bin(x|y))
#Write a program to perform bitwise NOT
x = 20
y = ~x
print(y)
print(bin(y))

#Write a program to perform bitwise XOR 
x = 20
y = 16
z = x ^ y

print(z)
print(bin(z))

#Write a program to perform left shift operation
x =5
print(bin(x))
y= x>>2
print(y)
print(bin(y))

x = 10
print(bin(x))
y = x<<1
print(y)
print(bin(y))

#Write a program to check if a value exists in a list
a = [10,20,30,40,50]
x = int(input("enter a number:"))
if x in a :
    print("Value exists in the list")
else:
    print("Value does not exist in the list")
    
"OR"
a = [10,20,30,40,50]
print(20 in a)
print(60 in a)

#Write a program to check if a character exists in a string
x = input("Enter a string:")
y = input("Enter a character to search:")
if y in x:
    print("Character exist in the string")
else:
    print("Character does not exist in the string")

#Write a program to use not in operator
x = input("Enter a string:")
y = input("Enter a character to search:")
if y not in x:
    print("Character doesn't exist")
else:
    print("Character exists")
    "OR"
    x = [10,20,30,40,50]
    print(60 not in x)

#Write a program to check if two variables refer to the same object
a = [10,20,30]
b = [10,20,30]
if a is b:
    print("The list B is equal to list A")
else:
    print("Not equal")

#Write a program to check if two variables refer to the same object
x=input("enter a name:")
y=input("enter a another name:")
if x is y:
    print("x is equal")
else:
    print("not equal")
 
 #Write a program to use is not operator
a = input("Enter first value: ")
b = input("Enter second value: ")

if a is not b:
    print("Both variables do NOT refer to the same object")
else:
    print("Both variables refer to the same object")
    
#Write a program using arithmetic + relational operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operations
add = a + b
sub = a - b
mul = a * b

# Relational operations
print("Is addition greater than subtraction?", add > sub)
print("Is multiplication equal to addition?", mul == add)
print("Is a less than b?", a < b)
print("Is a greater than or equal to b?", a >= b)
print("Is a not equal to b?", a != b)

#Write a program using logical + relational operators
a = int(input("enter the value: "))
b = int(input("enter another value: "))
print(a>b and b!=0)
print(a>b or a!=b)
print(a is not b)

#Write a program using assignment + arithmetic operators
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
x+= 5
y-= 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)

a = [10,20][20<10]
print(a)

#Write a program to find the largest of three numbers using operators
a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = int(input("enter third value: "))
if a>b>c:
    print("a is largest number")
elif a<b>c:
    print("b is the largest number")
else:
    print("c is the largest number")
    '''