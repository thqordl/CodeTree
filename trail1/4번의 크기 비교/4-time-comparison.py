a = int(input())
b,c,d,e = map(int, input().split())
cases=[b,c,d,e]
for c in cases:
    if a>c:
        print(1)
    else:
        print(0)