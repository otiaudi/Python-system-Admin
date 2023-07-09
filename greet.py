#!/usr/bin/python3
def greeting():
    """
    >>> greeting()
    "Hello"
    """
if __name__=="__main__":
    greeting("silas")
    import doctest
    doctest.testmod()
