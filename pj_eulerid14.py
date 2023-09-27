memo = {1: 0}

def CollatzSteps(n):
    if n in memo:
        return memo[n]
    else:
        if n % 2 == 0:
            memo[n] = 1 + CollatzSteps(n//2)
        else:
            memo[n] = 1 + CollatzSteps(3*n+1)
        return memo[n]

max_step, max_num = -1, -1
for i in range(1, 1000001):
    memo[i] = CollatzSteps(i)
    if memo[i] > max_step:
        max_step, max_num = memo[i], i

print(max_num)
