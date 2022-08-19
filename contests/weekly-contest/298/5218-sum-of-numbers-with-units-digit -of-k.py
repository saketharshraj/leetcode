# Given two integers num and k, consider a set of positive integers with the following properties:

# The units digit of each integer is k.
# The sum of the integers is num.
# Return the minimum possible size of such a set, or -1 if no such set exists.

# Note:

# The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
# The units digit of a number is the rightmost digit of the number.

# Input: num = 58, k = 9
# Output: 2
# Explanation:
# One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
# Another valid set is [19,39].
# It can be shown that 2 is the minimum possible size of a valid set.

# Input: num = 0, k = 7
# Output: 0
# Explanation: The sum of an empty set is considered 0.

def minimumNumbers(num: int, k: int) -> int:
    if num == 0:
        return 0
    if num < k:
        return -1
    if num == k:
        return 1

    for i in range(1, 3000):
        multiple = i*k
        if multiple > num:
            break
        if multiple % 10 == num % 10:
            return i
    return -1


print(minimumNumbers(37, 2))