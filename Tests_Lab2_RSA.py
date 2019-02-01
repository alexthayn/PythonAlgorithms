#Lab 2 RSA TESTS
import sys
from Lab2_RSA import ExtendedEuclidean, PowerMod, MultiplicativeInverse, StringToIntArr, IntArrToString

def test_ExtendedEuclidean():
    assert ExtendedEuclidean(0,0) == (0,0,1)
    assert ExtendedEuclidean(1,1) == (1,1,0)
    assert ExtendedEuclidean(1,2) == (1,1,0)
    assert ExtendedEuclidean(2,1) == (1,0,1)
    assert ExtendedEuclidean(100,2) == (2,0,1)
    assert ExtendedEuclidean(100,50) == (50,0,1)
    assert ExtendedEuclidean(12,18) == (6,-1,1)
    assert ExtendedEuclidean(1024,20) == (4,1,-51)

def test_PowerMod():
    assert PowerMod(6,2,3) == 0
    assert PowerMod(1,8,2) == 1
    assert PowerMod(2,8,7) == 4
    assert PowerMod(8,3,49320) == 512
    assert PowerMod(100,918,2000403402) == 1194280768

def test_MultiplicativeInverse():
    assert MultiplicativeInverse(0,0) == 0
    assert MultiplicativeInverse(0,1) == 0
    assert MultiplicativeInverse(3,11) == 4
    assert MultiplicativeInverse(3,43) == 29
    assert MultiplicativeInverse(23,28) == 11
    assert MultiplicativeInverse(324,4123) == 2965

def test_StringToIntArr():
    assert StringToIntArr('') == []
    assert StringToIntArr('1a@#') == [49, 97, 64, 35]
    assert StringToIntArr('1,2,3,4') == [49, 44, 50, 44, 51, 44, 52]
    assert StringToIntArr('abcde') == [97,98,99,100,101]
    assert StringToIntArr('HELLO!') == [72,69,76,76,79,33]

def test_IntArrToString():
    assert IntArrToString([]) == ''
    assert IntArrToString([49, 97, 64, 35]) == '1a@#'
    assert IntArrToString([49, 44, 50, 44, 51, 44, 52]) == '1,2,3,4'
    assert IntArrToString([97,98,99,100,101]) == 'abcde'
    assert IntArrToString([72,69,76,76,79,33]) == 'HELLO!'
