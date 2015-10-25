# Sequence practice
def exchange(s):
    '''Return the sequence with first and last elements exchanged'''
    return(s[-1:] + s[1:-1] + s[:1])

assert exchange([1, 2, 3, 4, 5]) ==[5, 2, 3, 4, 1]

def every_other(s):
    '''Return every other element'''
    return( s[::2])

assert every_other("abcdefg") == "aceg"

def first_last(s):
    '''Return the first and last 4 chars removed'''
    return( s[1:-4])

assert first_last("firstlast") =='irst'


def reverse_str(s):
    '''Reverse a string only using slicing'''
    return( s[::-1])

assert reverse_str("12345678") == '87654321'

def thirds(s):
    '''Return a sequence with middle third, last then, then first third'''
    third = len(s)//3
    return(s[third:third*2]+s[third*2:]+s[:third])

assert thirds("123456789") == '456789123'
