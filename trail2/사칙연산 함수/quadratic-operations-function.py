a, o, c = input().split()
a = int(a)
c = int(c)

def o_is(o):
    if o=='+' or o=='-' or o=='/' or o=='*':
        return True
    else:
        return False
    
def calculator(a,o,c):
    if o=='+':
        print(f'{a} + {c} = {a+c}')
    elif o=='-':
        print(f'{a} - {c} = {a-c}')
    elif o=='*':
        print(f'{a} * {c} = {a*c}')
    else:
        print(f'{a} / {c} = {int(a/c)}')

if o_is(o):
    calculator(a,o,c)
else:
    print('False')