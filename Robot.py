import math
y = 0
x = 0
u = input("How many feet do you want to go up? ")
while not u.isdigit():
    u = input("How many feet do you want to go up? ")
d = input("How many feet do you want to go down? ")
while not d.isdigit():
    d = input("How many feet do you want to go down? ")
l = input("How many feet do you want to go left? ")
while not l.isdigit():
    l = input("How many feet do you want to go left? ")
r = input("How many feet do you want to go right? ")
while not r.isdigit():
    r = input("How many feet do you want to go right? ")
u = int(u)
d = int(d)
l = int(l)
r = int(r)

y += u
y -= d
x += r
x -= l

distance = round(math.sqrt(x*x + y*y), 3)

print("You went", distance, "feet away from where you started.")