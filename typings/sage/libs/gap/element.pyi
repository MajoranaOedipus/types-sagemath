"""
GAP element wrapper

This document describes the individual wrappers for various GAP
elements. For general information about GAP, you should read the
:mod:`~sage.libs.gap.libgap` module documentation.
"""
from typing import overload, Self
from collections.abc import Callable
from typings_sagemath import Int, FloatingSage
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.rational_field import RationalField
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.abc import NumberField_cyclotomic, IntegerModRing
from sage.rings.finite_rings.integer_mod import IntegerMod_int
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.element import RingElement, Element, Matrix, Vector
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject
from sage.libs.gap.libgap import Gap
from sage.combinat.permutation import Permutation

type _Sage = SageObject | None | dict[str, _Sage] | list[_Sage] | bool | str 

class GapElement(RingElement[Gap]):
    r"""
    Wrapper for all Gap objects.

    .. NOTE::

        In order to create ``GapElements`` you should use the
        ``libgap`` instance (the parent of all Gap elements) to
        convert things into ``GapElement``. You must not create
        ``GapElement`` instances manually.

    EXAMPLES::

        sage: libgap(0)
        0

    If Gap finds an error while evaluating, a :exc:`GAPError`
    exception is raised::

        sage: libgap.eval('1/0')
        Traceback (most recent call last):
        ...
        GAPError: Error, Rational operations: <divisor> must not be zero

    Also, a :exc:`GAPError` is raised if the input is not a simple expression::

        sage: libgap.eval('1; 2; 3')
        Traceback (most recent call last):
        ...
        GAPError: can only evaluate a single statement
    """

    def __init__(self):
        """
        The ``GapElement`` constructor.

        Users must use the ``libgap`` instance to construct instances
        of :class:`GapElement`. Cython programmers must use
        :func:`make_GapElement` factory function.

        TESTS::

            sage: from sage.libs.gap.element import GapElement
            sage: GapElement()
            Traceback (most recent call last):
            ...
            TypeError: this class cannot be instantiated from Python
        """
        ...
    def __dealloc__(self) -> None:
        r"""
        The Cython destructor.

        TESTS::

            sage: pre_refcount = libgap.count_GAP_objects()
            sage: def f():
            ....:     local_variable = libgap.eval('"This is a new string"')
            sage: f()
            sage: f()
            sage: f()
            sage: post_refcount = libgap.count_GAP_objects()
            sage: post_refcount - pre_refcount
            0
        """
        ...
    def __copy__(self) -> Self:
        r"""
        TESTS::

            sage: a = libgap(1)
            sage: a.__copy__() is a
            True

            sage: a = libgap(1/3)
            sage: a.__copy__() is a
            True

            sage: a = libgap([1,2])
            sage: b = a.__copy__()
            sage: a is b
            False
            sage: a[0] = 3
            sage: a
            [ 3, 2 ]
            sage: b
            [ 1, 2 ]

            sage: a = libgap([[0,1],[2,3,4]])
            sage: b = a.__copy__()
            sage: b[0][1] = -2
            sage: b
            [ [ 0, -2 ], [ 2, 3, 4 ] ]
            sage: a
            [ [ 0, -2 ], [ 2, 3, 4 ] ]
        """
        ...
    def deepcopy(self, mut: bool) -> GapElement:
        r"""
        Return a deepcopy of this Gap object.

        Note that this is the same thing as calling ``StructuralCopy`` but much
        faster.

        INPUT:

        - ``mut`` -- boolean; whether to return a mutable copy

        EXAMPLES::

            sage: a = libgap([[0,1],[2,3]])
            sage: b = a.deepcopy(1)
            sage: b[0,0] = 5
            sage: a
            [ [ 0, 1 ], [ 2, 3 ] ]
            sage: b
            [ [ 5, 1 ], [ 2, 3 ] ]

            sage: l = libgap([0,1])
            sage: l.deepcopy(0).IsMutable()
            false
            sage: l.deepcopy(1).IsMutable()
            true
        """
        ...
    def __deepcopy__(self, memo):
        r"""
        TESTS::

            sage: a = libgap([[0,1],[2]])
            sage: b = deepcopy(a)
            sage: a[0,0] = -1
            sage: a
            [ [ -1, 1 ], [ 2 ] ]
            sage: b
            [ [ 0, 1 ], [ 2 ] ]
        """
        ...
    def __reduce__(self) -> tuple[Callable[[str | SageObject], GapElement], str | SageObject]:
        """
        Attempt to pickle GAP elements from libgap.

        This is inspired in part by
        ``sage.interfaces.interface.Interface._reduce``, though for a fallback
        we use ``str(self)`` instead of ``repr(self)``, since the former is
        equivalent in the libgap interface to the latter in the pexpect
        interface.

        TESTS:

        This workaround was motivated in particular by this example from the
        permutation groups implementation::

            sage: CC = libgap.eval('ConjugacyClass(SymmetricGroup([ 1 .. 5 ]), (1,2)(3,4))')
            sage: CC.sage()
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot construct equivalent Sage object
            sage: libgap.eval(str(CC))
            (1,2)(3,4)^G
            sage: loads(dumps(CC))
            (1,2)(3,4)^G
        """
        ...
    def __contains__(self, other: object) -> bool:
        r"""
        TESTS::

            sage: libgap(1) in libgap.eval('Integers')
            True
            sage: 1 in libgap.eval('Integers')
            True

            sage: 3 in libgap([1,5,3,2])
            True
            sage: -5 in libgap([1,5,3,2])
            False

            sage: libgap.eval('Integers') in libgap(1)
            Traceback (most recent call last):
            ...
            GAPError: Error, no method found! Error, no 1st choice method found for `in' on 2 arguments
        """
        ...
    def __dir__(self) -> list[str]:
        """
        Customize tab completion.

        EXAMPLES::

            sage: G = libgap.DihedralGroup(4)
            sage: 'GeneratorsOfMagmaWithInverses' in dir(G)
            True
            sage: 'GeneratorsOfGroup' in dir(G)    # known bug
            False
            sage: x = libgap(1)
            sage: len(dir(x)) > 100
            True
        """
        ...
    def __getattr__(self, name: str) -> GapElement_MethodProxy:
        r"""
        Return functionoid implementing the function ``name``.

        EXAMPLES::

            sage: lst = libgap([])
            sage: 'Add' in dir(lst)    # This is why tab-completion works
            True
            sage: lst.Add(1)    # this is the syntactic sugar
            sage: lst
            [ 1 ]

        The above is equivalent to the following calls::

            sage: lst = libgap.eval('[]')
            sage: libgap.eval('Add') (lst, 1)
            sage: lst
            [ 1 ]

        TESTS::

            sage: lst.Adddddd(1)
            Traceback (most recent call last):
            ...
            AttributeError: 'Adddddd' is not defined in GAP

            sage: libgap.eval('some_name := 1')
            1
            sage: lst.some_name
            Traceback (most recent call last):
            ...
            AttributeError: 'some_name' does not define a GAP function
        """
        ...
    def __str__(self) -> str:
        r"""
        Return a string representation of ``self`` for printing.

        EXAMPLES::

            sage: libgap(0)
            0
            sage: print(libgap.eval(''))
            None
            sage: print(libgap('a'))
            a
            sage: print(libgap.eval('SymmetricGroup(3)'))
            SymmetricGroup( [ 1 .. 3 ] )
            sage: libgap(0).__str__()
            '0'
        """
        ...
    def __hash__(self) -> int:
        """
        Make hashable.

        EXAMPLES::

            sage: hash(libgap(123))   # random output
            163512108404620371
        """
        return hash(str(self))
    def is_bool(self)-> int:
        r"""
        Return whether the wrapped GAP object is a GAP boolean.

        OUTPUT: boolean

        EXAMPLES::

            sage: libgap(True).is_bool()
            True
        """
        ...
    def is_function(self) -> bool:
        """
        Return whether the wrapped GAP object is a function.

        OUTPUT: boolean

        EXAMPLES::

            sage: a = libgap.eval("NormalSubgroups")
            sage: a.is_function()
            True
            sage: a = libgap(2/3)
            sage: a.is_function()
            False
        """
        ...
    def is_list(self) -> bool:
        r"""
        Return whether the wrapped GAP object is a GAP List.

        OUTPUT: boolean

        EXAMPLES::

            sage: libgap.eval('[1, 2,,,, 5]').is_list()
            True
            sage: libgap.eval('3/2').is_list()
            False
        """
        ...
    def is_string(self) -> bool:
        r"""
        Return whether the wrapped GAP object is a GAP string.

        OUTPUT: boolean

        EXAMPLES::

            sage: libgap('this is a string').is_string()
            True
        """
        ...
    def is_permutation(self) -> bool:
        r"""
        Return whether the wrapped GAP object is a GAP permutation.

        OUTPUT: boolean

        EXAMPLES::

            sage: perm = libgap.PermList( libgap([1,5,2,3,4]) );  perm
            (2,5,4,3)
            sage: perm.is_permutation()
            True
            sage: libgap('this is a string').is_permutation()
            False
        """
        ...
    def sage(self) -> _Sage:  # subclass can returns list, dict, etc
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        EXAMPLES::

            sage: libgap(1).sage()
            1
            sage: type(_)
            <class 'sage.rings.integer.Integer'>

            sage: libgap(3/7).sage()
            3/7
            sage: type(_)
            <class 'sage.rings.rational.Rational'>

            sage: libgap.eval('5 + 7*E(3)').sage()
            7*zeta3 + 5

            sage: libgap(Infinity).sage()
            +Infinity
            sage: libgap(-Infinity).sage()
            -Infinity

            sage: libgap(True).sage()
            True
            sage: libgap(False).sage()
            False
            sage: type(_)
            <... 'bool'>

            sage: libgap('this is a string').sage()
            'this is a string'
            sage: type(_)
            <... 'str'>

            sage: x = libgap.Integers.Indeterminate("x")

            sage: p = x^2 - 2*x + 3
            sage: p.sage()
            x^2 - 2*x + 3
            sage: p.sage().parent()
            Univariate Polynomial Ring in x over Integer Ring

            sage: p = x^-2 + 3*x
            sage: p.sage()
            x^-2 + 3*x
            sage: p.sage().parent()
            Univariate Laurent Polynomial Ring in x over Integer Ring

            sage: p = (3 * x^2 + x) / (x^2 - 2)
            sage: p.sage()
            (3*x^2 + x)/(x^2 - 2)
            sage: p.sage().parent()
            Fraction Field of Univariate Polynomial Ring in x over Integer Ring

            sage: G0 = libgap.SymplecticGroup(4,2)
            sage: P = G0.IsomorphismFpGroup().Range()
            sage: G = P.sage()
            sage: G.gap() == P
            True

            sage: F0 = libgap.FreeGroup(2)
            sage: F = F0.sage()
            sage: F.gap() is F0
            True

        TESTS:

        Check :issue:`30496`::

            sage: x = libgap.Integers.Indeterminate("x")
            sage: p = x^2 - 2*x
            sage: p.sage()
            x^2 - 2*x
        """
        ...

class GapElement_Ring(GapElement):
    r"""
    Derived class of GapElement for GAP rings (parents of ring elements).

    EXAMPLES::

        sage: i = libgap(ZZ)
        sage: type(i)
        <class 'sage.libs.gap.element.GapElement_Ring'>
    """

    def ring_integer(self) -> IntegerRing_class:
        """
        Construct the Sage integers.

        This method is not meant to be called directly, use :meth:`sage` instead.

        TESTS::

            sage: libgap.eval('Integers').ring_integer()
            Integer Ring
        """
        ...

    def ring_rational(self) -> RationalField:
        """
        Construct the Sage rationals.

        This method is not meant to be called directly, use :meth:`sage` instead.

        TESTS::

            sage: libgap.eval('Rationals').ring_rational()
            Rational Field
        """
        ...

    def ring_integer_mod(self) -> IntegerModRing:
        """
        Construct a Sage integer mod ring.

        This method is not meant to be called directly, use :meth:`sage` instead.

        TESTS::

            sage: libgap.eval('ZmodnZ(15)').ring_integer_mod()
            Ring of integers modulo 15
        """
        ...

    def ring_finite_field(self, var: str='a') -> FiniteField:
        """
        Construct a finite field.

        This method is not meant to be called directly, use :meth:`sage` instead.

        Note that for non-prime finite fields, this method is likely **unintended**,
        it always use the default-constructed finite field with ``var`` provided,
        which means the ``DefiningPolynomial`` of the GAP field is often not the same as the
        ``.modulus()`` of the Sage field. They are isomorphic, but the isomorphism may be
        difficult to compute.

        INPUT:

        - ``var`` -- string (default: 'a'); name of the generator of the finite field

        TESTS::

            sage: libgap.GF(3,2).ring_finite_field(var='A')
            Finite Field in A of size 3^2
        """
        ...

    def ring_cyclotomic(self) -> NumberField_cyclotomic:
        """
        Construct a cyclotomic field.

        This method is not meant to be called directly, use :meth:`sage` instead.

        TESTS::

            sage: libgap.CyclotomicField(6).ring_cyclotomic()
            Cyclotomic Field of order 3 and degree 2
        """
        ...

    def ring_polynomial(self) -> PolynomialRing_generic:
        """
        Construct a polynomial ring.

        This method is not meant to be called directly, use :meth:`sage` instead.

        TESTS::

            sage: B = libgap(QQ['x'])
            sage: B.ring_polynomial()
            Univariate Polynomial Ring in x over Rational Field

            sage: B = libgap(ZZ['x','y'])
            sage: B.ring_polynomial()
            Multivariate Polynomial Ring in x, y over Integer Ring
        """
        ...

    def sage(self, **kwds) -> RingElement:
        r"""
        Return the Sage equivalent of the :class:`GapElement_Ring`.

        INPUT:

        - ``**kwds`` -- keywords that are passed on to the ``ring_``
          method

        OUTPUT: a Sage ring

        EXAMPLES::

            sage: libgap.eval('Integers').sage()
            Integer Ring

            sage: libgap.eval('Rationals').sage()
            Rational Field

            sage: libgap.eval('ZmodnZ(15)').sage()
            Ring of integers modulo 15

            sage: libgap.GF(3,2).sage(var='A')
            Finite Field in A of size 3^2

            sage: libgap.CyclotomicField(6).sage()
            Cyclotomic Field of order 3 and degree 2

            sage: libgap(QQ['x','y']).sage()
            Multivariate Polynomial Ring in x, y over Rational Field
        """
        ...

class GapElement_Rational(GapElement):
    r"""
    Derived class of GapElement for GAP rational numbers.

    EXAMPLES::

        sage: r = libgap(123/456)
        sage: type(r)
        <class 'sage.libs.gap.element.GapElement_Rational'>
    """
    
    def sage(self, ring=None) -> Rational:
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        INPUT:

        - ``ring`` -- the Sage rational ring or ``None`` (default); if
          not specified, the rational ring is used automatically

        OUTPUT: a Sage rational number

        EXAMPLES::

            sage: r = libgap(123/456);  r
            41/152
            sage: type(_)
            <class 'sage.libs.gap.element.GapElement_Rational'>
            sage: r.sage()
            41/152
            sage: type(_)
            <class 'sage.rings.rational.Rational'>
        """
        ...

