n=int(input())
cl, co, ba=0,0,0
for i in range(1, n+1):
    if i%2==0 and i%3!=0 and i%12!=0:
        cl+=1
    if i%3==0 and i%12!=0:
        co+=1
    if i%12==0:
        ba+=1
print(cl, co, ba)