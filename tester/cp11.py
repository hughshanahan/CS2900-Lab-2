test = {
    'name': 'checkpoint-11',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the N matrix.
                    >>> # Have you defined it? I.e. N = np.array(. . .)
                    >>> "N" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your N matrix is incorrect.
                    >>> # Check the lecture slides for the definition of N.
                    >>> np.array_equal(N, np.load('tester/res/N.npy'))
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the Nsq matrix.
                    >>> # Have you defined it correctly?
                    >>> "Nsq" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your Nsq matrix is incorrect.
                    >>> # There is a simple way that you can square a matrix.
                    >>> np.array_equal(Nsq, np.array([[1, 0, 1, 1], [0, 3, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]))
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the Ncb matrix.
                    >>> # Have you defined it correctly?
                    >>> "Ncb" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your Ncb matrix is incorrect.
                    >>> # There is a simple way that you can square a matrix.
                    >>> np.array_equal(Ncb, np.array([[0, 3, 1, 1], [3, 2, 4, 4], [1, 4, 2, 3], [1, 4, 3, 2]]))
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
