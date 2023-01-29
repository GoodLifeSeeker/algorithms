"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.
When your friend makes a guess, you provide a hint with the following info:

- The number of "bulls", which are digits in the guess that are in the correct
position.
- The number of "cows", which are digits in the guess that are in your secret
number but are located in the wrong position. Specifically, the non-bull digits
in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint
for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is
the number of cows. Note that both secret and guess may contain duplicate
digits.

- 1 <= secret.length, guess.length <= 1000
- secret.length == guess.length
- secret and guess consist of digits only.
"""
from typing import Dict, List


def getHint(secret: str, guess: str) -> str:
    """Description: we need to create a dict for each digit, where
    digit is a key. Value is a list with 3 items: 
    - value[0] - How many times we met the digit in secret (possible cows and
    bulls),
    - value[1] - How many times we met the digit in guess (possible cows
    and bulls),
    - value[2] - How many times we guess the digit on its place (definetly
    bulls),

    After creating the dict, we run through its values and add value[2] to
    'amount_a'.

    If we found a cow then it's not a abcd, so we decrease value[1] by amount
    of found bulls.
    Then we decrease value[0] by amount of found bulls too, because we have
    uncovered some of them.

    Player can't guess cows more than there are left in value[0],
    so if value[0] < value[1], the player guessed all the possible cows and
    it's value[0].

    On the other hand the player can't guess cows more than he/she tried to
    guess, so if value[0] > value[1], the player guessed all called cows.

    In other words we have to find min value between value[0] and value[1],
    which are decreased by amount of bulls.
    """
    amount_a: int = 0
    amount_b: int = 0
    counts: Dict[str: List[int]] = {}
    
    for i in range(len(secret)):
        if secret[i] not in counts.keys():
            counts[secret[i]] = [1, 0, 0]
        else:
            counts[secret[i]][0] += 1

        if secret[i] == guess[i]:
            counts[secret[i]][2] += 1

        if guess[i] not in counts.keys():
            counts[guess[i]] = [0, 1, 0]
        else:
            counts[guess[i]][1] += 1
    for x in counts.values():
        amount_a += x[2]
        amount_b += min(x[0] - x[2], x[1] - x[2])
    return f'{amount_a}A{amount_b}B'



secret1 = '1807'
guess1 = '7810'

print(getHint(secret1, guess1))

secret2 = '1123'
guess2 = '0111'

print(getHint(secret2, guess2))
