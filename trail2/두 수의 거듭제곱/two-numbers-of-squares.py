a, b = map(int, input().split())

def prime(a,b):
    p=1
    for i in range(b):
        p*=a
    return p

print(prime(a,b))