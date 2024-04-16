x=[('a','b'),('c','d')]

with open('x.txt', 'w') as f:
    f.write(str(x))

with open('x.txt', 'r') as f:
    y=f.read()
xy=eval(y)
print(xy)