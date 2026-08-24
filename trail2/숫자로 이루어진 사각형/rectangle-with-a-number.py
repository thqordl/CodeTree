n = int(input())

def print_rec(n):
    cnt=0
    for i in range(n):
        for j in range(n):
            cnt+=1
            print(cnt, end=' ')
            if cnt==9:
                cnt=0
        print()

print_rec(n)