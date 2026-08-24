a, b = map(int, input().split())

def gugudan(i):
    while i>0:
        if i%10==3 or i%10==6 or i%10==9:
            return True
        i=i//10
    return False

def is_num(i):
    return i%3==0 or gugudan(i)

cnt=0
for i in range(a, b+1):
    if is_num(i):
        cnt+=1
print(cnt)