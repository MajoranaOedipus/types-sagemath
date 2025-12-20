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

import _cython_3_2_1
import sage.structure.coerce
import sage.structure.sage_object
from sage.structure.parent import Parent
from sage.arith.numerical_approx import digits_to_bits as digits_to_bits
from sage.misc.decorators import sage_wraps as sage_wraps
from sage.misc.lazy_format import LazyFormat as LazyFormat
from sage.misc.superseded import deprecation as deprecation
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, TypeVar, overload

__pyx_capi__: dict
bin_op: _cython_3_2_1.cython_function_or_method
def canonical_coercion(x, y) -> tuple:
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

coerce_binop: _cython_3_2_1.cython_function_or_method
coercion_model: sage.structure.coerce.CoercionModel
coercion_traceback: _cython_3_2_1.cython_function_or_method
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
is_AdditiveGroupElement: _cython_3_2_1.cython_function_or_method
is_AlgebraElement: _cython_3_2_1.cython_function_or_method
is_CommutativeAlgebraElement: _cython_3_2_1.cython_function_or_method
is_CommutativeRingElement: _cython_3_2_1.cython_function_or_method
is_DedekindDomainElement: _cython_3_2_1.cython_function_or_method
is_Element: _cython_3_2_1.cython_function_or_method
is_EuclideanDomainElement: _cython_3_2_1.cython_function_or_method
is_FieldElement: _cython_3_2_1.cython_function_or_method
is_InfinityElement: _cython_3_2_1.cython_function_or_method
is_IntegralDomainElement: _cython_3_2_1.cython_function_or_method
is_Matrix: _cython_3_2_1.cython_function_or_method
is_ModuleElement: _cython_3_2_1.cython_function_or_method
is_MonoidElement: _cython_3_2_1.cython_function_or_method
is_MultiplicativeGroupElement: _cython_3_2_1.cython_function_or_method
is_PrincipalIdealDomainElement: _cython_3_2_1.cython_function_or_method
is_RingElement: _cython_3_2_1.cython_function_or_method
is_Vector: _cython_3_2_1.cython_function_or_method
make_element: _cython_3_2_1.cython_function_or_method

@overload
def parent(x: Element) -> Parent:   # pyright: ignore[reportOverlappingOverload] # 
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


class AdditiveGroupElement(ModuleElement):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2602)

        Generic element of an additive group.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def order(self) -> Any:
        """AdditiveGroupElement.order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2606)

        Return additive order of element"""
    def __invert__(self) -> Any:
        """AdditiveGroupElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2612)"""

