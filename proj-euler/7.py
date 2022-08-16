# Problem 7

# 1. starting from 2, count infinitely
# 2. if number is prime, increment cnt
# 3. if cnt reaches nth number, return number

import itertools

def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    cnt = 0
    for i in itertools.count(2):
        if is_prime(i):
            cnt += 1
            if cnt == n:
                break
    return i

print(nth_prime(6))