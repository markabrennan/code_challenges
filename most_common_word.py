# Leet Code 819 - most common word
#
# Couple of versions
# Accepted:

def mostCommonWord(paragraph, banned):
    import re
    p1 = re.compile(',')
    p2 = re.compile('\.')
    p3 = re.compile(';')
    p4 = re.compile('-')
    p5 = re.compile(':')
    p6 = re.compile('!')
    p7 = re.compile('\?')
    p8 = re.compile("'")        
    paragraph = p1.sub(' ', paragraph)
    paragraph = p2.sub(' ', paragraph)
    paragraph = p3.sub(' ', paragraph)
    paragraph = p4.sub(' ', paragraph)
    paragraph = p5.sub(' ', paragraph)
    paragraph = p6.sub(' ', paragraph)        
    paragraph = p7.sub(' ', paragraph)        
    paragraph = p8.sub(' ', paragraph)                
    clean_para = paragraph.lower()
    new_para = clean_para.split()
    word_dict = dict.fromkeys(set(new_para), 0)
    for word in new_para:
        if word not in banned: 
            word_dict[word] += 1 
            
    return max(zip(word_dict.values(), word_dict.keys()))[1]


# version with string translate()
def f(paragraph, banned):
    import string
    punc_map = {ord(x):' ' for x in string.punctuation}
    clean_para = paragraph.translate(punc_map)
    clean_para_lower = clean_para.lower()
    new_para = clean_para_lower.split()
    word_dict = dict.fromkeys(set(new_para), 0)
    for word in new_para:
        if word not in banned: 
            word_dict[word] += 1 
            
    return max(zip(word_dict.values(), word_dict.keys()))[1]


# another version with Counter
def f2(paragraph, banned):
    from collections import Counter
    import string

    punc_map = {ord(x):' ' for x in string.punctuation}
    clean_para = paragraph.translate(punc_map)

    clean_para_lower = clean_para.lower()
    new_para = clean_para_lower.split()
    para_with_excl = [word for word in new_para if word not in banned]

    word_counts = Counter(para_with_excl)

    return word_counts.most_common(1)[0][0]
