'''
You are given a positive integer n. Each digit of n has a sign according to
the following rules:

- The most significant digit is assigned a positive sign.
- Each other digit has an opposite sign to its adjacent digits.

Return the sum of all digits with their corresponding sign.

Constraints:

1 <= n <= 10**9
'''

def alternateDigitSum(n: int) -> int:
    flag = True
    result = 0
    for num in str(n):
        if flag:
            result += int(num)
            flag = False
        else:
            result -= int(num)
            flag = True
    return result

print(alternateDigitSum(886996))

