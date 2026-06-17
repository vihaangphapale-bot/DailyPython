num = input("Please enter a number: ")
while not num.isdigit():
    num = input("Please enter a VALID number: ")
num = int(num)
total = 1
for i in range(1, num+1):
    total = total*i
print(total)