class AlgebraElement(RingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class CommutativeAlgebraElement(CommutativeRingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class CommutativeRingElement(RingElement):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3007)

        Base class for elements of commutative rings.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def divides(self, x) -> Any:
        """CommutativeRingElement.divides(self, x)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3043)

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
    @overload
    def divides(self, x) -> Any:
        """CommutativeRingElement.divides(self, x)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3043)

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
    @overload
    def divides(self, x) -> Any:
        """CommutativeRingElement.divides(self, x)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3043)

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
        """CommutativeRingElement.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3012)

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
    @overload
    def is_square(self, root=...) -> Any:
        """CommutativeRingElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3221)

        Return whether or not the ring element ``self`` is a square.

        If the optional argument root is ``True``, then also return
        the square root (or ``None``, if it is not a square).

        INPUT:

        - ``root`` -- boolean (default: ``False``); whether or not to also
          return a square root

        OUTPUT:

        - boolean; whether or not a square

        - object; (optional) an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = 12*(x+1)^2 * (x+3)^2
            sage: f.is_square()
            False
            sage: f.is_square(root=True)
            (False, None)
            sage: h = f/3
            sage: h.is_square()
            True
            sage: h.is_square(root=True)
            (True, 2*x^2 + 8*x + 6)

        .. NOTE::

            This is the is_square implementation for general commutative ring
            elements. It's implementation is to raise a
            :exc:`NotImplementedError`. The function definition is here to show
            what functionality is expected and provide a general framework."""
    @overload
    def is_square(self) -> Any:
        """CommutativeRingElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3221)

        Return whether or not the ring element ``self`` is a square.

        If the optional argument root is ``True``, then also return
        the square root (or ``None``, if it is not a square).

        INPUT:

        - ``root`` -- boolean (default: ``False``); whether or not to also
          return a square root

        OUTPUT:

        - boolean; whether or not a square

        - object; (optional) an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = 12*(x+1)^2 * (x+3)^2
            sage: f.is_square()
            False
            sage: f.is_square(root=True)
            (False, None)
            sage: h = f/3
            sage: h.is_square()
            True
            sage: h.is_square(root=True)
            (True, 2*x^2 + 8*x + 6)

        .. NOTE::

            This is the is_square implementation for general commutative ring
            elements. It's implementation is to raise a
            :exc:`NotImplementedError`. The function definition is here to show
            what functionality is expected and provide a general framework."""
    @overload
    def is_square(self, root=...) -> Any:
        """CommutativeRingElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3221)

        Return whether or not the ring element ``self`` is a square.

        If the optional argument root is ``True``, then also return
        the square root (or ``None``, if it is not a square).

        INPUT:

        - ``root`` -- boolean (default: ``False``); whether or not to also
          return a square root

        OUTPUT:

        - boolean; whether or not a square

        - object; (optional) an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = 12*(x+1)^2 * (x+3)^2
            sage: f.is_square()
            False
            sage: f.is_square(root=True)
            (False, None)
            sage: h = f/3
            sage: h.is_square()
            True
            sage: h.is_square(root=True)
            (True, 2*x^2 + 8*x + 6)

        .. NOTE::

            This is the is_square implementation for general commutative ring
            elements. It's implementation is to raise a
            :exc:`NotImplementedError`. The function definition is here to show
            what functionality is expected and provide a general framework."""
    @overload
    def is_square(self) -> Any:
        """CommutativeRingElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3221)

        Return whether or not the ring element ``self`` is a square.

        If the optional argument root is ``True``, then also return
        the square root (or ``None``, if it is not a square).

        INPUT:

        - ``root`` -- boolean (default: ``False``); whether or not to also
          return a square root

        OUTPUT:

        - boolean; whether or not a square

        - object; (optional) an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = 12*(x+1)^2 * (x+3)^2
            sage: f.is_square()
            False
            sage: f.is_square(root=True)
            (False, None)
            sage: h = f/3
            sage: h.is_square()
            True
            sage: h.is_square(root=True)
            (True, 2*x^2 + 8*x + 6)

        .. NOTE::

            This is the is_square implementation for general commutative ring
            elements. It's implementation is to raise a
            :exc:`NotImplementedError`. The function definition is here to show
            what functionality is expected and provide a general framework."""
    @overload
    def is_square(self, root=...) -> Any:
        """CommutativeRingElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3221)

        Return whether or not the ring element ``self`` is a square.

        If the optional argument root is ``True``, then also return
        the square root (or ``None``, if it is not a square).

        INPUT:

        - ``root`` -- boolean (default: ``False``); whether or not to also
          return a square root

        OUTPUT:

        - boolean; whether or not a square

        - object; (optional) an actual square root if found, and ``None``
          otherwise

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = 12*(x+1)^2 * (x+3)^2
            sage: f.is_square()
            False
            sage: f.is_square(root=True)
            (False, None)
            sage: h = f/3
            sage: h.is_square()
            True
            sage: h.is_square(root=True)
            (True, 2*x^2 + 8*x + 6)

        .. NOTE::

            This is the is_square implementation for general commutative ring
            elements. It's implementation is to raise a
            :exc:`NotImplementedError`. The function definition is here to show
            what functionality is expected and provide a general framework."""
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
    @overload
    def sqrt(self, extend=..., all=..., name=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, all=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, name=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, all=..., name=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, all=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, all=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, name=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, all=..., name=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """CommutativeRingElement.sqrt(self, extend=True, all=False, name=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3263)

        Compute the square root.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); whether to make a ring
          extension containing a square root if ``self`` is not a square

        - ``all`` -- boolean (default: ``False``); whether to return a list of
          all square roots or just a square root

        - ``name`` -- required when ``extend=True`` and ``self`` is not a
          square; this will be the name of the generator of the extension

        OUTPUT:

        - if ``all=False``, a square root; raises an error if ``extend=False``
          and ``self`` is not a square

        - if ``all=True``, a list of all the square roots (empty if
          ``extend=False`` and ``self`` is not a square)

        ALGORITHM:

        It uses ``is_square(root=true)`` for the hard part of the work, the rest
        is just wrapper code.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<x> = ZZ[]
            sage: (x^2).sqrt()
            x
            sage: f = x^2 - 4*x + 4; f.sqrt(all=True)
            [x - 2, -x + 2]
            sage: sqrtx = x.sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            x
            sage: x.sqrt(all=true, name='y')
            [y, -y]
            sage: x.sqrt(extend=False, all=True)
            []
            sage: x.sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square x with extend = False

        TESTS::

            sage: # needs sage.libs.pari
            sage: f = (x + 3)^2; f.sqrt()
            x + 3
            sage: f = (x + 3)^2; f.sqrt(all=True)
            [x + 3, -x - 3]
            sage: f = (x^2 - x + 3)^2; f.sqrt()
            x^2 - x + 3
            sage: f = (x^2 - x + 3)^6; f.sqrt()
            x^6 - 3*x^5 + 12*x^4 - 19*x^3 + 36*x^2 - 27*x + 27
            sage: g = (R.random_element(15))^2
            sage: g.sqrt()^2 == g
            True

            sage: # needs sage.libs.pari
            sage: R.<x> = GF(250037)[]
            sage: f = x^2/(x+1)^2; f.sqrt()
            x/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt()
            3*x^2/(x + 1)
            sage: f = 9 * x^4 / (x+1)^2; f.sqrt(all=True)
            [3*x^2/(x + 1), 250034*x^2/(x + 1)]

            sage: R.<x> = QQ[]
            sage: a = 2*(x+1)^2 / (2*(x-1)^2); a.sqrt()
            (x + 1)/(x - 1)
            sage: sqrtx=(1/x).sqrt(name='y'); sqrtx
            y
            sage: sqrtx^2
            1/x
            sage: (1/x).sqrt(all=true, name='y')
            [y, -y]
            sage: (1/x).sqrt(extend=False, all=True)
            []
            sage: (1/(x^2-1)).sqrt()
            Traceback (most recent call last):
            ...
            TypeError: Polynomial is not a square. You must specify the name
            of the square root when using the default extend = True
            sage: (1/(x^2-3)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: trying to take square root of non-square 1/(x^2 - 3) with extend = False"""

class DedekindDomainElement(IntegralDomainElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Element(sage.structure.sage_object.SageObject):
    """Element(parent)

    File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 369)

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
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 393)

                INPUT:

                - ``parent`` -- a SageObject
        """
    def base_extend(self, R) -> Any:
        """Element.base_extend(self, R)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 643)"""
    def base_ring(self) -> Any:
        """Element.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 648)

        Return the base ring of this element's parent (if that makes sense).

        TESTS::

            sage: QQ.base_ring()
            Rational Field
            sage: identity_matrix(3).base_ring()                                        # needs sage.modules
            Integer Ring"""
    def category(self) -> Any:
        """Element.category(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 661)"""
    def is_zero(self) -> Any:
        """Element.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1044)

        Return ``True`` if ``self`` equals ``self.parent()(0)``.

        The default implementation is to fall back to ``not
        self.__bool__``.

        .. WARNING::

            Do not re-implement this method in your subclass but
            implement ``__bool__`` instead."""
    @overload
    def n(self, prec=..., digits=..., algorithm=...) -> Any:
        """Element.n(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 894)

        Alias for :meth:`numerical_approx`.

        EXAMPLES::

            sage: (2/3).n()                                                             # needs sage.rings.real_mpfr
            0.666666666666667"""
    @overload
    def n(self) -> Any:
        """Element.n(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 894)

        Alias for :meth:`numerical_approx`.

        EXAMPLES::

            sage: (2/3).n()                                                             # needs sage.rings.real_mpfr
            0.666666666666667"""
    @overload
    def numerical_approx(self, prec=..., digits=..., algorithm=...) -> Any:
        """Element.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 853)

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
    @overload
    def numerical_approx(self) -> Any:
        """Element.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 853)

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
    def parent(self, x=...) -> Any:
        """Element.parent(self, x=None)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 770)

        Return the parent of this element; or, if the optional argument x is
        supplied, the result of coercing x into the parent of this element."""
    @overload
    def subs(self, in_dict=..., **kwds) -> Any:
        """Element.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 780)

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
    @overload
    def subs(self, x=...) -> Any:
        """Element.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 780)

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
    @overload
    def subs(self, x=...) -> Any:
        """Element.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 780)

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
    @overload
    def subs(self, x=...) -> Any:
        """Element.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 780)

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
    @overload
    def substitute(self, *args, **kwds) -> Any:
        """Element.substitute(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 832)

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
    @overload
    def substitute(self, x=...) -> Any:
        """Element.substitute(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 832)

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
    @overload
    def substitute(self, x=...) -> Any:
        """Element.substitute(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 832)

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
    @overload
    def substitute(self, x=...) -> Any:
        """Element.substitute(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 832)

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
    def __add__(self, left, right) -> Any:
        """Element.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1173)

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
        """True if self else False"""
    def __copy__(self) -> Any:
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
    def __dir__(self) -> Any:
        """Element.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 510)

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
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __floordiv__(self, left, right) -> Any:
        """Element.__floordiv__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1774)

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
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getmetaclass__(self, _) -> Any:
        """Element.__getmetaclass__(_)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 387)"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __matmul__(self, left, right) -> Any:
        """Element.__matmul__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1579)

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
    def __mod__(self, left, right) -> Any:
        """Element.__mod__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1874)

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
    @overload
    def __mul__(self, left, right) -> Any:
        """Element.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1444)

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
    @overload
    def __mul__(self, x) -> Any:
        """Element.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1444)

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
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """Element.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1390)

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
    def __pos__(self) -> Any:
        """Element.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 960)"""
    def __pow__(self, left, right, modulus) -> Any:
        """Element.__pow__(left, right, modulus)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1974)

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
    def __radd__(self, other):
        """Return value+self."""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rmatmul__(self, *args, **kwargs):
        """Return value@self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __sub__(self, left, right) -> Any:
        """Element.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1299)

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
    @overload
    def __truediv__(self, left, right) -> Any:
        ...
    @overload
    def __truediv__(self, right) -> Any:
        """Element.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 1671)

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
    def __xor__(self, right) -> Any:
        """Element.__xor__(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 956)"""

class ElementWithCachedMethod(Element):
    '''File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2162)

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
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class EuclideanDomainElement(PrincipalIdealDomainElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def degree(self) -> Any:
        """EuclideanDomainElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4321)"""
    def leading_coefficient(self) -> Any:
        """EuclideanDomainElement.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4324)"""
    def quo_rem(self, other) -> Any:
        """EuclideanDomainElement.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4327)"""

class Expression(CommutativeRingElement):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3400)

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
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class FieldElement(CommutativeRingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def canonical_associate(self) -> Any:
        """FieldElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4494)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]; k=R.fraction_field()
            sage: (x/y).canonical_associate()
            (1, x/y)
            sage: (0).canonical_associate()
            (0, 1)"""
    @overload
    def canonical_associate(self) -> Any:
        """FieldElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4494)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]; k=R.fraction_field()
            sage: (x/y).canonical_associate()
            (1, x/y)
            sage: (0).canonical_associate()
            (0, 1)"""
    @overload
    def canonical_associate(self) -> Any:
        """FieldElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4494)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]; k=R.fraction_field()
            sage: (x/y).canonical_associate()
            (1, x/y)
            sage: (0).canonical_associate()
            (0, 1)"""
    @overload
    def divides(self, FieldElementother) -> Any:
        """FieldElement.divides(self, FieldElement other)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4470)

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
    @overload
    def divides(self, rt3) -> Any:
        """FieldElement.divides(self, FieldElement other)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4470)

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
    @overload
    def is_unit(self) -> Any:
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
    @overload
    def is_unit(self) -> Any:
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
    @overload
    def quo_rem(self, right) -> Any:
        """FieldElement.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4448)

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
    @overload
    def quo_rem(self, u) -> Any:
        """FieldElement.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4448)

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

class InfinityElement(RingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __invert__(self) -> Any:
        """InfinityElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4575)"""

class IntegralDomainElement(CommutativeRingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def is_nilpotent(self) -> Any:
        """IntegralDomainElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4204)"""

class Matrix(ModuleElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __mul__(self, left, right) -> Any:
        """Matrix.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3805)

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
    def __rmul__(self, other):
        """Return value*self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, left, right) -> Any:
        """Matrix.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4137)

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

