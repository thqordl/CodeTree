arr = list(map(int, input().split()))
arodd=[]
areven=[]
for i in range(10):
    if i%2==0:
        arodd.append(arr[i])
    else:
        areven.append(arr[i])
if sum(arodd)>sum(areven):
    print(sum(arodd)-sum(areven))
else:
    print(sum(areven)-sum(arodd))