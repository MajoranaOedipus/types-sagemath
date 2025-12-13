import _cython_3_2_1
import sage as sage
import sage.structure.element
from sage.arith.numerical_approx import digits_to_bits as digits_to_bits
from sage.categories.category import ZZ as ZZ, __one__ as __one__, __two__ as __two__
from sage.categories.rings import Rings as Rings
from sage.rings.abc import ComplexDoubleField as ComplexDoubleField, RealDoubleField as RealDoubleField
from sage.rings.infinity import AnInfinity as AnInfinity, Infinity as Infinity
from sage.structure.element import canonical_coercion as canonical_coercion, have_same_parent as have_same_parent, parent as parent, Vector as Vector
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence
from typing import Any, ClassVar, Iterable, overload

free_module_element: _cython_3_2_1.cython_function_or_method
is_FreeModuleElement: _cython_3_2_1.cython_function_or_method
make_FreeModuleElement_generic_dense: _cython_3_2_1.cython_function_or_method
make_FreeModuleElement_generic_dense_v1: _cython_3_2_1.cython_function_or_method
make_FreeModuleElement_generic_sparse: _cython_3_2_1.cython_function_or_method
make_FreeModuleElement_generic_sparse_v1: _cython_3_2_1.cython_function_or_method
prepare: _cython_3_2_1.cython_function_or_method
random_vector: _cython_3_2_1.cython_function_or_method

@overload
def vector(object: Iterable, 
           sparse: bool | None = None, immutable: bool = False) -> Vector:
    ...
@overload
def vector(object: Iterable, ring: Rings,
           sparse: bool | None = None, immutable: bool = False) -> Vector:
    ...
@overload
def vector(ring: Rings, object: Iterable,
           sparse: bool | None = None, immutable: bool = False) -> Vector:
    ...
@overload
def vector(ring: Rings, degree: int, object: Iterable, 
           sparse: bool | None = None, immutable: bool = False) -> Vector:
    ...
@overload
def vector(ring: Rings, degree: int,
           sparse: bool | None = None, immutable: bool = False) -> Vector:
    """
    vector(arg0, arg1=None, arg2=None, sparse=None, immutable=False)

File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 157)

Return a vector or free module element with specified entries.

CALL FORMATS:

This constructor can be called in several different ways.
In each case, ``sparse=True`` or ``sparse=False`` as well
as ``immutable=True`` or ``immutable=False`` can be
supplied as an option.  ``free_module_element()`` is an
alias for ``vector()``.

    1. vector(object)

    2. vector(ring, object)

    3. vector(object, ring)

    4. vector(ring, degree, object)

    5. vector(ring, degree)

INPUT:

- ``object`` -- list, dictionary, or other
  iterable containing the entries of the vector, including
  any object that is palatable to the ``Sequence`` constructor

- ``ring`` -- a base ring (or field) for the vector space or free module,
  which contains all of the elements

- ``degree`` -- integer specifying the number of
  entries in the vector or free module element

- ``sparse`` -- boolean, whether the result should be a sparse vector

- ``immutable`` -- boolean (default: ``False``); whether the result
  should be an immutable vector

In call format 4, an error is raised if the ``degree`` does not match
the length of ``object`` so this call can provide some safeguards.
Note however that using this format when ``object`` is a dictionary
is unlikely to work properly.

OUTPUT:

An element of the ambient vector space or free module with the
given base ring and implied or specified dimension or rank,
containing the specified entries and with correct degree.

In call format 5, no entries are specified, so the element is
populated with all zeros.

If the ``sparse`` option is not supplied, the output will
generally have a dense representation.  The exception is if
``object`` is a dictionary, then the representation will be sparse.

EXAMPLES::

    sage: v = vector([1,2,3]); v
    (1, 2, 3)
    sage: v.parent()
    Ambient free module of rank 3 over the principal ideal domain Integer Ring
    sage: v = vector([1,2,3/5]); v
    (1, 2, 3/5)
    sage: v.parent()
    Vector space of dimension 3 over Rational Field

All entries must *canonically* coerce to some common ring::

    sage: v = vector([17, GF(11)(5), 19/3]); v
    Traceback (most recent call last):
    ...
    TypeError: unable to find a common ring for all elements

::

    sage: v = vector([17, GF(11)(5), 19]); v
    (6, 5, 8)
    sage: v.parent()
    Vector space of dimension 3 over Finite Field of size 11
    sage: v = vector([17, GF(11)(5), 19], QQ); v
    (17, 5, 19)
    sage: v.parent()
    Vector space of dimension 3 over Rational Field
    sage: v = vector((1,2,3), QQ); v
    (1, 2, 3)
    sage: v.parent()
    Vector space of dimension 3 over Rational Field
    sage: v = vector(QQ, (1,2,3)); v
    (1, 2, 3)
    sage: v.parent()
    Vector space of dimension 3 over Rational Field
    sage: v = vector(vector([1,2,3])); v
    (1, 2, 3)
    sage: v.parent()
    Ambient free module of rank 3 over the principal ideal domain Integer Ring

You can also use ``free_module_element``, which is
the same as ``vector``. ::

    sage: free_module_element([1/3, -4/5])
    (1/3, -4/5)

We make a vector mod 3 out of a vector over `\ZZ`. ::

    sage: vector(vector([1,2,3]), GF(3))
    (1, 2, 0)

The degree of a vector may be specified::

    sage: vector(QQ, 4, [1,1/2,1/3,1/4])
    (1, 1/2, 1/3, 1/4)

But it is an error if the degree and size of the list of entries
are mismatched::

    sage: vector(QQ, 5, [1,1/2,1/3,1/4])
    Traceback (most recent call last):
    ...
    ValueError: incompatible degrees in vector constructor

Providing no entries populates the vector with zeros, but of course,
you must specify the degree since it is not implied.  Here we use a
finite field as the base ring. ::

    sage: w = vector(FiniteField(7), 4); w
    (0, 0, 0, 0)
    sage: w.parent()
    Vector space of dimension 4 over Finite Field of size 7

The fastest method to construct a zero vector is to call the
:meth:`~sage.modules.free_module.FreeModule_generic.zero_vector`
method directly on a free module or vector space, since
vector(...)  must do a small amount of type checking.  Almost as
fast as the ``zero_vector()`` method is the
:func:`~sage.modules.free_module_element.zero_vector` constructor,
which defaults to the integers.  ::

    sage: vector(ZZ, 5)          # works fine
    (0, 0, 0, 0, 0)
    sage: (ZZ^5).zero_vector()   # very tiny bit faster
    (0, 0, 0, 0, 0)
    sage: zero_vector(ZZ, 5)     # similar speed to vector(...)
    (0, 0, 0, 0, 0)
    sage: z = zero_vector(5); z
    (0, 0, 0, 0, 0)
    sage: z.parent()
    Ambient free module of rank 5 over
    the principal ideal domain Integer Ring

Here we illustrate the creation of sparse vectors by using a
dictionary::

    sage: vector({1:1.1, 3:3.14})
    (0.000000000000000, 1.10000000000000, 0.000000000000000, 3.14000000000000)

With no degree given, a dictionary of entries implicitly declares a
degree by the largest index (key) present.  So you can provide a
terminal element (perhaps a zero?) to set the degree.  But it is probably safer
to just include a degree in your construction.  ::

    sage: v = vector(QQ, {0:1/2, 4:-6, 7:0}); v
    (1/2, 0, 0, 0, -6, 0, 0, 0)
    sage: v.degree()
    8
    sage: v.is_sparse()
    True
    sage: w = vector(QQ, 8, {0:1/2, 4:-6})
    sage: w == v
    True

It is an error to specify a negative degree. ::

    sage: vector(RR, -4, [1.0, 2.0, 3.0, 4.0])
    Traceback (most recent call last):
    ...
    ValueError: cannot specify the degree of a vector as a negative integer (-4)

It is an error to create a zero vector but not provide
a ring as the first argument.  ::

    sage: vector('junk', 20)
    Traceback (most recent call last):
    ...
    TypeError: first argument must be base ring of zero vector, not junk

And it is an error to specify an index in a dictionary
that is greater than or equal to a requested degree. ::

    sage: vector(ZZ, 10, {3:4, 7:-2, 10:637})
    Traceback (most recent call last):
    ...
    ValueError: dictionary of entries has a key (index) exceeding the requested degree

A 1-dimensional numpy array of type float or complex may be
passed to vector. Unless an explicit ring is given, the result will
be a vector in the appropriate dimensional vector space over the
real double field or the complex double field. The data in the array
must be contiguous, so column-wise slices of numpy matrices will
raise an exception. ::

    sage: # needs numpy
    sage: import numpy
    sage: x = numpy.random.randn(10)
    sage: y = vector(x)
    sage: parent(y)
    Vector space of dimension 10 over Real Double Field
    sage: parent(vector(RDF, x))
    Vector space of dimension 10 over Real Double Field
    sage: parent(vector(CDF, x))
    Vector space of dimension 10 over Complex Double Field
    sage: parent(vector(RR, x))
    Vector space of dimension 10 over Real Field with 53 bits of precision
    sage: v = numpy.random.randn(10) * complex(0,1)
    sage: w = vector(v)
    sage: parent(w)
    Vector space of dimension 10 over Complex Double Field

Multi-dimensional arrays are not supported::

    sage: # needs numpy
    sage: import numpy as np
    sage: a = np.array([[1, 2, 3], [4, 5, 6]], np.float64)
    sage: vector(a)
    Traceback (most recent call last):
    ...
    TypeError: cannot convert 2-dimensional array to a vector

If any of the arguments to vector have Python type int, real,
or complex, they will first be coerced to the appropriate Sage
objects. This fixes :issue:`3847`. ::

    sage: v = vector([int(0)]); v
    (0)
    sage: v[0].parent()
    Integer Ring
    sage: v = vector(range(10)); v
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    sage: v[3].parent()
    Integer Ring
    sage: v = vector([float(23.4), int(2), complex(2+7*I), 1]); v                   # needs sage.symbolic
    (23.4, 2.0, 2.0 + 7.0*I, 1.0)
    sage: v[1].parent()                                                             # needs sage.symbolic
    Complex Double Field

If the argument is a vector, it doesn't change the base ring. This
fixes :issue:`6643`::

    sage: # needs sage.rings.number_field
    sage: K.<sqrt3> = QuadraticField(3)
    sage: u = vector(K, (1/2, sqrt3/2))
    sage: vector(u).base_ring()
    Number Field in sqrt3 with defining polynomial x^2 - 3 with sqrt3 = 1.732050807568878?
    sage: v = vector(K, (0, 1))
    sage: vector(v).base_ring()
    Number Field in sqrt3 with defining polynomial x^2 - 3 with sqrt3 = 1.732050807568878?

Constructing a vector from a numpy array behaves as expected::

    sage: # needs numpy
    sage: import numpy
    sage: a = numpy.array([1,2,3])
    sage: v = vector(a); v
    (1, 2, 3)
    sage: parent(v)
    Ambient free module of rank 3 over the principal ideal domain Integer Ring

Complex numbers can be converted naturally to a sequence of length 2.  And
then to a vector.  ::

    sage: c = CDF(2 + 3*I)                                                          # needs sage.rings.complex_double sage.symbolic
    sage: v = vector(c); v                                                          # needs sage.rings.complex_double sage.symbolic
    (2.0, 3.0)

A generator, or other iterable, may also be supplied as input.  Anything
that can be converted to a :class:`~sage.structure.sequence.Sequence` is
a possible input.  ::

    sage: type(i^2 for i in range(3))
    <... 'generator'>
    sage: v = vector(i^2 for i in range(3)); v
    (0, 1, 4)

An empty list, without a ring given, will default to the integers. ::

    sage: x = vector([]); x
    ()
    sage: x.parent()
    Ambient free module of rank 0 over the principal ideal domain Integer Ring

The ``immutable`` switch allows to create an immutable vector. ::

    sage: v = vector(QQ, {0:1/2, 4:-6, 7:0}, immutable=True); v
    (1/2, 0, 0, 0, -6, 0, 0, 0)
    sage: v.is_immutable()
    True

The ``immutable`` switch works regardless of the type of valid input to the
constructor. ::

    sage: v = vector(ZZ, 4, immutable=True)
    sage: v.is_immutable()
    True
    sage: w = vector(ZZ, [1,2,3])
    sage: v = vector(w, ZZ, immutable=True)
    sage: v.is_immutable()
    True
    sage: v = vector(QQ, w, immutable=True)
    sage: v.is_immutable()
    True

    sage: # needs numpy sage.symbolic
    sage: import numpy as np
    sage: w = np.array([1, 2, pi], float)
    sage: v = vector(w, immutable=True)
    sage: v.is_immutable()
    True
    sage: w = np.array([i, 2, 3], complex)
    sage: v = vector(w, immutable=True)
    sage: v.is_immutable()
    True

TESTS:

We check that :issue:`31470` is fixed::

    sage: k.<a> = GF(5^3)                                                           # needs sage.rings.finite_rings
    sage: S.<x> = k['x', k.frobenius_endomorphism()]                                # needs sage.rings.finite_rings
    sage: vector(S, 3)                                                              # needs sage.rings.finite_rings
    ...
    (0, 0, 0)

We check that ``sparse`` is respected for numpy arrays::

    sage: # needs numpy
    sage: import numpy
    sage: a = numpy.array([1,2,3], dtype=numpy.float64)
    sage: v = vector(a, sparse=True); v
    (1.0, 2.0, 3.0)
    sage: v.is_sparse()
    True
"""

zero_vector: _cython_3_2_1.cython_function_or_method

