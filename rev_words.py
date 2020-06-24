"""
Interview Cake
Reverse words in place.
First reverse all characters;
then walk list of reversed characters, and reverse each word on the 
word boundary (space)
"""

def revw(msg):
    i = 0
    j = len(msg)-1
    while i < j:
        msg[i], msg[j] = msg[j], msg[i]
        i += 1
        j -= 1
    print(msg)
    i = 0
    j = len(msg)-1
    start = 0
    while i < j:
        while i <= j and msg[i] != ' ':
            i += 1
            print(f'i is now: {i}')
        ii = i-1
        print(f'ii: {ii} | start: {start}')
        while start < ii:
            print(f'msg: {msg}')
            msg[start], msg[ii] = msg[ii], msg[start]
            start += 1
            ii -= 1
            print(f'msg after swap: {msg}')
        i += 1
        start = i
