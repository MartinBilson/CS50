# x = int(input("What is x? "))
# y = int(input("What is y? "))

# print(x+y)
# x = float(input("Enter your number "))
# y = float(input("Enter your number "))

# z = round(x +y)

# #A string formatter
# print(f" {z:,}") 

# #TESTING STEP 2
# #I want to keep the entire domain including the '.com'
# x = ['www.a.com', 'www.b.com', 'www.c.com']
# y = []

# for i in x:
#     y.append(i.split('.')[1] + '.' + i.split('.')[2])
# print(y)
  
# #FUNCTIONS
# #Define a function hello, parameter hello and assign value
# def hello(to = "World"):
#     print("Hello ", to)

# #user to enter his name and call the function
# name = input("What is your full names: ")
# hello(name)

# #def main func, variable x and ask input and return its square
# def main():
#     x = int(input("Enter the value of x: "))
#     print("X squared is: ", square(x))

# def square(n):
#     return n **2

# main()

# #CONDITIONAL STATEMENTS
# #if statements
# x = int(input("whats x value: "))
# y = int(input("Whats y value: "))

# if x < y:
#     print(f"x value of {x} is less than y value of {y}")
# if x > y:
#     print(f"x value of {x} is greater than y value of {y}")
# if x == y:
#     print(f"x value of {x} is equal to y value of {y}")

# #Conditional statements (else if)
# #student marks
# score = int(input("Whats your score?:"))

# if score >= 90 and score <=100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# #Determine if the number is even and odd
# def main():
#     x = int(input("What is the value x: "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
        
# main()

# FUNCTIONS IN PYTHON that takes a number and return its square
#Example 1 how to execute it
def square(x):
    return x * x

for i in range(30):
    print(f"The square of {i} is {square(i)}")  

#Example 2 how to execute it
from function import square

for i in range(10):
    print(f"The square if {i} is {square(i)}")