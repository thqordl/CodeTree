n = int(input())
arr = list(map(int, input().split()))
doubled=[x**2 for x in arr]
for i in doubled:
    print(i, end=' ')