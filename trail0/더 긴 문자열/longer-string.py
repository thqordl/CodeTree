words = input().split()
a = words[0]
b = words[1]

if len(a)> len(b):
    print(a, end=' ')
    print(len(a))
elif len(b)> len(a):
    print(b, end=' ')
    print(len(b))
else:
    print('same')