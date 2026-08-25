n=int(input())
for i in range(n):
    for j in range(n):
        if (i+j+2)%4==0:
            print(f'({i+1}, {j+1})', end='\n')
        else:
            print(f'({i+1}, {j+1})', end=' ')