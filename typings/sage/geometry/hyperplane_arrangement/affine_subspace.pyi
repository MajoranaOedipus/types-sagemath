from sage.matrix.constructor import vector as vector
from sage.structure.sage_object import SageObject as SageObject

class AffineSubspace(SageObject):
    """
    An affine subspace.

    INPUT:

    - ``p`` -- list/tuple/iterable representing a point on the
      affine space

    - ``V`` -- vector subspace

    OUTPUT: affine subspace parallel to ``V`` and passing through ``p``

    EXAMPLES::

        sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
        sage: a = AffineSubspace([1,0,0,0], VectorSpace(QQ,4))
        sage: a
        Affine space p + W where:
          p = (1, 0, 0, 0)
          W = Vector space of dimension 4 over Rational Field
    """
    def __init__(self, p, V) -> None:
        """
        Construct an :class:`AffineSubspace`.

        TESTS::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0,0], VectorSpace(QQ,4))
            sage: TestSuite(a).run()
            sage: AffineSubspace(0, VectorSpace(QQ,4)).point()
            (0, 0, 0, 0)
        """
    def __hash__(self):
        """
        Return a hash value.

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0,0], VectorSpace(QQ,4))
            sage: a.__hash__()    # random output
            -3713096828371451969
        """
    def __eq__(self, other):
        """
        Test whether ``self`` is equal to ``other``.

        INPUT:

        - ``other`` -- an :class:`AffineSubspace`

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0], matrix([[1,0,0]]).right_kernel())
            sage: b = AffineSubspace([2,0,0], matrix([[1,0,0]]).right_kernel())
            sage: c = AffineSubspace([1,1,0], matrix([[1,0,0]]).right_kernel())
            sage: a == b
            False
            sage: a == c
            True
        """
    def __ne__(self, other):
        """
        Test whether ``self`` is not equal to ``other``.

        INPUT:

        - ``other`` -- an :class:`AffineSubspace`

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0],matrix([[1,0,0]]).right_kernel())
            sage: b = AffineSubspace([2,0,0],matrix([[1,0,0]]).right_kernel())
            sage: a == b
            False
            sage: a != b
            True
            sage: a != a
            False
        """
    def __le__(self, other):
        """
        Test whether ``self`` is an affine subspace of ``other``.

        INPUT:

        - ``other`` -- an :class:`AffineSubspace`

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: V = VectorSpace(QQ, 3)
            sage: W1 = V.subspace([[1,0,0],[0,1,0]])
            sage: W2 = V.subspace([[1,0,0]])
            sage: a = AffineSubspace([1,2,3], W1)
            sage: b = AffineSubspace([1,2,3], W2)
            sage: a <= b
            False
            sage: a <= a
            True
            sage: b <= a
            True
        """
    def __lt__(self, other):
        """
        Test whether ``self`` is a proper affine subspace of ``other``.

        INPUT:

        - ``other`` -- an :class:`AffineSubspace`

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: V = VectorSpace(QQ, 3)
            sage: W1 = V.subspace([[1,0,0], [0,1,0]])
            sage: W2 = V.subspace([[1,0,0]])
            sage: a = AffineSubspace([1,2,3], W1)
            sage: b = AffineSubspace([1,2,3], W2)
            sage: a < b
            False
            sage: a < a
            False
            sage: b < a
            True
        """
    def __contains__(self, q) -> bool:
        """
        Test whether the point ``q`` is in the affine space.

        INPUT:

        - ``q`` -- point as a list/tuple/iterable

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0], matrix([[1,0,0]]).right_kernel())
            sage: (1,1,0) in a
            True
            sage: (0,0,0) in a
            False
        """
    def linear_part(self):
        """
        Return the linear part of the affine space.

        OUTPUT: a vector subspace of the ambient space

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: A = AffineSubspace([2,3,1], matrix(QQ, [[1,2,3]]).right_kernel())
            sage: A.linear_part()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0 -1/3]
            [   0    1 -2/3]
            sage: A.linear_part().ambient_vector_space()
            Vector space of dimension 3 over Rational Field
        """
    def point(self):
        """
        Return a point ``p`` in the affine space.

        OUTPUT: a point of the affine space as a vector in the ambient space

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: A = AffineSubspace([2,3,1], VectorSpace(QQ,3))
            sage: A.point()
            (2, 3, 1)
        """
    def dimension(self):
        """
        Return the dimension of the affine space.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: a = AffineSubspace([1,0,0,0],VectorSpace(QQ,4))
            sage: a.dimension()
            4
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` with ``other``.

        INPUT:

        - ``other`` -- an :class:`AffineSubspace`

        OUTPUT:

        A new affine subspace, (or ``None`` if the intersection is
        empty).

        EXAMPLES::

            sage: from sage.geometry.hyperplane_arrangement.affine_subspace import AffineSubspace
            sage: V = VectorSpace(QQ,3)
            sage: U = V.subspace([(1,0,0), (0,1,0)])
            sage: W = V.subspace([(0,1,0), (0,0,1)])
            sage: A = AffineSubspace((0,0,0), U)
            sage: B = AffineSubspace((1,1,1), W)
            sage: A.intersection(B)
            Affine space p + W where:
              p = (1, 1, 0)
              W = Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [0 1 0]
            sage: C = AffineSubspace((0,0,1), U)
            sage: A.intersection(C)
            sage: C = AffineSubspace((7,8,9), U.complement())
            sage: A.intersection(C)
            Affine space p + W where:
              p = (7, 8, 0)
              W = Vector space of degree 3 and dimension 0 over Rational Field
            Basis matrix:
            []
            sage: A.intersection(C).intersection(B)

            sage: D = AffineSubspace([1,2,3], VectorSpace(GF(5),3))
            sage: E = AffineSubspace([3,4,5], VectorSpace(GF(5),3))
            sage: D.intersection(E)
            Affine space p + W where:
              p = (3, 4, 0)
              W = Vector space of dimension 3 over Finite Field of size 5
        """
