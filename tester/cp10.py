test = {
    'name': 'checkpoint-10',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the S matrix.
                    >>> # Have you defined it? I.e. S = np.array(. . .)
                    >>> "S" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your S matrix is incorrect.
                    >>> # You should have 5, 4 and 2 along the diagonal.
                    >>> S[0][0] == 5 and S[1][1] == 4 and S[2][2] == 2
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your S matrix is incorrect.
                    >>> # You should have 5, 4 and 2 along the diagonal and the rest zeros.
                    >>> np.sum(S) == 11
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the S_inv_form matrix.
                    >>> # Have you defined it correctly?
                    >>> "S_inv_form" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your S_inv_form matrix is incorrect.
                    >>> # Check that you are properly dividing the diagonal.
                    >>> np.all(S_inv_form == np.linalg.inv(S))
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the S_inv_calc matrix.
                    >>> # Have you defined it correctly?
                    >>> "S_inv_calc" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your squard difference is wrong by at least 0.001.
                    >>> # This should be zero. Ask yourself why this is.
                    >>> np.isclose(sqDiffMatrices(S_inv_form, S_inv_calc), 0.0, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
