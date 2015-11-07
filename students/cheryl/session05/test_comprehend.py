#!/usr/bin/env python3

from comprehend import count_evens

# Test count_evens
def test_count_evens_simple():
    assert count_evens([2, 1, 2, 3, 4]) == 3

# Test count_evens with a zero
def test_count_evens_zero():
    assert count_evens([2, 2, 0]) == 3

# Test count_evens with none 
def test_count_evens_none():
    assert count_evens([1, 3, 5]) == 0
