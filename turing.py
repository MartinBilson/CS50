#rewrite the algorithm
# x = ['www.a.com', 'www.b.com', 'www.c.com']
# y = []

# for i in x:
#     y.append(i.split('.')[1] + '.' + i.split('.')[2])
# print(y)
#Functions that takes a number and square it
def square(x):    
    return x * x

for i in range(100):
    print(f"The square of {i} is {square(i)}")