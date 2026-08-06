matrix = [list(map(int, input().split())) for i in range(4)]
hap = 0

for i in range(4):
    for j in range(4):
        if i<j:
            break
        hap+=matrix[i][j]
print(hap)