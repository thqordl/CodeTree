M, D = map(int, input().split())

def check_md(M,D):
    if M>12:
        return False
    elif M>7:
        if M%2==0:
            if D<=31:
                return True
            else:
                return False
        else:
            if D<=30:
                return True
            else:
                return False
    else:
        if M%2==0:
            if M==2:
                if D<=28:
                    return True
                else:
                    return False
            else:
                if D<=30:
                    return True
                else:
                    return False
        else:
            if D<=31:
                return True
            else:
                return False

if check_md(M,D):
    print('Yes')
else:
    print('No')