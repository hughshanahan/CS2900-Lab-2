test = {
    'name': 'checkpoint-7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the R1m variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "R1m" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the R1inv variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "R1inv" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your inverse is wrong by at least 0.001.
                    >>> # Are you using the correct variable as the argument to the linalg.inv function?
                    >>> np.allclose(R1inv, np.array([[0.7071, 0.7071, 0], [-0.7071, 0.7071, 0], [0, 0, 1]]), atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, your inverse is correct but you seem to have
                    >>> # computed it manually. We're looking for something else...
                    >>> # Hint: what is the inverse of a rotation matrix equivalent to?
                    >>> #
                    >>> # IMPORTANT: You must restart your kernel now before running
                    >>> # this checkpoint tester again.
                    >>> from tester.utils import check_rot_inv
                    >>> check_rot_inv()
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
