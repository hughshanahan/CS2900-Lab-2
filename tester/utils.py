"""
Utility functions for CS2900 Lab 2 checkpoint test suite.

Author: Tom Kuipers
"""


def check_code(regex):
    import inspect
    import re
    local_vars = str(inspect.currentframe().f_back.f_back.f_locals)
    no_match = len(re.findall(regex, local_vars)) == 0
    return no_match


def check_nrow_ncol():
    return (check_code(r"nrow\s*=\s*5") and check_code(r"ncol\s*=\s*3"))


def check_rot_inv():
    return not (check_code(r"R1m\s*=\s*R1\.t[^b-m]{3}[^a-o, w-z]{2}o[se]{2}\(\)") and check_code(r"R1m\s*=\s*np\.t[^b-m]{3}[^a-o, w-z]{2}o[se]{2}\(R1\)"))
