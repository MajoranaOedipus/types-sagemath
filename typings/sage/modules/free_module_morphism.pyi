from sage.categories.morphism import Morphism as Morphism
from sage.modules import free_module_homspace as free_module_homspace, matrix_morphism as matrix_morphism
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

def is_FreeModuleMorphism(x):
    """
    This function is deprecated.

    EXAMPLES::

        sage: V = ZZ^2; f = V.hom([V.1, -2*V.0])
        sage: sage.modules.free_module_morphism.is_FreeModuleMorphism(f)
        doctest:warning...
        DeprecationWarning: is_FreeModuleMorphism is deprecated;
        use isinstance(..., FreeModuleMorphism) or categories instead
        See https://github.com/sagemath/sage/issues/37731 for details.
        True
        sage: sage.modules.free_module_morphism.is_FreeModuleMorphism(0)
        False
    """

class FreeModuleMorphism(matrix_morphism.MatrixMorphism):
    def __init__(self, parent, A, side: str = 'left') -> None:
        """
        INPUT:

            - ``parent`` -- a homspace in a (sub) category of free modules

            - ``A`` -- matrix

            - ``side`` -- side of the vectors acted on by the matrix  (default: ``'left'``)

        EXAMPLES::

            sage: V = ZZ^3; W = span([[1,2,3], [-1,2,8]], ZZ)
            sage: phi = V.hom(matrix(ZZ, 3, [1..9]))
            sage: type(phi)
            <class 'sage.modules.free_module_morphism.FreeModuleMorphism'>
        """
    def pushforward(self, x):
        """
        Compute the image of a sub-module of the domain.

        EXAMPLES::

            sage: V = QQ^3; W = span([[1,2,3], [-1,2,5/3]], QQ)
            sage: phi = V.hom(matrix(QQ, 3, [1..9]))
            sage: phi.rank()
            2
            sage: phi(V)   #indirect doctest
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [ 1  0 -1]
            [ 0  1  2]

        We compute the image of a submodule of a ZZ-module embedded in
        a rational vector space::

            sage: V = QQ^3; W = V.span_of_basis([[2,2,3], [-1,2,5/3]], ZZ)
            sage: phi = W.hom([W.0, W.0 - W.1]); phi
            Free module morphism defined by the matrix
            [ 1  0]
            [ 1 -1]...
            sage: phi(span([2*W.1], ZZ))
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [  6   0 8/3]
            sage: phi(2*W.1)
            (6, 0, 8/3)
        """
    def change_ring(self, R):
        """
        Change the ring over which this morphism is defined.

        This changes the ring of the domain, codomain, and underlying matrix.

        EXAMPLES::

            sage: V0 = span([[0,0,1],[0,2,0]], ZZ); V1 = span([[1/2,0],[0,2]], ZZ)
            sage: W = span([[1,0],[0,6]], ZZ)
            sage: h = V0.hom([-3*V1.0 - 3*V1.1, -3*V1.0 - 3*V1.1])
            sage: h.base_ring()
            Integer Ring
            sage: h
            Free module morphism defined by the matrix
            [-3 -3]
            [-3 -3]...
            sage: h.change_ring(QQ).base_ring()
            Rational Field
            sage: f = h.change_ring(QQ); f
            Vector space morphism represented by the matrix:
            [-3 -3]
            [-3 -3]
            Domain:   Vector space of degree 3 and dimension 2 over Rational Field
                      Basis matrix:
                      [0 1 0]
                      [0 0 1]
            Codomain: Vector space of degree 2 and dimension 2 over Rational Field
                      Basis matrix:
                      [1 0]
                      [0 1]
            sage: f = h.change_ring(GF(7)); f
            Vector space morphism represented by the matrix:
            [4 4]
            [4 4]
            Domain:   Vector space of degree 3 and dimension 2 over Finite Field of size 7
                      Basis matrix:
                      [0 1 0]
                      [0 0 1]
            Codomain: Vector space of degree 2 and dimension 2 over Finite Field of size 7
                      Basis matrix:
                      [1 0]
                      [0 1]
        """
    def inverse_image(self, V):
        """
        Given a submodule V of the codomain of self, return the
        inverse image of V under self, i.e., the biggest submodule of
        the domain of ``self`` that maps into V.

        EXAMPLES:

        We test computing inverse images over a field::

            sage: V = QQ^3; W = span([[1,2,3], [-1,2,5/3]], QQ)
            sage: phi = V.hom(matrix(QQ, 3, [1..9]))
            sage: phi.rank()
            2
            sage: I = phi.inverse_image(W); I
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0    0]
            [   0    1 -1/2]
            sage: phi(I.0) in W
            True
            sage: phi(I.1) in W
            True
            sage: W = phi.image()
            sage: phi.inverse_image(W) == V
            True

        We test computing inverse images between two spaces embedded in different
        ambient spaces.::

            sage: V0 = span([[0,0,1],[0,2,0]],ZZ); V1 = span([[1/2,0],[0,2]],ZZ)
            sage: W = span([[1,0],[0,6]],ZZ)
            sage: h = V0.hom([-3*V1.0 - 3*V1.1, -3*V1.0 - 3*V1.1])
            sage: h.inverse_image(W)
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [0 2 1]
            [0 0 2]
            sage: h(h.inverse_image(W)).is_submodule(W)
            True
            sage: h(h.inverse_image(W)).index_in(W)
            +Infinity
            sage: h(h.inverse_image(W))
            Free module of degree 2 and rank 1 over Integer Ring
            Echelon basis matrix:
            [ 3 12]


        We test computing inverse images over the integers::

            sage: V = QQ^3; W = V.span_of_basis([[2,2,3],[-1,2,5/3]], ZZ)
            sage: phi = W.hom([W.0, W.0 - W.1])
            sage: Z = W.span([2*W.1]); Z
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [    2    -4 -10/3]
            sage: Y = phi.inverse_image(Z); Y
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [  6   0 8/3]
            sage: phi(Y) == Z
            True

        We test that :issue:`24590` is resolved::

            sage: A = FreeQuadraticModule(ZZ, 1, matrix([2]))
            sage: f = A.Hom(A).an_element()
            sage: f.inverse_image(A)
            Free module of degree 1 and rank 1 over Integer Ring
            Echelon basis matrix:
            [1]

        We test that it respects the ``side``::

            sage: V = ZZ^2
            sage: m = matrix(2, [1, 1, 0, 1])
            sage: h = V.hom(m, side='right')
            sage: h
            Free module morphism defined as left-multiplication by the matrix
            [1 1]
            [0 1]...
            sage: SV = V.span([V.0])
            sage: h.inverse_image(SV)
            Free module of degree 2 and rank 1 over Integer Ring
            Echelon basis matrix:
            [1 0]
            sage: V.hom(m).inverse_image(SV)
            Free module of degree 2 and rank 1 over Integer Ring
            Echelon basis matrix:
            [ 1 -1]
        """
    def lift(self, x):
        """
        Given an element of the image, return an element of the codomain that maps onto it.

        Note that ``lift`` and ``preimage_representative`` are
        equivalent names for this method, with the latter suggesting
        that the return value is a coset representative of the domain
        modulo the kernel of the morphism.

        EXAMPLES::

            sage: X = QQ**2
            sage: V = X.span([[2, 0], [0, 8]], ZZ)
            sage: W = (QQ**1).span([[1/12]], ZZ)
            sage: f = V.hom([W([1/3]), W([1/2])], W)
            sage: l=f.lift([1/3]); l  # random
            (8, -16)
            sage: f(l)
            (1/3)
            sage: f(f.lift([1/2]))
            (1/2)
            sage: f(f.lift([1/6]))
            (1/6)
            sage: f.lift([1/12])
            Traceback (most recent call last):
            ...
            ValueError: element is not in the image
            sage: f.lift([1/24])
            Traceback (most recent call last):
            ...
            TypeError: element [1/24] is not in free module

        This works for vector spaces, too::

            sage: V = VectorSpace(GF(3), 2)
            sage: W = VectorSpace(GF(3), 3)
            sage: f = V.hom([W.1, W.1 - W.0])
            sage: f.lift(W.1)
            (1, 0)
            sage: f.lift(W.2)
            Traceback (most recent call last):
            ...
            ValueError: element is not in the image
            sage: w = W((17, -2, 0))
            sage: f(f.lift(w)) == w
            True

        This example illustrates the use of the ``preimage_representative``
        as an equivalent name for this method.  ::

            sage: V = ZZ^3
            sage: W = ZZ^2
            sage: w = vector(ZZ, [1,2])
            sage: f = V.hom([w, w, w], W)
            sage: f.preimage_representative(vector(ZZ, [10, 20]))
            (0, 0, 10)

        ::

            sage: V = QQ^2; m = matrix(2, [1, 1, 0, 1])
            sage: V.hom(m, side='right').lift(V.0 + V.1)
            (0, 1)
            sage: V.hom(m).lift(V.0 + V.1)
            (1, 0)
        """
    preimage_representative = lift
    def eigenvalues(self, extend: bool = True):
        """
        Return a list with the eigenvalues of the endomorphism of vector spaces.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); decides if base field
          extensions should be considered or not

        EXAMPLES:

        We compute the eigenvalues of an endomorphism of `\\QQ^3`::

            sage: V = QQ^3
            sage: H = V.endomorphism_ring()([[1,-1,0], [-1,1,1], [0,3,1]])
            sage: H.eigenvalues()                                                       # needs sage.rings.number_field
            [3, 1, -1]

        Note the effect of the ``extend`` option::

            sage: V = QQ^2
            sage: H = V.endomorphism_ring()([[0,-1], [1,0]])
            sage: H.eigenvalues()                                                       # needs sage.rings.number_field
            [-1*I, 1*I]
            sage: H.eigenvalues(extend=False)                                           # needs sage.libs.pari
            []
        """
    def eigenvectors(self, extend: bool = True):
        """
        Compute the subspace of eigenvectors of a given eigenvalue.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); decides if base field
          extensions should be considered or not

        OUTPUT:

        A sequence of tuples. Each tuple contains an eigenvalue, a sequence
        with a basis of the corresponding subspace of eigenvectors, and the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: V = (QQ^4).subspace([[0,2,1,4], [1,2,5,0], [1,1,1,1]])
            sage: H = (V.Hom(V))(matrix(QQ, [[0,1,0], [-1,0,0], [0,0,3]]))
            sage: H.eigenvectors()
            [(3, [(0, 0, 1, -6/7)], 1),
             (-1*I, [(1, 1*I, 0, -0.571428571428572? + 2.428571428571429?*I)], 1),
             (1*I, [(1, -1*I, 0, -0.571428571428572? - 2.428571428571429?*I)], 1)]
            sage: H.eigenvectors(extend=False)
            [(3, [(0, 0, 1, -6/7)], 1)]
            sage: H1 = (V.Hom(V))(matrix(QQ, [[2,1,0],[0,2,0],[0,0,3]]))
            sage: H1.eigenvectors()
            [(3, [(0, 0, 1, -6/7)], 1), (2, [(0, 1, 0, 17/7)], 2)]
            sage: H1.eigenvectors(extend=False)
            [(3, [(0, 0, 1, -6/7)], 1), (2, [(0, 1, 0, 17/7)], 2)]

        ::

            sage: V = QQ^2
            sage: m = matrix(2, [1, 1, 0, 1])
            sage: V.hom(m, side='right').eigenvectors()                                 # needs sage.rings.number_field
            [(1, [(1, 0)], 2)]
            sage: V.hom(m).eigenvectors()                                               # needs sage.rings.number_field
            [(1, [(0, 1)], 2)]
        """
    def eigenspaces(self, extend: bool = True):
        """
        Compute a list of subspaces formed by eigenvectors of ``self``.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); determines if field
          extensions should be considered

        OUTPUT: a list of pairs ``(eigenvalue, eigenspace)``

        EXAMPLES::

            sage: V = QQ^3
            sage: h = V.hom([[1,0,0], [0,0,1], [0,-1,0]], V)
            sage: h.eigenspaces()                                                       # needs sage.rings.number_field
            [(1,    Vector space of degree 3 and dimension 1 over Rational Field
                     Basis matrix:
                     [1 0 0]),
             (-1*I, Vector space of degree 3 and dimension 1 over Algebraic Field
                     Basis matrix:
                     [  0   1 1*I]),
             (1*I,  Vector space of degree 3 and dimension 1 over Algebraic Field
                     Basis matrix:
                     [   0    1 -1*I])]

            sage: h.eigenspaces(extend=False)                                           # needs sage.rings.number_field
            [(1,
              Vector space of degree 3 and dimension 1 over Rational Field
              Basis matrix:
              [1 0 0])]

            sage: h = V.hom([[2,1,0], [0,2,0], [0,0,-1]], V)
            sage: h.eigenspaces()                                                       # needs sage.rings.number_field
            [(-1, Vector space of degree 3 and dimension 1 over Rational Field
                   Basis matrix:
                   [0 0 1]),
             (2, Vector space of degree 3 and dimension 1 over Rational Field
                  Basis matrix:
                  [0 1 0])]

            sage: h = V.hom([[2,1,0], [0,2,0], [0,0,2]], V)
            sage: h.eigenspaces()                                                       # needs sage.rings.number_field
            [(2, Vector space of degree 3 and dimension 2 over Rational Field
                  Basis matrix:
                  [0 1 0]
                  [0 0 1])]

        ::

            sage: V = QQ^2; m = matrix(2, [1, 1, 0, 1])
            sage: V.hom(m, side='right').eigenspaces()                                  # needs sage.rings.number_field
            [(1, Vector space of degree 2 and dimension 1 over Rational Field
                  Basis matrix:
                  [1 0])]
            sage: V.hom(m).eigenspaces()                                                # needs sage.rings.number_field
            [(1, Vector space of degree 2 and dimension 1 over Rational Field
                  Basis matrix:
                  [0 1])]
        """

