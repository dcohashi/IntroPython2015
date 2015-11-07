def count_evens(nums):
    '''Return the number of even integers in nums'''
    return(len([i for i in nums if not i%2]))