class GapElement_Cyclotomic(GapElement):
    r"""
    Derived class of GapElement for GAP universal cyclotomics.

    EXAMPLES::

        sage: libgap.eval('E(3)')
        E(3)
        sage: type(_)
        <class 'sage.libs.gap.element.GapElement_Cyclotomic'>
    """

    def sage(self, ring=None) -> NumberFieldElement:
        r"""
        Return the Sage equivalent of the :class:`GapElement_Cyclotomic`.

        INPUT:

        - ``ring`` -- a Sage cyclotomic field or ``None``
          (default); if not specified, a suitable minimal cyclotomic
          field will be constructed

        OUTPUT: a Sage cyclotomic field element

        EXAMPLES::

            sage: n = libgap.eval('E(3)')
            sage: n.sage()
            zeta3
            sage: parent(_)
            Cyclotomic Field of order 3 and degree 2

            sage: n.sage(ring=CyclotomicField(6))
            zeta6 - 1

            sage: libgap.E(3).sage(ring=CyclotomicField(3))
            zeta3
            sage: libgap.E(3).sage(ring=CyclotomicField(6))
            zeta6 - 1

        TESTS:

        Check that :issue:`15204` is fixed::

            sage: libgap.E(3).sage(ring=UniversalCyclotomicField())
            E(3)
            sage: libgap.E(3).sage(ring=CC)
            -0.500000000000000 + 0.866025403784439*I
        """
        ...

