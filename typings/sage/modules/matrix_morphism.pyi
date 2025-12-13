import sage.categories.morphism
from _typeshed import Incomplete
from sage.categories.finite_dimensional_modules_with_basis import FiniteDimensionalModulesWithBasis as FiniteDimensionalModulesWithBasis
from sage.structure.all import Sequence as Sequence, parent as parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp

def is_MatrixMorphism(x):
    """
    Return ``True`` if x is a Matrix morphism of free modules.

    This function is deprecated.

    EXAMPLES::

        sage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])
        sage: sage.modules.matrix_morphism.is_MatrixMorphism(phi)
        doctest:warning...
        DeprecationWarning: is_MatrixMorphism is deprecated;
        use isinstance(..., MatrixMorphism_abstract) or categories instead
        See https://github.com/sagemath/sage/issues/37731 for details.
        True
        sage: sage.modules.matrix_morphism.is_MatrixMorphism(3)
        False
    """

class MatrixMorphism_abstract(sage.categories.morphism.Morphism):
    characteristic_polynomial: Incomplete
    charpoly: Incomplete
    det: Incomplete
    determinant: Incomplete
    fcp: Incomplete
    trace: Incomplete
    def __init__(self, parent, side: str = 'left') -> None:
        """
        INPUT:

        - ``parent`` -- a homspace

        - ``A`` -- matrix

        EXAMPLES::

            sage: from sage.modules.matrix_morphism import MatrixMorphism
            sage: T = End(ZZ^3)
            sage: M = MatrixSpace(ZZ,3)
            sage: I = M.identity_matrix()
            sage: A = MatrixMorphism(T, I)
            sage: loads(A.dumps()) == A
            True
        """
    def __invert__(self):
        """
        Invert this matrix morphism.

        EXAMPLES::

            sage: V = QQ^2; phi = V.hom([3*V.0, 2*V.1])
            sage: phi^(-1)
            Vector space morphism represented by the matrix:
            [1/3   0]
            [  0 1/2]
            Domain: Vector space of dimension 2 over Rational Field
            Codomain: Vector space of dimension 2 over Rational Field

        Check that a certain non-invertible morphism isn't invertible::

            sage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])
            sage: phi^(-1)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: matrix morphism not invertible
        """
    def side(self):
        """
        Return the side of vectors acted on, relative to the matrix.

        EXAMPLES::

            sage: m = matrix(2, [1, 1, 0, 1])
            sage: V = ZZ^2
            sage: h1 = V.hom(m); h2 = V.hom(m, side='right')
            sage: h1.side()
            'left'
            sage: h1([1, 0])
            (1, 1)
            sage: h2.side()
            'right'
            sage: h2([1, 0])
            (1, 0)
        """
    def side_switch(self):
        """
        Return the same morphism, acting on vectors on the opposite side.

        EXAMPLES::

            sage: m = matrix(2, [1,1,0,1]); m
            [1 1]
            [0 1]
            sage: V = ZZ^2
            sage: h = V.hom(m); h.side()
            'left'
            sage: h2 = h.side_switch(); h2
            Free module morphism defined as left-multiplication by the matrix
            [1 0]
            [1 1]
            Domain: Ambient free module of rank 2 over the principal ideal domain Integer Ring
            Codomain: Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: h2.side()
            'right'
            sage: h2.side_switch().matrix()
            [1 1]
            [0 1]
        """
    def inverse(self):
        '''
        Return the inverse of this matrix morphism, if the inverse exists.

        This raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        EXAMPLES:

        An invertible morphism created as a restriction of
        a non-invertible morphism, and which has an unequal
        domain and codomain.  ::

            sage: V = QQ^4
            sage: W = QQ^3
            sage: m = matrix(QQ, [[2, 0, 3], [-6, 1, 4], [1, 2, -4], [1, 0, 1]])
            sage: phi = V.hom(m, W)
            sage: rho = phi.restrict_domain(V.span([V.0, V.3]))
            sage: zeta = rho.restrict_codomain(W.span([W.0, W.2]))
            sage: x = vector(QQ, [2, 0, 0, -7])
            sage: y = zeta(x); y
            (-3, 0, -1)
            sage: inv = zeta.inverse(); inv
            Vector space morphism represented by the matrix:
            [-1  3]
            [ 1 -2]
            Domain: Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0]
            [0 0 1]
            Codomain: Vector space of degree 4 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0 0]
            [0 0 0 1]
            sage: inv(y) == x
            True

        An example of an invertible morphism between modules,
        (rather than between vector spaces).  ::

            sage: M = ZZ^4
            sage: p = matrix(ZZ, [[ 0, -1,  1, -2],
            ....:                 [ 1, -3,  2, -3],
            ....:                 [ 0,  4, -3,  4],
            ....:                 [-2,  8, -4,  3]])
            sage: phi = M.hom(p, M)
            sage: x = vector(ZZ, [1, -3, 5, -2])
            sage: y = phi(x); y
            (1, 12, -12, 21)
            sage: rho = phi.inverse(); rho
            Free module morphism defined by the matrix
            [ -5   3  -1   1]
            [ -9   4  -3   2]
            [-20   8  -7   4]
            [ -6   2  -2   1]
            Domain: Ambient free module of rank 4 over the principal ideal domain ...
            Codomain: Ambient free module of rank 4 over the principal ideal domain ...
            sage: rho(y) == x
            True

        A non-invertible morphism, despite having an appropriate
        domain and codomain.  ::

            sage: V = QQ^2
            sage: m = matrix(QQ, [[1, 2], [20, 40]])
            sage: phi = V.hom(m, V)
            sage: phi.is_bijective()
            False
            sage: phi.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: matrix morphism not invertible

        The matrix representation of this morphism is invertible
        over the rationals, but not over the integers, thus the
        morphism is not invertible as a map between modules.
        It is easy to notice from the definition that every
        vector of the image will have a second entry that
        is an even integer.  ::

            sage: V = ZZ^2
            sage: q = matrix(ZZ, [[1, 2], [3, 4]])
            sage: phi = V.hom(q, V)
            sage: phi.matrix().change_ring(QQ).inverse()
            [  -2    1]
            [ 3/2 -1/2]
            sage: phi.is_bijective()
            False
            sage: phi.image()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1 0]
            [0 2]
            sage: phi.lift(vector(ZZ, [1, 1]))
            Traceback (most recent call last):
            ...
            ValueError: element is not in the image
            sage: phi.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: matrix morphism not invertible

        The unary invert operator (~, tilde, "wiggle") is synonymous
        with the ``inverse()`` method (and a lot easier to type).  ::

            sage: V = QQ^2
            sage: r = matrix(QQ, [[4, 3], [-2, 5]])
            sage: phi = V.hom(r, V)
            sage: rho = phi.inverse()
            sage: zeta = ~phi
            sage: rho.is_equal_function(zeta)
            True

        TESTS::

            sage: V = QQ^2
            sage: W = QQ^3
            sage: U = W.span([W.0, W.1])
            sage: m = matrix(QQ, [[2, 1], [3, 4]])
            sage: phi = V.hom(m, U)
            sage: inv = phi.inverse()
            sage: (inv*phi).is_identity()
            True
            sage: (phi*inv).is_identity()
            True
        '''
    def __rmul__(self, left):
        """
        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([V.0+V.1, 2*V.1])
            sage: 2*phi
            Free module morphism defined by the matrix
            [2 2]
            [0 4]...
            sage: phi*2
            Free module morphism defined by the matrix
            [2 2]
            [0 4]...
        """
    def __mul__(self, right):
        """
        Composition of morphisms, denoted by \\*.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([V.0+V.1, 2*V.1])
            sage: phi*phi
            Free module morphism defined by the matrix
            [1 3]
            [0 4]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...

            sage: V = QQ^3
            sage: E = V.endomorphism_ring()
            sage: phi = E(Matrix(QQ,3,range(9))) ; phi
            Vector space morphism represented by the matrix:
            [0 1 2]
            [3 4 5]
            [6 7 8]
            Domain: Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 3 over Rational Field
            sage: phi*phi
            Vector space morphism represented by the matrix:
            [ 15  18  21]
            [ 42  54  66]
            [ 69  90 111]
            Domain: Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 3 over Rational Field
            sage: phi.matrix()**2
            [ 15  18  21]
            [ 42  54  66]
            [ 69  90 111]

        ::

            sage: W = QQ**4
            sage: E_VW = V.Hom(W)
            sage: psi = E_VW(Matrix(QQ,3,4,range(12))) ; psi
            Vector space morphism represented by the matrix:
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            Domain: Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 4 over Rational Field
            sage: psi*phi
            Vector space morphism represented by the matrix:
            [ 20  23  26  29]
            [ 56  68  80  92]
            [ 92 113 134 155]
            Domain: Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 4 over Rational Field
            sage: phi*psi
            Traceback (most recent call last):
            ...
            TypeError: Incompatible composition of morphisms: domain of left morphism must be codomain of right.
            sage: phi.matrix()*psi.matrix()
            [ 20  23  26  29]
            [ 56  68  80  92]
            [ 92 113 134 155]

        Composite maps can be formed with matrix morphisms::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: V, VtoK, KtoV = K.vector_space()
            sage: f = V.hom([V.0 - V.1, V.0 + V.1])*KtoV; f
            Composite map:
            From: Number Field in a with defining polynomial x^2 + 23
            To:   Vector space of dimension 2 over Rational Field
            Defn:   Isomorphism map:
                    From: Number Field in a with defining polynomial x^2 + 23
                    To:   Vector space of dimension 2 over Rational Field
                    then
                    Vector space morphism represented by the matrix:
                    [ 1 -1]
                    [ 1  1]
                    Domain: Vector space of dimension 2 over Rational Field
                    Codomain: Vector space of dimension 2 over Rational Field
            sage: f(a)
            (1, 1)
            sage: V.hom([V.0 - V.1, V.0 + V.1], side='right')*KtoV
            Composite map:
              From: Number Field in a with defining polynomial x^2 + 23
              To:   Vector space of dimension 2 over Rational Field
              Defn:   Isomorphism map:
                      From: Number Field in a with defining polynomial x^2 + 23
                      To:   Vector space of dimension 2 over Rational Field
                    then
                      Vector space morphism represented as left-multiplication by the matrix:
                    [ 1  1]
                    [-1  1]
                    Domain: Vector space of dimension 2 over Rational Field
                    Codomain: Vector space of dimension 2 over Rational Field


        We can test interaction between morphisms with different ``side``::

            sage: V = ZZ^2
            sage: m = matrix(2, [1,1,0,1])
            sage: hl = V.hom(m)
            sage: hr = V.hom(m, side='right')
            sage: hl * hl
            Free module morphism defined by the matrix
            [1 2]
            [0 1]...
            sage: hl * hr
            Free module morphism defined by the matrix
            [1 1]
            [1 2]...
            sage: hl * hl.side_switch()
            Free module morphism defined by the matrix
            [1 2]
            [0 1]...
            sage: hr * hl
            Free module morphism defined by the matrix
            [2 1]
            [1 1]...
            sage: hl * hl
            Free module morphism defined by the matrix
            [1 2]
            [0 1]...
            sage: hr / hl
            Free module morphism defined by the matrix
            [ 0 -1]
            [ 1  1]...
            sage: hr / hr.side_switch()
            Free module morphism defined by the matrix
            [1 0]
            [0 1]...
            sage: hl / hl
            Free module morphism defined by the matrix
            [1 0]
            [0 1]...
            sage: hr / hr
            Free module morphism defined as left-multiplication by the matrix
            [1 0]
            [0 1]...

        .. WARNING::

            Matrix morphisms can be defined by either left or right-multiplication.
            The composite morphism always applies the morphism on the right of \\* first.
            The matrix of the composite morphism of two morphisms given by
            right-multiplication is not the morphism given by the product of their
            respective matrices.
            If the two morphisms act on different sides, then the side of the resulting
            morphism is the default one.
        """
    def __add__(self, right):
        """
        Sum of morphisms, denoted by +.

        EXAMPLES::

            sage: phi = (ZZ**2).endomorphism_ring()(Matrix(ZZ,2,[2..5])) ; phi
            Free module morphism defined by the matrix
            [2 3]
            [4 5]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...
            sage: phi + 3
            Free module morphism defined by the matrix
            [5 3]
            [4 8]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...
            sage: phi + phi
            Free module morphism defined by the matrix
            [ 4  6]
            [ 8 10]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...
            sage: psi = (ZZ**3).endomorphism_ring()(Matrix(ZZ,3,[22..30])) ; psi
            Free module morphism defined by the matrix
            [22 23 24]
            [25 26 27]
            [28 29 30]
            Domain: Ambient free module of rank 3 over the principal ideal domain ...
            Codomain: Ambient free module of rank 3 over the principal ideal domain ...
            sage: phi + psi
            Traceback (most recent call last):
            ...
            ValueError: inconsistent number of rows: should be 2 but got 3

        ::


            sage: V = ZZ^2
            sage: m = matrix(2, [1,1,0,1])
            sage: hl = V.hom(m)
            sage: hr = V.hom(m, side='right')
            sage: hl + hl
            Free module morphism defined by the matrix
            [2 2]
            [0 2]...
            sage: hr + hr
            Free module morphism defined as left-multiplication by the matrix
            [2 2]
            [0 2]...
            sage: hr + hl
            Free module morphism defined by the matrix
            [2 1]
            [1 2]...
            sage: hl + hr
            Free module morphism defined by the matrix
            [2 1]
            [1 2]...

        .. WARNING::

            If the two morphisms do not share the same ``side`` attribute, then
            the resulting morphism will be defined with the default value.
        """
    def __neg__(self):
        """
        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([V.0+V.1, 2*V.1])
            sage: -phi
            Free module morphism defined by the matrix
            [-1 -1]
            [ 0 -2]...
            sage: phi2 = phi.side_switch(); -phi2
            Free module morphism defined as left-multiplication by the matrix
            [-1  0]
            [-1 -2]...
        """
    def __sub__(self, other):
        """
        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([V.0+V.1, 2*V.1])
            sage: phi - phi
            Free module morphism defined by the matrix
            [0 0]
            [0 0]...

        ::

            sage: V = ZZ^2
            sage: m = matrix(2, [1,1,0,1])
            sage: hl = V.hom(m)
            sage: hr = V.hom(m, side='right')
            sage: hl - hr
            Free module morphism defined by the matrix
            [ 0  1]
            [-1  0]...
            sage: hl - hl
            Free module morphism defined by the matrix
            [0 0]
            [0 0]...
            sage: hr - hr
            Free module morphism defined as left-multiplication by the matrix
            [0 0]
            [0 0]...
            sage: hr-hl
            Free module morphism defined by the matrix
            [ 0 -1]
            [ 1  0]...

        .. WARNING::

            If the two morphisms do not share the same ``side`` attribute, then
            the resulting morphism will be defined with the default value.
        """
    def base_ring(self):
        """
        Return the base ring of ``self``, that is, the ring over which ``self``
        is given by a matrix.

        EXAMPLES::

            sage: sage.modules.matrix_morphism.MatrixMorphism((ZZ**2).endomorphism_ring(), Matrix(ZZ,2,[3..6])).base_ring()
            Integer Ring
        """
    def decomposition(self, *args, **kwds):
        """
        Return decomposition of this endomorphism, i.e., sequence of
        subspaces obtained by finding invariant subspaces of ``self``.

        See the documentation for ``self.matrix().decomposition`` for more
        details.  All inputs to this function are passed onto the
        matrix one.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([V.0+V.1, 2*V.1])
            sage: phi.decomposition()                                                   # needs sage.libs.pari
            [Free module of degree 2 and rank 1 over Integer Ring
             Echelon basis matrix:
             [0 1],
             Free module of degree 2 and rank 1 over Integer Ring
             Echelon basis matrix:
             [ 1 -1]]
            sage: phi2 = V.hom(phi.matrix(), side='right')
            sage: phi2.decomposition()                                                  # needs sage.libs.pari
            [Free module of degree 2 and rank 1 over Integer Ring
             Echelon basis matrix:
             [1 1],
             Free module of degree 2 and rank 1 over Integer Ring
             Echelon basis matrix:
             [1 0]]
        """
    def kernel(self):
        """
        Compute the kernel of this morphism.

        EXAMPLES::

            sage: V = VectorSpace(QQ, 3)
            sage: id = V.Hom(V)(identity_matrix(QQ,3))
            sage: null = V.Hom(V)(0*identity_matrix(QQ,3))
            sage: id.kernel()
            Vector space of degree 3 and dimension 0 over Rational Field
            Basis matrix:
            []
            sage: phi = V.Hom(V)(matrix(QQ, 3, range(9)))
            sage: phi.kernel()
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -2  1]
            sage: hom(CC^2, CC^2, matrix(CC, [[1,0], [0,1]])).kernel()
            Vector space of degree 2 and dimension 0 over Complex Field with 53 bits of precision
            Basis matrix:
            []
            sage: m = matrix(3, [1, 0, 0, 1, 0, 0, 0, 0, 1]); m
            [1 0 0]
            [1 0 0]
            [0 0 1]
            sage: f1 = V.hom(m)
            sage: f2 = V.hom(m, side='right')
            sage: f1.kernel()
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -1  0]
            sage: f2.kernel()
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [0 1 0]
        """
    def image(self):
        """
        Compute the image of this morphism.

        EXAMPLES::

            sage: V = VectorSpace(QQ, 3)
            sage: phi = V.Hom(V)(matrix(QQ, 3, range(9)))
            sage: phi.image()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [ 1  0 -1]
            [ 0  1  2]
            sage: hom(GF(7)^3, GF(7)^2, zero_matrix(GF(7), 3, 2)).image()
            Vector space of degree 2 and dimension 0 over Finite Field of size 7
            Basis matrix:
            []
            sage: m = matrix(3, [1, 0, 0, 1, 0, 0, 0, 0, 1]); m
            [1 0 0]
            [1 0 0]
            [0 0 1]
            sage: f1 = V.hom(m)
            sage: f2 = V.hom(m, side='right')
            sage: f1.image()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0]
            [0 0 1]
            sage: f2.image()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [1 1 0]
            [0 0 1]


        Compute the image of the identity map on a ZZ-submodule::

            sage: V = (ZZ^2).span([[1,2], [3,4]])
            sage: phi = V.Hom(V)(identity_matrix(ZZ,2))
            sage: phi(V.0) == V.0
            True
            sage: phi(V.1) == V.1
            True
            sage: phi.image()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1 0]
            [0 2]
            sage: phi.image() == V
            True
        """
    def matrix(self) -> None:
        """
        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom(V.basis())
            sage: phi.matrix()
            [1 0]
            [0 1]
            sage: sage.modules.matrix_morphism.MatrixMorphism_abstract.matrix(phi)
            Traceback (most recent call last):
            ...
            NotImplementedError: this method must be overridden in the extension class
        """
    def rank(self):
        """
        Return the rank of the matrix representing this morphism.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom(V.basis())
            sage: phi.rank()
            2
            sage: V = ZZ^2; phi = V.hom([V.0, V.0])
            sage: phi.rank()
            1
        """
    def nullity(self):
        """
        Return the nullity of the matrix representing this morphism, which is the
        dimension of its kernel.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom(V.basis())
            sage: phi.nullity()
            0
            sage: V = ZZ^2; phi = V.hom([V.0, V.0])
            sage: phi.nullity()
            1

        ::

            sage: m = matrix(2, [1, 2])
            sage: V = ZZ^2
            sage: h1 = V.hom(m)
            sage: h1.nullity()
            1
            sage: W = ZZ^1
            sage: h2 = W.hom(m, side='right')
            sage: h2.nullity()
            0
        """
    def is_bijective(self) -> bool:
        """
        Tell whether ``self`` is bijective.

        EXAMPLES:

        Two morphisms that are obviously not bijective, simply on
        considerations of the dimensions.  However, each fullfills
        half of the requirements to be a bijection.  ::

            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: m = matrix(QQ, [[1, 2, 3], [4, 5, 6]])
            sage: phi = V1.hom(m, V2)
            sage: phi.is_injective()
            True
            sage: phi.is_bijective()
            False
            sage: rho = V2.hom(m.transpose(), V1)
            sage: rho.is_surjective()
            True
            sage: rho.is_bijective()
            False

        We construct a simple bijection between two one-dimensional
        vector spaces.  ::

            sage: V1 = QQ^3
            sage: V2 = QQ^2
            sage: phi = V1.hom(matrix(QQ, [[1, 2], [3, 4], [5, 6]]), V2)
            sage: x = vector(QQ, [1, -1, 4])
            sage: y = phi(x); y
            (18, 22)
            sage: rho = phi.restrict_domain(V1.span([x]))
            sage: zeta = rho.restrict_codomain(V2.span([y]))
            sage: zeta.is_bijective()
            True

        AUTHOR:

        - Rob Beezer (2011-06-28)
        """
    def is_identity(self) -> bool:
        """
        Determine if this morphism is an identity function or not.

        EXAMPLES:

        A homomorphism that cannot possibly be the identity
        due to an unequal domain and codomain.  ::

            sage: V = QQ^3
            sage: W = QQ^2
            sage: m = matrix(QQ, [[1, 2], [3, 4], [5, 6]])
            sage: phi = V.hom(m, W)
            sage: phi.is_identity()
            False

        A bijection, but not the identity. ::

            sage: V = QQ^3
            sage: n = matrix(QQ, [[3, 1, -8], [5, -4, 6], [1, 1, -5]])
            sage: phi = V.hom(n, V)
            sage: phi.is_bijective()
            True
            sage: phi.is_identity()
            False

        A restriction that is the identity.  ::

            sage: V = QQ^3
            sage: p = matrix(QQ, [[1, 0, 0], [5, 8, 3], [0, 0, 1]])
            sage: phi = V.hom(p, V)
            sage: rho = phi.restrict(V.span([V.0, V.2]))
            sage: rho.is_identity()
            True

        An identity linear transformation that is defined with a
        domain and codomain with wildly different bases, so that the
        matrix representation is not simply the identity matrix. ::

            sage: A = matrix(QQ, [[1, 1, 0], [2, 3, -4], [2, 4, -7]])
            sage: B = matrix(QQ, [[2, 7, -2], [-1, -3, 1], [-1, -6, 2]])
            sage: U = (QQ^3).subspace_with_basis(A.rows())
            sage: V = (QQ^3).subspace_with_basis(B.rows())
            sage: H = Hom(U, V)
            sage: id = lambda x: x
            sage: phi = H(id)
            sage: phi([203, -179, 34])
            (203, -179, 34)
            sage: phi.matrix()
            [  1   0   1]
            [ -9 -18  -2]
            [-17 -31  -5]
            sage: phi.is_identity()
            True

        TESTS::

            sage: V = QQ^10
            sage: H = Hom(V, V)
            sage: id = H.identity()
            sage: id.is_identity()
            True

        AUTHOR:

        - Rob Beezer (2011-06-28)
        """
    def is_zero(self) -> bool:
        """
        Determine if this morphism is a zero function or not.

        EXAMPLES:

        A zero morphism created from a function.  ::

            sage: V = ZZ^5
            sage: W = ZZ^3
            sage: z = lambda x: zero_vector(ZZ, 3)
            sage: phi = V.hom(z, W)
            sage: phi.is_zero()
            True

        An image list that just barely makes a nonzero morphism.  ::

            sage: V = ZZ^4
            sage: W = ZZ^6
            sage: z = zero_vector(ZZ, 6)
            sage: images = [z, z, W.5, z]
            sage: phi = V.hom(images, W)
            sage: phi.is_zero()
            False

        TESTS::

            sage: V = QQ^10
            sage: W = QQ^3
            sage: H = Hom(V, W)
            sage: rho = H.zero()
            sage: rho.is_zero()
            True

        AUTHOR:

        - Rob Beezer (2011-07-15)
        """
    def is_equal_function(self, other) -> bool:
        '''
        Determine if two morphisms are equal functions.

        INPUT:

        - ``other`` -- a morphism to compare with ``self``

        OUTPUT:

        Returns ``True`` precisely when the two morphisms have
        equal domains and codomains (as sets) and produce identical
        output when given the same input.  Otherwise returns ``False``.

        This is useful when ``self`` and ``other`` may have different
        representations.

        Sage\'s default comparison of matrix morphisms requires the
        domains to have the same bases and the codomains to have the
        same bases, and then compares the matrix representations.
        This notion of equality is more permissive (it will
        return ``True`` "more often"), but is more correct
        mathematically.

        EXAMPLES:

        Three morphisms defined by combinations of different
        bases for the domain and codomain and different functions.
        Two are equal, the third is different from both of the others.  ::

            sage: B = matrix(QQ, [[-3,  5, -4,  2],
            ....:                 [-1,  2, -1,  4],
            ....:                 [ 4, -6,  5, -1],
            ....:                 [-5,  7, -6,  1]])
            sage: U = (QQ^4).subspace_with_basis(B.rows())
            sage: C = matrix(QQ, [[-1, -6, -4],
            ....:                 [ 3, -5,  6],
            ....:                 [ 1,  2,  3]])
            sage: V = (QQ^3).subspace_with_basis(C.rows())
            sage: H = Hom(U, V)

            sage: D = matrix(QQ, [[-7, -2, -5,  2],
            ....:                 [-5,  1, -4, -8],
            ....:                 [ 1, -1,  1,  4],
            ....:                 [-4, -1, -3,   1]])
            sage: X = (QQ^4).subspace_with_basis(D.rows())
            sage: E = matrix(QQ, [[ 4, -1,  4],
            ....:                 [ 5, -4, -5],
            ....:                 [-1,  0, -2]])
            sage: Y = (QQ^3).subspace_with_basis(E.rows())
            sage: K = Hom(X, Y)

            sage: f = lambda x: vector(QQ, [x[0]+x[1], 2*x[1]-4*x[2], 5*x[3]])
            sage: g = lambda x: vector(QQ, [x[0]-x[2], 2*x[1]-4*x[2], 5*x[3]])

            sage: rho = H(f)
            sage: phi = K(f)
            sage: zeta = H(g)

            sage: rho.is_equal_function(phi)
            True
            sage: phi.is_equal_function(rho)
            True
            sage: zeta.is_equal_function(rho)
            False
            sage: phi.is_equal_function(zeta)
            False

        TESTS::

            sage: H = Hom(ZZ^2, ZZ^2)
            sage: phi = H(matrix(ZZ, 2, range(4)))
            sage: phi.is_equal_function(\'junk\')
            Traceback (most recent call last):
            ...
            TypeError: can only compare to a matrix morphism, not junk

        AUTHOR:

        - Rob Beezer (2011-07-15)
        '''
    def restrict_domain(self, sub):
        """
        Restrict this matrix morphism to a subspace sub of the domain. The
        subspace sub should have a basis() method and elements of the basis
        should be coercible into domain.

        The resulting morphism has the same codomain as before, but a new
        domain.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])
            sage: phi.restrict_domain(V.span([V.0]))
            Free module morphism defined by the matrix
            [3 0]
            Domain: Free module of degree 2 and rank 1 over Integer Ring
            Echelon ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...
            sage: phi.restrict_domain(V.span([V.1]))
            Free module morphism defined by the matrix
            [0 2]...
            sage: m = matrix(2, range(1,5))
            sage: f1 = V.hom(m); f2 = V.hom(m, side='right')
            sage: SV = V.span([V.0])
            sage: f1.restrict_domain(SV)
            Free module morphism defined by the matrix
            [1 2]...
            sage: f2.restrict_domain(SV)
            Free module morphism defined as left-multiplication by the matrix
            [1]
            [3]...
        """
    def restrict_codomain(self, sub):
        """
        Restrict this matrix morphism to a subspace sub of the codomain.

        The resulting morphism has the same domain as before, but a new
        codomain.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([4*(V.0+V.1),0])
            sage: W = V.span([2*(V.0+V.1)])
            sage: phi
            Free module morphism defined by the matrix
            [4 4]
            [0 0]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Ambient free module of rank 2 over the principal ideal domain ...
            sage: psi = phi.restrict_codomain(W); psi
            Free module morphism defined by the matrix
            [2]
            [0]
            Domain: Ambient free module of rank 2 over the principal ideal domain ...
            Codomain: Free module of degree 2 and rank 1 over Integer Ring
            Echelon ...
            sage: phi2 = phi.side_switch(); phi2.restrict_codomain(W)
            Free module morphism defined as left-multiplication by the matrix
            [2 0]
            Domain: Ambient free module of rank 2 over the principal ideal domain Integer Ring
            Codomain: Free module of degree 2 and rank 1 over Integer Ring
            Echelon ...

        An example in which the codomain equals the full ambient space, but
        with a different basis::

            sage: V = QQ^2
            sage: W = V.span_of_basis([[1,2],[3,4]])
            sage: phi = V.hom(matrix(QQ,2,[1,0,2,0]),W)
            sage: phi.matrix()
            [1 0]
            [2 0]
            sage: phi(V.0)
            (1, 2)
            sage: phi(V.1)
            (2, 4)
            sage: X = V.span([[1,2]]); X
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 2]
            sage: phi(V.0) in X
            True
            sage: phi(V.1) in X
            True
            sage: psi = phi.restrict_codomain(X); psi
            Vector space morphism represented by the matrix:
            [1]
            [2]
            Domain: Vector space of dimension 2 over Rational Field
            Codomain: Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 2]
            sage: psi(V.0)
            (1, 2)
            sage: psi(V.1)
            (2, 4)
            sage: psi(V.0).parent() is X
            True
        """
    def restrict(self, sub):
        """
        Restrict this matrix morphism to a subspace sub of the domain.

        The codomain and domain of the resulting matrix are both sub.

        EXAMPLES::

            sage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])
            sage: phi.restrict(V.span([V.0]))
            Free module morphism defined by the matrix
            [3]
            Domain: Free module of degree 2 and rank 1 over Integer Ring
            Echelon ...
            Codomain: Free module of degree 2 and rank 1 over Integer Ring
            Echelon ...

            sage: V = (QQ^2).span_of_basis([[1,2], [3,4]])
            sage: phi = V.hom([V.0 + V.1, 2*V.1])
            sage: phi(V.1) == 2*V.1
            True
            sage: W = span([V.1])
            sage: phi(W)
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [  1 4/3]
            sage: psi = phi.restrict(W); psi
            Vector space morphism represented by the matrix:
            [2]
            Domain:   Vector space of degree 2 and dimension 1 over Rational Field
                      Basis matrix:
                      [  1 4/3]
            Codomain: Vector space of degree 2 and dimension 1 over Rational Field
                      Basis matrix:
                      [  1 4/3]
            sage: psi.domain() == W
            True
            sage: psi(W.0) == 2*W.0
            True

        ::

            sage: V = ZZ^3
            sage: h1 = V.hom([V.0, V.1+V.2, -V.1+V.2])
            sage: h2 = h1.side_switch()
            sage: SV = V.span([2*V.1,2*V.2])
            sage: h1.restrict(SV)
            Free module morphism defined by the matrix
            [ 1  1]
            [-1  1]
            Domain:   Free module of degree 3 and rank 2 over Integer Ring
                      Echelon basis matrix:
                      [0 2 0]
                      [0 0 2]
            Codomain: Free module of degree 3 and rank 2 over Integer Ring
                      Echelon basis matrix:
                      [0 2 0]
                      [0 0 2]
            sage: h2.restrict(SV)
            Free module morphism defined as left-multiplication by the matrix
            [ 1 -1]
            [ 1  1]
            Domain:   Free module of degree 3 and rank 2 over Integer Ring
                      Echelon basis matrix:
                      [0 2 0]
                      [0 0 2]
            Codomain: Free module of degree 3 and rank 2 over Integer Ring
                      Echelon basis matrix:
                      [0 2 0]
                      [0 0 2]
        """

