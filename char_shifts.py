"""
Duplicate entry for critical string shifting idioms
"""

s = 'cat'

# Shift LEFT by one
s[1:] + s[:1]

# Shift RIGHT by one: 
# use diff between length of string and pos/place
# to shift
pos = 1
s[len(s)-pos:] + s[:len(s)-pos]


