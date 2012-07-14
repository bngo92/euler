from prime import prime

def divide(a, b):
    s = ''
    while True:
        a *= 10
        x, y = divmod(a, b)
        s += str(x)
        if s == '0':
            s = ''
            continue
        if y == 0:
            return s
        if len(s) % 2 == 0 and s[:len(s)/2] == s[len(s)/2:]:
            return s[:len(s)/2]
        a = y

def e26():
    m = 0
    for x in prime(1000):
        s = len(divide(1, x))
        if s > m:
            m = s
            print x, m

e26()
