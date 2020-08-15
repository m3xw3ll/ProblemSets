

nums = [int(i) for i in input().split()]
out = []

for i in nums:
    count = 0
    for j in nums:
        if j != i and j < i:
            count +=1

    out.append(count)
print(out)