class ModuleElement(Element):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2377)

        Generic element of a module.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def additive_order(self) -> Any:
        """ModuleElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2456)

        Return the additive order of ``self``."""
    def order(self) -> Any:
        """ModuleElement.order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2449)

        Return the additive order of ``self``."""

class ModuleElementWithMutability(ModuleElement):
    """ModuleElementWithMutability(parent, is_immutable=False)

    File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2462)

    Generic element of a module with mutability."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, is_immutable=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2467)

                EXAMPLES::

                    sage: v = sage.modules.free_module_element.FreeModuleElement(QQ^3)          # needs sage.modules
                    sage: type(v)                                                               # needs sage.modules
                    <class 'sage.modules.free_module_element.FreeModuleElement'>
        """
    @overload
    def is_immutable(self) -> bool:
        """ModuleElementWithMutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2511)

        Return ``True`` if this vector is immutable, i.e., the entries cannot
        be changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_immutable()                       # needs sage.modules
            False
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_immutable()                                                      # needs sage.modules
            True"""
    @overload
    def is_immutable(self) -> Any:
        """ModuleElementWithMutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2511)

        Return ``True`` if this vector is immutable, i.e., the entries cannot
        be changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_immutable()                       # needs sage.modules
            False
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_immutable()                                                      # needs sage.modules
            True"""
    @overload
    def is_immutable(self) -> Any:
        """ModuleElementWithMutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2511)

        Return ``True`` if this vector is immutable, i.e., the entries cannot
        be changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_immutable()                       # needs sage.modules
            False
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_immutable()                                                      # needs sage.modules
            True"""
    @overload
    def is_mutable(self) -> bool:
        """ModuleElementWithMutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2496)

        Return ``True`` if this vector is mutable, i.e., the entries can be
        changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_mutable()                         # needs sage.modules
            True
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_mutable()                                                        # needs sage.modules
            False"""
    @overload
    def is_mutable(self) -> Any:
        """ModuleElementWithMutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2496)

        Return ``True`` if this vector is mutable, i.e., the entries can be
        changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_mutable()                         # needs sage.modules
            True
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_mutable()                                                        # needs sage.modules
            False"""
    @overload
    def is_mutable(self) -> Any:
        """ModuleElementWithMutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2496)

        Return ``True`` if this vector is mutable, i.e., the entries can be
        changed.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.is_mutable()                         # needs sage.modules
            True
            sage: v.set_immutable()                                                     # needs sage.modules
            sage: v.is_mutable()                                                        # needs sage.modules
            False"""
    def set_immutable(self) -> Any:
        """ModuleElementWithMutability.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2478)

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

class MonoidElement(Element):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2540)

        Generic element of a monoid.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def multiplicative_order(self) -> Any:
        """MonoidElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2555)

        Return the multiplicative order of ``self``."""
    def order(self) -> Any:
        """MonoidElement.order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2549)

        Return the multiplicative order of ``self``."""
    def powers(self, n) -> Any:
        """MonoidElement.powers(self, n)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2567)

        Return the list `[x^0, x^1, \\ldots, x^{n-1}]`.

        EXAMPLES::

            sage: G = SymmetricGroup(4)                                                 # needs sage.groups
            sage: g = G([2, 3, 4, 1])                                                   # needs sage.groups
            sage: g.powers(4)                                                           # needs sage.groups
            [(), (1,2,3,4), (1,3)(2,4), (1,4,3,2)]"""
    def __bool__(self) -> bool:
        """True if self else False"""

class MultiplicativeGroupElement(MonoidElement):
    """File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2625)

        Generic element of a multiplicative group.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def order(self) -> Any:
        """MultiplicativeGroupElement.order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2629)

        Return the multiplicative order of ``self``."""
    def __invert__(self) -> Any:
        """MultiplicativeGroupElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2642)

        Return the multiplicative inverse of ``self``.

        This may cause infinite recursion because of the default definition
        of division using inversion in ``_div_``."""

