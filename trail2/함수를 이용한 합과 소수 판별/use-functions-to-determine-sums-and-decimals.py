a, b = map(int, input().split())

def is_prime(i):
    for j in range(2,i):
        if i%j==0:
            return False
    return True

def is_even(i):
    a=i//10
    b=i%10
    if (a+b)%2==0:
        return True
    else:
        return False

cnt=0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        cnt+=1
print(cnt)