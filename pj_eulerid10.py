def generate_primes(n):
    sieve = [i for i in range(n+1)]
    sieve[0], sieve[1] = 0, 0
    for i in range(2, n+1):
        if sieve[i] != 0:
            for j in range(2*i, n+1, i):
                sieve[j] = 0
    return [num for num in sieve if num != 0]

print(sum(generate_primes(1999999)))
