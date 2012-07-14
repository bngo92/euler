s = set()
for x in (x for x in xrange(1,9876) if len(str(x)) == len(set(str(x)))
            and '0' not in str(x)):
    for y in (y for y in xrange(1,9876) 
            if len(str(x)+str(y)+str(x*y)) ==
            len(set(str(x)+str(y)+str(x*y))) == 9
            and '0' not in str(y)
            and '0' not in str(x*y)
            ):
        s.add(x*y)
        
print sum(s), s
