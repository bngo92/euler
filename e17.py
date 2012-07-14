def word(n):
    num = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
            8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
            13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
            17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
            30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
            80:'eighty',90:'ninety'}
    s = ''
    if n >= 1000:
        s += num[n/1000] + 'thousand'
        n -= n/1000*1000
        if n != 0:
            s += 'and'
    if n >= 100:
        s += num[n/100] + 'hundred'
        n -= n/100*100
        if n != 0:
            s += 'and'
    if n >= 20:
        s += num[n/10*10]
        n -= n/10*10
    if n in num:
        s += num[n]
    return s
    
n = 0
for x in range(1,1000+1):
    n += len(word(x))
print n
