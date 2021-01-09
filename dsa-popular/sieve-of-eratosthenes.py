from time import time

def generatePrimesUsingSieve(n):
    
    # O(n*log(log(n))) i.e. faster than n*logn but slower than n
    
    multiples = set()

    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            for j in range(i**2, n + 1, i):
                multiples.add(j)

def generatePrimesUsingBruteForce(n):

    for i in range(2, n + 1):
        for j in range(2, int(i**0.5) + 1): # slight optimisation to O(n*root(n))
            if i % j == 0:
                break
        else:
            yield i

N = 10 ** 6
t1 = time()
list(generatePrimesUsingBruteForce(N))
t2 = time()
list(generatePrimesUsingSieve(N))
t3 = time()

print(f'Brute Force: {t2 - t1}')
print(f'Sieve: {t3 - t2}')