count = 0
t = 200
for a1 in range(t/200+1):
    t1 = t - 200 * a1
    for a2 in range(t1/100+1):
        t2 = t1 - 100 * a2
        for a3 in range(t2/50+1):
            t3 = t2 - 50 * a3
            for a4 in range(t3/20+1):
                t4 = t3 - 20 * a4
                for a5 in range(t4/10+1):
                    t5 = t4 - 10 * a5
                    for a6 in range(t5/5+1):
                        t6 = t5 - 5 * a6
                        for a7 in range(t6/2+1):
                            count += 1
print count
