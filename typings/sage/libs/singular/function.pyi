import _cython_3_2_1
import sage.libs.singular.option
import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.interfaces.singular import get_docstring as get_docstring
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.verbose import get_verbose as get_verbose
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal as MPolynomialIdeal, NCPolynomialIdeal as NCPolynomialIdeal
from sage.rings.polynomial.multi_polynomial_sequence import PolynomialSequence_generic as PolynomialSequence_generic
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence, Sequence_generic as Sequence_generic
from typing import Any, ClassVar, overload

__pyx_capi__: dict
all_singular_poly_wrapper: _cython_3_2_1.cython_function_or_method
all_vectors: _cython_3_2_1.cython_function_or_method
arity_dict: dict
error_messages: list
get_printlevel: _cython_3_2_1.cython_function_or_method
is_sage_wrapper_for_singular_ring: _cython_3_2_1.cython_function_or_method
is_singular_poly_wrapper: _cython_3_2_1.cython_function_or_method
lib: _cython_3_2_1.cython_function_or_method
list_of_functions: _cython_3_2_1.cython_function_or_method
opt_ctx: sage.libs.singular.option.LibSingularOptionsContext
set_printlevel: _cython_3_2_1.cython_function_or_method
singular_function: _cython_3_2_1.cython_function_or_method

class BaseCallHandler:
    """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 987)

        A call handler is an abstraction which hides the details of the
        implementation differences between kernel and library functions.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Converter(sage.structure.sage_object.SageObject):
    """Converter(args, ring, attributes=None)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 483)

    A :class:`Converter` interfaces between Sage objects and Singular
    interpreter objects."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, args, ring, attributes=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 489)

                Create a new argument list.

                INPUT:

                - ``args`` -- list of Python objects
                - ``ring`` -- a multivariate polynomial ring
                - ``attributes`` -- an optional dictionary of Singular
                  attributes (default: ``None``)

                EXAMPLES::

                    sage: from sage.libs.singular.function import Converter
                    sage: P.<a,b,c> = PolynomialRing(GF(127))
                    sage: Converter([a,b,c],ring=P)
                    Singular Converter in Multivariate Polynomial Ring in a, b, c over Finite Field of size 127
        """
    @overload
    def ring(self) -> Any:
        """Converter.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 593)

        Return the ring in which the arguments of this list live.

        EXAMPLES::

            sage: from sage.libs.singular.function import Converter
            sage: P.<a,b,c> = PolynomialRing(GF(127))
            sage: Converter([a,b,c],ring=P).ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field of size 127"""
    @overload
    def ring(self) -> Any:
        """Converter.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 593)

        Return the ring in which the arguments of this list live.

        EXAMPLES::

            sage: from sage.libs.singular.function import Converter
            sage: P.<a,b,c> = PolynomialRing(GF(127))
            sage: Converter([a,b,c],ring=P).ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field of size 127"""
    def __len__(self) -> Any:
        """Converter.__len__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 622)

        EXAMPLES::

            sage: from sage.libs.singular.function import Converter
            sage: P.<a,b,c> = PolynomialRing(GF(127))
            sage: len(Converter([a,b,c],ring=P))
            3"""

class KernelCallHandler(BaseCallHandler):
    """KernelCallHandler(cmd_n, arity)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1058)

    A call handler is an abstraction which hides the details of the
    implementation differences between kernel and library functions.

    This class implements calling a kernel function.

    .. NOTE::

        Do not construct this class directly, use
        :func:`singular_function` instead."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, cmd_n, arity) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1070)

                EXAMPLES::

                    sage: from sage.libs.singular.function import KernelCallHandler
                    sage: KernelCallHandler(0,0)
                    <sage.libs.singular.function.KernelCallHandler object at 0x...>
        """

class LibraryCallHandler(BaseCallHandler):
    """LibraryCallHandler()

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1005)

    A call handler is an abstraction which hides the details of the
    implementation differences between kernel and library functions.

    This class implements calling a library function.

    .. NOTE::

        Do not construct this class directly, use
        :func:`singular_function` instead."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1017)

                EXAMPLES::

                    sage: from sage.libs.singular.function import LibraryCallHandler
                    sage: LibraryCallHandler()
                    <sage.libs.singular.function.LibraryCallHandler object at 0x...>
        """

class Resolution:
    """Resolution(base_ring)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 288)

    A simple wrapper around Singular's resolutions."""
    def __init__(self, base_ring) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 292)

                EXAMPLES::

                   sage: from sage.libs.singular.function import singular_function
                   sage: mres = singular_function("mres")
                   sage: syz = singular_function("syz")
                   sage: P.<x,y,z> = PolynomialRing(QQ)
                   sage: I = P.ideal([x+y,x*y-y, y*2,x**2+1])
                   sage: M = syz(I)
                   sage: resolution = mres(M, 0)
        '''

class RingWrap:
    """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 130)

        A simple wrapper around Singular's rings.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def characteristic(self) -> Any:
        '''RingWrap.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 235)

        Get characteristic.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).characteristic()
            0'''
    @overload
    def characteristic(self) -> Any:
        '''RingWrap.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 235)

        Get characteristic.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).characteristic()
            0'''
    @overload
    def is_commutative(self) -> Any:
        '''RingWrap.is_commutative(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 251)

        Determine whether a given ring is commutative.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).is_commutative()
            True'''
    @overload
    def is_commutative(self) -> Any:
        '''RingWrap.is_commutative(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 251)

        Determine whether a given ring is commutative.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).is_commutative()
            True'''
    @overload
    def ngens(self) -> Any:
        '''RingWrap.ngens(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 154)

        Get number of generators.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).ngens()
            3'''
    @overload
    def ngens(self) -> Any:
        '''RingWrap.ngens(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 154)

        Get number of generators.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).ngens()
            3'''
    @overload
    def npars(self) -> Any:
        '''RingWrap.npars(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 186)

        Get number of parameters.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).npars()
            0'''
    @overload
    def npars(self) -> Any:
        '''RingWrap.npars(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 186)

        Get number of parameters.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).npars()
            0'''
    @overload
    def ordering_string(self) -> Any:
        '''RingWrap.ordering_string(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 202)

        Get Singular string defining monomial ordering.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).ordering_string()
            \'dp(3),C\''''
    @overload
    def ordering_string(self) -> Any:
        '''RingWrap.ordering_string(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 202)

        Get Singular string defining monomial ordering.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).ordering_string()
            \'dp(3),C\''''
    @overload
    def par_names(self) -> Any:
        '''RingWrap.par_names(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 218)

        Get parameter names.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).par_names()
            []'''
    @overload
    def par_names(self) -> Any:
        '''RingWrap.par_names(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 218)

        Get parameter names.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).par_names()
            []'''
    @overload
    def var_names(self) -> Any:
        '''RingWrap.var_names(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 170)

        Get names of variables.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).var_names()
            [\'x\', \'y\', \'z\']'''
    @overload
    def var_names(self) -> Any:
        '''RingWrap.var_names(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 170)

        Get names of variables.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: ringlist = singular_function("ringlist")
            sage: l = ringlist(P)
            sage: ring = singular_function("ring")
            sage: ring(l, ring=P).var_names()
            [\'x\', \'y\', \'z\']'''

