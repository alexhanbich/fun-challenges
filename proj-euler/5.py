# Problem 5

# 1. Smallest possible number that is divisible by set(numbers)
#    can be described as Least Common Multiple (LCM) of set(nubmbers)
# 2. find all prime factors in range [1, d]
# 3. find val = max(prime_factor^x < n)
#    ex. for prime factor 2, value = max(2^x < n),
#    = value = 2^3 < n
#    = 8
# 4. repeat for all prime factors
# 4. multiply all vals

def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def LCM(d):
    dict = {}
    for i in range(2, d+1):
        if is_prime(i):
            dict[i] = i

    total = 1
    for key in dict:
        val = 1
        while True:
            if val * key < d:
                val *= key
            else:
                break
        print(val)
        total *= val
    return total

print(LCM(20))
        
