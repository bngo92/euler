def prime(n):
    s = []
    l = range(2, n)
    while l:
        x = l[0]
        s.append(x)
        l = [i for i in l if not i % x == 0]
    return s
