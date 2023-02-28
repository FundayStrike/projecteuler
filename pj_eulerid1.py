total_mul = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total_mul += 1

print(total_mul)