class GapElement_FiniteField(GapElement):
    r"""
    Derived class of GapElement for GAP finite field elements.

    EXAMPLES::

        sage: libgap.eval('Z(5)^2')
        Z(5)^2
        sage: type(_)
        <class 'sage.libs.gap.element.GapElement_FiniteField'>
    """

    def lift(self) -> GapElement_Integer:
        """
        Return an integer lift.

        OUTPUT:

        The smallest positive :class:`GapElement_Integer` that equals
        ``self`` in the prime finite field.

        EXAMPLES::

            sage: n = libgap.eval('Z(5)^2')
            sage: n.lift()
            4
            sage: type(_)
            <class 'sage.libs.gap.element.GapElement_Integer'>

            sage: n = libgap.eval('Z(25)')
            sage: n.lift()
            Traceback (most recent call last):
            TypeError: not in prime subfield
        """
        ...

    def sage(self, ring=None, var='a') -> FiniteRingElement:
        r"""
        Return the Sage equivalent of the :class:`GapElement_FiniteField`.

        INPUT:

        - ``ring`` -- a Sage finite field or ``None`` (default). The
          field to return ``self`` in. If not specified, a suitable
          finite field will be constructed.

        OUTPUT:

        A Sage finite field element. The isomorphism is chosen such
        that the Gap ``PrimitiveRoot()`` maps to the Sage
        :meth:`~sage.rings.finite_rings.finite_field_prime_modn.multiplicative_generator`.

        EXAMPLES::

            sage: n = libgap.eval('Z(25)^2')
            sage: n.sage()
            a + 3
            sage: parent(_)
            Finite Field in a of size 5^2

            sage: n.sage(ring=GF(5))
            Traceback (most recent call last):
            ...
            ValueError: the given ring is incompatible ...

        TESTS::

            sage: n = libgap.eval('Z(2^4)^2 + Z(2^4)^1 + Z(2^4)^0')
            sage: n
            Z(2^2)^2
            sage: n.sage()
            a + 1
            sage: parent(_)
            Finite Field in a of size 2^2
            sage: n.sage(ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: the given ring is incompatible ...
            sage: n.sage(ring=CC)
            Traceback (most recent call last):
            ...
            ValueError: the given ring is incompatible ...
            sage: n.sage(ring=GF(5))
            Traceback (most recent call last):
            ...
            ValueError: the given ring is incompatible ...
            sage: n.sage(ring=GF(2^3))
            Traceback (most recent call last):
            ...
            ValueError: the given ring is incompatible ...
            sage: n.sage(ring=GF(2^2, 'a'))
            a + 1
            sage: n.sage(ring=GF(2^4, 'a'))
            a^2 + a + 1
            sage: n.sage(ring=GF(2^8, 'a'))
            a^7 + a^6 + a^4 + a^2 + a + 1
            sage: (n^3).sage()
            1

        Check that :issue:`23153` is fixed::

            sage: n = libgap.eval('Z(2^4)^2 + Z(2^4)^1 + Z(2^4)^0')
            sage: n.sage(ring=GF(2^4, 'a'))
            a^2 + a + 1
        """
        ...

    def __int__(self) -> int:
        r"""
        TESTS::

            sage: int(libgap.eval("Z(53)"))
            2
        """
        ...

