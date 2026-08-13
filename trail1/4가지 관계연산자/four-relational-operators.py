a,b = map(int, input().split())
cases=[a>=b, a>b, b>=a, b>a]
for c in cases:
    if c is True:
        print(1)
    else:
        print(0)