class MatrixMorphism(MatrixMorphism_abstract):
    """
    A morphism defined by a matrix.

    INPUT:

    - ``parent`` -- a homspace

    - ``A`` -- matrix or a :class:`MatrixMorphism_abstract` instance

    - ``copy_matrix`` -- boolean (default: ``True``); make an immutable copy of
      the matrix ``A`` if it is mutable. If ``False``, then this makes
      ``A`` immutable.
    """
    def __init__(self, parent, A, copy_matrix: bool = True, side: str = 'left') -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.modules.matrix_morphism import MatrixMorphism
            sage: T = End(ZZ^3)
            sage: M = MatrixSpace(ZZ, 3)
            sage: I = M.identity_matrix()
            sage: A = MatrixMorphism(T, I)
            sage: loads(A.dumps()) == A
            True
        """
    def matrix(self, side=None):
        """
        Return a matrix that defines this morphism.

        INPUT:

        - ``side`` -- (default: ``None``) the side of the matrix
          where a vector is placed to effect the morphism (function)

        OUTPUT:

        A matrix which represents the morphism, relative to bases
        for the domain and codomain.  If the modules are provided
        with user bases, then the representation is relative to
        these bases.

        Internally, Sage represents a matrix morphism with the
        matrix multiplying a row vector placed to the left of the
        matrix.  If the option ``side='right'`` is used, then a
        matrix is returned that acts on a vector to the right of
        the matrix.  These two matrices are just transposes of
        each other and the difference is just a preference for
        the style of representation.

        EXAMPLES::

            sage: V = ZZ^2; W = ZZ^3
            sage: m = column_matrix([3*V.0 - 5*V.1, 4*V.0 + 2*V.1, V.0 + V.1])
            sage: phi = V.hom(m, W)
            sage: phi.matrix()
            [ 3  4  1]
            [-5  2  1]

            sage: phi.matrix(side='right')
            [ 3 -5]
            [ 4  2]
            [ 1  1]

        TESTS::

            sage: V = ZZ^2
            sage: phi = V.hom([3*V.0, 2*V.1])
            sage: phi.matrix(side='junk')
            Traceback (most recent call last):
            ...
            ValueError: side must be 'left' or 'right', not junk
        """
    def is_injective(self) -> bool:
        """
        Tell whether ``self`` is injective.

        EXAMPLES::

            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi = V1.hom(Matrix([[1,2,3], [4,5,6]]),V2)
            sage: phi.is_injective()
            True
            sage: psi = V2.hom(Matrix([[1,2], [3,4], [5,6]]),V1)
            sage: psi.is_injective()
            False

        AUTHOR:

        -- Simon King (2010-05)
        """
    def is_surjective(self) -> bool:
        """
        Tell whether ``self`` is surjective.

        EXAMPLES::

            sage: V1 = QQ^2
            sage: V2 = QQ^3
            sage: phi = V1.hom(Matrix([[1,2,3], [4,5,6]]), V2)
            sage: phi.is_surjective()
            False
            sage: psi = V2.hom(Matrix([[1,2], [3,4], [5,6]]), V1)
            sage: psi.is_surjective()
            True

        An example over a PID that is not `\\ZZ`.  ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: A = R^2
            sage: B = R^2
            sage: H = A.hom([B([x^2 - 1, 1]), B([x^2, 1])])
            sage: H.image()
            Free module of degree 2 and rank 2 over Univariate Polynomial Ring in x over Rational Field
            Echelon basis matrix:
            [ 1  0]
            [ 0 -1]
            sage: H.is_surjective()
            True

        This tests if :issue:`11552` is fixed. ::

            sage: V = ZZ^2
            sage: m = matrix(ZZ, [[1,2], [0,2]])
            sage: phi = V.hom(m, V)
            sage: phi.lift(vector(ZZ, [0, 1]))
            Traceback (most recent call last):
            ...
            ValueError: element is not in the image
            sage: phi.is_surjective()
            False

        AUTHORS:

        - Simon King (2010-05)
        - Rob Beezer (2011-06-28)
        """
