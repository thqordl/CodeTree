fruits = ['apple', 'banana', 'grape', 'blueberry', 'orange']
cnt = 0
n = input()

for fruit in fruits:
    if fruit[2]==n or fruit[3]==n:
        print(fruit)
        cnt +=1
print(cnt)
    