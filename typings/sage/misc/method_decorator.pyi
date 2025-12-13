from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject
from typing import Self

class MethodDecorator(SageObject):
    f: Incomplete
    __doc__: Incomplete
    __module__: Incomplete
    def __init__(self, f) -> None:
        """
        EXAMPLES::

            sage: from sage.misc.method_decorator import MethodDecorator
            sage: class Foo:
            ....:     @MethodDecorator
            ....:     def bar(self, x):
            ....:         return x**2
            sage: J = Foo()
            sage: J.bar
            <sage.misc.method_decorator.MethodDecorator object at ...>
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES:

        This class is rather abstract so we showcase its features
        using one of its subclasses::

            sage: P.<x,y,z> = PolynomialRing(Zmod(126))
            sage: I = ideal( x^2 - 3*y, y^3 - x*y, z^3 - x, x^4 - y*z + 1 )
            sage: I.primary_decomposition() # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: Coefficient ring must be a field for function 'primary_decomposition'.
        """
    def __get__(self, inst, cls=None) -> Self:
        """
        EXAMPLES:

        This class is rather abstract so we showcase its features
        using one of its subclasses::

            sage: P.<x,y,z> = PolynomialRing(Zmod(126))
            sage: I = ideal( x^2 - 3*y, y^3 - x*y, z^3 - x, x^4 - y*z + 1 )
            sage: I.primary_decomposition() # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: Coefficient ring must be a field for function 'primary_decomposition'.
        """
