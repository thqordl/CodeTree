a,b,c = map(int, input().split())
arr = [a,b,c]
avg = int(sum(arr)/len(arr))
print(sum(arr), avg, sum(arr)-avg, sep='\n')