class GapElement_IntegerMod(GapElement):
    r"""
    Derived class of GapElement for GAP integers modulo an integer.

    EXAMPLES::

        sage: n = IntegerModRing(123)(13)
        sage: i = libgap(n)
        sage: type(i)
        <class 'sage.libs.gap.element.GapElement_IntegerMod'>
    """

    def lift(self) -> GapElement_Integer:
        """
        Return an integer lift.

        OUTPUT:

        A :class:`GapElement_Integer` that equals ``self`` in the
        integer mod ring.

        EXAMPLES::

            sage: n = libgap.eval('One(ZmodnZ(123)) * 13')
            sage: n.lift()
            13
            sage: type(_)
            <class 'sage.libs.gap.element.GapElement_Integer'>
        """
        ...

    @overload
    def sage(self) -> IntegerMod_int: ...
    @overload
    def sage[P: Parent](self, ring: P) -> Element[P]:
        r"""
        Return the Sage equivalent of the :class:`GapElement_IntegerMod`.

        INPUT:

        - ``ring`` -- Sage integer mod ring or ``None`` (default); if
          not specified, a suitable integer mod ring is used
          automatically

        OUTPUT: a Sage integer modulo another integer

        EXAMPLES::

            sage: n = libgap.eval('One(ZmodnZ(123)) * 13')
            sage: n.sage()
            13
            sage: parent(_)
            Ring of integers modulo 123
        """
        if ring is None:
            # ring = self.DefaultRing().sage()
            characteristic = self.Characteristic().sage()
            ring = ZZ.quotient_ring(characteristic)
        return ring(self.lift())

