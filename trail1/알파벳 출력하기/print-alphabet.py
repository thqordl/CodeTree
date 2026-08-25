n= int(input())
ch=65
for i in range(n):
    for j in range(i+1):
        print(chr(ch), end='')
        ch+=1
        if chr(ch)=='[':
            ch=65
    print()