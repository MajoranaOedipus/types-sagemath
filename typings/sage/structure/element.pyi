r"""
Elements

AUTHORS:

- David Harvey (2006-10-16): changed CommutativeAlgebraElement to
  derive from CommutativeRingElement instead of AlgebraElement

- David Harvey (2006-10-29): implementation and documentation of new
  arithmetic architecture

- William Stein (2006-11): arithmetic architecture -- pushing it
  through to completion.

- Gonzalo Tornaria (2007-06): recursive base extend for coercion --
  lots of tests

- Robert Bradshaw (2007-2010): arithmetic operators and coercion

- Maarten Derickx (2010-07): added architecture for is_square and sqrt

- Jeroen Demeyer (2016-08): moved all coercion to the base class
  :class:`Element`, see :issue:`20767`

The Abstract Element Class Hierarchy
====================================

This is the abstract class hierarchy, i.e., these are all
abstract base classes.

::

    SageObject
        Element
            ModuleElement
                RingElement
                    CommutativeRingElement
                        IntegralDomainElement
                            DedekindDomainElement
                                PrincipalIdealDomainElement
                                    EuclideanDomainElement
                        FieldElement
                        CommutativeAlgebraElement
                        Expression
                    AlgebraElement
                        Matrix
                    InfinityElement
                AdditiveGroupElement
                Vector

            MonoidElement
                MultiplicativeGroupElement
        ElementWithCachedMethod


How to Define a New Element Class
=================================

Elements typically define a method ``_new_c``, e.g.,

.. code-block:: cython

    cdef _new_c(self, defining data):
        cdef FreeModuleElement_generic_dense x
        x = FreeModuleElement_generic_dense.__new__(FreeModuleElement_generic_dense)
        x._parent = self._parent
        x._entries = v

that creates a new sibling very quickly from defining data
with assumed properties.

.. _element_arithmetic:

Arithmetic for Elements
-----------------------

Sage has a special system for handling arithmetic operations on Sage
elements (that is instances of :class:`Element`), in particular to
manage uniformly mixed arithmetic operations using the :mod:`coercion
model <sage.structure.coerce>`. We describe here the rules that must
be followed by both arithmetic implementers and callers.

A quick summary for the impatient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To implement addition for any :class:`Element` subclass, override the
``def _add_(self, other)`` method instead of the usual Python
``__add__`` :python:`special method <reference/datamodel.html#special-method-names>`.
Within ``_add_(self, other)``, you may assume that ``self`` and
``other`` have the same parent.

If the implementation is generic across all elements in a given
category `C`, then this method can be put in ``C.ElementMethods``.

When writing *Cython* code, ``_add_`` should be a cpdef method:
``cpdef _add_(self, other)``.

When doing arithmetic with two elements having different parents,
the :mod:`coercion model <sage.structure.coerce>` is responsible for
"coercing" them to a common parent and performing arithmetic on the
coerced elements.

Arithmetic in more detail
^^^^^^^^^^^^^^^^^^^^^^^^^

The aims of this system are to provide (1) an efficient calling protocol
from both Python and Cython, (2) uniform coercion semantics across Sage,
(3) ease of use, (4) readability of code.

We will take addition as an example; all other operators are similar.
There are two relevant functions, with differing names
(single vs. double underscores).

-  **def Element.__add__(left, right)**

   This function is called by Python or Cython when the binary "+"
   operator is encountered. It assumes that at least one of its
   arguments is an :class:`Element`.

   It has a fast pathway to deal with the most common case where both
   arguments have the same parent. Otherwise, it uses the coercion
   model to work out how to make them have the same parent. The
   coercion model then adds the coerced elements (technically, it calls
   ``operator.add``). Note that the result of coercion is not required
   to be a Sage :class:`Element`, it could be a plain Python type.

   Note that, although this function is declared as ``def``, it doesn't
   have the usual overheads associated with Python functions (either
   for the caller or for ``__add__`` itself). This is because Python
   has optimised calling protocols for such special functions.

-  **def Element._add_(self, other)**

   This is the function that you should override to implement addition
   in a subclass of :class:`Element`.

   The two arguments to this function are guaranteed to have the **same
   parent**, but not necessarily the same Python type.

   When implementing ``_add_`` in a Cython extension type, use
   ``cpdef _add_`` instead of ``def _add_``.

   In Cython code, if you want to add two elements and you know that
   their parents are identical, you are encouraged to call this
   function directly, instead of using ``x + y``. This only works if
   Cython knows that the left argument is an ``Element``. You can
   always cast explicitly: ``(<Element>x)._add_(y)`` to force this.
   In plain Python, ``x + y`` is always the fastest way to add two
   elements because the special method ``__add__`` is optimized
   unlike the normal method ``_add_``.

The difference in the names of the arguments (``left, right``
versus ``self, other``) is intentional: ``self`` is guaranteed to be an
instance of the class in which the method is defined. In Cython, we know
that at least one of ``left`` or ``right`` is an instance of the class
but we do not know a priori which one.

Powering is a special case: first of all, the 3-argument version of
``pow()`` is not supported. Second, the coercion model checks whether
the exponent looks like an integer. If so, the function ``_pow_int``
is called. If the exponent is not an integer, the arguments are coerced
to a common parent and ``_pow_`` is called. So, if your type only
supports powering to an integer exponent, you should implement only
``_pow_int``. If you want to support arbitrary powering, implement both
``_pow_`` and ``_pow_int``.

For addition, multiplication and powering (not for other operators),
there is a fast path for operations with a C ``long``. For example,
implement ``cdef _add_long(self, long n)`` with optimized code for
``self + n``. The addition and multiplication are assumed to be
commutative, so they are also called for ``n + self`` or ``n * self``.
From Cython code, you can also call ``_add_long`` or ``_mul_long``
directly. This is strictly an optimization: there is a default
implementation falling back to the generic arithmetic function.

Examples
^^^^^^^^

We need some :class:`Parent` to work with::

    sage: from sage.structure.parent import Parent
    sage: class ExampleParent(Parent):
    ....:     def __init__(self, name, **kwds):
    ....:         Parent.__init__(self, **kwds)
    ....:         self.rename(name)

We start with a very basic example of a Python class implementing
``_add_``::

    sage: from sage.structure.element import Element
    sage: class MyElement(Element):
    ....:     def _add_(self, other):
    ....:         return 42
    sage: p = ExampleParent("Some parent")
    sage: x = MyElement(p)
    sage: x + x
    42

When two different parents are involved, this no longer works since
there is no coercion::

    sage: q = ExampleParent("Other parent")
    sage: y = MyElement(q)
    sage: x + y
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for +: 'Some parent' and 'Other parent'

If ``_add_`` is not defined, an error message is raised, referring to
the parents::

    sage: x = Element(p)
    sage: x._add_(x)
    Traceback (most recent call last):
    ...
    AttributeError: 'sage.structure.element.Element' object has no attribute '_add_'...
    sage: x + x
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for +: 'Some parent' and 'Some parent'
    sage: y = Element(q)
    sage: x + y
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for +: 'Some parent' and 'Other parent'

We can also implement arithmetic generically in categories::

    sage: class MyCategory(Category):
    ....:     def super_categories(self):
    ....:         return [Sets()]
    ....:     class ElementMethods:
    ....:         def _add_(self, other):
    ....:             return 42
    sage: p = ExampleParent("Parent in my category", category=MyCategory())
    sage: x = Element(p)
    sage: x + x
    42

Implementation details
^^^^^^^^^^^^^^^^^^^^^^

Implementing the above features actually takes a bit of magic. Casual
callers and implementers can safely ignore it, but here are the
details for the curious.

To achieve fast arithmetic, it is critical to have a fast path in Cython
to call the ``_add_`` method of a Cython object. So we would like
to declare ``_add_`` as a ``cpdef`` method of class :class:`Element`.
Remember however that the abstract classes coming
from categories come after :class:`Element` in the method resolution
order (or fake method resolution order in case of a Cython
class). Hence any generic implementation of ``_add_`` in such an
abstract class would in principle be shadowed by ``Element._add_``.
This is worked around by defining ``Element._add_`` as a ``cdef``
instead of a ``cpdef`` method. Concrete implementations in subclasses
should be ``cpdef`` or ``def`` methods.

Let us now see what happens upon evaluating ``x + y`` when ``x`` and ``y``
are instances of a class that does not implement ``_add_`` but where
``_add_`` is implemented in the category.
First, ``x.__add__(y)`` is called, where ``__add__`` is implemented
in :class:`Element`.
Assuming that ``x`` and ``y`` have the same parent, a Cython call to
``x._add_(y)`` will be done.
The latter is implemented to trigger a Python level call to ``x._add_(y)``
which will succeed as desired.

In case that Python code calls ``x._add_(y)`` directly,
``Element._add_`` will be invisible, and the method lookup will
continue down the MRO and find the ``_add_`` method in the category.
"""

from collections.abc import Callable
from typing import (
    Any, TypeGuard, overload, Self, SupportsFloat, 
    Literal, SupportsIndex, Protocol
)
from typings_sagemath import Int, ComparableWithZero, SupportsSage
from sage.structure.sage_object import SageObject
from sage.misc.inherit_comparison import InheritComparisonMetaclass
from sage.categories.category_types import Elements
from sage.rings.real_mpfr import RealNumber
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.integer import Integer
from numpy import number as NumPyNumber

