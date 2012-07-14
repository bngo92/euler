
primes = prime(100000)
bf = 0
cf = 0
n = 0
for b in xrange(-999, 1000):
    for c in xrange(-999, 1000):
        x = 0
        while x**2 + b*x + c in primes:
            x += 1
        if x > n:
            bf = b
            cf = c
            n = x
print bf*cf
