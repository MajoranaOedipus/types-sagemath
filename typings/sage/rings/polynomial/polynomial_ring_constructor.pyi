from _typeshed import Incomplete
from sage import categories as categories
from sage.categories.algebras import Algebras as Algebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields, CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.categories.domains import Domains as Domains
from sage.categories.fields import Fields as Fields
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import weak_cached_function as weak_cached_function
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.structure.category_object import normalize_names as normalize_names

class padic_base_leaves:
    pAdicFieldCappedRelative: Incomplete
    pAdicRingCappedRelative: Incomplete
    pAdicRingCappedAbsolute: Incomplete
    pAdicRingFixedMod: Incomplete

def PolynomialRing(base_ring, *args, **kwds):
    '''
    Return the globally unique univariate or multivariate polynomial
    ring with given properties and variable name or names.

    There are many ways to specify the variables for the polynomial ring:

    1. ``PolynomialRing(base_ring, name, ...)``
    2. ``PolynomialRing(base_ring, names, ...)``
    3. ``PolynomialRing(base_ring, n, names, ...)``
    4. ``PolynomialRing(base_ring, n, ..., var_array=var_array, ...)``

    The ``...`` at the end of these commands stands for additional
    keywords, like ``sparse`` or ``order``.

    INPUT:

    - ``base_ring`` -- a ring

    - ``n`` -- integer

    - ``name`` -- string

    - ``names`` -- list or tuple of names (strings), or a comma separated string

    - ``var_array`` -- list or tuple of names, or a comma separated string

    - ``sparse`` -- boolean; whether or not elements are sparse. The
      default is a dense representation (``sparse=False``) for
      univariate rings and a sparse representation (``sparse=True``)
      for multivariate rings.

    - ``order`` -- string or
      :class:`~sage.rings.polynomial.term_order.TermOrder` object, e.g.,

      - ``\'degrevlex\'`` -- default; degree reverse lexicographic
      - ``\'lex\'`` -- lexicographic
      - ``\'deglex\'`` -- degree lexicographic
      - ``TermOrder(\'deglex\',3) + TermOrder(\'deglex\',3)`` -- block ordering

    - ``implementation`` -- string or None; selects an implementation in cases
      where Sage includes multiple choices (currently `\\ZZ[x]` can be
      implemented with ``\'NTL\'`` or ``\'FLINT\'``; default is ``\'FLINT\'``).
      For many base rings, the ``\'singular\'`` implementation is available.
      One can always specify ``implementation="generic"`` for a generic
      Sage implementation which does not use any specialized library.

    .. NOTE::

        If the given implementation does not exist for rings with the given
        number of generators and the given sparsity, then an error results.

    OUTPUT:

    ``PolynomialRing(base_ring, name, sparse=False)`` returns a univariate
    polynomial ring; also, PolynomialRing(base_ring, names, sparse=False)
    yields a univariate polynomial ring, if names is a list or tuple
    providing exactly one name. All other input formats return a
    multivariate polynomial ring.

    UNIQUENESS and IMMUTABILITY: In Sage there is exactly one
    single-variate polynomial ring over each base ring in each choice
    of variable, sparseness, and implementation.  There is also exactly
    one multivariate polynomial ring over each base ring for each
    choice of names of variables and term order.  The names of the
    generators can only be temporarily changed after the ring has been
    created.  Do this using the :func:`localvars` context.

    EXAMPLES:

    **1. PolynomialRing(base_ring, name, ...)**

    ::

        sage: PolynomialRing(QQ, \'w\')
        Univariate Polynomial Ring in w over Rational Field
        sage: PolynomialRing(QQ, name=\'w\')
        Univariate Polynomial Ring in w over Rational Field

    Use the diamond brackets notation to make the variable
    ready for use after you define the ring::

        sage: R.<w> = PolynomialRing(QQ)
        sage: (1 + w)^3
        w^3 + 3*w^2 + 3*w + 1

    You must specify a name::

        sage: PolynomialRing(QQ)
        Traceback (most recent call last):
        ...
        TypeError: you must specify the names of the variables

        sage: R.<abc> = PolynomialRing(QQ, sparse=True); R
        Sparse Univariate Polynomial Ring in abc over Rational Field

        sage: R.<w> = PolynomialRing(PolynomialRing(GF(7),\'k\')); R
        Univariate Polynomial Ring in w over
         Univariate Polynomial Ring in k over Finite Field of size 7

    The square bracket notation::

        sage: R.<y> = QQ[\'y\']; R
        Univariate Polynomial Ring in y over Rational Field
        sage: y^2 + y
        y^2 + y

    In fact, since the diamond brackets on the left determine the
    variable name, you can omit the variable from the square brackets::

        sage: R.<zz> = QQ[]; R
        Univariate Polynomial Ring in zz over Rational Field
        sage: (zz + 1)^2
        zz^2 + 2*zz + 1

    This is exactly the same ring as what PolynomialRing returns::

        sage: R is PolynomialRing(QQ, \'zz\')
        True

    However, rings with different variables are different::

        sage: QQ[\'x\'] == QQ[\'y\']
        False

    Sage has two implementations of univariate polynomials over the
    integers, one based on NTL and one based on FLINT.  The default
    is FLINT. Note that FLINT uses a "more dense" representation for
    its polynomials than NTL, so in particular, creating a polynomial
    like 2^1000000 * x^1000000 in FLINT may be unwise.
    ::

        sage: ZxNTL = PolynomialRing(ZZ, \'x\', implementation=\'NTL\'); ZxNTL              # needs sage.libs.ntl
        Univariate Polynomial Ring in x over Integer Ring (using NTL)
        sage: ZxFLINT = PolynomialRing(ZZ, \'x\', implementation=\'FLINT\'); ZxFLINT        # needs sage.libs.flint
        Univariate Polynomial Ring in x over Integer Ring
        sage: ZxFLINT is ZZ[\'x\']                                                        # needs sage.libs.flint
        True
        sage: ZxFLINT is PolynomialRing(ZZ, \'x\')                                        # needs sage.libs.flint
        True
        sage: xNTL = ZxNTL.gen()                                                        # needs sage.libs.ntl
        sage: xFLINT = ZxFLINT.gen()                                                    # needs sage.libs.flint
        sage: xNTL.parent()                                                             # needs sage.libs.ntl
        Univariate Polynomial Ring in x over Integer Ring (using NTL)
        sage: xFLINT.parent()                                                           # needs sage.libs.flint
        Univariate Polynomial Ring in x over Integer Ring

    There is a coercion from the non-default to the default
    implementation, so the values can be mixed in a single
    expression::

        sage: (xNTL + xFLINT^2)                                                         # needs sage.libs.flint sage.libs.ntl
        x^2 + x

    The result of such an expression will use the default, i.e.,
    the FLINT implementation::

        sage: (xNTL + xFLINT^2).parent()                                                # needs sage.libs.flint sage.libs.ntl
        Univariate Polynomial Ring in x over Integer Ring

    The generic implementation uses neither NTL nor FLINT::

        sage: Zx = PolynomialRing(ZZ, \'x\', implementation=\'generic\'); Zx
        Univariate Polynomial Ring in x over Integer Ring
        sage: Zx.element_class
        <... \'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense\'>

    **2. PolynomialRing(base_ring, names, ...)**

    ::

        sage: R = PolynomialRing(QQ, \'a,b,c\'); R
        Multivariate Polynomial Ring in a, b, c over Rational Field

        sage: S = PolynomialRing(QQ, [\'a\',\'b\',\'c\']); S
        Multivariate Polynomial Ring in a, b, c over Rational Field

        sage: T = PolynomialRing(QQ, (\'a\',\'b\',\'c\')); T
        Multivariate Polynomial Ring in a, b, c over Rational Field

    All three rings are identical::

        sage: R is S
        True
        sage: S is T
        True

    There is a unique polynomial ring with each term order::

        sage: R = PolynomialRing(QQ, \'x,y,z\', order=\'degrevlex\'); R
        Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: S = PolynomialRing(QQ, \'x,y,z\', order=\'invlex\'); S
        Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: S is PolynomialRing(QQ, \'x,y,z\', order=\'invlex\')
        True
        sage: R == S
        False

    Note that a univariate polynomial ring is returned, if the list
    of names is of length one. If it is of length zero, a multivariate
    polynomial ring with no variables is returned.

    ::

        sage: PolynomialRing(QQ,["x"])
        Univariate Polynomial Ring in x over Rational Field
        sage: PolynomialRing(QQ,[])
        Multivariate Polynomial Ring in no variables over Rational Field

    The Singular implementation always returns a multivariate ring,
    even for 1 variable::

        sage: PolynomialRing(QQ, "x", implementation=\'singular\')                        # needs sage.libs.singular
        Multivariate Polynomial Ring in x over Rational Field
        sage: P.<x> = PolynomialRing(QQ, implementation=\'singular\'); P                  # needs sage.libs.singular
        Multivariate Polynomial Ring in x over Rational Field

    **3. PolynomialRing(base_ring, n, names, ...)** (where the arguments
    ``n`` and ``names`` may be reversed)

    If you specify a single name as a string and a number of
    variables, then variables labeled with numbers are created.

    ::

        sage: PolynomialRing(QQ, \'x\', 10)
        Multivariate Polynomial Ring in x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 over Rational Field

        sage: PolynomialRing(QQ, 2, \'alpha0\')
        Multivariate Polynomial Ring in alpha00, alpha01 over Rational Field

        sage: PolynomialRing(GF(7), \'y\', 5)
        Multivariate Polynomial Ring in y0, y1, y2, y3, y4 over Finite Field of size 7

        sage: PolynomialRing(QQ, \'y\', 3, sparse=True)
        Multivariate Polynomial Ring in y0, y1, y2 over Rational Field

    Note that a multivariate polynomial ring is returned when an
    explicit number is given.

    ::

        sage: PolynomialRing(QQ,"x",1)
        Multivariate Polynomial Ring in x over Rational Field
        sage: PolynomialRing(QQ,"x",0)
        Multivariate Polynomial Ring in no variables over Rational Field

    It is easy in Python to create fairly arbitrary variable names.  For
    example, here is a ring with generators labeled by the primes less
    than 100::

        sage: R = PolynomialRing(ZZ, [\'x%s\'%p for p in primes(100)]); R                 # needs sage.libs.pari
        Multivariate Polynomial Ring in x2, x3, x5, x7, x11, x13, x17, x19, x23, x29,
         x31, x37, x41, x43, x47, x53, x59, x61, x67, x71, x73, x79, x83, x89, x97
         over Integer Ring

    By calling the
    :meth:`~sage.structure.category_object.CategoryObject.inject_variables`
    method, all those variable names are available for interactive use::

        sage: R.inject_variables()                                                      # needs sage.libs.pari
        Defining x2, x3, x5, x7, x11, x13, x17, x19, x23, x29, x31, x37, x41, x43,
        x47, x53, x59, x61, x67, x71, x73, x79, x83, x89, x97
        sage: (x2 + x41 + x71)^2                                                        # needs sage.libs.pari
        x2^2 + 2*x2*x41 + x41^2 + 2*x2*x71 + 2*x41*x71 + x71^2

    **4. PolynomialRing(base_ring, n, ..., var_array=var_array, ...)**

    This creates an array of variables where each variables begins with an
    entry in ``var_array`` and is indexed from 0 to `n-1`. ::

        sage: PolynomialRing(ZZ, 3, var_array=[\'x\',\'y\'])
        Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Integer Ring
        sage: PolynomialRing(ZZ, 3, var_array=\'a,b\')
        Multivariate Polynomial Ring in a0, b0, a1, b1, a2, b2 over Integer Ring

    It is possible to create higher-dimensional arrays::

        sage: PolynomialRing(ZZ, 2, 3, var_array=(\'p\', \'q\'))
        Multivariate Polynomial Ring
         in p00, q00, p01, q01, p02, q02, p10, q10, p11, q11, p12, q12
         over Integer Ring
        sage: PolynomialRing(ZZ, 2, 3, 4, var_array=\'m\')
        Multivariate Polynomial Ring in m000, m001, m002, m003, m010, m011,
         m012, m013, m020, m021, m022, m023, m100, m101, m102, m103, m110,
         m111, m112, m113, m120, m121, m122, m123 over Integer Ring

    The array is always at least 2-dimensional. So, if
    ``var_array`` is a single string and only a single number `n`
    is given, this creates an `n \\times n` array of variables::

        sage: PolynomialRing(ZZ, 2, var_array=\'m\')
        Multivariate Polynomial Ring in m00, m01, m10, m11 over Integer Ring

    **Square brackets notation**

    You can alternatively create a polynomial ring over a ring `R` with
    square brackets::

        sage: # needs sage.rings.real_mpfr
        sage: RR["x"]
        Univariate Polynomial Ring in x over Real Field with 53 bits of precision
        sage: RR["x,y"]
        Multivariate Polynomial Ring in x, y over Real Field with 53 bits of precision
        sage: P.<x,y> = RR[]; P
        Multivariate Polynomial Ring in x, y over Real Field with 53 bits of precision

    This notation does not allow to set any of the optional arguments.

    **Changing variable names**

    Consider ::

        sage: R.<x,y> = PolynomialRing(QQ, 2); R
        Multivariate Polynomial Ring in x, y over Rational Field
        sage: f = x^2 - 2*y^2

    You can\'t just globally change the names of those variables.
    This is because objects all over Sage could have pointers to
    that polynomial ring. ::

        sage: R._assign_names([\'z\',\'w\'])
        Traceback (most recent call last):
        ...
        ValueError: variable names cannot be changed after object creation.

    However, you can very easily change the names within a ``with`` block::

        sage: with localvars(R, [\'z\',\'w\']):
        ....:     print(f)
        z^2 - 2*w^2

    After the ``with`` block the names revert to what they were before::

        sage: print(f)
        x^2 - 2*y^2

    TESTS:

    We test here some changes introduced in :issue:`9944`.

    If there is no dense implementation for the given number of
    variables, then requesting a dense ring is an error::

        sage: S.<x,y> = PolynomialRing(QQ, sparse=False)
        Traceback (most recent call last):
        ...
        NotImplementedError: a dense representation of multivariate polynomials is not supported

    Check uniqueness if the same implementation is used for different
    values of the ``\'implementation\'`` keyword::

        sage: R = PolynomialRing(QQbar, \'j\', implementation=\'generic\')                  # needs sage.rings.number_field
        sage: S = PolynomialRing(QQbar, \'j\', implementation=None)                       # needs sage.rings.number_field
        sage: R is S                                                                    # needs sage.rings.number_field
        True

        sage: R = PolynomialRing(ZZ[\'t\'], \'j\', implementation=\'generic\')
        sage: S = PolynomialRing(ZZ[\'t\'], \'j\', implementation=None)
        sage: R is S
        True

        sage: # needs sage.rings.number_field
        sage: R = PolynomialRing(QQbar, \'j,k\', implementation=\'generic\')
        sage: S = PolynomialRing(QQbar, \'j,k\', implementation=None)
        sage: R is S
        True

        sage: # needs sage.libs.singular
        sage: R = PolynomialRing(ZZ, \'j,k\', implementation=\'singular\')
        sage: S = PolynomialRing(ZZ, \'j,k\', implementation=None)
        sage: R is S
        True

        sage: R = PolynomialRing(ZZ, \'p\', sparse=True, implementation=\'generic\')
        sage: S = PolynomialRing(ZZ, \'p\', sparse=True)
        sage: R is S
        True

    The generic implementation is different in some cases::

        sage: R = PolynomialRing(GF(2), \'j\', implementation=\'generic\'); TestSuite(R).run(skip=[\'_test_construction\', \'_test_pickling\']); type(R)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category\'>
        sage: S = PolynomialRing(GF(2), \'j\'); TestSuite(S).run(); type(S)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_mod_p_with_category\'>

        sage: R = PolynomialRing(ZZ, \'x,y\', implementation=\'generic\'); TestSuite(R).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\']); type(R)
        <class \'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain_with_category\'>
        sage: S = PolynomialRing(ZZ, \'x,y\'); TestSuite(S).run(skip=\'_test_elements\'); type(S)       # needs sage.libs.singular
        <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular\'>

    Sparse univariate polynomials only support a generic
    implementation::

        sage: R = PolynomialRing(ZZ, \'j\', sparse=True); TestSuite(R).run(); type(R)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain_with_category\'>
        sage: R = PolynomialRing(GF(49), \'j\', sparse=True); TestSuite(R).run(); type(R)             # needs sage.rings.finite_rings
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category\'>

    If the requested implementation is not known or not supported for
    the given arguments, then an error results::

        sage: R.<x0> = PolynomialRing(ZZ, implementation=\'Foo\')
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'Foo\' for dense polynomial rings over Integer Ring
        sage: R.<x0> = PolynomialRing(GF(2), implementation=\'GF2X\', sparse=True)
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'GF2X\' for sparse polynomial rings over Finite Field of size 2
        sage: R.<x,y> = PolynomialRing(ZZ, implementation=\'FLINT\')
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'FLINT\' for multivariate polynomial rings
        sage: R.<x> = PolynomialRing(QQbar, implementation=\'whatever\')                  # needs sage.rings.number_field
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'whatever\' for dense polynomial rings over Algebraic Field
        sage: R.<x> = PolynomialRing(ZZ[\'t\'], implementation=\'whatever\')
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'whatever\' for dense polynomial rings over Univariate Polynomial Ring in t over Integer Ring
        sage: PolynomialRing(RR, "x,y", implementation=\'whatever\')
        Traceback (most recent call last):
        ...
        ValueError: unknown implementation \'whatever\' for multivariate polynomial rings
        sage: PolynomialRing(RR, name=\'x\', implementation=\'singular\')                   # needs sage.libs.singular
        Traceback (most recent call last):
        ...
        NotImplementedError: polynomials over Real Field with 53 bits of precision are not supported in Singular

    The following corner case used to result in a warning message from
    ``libSingular``, and the generators of the resulting polynomial
    ring were not zero::

        sage: R = Integers(1)[\'x\',\'y\']
        sage: R.0 == 0
        True

    We verify that :issue:`13187` is fixed::

        sage: var(\'t\')                                                                  # needs sage.symbolic
        t
        sage: PolynomialRing(ZZ, name=t) == PolynomialRing(ZZ, name=\'t\')                # needs sage.symbolic
        True

    We verify that polynomials with interval coefficients from
    :issue:`7712` and :issue:`13760` are fixed::

        sage: # needs sage.rings.real_interval_field
        sage: P.<y,z> = PolynomialRing(RealIntervalField(2))
        sage: TestSuite(P).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\'])
        sage: Q.<x> = PolynomialRing(P)
        sage: TestSuite(Q).run(skip=[\'_test_additive_associativity\', \'_test_associativity\',
        ....:                        \'_test_distributivity\', \'_test_prod\'])
        sage: C = (y-x)^3
        sage: C(y/2)
        1.?*y^3
        sage: R.<x,y> = PolynomialRing(RIF,2)
        sage: TestSuite(R).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\'])
        sage: RIF(-2,1)*x
        0.?e1*x

    For historical reasons, we allow redundant variable names with the
    angle bracket notation. The names must be consistent though! ::

        sage: P.<x,y> = PolynomialRing(ZZ, "x,y"); P
        Multivariate Polynomial Ring in x, y over Integer Ring
        sage: P.<x,y> = ZZ["x,y"]; P
        Multivariate Polynomial Ring in x, y over Integer Ring
        sage: P.<x,y> = PolynomialRing(ZZ, 2, "x"); P
        Traceback (most recent call last):
        ...
        TypeError: variable names specified twice inconsistently: (\'x0\', \'x1\') and (\'x\', \'y\')

    We test a lot of invalid input::

        sage: PolynomialRing(4)
        Traceback (most recent call last):
        ...
        TypeError: base_ring 4 must be a ring or the tropical semiring
        sage: PolynomialRing(QQ, -1)
        Traceback (most recent call last):
        ...
        ValueError: number of variables must be nonnegative
        sage: PolynomialRing(QQ, 1)
        Traceback (most recent call last):
        ...
        TypeError: you must specify the names of the variables
        sage: PolynomialRing(QQ, \'x\', None)
        Traceback (most recent call last):
        ...
        TypeError: invalid arguments (\'x\', None) for PolynomialRing
        sage: PolynomialRing(QQ, \'x\', \'y\')
        Traceback (most recent call last):
        ...
        TypeError: variable names specified twice: \'x\' and \'y\'
        sage: PolynomialRing(QQ, 1, \'x\', 2)
        Traceback (most recent call last):
        ...
        TypeError: number of variables specified twice: 1 and 2
        sage: PolynomialRing(QQ, \'x\', names=\'x\')
        Traceback (most recent call last):
        ...
        TypeError: variable names specified twice inconsistently: (\'x\',) and \'x\'
        sage: PolynomialRing(QQ, name=\'x\', names=\'x\')
        Traceback (most recent call last):
        ...
        TypeError: keyword argument \'name\' cannot be combined with \'names\'
        sage: PolynomialRing(QQ, var_array=\'x\')
        Traceback (most recent call last):
        ...
        TypeError: you must specify the number of the variables
        sage: PolynomialRing(QQ, 2, \'x\', var_array=\'x\')
        Traceback (most recent call last):
        ...
        TypeError: unable to convert \'x\' to an integer

    We run the testsuite for various polynomial rings, skipping tests that currently fail::

        sage: R.<w> = PolynomialRing(PolynomialRing(GF(7),\'k\')); TestSuite(R).run(); R
        Univariate Polynomial Ring in w over Univariate Polynomial Ring in k over Finite Field of size 7
        sage: ZxNTL = PolynomialRing(ZZ, \'x\', implementation=\'NTL\'); TestSuite(ZxNTL).run(skip=\'_test_pickling\'); ZxNTL                                         # needs sage.libs.ntl
        Univariate Polynomial Ring in x over Integer Ring (using NTL)
        sage: ZxFLINT = PolynomialRing(ZZ, \'x\', implementation=\'FLINT\'); TestSuite(ZxFLINT).run(); ZxFLINT
        Univariate Polynomial Ring in x over Integer Ring
        sage: Zx = PolynomialRing(ZZ, \'x\', implementation=\'generic\'); TestSuite(Zx).run(skip=[\'_test_construction\', \'_test_pickling\']); Zx
        Univariate Polynomial Ring in x over Integer Ring
        sage: R = PolynomialRing(QQ, \'a,b,c\'); TestSuite(R).run(skip=\'_test_elements\'); R
        Multivariate Polynomial Ring in a, b, c over Rational Field
        sage: R = PolynomialRing(QQ, \'x,y,z\', order=\'degrevlex\'); TestSuite(R).run(skip=\'_test_elements\'); R
        Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: S = PolynomialRing(QQ, \'x,y,z\', order=\'invlex\'); TestSuite(S).run(skip=[\'_test_construction\', \'_test_elements\']); S
        Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: Q0 = PolynomialRing(QQ,[]); TestSuite(Q0).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\', \'_test_gcd_vs_xgcd\', \'_test_quo_rem\']); Q0
        Multivariate Polynomial Ring in no variables over Rational Field
        sage: P.<x> = PolynomialRing(QQ, implementation=\'singular\'); TestSuite(P).run(skip=[\'_test_construction\', \'_test_elements\',                             # needs sage.libs.singular
        ....:                                                                               \'_test_euclidean_degree\', \'_test_quo_rem\']); P
        Multivariate Polynomial Ring in x over Rational Field
        sage: Q1 = PolynomialRing(QQ,"x",1); TestSuite(Q1).run(skip=[\'_test_construction\', \'_test_elements\', \'_test_euclidean_degree\', \'_test_quo_rem\']); Q1
        Multivariate Polynomial Ring in x over Rational Field
        sage: Q0 = PolynomialRing(QQ,"x",0); TestSuite(Q0).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\', \'_test_gcd_vs_xgcd\', \'_test_quo_rem\']); Q0
        Multivariate Polynomial Ring in no variables over Rational Field
        sage: R = PolynomialRing(GF(2), \'j\', implementation=\'generic\'); TestSuite(R).run(skip=[\'_test_construction\', \'_test_pickling\']); type(R)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category\'>
        sage: S = PolynomialRing(GF(2), \'j\'); TestSuite(S).run(); type(S)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_mod_p_with_category\'>
        sage: R = PolynomialRing(ZZ, \'x,y\', implementation=\'generic\'); TestSuite(R).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\']); type(R)
        <class \'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain_with_category\'>
        sage: S = PolynomialRing(ZZ, \'x,y\'); TestSuite(S).run(skip=\'_test_elements\'); type(S)       # needs sage.libs.singular
        <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular\'>
        sage: R = PolynomialRing(ZZ, \'j\', sparse=True); TestSuite(R).run(); type(R)
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain_with_category\'>
        sage: R = PolynomialRing(GF(49), \'j\', sparse=True); TestSuite(R).run(); type(R)             # needs sage.rings.finite_rings
        <class \'sage.rings.polynomial.polynomial_ring.PolynomialRing_field_with_category\'>

        sage: # needs sage.rings.real_interval_field
        sage: P.<y,z> = PolynomialRing(RealIntervalField(2))
        sage: TestSuite(P).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\'])
        sage: Q.<x> = PolynomialRing(P)
        sage: TestSuite(Q).run(skip=[\'_test_additive_associativity\', \'_test_associativity\',
        ....:                        \'_test_distributivity\', \'_test_prod\'])
        sage: R.<x,y> = PolynomialRing(RIF,2)
        sage: TestSuite(R).run(skip=[\'_test_elements\', \'_test_elements_eq_transitive\'])

    We verify that multivariate polynomial rings over ``InfinityRing`` from
    :issue:`34675` are fixed::

        sage: PolynomialRing(InfinityRing, 2, \'x\')
        Multivariate Polynomial Ring in x0, x1 over The Infinity Ring
    '''
