n = int(input("What is the limit? "))
amount = 0
add = 0
for i in range(0, n+1):
    add = i/(i+1)
    amount += add
    add = 0

print(amount)