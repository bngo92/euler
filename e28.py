n = 1
sum = 1

i = 3
while i <= 1001:#1001
    for x in range(4):
        n += i-1
        sum += n
    i += 2
print sum
