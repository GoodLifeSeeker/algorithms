'''You are given a string number representing a positive integer and a
character digit.

Return the resulting string after removing exactly one occurrence of digit
from number such that the value of the resulting string in decimal form is
maximized. The test cases are generated such that digit occurs at least once
in number.

Constraints:
2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number.
'''
from typing import List


def removeDigit(number: str, digit: str) -> str:
    '''Func name was taken from the task.'''
    new_number: List[str] = []
    for i in range(len(number)):
        if number[i] == digit:
            if i == 0:
                new_number.append(number[i+1:])
            elif i == len(number) - 1:
                new_number.append(number[:i])
            else:
                new_number.append(number[:i] + number[i+1:])
    max_value = max(map(int, new_number))
    return str(max_value)

print(removeDigit('123', '3'))  # 12
print(removeDigit('1231', '1'))  # 231
print(removeDigit('551', '5'))  # 51
print(removeDigit('133235', '3'))  # 13325