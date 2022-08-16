# Problem 4

# 1. find smallest n digit num, and highest digit num
# 2. find product of every pair in between two num
# 3. pick the max value of product which is a palindrome

def is_num_palindrome(num):
    # reverse the number
    original_num = num
    reversed_num = 0
    while num > 0:
        r = num % 10
        reversed_num = reversed_num * 10 + r
        num = num // 10
    return original_num == reversed_num

def largest_palindrome(n):
    # smallest n digit number
    low_thresh = pow(10, n) // 10
    # largest n digit number
    high_thresh = pow(10, n) - 1
    max_product = 0
    # find product of every pair in between [low_thresh, high_thresh]
    # and check if it is a palindrome
    for high in range(high_thresh, low_thresh-1, -1):
        for low in range(high, low_thresh-1, -1):
            product = low * high
            if product < max_product:
                break
            if is_num_palindrome(product):
                max_product = product
    return max_product

print(largest_palindrome(3))