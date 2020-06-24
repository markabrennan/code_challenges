"""
Leet Code April Daily Challenge:
Best Time to Buy and Sell Stock II
"""

def get_best(txns):
    sorted_txns = sorted(txns, key=lambda x: x['profit'], reverse=True)
    max_profit = 0
    i = 0
    end = len(sorted_txns)
    while i < end:
        best = sorted_txns[i]
        best_profit = best['profit']
        best_start, best_end = best['pos']
        j = i + 1
        while j < end:
            cur = sorted_txns[j]
            cur_profit = cur['profit']
            cur_start, cur_end = cur['pos']
            if cur_start > best_end:
                max_profit = max(max_profit, best_profit+cur_profit)
            elif cur_end < best_start:
                max_profit = max(max_profit, best_profit+cur_profit)
            j += 1
        max_profit = max(max_profit, best_profit)
        i += 1

    return max_profit


def brute_force(prices):
    transactions = []
    prev_elem = 0
    prev_pos = 0
    i = 0
    end = len(prices) - 1
    j = 0
    while i <= end:
        print(f'pos: {i}')
        prev_elem = prices[i]
        prev_pos = i
        print(f'elem: {prev_elem} | i: {i}')
        j = i+1
        while j <= end:
            next_elem= prices[j]
            if next_elem > prev_elem:
                print(f'next_elem: {next_elem} | prev_elem: {prev_elem} | j: {j}')
                transactions.append(dict(profit=next_elem-prev_elem, buy_sell=(prev_elem,next_elem), pos=(prev_pos,j)))
            j += 1
        i += 1
        
    return get_best(transactions)


"""
Python solution from comments
"""
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        print(f'prices[{i}]: {prices[i]} | prices[{i-1}] | {prices[i-1]} | new max: {max(prices[i]-prices[i-1], 0)}')
        profit += max(prices[i]-prices[i-1], 0)
    return profit    


"""
TEST CASES
"""

stocks =  [7,1,5,3,6,4]
"""
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""

#stocks = [1,2,3,4,5]
"""
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
"""

#stocks =  [7,6,4,3,1]
"""
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

#stocks = [6,1,3,2,4,7]  # expected result:  7

#stocks = [3,3,5,0,0,3,1,4]  #expected result:  8

print(maxProfit(stocks))

