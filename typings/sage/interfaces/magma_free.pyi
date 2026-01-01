"Interface to the free online MAGMA calculator"

class MagmaExpr(str): ...

def magma_free_eval(code, strip: bool = True, columns: int = 0):
    '''
    Use the free online MAGMA calculator to evaluate the given
    input code and return the answer as a string.

    .. WARNING::

        The code must evaluate in at most 120 seconds
        and there is a limitation on the amount of RAM.

    EXAMPLES::

        sage: magma_free("Factorization(9290348092384)")  # optional - internet
        [ <2, 5>, <290323377887, 1> ]
    '''

class MagmaFree:
    '''
    Evaluate MAGMA code without requiring that MAGMA be installed
    on your computer by using the free online MAGMA calculator.

    EXAMPLES::

        sage: magma_free("Factorization(9290348092384)")  # optional - internet
        [ <2, 5>, <290323377887, 1> ]
    '''
    def eval(self, x, **kwds): ...
    def __call__(self, code, strip: bool = True, columns: int = 0): ...

magma_free: MagmaFree
