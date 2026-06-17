num = int(input("Enter a number: ")) 
factors = []
for i in range(1, num+1):
    if num % i == 0:
        bob = str(i)+'x'+str(int((num/i)))
        factors.append(bob)

for b in factors:
    print(b)