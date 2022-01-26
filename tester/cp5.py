test = {
    'name': 'checkpoint-5',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the Rx function. Check the name.
                    >>> # Have you defined it exactly as 'def Rx(R, x)'?
                    >>> "Rx" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return anything!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> Rx(R, x) is None
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a vector here!
                    >>> # Your function returns something else...
                    >>> type(Rx(R, x)).__name__ == 'ndarray'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a vector here, not a matrix.
                    >>> # Check you are multiplying R and x correctly.
                    >>> Rx(R, x).shape == (3,)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the Rx_cp5 variable. You need to test your Rx function.
                    >>> # You should have 'Rx_cp5 = Rx(. . .)'
                    >>> "Rx_cp5" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your vector y is wrong by at least 0.001.
                    >>> # Print out what your function calculated and compare it with
                    >>> # what you have worked out on paper.
                    >>> np.allclose(Rx(R, x), np.array([1.1102e-16, 1.4142, 1.0000]), atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> R = thetaRot(math.pi / 4)
            >>> x = np.ones(3)
            """,
            'type': 'doctest'
        }
    ]
}
