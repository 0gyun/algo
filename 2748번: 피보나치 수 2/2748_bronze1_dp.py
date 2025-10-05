import sys

input = sys.stdin.readline

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

def fibo(n):
    if n+1 <= len(fib):
        return fib[n]
    else:
        f = fibo(n-2) + fibo(n-1)
        fib.append(f)
        return fibo(n-2) + fibo(n-1)

n = int(input())
if n <= 17:
    print(fib[n])
else:
    print(fibo(n))