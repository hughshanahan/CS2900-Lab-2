test = {
    'name': 'checkpoint-2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems X is undefined. Have you defined it correctly?
                    >>> # I.e. X = np.array( . . . )
                    >>> "X" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your array has 4 rows and 2 columns.
                    >>> # We want 2 rows and 4 columns. Swap your numbers around for the shape.
                    >>> X.shape != (4,2)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, X is not the correct shape.
                    >>> # You need to specify the shape as an argument.
                    >>> X.shape == (2,4)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your matrix X does not contain only 1s.
                    >>> # Are you using np.ones(. . .)?
                    >>> np.all(X[:] == 1)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