def unpickle_PolynomialRing(base_ring, arg1=None, arg2=None, sparse: bool = False):
    """
    Custom unpickling function for polynomial rings.

    This has the same positional arguments as the old
    ``PolynomialRing`` constructor before :issue:`23338`.
    """
@weak_cached_function
def polynomial_default_category(base_ring_category, n_variables):
    """
    Choose an appropriate category for a polynomial ring.

    It is assumed that the corresponding base ring is nonzero.

    INPUT:

    - ``base_ring_category`` -- the category of ring over which the polynomial
      ring shall be defined
    - ``n_variables`` -- number of variables

    EXAMPLES::

        sage: from sage.rings.polynomial.polynomial_ring_constructor import polynomial_default_category
        sage: polynomial_default_category(Rings(), 1)
        Category of infinite algebras with basis over rings
        sage: polynomial_default_category(Rings().Commutative(), 1)
        Category of infinite commutative algebras with basis
            over commutative rings
        sage: polynomial_default_category(Fields(), 1)
        Join of Category of euclidean domains
            and Category of algebras with basis over fields
            and Category of commutative algebras over fields
            and Category of infinite sets
        sage: polynomial_default_category(Fields(), 2)
        Join of Category of unique factorization domains
            and Category of algebras with basis over fields
            and Category of commutative algebras over fields
            and Category of infinite sets

        sage: QQ['t'].category() is EuclideanDomains() & CommutativeAlgebras(QQ.category()).WithBasis().Infinite()
        True
        sage: QQ['s','t'].category() is UniqueFactorizationDomains() & CommutativeAlgebras(QQ.category()).WithBasis().Infinite()
        True
        sage: QQ['s']['t'].category() is UniqueFactorizationDomains() & CommutativeAlgebras(QQ['s'].category()).WithBasis().Infinite()
        True
    """
