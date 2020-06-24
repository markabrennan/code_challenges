"""
Classic greedy search problem
from Interview Cake

Three Versions - third one is from Interview Cake
"""

def gf3(l):
    mn = l[0]
    mx = None
    for i in range(1, len(l)):
        cur = l[i]
        if mx is None:
            mx = cur - mn
        else:
            mx = max(cur-mn, mx)
        mn = min(cur, mn)
    return mx


def gf2(l):
    if len(l) < 2:
        return 0
    print(f'l: {l}')
    prev = l[0]
    cur = l[1]
    mx = cur - prev
    for i in range(2, len(l)):
        cur = l[i] 
        print(f'cur: {cur} | prev: {prev} | mx: {mx} | cur-prev: {cur-prev}') 
        if cur > prev:
            mx = max(mx, cur-prev)
        else:
            prev = cur
    return mx


    def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit


# test cases
p1 = [10, 7, 5, 8, 11, 9]
p2 = [10, 7, 5, 8, 11, 9, 2]
p3 = [9, 7, 4, 1]

