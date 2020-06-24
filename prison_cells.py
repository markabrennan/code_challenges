"""
Leet Code Problem #957: Prison Cells After N Days

brute force will probably NOT work here, given
N can be 1B!!
"""

# def f(l, n):
#     ret = l[:]
#     prev = ret[:]
#     seen = {}
    
#     print(f'ret: {ret}')
#     for d in range(0, n):
#         if d == 0
#         ret[0] = 0
#         ret[-1] = 0
#         for i in range(1, len(ret)-1):
# #            print(f'i is {i} | prev[{i-1}]: {prev[i-1]} | prev[{i+1}]: {prev[i+1]}')

#             if (i >0 and i<7 and prev[i-1] == prev[i+1]):
#                 ret[i] = 1
#             else:
#                 ret[i] = 0
#         memo[prev] = ret
#         prev = ret[:]
# #        print(f'Day {d+1}:  ret is now: {ret}')
               
#     return prev


def f1(cells, N):
    def next_day(cells):
        return [ int(i>0 and i<7 and cells[i-1] == cells[i+1]) for i in range(8) ]
    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            print(f'N: {N} | seen[c]: {seen[c]} | seen[c] - N: {seen[c]-N} | new N: {N%(seen[c]-N)}')
            print(f'size of seen:  {len(seen)}')
            N %= seen[c] - N
        seen[c] = N
        if N >= 1:
            N -= 1
            cells = next_day(cells)
    return cells    


#cells =  [0,1,0,1,1,0,0,1]   # for N=7:  Output should be:  0,0,1,1,0,0,0,0
cells = [1,0,0,1,0,0,1,0]    # for N=10^9:  Output should be [0,0,1,1,1,1,1,0] 
n = 1000000000

print(f1(cells, n))

#print(f(cells, n)) 