s = input()

first = s[:1]
middle = s[1:-1]
last = s[-1:]

if len(middle) >= 1:
    middle = 'a' + middle[1:]

if len(middle) >= 2:
    middle = middle[:-1] + 'a'

print(first + middle + last)