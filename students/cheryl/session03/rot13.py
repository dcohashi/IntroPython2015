#!/usr/bin/env python3

"""
decrypt a ROT13 string
"""

def rot13(s):
    dec_table = s.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?", 
                            "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM ,.!?")
    return(s.translate(dec_table))

if __name__ == '__main__':
    assert rot13("test") == 'grfg'
    assert rot13(rot13("This is a string.")) == "This is a string."

    print (rot13("Zntargvp sebz bhgfvqr arne pbeare"))