class FreeModuleElement(sage.structure.element.Vector):
    """FreeModuleElement(parent)

    File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 955)

    An element of a generic free module."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 959)

                EXAMPLES::

                    sage: v = sage.modules.free_module_element.FreeModuleElement(QQ^3)
                    sage: type(v)
                    <class 'sage.modules.free_module_element.FreeModuleElement'>
        """
    def Mod(self, p) -> Any:
        """FreeModuleElement.Mod(self, p)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2030)

        EXAMPLES::

            sage: V = vector(ZZ, [5, 9, 13, 15])
            sage: V.Mod(7)
            (5, 2, 6, 1)
            sage: parent(V.Mod(7))
            Vector space of dimension 4 over Ring of integers modulo 7"""
    @overload
    def additive_order(self) -> Any:
        """FreeModuleElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1659)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: v = vector(Integers(4), [1,2])
            sage: v.additive_order()
            4

        ::

            sage: v = vector([1,2,3])
            sage: v.additive_order()
            +Infinity

        ::

            sage: v = vector(Integers(30), [6, 15]); v
            (6, 15)
            sage: v.additive_order()
            10
            sage: 10*v
            (0, 0)"""
    @overload
    def additive_order(self) -> Any:
        """FreeModuleElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1659)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: v = vector(Integers(4), [1,2])
            sage: v.additive_order()
            4

        ::

            sage: v = vector([1,2,3])
            sage: v.additive_order()
            +Infinity

        ::

            sage: v = vector(Integers(30), [6, 15]); v
            (6, 15)
            sage: v.additive_order()
            10
            sage: 10*v
            (0, 0)"""
    @overload
    def additive_order(self) -> Any:
        """FreeModuleElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1659)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: v = vector(Integers(4), [1,2])
            sage: v.additive_order()
            4

        ::

            sage: v = vector([1,2,3])
            sage: v.additive_order()
            +Infinity

        ::

            sage: v = vector(Integers(30), [6, 15]); v
            (6, 15)
            sage: v.additive_order()
            10
            sage: 10*v
            (0, 0)"""
    @overload
    def additive_order(self) -> Any:
        """FreeModuleElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1659)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: v = vector(Integers(4), [1,2])
            sage: v.additive_order()
            4

        ::

            sage: v = vector([1,2,3])
            sage: v.additive_order()
            +Infinity

        ::

            sage: v = vector(Integers(30), [6, 15]); v
            (6, 15)
            sage: v.additive_order()
            10
            sage: 10*v
            (0, 0)"""
    @overload
    def apply_map(self, phi, R=..., sparse=...) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def apply_map(self, lambdax) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def apply_map(self, sin) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def apply_map(self, k) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def apply_map(self, f, k) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def apply_map(self, lambdax) -> Any:
        """FreeModuleElement.apply_map(self, phi, R=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3903)

        Apply the given map phi (an arbitrary Python function or callable
        object) to this free module element. If R is not given,
        automatically determine the base ring of the resulting element.

        INPUT:

        - ``sparse`` -- boolean; will control whether the result is sparse.
          By default, the result is sparse iff self is sparse.

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        OUTPUT: a free module element over R

        EXAMPLES::

            sage: m = vector([1,x,sin(x+1)])                                            # needs sage.symbolic
            sage: m.apply_map(lambda x: x^2)                                            # needs sage.symbolic
            (1, x^2, sin(x + 1)^2)
            sage: m.apply_map(sin)                                                      # needs sage.symbolic
            (sin(1), sin(x), sin(sin(x + 1)))

        ::

            sage: m = vector(ZZ, 9, range(9))
            sage: k.<a> = GF(9)                                                         # needs sage.rings.finite_rings
            sage: m.apply_map(k)                                                        # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)

        In this example, we explicitly specify the codomain.

        ::

            sage: s = GF(3)
            sage: f = lambda x: s(x)
            sage: n = m.apply_map(f, k); n                                              # needs sage.rings.finite_rings
            (0, 1, 2, 0, 1, 2, 0, 1, 2)
            sage: n.parent()                                                            # needs sage.rings.finite_rings
            Vector space of dimension 9 over Finite Field in a of size 3^2

        If your map sends 0 to a nonzero value, then your resulting
        vector is not mathematically sparse::

            sage: v = vector([0] * 6 + [1], sparse=True); v
            (0, 0, 0, 0, 0, 0, 1)
            sage: v2 = v.apply_map(lambda x: x+1); v2
            (1, 1, 1, 1, 1, 1, 2)

        but it's still represented with a sparse data type::

            sage: parent(v2)
            Ambient sparse free module of rank 7 over the principal ideal domain Integer Ring

        This data type is inefficient for dense vectors, so you may
        want to specify sparse=False::

            sage: v2 = v.apply_map(lambda x: x+1, sparse=False); v2
            (1, 1, 1, 1, 1, 1, 2)
            sage: parent(v2)
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        Or if you have a map that will result in mostly zeroes, you may
        want to specify sparse=True::

            sage: v = vector(srange(10))
            sage: v2 = v.apply_map(lambda x: 0 if x else 1, sparse=True); v2
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: parent(v2)
            Ambient sparse free module of rank 10 over the principal ideal domain Integer Ring

        TESTS::

            sage: m = vector(SR,[])                                                     # needs sage.symbolic
            sage: m.apply_map(lambda x: x*x) == m                                       # needs sage.symbolic
            True

        Check that we don't unnecessarily apply phi to 0 in the sparse case::

            sage: m = vector(ZZ, range(1, 4), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            (1, 1/2, 1/3)

            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=True).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=True))
            Sparse vector space of dimension 0 over Real Double Field
            sage: parent(vector(RDF, (), sparse=False).apply_map(lambda x: x, sparse=False))
            Vector space of dimension 0 over Real Double Field

        Check that the bug in :issue:`14558` has been fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(9)
            sage: v = vector([a, 0, 0, 0], sparse=True)
            sage: f = F.hom([a**3])
            sage: v.apply_map(f)
            (2*a + 1, 0, 0, 0)"""
    @overload
    def change_ring(self, R) -> Any:
        """FreeModuleElement.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1617)

        Change the base ring of this vector.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.change_ring(GF(3))
            (1, 2, 0, 1, 2)

        TESTS:

        Check for :issue:`29630`::

            sage: v = vector(QQ, 4, {0:1}, sparse=True)
            sage: v.change_ring(AA).is_sparse()                                         # needs sage.rings.number_field
            True"""
    @overload
    def change_ring(self, AA) -> Any:
        """FreeModuleElement.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1617)

        Change the base ring of this vector.

        EXAMPLES::

            sage: v = vector(QQ['x,y'], [1..5]); v.change_ring(GF(3))
            (1, 2, 0, 1, 2)

        TESTS:

        Check for :issue:`29630`::

            sage: v = vector(QQ, 4, {0:1}, sparse=True)
            sage: v.change_ring(AA).is_sparse()                                         # needs sage.rings.number_field
            True"""
    @overload
    def column(self) -> Any:
        """FreeModuleElement.column(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1504)

        Return a matrix with a single column and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single column.  The entries of the column are identical to those of the
        vector, and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.column(); w
            [1]
            [2]
            [3]
            sage: w.parent()
            Full MatrixSpace of 3 by 1 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.column()
            [2]
            [4]
            [8]
            [3]

        There is more than one way to get one-column matrix from a vector.
        The ``column`` method is about equally efficient to making a row and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.libs.pari sage.symbolic
            sage: x.column() == matrix(x).transpose()
            True
            sage: x.column() == x.row().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.column()
            sage: sm = s.column()                                                       # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.column` method will return
        a specified column of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1],[2],[3]])
            sage: A == A.column(0).column()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.column().column(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.column()
            sage: w.parent()
            Full MatrixSpace of 0 by 1 dense matrices over Integer Ring"""
    @overload
    def column(self) -> Any:
        """FreeModuleElement.column(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1504)

        Return a matrix with a single column and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single column.  The entries of the column are identical to those of the
        vector, and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.column(); w
            [1]
            [2]
            [3]
            sage: w.parent()
            Full MatrixSpace of 3 by 1 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.column()
            [2]
            [4]
            [8]
            [3]

        There is more than one way to get one-column matrix from a vector.
        The ``column`` method is about equally efficient to making a row and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.libs.pari sage.symbolic
            sage: x.column() == matrix(x).transpose()
            True
            sage: x.column() == x.row().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.column()
            sage: sm = s.column()                                                       # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.column` method will return
        a specified column of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1],[2],[3]])
            sage: A == A.column(0).column()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.column().column(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.column()
            sage: w.parent()
            Full MatrixSpace of 0 by 1 dense matrices over Integer Ring"""
    @overload
    def column(self) -> Any:
        """FreeModuleElement.column(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1504)

        Return a matrix with a single column and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single column.  The entries of the column are identical to those of the
        vector, and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.column(); w
            [1]
            [2]
            [3]
            sage: w.parent()
            Full MatrixSpace of 3 by 1 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.column()
            [2]
            [4]
            [8]
            [3]

        There is more than one way to get one-column matrix from a vector.
        The ``column`` method is about equally efficient to making a row and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.libs.pari sage.symbolic
            sage: x.column() == matrix(x).transpose()
            True
            sage: x.column() == x.row().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.column()
            sage: sm = s.column()                                                       # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.column` method will return
        a specified column of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1],[2],[3]])
            sage: A == A.column(0).column()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.column().column(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.column()
            sage: w.parent()
            Full MatrixSpace of 0 by 1 dense matrices over Integer Ring"""
    @overload
    def concatenate(self, other, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def concatenate(self, w2, ring=...) -> Any:
        """FreeModuleElement.concatenate(self, other, *, ring=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4193)

        Return the result of concatenating this vector with a sequence
        of elements given by another iterable.

        If the optional keyword argument ``ring`` is passed, this method
        will return a vector over the specified ring (or fail). If no
        base ring is given, the base ring is determined automatically by
        the :func:`vector` constructor.

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: w = vector([4, 5])
            sage: v.concatenate(w)
            (1, 2, 3, 4, 5)
            sage: v.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: w.parent()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: v.concatenate(w).parent()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring

        Forcing a base ring is possible using the ``ring`` argument::

            sage: v.concatenate(w, ring=QQ)
            (1, 2, 3, 4, 5)
            sage: v.concatenate(w, ring=QQ).parent()
            Vector space of dimension 5 over Rational Field

        ::

            sage: v.concatenate(w, ring=Zmod(3))
            (1, 2, 0, 1, 2)

        The method accepts arbitrary iterables of elements which can
        be coerced to a common base ring::

            sage: v.concatenate(range(4,8))
            (1, 2, 3, 4, 5, 6, 7)
            sage: v.concatenate(range(4,8)).parent()
            Ambient free module of rank 7 over the principal ideal domain Integer Ring

        ::

            sage: w2 = [4, QQbar(-5).sqrt()]
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field
            sage: w2 = vector(w2)
            sage: v.concatenate(w2)
            (1, 2, 3, 4, 2.236...*I)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 5 over Algebraic Field

        ::

            sage: w2 = polygen(QQ)^4 + 5
            sage: v.concatenate(w2)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2).parent()
            Vector space of dimension 8 over Rational Field
            sage: v.concatenate(w2, ring=ZZ)
            (1, 2, 3, 5, 0, 0, 0, 1)
            sage: v.concatenate(w2, ring=ZZ).parent()
            Ambient free module of rank 8 over the principal ideal domain Integer Ring

        ::

            sage: v.concatenate(GF(9).gens())
            (1, 2, 0, z2)
            sage: v.concatenate(GF(9).gens()).parent()
            Vector space of dimension 4 over Finite Field in z2 of size 3^2"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def conjugate(self) -> Any:
        """FreeModuleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3215)

        Return a vector where every entry has been replaced by its complex conjugate.

        OUTPUT:

        A vector of the same length, over the same ring,
        but with each entry replaced by the complex conjugate, as
        implemented by the ``conjugate()`` method for elements of
        the base ring, which is presently always complex conjugation.

        EXAMPLES::

            sage: v = vector(CDF, [2.3 - 5.4*I, -1.7 + 3.6*I])                          # needs sage.symbolic
            sage: w = v.conjugate(); w                                                  # needs sage.symbolic
            (2.3 + 5.4*I, -1.7 - 3.6*I)
            sage: w.parent()                                                            # needs sage.symbolic
            Vector space of dimension 2 over Complex Double Field

        Even if conjugation seems nonsensical over a certain ring, this
        method for vectors cooperates silently. ::

            sage: u = vector(ZZ, range(6))
            sage: u.conjugate()
            (0, 1, 2, 3, 4, 5)

        Sage implements a few specialized subfields of the complex numbers,
        such as the cyclotomic fields.  This example uses such a field
        containing a primitive 7-th root of unity named ``a``. ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = CyclotomicField(7)
            sage: v = vector(F, [a^i for i in range(7)])
            sage: v
            (1, a, a^2, a^3, a^4, a^5, -a^5 - a^4 - a^3 - a^2 - a - 1)
            sage: v.conjugate()
            (1, -a^5 - a^4 - a^3 - a^2 - a - 1, a^5, a^4, a^3, a^2, a)

        Sparse vectors are returned as such. ::

            sage: # needs sage.symbolic
            sage: v = vector(CC, {1: 5 - 6*I, 3: -7*I}); v
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)
            sage: v.is_sparse()
            True
            sage: vc = v.conjugate(); vc
            (0.000000000000000, 5.00000000000000 + 6.00000000000000*I, 0.000000000000000, 7.00000000000000*I)
            sage: vc.conjugate()
            (0.000000000000000, 5.00000000000000 - 6.00000000000000*I, 0.000000000000000, -7.00000000000000*I)

        TESTS::

            sage: n = 15
            sage: x = vector(CDF, [sin(i*pi/n)+cos(i*pi/n)*I for i in range(n)])        # needs sage.symbolic
            sage: x + x.conjugate() in RDF^n                                            # needs sage.symbolic
            True
            sage: I*(x - x.conjugate()) in RDF^n                                        # needs sage.symbolic
            True

        The parent of the conjugate is the same as that of the original vector.
        We test this by building a specialized vector space with a non-standard
        inner product, and constructing a test vector in this space. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: V = VectorSpace(CDF, 2, inner_product_matrix=[[2,1],[1,5]])
            sage: v = vector(CDF, [2-3*I, 4+5*I])
            sage: w = V(v)
            sage: w.parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]
            sage: w.conjugate().parent()
            Ambient quadratic space of dimension 2 over Complex Double Field
            Inner product matrix:
            [2.0 1.0]
            [1.0 5.0]"""
    @overload
    def coordinate_ring(self) -> Any:
        """FreeModuleElement.coordinate_ring(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1641)

        Return the ring from which the coefficients of this vector come.

        This is different from :meth:`base_ring`, which returns the ring
        of scalars.

        EXAMPLES::

            sage: M = (ZZ^2) * (1/2)
            sage: v = M([0,1/2])
            sage: v.base_ring()
            Integer Ring
            sage: v.coordinate_ring()
            Rational Field"""
    @overload
    def coordinate_ring(self) -> Any:
        """FreeModuleElement.coordinate_ring(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1641)

        Return the ring from which the coefficients of this vector come.

        This is different from :meth:`base_ring`, which returns the ring
        of scalars.

        EXAMPLES::

            sage: M = (ZZ^2) * (1/2)
            sage: v = M([0,1/2])
            sage: v.base_ring()
            Integer Ring
            sage: v.coordinate_ring()
            Rational Field"""
    @overload
    def cross_product(self, right) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, v) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, w) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, v) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, v, u) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, u, w) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, u) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, w, u) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    @overload
    def cross_product(self, v) -> Any:
        """FreeModuleElement.cross_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2702)

        Return the cross product of ``self`` and ``right``, which is only defined
        for vectors of length 3 or 7.

        INPUT:

        - ``right`` -- a vector of the same size as ``self``, either
          degree three or degree seven

        OUTPUT:

        The cross product (vector product) of ``self`` and ``right``,
        a vector of the same size of ``self`` and ``right``.

        This product is performed under the assumption that the basis
        vectors are orthonormal. See the method
        :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.cross_product`
        of vector fields for more general cases.

        EXAMPLES::

            sage: v = vector([1,2,3]); w = vector([0,5,-9])
            sage: v.cross_product(v)
            (0, 0, 0)
            sage: u = v.cross_product(w); u
            (-33, 9, 5)
            sage: u.dot_product(v)
            0
            sage: u.dot_product(w)
            0

        The cross product is defined for degree seven vectors as well:
        see :wikipedia:`Cross_product`.
        The 3-D cross product is achieved using the quaternions,
        whereas the 7-D cross product is achieved using the octonions. ::

            sage: u = vector(QQ, [1, -1/3, 57, -9, 56/4, -4,1])
            sage: v = vector(QQ, [37, 55, -99/57, 9, -12, 11/3, 4/98])
            sage: u.cross_product(v)
            (1394815/2793, -2808401/2793, 39492/49, -48737/399, -9151880/2793, 62513/2793, -326603/171)

        The degree seven cross product is anticommutative. ::

            sage: u.cross_product(v) + v.cross_product(u)
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product is distributive across addition. ::

            sage: v = vector([-12, -8/9, 42, 89, -37, 60/99, 73])
            sage: u = vector([31, -42/7, 97, 80, 30/55, -32, 64])
            sage: w = vector([-25/4, 40, -89, -91, -72/7, 79, 58])
            sage: v.cross_product(u + w) - (v.cross_product(u) + v.cross_product(w))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects scalar multiplication. ::

            sage: v = vector([2, 17, -11/5, 21, -6, 2/17, 16])
            sage: u = vector([-8, 9, -21, -6, -5/3, 12, 99])
            sage: (5*v).cross_product(u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: v.cross_product(5*u) - 5*(v.cross_product(u))
            (0, 0, 0, 0, 0, 0, 0)
            sage: (5*v).cross_product(u) - (v.cross_product(5*u))
            (0, 0, 0, 0, 0, 0, 0)

        The degree seven cross product respects the scalar triple product. ::

            sage: v = vector([2,6,-7/4,-9/12,-7,12,9])
            sage: u = vector([22,-7,-9/11,12,15,15/7,11])
            sage: w = vector([-11,17,19,-12/5,44,21/56,-8])
            sage: v.dot_product(u.cross_product(w)) - w.dot_product(v.cross_product(u))
            0

        TESTS:

        Both vectors need to be of length three or both vectors need to be of length seven. ::

            sage: u = vector(range(7))
            sage: v = vector(range(3))
            sage: u.cross_product(v)
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not (7 and 3)

        AUTHOR:

        Billy Wonderly (2010-05-11), Added 7-D Cross Product"""
    def cross_product_matrix(self) -> Any:
        """FreeModuleElement.cross_product_matrix(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2812)

        Return the matrix which describes a cross product
        between ``self`` and some other vector.

        This operation is sometimes written using the hat operator:
        see :wikipedia:`Hat_operator#Cross_product`.
        It is only defined for vectors of length 3 or 7.
        For a vector `v` the cross product matrix `\\hat{v}`
        is a matrix which satisfies `\\hat{v} \\cdot w = v \\times w`
        and also `w \\cdot \\hat{v} = w \\times v` for all vectors `w`.
        The basis vectors are assumed to be orthonormal.

        OUTPUT: the cross product matrix of this vector

        EXAMPLES::

            sage: v = vector([1, 2, 3])
            sage: vh = v.cross_product_matrix()
            sage: vh
            [ 0 -3  2]
            [ 3  0 -1]
            [-2  1  0]
            sage: w = random_vector(3, x=1, y=100)
            sage: vh*w == v.cross_product(w)
            True
            sage: w*vh == w.cross_product(v)
            True
            sage: vh.is_alternating()
            True

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(previous_prime(2^32))
            sage: v = random_vector(F, 3)
            sage: w = random_vector(F, 3)
            sage: vh = v.cross_product_matrix()
            sage: vh*w == v.cross_product(w)
            True
            sage: w*vh == w.cross_product(v)
            True
            sage: vh.is_alternating()
            True
            sage: v = random_vector(F, 7)
            sage: w = random_vector(F, 7)
            sage: vh = v.cross_product_matrix()
            sage: vh*w == v.cross_product(w)
            True
            sage: w*vh == w.cross_product(v)
            True
            sage: vh.is_alternating()
            True
            sage: random_vector(F, 5).cross_product_matrix()
            Traceback (most recent call last):
            ...
            TypeError: Cross product only defined for vectors of length three or seven, not 5"""
    @overload
    def curl(self, variables=...) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def curl(self) -> Any:
        """FreeModuleElement.curl(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3086)

        Return the curl of this two-dimensional or three-dimensional
        vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([-y, x, 0]).curl()
            (0, 0, 2)
            sage: vector([y, -x, x*y*z]).curl()
            (x*z, -y*z, -2)
            sage: vector([y^2, 0, 0]).curl()
            (0, 0, -2*y)
            sage: (R^3).random_element().curl().div()
            0

        For rings where the variable order is not well defined, it must be
        defined explicitly::

            sage: v = vector(SR, [-y, x, 0])                                            # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: v.curl([x, y, z])                                                     # needs sage.symbolic
            (0, 0, 2)

        Note that callable vectors have well defined variable orderings::

            sage: v(x, y, z) = (-y, x, 0)                                               # needs sage.symbolic
            sage: v.curl()                                                              # needs sage.symbolic
            (x, y, z) |--> (0, 0, 2)

        In two dimensions, this returns a scalar value::

            sage: R.<x,y> = QQ[]
            sage: vector([-y, x]).curl()
            2

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the curl
            in curvilinear coordinates."""
    @overload
    def degree(self) -> Any:
        """FreeModuleElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2246)

        Return the degree of this vector, which is simply the number
        of entries.

        EXAMPLES::

            sage: sage.modules.free_module_element.FreeModuleElement(QQ^389).degree()
            389
            sage: vector([1,2/3,8]).degree()
            3"""
    @overload
    def degree(self) -> Any:
        """FreeModuleElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2246)

        Return the degree of this vector, which is simply the number
        of entries.

        EXAMPLES::

            sage: sage.modules.free_module_element.FreeModuleElement(QQ^389).degree()
            389
            sage: vector([1,2/3,8]).degree()
            3"""
    @overload
    def degree(self) -> Any:
        """FreeModuleElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2246)

        Return the degree of this vector, which is simply the number
        of entries.

        EXAMPLES::

            sage: sage.modules.free_module_element.FreeModuleElement(QQ^389).degree()
            389
            sage: vector([1,2/3,8]).degree()
            3"""
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2260)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14])
            sage: v.denominator()
            70
            sage: 2*5*7
            70

        ::

            sage: M = (ZZ^2)*(1/2)
            sage: M.basis()[0].denominator()
            2

        TESTS:

        The following was fixed in :issue:`8800`::

            sage: M = GF(5)^3
            sage: v = M((4,0,2))
            sage: v.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2260)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14])
            sage: v.denominator()
            70
            sage: 2*5*7
            70

        ::

            sage: M = (ZZ^2)*(1/2)
            sage: M.basis()[0].denominator()
            2

        TESTS:

        The following was fixed in :issue:`8800`::

            sage: M = GF(5)^3
            sage: v = M((4,0,2))
            sage: v.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2260)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14])
            sage: v.denominator()
            70
            sage: 2*5*7
            70

        ::

            sage: M = (ZZ^2)*(1/2)
            sage: M.basis()[0].denominator()
            2

        TESTS:

        The following was fixed in :issue:`8800`::

            sage: M = GF(5)^3
            sage: v = M((4,0,2))
            sage: v.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2260)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14])
            sage: v.denominator()
            70
            sage: 2*5*7
            70

        ::

            sage: M = (ZZ^2)*(1/2)
            sage: M.basis()[0].denominator()
            2

        TESTS:

        The following was fixed in :issue:`8800`::

            sage: M = GF(5)^3
            sage: v = M((4,0,2))
            sage: v.denominator()
            1"""
    @overload
    def dense_vector(self) -> Any:
        """FreeModuleElement.dense_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3865)

        Return dense version of ``self``.  If ``self`` is dense, just return
        ``self``; otherwise, create and return correspond dense vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def dense_vector(self) -> Any:
        """FreeModuleElement.dense_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3865)

        Return dense version of ``self``.  If ``self`` is dense, just return
        ``self``; otherwise, create and return correspond dense vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def dense_vector(self) -> Any:
        """FreeModuleElement.dense_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3865)

        Return dense version of ``self``.  If ``self`` is dense, just return
        ``self``; otherwise, create and return correspond dense vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def dense_vector(self) -> Any:
        """FreeModuleElement.dense_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3865)

        Return dense version of ``self``.  If ``self`` is dense, just return
        ``self``; otherwise, create and return correspond dense vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector().is_dense()
            True
            sage: vector([-1,0,3,0,0,0],sparse=True).dense_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def derivative(self, *args) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def derivative(self) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def derivative(self, x) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def derivative(self, x) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def derivative(self, x) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def derivative(self, x) -> Any:
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def dict(self, copy=...) -> Any:
        """FreeModuleElement.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2299)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14])
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]

        In some cases, when ``copy=False``, we get back a dangerous
        reference::

            sage: v = vector({0:5, 2:3/7}, sparse=True)
            sage: v.dict(copy=False)
            {0: 5, 2: 3/7}
            sage: v.dict(copy=False)[0] = 18
            sage: v
            (18, 0, 3/7)"""
    @overload
    def dict(self) -> Any:
        """FreeModuleElement.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2299)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14])
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]

        In some cases, when ``copy=False``, we get back a dangerous
        reference::

            sage: v = vector({0:5, 2:3/7}, sparse=True)
            sage: v.dict(copy=False)
            {0: 5, 2: 3/7}
            sage: v.dict(copy=False)[0] = 18
            sage: v
            (18, 0, 3/7)"""
    @overload
    def dict(self, copy=...) -> Any:
        """FreeModuleElement.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2299)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14])
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]

        In some cases, when ``copy=False``, we get back a dangerous
        reference::

            sage: v = vector({0:5, 2:3/7}, sparse=True)
            sage: v.dict(copy=False)
            {0: 5, 2: 3/7}
            sage: v.dict(copy=False)[0] = 18
            sage: v
            (18, 0, 3/7)"""
    @overload
    def dict(self, copy=...) -> Any:
        """FreeModuleElement.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2299)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14])
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]

        In some cases, when ``copy=False``, we get back a dangerous
        reference::

            sage: v = vector({0:5, 2:3/7}, sparse=True)
            sage: v.dict(copy=False)
            {0: 5, 2: 3/7}
            sage: v.dict(copy=False)[0] = 18
            sage: v
            (18, 0, 3/7)"""
    def diff(self, *args, **kwargs):
        """FreeModuleElement.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4094)

        Derivative with respect to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global derivative() function for more
        details.

        :meth:`diff` is an alias of this function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,x,x^2])
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v = vector([1,x,x^2], sparse=True)
            sage: v.derivative(x)
            (0, 1, 2*x)
            sage: type(v.derivative(x)) == type(v)
            True
            sage: v.derivative(x,x)
            (0, 0, 2)"""
    @overload
    def div(self, variables=...) -> Any:
        """FreeModuleElement.div(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3046)

        Return the divergence of this vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([x, y, z]).div()
            3
            sage: vector([x*y, y*z, z*x]).div()
            x + y + z

            sage: R.<x,y,z,w> = QQ[]
            sage: vector([x*y, y*z, z*x]).div([x, y, z])
            x + y + z
            sage: vector([x*y, y*z, z*x]).div([z, x, y])
            0
            sage: vector([x*y, y*z, z*x]).div([x, y, w])
            y + z

            sage: vector(SR, [x*y, y*z, z*x]).div()                                     # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: vector(SR, [x*y, y*z, z*x]).div([x, y, z])                            # needs sage.symbolic
            x + y + z

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.divergence`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the
            divergence in curvilinear coordinates."""
    @overload
    def div(self) -> Any:
        """FreeModuleElement.div(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3046)

        Return the divergence of this vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([x, y, z]).div()
            3
            sage: vector([x*y, y*z, z*x]).div()
            x + y + z

            sage: R.<x,y,z,w> = QQ[]
            sage: vector([x*y, y*z, z*x]).div([x, y, z])
            x + y + z
            sage: vector([x*y, y*z, z*x]).div([z, x, y])
            0
            sage: vector([x*y, y*z, z*x]).div([x, y, w])
            y + z

            sage: vector(SR, [x*y, y*z, z*x]).div()                                     # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: vector(SR, [x*y, y*z, z*x]).div([x, y, z])                            # needs sage.symbolic
            x + y + z

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.divergence`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the
            divergence in curvilinear coordinates."""
    @overload
    def div(self) -> Any:
        """FreeModuleElement.div(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3046)

        Return the divergence of this vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([x, y, z]).div()
            3
            sage: vector([x*y, y*z, z*x]).div()
            x + y + z

            sage: R.<x,y,z,w> = QQ[]
            sage: vector([x*y, y*z, z*x]).div([x, y, z])
            x + y + z
            sage: vector([x*y, y*z, z*x]).div([z, x, y])
            0
            sage: vector([x*y, y*z, z*x]).div([x, y, w])
            y + z

            sage: vector(SR, [x*y, y*z, z*x]).div()                                     # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: vector(SR, [x*y, y*z, z*x]).div([x, y, z])                            # needs sage.symbolic
            x + y + z

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.divergence`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the
            divergence in curvilinear coordinates."""
    @overload
    def div(self) -> Any:
        """FreeModuleElement.div(self, variables=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3046)

        Return the divergence of this vector function.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: vector([x, y, z]).div()
            3
            sage: vector([x*y, y*z, z*x]).div()
            x + y + z

            sage: R.<x,y,z,w> = QQ[]
            sage: vector([x*y, y*z, z*x]).div([x, y, z])
            x + y + z
            sage: vector([x*y, y*z, z*x]).div([z, x, y])
            0
            sage: vector([x*y, y*z, z*x]).div([x, y, w])
            y + z

            sage: vector(SR, [x*y, y*z, z*x]).div()                                     # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Unable to determine ordered variable names for Symbolic Ring
            sage: vector(SR, [x*y, y*z, z*x]).div([x, y, z])                            # needs sage.symbolic
            x + y + z

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.divergence`
            of vector fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the
            divergence in curvilinear coordinates."""
    def dot_product(self, right) -> Any:
        """FreeModuleElement.dot_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2580)

        Return the dot product of ``self`` and ``right``, which is the
        sum of the product of the corresponding entries.

        INPUT:

        - ``right`` -- a vector of the same degree as ``self``.
          It does not need to belong to the same parent as ``self``,
          so long as the necessary products and sums are defined.

        OUTPUT:

        If ``self`` and ``right`` are the vectors `\\vec{x}` and `\\vec{y}`,
        of degree `n`, then this method returns

        .. MATH::

            \\sum_{i=1}^{n}x_iy_i

        .. NOTE::

            The :meth:`inner_product` is a more general version of
            this method, and the :meth:`hermitian_inner_product`
            method may be more appropriate if your vectors
            have complex entries.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.dot_product(w)
            32

        ::

            sage: R.<x> = QQ[]
            sage: v = vector([x,x^2,3*x]); w = vector([2*x,x,3+x])
            sage: v*w
            x^3 + 5*x^2 + 9*x
            sage: (x*2*x) + (x^2*x) + (3*x*(3+x))
            x^3 + 5*x^2 + 9*x
            sage: w*v
            x^3 + 5*x^2 + 9*x

        The vectors may be from different vector spaces,
        provided the necessary operations make sense.
        Notice that coercion will generate a result of
        the same type, even if the order of the
        arguments is reversed.::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = vector(FiniteField(3), [0,1,2])
            sage: ip = w.dot_product(v); ip
            2
            sage: ip.parent()
            Finite Field of size 3

            sage: ip = v.dot_product(w); ip
            2
            sage: ip.parent()
            Finite Field of size 3

        The dot product of a vector with itself is the 2-norm, squared. ::

            sage: v = vector(QQ, [3, 4, 7])
            sage: v.dot_product(v) - v.norm()^2                                         # needs sage.symbolic
            0

        TESTS:

        The second argument must be a free module element. ::

            sage: v = vector(QQ, [1,2])
            sage: v.dot_product('junk')
            Traceback (most recent call last):
            ...
            TypeError: Cannot convert str to sage.modules.free_module_element.FreeModuleElement

        The degrees of the arguments must match. ::

            sage: v = vector(QQ, [1,2])
            sage: w = vector(QQ, [1,2,3])
            sage: v.dot_product(w)
            Traceback (most recent call last):
            ...
            ArithmeticError: degrees (2 and 3) must be the same

        Check that vectors with different base rings play out nicely (:issue:`3103`)::

            sage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])
            8.0

        Zero-dimensional vectors work::

            sage: v = vector(ZZ, [])
            sage: v.dot_product(v)
            0

        TESTS:

        Check for :issue:`33814`::

            sage: rings = [ZZ, QQ, RDF, ZZ['x']]
            sage: rings += [RR]                                                         # needs sage.rings.real_mpfr
            sage: rings += [GF(2), GF(3)]
            sage: rings += [GF(4)]                                                      # needs sage.rings.finite_rings
            sage: for R in rings:
            ....:     _ = (R**0)().dot_product((R**0)())"""
    @overload
    def element(self) -> Any:
        """FreeModuleElement.element(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3155)

        Simply return ``self``.  This is useful, since for many objects,
        ``self.element()`` returns a vector corresponding to ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,0]); v
            (1/2, 2/5, 0)
            sage: v.element()
            (1/2, 2/5, 0)"""
    @overload
    def element(self) -> Any:
        """FreeModuleElement.element(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3155)

        Simply return ``self``.  This is useful, since for many objects,
        ``self.element()`` returns a vector corresponding to ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,0]); v
            (1/2, 2/5, 0)
            sage: v.element()
            (1/2, 2/5, 0)"""
    @overload
    def element(self) -> Any:
        """FreeModuleElement.element(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3155)

        Simply return ``self``.  This is useful, since for many objects,
        ``self.element()`` returns a vector corresponding to ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,0]); v
            (1/2, 2/5, 0)
            sage: v.element()
            (1/2, 2/5, 0)"""
    def get(self, i) -> Any:
        """FreeModuleElement.get(self, i)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1918)

        Like ``__getitem__`` but without bounds checking:
        `i` must satisfy ``0 <= i < self.degree``.

        EXAMPLES::

            sage: vector(SR, [1/2,2/5,0]).get(0)                                        # needs sage.symbolic
            1/2"""
    @overload
    def hamming_weight(self) -> int:
        """FreeModuleElement.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3815)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).hamming_weight()
            3"""
    @overload
    def hamming_weight(self) -> Any:
        """FreeModuleElement.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3815)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).hamming_weight()
            3"""
    def hermitian_inner_product(self, right) -> Any:
        """FreeModuleElement.hermitian_inner_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3527)

        Return the dot product, but with the entries of the first vector
        conjugated beforehand.

        INPUT:

        - ``right`` -- a vector of the same degree as ``self``

        OUTPUT:

        If ``self`` and ``right`` are the vectors `\\vec{x}` and
        `\\vec{y}` of degree `n` then this routine computes

        .. MATH::

            \\sum_{i=1}^{n}\\overline{x}_i{y}_i

        where the bar indicates complex conjugation.

        .. NOTE::

            If your vectors do not contain complex entries, then
            :meth:`dot_product` will return the same result without
            the overhead of conjugating elements of ``self``.

            If you are not computing a weighted inner product, and
            your vectors do not have complex entries, then the
            :meth:`dot_product` will return the same result.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector(CDF, [2+3*I, 5-4*I])
            sage: w = vector(CDF, [6-4*I, 2+3*I])
            sage: v.hermitian_inner_product(w)
            -2.0 - 3.0*I

        Sage implements a few specialized fields over the complex numbers,
        such as cyclotomic fields and quadratic number fields.  So long as
        the base rings have a conjugate method, then the Hermitian inner
        product will be available. ::

            sage: # needs sage.rings.number_field
            sage: Q.<a> = QuadraticField(-7)
            sage: a^2
            -7
            sage: v = vector(Q, [3+a, 5-2*a])
            sage: w = vector(Q, [6, 4+3*a])
            sage: v.hermitian_inner_product(w)
            17*a - 4

        The Hermitian inner product should be additive in
        each argument (we only need to test one), linear
        in each argument (with conjugation on the first scalar),
        and anti-commutative. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: alpha = CDF(5.0 + 3.0*I)
            sage: u = vector(CDF, [2+4*I, -3+5*I, 2-7*I])
            sage: v = vector(CDF, [-1+3*I, 5+4*I, 9-2*I])
            sage: w = vector(CDF, [8+3*I, -4+7*I, 3-6*I])
            sage: (u+v).hermitian_inner_product(w) == u.hermitian_inner_product(w) + v.hermitian_inner_product(w)
            True
            sage: (alpha*u).hermitian_inner_product(w) == alpha.conjugate()*u.hermitian_inner_product(w)
            True
            sage: u.hermitian_inner_product(alpha*w) == alpha*u.hermitian_inner_product(w)
            True
            sage: u.hermitian_inner_product(v) == v.hermitian_inner_product(u).conjugate()
            True

        For vectors with complex entries, the Hermitian inner product
        has a more natural relationship with the 2-norm (which is the
        default for the :meth:`norm` method). The norm squared equals
        the Hermitian inner product of the vector with itself.  ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: v = vector(CDF, [-0.66+0.47*I, -0.60+0.91*I, -0.62-0.87*I, 0.53+0.32*I])
            sage: abs(v.norm()^2 - v.hermitian_inner_product(v)) < 1.0e-10
            True

        TESTS:

        This method is built on the :meth:`dot_product` method,
        which allows for a wide variety of inputs.  Any error
        handling happens there. ::

            sage: # needs sage.rings.complex_double sage.symbolic
            sage: v = vector(CDF, [2+3*I])
            sage: w = vector(CDF, [5+2*I, 3+9*I])
            sage: v.hermitian_inner_product(w)
            Traceback (most recent call last):
            ...
            ArithmeticError: degrees (1 and 2) must be the same"""
    def inner_product(self, right) -> Any:
        """FreeModuleElement.inner_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3304)

        Return the inner product of ``self`` and ``right``,
        possibly using an inner product matrix from the parent of ``self``.

        INPUT:

        - ``right`` -- a vector of the same degree as ``self``

        OUTPUT:

        If the parent vector space does not have an inner product
        matrix defined, then this is the usual dot product
        (:meth:`dot_product`).  If ``self`` and ``right`` are
        considered as single column matrices, `\\vec{x}` and `\\vec{y}`,
        and `A` is the inner product matrix, then this method computes

        .. MATH::

            \\left(\\vec{x}\\right)^tA\\vec{y}

        where `t` indicates the transpose.

        .. NOTE::

            If your vectors have complex entries, the
            :meth:`hermitian_inner_product` may be more
            appropriate for your purposes.

        EXAMPLES::

            sage: v = vector(QQ, [1,2,3])
            sage: w = vector(QQ, [-1,2,-3])
            sage: v.inner_product(w)
            -6
            sage: v.inner_product(w) == v.dot_product(w)
            True

        The vector space or free module that is the parent to
        ``self`` can have an inner product matrix defined, which
        will be used by this method.  This matrix will be passed
        through to subspaces. ::

            sage: ipm = matrix(ZZ,[[2,0,-1], [0,2,0], [-1,0,6]])
            sage: M = FreeModule(ZZ, 3, inner_product_matrix=ipm)
            sage: v = M([1,0,0])
            sage: v.inner_product(v)
            2
            sage: K = M.span_of_basis([[0/2,-1/2,-1/2], [0,1/2,-1/2], [2,0,0]])
            sage: (K.0).inner_product(K.0)
            2
            sage: w = M([1,3,-1])
            sage: v = M([2,-4,5])
            sage: w.row()*ipm*v.column() == w.inner_product(v)
            True

        Note that the inner product matrix comes from the parent of ``self``.
        So if a vector is not an element of the correct parent, the result
        could be a source of confusion.  ::

            sage: V = VectorSpace(QQ, 2, inner_product_matrix=[[1,2],[2,1]])
            sage: v = V([12, -10])
            sage: w = vector(QQ, [10,12])
            sage: v.inner_product(w)
            88
            sage: w.inner_product(v)
            0
            sage: w = V(w)
            sage: w.inner_product(v)
            88

        .. NOTE::

            The use of an inner product matrix makes no restrictions on
            the nature of the matrix.  In particular, in this context it
            need not be Hermitian and positive-definite (as it is in the
            example above).

        TESTS:

        Most error handling occurs in the :meth:`dot_product` method.
        But with an inner product defined, this method will check
        that the input is a vector or free module element. ::

            sage: W = VectorSpace(RDF, 2, inner_product_matrix=matrix(RDF, 2, [1.0,2.0,3.0,4.0]))
            sage: v = W([2.0, 4.0])
            sage: v.inner_product(5)
            Traceback (most recent call last):
            ...
            TypeError: right must be a free module element"""
    @overload
    def integral(self, *args, **kwds) -> Any:
        """FreeModuleElement.integral(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4125)

        Return a symbolic integral of the vector, component-wise.

        :meth:`integrate` is an alias of the function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = var('t')
            sage: r = vector([t,t^2,sin(t)])
            sage: r.integral(t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: integrate(r, t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: r.integrate(t, 0, 1)
            (1/2, 1/3, -cos(1) + 1)"""
    @overload
    def integral(self, t) -> Any:
        """FreeModuleElement.integral(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4125)

        Return a symbolic integral of the vector, component-wise.

        :meth:`integrate` is an alias of the function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = var('t')
            sage: r = vector([t,t^2,sin(t)])
            sage: r.integral(t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: integrate(r, t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: r.integrate(t, 0, 1)
            (1/2, 1/3, -cos(1) + 1)"""
    def integrate(self, r, t) -> Any:
        """FreeModuleElement.integral(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4125)

        Return a symbolic integral of the vector, component-wise.

        :meth:`integrate` is an alias of the function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = var('t')
            sage: r = vector([t,t^2,sin(t)])
            sage: r.integral(t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: integrate(r, t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: r.integrate(t, 0, 1)
            (1/2, 1/3, -cos(1) + 1)"""
    @overload
    def is_dense(self) -> bool:
        """FreeModuleElement.is_dense(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3624)

        Return ``True`` if this is a dense vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_dense()
            True
            sage: vector([1/2, 2/5, 0], sparse=True).is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """FreeModuleElement.is_dense(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3624)

        Return ``True`` if this is a dense vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_dense()
            True
            sage: vector([1/2, 2/5, 0], sparse=True).is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """FreeModuleElement.is_dense(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3624)

        Return ``True`` if this is a dense vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_dense()
            True
            sage: vector([1/2, 2/5, 0], sparse=True).is_dense()
            False"""
    @overload
    def is_sparse(self) -> bool:
        """FreeModuleElement.is_sparse(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3642)

        Return ``True`` if this is a sparse vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_sparse()
            False
            sage: vector([1/2, 2/5, 0], sparse=True).is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """FreeModuleElement.is_sparse(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3642)

        Return ``True`` if this is a sparse vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_sparse()
            False
            sage: vector([1/2, 2/5, 0], sparse=True).is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """FreeModuleElement.is_sparse(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3642)

        Return ``True`` if this is a sparse vector, which is just a
        statement about the data structure, not the number of nonzero
        entries.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_sparse()
            False
            sage: vector([1/2, 2/5, 0], sparse=True).is_sparse()
            True"""
    @overload
    def is_vector(self) -> bool:
        """FreeModuleElement.is_vector(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3660)

        Return ``True``, since this is a vector.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_vector()
            True"""
    @overload
    def is_vector(self) -> Any:
        """FreeModuleElement.is_vector(self) -> bool

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3660)

        Return ``True``, since this is a vector.

        EXAMPLES::

            sage: vector([1/2, 2/5, 0]).is_vector()
            True"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1694)

        Return an iterator over ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi])                                                # needs sage.symbolic
            sage: v.items()                                                             # needs sage.symbolic
            <...generator object at ...>
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1694)

        Return an iterator over ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi])                                                # needs sage.symbolic
            sage: v.items()                                                             # needs sage.symbolic
            <...generator object at ...>
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1694)

        Return an iterator over ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi])                                                # needs sage.symbolic
            sage: v.items()                                                             # needs sage.symbolic
            <...generator object at ...>
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    def iteritems(self) -> Any:
        """FreeModuleElement.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1694)

        Return an iterator over ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi])                                                # needs sage.symbolic
            sage: v.items()                                                             # needs sage.symbolic
            <...generator object at ...>
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def lift(self) -> Any:
        """FreeModuleElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2090)

        Lift ``self`` to the cover ring.

        OUTPUT:

        Return a lift of ``self`` to the covering ring of the base ring `R`,
        which is by definition the ring returned by calling
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        on `R`, or just `R` itself if the
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        method is not defined.

        EXAMPLES::

            sage: V = vector(Integers(7), [5, 9, 13, 15]) ; V
            (5, 2, 6, 1)
            sage: V.lift()
            (5, 2, 6, 1)
            sage: parent(V.lift())
            Ambient free module of rank 4 over the principal ideal domain Integer Ring

        If the base ring does not have a cover method, return a copy of the vector::

            sage: W = vector(QQ, [1, 2, 3])
            sage: W1 = W.lift()
            sage: W is W1
            False
            sage: parent(W1)
            Vector space of dimension 3 over Rational Field"""
    @overload
    def lift(self) -> Any:
        """FreeModuleElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2090)

        Lift ``self`` to the cover ring.

        OUTPUT:

        Return a lift of ``self`` to the covering ring of the base ring `R`,
        which is by definition the ring returned by calling
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        on `R`, or just `R` itself if the
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        method is not defined.

        EXAMPLES::

            sage: V = vector(Integers(7), [5, 9, 13, 15]) ; V
            (5, 2, 6, 1)
            sage: V.lift()
            (5, 2, 6, 1)
            sage: parent(V.lift())
            Ambient free module of rank 4 over the principal ideal domain Integer Ring

        If the base ring does not have a cover method, return a copy of the vector::

            sage: W = vector(QQ, [1, 2, 3])
            sage: W1 = W.lift()
            sage: W is W1
            False
            sage: parent(W1)
            Vector space of dimension 3 over Rational Field"""
    @overload
    def lift(self) -> Any:
        """FreeModuleElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2090)

        Lift ``self`` to the cover ring.

        OUTPUT:

        Return a lift of ``self`` to the covering ring of the base ring `R`,
        which is by definition the ring returned by calling
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        on `R`, or just `R` itself if the
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        method is not defined.

        EXAMPLES::

            sage: V = vector(Integers(7), [5, 9, 13, 15]) ; V
            (5, 2, 6, 1)
            sage: V.lift()
            (5, 2, 6, 1)
            sage: parent(V.lift())
            Ambient free module of rank 4 over the principal ideal domain Integer Ring

        If the base ring does not have a cover method, return a copy of the vector::

            sage: W = vector(QQ, [1, 2, 3])
            sage: W1 = W.lift()
            sage: W is W1
            False
            sage: parent(W1)
            Vector space of dimension 3 over Rational Field"""
    @overload
    def lift(self) -> Any:
        """FreeModuleElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2090)

        Lift ``self`` to the cover ring.

        OUTPUT:

        Return a lift of ``self`` to the covering ring of the base ring `R`,
        which is by definition the ring returned by calling
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        on `R`, or just `R` itself if the
        :meth:`~sage.rings.quotient_ring.QuotientRing_nc.cover_ring`
        method is not defined.

        EXAMPLES::

            sage: V = vector(Integers(7), [5, 9, 13, 15]) ; V
            (5, 2, 6, 1)
            sage: V.lift()
            (5, 2, 6, 1)
            sage: parent(V.lift())
            Ambient free module of rank 4 over the principal ideal domain Integer Ring

        If the base ring does not have a cover method, return a copy of the vector::

            sage: W = vector(QQ, [1, 2, 3])
            sage: W1 = W.lift()
            sage: W is W1
            False
            sage: parent(W1)
            Vector space of dimension 3 over Rational Field"""
    def lift_centered(self) -> Any:
        """FreeModuleElement.lift_centered(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2127)

        Lift to a congruent, centered vector.

        INPUT:

        - ``self`` A vector with coefficients in `Integers(n)`.

        OUTPUT:

        - The unique integer vector `v` such that foreach `i`,
          `Mod(v[i],n) = Mod(self[i],n)` and `-n/2 < v[i] \\leq n/2`.

        EXAMPLES::

            sage: V = vector(Integers(7), [5, 9, 13, 15]) ; V
            (5, 2, 6, 1)
            sage: V.lift_centered()
            (-2, 2, -1, 1)
            sage: parent(V.lift_centered())
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def list(self, copy=...) -> Any:
        """FreeModuleElement.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2042)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); whether returned list is a
          copy that is safe to change (ignored)

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z], sparse=True)
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)

        The optional argument ``copy`` is ignored::

            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)"""
    @overload
    def list(self) -> Any:
        """FreeModuleElement.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2042)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); whether returned list is a
          copy that is safe to change (ignored)

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z], sparse=True)
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)

        The optional argument ``copy`` is ignored::

            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)"""
    @overload
    def list(self, copy=...) -> Any:
        """FreeModuleElement.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2042)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); whether returned list is a
          copy that is safe to change (ignored)

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z], sparse=True)
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)

        The optional argument ``copy`` is ignored::

            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)"""
    def list_from_positions(self, positions) -> Any:
        """FreeModuleElement.list_from_positions(self, positions)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2072)

        Return list of elements chosen from this vector using the
        given positions of this vector.

        INPUT:

        - ``positions`` -- iterable of integers

        EXAMPLES::

            sage: v = vector([1, 2/3, pi])                                              # needs sage.symbolic
            sage: v.list_from_positions([0,0,0,2,1])                                    # needs sage.symbolic
            [1, 1, 1, pi, 2/3]"""
    @overload
    def monic(self) -> Any:
        """FreeModuleElement.monic(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3169)

        Return this vector divided through by the first nonzero entry of
        this vector.

        EXAMPLES::

            sage: v = vector(QQ, [0, 4/3, 5, 1, 2])
            sage: v.monic()
            (0, 1, 15/4, 3/4, 3/2)
            sage: v = vector(QQ, [])
            sage: v.monic()
            ()"""
    @overload
    def monic(self) -> Any:
        """FreeModuleElement.monic(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3169)

        Return this vector divided through by the first nonzero entry of
        this vector.

        EXAMPLES::

            sage: v = vector(QQ, [0, 4/3, 5, 1, 2])
            sage: v.monic()
            (0, 1, 15/4, 3/4, 3/2)
            sage: v = vector(QQ, [])
            sage: v.monic()
            ()"""
    @overload
    def monic(self) -> Any:
        """FreeModuleElement.monic(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3169)

        Return this vector divided through by the first nonzero entry of
        this vector.

        EXAMPLES::

            sage: v = vector(QQ, [0, 4/3, 5, 1, 2])
            sage: v.monic()
            (0, 1, 15/4, 3/4, 3/2)
            sage: v = vector(QQ, [])
            sage: v.monic()
            ()"""
    @overload
    def monomial_coefficients(self, copy=...) -> Any:
        """FreeModuleElement.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 972)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: V = ZZ^3
            sage: v = V([1, 0, 5])
            sage: v.monomial_coefficients()
            {0: 1, 2: 5}

        Check that it works for submodules (:issue:`34455`)::

            sage: V = ZZ^3
            sage: U = V.submodule([[1, 2, 3], [1, 1, 1]])
            sage: U
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1  0 -1]
            [ 0  1  2]
            sage: u = U([2, 3, 4])
            sage: u.monomial_coefficients()
            {0: 2, 1: 3}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """FreeModuleElement.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 972)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: V = ZZ^3
            sage: v = V([1, 0, 5])
            sage: v.monomial_coefficients()
            {0: 1, 2: 5}

        Check that it works for submodules (:issue:`34455`)::

            sage: V = ZZ^3
            sage: U = V.submodule([[1, 2, 3], [1, 1, 1]])
            sage: U
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1  0 -1]
            [ 0  1  2]
            sage: u = U([2, 3, 4])
            sage: u.monomial_coefficients()
            {0: 2, 1: 3}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """FreeModuleElement.monomial_coefficients(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 972)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: V = ZZ^3
            sage: v = V([1, 0, 5])
            sage: v.monomial_coefficients()
            {0: 1, 2: 5}

        Check that it works for submodules (:issue:`34455`)::

            sage: V = ZZ^3
            sage: U = V.submodule([[1, 2, 3], [1, 1, 1]])
            sage: U
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1  0 -1]
            [ 0  1  2]
            sage: u = U([2, 3, 4])
            sage: u.monomial_coefficients()
            {0: 2, 1: 3}"""
    def nintegral(self, *args, **kwds) -> Any:
        """FreeModuleElement.nintegral(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4148)

        Return a numeric integral of the vector, component-wise, and
        the result of the nintegral command on each component of the
        input.

        :meth:`nintegrate` is an alias of the function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = var('t')
            sage: r = vector([t,t^2,sin(t)])
            sage: vec, answers = r.nintegral(t,0,1)
            sage: vec  # abs tol 1e-15
            (0.5, 0.3333333333333334, 0.4596976941318602)
            sage: type(vec)
            <class 'sage.modules.vector_real_double_dense.Vector_real_double_dense'>
            sage: answers
            [(0.5, 5.55111512312578...e-15, 21, 0),
             (0.3333333333333..., 3.70074341541719...e-15, 21, 0),
             (0.45969769413186..., 5.10366964392284...e-15, 21, 0)]

            sage: # needs sage.symbolic
            sage: r = vector([t,0,1], sparse=True)
            sage: r.nintegral(t, 0, 1)
            ((0.5, 0.0, 1.0),
             {0: (0.5, 5.55111512312578...e-15, 21, 0),
              2: (1.0, 1.11022302462515...e-14, 21, 0)})"""
    def nintegrate(self, *args, **kwargs):
        """FreeModuleElement.nintegral(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4148)

        Return a numeric integral of the vector, component-wise, and
        the result of the nintegral command on each component of the
        input.

        :meth:`nintegrate` is an alias of the function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = var('t')
            sage: r = vector([t,t^2,sin(t)])
            sage: vec, answers = r.nintegral(t,0,1)
            sage: vec  # abs tol 1e-15
            (0.5, 0.3333333333333334, 0.4596976941318602)
            sage: type(vec)
            <class 'sage.modules.vector_real_double_dense.Vector_real_double_dense'>
            sage: answers
            [(0.5, 5.55111512312578...e-15, 21, 0),
             (0.3333333333333..., 3.70074341541719...e-15, 21, 0),
             (0.45969769413186..., 5.10366964392284...e-15, 21, 0)]

            sage: # needs sage.symbolic
            sage: r = vector([t,0,1], sparse=True)
            sage: r.nintegral(t, 0, 1)
            ((0.5, 0.0, 1.0),
             {0: (0.5, 5.55111512312578...e-15, 21, 0),
              2: (1.0, 1.11022302462515...e-14, 21, 0)})"""
    @overload
    def nonzero_positions(self) -> Any:
        """FreeModuleElement.nonzero_positions(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3790)

        Return the sorted list of integers ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).nonzero_positions()
            [0, 2, 6]"""
    @overload
    def nonzero_positions(self) -> Any:
        """FreeModuleElement.nonzero_positions(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3790)

        Return the sorted list of integers ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).nonzero_positions()
            [0, 2, 6]"""
    @overload
    def norm(self, p=...) -> Any:
        """FreeModuleElement.norm(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1732)

        Return the `p`-norm of ``self``.

        INPUT:

        - ``p`` -- (default: 2) ``p`` can be a real number greater than 1,
          infinity (``oo`` or ``Infinity``), or a symbolic expression:

          - `p=1`: the taxicab (Manhattan) norm
          - `p=2`: the usual Euclidean norm (the default)
          - `p=\\infty`: the maximum entry (in absolute value)

        .. NOTE::

            See also :func:`sage.misc.functional.norm`

        EXAMPLES::

            sage: v = vector([1,2,-3])
            sage: v.norm(5)                                                             # needs sage.symbolic
            276^(1/5)

        The default is the usual Euclidean norm.  ::

            sage: v.norm()                                                              # needs sage.symbolic
            sqrt(14)
            sage: v.norm(2)                                                             # needs sage.symbolic
            sqrt(14)

        The infinity norm is the maximum size (in absolute value)
        of the entries.  ::

            sage: v.norm(Infinity)
            3
            sage: v.norm(oo)
            3

        Real or symbolic values may be used for ``p``.  ::

            sage: v=vector(RDF,[1,2,3])
            sage: v.norm(5)
            3.077384885394063

            sage: # needs sage.symbolic
            sage: v.norm(pi/2)    # abs tol 1e-15
            4.216595864704748
            sage: _ = var('a b c d p'); v = vector([a, b, c, d])
            sage: v.norm(p)
            (abs(a)^p + abs(b)^p + abs(c)^p + abs(d)^p)^(1/p)

        Notice that the result may be a symbolic expression, owing to
        the necessity of taking a square root (in the default case).
        These results can be converted to numerical values if needed. ::

            sage: v = vector(ZZ, [3,4])
            sage: nrm = v.norm(); nrm
            5
            sage: nrm.parent()
            Rational Field

            sage: # needs sage.symbolic
            sage: v = vector(QQ, [3, 5])
            sage: nrm = v.norm(); nrm
            sqrt(34)
            sage: nrm.parent()
            Symbolic Ring
            sage: numeric = N(nrm); numeric
            5.83095189484...
            sage: numeric.parent()
            Real Field with 53 bits of precision

        TESTS:

        The value of ``p`` must be greater than, or
        equal to, one. ::

            sage: v = vector(QQ, [1,2])
            sage: v.norm(0.99)
            Traceback (most recent call last):
            ...
            ValueError: 0.990000000000000 is not greater than or equal to 1

        Norm works with Python integers (see :issue:`13502`). ::

            sage: v = vector(QQ, [1,2])
            sage: v.norm(int(2))                                                        # needs sage.symbolic
            sqrt(5)"""
    @overload
    def norm(self, thedefault) -> Any:
        """FreeModuleElement.norm(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1732)

        Return the `p`-norm of ``self``.

        INPUT:

        - ``p`` -- (default: 2) ``p`` can be a real number greater than 1,
          infinity (``oo`` or ``Infinity``), or a symbolic expression:

          - `p=1`: the taxicab (Manhattan) norm
          - `p=2`: the usual Euclidean norm (the default)
          - `p=\\infty`: the maximum entry (in absolute value)

        .. NOTE::

            See also :func:`sage.misc.functional.norm`

        EXAMPLES::

            sage: v = vector([1,2,-3])
            sage: v.norm(5)                                                             # needs sage.symbolic
            276^(1/5)

        The default is the usual Euclidean norm.  ::

            sage: v.norm()                                                              # needs sage.symbolic
            sqrt(14)
            sage: v.norm(2)                                                             # needs sage.symbolic
            sqrt(14)

        The infinity norm is the maximum size (in absolute value)
        of the entries.  ::

            sage: v.norm(Infinity)
            3
            sage: v.norm(oo)
            3

        Real or symbolic values may be used for ``p``.  ::

            sage: v=vector(RDF,[1,2,3])
            sage: v.norm(5)
            3.077384885394063

            sage: # needs sage.symbolic
            sage: v.norm(pi/2)    # abs tol 1e-15
            4.216595864704748
            sage: _ = var('a b c d p'); v = vector([a, b, c, d])
            sage: v.norm(p)
            (abs(a)^p + abs(b)^p + abs(c)^p + abs(d)^p)^(1/p)

        Notice that the result may be a symbolic expression, owing to
        the necessity of taking a square root (in the default case).
        These results can be converted to numerical values if needed. ::

            sage: v = vector(ZZ, [3,4])
            sage: nrm = v.norm(); nrm
            5
            sage: nrm.parent()
            Rational Field

            sage: # needs sage.symbolic
            sage: v = vector(QQ, [3, 5])
            sage: nrm = v.norm(); nrm
            sqrt(34)
            sage: nrm.parent()
            Symbolic Ring
            sage: numeric = N(nrm); numeric
            5.83095189484...
            sage: numeric.parent()
            Real Field with 53 bits of precision

        TESTS:

        The value of ``p`` must be greater than, or
        equal to, one. ::

            sage: v = vector(QQ, [1,2])
            sage: v.norm(0.99)
            Traceback (most recent call last):
            ...
            ValueError: 0.990000000000000 is not greater than or equal to 1

        Norm works with Python integers (see :issue:`13502`). ::

            sage: v = vector(QQ, [1,2])
            sage: v.norm(int(2))                                                        # needs sage.symbolic
            sqrt(5)"""
    @overload
    def normalized(self, p=...) -> Any:
        """FreeModuleElement.normalized(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3189)

        Return the input vector divided by the p-norm.

        INPUT:

        - ``p`` -- (default: 2) p value for the norm

        EXAMPLES::

            sage: v = vector(QQ, [4, 1, 3, 2])
            sage: v.normalized()                                                        # needs sage.symbolic
            (2/15*sqrt(30), 1/30*sqrt(30), 1/10*sqrt(30), 1/15*sqrt(30))
            sage: sum(v.normalized(1))
            1

        Note that normalizing the vector may change the base ring::

            sage: v.base_ring() == v.normalized().base_ring()                           # needs sage.symbolic
            False
            sage: u = vector(RDF, [-3, 4, 6, 9])
            sage: u.base_ring() == u.normalized().base_ring()
            True"""
    @overload
    def normalized(self) -> Any:
        """FreeModuleElement.normalized(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3189)

        Return the input vector divided by the p-norm.

        INPUT:

        - ``p`` -- (default: 2) p value for the norm

        EXAMPLES::

            sage: v = vector(QQ, [4, 1, 3, 2])
            sage: v.normalized()                                                        # needs sage.symbolic
            (2/15*sqrt(30), 1/30*sqrt(30), 1/10*sqrt(30), 1/15*sqrt(30))
            sage: sum(v.normalized(1))
            1

        Note that normalizing the vector may change the base ring::

            sage: v.base_ring() == v.normalized().base_ring()                           # needs sage.symbolic
            False
            sage: u = vector(RDF, [-3, 4, 6, 9])
            sage: u.base_ring() == u.normalized().base_ring()
            True"""
    @overload
    def normalized(self) -> Any:
        """FreeModuleElement.normalized(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3189)

        Return the input vector divided by the p-norm.

        INPUT:

        - ``p`` -- (default: 2) p value for the norm

        EXAMPLES::

            sage: v = vector(QQ, [4, 1, 3, 2])
            sage: v.normalized()                                                        # needs sage.symbolic
            (2/15*sqrt(30), 1/30*sqrt(30), 1/10*sqrt(30), 1/15*sqrt(30))
            sage: sum(v.normalized(1))
            1

        Note that normalizing the vector may change the base ring::

            sage: v.base_ring() == v.normalized().base_ring()                           # needs sage.symbolic
            False
            sage: u = vector(RDF, [-3, 4, 6, 9])
            sage: u.base_ring() == u.normalized().base_ring()
            True"""
    @overload
    def normalized(self) -> Any:
        """FreeModuleElement.normalized(self, p=__two__)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3189)

        Return the input vector divided by the p-norm.

        INPUT:

        - ``p`` -- (default: 2) p value for the norm

        EXAMPLES::

            sage: v = vector(QQ, [4, 1, 3, 2])
            sage: v.normalized()                                                        # needs sage.symbolic
            (2/15*sqrt(30), 1/30*sqrt(30), 1/10*sqrt(30), 1/15*sqrt(30))
            sage: sum(v.normalized(1))
            1

        Note that normalizing the vector may change the base ring::

            sage: v.base_ring() == v.normalized().base_ring()                           # needs sage.symbolic
            False
            sage: u = vector(RDF, [-3, 4, 6, 9])
            sage: u.base_ring() == u.normalized().base_ring()
            True"""
    @overload
    def numerical_approx(self, prec=..., digits=..., algorithm=...) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numerical_approx(self, v) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numerical_approx(self, v, digits=...) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numerical_approx(self) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numerical_approx(self, u) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numerical_approx(self, digits=...) -> Any:
        """FreeModuleElement.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1299)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(212), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: numerical_approx(v)
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision
            sage: numerical_approx(v, digits=3)
            (1.00, 2.00, 3.00)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 14 bits of precision

        Both functional and object-oriented usage is possible.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: u.n()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: u.numerical_approx()
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: n(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: N(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)
            sage: numerical_approx(u)
            (0.500000000000000, 0.333333333333333, 0.250000000000000)

        Precision (bits) and digits (decimal) may be specified.
        When both are given, ``prec`` wins.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4])
            sage: n(u, prec=15)
            (0.5000, 0.3333, 0.2500)
            sage: n(u, digits=5)
            (0.50000, 0.33333, 0.25000)
            sage: n(u, prec=30, digits=100)
            (0.50000000, 0.33333333, 0.25000000)

        These are some legacy doctests that were part of various specialized
        versions of the numerical approximation routine that were removed as
        part of :issue:`12195`.  ::

            sage: v = vector(ZZ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(RDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v = vector(CDF, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Complex Field with 53 bits of precision

            sage: v = vector(Integers(8), [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

            sage: v = vector(QQ, [1,2,3])
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        ::

            sage: v = vector(GF(2), [1,2,3])
            sage: v.n()
            (1.00000000000000, 0.000000000000000, 1.00000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 0.0000000000000000000000, 1.000000000000000000000)
            sage: _.parent()
            Vector space of dimension 3 over Real Field with 75 bits of precision

        TESTS:

        Sparse vectors have a similar method that works efficiently for
        the sparse case.  We test that it is working as it should.  ::

            sage: v = vector(QQ, [1/2, 0, 0, 1/3, 0, 0, 0, 1/4], sparse=True)
            sage: u = v.numerical_approx(digits=4)
            sage: u.is_sparse()
            True
            sage: u
            (0.5000, 0.0000, 0.0000, 0.3333, 0.0000, 0.0000, 0.0000, 0.2500)"""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    @overload
    def numpy(self, dtype=...) -> Any:
        """FreeModuleElement.numpy(self, dtype=object)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1135)

        Convert ``self`` to a numpy array.

        INPUT:

        - ``dtype`` -- the `numpy dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_
          of the returned array

        EXAMPLES::

            sage: # needs numpy
            sage: v = vector([1,2,3])
            sage: v.numpy()
            array([1, 2, 3], dtype=object)
            sage: v.numpy() * v.numpy()
            array([1, 4, 9], dtype=object)

            sage: vector(QQ, [1, 2, 5/6]).numpy()                                       # needs numpy
            array([1, 2, 5/6], dtype=object)

        By default, the ``object`` `dtype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ is used.
        Alternatively, the desired dtype can be passed in as a parameter::

            sage: # needs numpy
            sage: v = vector(QQ, [1, 2, 5/6])
            sage: v.numpy()
            array([1, 2, 5/6], dtype=object)
            sage: v.numpy(dtype=float)
            array([1.        , 2.        , 0.83333333])
            sage: v.numpy(dtype=int)
            array([1, 2, 0])
            sage: import numpy
            sage: v.numpy(dtype=numpy.uint8)
            array([1, 2, 0], dtype=uint8)

        Passing a dtype of None will let numpy choose a native type, which can
        be more efficient but may have unintended consequences::

            sage: # needs numpy
            sage: v.numpy(dtype=None)
            array([1.        , 2.        , 0.83333333])

            sage: w = vector(ZZ, [0, 1, 2^63 -1]); w
            (0, 1, 9223372036854775807)
            sage: wn = w.numpy(dtype=None); wn                                          # needs numpy
            array([                  0,                   1, 9223372036854775807]...)
            sage: wn.dtype                                                              # needs numpy
            dtype('int64')
            sage: w.dot_product(w)
            85070591730234615847396907784232501250
            sage: wn.dot(wn)        # overflow                                          # needs numpy
            2

        Numpy can give rather obscure errors; we wrap these to give a bit of context::

            sage: vector([1, 1/2, QQ['x'].0]).numpy(dtype=float)                        # needs numpy
            Traceback (most recent call last):
            ...
            ValueError: Could not convert vector over Univariate Polynomial Ring in x
            over Rational Field to numpy array of type <... 'float'>:
            setting an array element with a sequence."""
    def outer_product(self, right) -> Any:
        '''FreeModuleElement.outer_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3409)

        Return a matrix, the outer product of two vectors ``self`` and ``right``.

        INPUT:

        - ``right`` -- a vector (or free module element) of any size, whose
          elements are compatible (with regard to multiplication) with the
          elements of ``self``.

        OUTPUT:

        The outer product of two vectors `x` and `y` (respectively
        ``self`` and ``right``) can be described several ways.  If we
        interpret `x` as a `m\\times 1` matrix and interpret `y` as a
        `1\\times n` matrix, then the outer product is the `m\\times n`
        matrix from the usual matrix product `xy`.  Notice how this
        is the "opposite" in some ways from an inner product (which
        would require `m=n`).

        If we just consider vectors, use each entry of `x` to create
        a scalar multiples of the vector `y` and use these vectors as
        the rows of a matrix.  Or use each entry of `y` to create a
        scalar multiples of `x` and use these vectors as the columns
        of a matrix.

        EXAMPLES::

            sage: u = vector(QQ, [1/2, 1/3, 1/4, 1/5])
            sage: v = vector(ZZ, [60, 180, 600])
            sage: u.outer_product(v)
            [ 30  90 300]
            [ 20  60 200]
            [ 15  45 150]
            [ 12  36 120]
            sage: M = v.outer_product(u); M
            [ 30  20  15  12]
            [ 90  60  45  36]
            [300 200 150 120]
            sage: M.parent()
            Full MatrixSpace of 3 by 4 dense matrices over Rational Field

        The more general :meth:`sage.matrix.matrix2.tensor_product` is an
        operation on a pair of matrices.  If we construct a pair of vectors
        as a column vector and a row vector, then an outer product and a
        tensor product are identical.  Thus ``tensor_product`` is a synonym
        for this method.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4, 1/5])
            sage: v = vector(ZZ, [60, 180, 600])
            sage: u.tensor_product(v) == (u.column()).tensor_product(v.row())
            True

        The result is always a dense matrix, no matter if the two
        vectors are, or are not, dense.  ::

            sage: d = vector(ZZ,[4,5], sparse=False)
            sage: s = vector(ZZ, [1,2,3], sparse=True)
            sage: dd = d.outer_product(d)
            sage: ds = d.outer_product(s)
            sage: sd = s.outer_product(d)
            sage: ss = s.outer_product(s)
            sage: all([dd.is_dense(), ds.is_dense(), sd.is_dense(), dd.is_dense()])
            True

        Vectors with no entries do the right thing.  ::

            sage: v = vector(ZZ, [])
            sage: z = v.outer_product(v)
            sage: z.parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring

        There is a fair amount of latitude in the value of the ``right``
        vector, and the matrix that results can have entries from a new
        ring large enough to contain the result. If you know better,
        you can sometimes bring the result down to a less general ring.  ::

            sage: R.<t> = ZZ[]
            sage: v = vector(R, [12, 24*t])
            sage: w = vector(QQ, [1/2, 1/3, 1/4])
            sage: op = v.outer_product(w); op
            [   6    4    3]
            [12*t  8*t  6*t]
            sage: op.base_ring()
            Univariate Polynomial Ring in t over Rational Field
            sage: m = op.change_ring(R); m
            [   6    4    3]
            [12*t  8*t  6*t]
            sage: m.base_ring()
            Univariate Polynomial Ring in t over Integer Ring

        But some inputs are not compatible, even if vectors. ::

            sage: w = vector(GF(5), [1,2])
            sage: v = vector(GF(7), [1,2,3,4])
            sage: z = w.outer_product(v)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            \'Full MatrixSpace of 2 by 1 dense matrices over Finite Field of size 5\' and
            \'Full MatrixSpace of 1 by 4 dense matrices over Finite Field of size 7\'

        And some inputs don\'t make any sense at all. ::

            sage: w = vector(QQ, [5,10])
            sage: z = w.outer_product(6)
            Traceback (most recent call last):
            ...
            TypeError: right operand in an outer product must be a vector,
            not an element of Integer Ring'''
    @overload
    def pairwise_product(self, right) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, w) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, w) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, v) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, v) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, w) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, w) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    @overload
    def pairwise_product(self, v, w) -> Any:
        """FreeModuleElement.pairwise_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2895)

        Return the pairwise product of ``self`` and ``right``, which is a vector of
        the products of the corresponding entries.

        INPUT:

        - ``right`` -- vector of the same degree as ``self``. It
          need not be in the same vector space as ``self``, as long as the
          coefficients can be multiplied.

        EXAMPLES::

            sage: V = FreeModule(ZZ, 3)
            sage: v = V([1,2,3])
            sage: w = V([4,5,6])
            sage: v.pairwise_product(w)
            (4, 10, 18)
            sage: sum(v.pairwise_product(w)) == v.dot_product(w)
            True

        ::

            sage: W = VectorSpace(GF(3), 3)
            sage: w = W([0,1,2])
            sage: w.pairwise_product(v)
            (0, 2, 0)
            sage: w.pairwise_product(v).parent()
            Vector space of dimension 3 over Finite Field of size 3

        Implicit coercion is well defined (regardless of order), so we
        get 2 even if we do the dot product in the other order.

        ::

            sage: v.pairwise_product(w).parent()
            Vector space of dimension 3 over Finite Field of size 3

        TESTS::

        ::

            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: parent(vector(ZZ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(ZZ,[1,2])))
            Vector space of dimension 2 over Rational Field
            sage: parent(vector(QQ,[1,2]).pairwise_product(vector(QQ,[1,2])))
            Vector space of dimension 2 over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ,[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ,[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['x'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(QQ['y'],[1,2,3,4]).pairwise_product(vector(ZZ['x']['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
            sage: parent(vector(ZZ['x']['y'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Ambient free module of rank 4 over the integral domain
             Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field

        ::

            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(ZZ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in x over Integer Ring' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(ZZ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the integral domain Univariate Polynomial Ring in y over Integer Ring'
            sage: parent(vector(QQ['x'],[1,2,3,4]).pairwise_product(vector(QQ['y'],[1,2,3,4])))
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field' and
            'Ambient free module of rank 4 over the principal ideal domain Univariate Polynomial Ring in y over Rational Field'
            sage: v = vector({1: 1, 3: 2})  # test sparse vectors
            sage: w = vector({0: 6, 3: -4})
            sage: v.pairwise_product(w)
            (0, 0, 0, -8)
            sage: w.pairwise_product(v) == v.pairwise_product(w)
            True"""
    def plot(self, *args, **kwargs):
        """FreeModuleElement.plot(self, plot_type=None, start=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2345)

        INPUT:

        - ``plot_type`` -- (default: 'arrow' if v has 3 or fewer components,
            otherwise 'step') type of plot. Options are:

            - 'arrow' to draw an arrow

            - 'point' to draw a point at the coordinates specified by the
              vector

            - 'step' to draw a step function representing the coordinates
              of the vector.

          Both 'arrow' and 'point' raise exceptions if the vector has
          more than 3 dimensions.

        - ``start`` -- (default: origin in correct dimension) may be a tuple,
          list, or vector

        EXAMPLES:

        The following both plot the given vector::

            sage: v = vector(RDF, (1,2))
            sage: A = plot(v)                                                           # needs sage.plot
            sage: B = v.plot()                                                          # needs sage.plot
            sage: A + B  # should just show one vector                                  # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        Examples of the plot types::

            sage: # needs sage.plot
            sage: A = plot(v, plot_type='arrow')
            sage: B = plot(v, plot_type='point', color='green', size=20)
            sage: C = plot(v, plot_type='step') # calls v.plot_step()
            sage: A+B+C
            Graphics object consisting of 3 graphics primitives

        You can use the optional arguments for :meth:`plot_step`::

            sage: eps = 0.1
            sage: plot(v, plot_type='step', eps=eps, xmax=5, hue=0)                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Three-dimensional examples::

            sage: v = vector(RDF, (1,2,1))
            sage: plot(v)  # defaults to an arrow plot                                  # needs sage.plot
            Graphics3d Object

        ::

            sage: plot(v, plot_type='arrow')                                            # needs sage.plot
            Graphics3d Object

        ::

            sage: from sage.plot.plot3d.shapes2 import frame3d                          # needs sage.plot
            sage: plot(v, plot_type='point')+frame3d((0,0,0), v.list())                 # needs sage.plot
            Graphics3d Object

        ::

            sage: plot(v, plot_type='step')  # calls v.plot_step()                      # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        ::

            sage: plot(v, plot_type='step', eps=eps, xmax=5, hue=0)                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        With greater than three coordinates, it defaults to a step plot::

            sage: v = vector(RDF, (1,2,3,4))
            sage: plot(v)                                                               # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        One dimensional vectors are plotted along the horizontal axis of
        the coordinate plane::

            sage: plot(vector([1]))                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        An optional start argument may also be specified by a tuple, list, or vector::

            sage: u = vector([1,2]); v = vector([2,5])
            sage: plot(u, start=v)                                                      # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        TESTS::

            sage: u = vector([1,1]); v = vector([2,2,2]); z=(3,3,3)
            sage: plot(u)  #test when start=None                                        # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        ::

            sage: # needs sage.plot
            sage: plot(u, start=v) #test when coordinate dimension mismatch exists
            Traceback (most recent call last):
            ...
            ValueError: vector coordinates are not of the same dimension
            sage: P = plot(v, start=z)        # test when start coordinates are passed as a tuple
            sage: P = plot(v, start=list(z))  # test when start coordinates are passed as a list"""
    def plot_step(self, xmin=..., xmax=..., eps=..., res=..., connect=..., **kwds) -> Any:
        """FreeModuleElement.plot_step(self, xmin=0, xmax=1, eps=None, res=None, connect=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2496)

        INPUT:

        - ``xmin`` -- (default: 0) start x position to start
          plotting

        - ``xmax`` -- (default: 1) stop x position to stop
          plotting

        - ``eps`` -- (default: determined by xmax) we view this
          vector as defining a function at the points xmin, xmin + eps, xmin
          + 2\\*eps, ...,

        - ``res`` -- (default: all points) total number of
          points to include in the graph

        - ``connect`` -- boolean (default: ``True``); if ``True`` draws a line,
          otherwise draw a list of points

        EXAMPLES::

            sage: eps = 0.1
            sage: v = vector(RDF, [sin(n*eps) for n in range(100)])
            sage: v.plot_step(eps=eps, xmax=5, hue=0)                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def row(self) -> Any:
        """FreeModuleElement.row(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1437)

        Return a matrix with a single row and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single row.  The entries of the row are identical to those of the vector,
        and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.row(); w
            [1 2 3]
            sage: w.parent()
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.row()
            [2 4 8 3]

        There is more than one way to get one-row matrix from a vector,
        but the ``row`` method is more efficient than making a column and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.symbolic
            sage: x.row() == matrix(x)
            True
            sage: x.row() == x.column().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.row()
            sage: sm = s.row()                                                          # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.row` method will return
        a specified row of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1,2,3]])
            sage: A == A.row(0).row()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.row().row(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.row()
            sage: w.parent()
            Full MatrixSpace of 1 by 0 dense matrices over Integer Ring"""
    @overload
    def row(self) -> Any:
        """FreeModuleElement.row(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1437)

        Return a matrix with a single row and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single row.  The entries of the row are identical to those of the vector,
        and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.row(); w
            [1 2 3]
            sage: w.parent()
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.row()
            [2 4 8 3]

        There is more than one way to get one-row matrix from a vector,
        but the ``row`` method is more efficient than making a column and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.symbolic
            sage: x.row() == matrix(x)
            True
            sage: x.row() == x.column().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.row()
            sage: sm = s.row()                                                          # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.row` method will return
        a specified row of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1,2,3]])
            sage: A == A.row(0).row()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.row().row(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.row()
            sage: w.parent()
            Full MatrixSpace of 1 by 0 dense matrices over Integer Ring"""
    @overload
    def row(self) -> Any:
        """FreeModuleElement.row(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1437)

        Return a matrix with a single row and the same entries as the vector ``self``.

        OUTPUT:

        A matrix over the same ring as the vector (or free module element), with
        a single row.  The entries of the row are identical to those of the vector,
        and in the same order.

        EXAMPLES::

            sage: v = vector(ZZ, [1,2,3])
            sage: w = v.row(); w
            [1 2 3]
            sage: w.parent()
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring

            sage: x = vector(FiniteField(13), [2,4,8,16])
            sage: x.row()
            [2 4 8 3]

        There is more than one way to get one-row matrix from a vector,
        but the ``row`` method is more efficient than making a column and
        then taking a transpose.  Notice that supplying a vector to the
        matrix constructor demonstrates Sage's preference for rows. ::

            sage: x = vector(RDF, [sin(i*pi/20) for i in range(10)])                    # needs sage.symbolic
            sage: x.row() == matrix(x)
            True
            sage: x.row() == x.column().transpose()
            True

        Sparse or dense implementations are preserved. ::

            sage: d = vector(RR, [1.0, 2.0, 3.0])
            sage: s = vector(CDF, {2: 5.0+6.0*I})                                       # needs sage.symbolic
            sage: dm = d.row()
            sage: sm = s.row()                                                          # needs sage.symbolic
            sage: all([d.is_dense(), dm.is_dense(), s.is_sparse(), sm.is_sparse()])     # needs sage.symbolic
            True

        TESTS:

        The :meth:`~sage.matrix.matrix1.Matrix.row` method will return
        a specified row of a matrix as a vector.  So here are a couple
        of round-trips. ::

            sage: A = matrix(ZZ, [[1,2,3]])
            sage: A == A.row(0).row()
            True
            sage: v = vector(ZZ, [4,5,6])
            sage: v == v.row().row(0)
            True

        And a very small corner case. ::

            sage: v = vector(ZZ, [])
            sage: w = v.row()
            sage: w.parent()
            Full MatrixSpace of 1 by 0 dense matrices over Integer Ring"""
    def set(self, i, value) -> Any:
        """FreeModuleElement.set(self, i, value)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1980)

        Like ``__setitem__`` but without type or bounds checking:
        `i` must satisfy ``0 <= i < self.degree`` and ``value`` must be
        an element of the coordinate ring.

        EXAMPLES::

            sage: v = vector(SR, [1/2,2/5,0]); v                                        # needs sage.symbolic
            (1/2, 2/5, 0)
            sage: v.set(2, pi); v                                                       # needs sage.symbolic
            (1/2, 2/5, pi)"""
    @overload
    def sparse_vector(self) -> Any:
        """FreeModuleElement.sparse_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3884)

        Return sparse version of ``self``.  If ``self`` is sparse, just return
        self; otherwise, create and return correspond sparse vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def sparse_vector(self) -> Any:
        """FreeModuleElement.sparse_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3884)

        Return sparse version of ``self``.  If ``self`` is sparse, just return
        self; otherwise, create and return correspond sparse vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def sparse_vector(self) -> Any:
        """FreeModuleElement.sparse_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3884)

        Return sparse version of ``self``.  If ``self`` is sparse, just return
        self; otherwise, create and return correspond sparse vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def sparse_vector(self) -> Any:
        """FreeModuleElement.sparse_vector(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3884)

        Return sparse version of ``self``.  If ``self`` is sparse, just return
        self; otherwise, create and return correspond sparse vector.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector().is_sparse()
            True
            sage: vector([-1,0,3,0,0,0]).sparse_vector()
            (-1, 0, 3, 0, 0, 0)"""
    @overload
    def subs(self, in_dict=..., **kwds) -> Any:
        """FreeModuleElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1602)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: var('a,b,d,e')
            (a, b, d, e)
            sage: v = vector([a, b, d, e])
            sage: v.substitute(a=1)
            (1, b, d, e)
            sage: v.subs(a=b, b=d)
            (b, d, d, e)"""
    @overload
    def subs(self, a=..., b=...) -> Any:
        """FreeModuleElement.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1602)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: var('a,b,d,e')
            (a, b, d, e)
            sage: v = vector([a, b, d, e])
            sage: v.substitute(a=1)
            (1, b, d, e)
            sage: v.subs(a=b, b=d)
            (b, d, d, e)"""
    @overload
    def support(self) -> Any:
        """FreeModuleElement.support(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3803)

        Return the integers ``i`` such that ``self[i] != 0``.
        This is the same as the ``nonzero_positions`` function.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).support()
            [0, 2, 6]"""
    @overload
    def support(self) -> Any:
        """FreeModuleElement.support(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3803)

        Return the integers ``i`` such that ``self[i] != 0``.
        This is the same as the ``nonzero_positions`` function.

        EXAMPLES::

            sage: vector([-1,0,3,0,0,0,0.01]).support()
            [0, 2, 6]"""
    def tensor_product(self, *args, **kwargs):
        '''FreeModuleElement.outer_product(self, right)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 3409)

        Return a matrix, the outer product of two vectors ``self`` and ``right``.

        INPUT:

        - ``right`` -- a vector (or free module element) of any size, whose
          elements are compatible (with regard to multiplication) with the
          elements of ``self``.

        OUTPUT:

        The outer product of two vectors `x` and `y` (respectively
        ``self`` and ``right``) can be described several ways.  If we
        interpret `x` as a `m\\times 1` matrix and interpret `y` as a
        `1\\times n` matrix, then the outer product is the `m\\times n`
        matrix from the usual matrix product `xy`.  Notice how this
        is the "opposite" in some ways from an inner product (which
        would require `m=n`).

        If we just consider vectors, use each entry of `x` to create
        a scalar multiples of the vector `y` and use these vectors as
        the rows of a matrix.  Or use each entry of `y` to create a
        scalar multiples of `x` and use these vectors as the columns
        of a matrix.

        EXAMPLES::

            sage: u = vector(QQ, [1/2, 1/3, 1/4, 1/5])
            sage: v = vector(ZZ, [60, 180, 600])
            sage: u.outer_product(v)
            [ 30  90 300]
            [ 20  60 200]
            [ 15  45 150]
            [ 12  36 120]
            sage: M = v.outer_product(u); M
            [ 30  20  15  12]
            [ 90  60  45  36]
            [300 200 150 120]
            sage: M.parent()
            Full MatrixSpace of 3 by 4 dense matrices over Rational Field

        The more general :meth:`sage.matrix.matrix2.tensor_product` is an
        operation on a pair of matrices.  If we construct a pair of vectors
        as a column vector and a row vector, then an outer product and a
        tensor product are identical.  Thus ``tensor_product`` is a synonym
        for this method.  ::

            sage: u = vector(QQ, [1/2, 1/3, 1/4, 1/5])
            sage: v = vector(ZZ, [60, 180, 600])
            sage: u.tensor_product(v) == (u.column()).tensor_product(v.row())
            True

        The result is always a dense matrix, no matter if the two
        vectors are, or are not, dense.  ::

            sage: d = vector(ZZ,[4,5], sparse=False)
            sage: s = vector(ZZ, [1,2,3], sparse=True)
            sage: dd = d.outer_product(d)
            sage: ds = d.outer_product(s)
            sage: sd = s.outer_product(d)
            sage: ss = s.outer_product(s)
            sage: all([dd.is_dense(), ds.is_dense(), sd.is_dense(), dd.is_dense()])
            True

        Vectors with no entries do the right thing.  ::

            sage: v = vector(ZZ, [])
            sage: z = v.outer_product(v)
            sage: z.parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring

        There is a fair amount of latitude in the value of the ``right``
        vector, and the matrix that results can have entries from a new
        ring large enough to contain the result. If you know better,
        you can sometimes bring the result down to a less general ring.  ::

            sage: R.<t> = ZZ[]
            sage: v = vector(R, [12, 24*t])
            sage: w = vector(QQ, [1/2, 1/3, 1/4])
            sage: op = v.outer_product(w); op
            [   6    4    3]
            [12*t  8*t  6*t]
            sage: op.base_ring()
            Univariate Polynomial Ring in t over Rational Field
            sage: m = op.change_ring(R); m
            [   6    4    3]
            [12*t  8*t  6*t]
            sage: m.base_ring()
            Univariate Polynomial Ring in t over Integer Ring

        But some inputs are not compatible, even if vectors. ::

            sage: w = vector(GF(5), [1,2])
            sage: v = vector(GF(7), [1,2,3,4])
            sage: z = w.outer_product(v)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            \'Full MatrixSpace of 2 by 1 dense matrices over Finite Field of size 5\' and
            \'Full MatrixSpace of 1 by 4 dense matrices over Finite Field of size 7\'

        And some inputs don\'t make any sense at all. ::

            sage: w = vector(QQ, [5,10])
            sage: z = w.outer_product(6)
            Traceback (most recent call last):
            ...
            TypeError: right operand in an outer product must be a vector,
            not an element of Integer Ring'''
    def __abs__(self) -> Any:
        """FreeModuleElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1718)

        Return the square root of the sum of the squares of the entries of
        this vector.

        EXAMPLES::

            sage: v = vector([1..5]); abs(v)                                            # needs sage.symbolic
            sqrt(55)
            sage: v = vector(RDF, [1..5]); abs(v)
            7.416198487095663"""
    def __copy__(self) -> Any:
        """FreeModuleElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1576)

        Make a copy of this vector.

        EXAMPLES::

            sage: v = vector([1..5]); v
            (1, 2, 3, 4, 5)
            sage: w = copy(v)
            sage: v == w
            True
            sage: v is w
            False

        ::

            sage: v = vector([1..5], sparse=True); v
            (1, 2, 3, 4, 5)
            sage: copy(v)
            (1, 2, 3, 4, 5)"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, i) -> Any:
        """FreeModuleElement.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1878)

        Return `i`-th entry or slice of ``self``.

        EXAMPLES::

            sage: v = sage.modules.free_module_element.FreeModuleElement(QQ^3)
            sage: v.__getitem__(0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def __hash__(self) -> Any:
        """FreeModuleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1209)

        Return hash of this vector.  Only immutable vectors are hashable.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,2/3,pi])
            sage: v.__hash__()
            Traceback (most recent call last):
            ...
            TypeError: mutable vectors are unhashable
            sage: v.set_immutable()
            sage: v.__hash__()   # random output"""
    @overload
    def __hash__(self) -> Any:
        """FreeModuleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1209)

        Return hash of this vector.  Only immutable vectors are hashable.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,2/3,pi])
            sage: v.__hash__()
            Traceback (most recent call last):
            ...
            TypeError: mutable vectors are unhashable
            sage: v.set_immutable()
            sage: v.__hash__()   # random output"""
    @overload
    def __hash__(self) -> Any:
        """FreeModuleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1209)

        Return hash of this vector.  Only immutable vectors are hashable.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([1,2/3,pi])
            sage: v.__hash__()
            Traceback (most recent call last):
            ...
            TypeError: mutable vectors are unhashable
            sage: v.set_immutable()
            sage: v.__hash__()   # random output"""
    @overload
    def __invert__(self) -> Any:
        """FreeModuleElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1996)

        Invert v, which makes no sense, and is hence is not implemented.

        EXAMPLES::

            sage: vector([1,2/3,pi]).__invert__()                                       # needs sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def __invert__(self) -> Any:
        """FreeModuleElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1996)

        Invert v, which makes no sense, and is hence is not implemented.

        EXAMPLES::

            sage: vector([1,2/3,pi]).__invert__()                                       # needs sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def __len__(self) -> Any:
        """FreeModuleElement.__len__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2009)

        EXAMPLES::

            sage: len(sage.modules.free_module_element.FreeModuleElement(QQ^2010))
            2010"""
    def __mod__(self, p) -> Any:
        """FreeModuleElement.__mod__(self, p)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2018)

        EXAMPLES::

            sage: V = vector(ZZ, [5, 9, 13, 15])
            sage: V % 7
            (5, 2, 6, 1)
            sage: parent(V % 7)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def __pari__(self) -> Any:
        """FreeModuleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1038)

        Convert ``self`` to a PARI vector.

        OUTPUT: a PARI ``gen`` of type ``t_VEC``

        EXAMPLES::

            sage: v = vector(range(4))
            sage: v.__pari__()                                                          # needs sage.libs.pari
            [0, 1, 2, 3]
            sage: v.__pari__().type()                                                   # needs sage.libs.pari
            't_VEC'

        A list of vectors::

            sage: L = [vector(i^n for i in range(4)) for n in [1,3,5]]
            sage: pari(L)                                                               # needs sage.libs.pari
            [[0, 1, 2, 3], [0, 1, 8, 27], [0, 1, 32, 243]]"""
    @overload
    def __pari__(self) -> Any:
        """FreeModuleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1038)

        Convert ``self`` to a PARI vector.

        OUTPUT: a PARI ``gen`` of type ``t_VEC``

        EXAMPLES::

            sage: v = vector(range(4))
            sage: v.__pari__()                                                          # needs sage.libs.pari
            [0, 1, 2, 3]
            sage: v.__pari__().type()                                                   # needs sage.libs.pari
            't_VEC'

        A list of vectors::

            sage: L = [vector(i^n for i in range(4)) for n in [1,3,5]]
            sage: pari(L)                                                               # needs sage.libs.pari
            [[0, 1, 2, 3], [0, 1, 8, 27], [0, 1, 32, 243]]"""
    @overload
    def __pari__(self) -> Any:
        """FreeModuleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1038)

        Convert ``self`` to a PARI vector.

        OUTPUT: a PARI ``gen`` of type ``t_VEC``

        EXAMPLES::

            sage: v = vector(range(4))
            sage: v.__pari__()                                                          # needs sage.libs.pari
            [0, 1, 2, 3]
            sage: v.__pari__().type()                                                   # needs sage.libs.pari
            't_VEC'

        A list of vectors::

            sage: L = [vector(i^n for i in range(4)) for n in [1,3,5]]
            sage: pari(L)                                                               # needs sage.libs.pari
            [[0, 1, 2, 3], [0, 1, 8, 27], [0, 1, 32, 243]]"""
    @overload
    def __pos__(self) -> Any:
        """FreeModuleElement.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2154)

        Always returns ``self``, since ``+self == self``.

        EXAMPLES::

            sage: v = vector([1,2/3,8])
            sage: v.__pos__()
            (1, 2/3, 8)
            sage: +v
            (1, 2/3, 8)"""
    @overload
    def __pos__(self) -> Any:
        """FreeModuleElement.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2154)

        Always returns ``self``, since ``+self == self``.

        EXAMPLES::

            sage: v = vector([1,2/3,8])
            sage: v.__pos__()
            (1, 2/3, 8)
            sage: +v
            (1, 2/3, 8)"""
    def __pow__(self, n, dummy) -> Any:
        """FreeModuleElement.__pow__(self, n, dummy)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 2168)

        Raises a :exc:`NotImplementedError`, since powering doesn't make
        sense for vectors.

        EXAMPLES::

            sage: v = vector([1,2/3,8])
            sage: v^2
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def __rmod__(self, other):
        """Return value%self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __setitem__(self, i, value) -> Any:
        """FreeModuleElement.__setitem__(self, i, value)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 1930)

        Set the `i`-th entry or slice of ``self`` to ``value``.

        EXAMPLES::

            sage: v = sage.modules.free_module_element.FreeModuleElement(QQ^3)
            sage: v[0] = 5
            Traceback (most recent call last):
            ...
            NotImplementedError

        For derived classes, this works::

            sage: v = vector([1,2/3,8])
            sage: v[0] = 5
            sage: v
            (5, 2/3, 8)"""

class FreeModuleElement_generic_dense(FreeModuleElement):
    """FreeModuleElement_generic_dense(parent, entries, coerce=True, copy=True)

    File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4328)

    A generic dense element of a free module.

    TESTS::

        sage: V = ZZ^3
        sage: loads(dumps(V)) == V
        True
        sage: v = V.0
        sage: loads(dumps(v)) == v
        True
        sage: v = (QQ['x']^3).0
        sage: loads(dumps(v)) == v
        True

    ::

        sage: v = vector([1,2/3,pi])                                                    # needs sage.symbolic
        sage: v == v
        True

    ::

        sage: v = vector(RR, [1,2/3,pi])                                                # needs sage.symbolic
        sage: v.set_immutable()
        sage: isinstance(hash(v), int)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries, coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4404)

                EXAMPLES::

                    sage: type(vector(RR, [-1,0,2/3,pi,oo]))                                    # needs sage.symbolic
                    <class 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>

                We can initialize with lists, tuples and derived types::

                    sage: from sage.modules.free_module_element import FreeModuleElement_generic_dense
                    sage: FreeModuleElement_generic_dense(RR^5, [-1,0,2/3,pi,oo])               # needs sage.symbolic
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_dense(RR^5, (-1,0,2/3,pi,oo))               # needs sage.symbolic
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_dense(RR^5, Sequence([-1,0,2/3,pi,oo]))     # needs sage.symbolic
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_dense(RR^0, 0)
                    ()

                TESTS:

                Disabling coercion can lead to illegal objects::

                    sage: FreeModuleElement_generic_dense(RR^5, [-1,0,2/3,pi,oo], coerce=False)             # needs sage.symbolic
                    (-1, 0, 2/3, pi, +Infinity)

                We test the ``copy`` flag::

                    sage: # needs sage.symbolic
                    sage: from sage.modules.free_module_element import FreeModuleElement_generic_dense
                    sage: L = [RR(x) for x in (-1,0,2/3,pi,oo)]
                    sage: FreeModuleElement_generic_dense(RR^5, tuple(L), coerce=False, copy=False)
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: v = FreeModuleElement_generic_dense(RR^5, L, coerce=False, copy=False)
                    sage: L[4] = 42.0
                    sage: v  # last entry changed since we didn't copy
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, 42.0000000000000)

                ::

                    sage: # needs sage.symbolic
                    sage: L = [RR(x) for x in (-1,0,2/3,pi,oo)]
                    sage: v = FreeModuleElement_generic_dense(RR^5, L, coerce=False, copy=True)
                    sage: L[4] = 42.0
                    sage: v  # last entry did not change
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)

                Check that :issue:`11751` is fixed::

                    sage: K.<x> = QQ[]
                    sage: M = K^1
                    sage: N = M.span([[1/x]]); N
                    Free module of degree 1 and rank 1 over Univariate Polynomial Ring in x over Rational Field
                    Echelon basis matrix:
                    [1/x]
                    sage: N([1/x]) # this used to fail prior to #11751
                    (1/x)
                    sage: N([1/x^2])
                    Traceback (most recent call last):
                    ...
                    TypeError: element [1/x^2] is not in free module

                ::

                    sage: L=K^2
                    sage: R=L.span([[x,0],[0,1/x]], check=False, already_echelonized=True)
                    sage: R.basis()[0][0].parent()
                    Fraction Field of Univariate Polynomial Ring in x over Rational Field
                    sage: R=L.span([[x,x^2]])
                    sage: R.basis()[0][0].parent()
                    Univariate Polynomial Ring in x over Rational Field
        """
    def function(self, *args) -> Any:
        """FreeModuleElement_generic_dense.function(self, *args)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4719)

        Return a vector over a callable symbolic expression ring.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, y = var('x,y')
            sage: v = vector([x, y, x*sin(y)])
            sage: w = v.function([x,y]); w
            (x, y) |--> (x, y, x*sin(y))
            sage: w.coordinate_ring()
            Callable function ring with arguments (x, y)
            sage: w(1,2)
            (1, 2, sin(2))
            sage: w(2,1)
            (2, 1, 2*sin(1))
            sage: w(y=1,x=2)
            (2, 1, 2*sin(1))

        ::

            sage: # needs sage.symbolic
            sage: x,y = var('x,y')
            sage: v = vector([x, y, x*sin(y)])
            sage: w = v.function([x]); w
            x |--> (x, y, x*sin(y))
            sage: w.coordinate_ring()
            Callable function ring with argument x
            sage: w(4)
            (4, y, 4*sin(y))"""
    @overload
    def list(self, copy=...) -> Any:
        """FreeModuleElement_generic_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4665)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean; return list of underlying entries

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z])
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)
            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x*y, y, z)"""
    @overload
    def list(self) -> Any:
        """FreeModuleElement_generic_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4665)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean; return list of underlying entries

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z])
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)
            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x*y, y, z)"""
    @overload
    def list(self, copy=...) -> Any:
        """FreeModuleElement_generic_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4665)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- boolean; return list of underlying entries

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: v = vector([x,y,z])
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>
            sage: a = v.list(); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x, y, z)
            sage: a = v.list(copy=False); a
            [x, y, z]
            sage: a[0] = x*y; v
            (x*y, y, z)"""
    def __call__(self, *args, **kwargs) -> Any:
        """FreeModuleElement_generic_dense.__call__(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4693)

        Calling a free module element returns the result of calling each
        component.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, y = var('x,y')
            sage: f = x^2 + y^2
            sage: g = f.gradient()
            sage: g
            (2*x, 2*y)
            sage: type(g)
            <class 'sage.modules.free_module.FreeModule_ambient_field_with_category.element_class'>
            sage: g(y=2, x=3)
            (6, 4)
            sage: f(x,y) = x^2 + y^2
            sage: g = f.gradient()
            sage: g(3,2)
            (6, 4)
            sage: g(x=3, y=2)
            (6, 4)"""
    @overload
    def __copy__(self) -> Any:
        """FreeModuleElement_generic_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4380)

        Return a copy of this generic dense vector.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([-1,0,3,pi])
            sage: type(v)
            <class 'sage.modules.free_module.FreeModule_ambient_field_with_category.element_class'>
            sage: v.__copy__()
            (-1, 0, 3, pi)
            sage: v.__copy__() is v
            False

            sage: copy(v)                                                               # needs sage.symbolic
            (-1, 0, 3, pi)
            sage: copy(v) == v                                                          # needs sage.symbolic
            True
            sage: copy(v) is v                                                          # needs sage.symbolic
            False"""
    @overload
    def __copy__(self) -> Any:
        """FreeModuleElement_generic_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4380)

        Return a copy of this generic dense vector.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([-1,0,3,pi])
            sage: type(v)
            <class 'sage.modules.free_module.FreeModule_ambient_field_with_category.element_class'>
            sage: v.__copy__()
            (-1, 0, 3, pi)
            sage: v.__copy__() is v
            False

            sage: copy(v)                                                               # needs sage.symbolic
            (-1, 0, 3, pi)
            sage: copy(v) == v                                                          # needs sage.symbolic
            True
            sage: copy(v) is v                                                          # needs sage.symbolic
            False"""
    @overload
    def __copy__(self) -> Any:
        """FreeModuleElement_generic_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4380)

        Return a copy of this generic dense vector.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: v = vector([-1,0,3,pi])
            sage: type(v)
            <class 'sage.modules.free_module.FreeModule_ambient_field_with_category.element_class'>
            sage: v.__copy__()
            (-1, 0, 3, pi)
            sage: v.__copy__() is v
            False

            sage: copy(v)                                                               # needs sage.symbolic
            (-1, 0, 3, pi)
            sage: copy(v) == v                                                          # needs sage.symbolic
            True
            sage: copy(v) is v                                                          # needs sage.symbolic
            False"""
    @overload
    def __reduce__(self) -> Any:
        """FreeModuleElement_generic_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4603)

        EXAMPLES::

            sage: v = vector([-1,0,3,pi])                                               # needs sage.symbolic
            sage: v.__reduce__()                                                        # needs sage.symbolic
            (<cyfunction make_FreeModuleElement_generic_dense_v1 at ...>,
             (Vector space of dimension 4 over Symbolic Ring, [-1, 0, 3, pi], 4, True))"""
    @overload
    def __reduce__(self) -> Any:
        """FreeModuleElement_generic_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4603)

        EXAMPLES::

            sage: v = vector([-1,0,3,pi])                                               # needs sage.symbolic
            sage: v.__reduce__()                                                        # needs sage.symbolic
            (<cyfunction make_FreeModuleElement_generic_dense_v1 at ...>,
             (Vector space of dimension 4 over Symbolic Ring, [-1, 0, 3, pi], 4, True))"""

class FreeModuleElement_generic_sparse(FreeModuleElement):
    """FreeModuleElement_generic_sparse(parent, entries=0, coerce=True, copy=True)

    File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4794)

    A generic sparse free module element is a dictionary with keys ints
    i and entries in the base ring.

    TESTS::

        sage: v = vector([1,2/3,pi], sparse=True)                                       # needs sage.symbolic
        sage: v.set_immutable()                                                         # needs sage.symbolic
        sage: isinstance(hash(v), int)                                                  # needs sage.symbolic
        True

    Pickling works::

        sage: v = FreeModule(ZZ, 3, sparse=True).0
        sage: loads(dumps(v)) == v
        True
        sage: v = FreeModule(Integers(8)['x,y'], 5, sparse=True).1
        sage: loads(dumps(v)) - v
        (0, 0, 0, 0, 0)

    ::

        sage: a = vector([-1,0,1/1],sparse=True); b = vector([-1/1,0,0],sparse=True)
        sage: a.parent()
        Sparse vector space of dimension 3 over Rational Field
        sage: b - a
        (0, 0, -1)
        sage: (b-a).dict()
        {2: -1}"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4859)

                EXAMPLES::

                    sage: v = sage.modules.free_module_element.FreeModuleElement_generic_sparse(VectorSpace(QQ,3,sparse=True), {1:5/4}); v
                    (0, 5/4, 0)
                    sage: v.is_sparse()
                    True

                We can initialize with dicts, lists, tuples and derived types::

                    sage: from sage.modules.free_module_element import FreeModuleElement_generic_sparse
                    sage: def S(R, n):
                    ....:     return FreeModule(R, n, sparse=True)

                    sage: # needs sage.symbolic
                    sage: FreeModuleElement_generic_sparse(S(RR,5), {0:-1, 2:2/3, 3:pi, 4:oo})
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_sparse(S(RR,5), [-1,0,2/3,pi,oo])
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_sparse(S(RR,5), (-1,0,2/3,pi,oo))
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)
                    sage: FreeModuleElement_generic_sparse(S(RR,5), Sequence([-1,0,2/3,pi,oo]))
                    (-1.00000000000000, 0.000000000000000, 0.666666666666667, 3.14159265358979, +infinity)

                    sage: FreeModuleElement_generic_sparse(S(RR,0), 0)
                    ()

                    sage: from collections import defaultdict
                    sage: D = defaultdict(RR)
                    sage: D[0] = -1
                    sage: FreeModuleElement_generic_sparse(S(RR,5), D)
                    (-1.00000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000)

                TESTS:

                Test that :issue:`11751` is fixed::

                    sage: K.<x> = QQ[]
                    sage: M = FreeModule(K, 1, sparse=True)
                    sage: N = M.span([{0:1/x}]); N
                    Sparse free module of degree 1 and rank 1 over Univariate Polynomial Ring in x over Rational Field
                    Echelon basis matrix:
                    [1/x]
                    sage: N({0:1/x}) # this used to fail prior to #11751
                    (1/x)
                    sage: N({0:1/x^2})
                    Traceback (most recent call last):
                    ...
                    TypeError: element {0: 1/x^2} is not in free module

                ::

                    sage: L = FreeModule(K, 2, sparse=True)
                    sage: R = L.span([{0:x, 1:0}, {0:0, 1:1/x}], check=False, already_echelonized=True)
                    sage: R.basis()[0][0].parent()
                    Fraction Field of Univariate Polynomial Ring in x over Rational Field
                    sage: R = L.span([{0:x, 1:x^2}])
                    sage: R.basis()[0][0].parent()
                    Univariate Polynomial Ring in x over Rational Field

                Test that :issue:`17101` is fixed::

                    sage: # needs sage.rings.real_interval_field
                    sage: v = vector([RIF(-1, 1)], sparse=True)
                    sage: v.is_zero()
                    False

                We correctly initialize values which become 0 only after coercion::

                    sage: v = FreeModuleElement_generic_sparse(S(GF(3), 6), [1,2,3,4,5,6])
                    sage: v.nonzero_positions()
                    [0, 1, 3, 4]
        """
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement_generic_sparse.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5314)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14], sparse=True)
            sage: v.denominator()
            70"""
    @overload
    def denominator(self) -> Any:
        """FreeModuleElement_generic_sparse.denominator(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5314)

        Return the least common multiple of the denominators of the
        entries of ``self``.

        EXAMPLES::

            sage: v = vector([1/2,2/5,3/14], sparse=True)
            sage: v.denominator()
            70"""
    @overload
    def dict(self, copy=...) -> Any:
        """FreeModuleElement_generic_sparse.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5336)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14], sparse=True)
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]"""
    @overload
    def dict(self) -> Any:
        """FreeModuleElement_generic_sparse.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5336)

        Return dictionary of nonzero entries of ``self``.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements in the support of ``self`` and whose values are
        the corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        OUTPUT: Python dictionary

        EXAMPLES::

            sage: v = vector([0,0,0,0,1/2,0,3/14], sparse=True)
            sage: v.dict()
            {4: 1/2, 6: 3/14}
            sage: sorted(v.support())
            [4, 6]"""
    @overload
    def hamming_weight(self) -> int:
        """FreeModuleElement_generic_sparse.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5410)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: v = vector({1: 1, 3: -2})
            sage: w = vector({1: 4, 3: 2})
            sage: v+w
            (0, 5, 0, 0)
            sage: (v+w).hamming_weight()
            1"""
    @overload
    def hamming_weight(self) -> Any:
        """FreeModuleElement_generic_sparse.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5410)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: v = vector({1: 1, 3: -2})
            sage: w = vector({1: 4, 3: 2})
            sage: v+w
            (0, 5, 0, 0)
            sage: (v+w).hamming_weight()
            1"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement_generic_sparse.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5148)

        Return an iterator over the entries of ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: next(v.items())                                                       # needs sage.symbolic
            (0, 1)
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement_generic_sparse.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5148)

        Return an iterator over the entries of ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: next(v.items())                                                       # needs sage.symbolic
            (0, 1)
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def items(self) -> Any:
        """FreeModuleElement_generic_sparse.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5148)

        Return an iterator over the entries of ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: next(v.items())                                                       # needs sage.symbolic
            (0, 1)
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    def iteritems(self) -> Any:
        """FreeModuleElement_generic_sparse.items(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5148)

        Return an iterator over the entries of ``self``.

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: next(v.items())                                                       # needs sage.symbolic
            (0, 1)
            sage: list(v.items())                                                       # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]

        TESTS:

        Using iteritems as an alias::

            sage: list(v.iteritems())                                                   # needs sage.symbolic
            [(0, 1), (1, 2/3), (2, pi)]"""
    @overload
    def list(self, copy=...) -> Any:
        """FreeModuleElement_generic_sparse.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5366)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- ignored for sparse vectors

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: M = FreeModule(R, 3, sparse=True) * (1/x)
            sage: v = M([-x^2, 3/x, 0])
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>
            sage: a = v.list()
            sage: a
            [-x^2, 3/x, 0]
            sage: [parent(c) for c in a]
            [Fraction Field of Univariate Polynomial Ring in x over Rational Field,
             Fraction Field of Univariate Polynomial Ring in x over Rational Field,
             Fraction Field of Univariate Polynomial Ring in x over Rational Field]"""
    @overload
    def list(self) -> Any:
        """FreeModuleElement_generic_sparse.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5366)

        Return list of elements of ``self``.

        INPUT:

        - ``copy`` -- ignored for sparse vectors

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: M = FreeModule(R, 3, sparse=True) * (1/x)
            sage: v = M([-x^2, 3/x, 0])
            sage: type(v)
            <class 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>
            sage: a = v.list()
            sage: a
            [-x^2, 3/x, 0]
            sage: [parent(c) for c in a]
            [Fraction Field of Univariate Polynomial Ring in x over Rational Field,
             Fraction Field of Univariate Polynomial Ring in x over Rational Field,
             Fraction Field of Univariate Polynomial Ring in x over Rational Field]"""
    @overload
    def nonzero_positions(self) -> Any:
        """FreeModuleElement_generic_sparse.nonzero_positions(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5395)

        Return the list of numbers ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: v = vector({1: 1, 3: -2})
            sage: w = vector({1: 4, 3: 2})
            sage: v+w
            (0, 5, 0, 0)
            sage: (v+w).nonzero_positions()
            [1]"""
    @overload
    def nonzero_positions(self) -> Any:
        """FreeModuleElement_generic_sparse.nonzero_positions(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5395)

        Return the list of numbers ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: v = vector({1: 1, 3: -2})
            sage: w = vector({1: 4, 3: 2})
            sage: v+w
            (0, 5, 0, 0)
            sage: (v+w).nonzero_positions()
            [1]"""
    def numerical_approx(self, prec=..., digits=..., algorithm=...) -> Any:
        """FreeModuleElement_generic_sparse.numerical_approx(self, prec=None, digits=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5425)

        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision, by approximating all
        entries.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute the
          approximation of the entries (the accepted algorithms depend
          on the object)

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: v = vector(RealField(200), [1,2,3], sparse=True)
            sage: v.n()
            (1.00000000000000, 2.00000000000000, 3.00000000000000)
            sage: _.parent()
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision
            sage: v.n(prec=75)
            (1.000000000000000000000, 2.000000000000000000000, 3.000000000000000000000)
            sage: _.parent()
            Sparse vector space of dimension 3 over Real Field with 75 bits of precision"""
    @overload
    def __copy__(self) -> Any:
        """FreeModuleElement_generic_sparse.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4849)

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: v.__copy__()                                                          # needs sage.symbolic
            (1, 2/3, pi)"""
    @overload
    def __copy__(self) -> Any:
        """FreeModuleElement_generic_sparse.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 4849)

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: v.__copy__()                                                          # needs sage.symbolic
            (1, 2/3, pi)"""
    def __getitem__(self, i) -> Any:
        """FreeModuleElement_generic_sparse.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5183)

        EXAMPLES::

            sage: v = vector(RR, range(6), sparse=True); v
            (0.000000000000000, 1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000, 5.00000000000000)
            sage: v[1]
            1.00000000000000
            sage: v[-1]
            5.00000000000000
            sage: v[9]
            Traceback (most recent call last):
            ...
            IndexError: vector index out of range
            sage: v[-7]
            Traceback (most recent call last):
            ...
            IndexError: vector index out of range
            sage: v[::2]
            (0.000000000000000, 2.00000000000000, 4.00000000000000)
            sage: v[5:2:-1]
            (5.00000000000000, 4.00000000000000, 3.00000000000000)

        All these operations with zero vectors should be very fast::

            sage: v = vector(RR, 10^9, sparse=True)
            sage: v[123456789]
            0.000000000000000
            sage: w = v[::-1]
            sage: v[::-250000000]
            (0.000000000000000, 0.000000000000000, 0.000000000000000, 0.000000000000000)
            sage: v[123456789:123456798:3]
            (0.000000000000000, 0.000000000000000, 0.000000000000000)"""
    @overload
    def __reduce__(self) -> Any:
        """FreeModuleElement_generic_sparse.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5171)

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: v.__reduce__()                                                        # needs sage.symbolic
            (<cyfunction make_FreeModuleElement_generic_sparse_v1 at ...>,
             (Sparse vector space of dimension 3 over Symbolic Ring, {0: 1, 1: 2/3, 2: pi}, 3, True))"""
    @overload
    def __reduce__(self) -> Any:
        """FreeModuleElement_generic_sparse.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/free_module_element.pyx (starting at line 5171)

        EXAMPLES::

            sage: v = vector([1,2/3,pi], sparse=True)                                   # needs sage.symbolic
            sage: v.__reduce__()                                                        # needs sage.symbolic
            (<cyfunction make_FreeModuleElement_generic_sparse_v1 at ...>,
             (Sparse vector space of dimension 3 over Symbolic Ring, {0: 1, 1: 2/3, 2: pi}, 3, True))"""
