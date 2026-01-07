r"""
Fast Numerical Evaluation

For many applications such as numerical integration, differential
equation approximation, plotting a 3d surface, optimization problems,
monte-carlo simulations, etc., one wishes to pass around and evaluate
a single algebraic expression many, many times at various floating
point values. Doing this via recursive calls over a python
representation of the object (even if Maxima or other outside packages
are not involved) is extremely inefficient.

The solution implemented in this module, by Robert Bradshaw (2008-10),
has been superseded by :func:`~sage.ext.fast_callable.fast_callable`.
All that remains here is a compatible interface function :func:`fast_float`.

AUTHORS:

- Robert Bradshaw (2008-10): Initial version
"""

from typing import TypeGuard, overload
from sage.ext.fast_callable import Expression
from sage.symbolic.expression import Expression as SRElement
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base
from sage.structure.element import Element

from sage.ext.fast_callable import Wrapper as Wrapper, fast_callable as fast_callable
from sage.ext.interpreters.wrapper_rdf import Wrapper_rdf

type _X = Expression | SRElement | Element[PolynomialRing_generic] | Element[MPolynomialRing_base]

type _Fs = tuple[_Fs, ...] | list[_Fs] | _X


type _T = tuple[_T, ...] | Wrapper_rdf[float]

@overload
def fast_float(f: tuple[_Fs, ...] | list[_Fs], *vars: str | object, expect_one_var: bool = False) -> tuple[_T, ...]: ...
@overload
def fast_float(f: _X, *vars: str | object, expect_one_var: bool = False) -> Wrapper_rdf[float]: ...
@overload
def fast_float[NotSupported](f: NotSupported, *vars: str | object, expect_one_var: bool = False) -> NotSupported:
    """
    Try to create a function that evaluates f quickly using
    floating-point numbers, if possible.

    On failure, returns the input unchanged.

    This is an alternative interface to :func:`sage.ext.fast_callable.fast_callable`.
    :issue:`32268` proposes to deprecate this function.

    INPUT:

    - ``f`` -- an expression
    - ``vars`` -- the names of the arguments
    - ``expect_one_var`` -- don't give deprecation warning if ``vars`` is
      omitted, as long as expression has only one var

    EXAMPLES::

        sage: from sage.ext.fast_eval import fast_float
        sage: x,y = var('x,y')                                                          # needs sage.symbolic
        sage: f = fast_float(sqrt(x^2+y^2), 'x', 'y')                                   # needs sage.symbolic
        sage: f(3,4)                                                                    # needs sage.symbolic
        5.0

    Specifying the argument names is essential, as fast_float objects
    only distinguish between arguments by order. ::

        sage: # needs sage.symbolic
        sage: f = fast_float(x-y, 'x','y')
        sage: f(1,2)
        -1.0
        sage: f = fast_float(x-y, 'y','x')
        sage: f(1,2)
        1.0
    """

def is_fast_float(x: object) -> TypeGuard[Wrapper]: ...
