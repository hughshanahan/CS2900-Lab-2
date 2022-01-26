test = {
    'name': 'checkpoint-4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the thetaRot function. Check the name.
                    >>> # Have you defined it exactly as 'def thetaRot(theta)'?
                    >>> "thetaRot" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return anything!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> thetaRot(theta) is None
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a rotation matrix here!
                    >>> # Your function returns something else...
                    >>> type(thetaRot(theta)).__name__ == 'ndarray'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your rotation matrix is wrong by at least 0.001.
                    >>> # Print out what your function calculated and compare it with
                    >>> # what you have worked out on paper.
                    >>> np.allclose(thetaRot(math.pi/8), test_rot, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> theta = math.pi / 4
            >>> test_rot = np.array([[0.92387, -0.38268, 0], [0.38268, 0.92387, 0], [0, 0, 1]])
            """,
            'type': 'doctest'
        }
    ]
}
