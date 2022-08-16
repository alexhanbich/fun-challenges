# Problem 1

# 1. if num divides 3 or 5, add num to total
def mult_of_3_or_5(num):
    total = 0
    for i in range(num):
        if i%3 == 0 or i%5 == 0:
            total += i
    return total

print(mult_of_3_or_5(1000))