import _cython_3_2_1
import sage.structure.coerce
from sage.structure.parent import Parent
from sage.arith.numerical_approx import digits_to_bits as digits_to_bits
from sage.misc.decorators import sage_wraps as sage_wraps
from sage.misc.lazy_format import LazyFormat as LazyFormat
from sage.misc.superseded import deprecation as deprecation
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal

# __getattr__ will look into its parent's _abstract_element_class
# so concrete elements should include that as base?
class Element[P: Parent](SageObject):  # should P be invariant or covariant?
    """
    Generic element of a structure. All other types of elements
    (:class:`RingElement`, :class:`ModuleElement`, etc)
    derive from this type.

    Subtypes must either call ``__init__()`` to set ``_parent``, or may
    set ``_parent`` themselves if that would be more efficient.

    .. automethod:: _richcmp_
    .. automethod:: __add__
    .. automethod:: __sub__
    .. automethod:: __neg__
    .. automethod:: __mul__
    .. automethod:: __truediv__
    .. automethod:: __floordiv__
    .. automethod:: __mod__"""
    
    def __init__(self, parent: P):
        """
                INPUT:

                - ``parent`` -- a SageObject
        """
    def base_extend(self, R) -> Element: ...
    def base_ring(self) -> Any:
        """Element.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 648)

        Return the base ring of this element's parent (if that makes sense).

        TESTS::

            sage: QQ.base_ring()
            Rational Field
            sage: identity_matrix(3).base_ring()                                        # needs sage.modules
            Integer Ring"""
    def category(self) -> Elements[P]:
        """Element.category(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 661)"""
    def is_zero(self) -> bool:
        """
        Return ``True`` if ``self`` equals ``self.parent()(0)``.

        The default implementation is to fall back to ``not
        self.__bool__``.

        .. WARNING::

            Do not re-implement this method in your subclass but
            implement ``__bool__`` instead."""
    def n(self, prec: Int | None = None, digits: SupportsFloat | None = None, algorithm=None) -> RealNumber | ComplexNumber:
        """
        Alias for :meth:`numerical_approx`.

        EXAMPLES::

            sage: (2/3).n()                                                             # needs sage.rings.real_mpfr
            0.666666666666667"""
    def numerical_approx(self, prec: Int | None = None, digits: SupportsFloat | None = None, algorithm=None) -> RealNumber | ComplexNumber:
        """
        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision.

        No guarantee is made about the accuracy of the result.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute this
          approximation (the accepted algorithms depend on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: (2/3).numerical_approx()                                              # needs sage.rings.real_mpfr
            0.666666666666667
            sage: pi.n(digits=10)                                                       # needs sage.symbolic
            3.141592654
            sage: pi.n(prec=20)                                                         # needs sage.symbolic
            3.1416

        TESTS:

        Check that :issue:`14778` is fixed::

            sage: (0).n(algorithm='foo')                                                # needs sage.rings.real_mpfr
            0.000000000000000"""
    def parent(self, x: Any = None) -> P:
        """
        Return the parent of this element; or, if the optional argument x is
        supplied, the result of coercing x into the parent of this element."""
    def subs(self, in_dict: dict | None = None, **kwds) -> Any:
        """
        Substitutes given generators with given values while not touching
        other generators.

        This is a generic wrapper around ``__call__``.  The syntax is
        meant to be compatible with the corresponding method for
        symbolic expressions.

        INPUT:

        - ``in_dict`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new object if substitution is possible, otherwise ``self``

        EXAMPLES::

            sage: x, y = PolynomialRing(ZZ,2,'xy').gens()
            sage: f = x^2 + y + x^2*y^2 + 5
            sage: f((5,y))
            25*y^2 + y + 30
            sage: f.subs({x:5})
            25*y^2 + y + 30
            sage: f.subs(x=5)
            25*y^2 + y + 30
            sage: (1/f).subs(x=5)
            1/(25*y^2 + y + 30)
            sage: Integer(5).subs(x=4)
            5"""
    def substitute(self, in_dict: dict | None = None, **kwds) -> Any:
        """
        This calls :meth:`self.subs`.

        EXAMPLES::

            sage: x, y = PolynomialRing(ZZ, 2, 'xy').gens()
            sage: f = x^2 + y + x^2*y^2 + 5
            sage: f((5,y))
            25*y^2 + y + 30
            sage: f.substitute({x: 5})
            25*y^2 + y + 30
            sage: f.substitute(x=5)
            25*y^2 + y + 30
            sage: (1/f).substitute(x=5)
            1/(25*y^2 + y + 30)
            sage: Integer(5).substitute(x=4)
            5"""
    def __add__(self, right) -> Any:    # I don't know how to type this
        """
        Top-level addition operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _add_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e + e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: e + e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 + e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e + 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) + e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'int' and 'sage.structure.element.Element'
            sage: e + int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'sage.structure.element.Element' and 'int'
            sage: None + e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'NoneType' and 'sage.structure.element.Element'
            sage: e + None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'sage.structure.element.Element' and 'NoneType'"""
    def __bool__(self) -> bool:
        r"""
        Return whether this element is equal to ``self.parent()(0)``.

        Note that this is automatically called when converting to
        boolean, as in the conditional of an if or while statement.

        EXAMPLES::

            sage: bool(1) # indirect doctest
            True

        If ``self.parent()(0)`` raises an exception (because there is no
        meaningful zero element,) then this method returns ``True``. Here,
        there is no zero morphism of rings that goes to a non-trivial ring::

            sage: bool(Hom(ZZ, Zmod(2)).an_element())
            True

        But there is a zero morphism to the trivial ring::

            sage: bool(Hom(ZZ, Zmod(1)).an_element())
            False

        TESTS:

        Verify that :issue:`5185` is fixed::

            sage: # needs sage.modules
            sage: v = vector({1: 1, 3: -1})
            sage: w = vector({1: -1, 3: 1})
            sage: v + w
            (0, 0, 0, 0)
            sage: (v + w).is_zero()
            True
            sage: bool(v + w)
            False
        """
    def __copy__(self) -> Self:
        """Element.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 594)

        Return a copy of ``self``.

        OUTPUT: a new object which is a copy of ``self``

        This implementation ensures that ``self.__dict__`` is properly copied
        when it exists (typically for instances of classes deriving from
        :class:`Element`).

        TESTS::

            sage: from sage.structure.element import Element
            sage: el = Element(parent = ZZ)
            sage: el1 = copy(el)
            sage: el1 is el
            False

            sage: class Demo(Element): pass
            sage: el = Demo(parent = ZZ)
            sage: el.x = [1,2,3]
            sage: el1 = copy(el)
            sage: el1 is el
            False
            sage: el1.__dict__ is el.__dict__
            False"""
    def __dir__(self) -> list[str]:
        """
        Emulate ``__dir__`` for elements with dynamically attached methods.

        Let cat be the category of the parent of ``self``. This method
        emulates ``self`` being an instance of both ``Element`` and
        ``cat.element_class`` (and the corresponding ``morphism_class`` in the
        case of a morphism), in that order, for attribute directory.

        EXAMPLES::

            sage: dir(1/2)
            [..., 'is_idempotent', 'is_integer', 'is_integral', ...]

        Caveat: dir on Integer's and some other extension types seem to ignore __dir__::

            sage: 1.__dir__()
            [..., 'is_idempotent', 'is_integer', 'is_integral', ...]
            sage: dir(1)         # todo: not implemented
            [..., 'is_idempotent', 'is_integer', 'is_integral', ...]

        TESTS:

        Check that morphism classes are handled correctly (:issue:`29776`)::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x, y+1], R)
            sage: 'cartesian_product' in dir(f)
            True
            sage: 'extend_to_fraction_field' in dir(f)
            True"""
    def __eq__(self, other): ...
    def __floordiv__(self, right) -> Any:
        """
        Top-level floor division operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: 7 // 3
            2
            sage: 7 // int(3)
            2
            sage: int(7) // 3
            2

        ::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _floordiv_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e // e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: e // e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for //: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 // e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for //: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e // 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for //: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) // e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for //: 'int' and 'sage.structure.element.Element'
            sage: e // int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for //: 'sage.structure.element.Element' and 'int'
            sage: None // e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for //: 'NoneType' and 'sage.structure.element.Element'
            sage: e // None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for //: 'sage.structure.element.Element' and 'NoneType'"""
    def __ge__(self, other): ...
    def __getmetaclass__(self) -> type[InheritComparisonMetaclass]:
        ...
    def __getstate__(self) -> tuple[P, dict[str, Any]]:
        """
        Return a tuple describing the state of your object.

        This should return all information that will be required to unpickle
        the object. The functionality for unpickling is implemented in
        __setstate__().

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: i = ideal(x^2 - y^2 + 1)
            sage: i.__getstate__()
            (Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field,
             {'_Ideal_generic__gens': (x^2 - y^2 + 1,),
              '_Ideal_generic__ring': Multivariate Polynomial Ring in x, y over Rational Field,
              '_gb_by_ordering': {}})
        """
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __matmul__(self, right) -> Any:
        """
        Top-level matrix multiplication operator for :class:`Element`
        invoking the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _matmul_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: from operator import matmul
            sage: matmul(e, e)
            42

        TESTS::

            sage: e = Element(Parent())
            sage: matmul(e, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for @: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: matmul(1, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for @: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: matmul(e, 1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for @: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: matmul(int(1), e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for @: 'int' and 'sage.structure.element.Element'
            sage: matmul(e, int(1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for @: 'sage.structure.element.Element' and 'int'
            sage: matmul(None, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for @: 'NoneType' and 'sage.structure.element.Element'
            sage: matmul(e, None)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for @: 'sage.structure.element.Element' and 'NoneType'"""
    def __mod__(self, right) -> Any:
        """
        Top-level modulo operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: 7 % 3
            1
            sage: 7 % int(3)
            1
            sage: int(7) % 3
            1

        ::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _mod_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e % e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: e % e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for %: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 % e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for %: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e % 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for %: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) % e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for %: 'int' and 'sage.structure.element.Element'
            sage: e % int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for %: 'sage.structure.element.Element' and 'int'
            sage: None % e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for %: 'NoneType' and 'sage.structure.element.Element'
            sage: e % None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for %: 'sage.structure.element.Element' and 'NoneType'"""
    def __mul__(self, right) -> Any:
        """
        Top-level multiplication operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _mul_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e * e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: e * e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 * e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e * 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) * e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for *: 'int' and 'sage.structure.element.Element'
            sage: e * int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for *: 'sage.structure.element.Element' and 'int'
            sage: None * e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for *: 'NoneType' and 'sage.structure.element.Element'
            sage: e * None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for *: 'sage.structure.element.Element' and 'NoneType'

        ::

            sage: # needs sage.combinat sage.modules
            sage: A = AlgebrasWithBasis(QQ).example(); A
            An example of an algebra with basis: the free algebra
            on the generators ('a', 'b', 'c') over Rational Field
            sage: x = A.an_element()
            sage: x
            B[word: ] + 2*B[word: a] + 3*B[word: b] + B[word: bab]
            sage: x.__mul__(x)
            B[word: ] + 4*B[word: a] + 4*B[word: aa] + 6*B[word: ab]
            + 2*B[word: abab] + 6*B[word: b] + 6*B[word: ba]
            + 2*B[word: bab] + 2*B[word: baba] + 3*B[word: babb]
            + B[word: babbab] + 9*B[word: bb] + 3*B[word: bbab]"""
    def __ne__(self, other): ...
    def __neg__(self) -> Self | Any:
        """
        Top-level negation operator for :class:`Element`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _neg_(self):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: -e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: -e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent for unary -: '<sage.structure.parent.Parent object at ...>'"""
    def __pos__(self) -> Self:
        ...
    def __pow__(self, right, modulus = None) -> Any:
        """
        Top-level power operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _add_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e + e
            42
            sage: a = Integers(389)['x']['y'](37)
            sage: p = sage.structure.element.RingElement.__pow__
            sage: p(a, 2)
            202
            sage: p(a, 2, 1)
            Traceback (most recent call last):
            ...
            TypeError: the 3-argument version of pow() is not supported

        ::

            sage: # needs sage.symbolic
            sage: (2/3)^I
            (2/3)^I
            sage: (2/3)^sqrt(2)
            (2/3)^sqrt(2)
            sage: var('x,y,z,n')
            (x, y, z, n)
            sage: (2/3)^(x^n + y^n + z^n)
            (2/3)^(x^n + y^n + z^n)
            sage: (-7/11)^(tan(x)+exp(x))
            (-7/11)^(e^x + tan(x))

            sage: float(1.2)**(1/2)
            1.0954451150103321
            sage: complex(1,2)**(1/2)                                                   # needs sage.rings.complex_double
            (1.272019649514069+0.786151377757423...j)

        TESTS::

            sage: e = Element(Parent())
            sage: e ^ e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for ^: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 ^ e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for ^: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e ^ 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for ^: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) ^ e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'sage.structure.element.Element'
            sage: e ^ int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'sage.structure.element.Element' and 'int'
            sage: None ^ e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'sage.structure.element.Element'
            sage: e ^ None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'sage.structure.element.Element' and 'NoneType'"""
    def __radd__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __rmatmul__(self, other): ...
    def __rmod__(self, other): ...
    def __rmul__(self, other): ...
    def __rpow__(self, other): ...
    def __rsub__(self, other): ...
    def __rtruediv__(self, other): ...
    def __setstate__(self, state: tuple[P, dict[str, Any]]) -> None:
        """
        Initialize the state of the object from data saved in a pickle.

        During unpickling ``__init__`` methods of classes are not called, the
        saved data is passed to the class via this function instead.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: i = ideal(x); i
            Ideal (x) of Multivariate Polynomial Ring in x, y over Rational Field
            sage: S.<x,y,z> = ZZ[]
            sage: i.__setstate__((R,{'_Ideal_generic__ring':S,'_Ideal_generic__gens': (S(x^2 - y^2 + 1),)}))
            sage: i
            Ideal (x^2 - y^2 + 1) of Multivariate Polynomial Ring in x, y, z over Integer Ring
        """
    def __sub__(self, right) -> Any:
        """
        Top-level subtraction operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _sub_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: e - e
            42

        TESTS::

            sage: e = Element(Parent())
            sage: e - e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for -: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: 1 - e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for -: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: e - 1
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for -: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: int(1) - e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for -: 'int' and 'sage.structure.element.Element'
            sage: e - int(1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for -: 'sage.structure.element.Element' and 'int'
            sage: None - e
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for -: 'NoneType' and 'sage.structure.element.Element'
            sage: e - None
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for -: 'sage.structure.element.Element' and 'NoneType'"""
    def __truediv__(self, right) -> Any:
        """
        Top-level true division operator for :class:`Element` invoking
        the coercion model.

        See :ref:`element_arithmetic`.

        EXAMPLES::

            sage: operator.truediv(2, 3)
            2/3
            sage: operator.truediv(pi, 3)                                               # needs sage.symbolic
            1/3*pi
            sage: x = polygen(QQ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)                                          # needs sage.rings.number_field
            sage: operator.truediv(2, K.ideal(i + 1))                                   # needs sage.rings.number_field
            Fractional ideal (-i + 1)

        ::

            sage: from sage.structure.element import Element
            sage: class MyElement(Element):
            ....:     def _div_(self, other):
            ....:         return 42
            sage: e = MyElement(Parent())
            sage: operator.truediv(e, e)
            42

        TESTS::

            sage: e = Element(Parent())
            sage: operator.truediv(e, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for /: '<sage.structure.parent.Parent object at ...>' and '<sage.structure.parent.Parent object at ...>'
            sage: operator.truediv(1, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for /: 'Integer Ring' and '<sage.structure.parent.Parent object at ...>'
            sage: operator.truediv(e, 1)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for /: '<sage.structure.parent.Parent object at ...>' and 'Integer Ring'
            sage: operator.truediv(int(1), e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for /: 'int' and 'sage.structure.element.Element'
            sage: operator.truediv(e, int(1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for /: 'sage.structure.element.Element' and 'int'
            sage: operator.truediv(None, e)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for /: 'NoneType' and 'sage.structure.element.Element'
            sage: operator.truediv(e, None)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for /: 'sage.structure.element.Element' and 'NoneType'"""

