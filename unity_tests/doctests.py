# python -m doctest -v nome_modulo_a_ser_testado.py

#def soma(a, b):
#    """soma os números a e b
#    
#    >>> soma(4, 6)
#    10
#    """
#    return a + b

"""
OUTPUT:
    Trying:
        soma(4, 6)
    Expecting:
        10
    ok
    1 items had no tests:
        doctests
    1 items passed all tests:
    1 tests in doctests.soma
    1 tests in 2 items.
    1 passed and 0 failed.
    Test passed.
"""

#def soma(a, b):
#    """soma os números a e b
#    
#    >>> soma(4, 1)
#    10
#    """
#    return a + b

"""
Trying:
    soma(4, 1)
Expecting:
    10
**********************************************************************
File "/home/user/Documentos/Python/learn_DS/unity_tests/doctests.py", line 30, in doctests.soma
Failed example:
    soma(4, 1)
Expected:
    10
Got:
    5
1 items had no tests:
    doctests
**********************************************************************
1 items had failures:
   1 of   1 in doctests.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
"""

def double(values):
    """duplica os valores em uma lista
    
    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TyperError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
