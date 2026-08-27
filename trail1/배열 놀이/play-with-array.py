n,q = map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    qst=list(map(int,input().split()))
    if qst[0]==1:
        a=qst[1]-1
        print(arr[a])
    elif qst[0]==2:
        if qst[1] in arr:
            print(arr.index(qst[1])+1)
        else:
            print(0)
    else:
        for j in range(qst[1]-1,qst[2]):
            print(arr[j], end=' ')
        print()