def bin_op(x: object, y: object, op: Callable[[Any, Any], Any]) -> Any: ...

type _Numeric = int | float | complex | NumPyNumber
type _Sage = SageObject | SupportsSage

@overload
def canonical_coercion[P: Parent](
    x: Element[P], y: Element[P]
) -> tuple[Element[P], Element[P]]: ...
@overload
def canonical_coercion(x: _Numeric, y: _Numeric) -> tuple[_Numeric, _Numeric]: ...
@overload
def canonical_coercion[P: Parent](
    x: _Sage, y: _Numeric) -> tuple[Element[P], Element[P]]: ...
@overload
def canonical_coercion[P: Parent](
    x: _Numeric, y: _Sage) -> tuple[Element[P], Element[P]]: ...
@overload
def canonical_coercion[P: Parent](
    x: _Sage, y: _Sage) -> tuple[Element[P], Element[P]]:
    """``canonical_coercion(x,y)`` is what is called before doing an
arithmetic operation between ``x`` and ``y``.  It returns a pair ``(z,w)``
such that ``z`` is got from ``x`` and ``w`` from ``y`` via canonical coercion and
the parents of ``z`` and ``w`` are identical.

EXAMPLES::

    sage: A = Matrix([[0, 1], [1, 0]])                                              # needs sage.modules
    sage: canonical_coercion(A, 1)                                                  # needs sage.modules
    (
    [0 1]  [1 0]
    [1 0], [0 1]
    )
"""

class _BinopMethod(Protocol):
    def __call__(self, other, *args, **kwargs): ...

