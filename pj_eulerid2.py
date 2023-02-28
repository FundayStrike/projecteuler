def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

lst = []

n = 1
while fib(n) <= 4000000:
    lst.append(fib(n))
    n += 1

print(sum(list(filter(lambda x: x%2==0, lst))))