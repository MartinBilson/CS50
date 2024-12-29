#rewrite the algorithm
x = ['www.a.com', 'www.b.com', 'www.c.com']
y = []

for i in x:
    y.append(i.split('.')[1] + '.' + i.split('.')[2])
print(y)