def coerce_binop(method: _BinopMethod) -> _BinopMethod:
    r"""
    Decorator for a binary operator method for applying coercion to the
    arguments before calling the method.

    Consider a parent class in the category framework, `S`, whose element class
    expose a method `binop`. If `a` and `b` are elements of `S`, then
    `a.binop(b)` behaves as expected. If `a` and `b` are not elements of `S`,
    but rather have a common parent `T` whose element class also exposes
    `binop`, we would rather expect `a.binop(b)` to compute `aa.binop(bb)`,
    where `aa = T(a)` and `bb = T(b)`. This decorator ensures that behaviour
    without having to otherwise modify the implementation of `binop` on the
    element class of `A`.

    Since coercion will be attempted on the arguments of the decorated method, a
    `TypeError` will be thrown if there is no common parent between the
    elements. An `AttributeError` or `NotImplementedError` or similar will be
    thrown if there is a common parent of the arguments, but its element class
    does not implement a method of the same name as the decorated method.

    EXAMPLES:

    Sparse polynomial rings uses ``@coerce_binop`` on ``gcd``::

        sage: S.<x> = PolynomialRing(ZZ, sparse=True)
        sage: f = x^2
        sage: g = x
        sage: f.gcd(g)  #indirect doctest
        x
        sage: T = PolynomialRing(QQ, name='x', sparse=True)
        sage: h = 1/2*T(x)
        sage: u = f.gcd(h); u  #indirect doctest
        x
        sage: u.parent() == T
        True

    Another real example::

        sage: R1 = QQ['x,y']
        sage: R2 = QQ['x,y,z']
        sage: f = R1(1)
        sage: g = R1(2)
        sage: h = R2(1)
        sage: f.gcd(g)
        1
        sage: f.gcd(g, algorithm='modular')
        1
        sage: f.gcd(h)
        1
        sage: f.gcd(h, algorithm='modular')
        1
        sage: h.gcd(f)
        1
        sage: h.gcd(f, 'modular')
        1

    We demonstrate a small class using ``@coerce_binop`` on a method::

        sage: from sage.structure.element import coerce_binop
        sage: class MyRational(Rational):
        ....:     def __init__(self, value):
        ....:         self.v = value
        ....:     @coerce_binop
        ....:     def test_add(self, other, keyword='z'):
        ....:         return (self.v, other, keyword)

    Calls func directly if the two arguments have the same parent::

        sage: x = MyRational(1)
        sage: x.test_add(1/2)
        (1, 1/2, 'z')
        sage: x.test_add(1/2, keyword=3)
        (1, 1/2, 3)

    Passes through coercion and does a method lookup if the left operand is not
    the same. If the common parent's element class does not have a method of the
    same name, an exception is raised::

        sage: x.test_add(2)
        (1, 2, 'z')
        sage: x.test_add(2, keyword=3)
        (1, 2, 3)
        sage: x.test_add(CC(2))
        Traceback (most recent call last):
        ...
        AttributeError: 'sage.rings.complex_mpfr.ComplexNumber' object has no attribute 'test_add'...

    TESTS:

    Test that additional arguments given to the method do not override
    the ``self`` argument, see :issue:`21322`::

        sage: f.gcd(g, 1)
        Traceback (most recent call last):
        ...
        TypeError: algorithm 1 not supported
    """
    ...
coercion_model: sage.structure.coerce.CoercionModel

@overload
def coercion_traceback(dump: Literal[False]) -> list[str]: ...
@overload
def coercion_traceback(dump: Literal[True] = True) -> None:
    r"""
    This function is very helpful in debugging coercion errors. It prints
    the tracebacks of all the errors caught in the coercion detection. Note
    that failure is cached, so some errors may be omitted the second time
    around (as it remembers not to retry failed paths for speed reasons.

    For performance and caching reasons, exception recording must be
    explicitly enabled before using this function.

    EXAMPLES::

        sage: cm = sage.structure.element.get_coercion_model()
        sage: cm.record_exceptions()
        sage: 1 + 1/5
        6/5
        sage: coercion_traceback()  # Should be empty, as all went well.
        sage: 1/5 + GF(5).gen()
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand parent(s) for +:
        'Rational Field' and 'Finite Field of size 5'
        sage: coercion_traceback()
        Traceback (most recent call last):
        ...
        TypeError: no common canonical parent for objects with parents:
        'Rational Field' and 'Finite Field of size 5'
    """
def get_coercion_model() -> sage.structure.coerce.CoercionModel: 
    """
    Return the global coercion model.

    EXAMPLES::

       sage: import sage.structure.element as e
       sage: cm = e.get_coercion_model()
       sage: cm
       <sage.structure.coerce.CoercionModel object at ...>
       sage: cm is coercion_model
       True
    """
    ...
have_same_parent: _cython_3_2_1.cython_function_or_method
def is_AdditiveGroupElement(x: object) -> TypeGuard[AdditiveGroupElement]:
    """
    Return ``True`` if x is of type AdditiveGroupElement.
    """
def is_AlgebraElement(x: object) -> TypeGuard[AlgebraElement]:
    """
    Return ``True`` if x is of type AlgebraElement.
    """
def is_CommutativeAlgebraElement(x: object) -> TypeGuard[CommutativeAlgebraElement]:
    """
    Return ``True`` if x is of type CommutativeAlgebraElement.
    """
def is_CommutativeRingElement(x: object) -> TypeGuard[CommutativeRingElement]:
    """
    Return ``True`` if x is of type CommutativeRingElement.

    TESTS::

        sage: from sage.structure.element import is_CommutativeRingElement
        sage: is_CommutativeRingElement(oo)
        doctest:warning...
        DeprecationWarning: The function is_CommutativeRingElement is deprecated; use 'isinstance(..., CommutativeRingElement)' instead.
        See https://github.com/sagemath/sage/issues/38077 for details.
        False

        sage: is_CommutativeRingElement(1)
        True
    """
def is_DedekindDomainElement(x: object) -> TypeGuard[DedekindDomainElement]:
    """
    Return ``True`` if x is of type DedekindDomainElement.
    """
def is_Element(x: object) -> TypeGuard[Element]:
    """
    Return ``True`` if x is of type Element.
    """
def is_EuclideanDomainElement(x: object) -> TypeGuard[EuclideanDomainElement]:
    """
    Return ``True`` if x is of type EuclideanDomainElement.
    """
def is_FieldElement(x: object) -> TypeGuard[FieldElement]:
    """
    Return ``True`` if x is of type FieldElement.
    """
def is_InfinityElement(x: object) -> TypeGuard[InfinityElement]:
    """
    Return ``True`` if x is of type InfinityElement.
    """
def is_IntegralDomainElement(x: object) -> TypeGuard[IntegralDomainElement]:
    """
    Return ``True`` if x is of type IntegralDomainElement.
    """
def is_Matrix(x: object) -> TypeGuard[Matrix]:
    ...
def is_ModuleElement(x: object) -> TypeGuard[ModuleElement]:
    """
    Return ``True`` if x is of type ModuleElement.

    This is even faster than using isinstance inline.

    EXAMPLES::

        sage: from sage.structure.element import is_ModuleElement
        sage: is_ModuleElement(2/3)
        doctest:warning...
        DeprecationWarning: The function is_ModuleElement is deprecated; use 'isinstance(..., ModuleElement)' instead.
        See https://github.com/sagemath/sage/issues/38077 for details.
        True
        sage: is_ModuleElement((QQ^3).0)                                                # needs sage.modules
        True
        sage: is_ModuleElement('a')
        False
    """
def is_MonoidElement(x: object) -> TypeGuard[MonoidElement]:
    """
    Return ``True`` if x is of type MonoidElement.
    """
def is_MultiplicativeGroupElement(x: object) -> TypeGuard[MultiplicativeGroupElement]:
    """
    Return ``True`` if x is of type MultiplicativeGroupElement.
    """
def is_PrincipalIdealDomainElement(x: object) -> TypeGuard[PrincipalIdealDomainElement]:
    """
    Return ``True`` if x is of type PrincipalIdealDomainElement.
    """
def is_RingElement(x: object) -> TypeGuard[RingElement]:
    """
    Return ``True`` if x is of type RingElement.
    """
def is_Vector(x: object) -> TypeGuard[Vector]: ...
def make_element(_class, _dict, parent):
    """
    This function is only here to support old pickles.

    Pickling functionality is moved to Element.{__getstate__,__setstate__}
    functions.
    """

@overload
def parent[P: Parent](x: Element[P]) -> P:  # pyright: ignore[reportOverlappingOverload]
    ...
@overload
def parent[T](x: T) -> type[T]:
    """
    Return the parent of the element ``x``.

    Usually, this means the mathematical object of which ``x`` is an
    element.

    INPUT:

    - ``x`` -- an element

    OUTPUT:

    - If ``x`` is a Sage :class:`Element`, return ``x.parent()``.

    - Otherwise, return ``type(x)``.

    .. SEEALSO::

        `Parents, Conversion and Coercion <http://doc.sagemath.org/html/en/tutorial/tour_coercion.html>`_
        Section in the Sage Tutorial

    EXAMPLES::

        sage: a = 42
        sage: parent(a)
        Integer Ring
        sage: b = 42/1
        sage: parent(b)
        Rational Field
        sage: c = 42.0
        sage: parent(c)                                                                 # needs sage.rings.real_mpfr
        Real Field with 53 bits of precision

    Some more complicated examples::

        sage: x = Partition([3,2,1,1,1])                                                # needs sage.combinat
        sage: parent(x)                                                                 # needs sage.combinat
        Partitions
        sage: v = vector(RDF, [1,2,3])                                                  # needs sage.modules
        sage: parent(v)                                                                 # needs sage.modules
        Vector space of dimension 3 over Real Double Field

    The following are not considered to be elements, so the type is
    returned::

        sage: d = int(42)  # Python int
        sage: parent(d)
        <... 'int'>
        sage: L = list(range(10))
        sage: parent(L)
        <... 'list'>
    """

