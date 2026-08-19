n = int(input())
cnt=n-1
for i in range(2*n-1):
    for j in range(cnt):
        if i<(n-1):
            print(' ',end=' ')
        else:
            continue
    for j in range(n-cnt):
        print('@', end=' ')
    print()
    if i<(n-1):
        cnt-=1
    else:cnt+=1