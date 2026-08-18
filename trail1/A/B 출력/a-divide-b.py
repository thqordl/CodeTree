a, b = map(int, input().split())

print(f"{a//b}." , end='')
c = a%b
for i in range(20):
    print((10*c)//b, end='')
    c=(10*c)%b