def BooleanPolynomialRing_constructor(n=None, names=None, order: str = 'lex'):
    """
    Construct a boolean polynomial ring with the following
    parameters:

    INPUT:

    - ``n`` -- number of variables (an integer > 1)
    - ``names`` -- names of ring variables, may be a string or list/tuple of strings
    - ``order`` -- term order (default: ``'lex'``)

    EXAMPLES::

        sage: # needs sage.rings.polynomial.pbori
        sage: R.<x, y, z> = BooleanPolynomialRing(); R  # indirect doctest
        Boolean PolynomialRing in x, y, z
        sage: p = x*y + x*z + y*z
        sage: x*p
        x*y*z + x*y + x*z
        sage: R.term_order()
        Lexicographic term order

        sage: R = BooleanPolynomialRing(5, 'x', order='deglex(3),deglex(2)')            # needs sage.rings.polynomial.pbori
        sage: R.term_order()                                                            # needs sage.rings.polynomial.pbori
        Block term order with blocks:
        (Degree lexicographic term order of length 3,
         Degree lexicographic term order of length 2)

        sage: R = BooleanPolynomialRing(3, 'x', order='degneglex')                      # needs sage.rings.polynomial.pbori
        sage: R.term_order()                                                            # needs sage.rings.polynomial.pbori
        Degree negative lexicographic term order

        sage: BooleanPolynomialRing(names=('x','y'))                                    # needs sage.rings.polynomial.pbori
        Boolean PolynomialRing in x, y

        sage: BooleanPolynomialRing(names='x,y')                                        # needs sage.rings.polynomial.pbori
        Boolean PolynomialRing in x, y

    TESTS::

        sage: P.<x,y> = BooleanPolynomialRing(2, order='deglex')                        # needs sage.rings.polynomial.pbori
        sage: x > y                                                                     # needs sage.rings.polynomial.pbori
        True

        sage: # needs sage.rings.polynomial.pbori
        sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4, order='deglex(2),deglex(2)')
        sage: x0 > x1
        True
        sage: x2 > x3
        True
    """
