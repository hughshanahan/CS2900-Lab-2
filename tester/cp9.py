test = {
    'name': 'checkpoint-9',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the sqDiffMatrices function.
                    >>> # You need to have completed checkpoint 8 for this question!
                    >>> "sqDiffMatrices" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the A_cp9 matrix.
                    >>> # Have you defined it correctly?
                    >>> "A_cp9" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the B_cp9 matrix.
                    >>> # Have you defined it correctly?
                    >>> "B_cp9" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your squard difference is wrong by at least 0.001.
                    >>> # Check that you are first subtracting and then squaring.
                    >>> np.isclose(sqDiffMatrices(A_cp9, B_cp9), 0.177, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
