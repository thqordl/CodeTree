a,b,c = map(int, input().split())
if a>=b and c>=b:
    print(b)
elif a>=b and b>=c:
    print(c)
elif b>=a and c>=a:
    print(a)
elif b>=a and a>=c:
    print(c)
elif c>=a and b>=a:
    print(a)
else:
    print(b)