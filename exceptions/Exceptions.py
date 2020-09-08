T = int(input())
for _ in range(T):
    try:
        a,b = map(int,input().split())
        c = a//b
        print(c)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code:",e)
