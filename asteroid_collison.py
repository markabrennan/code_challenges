"""
Leet Code Problem # 735: Asteroid Collison

Initial intuition is to use two queues, but not 
sure that works.

"""


from collections import deque

def collision(l):
    right_moving = deque()
    left_moving = deque()
    results = []
    # asteroid is guaranteed to be non-zero
    for i in l:
        if i > 0:
            right_moving.append(i)
        else:
            left_moving.append(i)
    while right_moving and left_moving:
        right = right_moving[0]
        left = left_moving[0]
        if abs(right) > abs(left):
            left_moving.popleft()
            results.append(right)
        elif abs(left) > abs(right):
            right_moving.popleft()
            results.append(left)
        elif abs(left) == abs(right):
            right_moving.popleft()
            left_moving.popleft()
            
            

    if right_moving:
        results.extend([i for i in right_moving])
    if left_moving:
        results.extend([i for i in leftt_moving])
    return results


"""
That attempt was a spectactular failure!
Going to start all over again. Idea
is to sort positive and negative "asteroids"
and then seen about offseting them. If they don't offset,
the larger wins.
"""

def collision2(l):
    pos = sorted([i for i in l if i >0], reverse=True)    
    neg = sorted([i for i in l if i <0], reverse=True)    
    results = []
    while pos and neg:
        p = pos.pop(0)
        n = neg.pop(0)
        if abs(p) > abs(n):
            results.append(p)
        elif abs(n) > abs(p):
            results.append(n)
    if pos:
       results.extend(pos)
    elif neg:
        results.extend(neg)
    
    return sorted(results)

"""
another attempt:
this one will be a brute force attempt, which
won't be acceptable, but let's see if we can 
get it to work.
"""

def collision3(asteroids):
    results = []
    left = []
    end = len(asteroids) - 1
    # navigate to last neg number:
    first_neg_pos = None
    last_pos_pos = None
    first_pos = None
    
    for ix, v in enumerate(asteroids):
        if v > 0 and first_pos is None:
            first_pos = ix
        if first_pos is not None and first_neg_pos is None and v < 0:
            first_neg_pos = ix

    # for each negative asteroid, travel
    # 'backwards' colliding with each 
    # positive asteroid    
    if first_neg_pos is not None and first_pos is not None:
        negs = asteroids[first_neg_pos:]
        pos = list(reversed(asteroids[first_pos:first_neg_pos]))
        left = asteroids[0:first_pos]
        results.extend(left)
        
        print(f'neg:  {negs}  |  pos:  {pos} | left: {left}')

        i = j = 0
        while i <= len(negs)-1:
            while j <= len(pos)-1:
                if abs(negs[i]) > abs(pos[j]):
                    results.append(negs[i])
                    break
                elif abs(pos[j]) > abs(negs[i]):
                    results.append(pos[j])
                    break
                elif abs(pos[j]) == abs(negs[i]):
                    break
            i += 1
            j += 1
        if i < len(negs)-1:
            results.extend(negs[i+1:])
        if j < len(pos)-1:
            results.extend(pos[j+1:])
    else:
        return asteroids
    
    if left:
        return results
    else:
        return list(reversed(results))


"""
Yet another attempt - maybe try some
recursion...or not.
"""

"""
def collison4(asteroids):
    restuls = []
    i = 0
    end = len(asteroids) - 1
    while i < end:
        if asteroids[i] < 0 and i+1 < end and asteroids[i+1] < 0:
            results.append(asteroids[i])
        elif asteroids[i] < 0 and i+1 < end and asteroids[i=1] > 0:
            if abs(asteroids[i]) > abs(asteroids[i+1]):
                results.append(asteroids[i])
            elif abs(asteroids[i]) < abs(asteroids[i+1]):
                results.append(asteroids[i+1])
            i += 1
        elif asteroids[i] > 0 and i+1 < end and asteroids[i+1] > 0:
            i += 1
           
"""

"""
Another attempt
Try a stack
"""
def collision5(asteroids):
    def wind_down(asteroids):
        top = asteroids[-1]
        prev_pos = len(asteroids) - 1
        j = prev_pos - 1
        run_neg = False
        while j >= 0:
            top = asteroids[prev_pos]
            peek = asteroids[j]
            if top < 0 and peek > 0 and abs(top) > abs(peek):
                asteroids.pop(j)
            elif top < 0 and peek > 0 and abs(top) < abs(peek):
                asteroids.pop(prev_pos)
            elif top < 0 and peek > 0 and abs(top) == abs(peek):
                asteroids.pop(prev_pos)
                asteroids.pop(j)
                j -= 1
                prev_pos -= 1
            j -= 1
            prev_pos -= 1
        return asteroids

    # get successive starting negative asteroids:
    start = 0
    results = asteroids[:]
    i = 1
    j = len(asteroids) - 1
    while i <= j:
        if asteroids[i] < 0 and asteroids[i-1] > 0:
            # first negative, move it down:
            results = wind_down(asteroids[0:i+1])
            if len(results) < 1: #or results[-1] < 0:
                break
            asteroids = results + asteroids[i+1:]
            i = 1
            j = len(asteroids) - 1
        else:
            i += 1
    return results


"""
Leet Code Solution - much less
code than I had!
"""
def asteroidCollision(asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans

"""
Same function from the published
Leet Code solution, but I'm re-writing it
to use some of the idioms I used (e.g., abs()
instead of -new).
"""

def asteroidCollision2(asteroids):
    results = []
    for cur in asteroids:
        while results and cur < 0 < results[-1]:
            # processing a negative asteroid
            if abs(cur) > abs(results[-1]):
                results.pop()
                # the negative asteroid broke up a positive
                # asteroid beneath it, so the negative
                # asteroid keeps moving left (down)
                # so by continuing, we ensure it will
                # be processed again and evaluated against
                # the next item beneath it (in the stack)
                continue
            elif abs(cur) == abs(results[-1]):
                results.pop()
            # by breaking we also discard the new asteroid
            # this means the current asteroid was destroyed
            # by its collision with the top of the stack
            # (i.e., top of stack is a postive number greater
            # # than the current negative number)
            break
        else: # else statement with a while
            # add to stack
            results.append(cur)
    return results

            
            
"""
TEST CASES
"""

#asteroids = [5, 10, -5]  # expected result:  [5, 10]
#asteroids =  [8, -8]  # expected result: []
#asteroids = [10, 2, -5]  # expected result:  [10]
#asteroids =  [-2, -1, 1, 2]  # expected result:   [-2, -1, 1, 2]
#asteroids = [-2,-2,1,-2]  # expected results:  [-2,-2,-2]
#asteroids = [-2,-2,2,-1]  # expected results:  [-2,-2,2]
asteroids = [-2,1,-2,-2]  # expected results:  [-2,-2,-2]
#asteroids = [-2,1,-2,-1]  # expected results:  [-2,-2,-1]
#asteroids = [-2,-2,1,-1]  # expected results:  [-2, -2]
#asteroids = [-2,2,-1,-2]  # expected results:  [-2]

print(asteroidCollision2(asteroids))