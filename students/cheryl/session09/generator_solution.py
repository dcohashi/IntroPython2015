#!/usr/bin/env python3
'''
generators
'''

def intsum():
    i = 0
    j= 0
    while True:
        yield i
        j = j + 1
        i = i + j

def doubler():
    i = 1
    while True:
        yield i
        i = i*2

def fib():
    yield 1
    prev = 0
    next = 1
    while True:
        ans = prev + next
        yield ans
        prev = next 
        next = ans

def prime():
    i = 1
    while True:
        i += 1
        print('i = {}'.format(i))
        is_prime = True
        for j in range(2, i-1):
            print('J= {}'.format(j))
            if i%j == 0:
                is_prime = False
                print('is_prime: {}'.format(is_prime))
                break
        if is_prime:
            yield i