class GapElement_Float(GapElement):
    r"""
    Derived class of GapElement for GAP floating point numbers.

    EXAMPLES::

        sage: i = libgap(123.5)
        sage: type(i)
        <class 'sage.libs.gap.element.GapElement_Float'>
        sage: RDF(i)
        123.5
        sage: float(i)
        123.5

    TESTS::

        sage: a = RDF.random_element()
        sage: libgap(a).sage() == a
        True
    """
    def sage(self, ring=None) -> FloatingSage:
        r"""
        Return the Sage equivalent of the :class:`GapElement_Float`.

        - ``ring`` -- a floating point field or ``None`` (default); if not
          specified, the default Sage ``RDF`` is used

        OUTPUT: a Sage double precision floating point number

        EXAMPLES::

            sage: a = libgap.eval("Float(3.25)").sage()
            sage: a
            3.25
            sage: parent(a)
            Real Double Field
        """
        ...

    def __float__(self) -> float:
        r"""
        TESTS::

            sage: float(libgap.eval("Float(3.5)"))
            3.5
        """
        ...

class GapElement_MethodProxy(GapElement_Function):
    r"""
    Helper class returned by ``GapElement.__getattr__``.

    Derived class of GapElement for GAP functions. Like its parent,
    you can call instances to implement function call syntax. The only
    difference is that a fixed first argument is prepended to the
    argument list.

    EXAMPLES::

        sage: lst = libgap([])
        sage: lst.Add
        <Gap function "Add">
        sage: type(_)
        <class 'sage.libs.gap.element.GapElement_MethodProxy'>
        sage: lst.Add(1)
        sage: lst
        [ 1 ]
    """

    def __call__(self, *args) -> GapElement | None:
        """
        Call syntax for methods.

        This method is analogous to
        :meth:`GapElement_Function.__call__`, except that it inserts a
        fixed :class:`GapElement` in the first slot of the function.

        INPUT:

        - ``*args`` -- arguments. Will be converted to `GapElement` if
          they are not already of this type

        OUTPUT:

        A :class:`GapElement` encapsulating the functions return
        value, or ``None`` if it does not return anything.

        EXAMPLES::

            sage: lst = libgap.eval('[1,,3]')
            sage: lst.Add.__call__(4)
            sage: lst.Add(5)
            sage: lst
            [ 1,, 3, 4, 5 ]
        """
        ...

class GapElement_Function(GapElement):
    r"""
    Derived class of GapElement for GAP functions.

    EXAMPLES::

        sage: f = libgap.Cycles
        sage: type(f)
        <class 'sage.libs.gap.element.GapElement_Function'>
    """

    def __repr__(self) -> str:
        r"""
        Return a string representation.

        OUTPUT: string

        EXAMPLES::

            sage: libgap.Orbits
            <Gap function "Orbits">
        """
        ...
    def __call__(self, *args) -> GapElement | None:
        """
        Call syntax for functions.

        INPUT:

        - ``*args`` -- arguments. Will be converted to `GapElement` if
          they are not already of this type

        OUTPUT:

        A :class:`GapElement` encapsulating the functions return
        value, or ``None`` if it does not return anything.

        EXAMPLES::

            sage: a = libgap.NormalSubgroups
            sage: b = libgap.SymmetricGroup(4)
            sage: libgap.collect()
            sage: a
            <Gap function "NormalSubgroups">
            sage: b
            Sym( [ 1 .. 4 ] )
            sage: [x.StructureDescription() for x in sorted(a(b))]
            ["1", "S4", "A4", "C2 x C2"]

            sage: libgap.eval("a := NormalSubgroups")
            <Gap function "NormalSubgroups">
            sage: libgap.eval("b := SymmetricGroup(4)")
            Sym( [ 1 .. 4 ] )
            sage: libgap.collect()
            sage: [x.StructureDescription() for x in sorted(libgap.eval('a') (libgap.eval('b')))]
            ["1", "S4", "A4", "C2 x C2"]

            sage: a = libgap.eval('a')
            sage: b = libgap.eval('b')
            sage: libgap.collect()
            sage: [x.StructureDescription() for x in sorted(a(b))]
            ["1", "S4", "A4", "C2 x C2"]

        Not every ``GapElement`` is callable::

            sage: f = libgap(3)
            sage: f()
            Traceback (most recent call last):
            ...
            TypeError: 'sage.libs.gap.element.GapElement_Integer' object is not callable

        We illustrate appending to a list which returns None::

            sage: a = libgap([]); a
            [  ]
            sage: a.Add(5); a
            [ 5 ]
            sage: a.Add(10); a
            [ 5, 10 ]

        TESTS::

            sage: s = libgap.Sum
            sage: s(libgap([1,2]))
            3
            sage: s(libgap(1), libgap(2))
            Traceback (most recent call last):
            ...
            GAPError: Error, no method found!
            Error, no 1st choice method found for `SumOp' on 2 arguments

            sage: for i in range(100):
            ....:     rnd = [ randint(-10,10) for i in range(randint(0,7)) ]
            ....:     # compute the sum in GAP
            ....:     _ = libgap.Sum(rnd)
            ....:     try:
            ....:         libgap.Sum(*rnd)
            ....:         print('This should have triggered a ValueError')
            ....:         print('because Sum needs a list as argument')
            ....:     except ValueError:
            ....:         pass

            sage: libgap_exec = libgap.eval("Exec")
            sage: libgap_exec('echo hello from the shell')
            hello from the shell
        """
        ...

