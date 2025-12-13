def coeff_repr(c, is_latex: bool = False):
    """
    String representing coefficients in a linear combination.

    INPUT:

    - ``c`` -- a coefficient (i.e., an element of a ring)

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.repr import coeff_repr
        sage: coeff_repr(QQ(1/2))
        '1/2'
        sage: coeff_repr(-x^2)                                                          # needs sage.symbolic
        '(-x^2)'
        sage: coeff_repr(QQ(1/2), is_latex=True)
        '\\\\frac{1}{2}'
        sage: coeff_repr(-x^2, is_latex=True)                                           # needs sage.symbolic
        '\\\\left(-x^{2}\\\\right)'
    """
def repr_lincomb(terms, is_latex: bool = False, scalar_mult: str = '*', strip_one: bool = False, repr_monomial=None, latex_scalar_mult=None):
    '''
    Compute a string representation of a linear combination of some
    formal symbols.

    INPUT:

    - ``terms`` -- list of terms, as pairs (support, coefficient)
    - ``is_latex`` -- whether to produce latex (default: ``False``)
    - ``scalar_mult`` -- string representing the multiplication (default: ``\'*\'``)
    - ``latex_scalar_mult`` -- latex string representing the multiplication
      (default: a space if ``scalar_mult`` is ``\'*\'``; otherwise ``scalar_mult``)
    - ``coeffs`` -- for backward compatibility

    EXAMPLES::

        sage: repr_lincomb([(\'a\',1), (\'b\',-2), (\'c\',3)])
        \'a - 2*b + 3*c\'
        sage: repr_lincomb([(\'a\',0), (\'b\',-2), (\'c\',3)])
        \'-2*b + 3*c\'
        sage: repr_lincomb([(\'a\',0), (\'b\',2), (\'c\',3)])
        \'2*b + 3*c\'
        sage: repr_lincomb([(\'a\',1), (\'b\',0), (\'c\',3)])
        \'a + 3*c\'
        sage: repr_lincomb([(\'a\',-1), (\'b\',\'2+3*x\'), (\'c\',3)])
        \'-a + (2+3*x)*b + 3*c\'
        sage: repr_lincomb([(\'a\', \'1+x^2\'), (\'b\', \'2+3*x\'), (\'c\', 3)])
        \'(1+x^2)*a + (2+3*x)*b + 3*c\'
        sage: repr_lincomb([(\'a\', \'1+x^2\'), (\'b\', \'-2+3*x\'), (\'c\', 3)])
        \'(1+x^2)*a + (-2+3*x)*b + 3*c\'
        sage: repr_lincomb([(\'a\', 1), (\'b\', -2), (\'c\', -3)])
        \'a - 2*b - 3*c\'
        sage: t = PolynomialRing(RationalField(),\'t\').gen()
        sage: repr_lincomb([(\'a\', -t), (\'s\', t - 2), (\'\', t^2 + 2)])
        \'-t*a + (t-2)*s + (t^2+2)\'

    Examples for ``scalar_mult``::

        sage: repr_lincomb([(\'a\',1), (\'b\',2), (\'c\',3)], scalar_mult=\'*\')
        \'a + 2*b + 3*c\'
        sage: repr_lincomb([(\'a\',2), (\'b\',0), (\'c\',-3)], scalar_mult=\'**\')
        \'2**a - 3**c\'
        sage: repr_lincomb([(\'a\',-1), (\'b\',2), (\'c\',3)], scalar_mult=\'**\')
        \'-a + 2**b + 3**c\'

    Examples for ``scalar_mult`` and ``is_latex``::

        sage: repr_lincomb([(\'a\',-1), (\'b\',2), (\'c\',3)], is_latex=True)
        \'-a + 2 b + 3 c\'
        sage: repr_lincomb([(\'a\',-1), (\'b\',-1), (\'c\',3)], is_latex=True, scalar_mult=\'*\')
        \'-a - b + 3 c\'
        sage: repr_lincomb([(\'a\',-1), (\'b\',2), (\'c\',-3)], is_latex=True, scalar_mult=\'**\')
        \'-a + 2**b - 3**c\'
        sage: repr_lincomb([(\'a\',-2), (\'b\',-1), (\'c\',-3)], is_latex=True, latex_scalar_mult=\'*\')
        \'-2*a - b - 3*c\'
        sage: repr_lincomb([(\'a\',-2), (\'b\',-1), (\'c\',-3)], is_latex=True, latex_scalar_mult=\'\')
        \'-2a - b - 3c\'

    Examples for ``strip_one``::

        sage: repr_lincomb([ (\'a\',1), (1,-2), (\'3\',3) ])
        \'a - 2*1 + 3*3\'
        sage: repr_lincomb([ (\'a\',-1), (1,1), (\'3\',3) ])
        \'-a + 1 + 3*3\'
        sage: repr_lincomb([ (\'a\',1), (1,-2), (\'3\',3) ], strip_one = True)
        \'a - 2 + 3*3\'
        sage: repr_lincomb([ (\'a\',-1), (1,1), (\'3\',3) ], strip_one = True)
        \'-a + 1 + 3*3\'
        sage: repr_lincomb([ (\'a\',1), (1,-1), (\'3\',3) ], strip_one = True)
        \'a - 1 + 3*3\'

    Examples for ``repr_monomial``::

        sage: repr_lincomb([(\'a\',1), (\'b\',2), (\'c\',3)], repr_monomial = lambda s: s+"1")
        \'a1 + 2*b1 + 3*c1\'

    TESTS:

    Verify that :issue:`31672` is fixed::

        sage: # needs sage.symbolic
        sage: alpha = var("alpha")
        sage: repr_lincomb([(x, alpha)], is_latex=True)
        \'\\alpha x\'
        sage: A.<psi> = PolynomialRing(QQ)
        sage: B.<t> = FreeAlgebra(A)                                                    # needs sage.combinat sage.modules
        sage: (psi * t)._latex_()                                                       # needs sage.combinat sage.modules
        \'\\psi t\'
    '''