class AdditiveGroupElement[P: Parent](ModuleElement[P]):
    """
        Generic element of an additive group.
    """
    def order(self) -> Any:
        """
        Return additive order of element"""

class AlgebraElement[P: Parent](RingElement[P]): ...

class CommutativeAlgebraElement[P: Parent](CommutativeRingElement[P]): ...

class CommutativeRingElement[P: Parent](RingElement[P]):
    """
        Base class for elements of commutative rings.
    """
    def divides(self, other) -> bool:
        """
        Return ``True`` if ``self`` divides x.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(QQ)
            sage: x.divides(x^2)
            True
            sage: x.divides(x^2 + 2)
            False
            sage: (x^2 + 2).divides(x)
            False
            sage: P.<x> = PolynomialRing(ZZ)
            sage: x.divides(x^2)
            True
            sage: x.divides(x^2 + 2)
            False
            sage: (x^2 + 2).divides(x)
            False

        :issue:`5347` has been fixed::

            sage: K = GF(7)
            sage: K(3).divides(1)
            True
            sage: K(3).divides(K(1))
            True

        ::

            sage: R = Integers(128)
            sage: R(0).divides(1)
            False
            sage: R(0).divides(0)
            True
            sage: R(0).divides(R(0))
            True
            sage: R(1).divides(0)
            True
            sage: R(121).divides(R(120))
            True
            sage: R(120).divides(R(121))
            False

        If ``x`` has different parent than ``self``, they are first coerced to a
        common parent if possible. If this coercion fails, it returns a
        :exc:`TypeError`. This fixes :issue:`5759`. ::

            sage: Zmod(2)(0).divides(Zmod(2)(0))
            True
            sage: Zmod(2)(0).divides(Zmod(2)(1))
            False
            sage: Zmod(5)(1).divides(Zmod(2)(1))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ring of integers modulo 5' and 'Ring of integers modulo 2'
            sage: Zmod(35)(4).divides(Zmod(7)(1))
            True
            sage: Zmod(35)(7).divides(Zmod(7)(1))
            False"""
    def inverse_mod(self, I) -> Any:
        """
        Return an inverse of ``self`` modulo the ideal `I`, if defined,
        i.e., if `I` and ``self`` together generate the unit ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(25)
            sage: x = F.gen()
            sage: z = F.zero()
            sage: x.inverse_mod(F.ideal(z))
            2*z2 + 3
            sage: x.inverse_mod(F.ideal(1))
            1
            sage: z.inverse_mod(F.ideal(1))
            1
            sage: z.inverse_mod(F.ideal(z))
            Traceback (most recent call last):
            ...
            ValueError: an element of a proper ideal does not have an inverse modulo that ideal"""
    def mod(self, I) -> Any:
        """CommutativeRingElement.mod(self, I)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3146)

        Return a representative for ``self`` modulo the ideal I (or the ideal
        generated by the elements of I if I is not an ideal.)

        EXAMPLES:  Integers
        Reduction of 5 modulo an ideal::

            sage: n = 5
            sage: n.mod(3*ZZ)
            2

        Reduction of 5 modulo the ideal generated by 3::

            sage: n.mod(3)
            2

        Reduction of 5 modulo the ideal generated by 15 and 6, which is `(3)`.

        ::

            sage: n.mod([15,6])
            2

        EXAMPLES: Univariate polynomials

        ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^3 + x + 1
            sage: f.mod(x + 1)
            -1

        Reduction for `\\ZZ[x]`::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = x^3 + x + 1
            sage: f.mod(x + 1)
            -1

        When little is implemented about a given ring, then ``mod`` may
        simply return `f`.

        EXAMPLES: Multivariate polynomials
        We reduce a polynomial in two variables modulo a polynomial
        and an ideal::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: (x^2 + y^2 + z^2).mod(x + y + z)                                      # needs sage.libs.singular
            2*y^2 + 2*y*z + 2*z^2

        Notice above that `x` is eliminated.  In the next example,
        both `y` and `z` are eliminated::

            sage: (x^2 + y^2 + z^2).mod( (x - y, y - z) )                               # needs sage.libs.singular
            3*z^2
            sage: f = (x^2 + y^2 + z^2)^2; f
            x^4 + 2*x^2*y^2 + y^4 + 2*x^2*z^2 + 2*y^2*z^2 + z^4
            sage: f.mod( (x - y, y - z) )                                               # needs sage.libs.singular
            9*z^4

        In this example `y` is eliminated::

            sage: (x^2 + y^2 + z^2).mod( (x^3, y - z) )                                 # needs sage.libs.singular
            x^2 + 2*z^2"""
    
class DedekindDomainElement[P: Parent](IntegralDomainElement[P]): ...

class ElementWithCachedMethod[P: Parent](Element[P]):
    '''
        An element class that fully supports cached methods.

        NOTE:

        The :class:`~sage.misc.cachefunc.cached_method` decorator provides
        a convenient way to automatically cache the result of a computation.
        Since :issue:`11115`, the cached method decorator applied to a
        method without optional arguments is faster than a hand-written cache
        in Python, and a cached method without any arguments (except ``self``)
        is actually faster than a Python method that does nothing more but
        to return ``1``. A cached method can also be inherited from the parent
        or element class of a category.

        However, this holds true only if attribute assignment is supported.
        If you write an extension class in Cython that does not accept attribute
        assignment then a cached method inherited from the category will be
        slower (for :class:`~sage.structure.parent.Parent`) or the cache would
        even break (for :class:`Element`).

        This class should be used if you write an element class, cannot provide
        it with attribute assignment, but want that it inherits a cached method
        from the category. Under these conditions, your class should inherit
        from this class rather than :class:`Element`. Then, the cache will work,
        but certainly slower than with attribute assignment. Lazy attributes
        work as well.

        EXAMPLES:

        We define three element extension classes. The first inherits from
        :class:`Element`, the second from this class, and the third simply
        is a Python class. We also define a parent class and, in Python, a
        category whose element and parent classes define cached methods.
        ::

            sage: # needs sage.misc.cython
            sage: cython_code = ["from sage.structure.element cimport Element, ElementWithCachedMethod",
            ....:     "from sage.structure.richcmp cimport richcmp",
            ....:     "cdef class MyBrokenElement(Element):",
            ....:     "    cdef public object x",
            ....:     "    def __init__(self, P, x):",
            ....:     "        self.x = x",
            ....:     "        Element.__init__(self, P)",
            ....:     "    def __neg__(self):",
            ....:     "        return MyBrokenElement(self.parent(), -self.x)",
            ....:     "    def _repr_(self):",
            ....:     "        return \'<%s>\' % self.x",
            ....:     "    def __hash__(self):",
            ....:     "        return hash(self.x)",
            ....:     "    cpdef _richcmp_(left, right, int op):",
            ....:     "        return richcmp(left.x, right.x, op)",
            ....:     "    def raw_test(self):",
            ....:     "        return -self",
            ....:     "cdef class MyElement(ElementWithCachedMethod):",
            ....:     "    cdef public object x",
            ....:     "    def __init__(self, P, x):",
            ....:     "        self.x = x",
            ....:     "        Element.__init__(self, P)",
            ....:     "    def __neg__(self):",
            ....:     "        return MyElement(self.parent(), -self.x)",
            ....:     "    def _repr_(self):",
            ....:     "        return \'<%s>\' % self.x",
            ....:     "    def __hash__(self):",
            ....:     "        return hash(self.x)",
            ....:     "    cpdef _richcmp_(left, right, int op):",
            ....:     "        return richcmp(left.x, right.x, op)",
            ....:     "    def raw_test(self):",
            ....:     "        return -self",
            ....:     "class MyPythonElement(MyBrokenElement): pass",
            ....:     "from sage.structure.parent cimport Parent",
            ....:     "cdef class MyParent(Parent):",
            ....:     "    Element = MyElement"]
            sage: cython(\'\\n\'.join(cython_code))
            sage: cython_code = ["from sage.misc.cachefunc import cached_method",
            ....:     "from sage.misc.cachefunc import cached_in_parent_method",
            ....:     "from sage.categories.category import Category",
            ....:     "from sage.categories.objects import Objects",
            ....:     "class MyCategory(Category):",
            ....:     "    @cached_method",
            ....:     "    def super_categories(self):",
            ....:     "        return [Objects()]",
            ....:     "    class ElementMethods:",
            ....:     "        @cached_method",
            ....:     "        def element_cache_test(self):",
            ....:     "            return -self",
            ....:     "        @cached_in_parent_method",
            ....:     "        def element_via_parent_test(self):",
            ....:     "            return -self",
            ....:     "    class ParentMethods:",
            ....:     "        @cached_method",
            ....:     "        def one(self):",
            ....:     "            return self.element_class(self,1)",
            ....:     "        @cached_method",
            ....:     "        def invert(self, x):",
            ....:     "            return -x"]
            sage: cython(\'\\n\'.join(cython_code))
            sage: C = MyCategory()
            sage: P = MyParent(category=C)
            sage: ebroken = MyBrokenElement(P, 5)
            sage: e = MyElement(P, 5)

        The cached methods inherited by ``MyElement`` works::

            sage: # needs sage.misc.cython
            sage: e.element_cache_test()
            <-5>
            sage: e.element_cache_test() is e.element_cache_test()
            True
            sage: e.element_via_parent_test()
            <-5>
            sage: e.element_via_parent_test() is e.element_via_parent_test()
            True

        The other element class can only inherit a
        ``cached_in_parent_method``, since the cache is stored in the
        parent. In fact, equal elements share the cache, even if they are
        of different types::

            sage: e == ebroken                                                              # needs sage.misc.cython
            True
            sage: type(e) == type(ebroken)                                                  # needs sage.misc.cython
            False
            sage: ebroken.element_via_parent_test() is e.element_via_parent_test()          # needs sage.misc.cython
            True

        However, the cache of the other inherited method breaks, although the method
        as such works::

            sage: ebroken.element_cache_test()                                              # needs sage.misc.cython
            <-5>
            sage: ebroken.element_cache_test() is ebroken.element_cache_test()              # needs sage.misc.cython
            False

        Since ``e`` and ``ebroken`` share the cache, when we empty it for one element
        it is empty for the other as well::

            sage: b = ebroken.element_via_parent_test()                                     # needs sage.misc.cython
            sage: e.element_via_parent_test.clear_cache()                                   # needs sage.misc.cython
            sage: b is ebroken.element_via_parent_test()                                    # needs sage.misc.cython
            False

        Note that the cache only breaks for elements that do no allow attribute assignment.
        A Python version of ``MyBrokenElement`` therefore allows for cached methods::

            sage: epython = MyPythonElement(P, 5)                                           # needs sage.misc.cython
            sage: epython.element_cache_test()                                              # needs sage.misc.cython
            <-5>
            sage: epython.element_cache_test() is epython.element_cache_test()              # needs sage.misc.cython
            True
    '''
    ...

