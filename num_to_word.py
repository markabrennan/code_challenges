"""
Converting a number to a word.  Problem by way of Steven Kaneti
"""


"""
Need some maps to get words
"""

mults = {
        1000000000:'Billion',
        1000000:'Million', 
        1000:'Thousand', 
        100:'Hundred', 
        10:'Ten', 
        1:'One'}

tens_dict = {
            2:'Twenty', 
            3:'Thirty', 
            4:'Forty', 
            5:'Fifty', 
            6:'Sixty', 
            7:'Seventy', 
            8:'Eighty', 
            9:'Ninety', 
            11:'Eleven', 
            12:'Twelve', 
            13:'Thirteen',
            13:'Fourteen', 
            15:'Fifteen',
            16:'Sixteen', 
            17:'Seventeen', 
            18:'Eighteen', 
            19:'Nineteen'}

vals_dict = {
            1:'One',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
            10:'Ten',
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen',
            20:'Twenty'}


def num_to_word(num):
    rem = num
    w = ''
    for m in mults.keys():
        mult, rem = divmod(rem, m)
        if mult > 0:
            if m == 1:
                w += ' ' 
                w += vals_dict[mult]
            elif m == 10:
                w += ' '
                w += tens_dict[mult]
            elif m == 1000:
                w += ' '
                if mult < 10:
                    w += vals_dict[mult]
                    w += ' '
                    w += 'Thousand'
                    w += ' ' 
                elif mult < 100:
                    w += tens_dict[mult]
                    w += ' ' 
                    w += 'Thousand'
                    w += ' ' 
                elif mult < 1000:
                    rem2, mult2 = divmod(mult, 100)
                    w += ' '
                    w += vals_dict[rem2]
                    w += ' Hundred '
                    if mult2 < 20: 
                        w += tens_dict[mult2]
                        w += ' '
                    else:
                        r2, m2 = divmod(mult2, 10)
                        w += tens_dict[r2]
                        w += ' '
                        w += vals_dict[m2]
                        w += ' '
                    w += 'Thousand '
            elif m == 1000000:
                w += ' '
                if mult < 10:
                    w += vals_dict[mult]
                    w += ' '
                    w += 'Million'
                    w += ' ' 
                elif mult < 20:
                    w += tens_dict[mult]
                    w += ' ' 
                    w += 'Million'
                    w += ' ' 
                elif mult < 100:
                   rem2, mult2 = divmod(mult, 10)
                   w += ' '
                   w += tens_dict[rem2]
                   w += ' '
                   w += vals_dict[mult2]
                   w += ' Million '
                elif mult < 1000:
                    rem2, mult2 = divmod(mult, 100)
                    w += ' '
                    w += vals_dict[rem2]
                    w += ' Hundred '
                    if mult2 < 20: 
                        w += tens_dict[mult2]
                        w += ' Hundred '
                    else:
                        r2, m2 = divmod(mult2, 10)
                        w += tens_dict[r2]
                        w += ' '
                        w += vals_dict[m2]
                        w += ' '
                    w += ' Million '
            else: 
                w += vals_dict[mult]
                w += ' '
                w += mults[m]
                w += ' '
    return w


# Test Cases

num1 = 5431
num2 = 125345
num3 = 112345
num4 = 1425321
num5 = 23452178
num6 = 453123879
num7 = 7001123456
num8 = 7022123456
num9 = 7322123456

print(f'\t{num1}:\t{num_to_word(num1)}')
print(f'\t{num2}:\t{num_to_word(num2)}')
print(f'\t{num3}:\t{num_to_word(num3)}')
print(f'\t{num4}:\t{num_to_word(num4)}')
print(f'\t{num5}:\t{num_to_word(num5)}')
print(f'\t{num6}:\t{num_to_word(num6)}')
print(f'\t{num7}:\t{num_to_word(num7)}')
print(f'\t{num8}:\t{num_to_word(num8)}')
print(f'\t{num9}:\t{num_to_word(num9)}')