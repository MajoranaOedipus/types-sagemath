from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Matrix as Matrix, MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal

class AffineGroupElement(MultiplicativeGroupElement):
    """
    An affine group element.

    INPUT:

    - ``A`` -- an invertible matrix, or something defining a
      matrix if ``convert==True``

    - ``b`` -- a vector, or something defining a vector if
      ``convert==True`` (default: ``0``, defining the zero
      vector)

    - ``parent`` -- the parent affine group

    - ``convert`` -- boolean (default: ``True``); whether to convert
      ``A`` into the correct matrix space and ``b`` into the
      correct vector space

    - ``check`` -- boolean (default: ``True``); whether to do some
      checks or just accept the input as valid

    As a special case, ``A`` can be a matrix obtained from
    :meth:`matrix`, that is, one row and one column larger. In
    that case, the group element defining that matrix is
    reconstructed.

    OUTPUT: the affine group element `x \\mapsto Ax + b`

    EXAMPLES::

        sage: G = AffineGroup(2, GF(3))

        sage: # needs sage.libs.gap
        sage: g = G.random_element()
        sage: type(g)
        <class 'sage.groups.affine_gps.affine_group.AffineGroup_with_category.element_class'>
        sage: G(g.matrix()) == g
        True

        sage: G(2)
              [2 0]     [0]
        x |-> [0 2] x + [0]

    Conversion from a matrix and a matrix group element::

        sage: M = Matrix(4, 4, [0, 0, -1, 1, 0, -1, 0, 1, -1, 0, 0, 1, 0, 0, 0, 1])
        sage: A = AffineGroup(3, ZZ)
        sage: A(M)
              [ 0  0 -1]     [1]
        x |-> [ 0 -1  0] x + [1]
              [-1  0  0]     [1]
        sage: G = MatrixGroup([M])
        sage: A(G.0)
              [ 0  0 -1]     [1]
        x |-> [ 0 -1  0] x + [1]
              [-1  0  0]     [1]
    """
    def __init__(self, parent, A, b: int = 0, convert: bool = True, check: bool = True) -> None:
        """
        Create element of an affine group.

        TESTS::

            sage: # needs sage.libs.gap
            sage: G = AffineGroup(4, GF(5))
            sage: g = G.random_element()
            sage: TestSuite(g).run()
        """
    def A(self):
        """
        Return the general linear part of an affine group element.

        OUTPUT: the matrix `A` of the affine group element `Ax + b`

        EXAMPLES::

            sage: G = AffineGroup(3, QQ)
            sage: g = G([1,2,3,4,5,6,7,8,0], [10,11,12])
            sage: A = g.A(); A
            [1 2 3]
            [4 5 6]
            [7 8 0]
            sage: A.is_immutable()
            True
        """
    def b(self):
        """
        Return the translation part of an affine group element.

        OUTPUT: the vector `b` of the affine group element `Ax + b`

        EXAMPLES::

            sage: G = AffineGroup(3, QQ)
            sage: g = G([1,2,3,4,5,6,7,8,0], [10,11,12])
            sage: b = g.b(); b
            (10, 11, 12)
            sage: b.is_immutable()
            True
        """
    @cached_method
    def matrix(self):
        """
        Return the standard matrix representation of ``self``.

        .. SEEALSO::

            - :meth:`AffineGroup.linear_space()`

        EXAMPLES::

            sage: G = AffineGroup(3, GF(7))
            sage: g = G([1,2,3,4,5,6,7,8,0], [10,11,12])
            sage: g
                  [1 2 3]     [3]
            x |-> [4 5 6] x + [4]
                  [0 1 0]     [5]
            sage: g.matrix()
            [1 2 3|3]
            [4 5 6|4]
            [0 1 0|5]
            [-----+-]
            [0 0 0|1]
            sage: parent(g.matrix())
            Full MatrixSpace of 4 by 4 dense matrices over Finite Field of size 7
            sage: g.matrix() == matrix(g)
            True

        Composition of affine group elements equals multiplication of
        the matrices::

            sage: # needs sage.libs.gap
            sage: g1 = G.random_element()
            sage: g2 = G.random_element()
            sage: g1.matrix() * g2.matrix() == (g1*g2).matrix()
            True
        """
    def __call__(self, v):
        """
        Apply the affine transformation to ``v``.

        INPUT:

        - ``v`` -- a polynomial, a multivariate polynomial, a polyhedron, a
          vector, or anything that can be converted into a vector

        OUTPUT: the image of ``v`` under the affine group element

        EXAMPLES::

            sage: G = AffineGroup(2, QQ)
            sage: g = G([0,1,-1,0],[2,3]);  g
                  [ 0  1]     [2]
            x |-> [-1  0] x + [3]
            sage: v = vector([4,5])
            sage: g(v)
            (7, -1)

            sage: R.<x,y> = QQ[]
            sage: g(x), g(y)
            (y + 2, -x + 3)
            sage: p = x^2 + 2*x*y + y + 1
            sage: g(p)
            -2*x*y + y^2 - 5*x + 10*y + 20

        The action on polynomials is such that it intertwines with
        evaluation. That is::

            sage: p(*g(v)) == g(p)(*v)
            True

        Test that the univariate polynomial ring is covered::

            sage: H = AffineGroup(1, QQ)
            sage: h = H([2],[3]);  h
            x |-> [2] x + [3]
            sage: R.<z> = QQ[]
            sage: h(z+1)
            3*z + 2

        The action on a polyhedron is defined (see :issue:`30327`)::

            sage: F = AffineGroup(3, QQ)
            sage: M = matrix(3, [-1, -2, 0, 0, 0, 1, -2, 1, -1])
            sage: v = vector(QQ,(1,2,3))
            sage: f = F(M, v)
            sage: cube = polytopes.cube()                                               # needs sage.geometry.polyhedron
            sage: f(cube)                                                               # needs sage.geometry.polyhedron
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 8 vertices
        """
    def __invert__(self):
        """
        Return the inverse group element.

        OUTPUT: another affine group element

        EXAMPLES::

            sage: G = AffineGroup(2, GF(3))
            sage: g = G([1,2,3,4], [5,6])
            sage: g
                  [1 2]     [2]
            x |-> [0 1] x + [0]
            sage: ~g
                  [1 1]     [1]
            x |-> [0 1] x + [0]
            sage: g * g.inverse()   # indirect doctest
                  [1 0]     [0]
            x |-> [0 1] x + [0]
            sage: g * g.inverse() == g.inverse() * g == G(1)
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        OUTPUT: int

        EXAMPLES::

            sage: F = AffineGroup(3, QQ)
            sage: g = F([1,2,3,4,5,6,7,8,0], [10,11,12])
            sage: h = F([1,2,3,4,5,6,7,8,0], [10,11,0])
            sage: hash(g) == hash(h)
            False
            sage: hash(g) == hash(copy(g))
            True
            sage: f = g * h
            sage: hash(f) == hash(~f)
            False
        """
    def list(self):
        """
        Return list representation of ``self``.

        EXAMPLES::

            sage: F = AffineGroup(3, QQ)
            sage: g = F([1,2,3,4,5,6,7,8,0], [10,11,12])
            sage: g
                  [1 2 3]     [10]
            x |-> [4 5 6] x + [11]
                  [7 8 0]     [12]
            sage: g.matrix()
            [ 1  2  3|10]
            [ 4  5  6|11]
            [ 7  8  0|12]
            [--------+--]
            [ 0  0  0| 1]
            sage: g.list()
            [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 0, 12], [0, 0, 0, 1]]
        """
