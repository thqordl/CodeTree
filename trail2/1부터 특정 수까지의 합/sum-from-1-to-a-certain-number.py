n = int(input())

def hap(n):
    h=0
    res=0
    for i in range(1,n+1):
        h+=i
    res=h//10
    return res
print(hap(n))