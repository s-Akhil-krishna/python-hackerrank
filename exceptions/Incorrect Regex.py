import re
N = int(input())
for _ in range(N):
    res = True
    try:
        x = input()
        re.compile(x)
    except re.error:
        res = False
    print(res)