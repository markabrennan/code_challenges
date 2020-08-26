"""
Leet Code August Challenge Problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3408/
"""


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.hash_map:
            last_time = self.hash_map[message]
            if timestamp >= last_time + 10:
                self.hash_map[message] = timestamp
                return True
            else:
                return False
        else:
            self.hash_map[message] = timestamp
            return True

"""
TEST CASES
"""

# Your Logger object will be instantiated and called as such:
logger = Logger()

# logging string "foo" at timestamp 1
print('logger.shouldPrintMessage(1, "foo")', logger.shouldPrintMessage(1, "foo"))
# returns true 

# logging string "bar" at timestamp 2
print('logger.shouldPrintMessage(2,"bar")', logger.shouldPrintMessage(2,"bar"))
# returns true

# logging string "foo" at timestamp 3
print('logger.shouldPrintMessage(3,"foo")', logger.shouldPrintMessage(3,"foo"))
# returns false

# logging string "bar" at timestamp 8
print('logger.shouldPrintMessage(8,"bar")', logger.shouldPrintMessage(8,"bar"))
# returns false

# logging string "foo" at timestamp 10
print('logger.shouldPrintMessage(10,"foo")', logger.shouldPrintMessage(10,"foo"))
# returns false

# logging string "foo" at timestamp 11
print('logger.shouldPrintMessage(11,"foo")', logger.shouldPrintMessage(11,"foo"))
# returns true