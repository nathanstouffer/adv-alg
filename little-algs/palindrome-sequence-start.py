# a little script to compute the minimum number 
# of palindromes a word can be broken into

from sys import argv

def palin_seq(word, s, f):
    if (f == len(word)):
        if is_palin(word, s, f-1):
            return 1
        else:
            return "inf"
    cur = palin_seq(word, s, f+1)
    nxt = "inf"
    if is_palin(word, s, f):
        nxt = palin_seq(word, f+1, f+1)
    if (type(nxt) is not int):
        return cur
    if (type(cur) is not int):
        return nxt+1
    return min(cur, nxt+1)

def is_palin(word, s, f):
    if (s >= f):
        return True
    if (word[s] == word[f]):
        return is_palin(word, s+1, f-1)
    return False

script, word = argv
seq = palin_seq(word, 0, 0)
print("min number of sequential palindromes: " + str(seq))
