Y, M, D = map(int, input().split())

def yoon(Y):
    return Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0)

def lastday(Y,M,D):
    if yoon(Y) and M==2:
        return 29
    else:
        if M==2:
            return 28
        elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
            return 31
        else:
            return 30

def daycheck(Y,M,D):
    if M < 1 or M > 12:
        return False
    if D < 1 or D > lastday(Y, M, D):
        return False
    else:
        return True

def what(M):
    if M>=3 and M<=5:
        return 'Spring'
    elif M>=6 and M<=8:
        return 'Summer'
    elif M>=9 and M<=11:
        return 'Fall'
    elif M<=2 or M==12:
        return 'Winter'

if daycheck(Y,M,D):
    print(what(M))
else:
    print(-1)