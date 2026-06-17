nums = []
for i in range(0, 3001):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(i)
print(nums)