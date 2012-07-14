def amicable(n):
    return sum(filter(lambda x: n%x == 0, range(1,n/2+1)))

if __name__ == "__main__":
    l = range(1,10000)
    res = []
    while l:
        x = l.pop()
        t = amicable(x)
        if x == amicable(t) and x != t:
            res.append(x)
            res.append(t)
            l.remove(t)
        
    #print res
    print sum(res)
