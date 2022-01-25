"""
Utility functions for CS2900 Lab 2 checkpoint test suite.

Author: Tom Kuipers
"""


def check_nrow_ncol():
    import inspect
    import re
    local_vars = inspect.currentframe().f_back.f_locals
    nrow_match = len(re.findall("nrow\\s*=\\s*2", str(local_vars))) == 0
    ncol_match = len(re.findall("ncol\\s*=\\s*3", str(local_vars))) == 0
    return nrow_match and ncol_match