class EuclideanDomainElement[P: Parent](PrincipalIdealDomainElement[P]):
    def degree(self): ...
    def leading_coefficient(self) : ...
    def quo_rem(self, other): ...

class Expression[P: Parent](CommutativeRingElement[P]):
    """
        Abstract base class for :class:`~sage.symbolic.expression.Expression`.

        This class is defined for the purpose of :func:`isinstance` tests.  It should not be
        instantiated.

        EXAMPLES::

            sage: isinstance(SR.var('y'), sage.structure.element.Expression)                # needs sage.symbolic
            True

        By design, there is a unique direct subclass::

            sage: len(sage.structure.element.Expression.__subclasses__()) <= 1
            True
    """

class FieldElement[P: Parent](CommutativeRingElement[P]):
    def canonical_associate(self) -> tuple[Any, Self]:
        """
        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]; k=R.fraction_field()
            sage: (x/y).canonical_associate()
            (1, x/y)
            sage: (0).canonical_associate()
            (0, 1)"""
    def divides(self, other: FieldElement) -> bool:
        """
        Check whether ``self`` divides ``other``, for field elements.

        Since this is a field, all values divide all other values,
        except that zero does not divide any nonzero values.

        EXAMPLES::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K.<rt3> = QQ[sqrt(3)]
            sage: K(0).divides(rt3)
            False
            sage: rt3.divides(K(17))
            True
            sage: K(0).divides(K(0))
            True
            sage: rt3.divides(K(0))
            True"""
    def is_unit(self) -> bool:
        """FieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4414)

        Return ``True`` if ``self`` is a unit in its parent ring.

        EXAMPLES::

            sage: a = 2/3; a.is_unit()
            True

        On the other hand, 2 is not a unit, since its parent is `\\ZZ`.

        ::

            sage: a = 2; a.is_unit()
            False
            sage: parent(a)
            Integer Ring

        However, a is a unit when viewed as an element of QQ::

            sage: a = QQ(2); a.is_unit()
            True"""
    def quo_rem(self, right) -> tuple[Any, Literal[0]]:
        """
        Return the quotient and remainder obtained by dividing ``self`` by
        ``right``. Since this element lives in a field, the remainder is always
        zero and the quotient is ``self/right``.

        TESTS:

        Test if :issue:`8671` is fixed::

            sage: # needs sage.libs.pari sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = R.quo(y^2 + 1)
            sage: S.is_field = lambda: False
            sage: F = Frac(S); u = F.one()
            sage: u.quo_rem(u)
            (1, 0)"""

class InfinityElement[P: Parent](RingElement[P]):
    def __invert__(self) -> Integer: ...

class IntegralDomainElement[P: Parent](CommutativeRingElement[P]):
    def is_nilpotent(self) -> bool: ...

class Matrix[P: Parent](ModuleElement[P]):
    def __mul__(self, right) -> Any:
        """
        Multiplication of matrix by matrix, vector, or scalar.

        AUTHOR:

        - Gonzalo Tornaria (2007-06-25) - write test cases and fix them

        .. NOTE::

            scalar * matrix is implemented (and tested) in class RingElement
            vector * matrix is implemented (and tested) in class Vector

        TESTS:

        Here we test (matrix * matrix) multiplication::

            sage: # needs sage.modules
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * matrix(QQ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * matrix(QQ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * matrix(ZZ['x'], 2, 2, [1,2,3,4]))                                # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * matrix(QQ, 2, 2, [1,2,3,4]))                                # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                           # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * matrix(QQ, 2, 2, [1,2,3,4]))                           # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * matrix(QQ['x'], 2, 2, [1,2,3,4]))                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['y'], 2, 2, [1,2,3,4]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'

        We test that the bug reported in :issue:`27352` has been fixed::

            sage: A = matrix(QQ, [[1, 2], [-1, 0], [1, 1]])                                                             # needs sage.modules
            sage: B = matrix(QQ, [[0, 4], [1, -1], [1, 2]])                                                             # needs sage.modules
            sage: A * B                                                                                                 # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            'Full MatrixSpace of 3 by 2 dense matrices over Rational Field' and 'Full MatrixSpace of 3 by 2 dense matrices over Rational Field'

        Here we test (matrix * vector) multiplication::

            sage: # needs sage.modules
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * vector(ZZ, [1,2]))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * vector(ZZ, [1,2]))
            Vector space of dimension 2 over Rational Field
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * vector(QQ, [1,2]))
            Vector space of dimension 2 over Rational Field
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * vector(QQ, [1,2]))
            Vector space of dimension 2 over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * vector(ZZ['x'], [1,2]))                                          # needs sage.modules
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * vector(QQ, [1,2]))                                          # needs sage.modules
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * vector(ZZ['x']['y'], [1,2]))                                     # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * vector(QQ, [1,2]))                                     # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * vector(ZZ['x']['y'], [1,2]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * vector(QQ['x'], [1,2]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['y'], 2, 2, [1,2,3,4]) * vector(ZZ['x']['y'], [1,2]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * vector(QQ['y'], [1,2]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * vector(ZZ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * vector(QQ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * vector(ZZ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * vector(QQ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'

        Here we test (matrix * scalar) multiplication::

            sage: # needs sage.modules
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * ZZ(1))
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * ZZ(1))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(matrix(ZZ, 2, 2, [1,2,3,4]) * QQ(1))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * QQ(1))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * ZZ['x'](1))                                                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * QQ(1))                                                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ, 2, 2, [1,2,3,4]) * ZZ['x']['y'](1))                                                 # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * QQ(1))                                                 # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * ZZ['x']['y'](1))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * QQ['x'](1))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(matrix(QQ['y'], 2, 2, [1,2,3,4]) * ZZ['x']['y'](1))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]) * QQ['y'](1))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * ZZ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(ZZ['x'], 2, 2, [1,2,3,4]) * QQ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring' and
             'Univariate Polynomial Ring in y over Rational Field'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * ZZ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
              'Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(matrix(QQ['x'], 2, 2, [1,2,3,4]) * QQ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field' and
             'Univariate Polynomial Ring in y over Rational Field'

        Here we test (scalar * matrix) multiplication::

            sage: # needs sage.modules
            sage: parent(ZZ(1) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
            sage: parent(QQ(1) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(ZZ(1) * matrix(QQ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: parent(QQ(1) * matrix(QQ, 2, 2, [1,2,3,4]))
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: parent(QQ(1) * matrix(ZZ['x'], 2, 2, [1,2,3,4]))                                                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x'](1) * matrix(QQ, 2, 2, [1,2,3,4]))                                                      # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ(1) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                                 # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * matrix(QQ, 2, 2, [1,2,3,4]))                                                 # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ['x'](1) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * matrix(QQ['x'], 2, 2, [1,2,3,4]))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ['y'](1) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices
             over Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * matrix(QQ['y'], 2, 2, [1,2,3,4]))                                            # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices
             over Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(ZZ['x'](1) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(ZZ['x'](1) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'
            sage: parent(QQ['x'](1) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(QQ['x'](1) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'

        Examples with matrices having matrix coefficients::

            sage: m = matrix                                                                                            # needs sage.modules
            sage: a = m([[m([[1,2],[3,4]]),m([[5,6],[7,8]])],[m([[9,10],[11,12]]),m([[13,14],[15,16]])]])               # needs sage.modules
            sage: 3 * a                                                                                                 # needs sage.modules
            [[ 3  6]
            [ 9 12] [15 18]
            [21 24]]
            [[27 30]
            [33 36] [39 42]
            [45 48]]

            sage: m = matrix                                                                                            # needs sage.modules
            sage: a = m([[m([[1,2],[3,4]]),m([[5,6],[7,8]])],[m([[9,10],[11,12]]),m([[13,14],[15,16]])]])               # needs sage.modules
            sage: a * 3                                                                                                 # needs sage.modules
            [[ 3  6]
            [ 9 12] [15 18]
            [21 24]]
            [[27 30]
            [33 36] [39 42]
            [45 48]]"""
    def __rmul__(self, other): ...
    def __rtruediv__(self, other): ...
    def __truediv__(self,  right) -> Any:
        """
        Division of the matrix ``left`` by the matrix or scalar
        ``right``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: a = matrix(ZZ, 2, range(4))
            sage: operator.truediv(a, 5)
            [ 0 1/5]
            [2/5 3/5]
            sage: a = matrix(ZZ, 2, range(4))
            sage: b = matrix(ZZ, 2, [1,1,0,5])
            sage: operator.truediv(a, b)
            [  0 1/5]
            [  2 1/5]
            sage: c = matrix(QQ, 2, [3,2,5,7])
            sage: operator.truediv(c, a)
            [-5/2  3/2]
            [-1/2  5/2]

        TESTS::

            sage: # needs sage.modules
            sage: a = matrix(ZZ, [[1, 2], [0, 3]])
            sage: b = matrix(ZZ, 3, 2, range(6))
            sage: x = b / a; x
            [   0  1/3]
            [   2 -1/3]
            [   4   -1]
            sage: x == b * ~a
            True
            sage: a = matrix(ZZ, [[1, 2], [0, 3], [1, 5]])
            sage: (b / a) * a == b
            True"""

