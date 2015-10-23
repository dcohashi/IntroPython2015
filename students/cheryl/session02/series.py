# series homework
def fibonacci(n):
    '''Return the nth value of the fibonacci series'''
    if n<0:
        print ("value must be positive")
        return
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

def lucas(n):
    '''Return the nth value of the lucas series'''
    if n<0:
        print ("value must be positive")
        return
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, first_val=0, second_val=1):
    '''
    Return the nth value of a series of numbers where the next number
    in the series is a summation of the previous two numbers.
    The first two values in the series are option input parameters
    to this function.
    '''
    if n<0:
        print ("value must be positive")
        return
    if n==0:
        return first_val
    elif n==1:
        return second_val 
    else:
        return sum_series(n-1) + sum_series(n-2)

# Tests for the functions in this file
# test for fibonacci
fibonacci(-2)
assert fibonacci(5) == 5

# test for lucas
print ('Testing lucas')
lucas(-1)

for i in range(10):
    print(lucas(i))