class GapElement_List(GapElement):
    r"""
    Derived class of GapElement for GAP Lists.

    .. NOTE::

        Lists are indexed by `0..len(l)-1`, as expected from
        Python. This differs from the GAP convention where lists start
        at `1`.

    EXAMPLES::

        sage: lst = libgap.SymmetricGroup(3).List(); lst
        [ (), (1,3), (1,2,3), (2,3), (1,3,2), (1,2) ]
        sage: type(lst)
        <class 'sage.libs.gap.element.GapElement_List'>
        sage: len(lst)
        6
        sage: lst[3]
        (2,3)

    We can easily convert a Gap ``List`` object into a Python ``list``::

        sage: list(lst)
        [(), (1,3), (1,2,3), (2,3), (1,3,2), (1,2)]
        sage: type(_)
        <... 'list'>

    Range checking is performed::

        sage: lst[10]
        Traceback (most recent call last):
        ...
        IndexError: index out of range.
    """

    def __bool__(self) -> bool:
        r"""
        Return ``True`` if the list is non-empty, as with Python ``list``s.

        EXAMPLES::

            sage: lst = libgap.eval('[1,,,4]')
            sage: bool(lst)
            True
            sage: lst = libgap.eval('[]')
            sage: bool(lst)
            False
        """
    def __len__(self) -> int:
        r"""
        Return the length of the list.

        OUTPUT: integer

        EXAMPLES::

            sage: lst = libgap.eval('[1,,,4]')   # a sparse list
            sage: len(lst)
            4
        """
        ...
    def __getitem__(self, i: Int | tuple[Int, ...]) -> GapElement:
        r"""
        Return the ``i``-th element of the list.

        As usual in Python, indexing starts at `0` and not at `1` (as
        in GAP). This can also be used with multi-indices.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        The ``i``-th element as a :class:`GapElement`.

        EXAMPLES::

            sage: lst = libgap.eval('["first",,,"last"]')   # a sparse list
            sage: lst[0]
            "first"

            sage: l = libgap.eval('[ [0, 1], [2, 3] ]')
            sage: l[0,0]
            0
            sage: l[0,1]
            1
            sage: l[1,0]
            2
            sage: l[0,2]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: l[2,0]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: l[0,0,0]
            Traceback (most recent call last):
            ...
            ValueError: too many indices
        """
        ...
    def __setitem__(self, i: Int | tuple[Int, ...], elt) -> None:
        r"""
        Set the `i`-th item of this list.

        EXAMPLES::

            sage: l = libgap.eval('[0, 1]')
            sage: l
            [ 0, 1 ]
            sage: l[0] = 3
            sage: l
            [ 3, 1 ]

        Contrarily to Python lists, setting an element beyond the limit extends the list::

            sage: l[12] = -2
            sage: l
            [ 3, 1,,,,,,,,,,, -2 ]

        This function also handles multi-indices::

            sage: l = libgap.eval('[[[0,1],[2,3]],[[4,5], [6,7]]]')
            sage: l[0,1,0] = -18
            sage: l
            [ [ [ 0, 1 ], [ -18, 3 ] ], [ [ 4, 5 ], [ 6, 7 ] ] ]
            sage: l[0,0,0,0]
            Traceback (most recent call last):
            ...
            ValueError: too many indices

        Assignment to immutable objects gives error::

            sage: l = libgap([0,1])
            sage: u = l.deepcopy(0)
            sage: u[0] = 5
            Traceback (most recent call last):
            ...
            TypeError: immutable Gap object does not support item assignment

        TESTS::

            sage: m = libgap.eval('[[0,0],[0,0]]')
            sage: m[0,0] = 1
            sage: m[0,1] = 2
            sage: m[1,0] = 3
            sage: m[1,1] = 4
            sage: m
            [ [ 1, 2 ], [ 3, 4 ] ]
        """
        ...
    def sage(self, **kwds) -> list[_Sage]:
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        OUTPUT: a Python list

        EXAMPLES::

            sage: libgap([ 1, 3, 4 ]).sage()
            [1, 3, 4]
            sage: all( x in ZZ for x in _ )
            True
        """
        return [x.sage(**kwds) for x in self]
    def matrix(self, ring=None) -> Matrix:
        """
        Return the list as a matrix.

        GAP does not have a special matrix data type, they are just
        lists of lists. This function converts a GAP list of lists to
        a Sage matrix.

        OUTPUT: a Sage matrix

        EXAMPLES::

            sage: F = libgap.GF(4)
            sage: a = F.PrimitiveElement()
            sage: m = libgap([[a,a^0],[0*a,a^2]]); m
            [ [ Z(2^2), Z(2)^0 ],
              [ 0*Z(2), Z(2^2)^2 ] ]
            sage: m.IsMatrix()
            true
            sage: matrix(m)
            [    a     1]
            [    0 a + 1]
            sage: matrix(GF(4,'B'), m)
            [    B     1]
            [    0 B + 1]

            sage: M = libgap.eval('SL(2,GF(5))').GeneratorsOfGroup()[1]
            sage: type(M)
            <class 'sage.libs.gap.element.GapElement_List'>
            sage: M[0][0]
            Z(5)^2
            sage: M.IsMatrix()
            true
            sage: M.matrix()
            [4 1]
            [4 0]
        """
        ...
    def vector(self, ring=None) -> Vector:
        """
        Return the list as a vector.

        GAP does not have a special vector data type, they are just
        lists. This function converts a GAP list to a Sage vector.

        OUTPUT: a Sage vector

        EXAMPLES::

            sage: F = libgap.GF(4)
            sage: a = F.PrimitiveElement()
            sage: m = libgap([0*a, a, a^3, a^2]); m
            [ 0*Z(2), Z(2^2), Z(2)^0, Z(2^2)^2 ]
            sage: type(m)
            <class 'sage.libs.gap.element.GapElement_List'>
            sage: m[3]
            Z(2^2)^2
            sage: vector(m)
            (0, a, 1, a + 1)
            sage: vector(GF(4,'B'), m)
            (0, B, 1, B + 1)
        """
        ...

class GapElement_Boolean(GapElement):
    r"""
    Derived class of GapElement for GAP boolean values.

    EXAMPLES::

        sage: b = libgap(True)
        sage: type(b)
        <class 'sage.libs.gap.element.GapElement_Boolean'>
    """

    def sage(self) -> bool:
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        OUTPUT:

        A Python boolean if the values is either true or false. GAP
        booleans can have the third value ``Fail``, in which case a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: b = libgap.eval('true');  b
            true
            sage: type(_)
            <class 'sage.libs.gap.element.GapElement_Boolean'>
            sage: b.sage()
            True
            sage: type(_)
            <... 'bool'>

            sage: libgap.eval('fail')
            fail
            sage: _.sage()
            Traceback (most recent call last):
            ...
            ValueError: the GAP boolean value "fail" cannot be represented in Sage
        """
        ...
    def __bool__(self) -> bool:
        """
        Check that the boolean is "true".

        This is syntactic sugar for using libgap. See the examples below.

        OUTPUT: boolean

        EXAMPLES::

            sage: gap_bool = [libgap.eval('true'), libgap.eval('false'), libgap.eval('fail')]
            sage: for x in gap_bool:
            ....:     if x:     # this calls __bool__
            ....:         print("{} {}".format(x, type(x)))
            true <class 'sage.libs.gap.element.GapElement_Boolean'>

            sage: for x in gap_bool:
            ....:     if not x:     # this calls __bool__
            ....:         print("{} {}".format( x, type(x)))
            false <class 'sage.libs.gap.element.GapElement_Boolean'>
            fail <class 'sage.libs.gap.element.GapElement_Boolean'>
        """
        ...

