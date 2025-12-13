from _typeshed import Incomplete
from sage.categories.monoids import Monoids as Monoids
from sage.categories.morphism import Morphism as Morphism
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import MonoidElement as MonoidElement
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Sigma0ActionAdjuster(UniqueRepresentation):
    @abstract_method
    def __call__(self, x) -> None:
        """
        Given a :class:`Sigma0element` ``x``, return four integers.

        This is used to allow for other conventions for the action of Sigma0
        on the space of distributions.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import _default_adjuster
            sage: A = _default_adjuster()
            sage: A(matrix(ZZ, 2, [3,4,5,6])) # indirect doctest
            (3, 4, 5, 6)
        """

class _default_adjuster(Sigma0ActionAdjuster):
    """
    A callable object that does nothing to a matrix, returning its entries
    in the natural, by-row, order.

    INPUT:

    - ``g`` -- a `2 \times 2` matrix

    OUTPUT: a 4-tuple consisting of the entries of the matrix

    EXAMPLES::

        sage: A = sage.modular.pollack_stevens.sigma0._default_adjuster(); A
        <sage.modular.pollack_stevens.sigma0._default_adjuster object at 0x...>
        sage: TestSuite(A).run()
    """
    def __call__(self, g):
        """
        EXAMPLES::

            sage: T = sage.modular.pollack_stevens.sigma0._default_adjuster()
            sage: T(matrix(ZZ,2,[1..4])) # indirect doctest
            (1, 2, 3, 4)
        """

class Sigma0_factory(UniqueFactory):
    """
    Create the monoid of non-singular matrices, upper triangular mod `N`.

    INPUT:

    - ``N`` -- integer; the level (should be strictly positive)
    - ``base_ring`` (commutative ring, default `\\ZZ`) -- the base
      ring (normally `\\ZZ` or a `p`-adic ring)
    - ``adjuster`` -- ``None``, or a callable which takes a `2 \\times 2` matrix
      and returns a 4-tuple of integers. This is supplied in order to support
      differing conventions for the action of `2 \\times 2` matrices on
      distributions.

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
        sage: Sigma0(3)
        Monoid Sigma0(3) with coefficients in Integer Ring
    """
    def create_key(self, N, base_ring=..., adjuster=None):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: Sigma0.create_key(3)
            (3, Integer Ring, <sage.modular.pollack_stevens.sigma0._default_adjuster object at 0x...>)
            sage: TestSuite(Sigma0).run()
        """
    def create_object(self, version, key):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: Sigma0(3) # indirect doctest
            Monoid Sigma0(3) with coefficients in Integer Ring
        """

Sigma0: Incomplete

class Sigma0Element(MonoidElement):
    """
    An element of the monoid Sigma0. This is a wrapper around a `2 \\times 2` matrix.

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
        sage: S = Sigma0(7)
        sage: g = S([2,3,7,1])
        sage: g.det()
        -19
        sage: h = S([1,2,0,1])
        sage: g * h
        [ 2  7]
        [ 7 15]
        sage: g.inverse()
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
        sage: h.inverse()
        [ 1 -2]
        [ 0  1]
    """
    def __init__(self, parent, mat) -> None:
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: s = Sigma0(3)([1,4,3,3]) # indirect doctest
            sage: TestSuite(s).run()
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: s = Sigma0(3)([1,4,3,3])
            sage: hash(s) # indirect doctest
            8095169151987216923  # 64-bit
            619049499            # 32-bit
        """
    def det(self):
        """
        Return the determinant of this matrix, which is (by assumption) nonzero.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: s = Sigma0(3)([1,4,3,3])
            sage: s.det()
            -9
        """
    def matrix(self):
        """
        Return ``self`` as a matrix (forgetting the additional data that it is
        in ``Sigma0(N)``).

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: s = Sigma0(3)([1,4,3,3])
            sage: sm = s.matrix()
            sage: type(s)
            <class 'sage.modular.pollack_stevens.sigma0.Sigma0_class_with_category.element_class'>
            sage: type(sm)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: s == sm
            True
        """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        This will raise an error if the result is not in the monoid.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: s = Sigma0(3)([1,4,3,13])
            sage: s.inverse()    # indirect doctest
            [13 -4]
            [-3  1]
            sage: Sigma0(3)([1, 0, 0, 3]).inverse()
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        .. TODO::

            In an ideal world this would silently extend scalars to `\\QQ` if
            the inverse has non-integer entries but is still in `\\Sigma_0(N)`
            locally at `N`. But we do not use such functionality, anyway.
        """

class _Sigma0Embedding(Morphism):
    '''
    A Morphism object giving the natural inclusion of `\\Sigma_0` into the
    appropriate matrix space. This snippet of code is fed to the coercion
    framework so that "x * y" will work if ``x`` is a matrix and ``y`` is a `\\Sigma_0`
    element (returning a matrix, *not* a Sigma0 element).
    '''
    def __init__(self, domain) -> None:
        """
        TESTS::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0, _Sigma0Embedding
            sage: x = _Sigma0Embedding(Sigma0(3))
            sage: TestSuite(x).run(skip=['_test_category'])

        # TODO: The category test breaks because _Sigma0Embedding is not an instance of
        # the element class of its parent (a homset in the category of
        # monoids). I have no idea how to fix this.
        """

class Sigma0_class(Parent):
    """
    The class representing the monoid `\\Sigma_0(N)`.

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
        sage: S = Sigma0(5); S
        Monoid Sigma0(5) with coefficients in Integer Ring
        sage: S([1,2,1,1])
        Traceback (most recent call last):
        ...
        TypeError: level 5^1 does not divide 1
        sage: S([1,2,5,1])
        [1 2]
        [5 1]
    """
    Element = Sigma0Element
    def __init__(self, N, base_ring, adjuster) -> None:
        """
        Standard init function. For args documentation see the factory
        function.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: S = Sigma0(3) # indirect doctest
            sage: TestSuite(S).run()
        """
    def level(self):
        """
        If this monoid is `\\Sigma_0(N)`, return `N`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: S = Sigma0(3)
            sage: S.level()
            3
        """
    def base_ring(self):
        """
        Return the base ring.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: S = Sigma0(3)
            sage: S.base_ring()
            Integer Ring
        """
