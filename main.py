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
  
# #function
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

#Conditional statements (questionning styles))
x = int(input("whats x value: "))
y = int(input("Whats y value: "))

if x < y:
    print(f"x value of {x} is less than y value of {y}")
else:
    print(f"x value of {x} is greater than y value of {y}")