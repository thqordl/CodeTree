n = int(input())

def res(n):
    a=n//10
    b=n%10
    return n%2==0 and (a+b)%5==0

if res(n):
    print("Yes")
else:
    print("No")