class BaseIsomorphism1D(Morphism):
    """
    An isomorphism between a ring and a free rank-1 module over the ring.

    EXAMPLES::

        sage: R.<x,y> = QQ[]
        sage: V, from_V, to_V = R.free_module(R)
        sage: from_V
        Isomorphism morphism:
          From: Ambient free module of rank 1 over the integral domain
                Multivariate Polynomial Ring in x, y over Rational Field
          To:   Multivariate Polynomial Ring in x, y over Rational Field
    """
    def is_injective(self) -> bool:
        """
        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: V, from_V, to_V = R.free_module(R)
            sage: from_V.is_injective()
            True
        """
    def is_surjective(self) -> bool:
        """
        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: V, from_V, to_V = R.free_module(R)
            sage: from_V.is_surjective()
            True
        """

class BaseIsomorphism1D_to_FM(BaseIsomorphism1D):
    """
    An isomorphism from a ring to its 1-dimensional free module.

    INPUT:

    - ``parent`` -- the homset
    - ``basis`` -- (default: 1) an invertible element of the ring

    EXAMPLES::

        sage: R = Zmod(8)
        sage: V, from_V, to_V = R.free_module(R)
        sage: v = to_V(2); v
        (2)
        sage: from_V(v)
        2
        sage: W, from_W, to_W = R.free_module(R, basis=3)
        sage: W is V
        True
        sage: w = to_W(2); w
        (6)
        sage: from_W(w)
        2

    The basis vector has to be a unit so that the map is an isomorphism::

        sage: W, from_W, to_W = R.free_module(R, basis=4)
        Traceback (most recent call last):
        ...
        ValueError: basis element must be a unit
    """
    def __init__(self, parent, basis=None) -> None:
        """
        TESTS::

            sage: R = Zmod(8)
            sage: W, from_W, to_W = R.free_module(R, basis=3)
            sage: TestSuite(to_W).run()
        """

class BaseIsomorphism1D_from_FM(BaseIsomorphism1D):
    """
    An isomorphism to a ring from its 1-dimensional free module.

    INPUT:

    - ``parent`` -- the homset
    - ``basis`` -- (default: 1) an invertible element of the ring

    EXAMPLES::

        sage: R.<x> = QQ[[]]
        sage: V, from_V, to_V = R.free_module(R)
        sage: v = to_V(1+x); v
        (1 + x)
        sage: from_V(v)
        1 + x
        sage: W, from_W, to_W = R.free_module(R, basis=(1-x))
        sage: W is V
        True
        sage: w = to_W(1+x); w
        (1 - x^2)
        sage: from_W(w)
        1 + x + O(x^20)

    The basis vector has to be a unit so that the map is an isomorphism::

        sage: W, from_W, to_W = R.free_module(R, basis=x)
        Traceback (most recent call last):
        ...
        ValueError: basis element must be a unit
    """
    def __init__(self, parent, basis=None) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[[]]
            sage: W, from_W, to_W = R.free_module(R, basis=(1-x))
            sage: TestSuite(from_W).run(skip='_test_nonzero_equal')
        """
