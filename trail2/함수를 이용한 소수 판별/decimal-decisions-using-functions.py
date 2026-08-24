a, b = map(int, input().split())

def is_prime(i):
    for j in range(2, i):
        if i%j==0:
            return False
    return True

cnt=0
for i in range(a, b+1):
    if is_prime(i):
        cnt+=i
print(cnt)