n=int(input())
arr=list(map(int,input().split()))
even=[]
for a in arr:
    if a%2==0:
        even.append(a)

for e in even[::-1]:
    print(e, end=' ')