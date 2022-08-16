# Problem 3

# Examples of numbers -> product of prime factors:
# 40 = 2^3 * 5
# 95 = 2 * 3^2 * 5
# 13195 = 5 * 7 * 13 * 29
# 63000 = 2^3 * 3^2 * 5^3 * 7

# composite property:
# every composite number has at least one prime factor less than or equal to square root of itself
 
# What the function does:
# removes lower prime factors until we have the largest factor
# 1. find factor range: [2, sqrt(n)] based on a composite property
# 2. go through the factors and divide by factor to remove the smaller factors
# 3. return the largest number

def largest_prime(n):
    if n < 2:
        return None
    # using trial divison
    f = 2
    # f*f <= n: max possible factor
    while f*f <= n:
        # if divisible by factor, keep dividing num by factor
        # if num == factor, num is the largest factor
        while n % f == 0 and n != f:
            n //= f
        f += 1
    return n

# test run for 40
# factor = 2
# 2^2 < 45
# 40 % 2 == 0 and 40 != 4
# 40 // 2 = 20
# 20 % 2 == 0 and 20 != 4
## 20 // 2 = 10
# 10 % 2 == 0 and 10 != 4
# 10 // 2 = 5
# 5 % 2 != 0, loop end
# factor += 1
# 3^2 > 5
# return n

print(largest_prime(6008514751430))