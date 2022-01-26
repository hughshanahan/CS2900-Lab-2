test = {
    'name': 'checkpoint-3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems R is undefined. Have you defined it correctly?
                    >>> # I.e. R = np.array( . . . )
                    >>> "R" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems x is undefined. Have you defined it correctly?
                    >>> # I.e. x = np.array( . . . )
                    >>> "x" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems y is undefined. Have you defined it correctly?
                    >>> # I.e. y = np.array( . . . )
                    >>> "y" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your vector y is incorrect.
                    >>> # Check the order in which you are multiplying Rx.
                    >>> np.array_equal(y, np.array([6,-3]))
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