class ModuleElement[P: Parent](Element[P]):
    """
        Generic element of a module.
    """

    def additive_order(self):    # NotImplemented
        """
        Return the additive order of ``self``."""
    def order(self):    # NotImplemented
        """
        Return the additive order of ``self``."""

class ModuleElementWithMutability[P: Parent](ModuleElement[P]):
    """
    Generic element of a module with mutability."""
    
    def __init__(self, parent: P, is_immutable: bool = False):
        """
                EXAMPLES::

                    sage: v = sage.modules.free_module_element.FreeModuleElement(QQ^3)          # needs sage.modules
                    sage: type(v)                                                               # needs sage.modules
                    <class 'sage.modules.free_module_element.FreeModuleElement'>
        """
    def is_immutable(self) -> bool:
        """
        Return ``True`` if this vector is immutable, i.e., the entries cannot
        be changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_immutable()                       # needs sage.modules
            False
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_immutable()                                                      # needs sage.modules
            True"""
    def is_mutable(self) -> bool:
        """
        Return ``True`` if this vector is mutable, i.e., the entries can be
        changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_mutable()                         # needs sage.modules
            True
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_mutable()                                                        # needs sage.modules
            False"""
    def set_immutable(self) -> None:
        """
        Make this vector immutable. This operation can't be undone.

        EXAMPLES::

            sage: # needs sage.modules
            sage: v = vector([1..5]); v
            (1, 2, 3, 4, 5)
            sage: v[1] = 10
            sage: v.set_immutable()
            sage: v[1] = 10
            Traceback (most recent call last):
            ...
            ValueError: vector is immutable; please change a copy instead (use copy())"""

class _N(SupportsIndex, ComparableWithZero): ...
class MonoidElement[P: Parent](Element[P]):
    """
        Generic element of a monoid.
    """
    def multiplicative_order(self):
        """MonoidElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2555)

        Return the multiplicative order of ``self``."""
    def order(self):
        """MonoidElement.order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2549)

        Return the multiplicative order of ``self``."""
    def powers(self, n: _N) -> list[Self | Any]:
        """
        Return the list `[x^0, x^1, \\ldots, x^{n-1}]`.

        EXAMPLES::

            sage: G = SymmetricGroup(4)                                                 # needs sage.groups
            sage: g = G([2, 3, 4, 1])                                                   # needs sage.groups
            sage: g.powers(4)                                                           # needs sage.groups
            [(), (1,2,3,4), (1,3)(2,4), (1,4,3,2)]"""
    def __bool__(self) -> Literal[True]: ...

class MultiplicativeGroupElement[P: Parent](MonoidElement[P]):
    """
        Generic element of a multiplicative group.
    """
    def order(self) -> Any:
        """
        Return the multiplicative order of ``self``."""
    def __invert__(self) -> Any:
        """
        Return the multiplicative inverse of ``self``.

        This may cause infinite recursion because of the default definition
        of division using inversion in ``_div_``."""

class PrincipalIdealDomainElement[P: Parent](DedekindDomainElement[P]):
    def gcd(self, right) -> Any:
        """
        Return the greatest common divisor of ``self`` and ``other``.

        TESTS:

        :issue:`30849`::

            sage: 2.gcd(pari(3))                                                        # needs sage.libs.pari
            1
            sage: type(2.gcd(pari(3)))                                                  # needs sage.libs.pari
            <class 'sage.rings.integer.Integer'>

            sage: 2.gcd(pari('1/3'))                                                    # needs sage.libs.pari
            1/3
            sage: type(2.gcd(pari('1/3')))                                              # needs sage.libs.pari
            <class 'sage.rings.rational.Rational'>

            sage: import gmpy2
            sage: 2.gcd(gmpy2.mpz(3))
            1
            sage: type(2.gcd(gmpy2.mpz(3)))
            <class 'sage.rings.integer.Integer'>

            sage: 2.gcd(gmpy2.mpq(1,3))
            1/3
            sage: type(2.gcd(pari('1/3')))                                              # needs sage.libs.pari
            <class 'sage.rings.rational.Rational'>"""
    def lcm(self, right) -> Any:
        """
        Return the least common multiple of ``self`` and ``right``.

        TESTS:

        :issue:`30849`::

            sage: 2.lcm(pari(3))                                                        # needs sage.libs.pari
            6
            sage: type(2.lcm(pari(3)))                                                  # needs sage.libs.pari
            <class 'sage.rings.integer.Integer'>

            sage: 2.lcm(pari('1/3'))                                                    # needs sage.libs.pari
            2
            sage: type(2.lcm(pari('1/3')))                                              # needs sage.libs.pari
            <class 'sage.rings.rational.Rational'>

            sage: import gmpy2
            sage: 2.lcm(gmpy2.mpz(3))
            6
            sage: type(2.lcm(gmpy2.mpz(3)))
            <class 'sage.rings.integer.Integer'>"""

