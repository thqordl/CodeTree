n = int(input())
x=0
while True:
    if n%2!=0:
        break
    n=n//2
    x+=1
print(x)