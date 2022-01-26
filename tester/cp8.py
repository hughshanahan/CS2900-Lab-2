test = {
    'name': 'checkpoint-8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the sqDiffMatrices function. Check the name.
                    >>> # Have you defined it properly? I.e. 'def sqDiffMatrices(A, B)'
                    >>> "sqDiffMatrices" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your squard difference is wrong by at least 0.001.
                    >>> # Check that you are first subtracting and then squaring.
                    >>> np.isclose(sqDiffMatrices(R1m, R1inv), 0.0, atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your squard difference is wrong by at least 0.001.
                    >>> # Check that you are first subtracting and then squaring.
                    >>> np.isclose(sqDiffMatrices(R1m, R2), 1.431, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
