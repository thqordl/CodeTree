n = int(input())
i=1
while i<=n:
    d=i//10
    r=i%10
    if i%3==0 or (d!=0 and d%3==0) or (r!=0 and r%3==0):
        print(0, end=' ')
    else:
        print(i, end=' ')
    i+=1