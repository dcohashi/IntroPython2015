#!/usr/bin/env python3

import pytest
from sparse_array import SparseArray as SA

def test_init():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a.length == 12

def test_load():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a.data[0] == 1 

def test_end():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a.data[11] == 5 

def test_len():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a.length == 12 

def test_set():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a[2] = 4
    assert a[2] == 4 

def test_get():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a[5] == 3 

def test_get0():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    assert a[7] == 0 

def test_out_of_range():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    with pytest.raises(IndexError):
        a[15] = 5

def test_set0():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a[2] = 0
    assert a[2] == 0 

def test_set0_from_num():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a[5] = 0
    assert a[5] == 0 

def test_del():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    del a[2]
    assert a.length == 11
    assert a[0] == 1
    assert a[4] == 3

def test_append():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a.append(8)
    assert a[12] == 8

def test_append0():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a.append(0)
    assert a[12] == 0
    assert a.length == 13

def test_append_array():
    a = SA([1,0,0,0,0,3,0,0,0,4,0,5])
    a.append([0,9])
    assert a[12] == 0
    assert a[13] == 9
    assert a.length == 14


