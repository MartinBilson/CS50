# x = int(input("What is x? "))
# y = int(input("What is y? "))

# print(x+y)

# x = float(input("Enter your number "))
# y = float(input("Enter your number "))

# z = round(x +y)

# #A string formatter
# print(f" {z:,}") 

#TESTING STEP 2
x = ['www.a.com', 'www.b.com', 'www.c.com']
y = []

for i in x:
    y.append(i.split('.')[1] + '.' + i.split('.')[2])
print(y)