class PrincipalIdealDomainElement(DedekindDomainElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd(self, right) -> Any:
        """PrincipalIdealDomainElement.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4231)

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
        """PrincipalIdealDomainElement.lcm(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 4270)

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

class RingElement(ModuleElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
    @overload
    def abs(self) -> Any:
        """RingElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2881)

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
        """RingElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2842)

        Return the additive order of ``self``."""
    @overload
    def is_nilpotent(self) -> Any:
        """RingElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2858)

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
    @overload
    def is_nilpotent(self) -> Any:
        """RingElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2858)

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
    @overload
    def is_nilpotent(self) -> Any:
        """RingElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2858)

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
    @overload
    def is_nilpotent(self) -> Any:
        """RingElement.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2858)

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
    def is_one(self) -> Any:
        """RingElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2677)"""
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    @overload
    def is_prime(self) -> Any:
        """RingElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2901)

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
    def powers(self, n) -> Any:
        """RingElement.powers(self, n)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2743)

        Return the list `[x^0, x^1, \\ldots, x^{n-1}]`.

        EXAMPLES::

            sage: 5.powers(3)
            [1, 5, 25]"""
    def __divmod__(self, other) -> Any:
        """RingElement.__divmod__(self, other)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2773)

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
    def __invert__(self) -> Any:
        """RingElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 2839)"""
    def __rdivmod__(self, other):
        """Return divmod(value, self)."""

class Vector(ModuleElementWithMutability):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __mul__(self, left, right) -> Any:
        """Vector.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3430)

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
    def __rmul__(self, other):
        """Return value*self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, right) -> Any:
        """Vector.__truediv__(self, right)

        File: /build/sagemath/src/sage/src/sage/structure/element.pyx (starting at line 3714)

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
