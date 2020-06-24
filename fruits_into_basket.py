"""
Educative Coding Pattern
https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
"""



def fruits_into_basket(fruits):
    basket = {}
    start = 0
    for fruit in fruits:
        if fruit not in basket and len(basket) < 2:
            basket[fruit] = 1
        elif fruit in basket and len(basket) <= 2:
            basket[fruit] += 1
        elif len(basket) == 2:
            prev_fruit = fruits[start]
            if prev_fruit in basket and basket[prev_fruit] == 1:
                del basket[prev_fruit]
            basket[fruit] = 1
            start += 1
    return sum(basket.values())


def fruits_into_basket2(fruits):
    basket = {}
    start = 0
    for fruit in fruits:
        cur_fruit = fruit
        if cur_fruit not in basket:
            basket[cur_fruit] = 1
        else:
            basket[cur_fruit] += 1
        while len(basket) > 2:
            prev_fruit = fruits[start]
            basket[prev_fruit] -= 1
            if basket[prev_fruit] == 0:
                del basket[prev_fruit]
            start += 1
    return sum(basket.values())


"""
TEST CASES
"""

"""
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
"""
#fruits = ['A', 'B', 'C', 'A', 'C']

"""
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""
fruits =['A', 'B', 'C', 'B', 'B', 'C']

print(fruits_into_basket2(fruits))