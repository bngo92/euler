import math

def factors1(n):
    sq = math.sqrt(n)
    l1 = [x for x in range(1, int(sq)+1) if n % x == 0]
    l2 = [n / x for x in l1 if x != 1 and x != sq]
    return l1 + l2

def factors2(n):
    return filter(lambda x: n % x == 0, range(1, n/2+1))

abundant = set(x for x in xrange(1, 20161+1) if sum(factors1(x)) > x)
sum = 0
for x in xrange(1, 28123):
    b = True
    for y in abundant:
        if x - y in abundant:
            b = False
            break
    if b:
        sum += x
print sum
