test = {
    'name': 'checkpoint-6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the R1 variable. Don't skip things...
                    >>> # You need to run the cell just above the extension work to define R1.
                    >>> "R1" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the compare function. Check the name.
                    >>> # Have you defined it exactly as 'def compare(x, y)'?
                    >>> "compare" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return anything!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> compare(x, y) is None
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a Python tuple here! 
                    >>> # Your function returns a list or Numpy array...
                    >>> type(compare(x, y)).__name__ not in ['list', 'ndarray']
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a tuple here!
                    >>> # Your function returns something else entirely...
                    >>> type(compare(x, y)).__name__ == 'tuple'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the vector x and/or y...
                    >>> # You need to define them as above and test your compare function.
                    >>> "x" in dir() and "y" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your vector y is wrong by at least 0.001.
                    >>> # Print out what your function calculated and compare it with
                    >>> # what you have worked out on paper.
                    >>> np.allclose(np.array(compare(x, y)), np.array([1.732, 1.732, 1, 1]), atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> x = np.ones(3)
            >>> y = np.array([1,1,-1])
            """,
            'type': 'doctest'
        }
    ]
}
