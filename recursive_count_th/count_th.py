'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    lst = list(word)
    if len(lst) == 0:
        return 0
    if len(lst) == 1: 
        return 0
    if lst[0] == 't' and lst[1] == 'h':
        return 1 + count_th(lst[1:])
    else:
        return 0 + count_th(lst[1:])
