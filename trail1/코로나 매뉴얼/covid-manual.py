p1, t1 = input().split()
p2, t2 = input().split()
p3, t3 = input().split()

if p1=='Y' and int(t1)>=37:
    if p2=='Y' and int(t2)>=37 or p3=='Y' and int(t3)>=37:
        print('E')
    else:
        print('N')
else:
    if (p2=='Y' and int(t2)>=37) and (p3=='Y' and int(t3)>=37):
        print('E')
    else:
        print('N')