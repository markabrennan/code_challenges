""" 
Interview Cake
"""
def mx(cakes, cap):
    if cap <= 0:
        return 0

    m = 0
    runval = 0
    runweight = 0
    left = 0
    new_runval = 0
    new_mult = 0
    new_left = 0

    for weight, val in cakes:
        # get the greater of: run val + new val * left mult
        # OR new val * new weight mult
        if weight > 0:
            new_runval = ((left // weight) * val) + runval
          
            new_mult, new_left = divmod(cap, weight)
        new_val = val * new_mult
        print(f'weight: {weight} | value: {val} | left: {left} | runval: {runval} | new_runval: {new_runval} | new_mult: {new_mult} | new_left: {new_left} | new_val: {new_val} | m: {m}')
        m = max(m, new_runval, new_val)
        print(f'm is now: {m}')

        left = new_left
        runval = m
        
    return m

"""
This is the latest version I did when trying to
solve this problem again; it is similar to the mx()
function above, but reworked slightly
"""
def f(cake_tuples, weight_capacity):
    mult = rem = prev_rem = prev_weight = max_val = prev_max_val = prev_mul = 0
    
    for weight, value in cake_tuples:
        print(f'weight: {weight} | value: {value} | prev_rem: {prev_rem}')
        
        if prev_rem > 0:
            prev_mul, prev_rem = divmod(weight, prev_rem)
            
        leftover_val = prev_mul * value
        print(f'leftover_val: {leftover_val}')
        
        if weight > 0:
            mult, rem = divmod(weight_capacity, weight)
        cur_val = mult * value
        print(f'cur_val: {cur_val}')
        
        max_val = max(max_val, cur_val, prev_max_val + leftover_val)
        
        prev_val = value
        prev_max_val = max_val
        prev_rem = rem
        
    return max_val



"""
This is the solution in Interview Cake
I do not iterate individual weights, but rather use
divmod to get as many - so I'm not sure what the difference is;
However, the individual calc per weight appears to be the classic
dynamic programming approach to the overlapping sub-problems.
"""

def max_duffel_bag_value(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                print(f'current_capacity: {current_capacity} | cake_weight: {cake_weight} | cake_value: {cake_value} | current_capacity - cake_weight: {current_capacity-cake_weight} | max_values_at_capacities[{current_capacity - cake_weight}]: {max_values_at_capacities[current_capacity - cake_weight]}')
                max_value_using_cake = (
                    cake_value
                    + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)
                print(f'max_value_using_cake: {max_value_using_cake} | current_max_value: {current_max_value}')

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]



cakes = [(7, 160), (3, 90), (2, 15)]

#print(mx(cakes, 20))
#print(f(cakes, 20))
print(max_duffel_bag_value(cakes, 20))

