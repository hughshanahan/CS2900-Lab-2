test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems A_cp1 is undefined. Have you defined it correctly?
                    >>> # I.e. A_cp1 = np.zeros(. . .)
                    >>> 'A_cp1' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems nrow is undefined. Have you defined it correctly?
                    >>> # I.e. nrow = ...
                    >>> 'nrow' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems ncol is undefined. Have you defined it correctly?
                    >>> # I.e. ncol = ...
                    >>> 'ncol' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your nrow seems to be the number of columns.
                    >>> # Check you're getting the right element of the shape array.
                    >>> nrow != 3
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your ncol seems to be the number of rows.
                    >>> # Check you're getting the right element of the shape array.
                    >>> ncol != 5
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # The values for nrow and ncol are incorrect.
                    >>> # You should be using A.shape to determine these.
                    >>> (nrow == 5) and (ncol == 3)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # You haven't used the 'shape' function from above.
                    >>> # Instead you seem to have set them manually.
                    >>> # Whilst your values are correct, this wasn't the way to do it.
                    >>> # Try to do it using the shape function.
                    >>> from tester.utils import check_nrow_ncol
                    >>> check_nrow_ncol()
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
