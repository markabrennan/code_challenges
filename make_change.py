"""
Interview Cake dynamic programming problem
"""

def change_possibilities_top_down(amount_left, denominations, current_index=0):

    # Base cases:
    # We hit the amount spot on. yes!
    if amount_left == 0:
        return 1

    # We overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0

    # We're out of denominations
    if current_index == len(denominations):
        return 0

    print("checking ways to make %i with %s" % (
        amount_left,
        denominations[current_index:],
    ))

    # Choose a current coin
    current_coin = denominations[current_index]

    # See how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(
            amount_left,
            denominations,
            current_index + 1,
        )
        amount_left -= current_coin

    return num_possibilities


print(change_possibilities_top_down(4, [1,2,3]))