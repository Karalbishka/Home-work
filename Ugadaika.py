L=1
R=100
s=0
d=(L+R)//2
while s!=1:
    print('Твоё число равно, меньше или больше, чем число',d,'?')
    s=int(input())
    if s == 1:
        print('твое число', d)
    elif s == 2:
        L = d+1
        d = (L+R)//2
    elif s == 3:
        R = d-1
        d = (L + R)//2