# Problem 2

# 1. use top-down dynamic programming to solve for fib
# 2. break when larger than thresh
# 3. add to total if even

def even_fib_num(thresh):
    total = 0
    # base case
    dp = [0, 1]
    i = 2
    while True:
        # recurrence relation
        # appends value at dp[i]
        dp.append(dp[i-1] + dp[i-2])
        if dp[i] > thresh:
            break
        if dp[i]%2 == 0:
            total += dp[i]
        i += 1
    return total

print(even_fib_num(4000000))