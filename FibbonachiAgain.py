num = [1, 1]
w = int(input("What digit of the Fibbonachi sequence do you want? "))

for i in range(0, w-2):
    num.append(num[-2] + num[-1])
print(num[len(num)-1])