class GapElement_String(GapElement):
    r"""
    Derived class of GapElement for GAP strings.

    EXAMPLES::

        sage: s = libgap('string')
        sage: type(s)
        <class 'sage.libs.gap.element.GapElement_String'>
        sage: s
        "string"
        sage: print(s)
        string
    """
    def __str__(self) -> str:
        r"""
        Convert this :class:`GapElement_String` to a Python string.

        OUTPUT: a Python string

        EXAMPLES::

            sage: s = libgap.eval(' "string" '); s
            "string"
            sage: type(_)
            <class 'sage.libs.gap.element.GapElement_String'>
            sage: str(s)
            'string'
            sage: s.sage()
            'string'
            sage: type(_)
            <class 'str'>
        """
        ...

    sage = __str__

class GapElement_Integer(GapElement):
    r"""
    Derived class of GapElement for GAP integers.

    EXAMPLES::

        sage: i = libgap(123)
        sage: type(i)
        <class 'sage.libs.gap.element.GapElement_Integer'>
        sage: ZZ(i)
        123
    """

    def is_C_int(self) -> bool:
        r"""
        Return whether the wrapped GAP object is a immediate GAP integer.

        An immediate integer is one that is stored as a C integer, and
        is subject to the usual size limits. Larger integers are
        stored in GAP as GMP integers.

        OUTPUT: boolean

        EXAMPLES::

            sage: n = libgap(1)
            sage: type(n)
            <class 'sage.libs.gap.element.GapElement_Integer'>
            sage: n.is_C_int()
            True
            sage: n.IsInt()
            true

            sage: N = libgap(2^130)
            sage: type(N)
            <class 'sage.libs.gap.element.GapElement_Integer'>
            sage: N.is_C_int()
            False
            sage: N.IsInt()
            true
        """
        ...
    @overload
    def sage[_Int: Int](self, ring: type[_Int]) -> _Int: ...
    @overload
    def sage[P: Parent](self, ring: P) -> RingElement[P]: ...
    @overload
    def sage(self) -> Integer:
        r"""
        Return the Sage equivalent of the :class:`GapElement_Integer`.

        - ``ring`` -- integer ring or ``None`` (default); if not
          specified, the default Sage integer ring is used

        OUTPUT: a Sage integer

        EXAMPLES::

            sage: libgap([ 1, 3, 4 ]).sage()
            [1, 3, 4]
            sage: all( x in ZZ for x in _ )
            True

            sage: libgap(132).sage(ring=IntegerModRing(13))
            2
            sage: parent(_)
            Ring of integers modulo 13

        TESTS::

            sage: libgap(0).sage()
            0
            sage: large = libgap.eval('2^130');  large
            1361129467683753853853498429727072845824
            sage: large.sage()
            1361129467683753853853498429727072845824

            sage: huge = libgap.eval('10^9999');  huge     # gap abbreviates very long ints
            <integer 100...000 (10000 digits)>
            sage: huge.sage().ndigits()
            10000
        """
        ...
    def __int__(self) -> int:
        r"""
        TESTS::

            sage: int(libgap(3))
            3
            sage: type(_)
            <class 'int'>

            sage: int(libgap(2)**128)
            340282366920938463463374607431768211456
            sage: type(_)
            <class 'int'>
        """
        ...
    def __index__(self) -> int:
        r"""
        TESTS:

        Check that gap integers can be used as indices (:issue:`23878`)::

            sage: s = 'abcd'
            sage: s[libgap(1)]
            'b'
        """
        ...

