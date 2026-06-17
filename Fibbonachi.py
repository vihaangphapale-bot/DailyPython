num = [1, 1]
w = int(input("How many digits of the sequence do you want? "))

for i in range(0, w-2):
    num.append(num[-2] + num[-1])
print(num)