"""
Leet Code Problem # 415: Add Strings
It was easy to convert a string to an int, then add;
but converting BACK to a string stumped me until I picked
up the 'get_pos_nums()' code
"""


def addStrings(self, num1: str, num2: str) -> str:
    def get_pos_nums(num):
        d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        pos_nums = []
        while num != 0:
            pos_nums.append(d[num % 10])
            num = num // 10
        return ''.join(pos_nums[::-1])        
    def add(num):
        n = 0
        e = 0
        d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        for i in num[::-1]:
            n += d[i] * (10 ** e)
            e += 1
        return n
    if num1 == '0' and num2 == '0':
        return '0'
    if num1 == '0' and num2 != '0':
        return num2
    if num2 == '0' and num1 != '0':
        return num1
    return get_pos_nums(add(num1) + add(num2))       


"""
This "string-to-int" function is MUCH beter than mine!
"""
def stringToInt(str1): # Requirement 4
    res = 0
    str_d = {str(i):i for i in range(0,10)}
    for d in str1:
        res = res * 10 + str_d[d]
    return res
 