class GapElement_Permutation(GapElement):
    r"""
    Derived class of GapElement for GAP permutations.

    .. NOTE::

        Permutations in GAP act on the numbers starting with 1.

    EXAMPLES::

        sage: perm = libgap.eval('(1,5,2)(4,3,8)')
        sage: type(perm)
        <class 'sage.libs.gap.element.GapElement_Permutation'>
    """

    @overload
    def sage(self) -> Permutation: ...
    @overload
    def sage[P: Parent](self, parent: P | None = None) -> Element[P]:
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        If the permutation group is given as parent, this method is
        *much* faster.

        EXAMPLES::

            sage: perm_gap = libgap.eval('(1,5,2)(4,3,8)');  perm_gap
            (1,5,2)(3,8,4)
            sage: perm_gap.sage()
            [5, 1, 8, 3, 2, 6, 7, 4]
            sage: type(_)
            <class 'sage.combinat.permutation.StandardPermutations_all_with_category.element_class'>
            sage: perm_gap.sage(PermutationGroup([(1,2),(1,2,3,4,5,6,7,8)]))
            (1,5,2)(3,8,4)
            sage: type(_)
            <class 'sage.groups.perm_gps.permgroup_element.PermutationGroupElement'>
        """

class GapElement_Record(GapElement):
    r"""
    Derived class of GapElement for GAP records.

    EXAMPLES::

        sage: rec = libgap.eval('rec(a:=123, b:=456)')
        sage: type(rec)
        <class 'sage.libs.gap.element.GapElement_Record'>
        sage: len(rec)
        2
        sage: rec['a']
        123

    We can easily convert a Gap ``rec`` object into a Python ``dict``::

        sage: dict(rec)
        {'a': 123, 'b': 456}
        sage: type(_)
        <... 'dict'>

    Range checking is performed::

        sage: rec['no_such_element']
        Traceback (most recent call last):
        ...
        GAPError: Error, Record Element: '<rec>.no_such_element' must have an assigned value
    """

    def __len__(self) -> int:
        r"""
        Return the length of the record.

        OUTPUT: integer; the number of entries in the record

        EXAMPLES::

            sage: rec = libgap.eval('rec(a:=123, b:=456, S3:=SymmetricGroup(3))')
            sage: len(rec)
            3
        """
        ...
    def __iter__(self) -> GapElement_RecordIterator:
        r"""
        Iterate over the elements of the record.

        OUTPUT: a :class:`GapElement_RecordIterator`

        EXAMPLES::

            sage: rec = libgap.eval('rec(a:=123, b:=456)')
            sage: iter = rec.__iter__()
            sage: type(iter)
            <class 'sage.libs.gap.element.GapElement_RecordIterator'>
            sage: sorted(rec)
            [('a', 123), ('b', 456)]
        """
        ...
    def record_name_to_index(self, name: str) -> int:
        r"""
        Convert string to GAP record index.

        INPUT:

        - ``py_name`` -- a python string

        OUTPUT:

        A ``UInt``, which is a GAP hash of the string. If this is the
        first time the string is encountered, a new integer is
        returned(!)

        EXAMPLES::

            sage: rec = libgap.eval('rec(first:=123, second:=456)')
            sage: rec.record_name_to_index('first')   # random output
            1812
            sage: rec.record_name_to_index('no_such_name') # random output
            3776
        """
        ...
    def __getitem__(self, name: str) -> GapElement:
        r"""
        Return the ``name``-th element of the GAP record.

        INPUT:

        - ``name`` -- string

        OUTPUT: the record element labelled by ``name`` as a :class:`GapElement`

        EXAMPLES::

            sage: rec = libgap.eval('rec(first:=123, second:=456)')
            sage: rec['first']
            123
        """
        ...
    def sage(self) -> dict[str, _Sage]:
        r"""
        Return the Sage equivalent of the :class:`GapElement`.

        EXAMPLES::

            sage: libgap.eval('rec(a:=1, b:=2)').sage()
            {'a': 1, 'b': 2}
            sage: all( isinstance(key,str) and val in ZZ for key,val in _.items() )
            True

            sage: rec = libgap.eval('rec(a:=123, b:=456, Sym3:=SymmetricGroup(3))')
            sage: rec.sage()
            {'Sym3': NotImplementedError('cannot construct equivalent Sage object'...),
             'a': 123,
             'b': 456}
        """
        ...

class GapElement_RecordIterator():
    r"""
    Iterator for :class:`GapElement_Record`.

    Since Cython does not support generators yet, we implement the
    older iterator specification with this auxiliary class.

    INPUT:

    - ``rec`` -- the :class:`GapElement_Record` to iterate over

    EXAMPLES::

        sage: rec = libgap.eval('rec(a:=123, b:=456)')
        sage: sorted(rec)
        [('a', 123), ('b', 456)]
        sage: dict(rec)
        {'a': 123, 'b': 456}
    """

    def __next__(self) -> tuple[str, GapElement]:
        r"""
        Return the next element in the record.

        OUTPUT:

        A tuple ``(key, value)`` where ``key`` is a string and
        ``value`` is the corresponding :class:`GapElement`.

        EXAMPLES::

            sage: rec = libgap.eval('rec(a:=123, b:=456)')
            sage: iter = rec.__iter__()
            sage: a = iter.__next__()
            sage: b = next(iter)
            sage: sorted([a, b])
            [('a', 123), ('b', 456)]
        """
        ...






