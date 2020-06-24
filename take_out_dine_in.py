"""
Interview Cake - greedy algorithm problem
"""


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    if len(served_orders) != len(take_out_orders) + len(dine_in_orders):
        return False
        
    i = 0
    j = 0

    for ord in served_orders:
        if i < len(take_out_orders) and ord == take_out_orders[i]:
            i += 1
        elif j < len(dine_in_orders) and ord == dine_in_orders[j]:
            j += 1
        else:
            return False

    if i < len(take_out_orders) or j < len(dine_in_orders):
        return False            
    return True