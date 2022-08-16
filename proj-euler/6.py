# Problem 6

# 1. find sum_of_square
# 2. find square_of_sum
# 3. return abs(difference)

def sum_square_difference(num):
    sum_of_square = 0
    for i in range(1, num+1):
        sum_of_square += i*i

    square_of_sum = 0
    for i in range(1, num+1):
        square_of_sum += i
    square_of_sum *= square_of_sum

    return abs(sum_of_square-square_of_sum)

print(sum_square_difference(100))