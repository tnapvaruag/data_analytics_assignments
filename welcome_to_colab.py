# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

#Python Practical Questions and Sollutions

#Q1 print Hello, World!

print("Hello, World!")

#Q2 program to displays your name and age

n = input("Enter your name: ")
a = input("Enter your age: ")
print("Your name is", n, "and your age is", a)

#Q3 keyword list

import keyword
print(keyword.kwlist)

#Q4 check a word ias a Python keyword

import keyword
w = input("Enter a word: ")
if keyword.iskeyword(w):
    print(w, "is a Python keyword.")
else:
    print(w, "is not a Python keyword.")

#Q5 check mutability

x=["ram", 2, 5] #a list
y=(3,4,6) # a tuple

x[0]=1
print(x)
y[0]=1
print(y)

# Q6- Q7 function to demonstrate behaviour of mutable and immutable arguments.
''' the solution to previous question does the same

List is mutable data type whereas tuple is immutable data type.
'''

# Q8 program to demonstrate use of logical operators

x=4
y=5
if x%2==0 and y%2!=0: #and is logical operators used for combining conditional statement
    print("x is even and y is odd")

else:
  print("x is odd and y is even")

#9 program to convert user input from string to integer; fload, and boolean types
x=input("Enter a number: ")
print(type(x))
print(int(x))
print(float(x))
print(bool(x))

#10 type casting with list elements

x=[4,5,6]
print(type(x[0]))
x[0]=str(x[0])
print(type(x[0]))

# Q11 to check if a number is positive negative or zero

x=int(input("Enter a number: "))
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")

# Q12 for loop to print numbers from 1 to 10

for i in range(1,11):
    print(i)

# Q13 program to find sum of all even number between 1 and 50

sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print(sum)

# Q14 program to reverse a string using a while loop

s=input("Enter a string: ")
i=len(s)-1
while i>=0:
    print(s[i], end="")
    i-=1

#Q15 program to calculate the factorial fo a number provided by the user using while loop

n=int(input("Enter a number: "))
fact=1
while n>0:
    fact*=n
    n-=1
print(fact)