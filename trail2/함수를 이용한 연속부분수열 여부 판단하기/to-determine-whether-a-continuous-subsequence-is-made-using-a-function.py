n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_line(p):
    for i in range(n2):
        if a[p+i]!=b[i]:
            return False
    return True

answer = False
for i in range(n1-n2+1):
    if is_line(i):
        answer=True
        break
print('Yes' if answer else 'No')