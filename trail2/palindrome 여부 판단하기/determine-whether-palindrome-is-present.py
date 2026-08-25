A = input()

def reverse(A):
    for i in range(len(A)):
        if A[i] != A[len(A)-i-1]:
            return False
    return True

if reverse(A):
    print('Yes')
else:
    print('No')