class SingularFunction(sage.structure.sage_object.SageObject):
    """SingularFunction(name)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1150)

    The base class for Singular functions either from the kernel or
    from the library."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1155)

                INPUT:

                - ``name`` -- the name of the function

                EXAMPLES::

                    sage: from sage.libs.singular.function import SingularFunction
                    sage: SingularFunction('foobar')
                    foobar (singular function)
        """
    def __call__(self, *args, ring=..., boolinterruptible=..., attributes=...) -> Any:
        """SingularFunction.__call__(self, *args, ring=None, bool interruptible=True, attributes=None)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1198)

        Call this function with the provided arguments ``args`` in the
        ``ring``.

        INPUT:

        - ``args`` -- list of arguments
        - ``ring`` -- a multivariate polynomial ring
        - ``interruptible`` -- if ``True`` pressing :kbd:`Ctrl` + :kbd:`C`
          during the execution of this function will interrupt the computation
          (default: ``True``)

        - ``attributes`` -- dictionary of optional Singular
          attributes assigned to Singular objects (default: ``None``)

        If ``ring`` is not specified, it is guessed from the given arguments.
        If this is not possible, then a dummy ring, univariate polynomial ring
        over ``QQ``, is used.

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: size = singular_function('size')
            sage: P.<a,b,c> = PolynomialRing(QQ)
            sage: size(a, ring=P)
            1
            sage: size(2r,ring=P)
            1
            sage: size(2, ring=P)
            1
            sage: size(2)
            1
            sage: size(Ideal([a*b + c, a + 1]))
            2
            sage: size(Ideal([a*b + c, a + 1]))
            2
            sage: size(1,2)
            Traceback (most recent call last):
            ...
            RuntimeError: error in Singular function call 'size':
            Wrong number of arguments (got 2 arguments, arity is CMD_1)
            sage: size('foobar', ring=P)
            6

        Show the usage of the optional ``attributes`` parameter::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([x^3*y^2 + 3*x^2*y^2*z + y^3*z^2 + z^5])
            sage: I = Ideal(I.groebner_basis())
            sage: hilb = sage.libs.singular.function_factory.ff.hilb
            sage: from sage.misc.sage_ostools import redirection
            sage: out = tmp_filename()
            sage: with redirection(sys.stdout,  open(out, 'w')):
            ....:     hilb(I) # Singular will print // ** _ is no standard basis
            sage: with open(out) as f:
            ....:     'is no standard basis' in f.read()
            True

        So we tell Singular that ``I`` is indeed a Groebner basis::

            sage: out = tmp_filename()
            sage: with redirection(sys.stdout,  open(out, 'w')):
            ....:     hilb(I,attributes={I:{'isSB':1}}) # no complaint from Singular
            sage: with open(out) as f:
            ....:     'is no standard basis' in f.read()
            False


        TESTS:

        We show that the interface recovers gracefully from errors::

            sage: P.<e,d,c,b,a> = PolynomialRing(QQ,5,order='lex')
            sage: I = sage.rings.ideal.Cyclic(P)

            sage: triangL = sage.libs.singular.function_factory.ff.triang__lib.triangL
            sage: _ = triangL(I)
            Traceback (most recent call last):
            ...
            RuntimeError: error in Singular function call 'triangL':
            The input is no groebner basis.
            leaving triang.lib::triangL (0)

        Flush any stray output -- see :issue:`28622`::

            sage: sys.stdout.flush()
            ...

            sage: G= Ideal(I.groebner_basis())
            sage: triangL(G,attributes={G:{'isSB':1}})
            [[e + d + c + b + a, ...]]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """SingularFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1412)

        EXAMPLES::

            sage: from sage.libs.singular.function import singular_function
            sage: groebner = singular_function('groebner')
            sage: groebner == loads(dumps(groebner))
            True"""

class SingularKernelFunction(SingularFunction):
    '''SingularKernelFunction(name)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1546)

    EXAMPLES::

        sage: from sage.libs.singular.function import SingularKernelFunction
        sage: R.<x,y> = PolynomialRing(QQ, order=\'lex\')
        sage: I = R.ideal(x, x+1)
        sage: f = SingularKernelFunction("std")
        sage: f(I)
        [1]'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1557)

                Construct a new Singular kernel function.

                EXAMPLES::

                    sage: from sage.libs.singular.function import SingularKernelFunction
                    sage: R.<x,y> = PolynomialRing(QQ, order=\'lex\')
                    sage: I = R.ideal(x + 1, x*y + 1)
                    sage: f = SingularKernelFunction("std")
                    sage: f(I)
                    [y - 1, x + 1]
                    sage: SingularKernelFunction("no_such_function")
                    Traceback (most recent call last):
                    ...
                    NameError: Singular kernel function \'no_such_function\' is not defined
        '''

class SingularLibraryFunction(SingularFunction):
    '''SingularLibraryFunction(name)

    File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1503)

    EXAMPLES::

        sage: from sage.libs.singular.function import SingularLibraryFunction
        sage: R.<x,y> = PolynomialRing(QQ, order=\'lex\')
        sage: I = R.ideal(x, x+1)
        sage: f = SingularLibraryFunction("groebner")
        sage: f(I)
        [1]'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/libs/singular/function.pyx (starting at line 1514)

                Construct a new Singular library function.

                EXAMPLES::

                    sage: from sage.libs.singular.function import SingularLibraryFunction
                    sage: R.<x,y> = PolynomialRing(QQ, order=\'lex\')
                    sage: I = R.ideal(x + 1, x*y + 1)
                    sage: f = SingularLibraryFunction("groebner")
                    sage: f(I)
                    [y - 1, x + 1]
        '''