class RingElement[P: Parent](ModuleElement[P]):
    def abs(self) -> Any:
        """
        Return the absolute value of ``self``.  (This just calls the ``__abs__``
        method, so it is equivalent to the ``abs()`` built-in function.)

        EXAMPLES::

            sage: RR(-1).abs()                                                          # needs sage.rings.real_mpfr
            1.00000000000000
            sage: ZZ(-1).abs()
            1
            sage: CC(I).abs()                                                           # needs sage.rings.real_mpfr sage.symbolic
            1.00000000000000
            sage: Mod(-15, 37).abs()
            Traceback (most recent call last):
            ...
            ArithmeticError: absolute value not defined on integers modulo n."""
    def additive_order(self) -> Any:
        """
        Return the additive order of ``self``."""
    def is_nilpotent(self) -> bool:
        """
        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        TESTS::

            sage: a = QQ(2)
            sage: a.is_nilpotent()
            False
            sage: a = QQ(0)
            sage: a.is_nilpotent()
            True
            sage: m = matrix(QQ, 3, [[3,2,3], [9,0,3], [-9,0,-3]])                      # needs sage.modules
            sage: m.is_nilpotent()                                                      # needs sage.modules
            True"""
    def is_one(self) -> bool: ...
    def is_prime(self) -> bool:
        """
        Check whether ``self`` is a prime element.

        A *prime* element is a nonzero, non-unit element `p` such that,
        whenever `p` divides `ab` for some `a` and `b`, then `p`
        divides `a` or `p` divides `b`.

        EXAMPLES:

        For polynomial rings, prime is the same as irreducible::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: x.is_prime()
            True
            sage: (x^2 + y^3).is_prime()
            True
            sage: (x^2 - y^2).is_prime()
            False
            sage: R(0).is_prime()
            False
            sage: R(2).is_prime()
            False

        For the Gaussian integers::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: ZI = K.ring_of_integers()
            sage: ZI(3).is_prime()
            True
            sage: ZI(5).is_prime()
            False
            sage: ZI(2 + i).is_prime()
            True
            sage: ZI(0).is_prime()
            False
            sage: ZI(1).is_prime()
            False

        In fields, an element is never prime::

            sage: RR(0).is_prime()
            False
            sage: RR(2).is_prime()
            False

        For integers, :meth:`is_prime` redefines prime numbers to be
        positive::

            sage: (-2).is_prime()
            False
            sage: RingElement.is_prime(-2)                                              # needs sage.libs.pari
            True

        Similarly,
        :class:`~sage.rings.number_field.number_field_base.NumberField`
        redefines :meth:`is_prime` to determine primality in the ring
        of integers::

            sage: # needs sage.rings.number_field
            sage: (1 + i).is_prime()
            True
            sage: K(5).is_prime()
            False
            sage: K(7).is_prime()
            True
            sage: K(7/13).is_prime()
            False

        However, for rationals, :meth:`is_prime` *does* follow the
        general definition of prime elements in a ring (i.e., always
        returns ``False``) since the rationals are not a
        :class:`~sage.rings.number_field.number_field_base.NumberField`
        in Sage::

            sage: QQ(7).is_prime()
            False"""
    def multiplicative_order(self) -> Any:
        """RingElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2848)

        Return the multiplicative order of ``self``, if ``self`` is a unit.

        This raises an :class:`ArithmeticError` otherwise."""
    def powers(self, n: _N) -> list[Self | Any]:
        """
        Return the list `[x^0, x^1, \\ldots, x^{n-1}]`.

        EXAMPLES::

            sage: 5.powers(3)
            [1, 5, 25]"""
    def __divmod__(self, other) -> Any:
        """
        Return the quotient and remainder of ``self`` divided by ``other``.

        This operation may not be defined in all rings.

        EXAMPLES::

            sage: divmod(5,3)
            (1, 2)
            sage: divmod(25r,12)
            (2, 1)
            sage: divmod(25,12r)
            (2, 1)

        ::

            sage: R.<x> = QQ[]
            sage: f = -19/13*x^5 - x^4 - 2/3*x^3 + 6*x^2 - 2
            sage: g = 3*x^2 + 5
            sage: q,r = divmod(f,g)
            sage: q
            -19/39*x^3 - 1/3*x^2 + 23/39*x + 23/9
            sage: r
            -115/39*x - 133/9
            sage: f == q*g + r
            True

        ::

            sage: R.<x> = ZZ[]
            sage: f = -2*x^5 + x^4 - 9*x^3 - 5*x^2 + 7*x + 4
            sage: g = x^2 + 5
            sage: q,r = divmod(f,g)
            sage: q
            -2*x^3 + x^2 + x - 10
            sage: r
            2*x + 54
            sage: f == q*g + r
            True
            sage: h = 3*x^2 + 5
            sage: q,r = divmod(f,h)
            sage: q
            -3*x - 2
            sage: r
            -2*x^5 + x^4 + x^2 + 22*x + 14
            sage: f == q*h + r
            True

        ::

            sage: R.<x> = GF(7)[]
            sage: divmod(x^2, x - 1)
            (x + 1, 1)

        ::

            sage: divmod(22./7, RR(pi))                                                 # needs sage.symbolic
            (1.00040249943477, 0.000000000000000)"""
    def __invert__(self) -> Self | Any: ...
    def __rdivmod__(self, other): ...

class Vector[P: Parent](ModuleElementWithMutability[P]):
    def __mul__(self, right) -> Any:
        """
        Multiplication of vector by vector, matrix, or scalar.

        AUTHOR:

        - Gonzalo Tornaria (2007-06-21) - write test cases and fix them

        .. NOTE::

            scalar * vector is implemented (and tested) in class RingElement
            matrix * vector is implemented (and tested) in class Matrix

        TESTS:

        Here we test (vector * vector) multiplication::

            sage: # needs sage.modules
            sage: parent(vector(ZZ, [1,2]) * vector(ZZ, [1,2]))
            Integer Ring
            sage: parent(vector(ZZ, [1,2]) * vector(QQ, [1,2]))
            Rational Field
            sage: parent(vector(QQ, [1,2]) * vector(ZZ, [1,2]))
            Rational Field
            sage: parent(vector(QQ, [1,2]) * vector(QQ, [1,2]))
            Rational Field

            sage: parent(vector(QQ, [1,2,3,4]) * vector(ZZ['x'], [1,2,3,4]))                                            # needs sage.modules
            Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'], [1,2,3,4]) * vector(QQ, [1,2,3,4]))                                            # needs sage.modules
            Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ, [1,2,3,4]) * vector(ZZ['x']['y'], [1,2,3,4]))                                       # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2,3,4]) * vector(QQ, [1,2,3,4]))                                       # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['x'], [1,2,3,4]) * vector(ZZ['x']['y'], [1,2,3,4]))                                  # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2,3,4]) * vector(QQ['x'], [1,2,3,4]))                                  # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['y'], [1,2,3,4]) * vector(ZZ['x']['y'], [1,2,3,4]))                                  # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2,3,4]) * vector(QQ['y'], [1,2,3,4]))                                  # needs sage.modules
            Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(vector(ZZ['x'], [1,2,3,4]) * vector(ZZ['y'], [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'], [1,2,3,4]) * vector(QQ['y'], [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'], [1,2,3,4]) * vector(ZZ['y'], [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'], [1,2,3,4]) * vector(QQ['y'], [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'

        Here we test (vector * matrix) multiplication::

            sage: # needs sage.modules
            sage: parent(vector(ZZ, [1,2]) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(QQ, [1,2]) * matrix(ZZ, 2, 2, [1,2,3,4]))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(ZZ, [1,2]) * matrix(QQ, 2, 2, [1,2,3,4]))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ, [1,2]) * matrix(QQ, 2, 2, [1,2,3,4]))
            Vector space of dimension 2 over Rational Field

            sage: parent(vector(QQ, [1,2]) * matrix(ZZ['x'], 2, 2, [1,2,3,4]))                                          # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'], [1,2]) * matrix(QQ, 2, 2, [1,2,3,4]))                                          # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ, [1,2]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                     # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * matrix(QQ, 2, 2, [1,2,3,4]))                                     # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['x'], [1,2]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * matrix(QQ['x'], 2, 2, [1,2,3,4]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['y'], [1,2]) * matrix(ZZ['x']['y'], 2, 2, [1,2,3,4]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))                                # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(vector(ZZ['x'], [1,2]) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'], [1,2]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'], [1,2]) * matrix(ZZ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'], [1,2]) * matrix(QQ['y'], 2, 2, [1,2,3,4]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in y over Rational Field'

        Here we test (vector * scalar) multiplication::

            sage: # needs sage.modules
            sage: parent(vector(ZZ, [1,2]) * ZZ(1))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(QQ, [1,2]) * ZZ(1))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(ZZ, [1,2]) * QQ(1))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ, [1,2]) * QQ(1))
            Vector space of dimension 2 over Rational Field

            sage: parent(vector(QQ, [1,2]) * ZZ['x'](1))                                                                # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'], [1,2]) * QQ(1))                                                                # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ, [1,2]) * ZZ['x']['y'](1))                                                           # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * QQ(1))                                                           # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['x'], [1,2]) * ZZ['x']['y'](1))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * QQ['x'](1))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(vector(QQ['y'], [1,2]) * ZZ['x']['y'](1))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'], [1,2]) * QQ['y'](1))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(vector(ZZ['x'], [1,2]) * ZZ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'], [1,2]) * QQ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
             'Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'], [1,2]) * ZZ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'], [1,2]) * QQ['y'](1))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
             'Univariate Polynomial Ring in y over Rational Field'

        Here we test (scalar * vector) multiplication::

            sage: # needs sage.modules
            sage: parent(ZZ(1) * vector(ZZ, [1,2]))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(QQ(1) * vector(ZZ, [1,2]))
            Vector space of dimension 2 over Rational Field
            sage: parent(ZZ(1) * vector(QQ, [1,2]))
            Vector space of dimension 2 over Rational Field
            sage: parent(QQ(1) * vector(QQ, [1,2]))
            Vector space of dimension 2 over Rational Field

            sage: parent(QQ(1) * vector(ZZ['x'], [1,2]))                                                                # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x'](1) * vector(QQ, [1,2]))                                                                # needs sage.modules
            Ambient free module of rank 2
             over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ(1) * vector(ZZ['x']['y'], [1,2]))                                                           # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * vector(QQ, [1,2]))                                                           # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ['x'](1) * vector(ZZ['x']['y'], [1,2]))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * vector(QQ['x'], [1,2]))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: parent(QQ['y'](1) * vector(ZZ['x']['y'], [1,2]))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(ZZ['x']['y'](1) * vector(QQ['y'], [1,2]))                                                      # needs sage.modules
            Ambient free module of rank 2 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

            sage: # needs sage.modules
            sage: parent(ZZ['x'](1) * vector(ZZ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(ZZ['x'](1) * vector(QQ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Integer Ring' and
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(QQ['x'](1) * vector(ZZ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Rational Field' and
             'Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(QQ['x'](1) * vector(QQ['y'], [1,2]))
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Univariate Polynomial Ring in x over Rational Field' and
             'Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'"""
    def __rmul__(self, other): ...
    def __rtruediv__(self, other): ...
    def __truediv__(self, right) -> Any:
        """
        Divide this vector by a scalar, vector or matrix.

        TESTS::

            sage: # needs sage.modules
            sage: A = matrix([[1, 2], [0, 3]])
            sage: b = vector([0, 1])
            sage: x = b / A; x
            (0, 1/3)
            sage: x == b * ~A
            True
            sage: A = matrix([[1, 2], [0, 3], [1, 5]])
            sage: (b / A) * A == b
            True"""

