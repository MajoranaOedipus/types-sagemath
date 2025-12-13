from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.modules import free_module as free_module

def FreeQuadraticModule(base_ring, rank, inner_product_matrix, sparse: bool = False, inner_product_ring=None):
    """
    Create the free quadratic module over the given commutative ring of the given rank.

    INPUT:

    - ``base_ring`` -- a commutative ring

    - ``rank`` -- nonnegative integer

    - ``inner_product_matrix`` -- the inner product matrix

    - ``sparse`` -- boolean (default: ``False``)

    - ``inner_product_ring`` -- the inner product codomain ring (default: ``None``)

    OUTPUT:

    A free quadratic module (with given inner product matrix).

    .. NOTE::

        In Sage, it is the case that there is only one dense and one
        sparse free ambient quadratic module of rank `n` over `R` and
        given inner product matrix.

    EXAMPLES::

        sage: M2 = FreeQuadraticModule(ZZ, 2, inner_product_matrix=[1,2,3,4])
        sage: M2 is FreeQuadraticModule(ZZ, 2, inner_product_matrix=[1,2,3,4])
        True
        sage: M2.inner_product_matrix()
        [1 2]
        [3 4]
        sage: M3 = FreeModule(ZZ, 2, inner_product_matrix=[[1,2],[3,4]])
        sage: M3 is M2
        True

    TESTS:

    Check for :issue:`10577`::

        sage: m = matrix.diagonal(GF(2), [1,1])
        sage: V2 = VectorSpace(GF(2), 2, inner_product_matrix=m)
        sage: deepcopy(V2)
        Ambient quadratic space of dimension 2 over Finite Field of size 2
        Inner product matrix:
        [1 0]
        [0 1]
    """
def QuadraticSpace(K, dimension, inner_product_matrix, sparse: bool = False):
    """
    EXAMPLES:

    The base can be complicated, as long as it is a field::

        sage: F.<x> = FractionField(PolynomialRing(ZZ,'x'))
        sage: D = diagonal_matrix([x, x - 1, x + 1])
        sage: V = QuadraticSpace(F, 3, D)
        sage: V
        Ambient quadratic space of dimension 3 over
         Fraction Field of Univariate Polynomial Ring in x over Integer Ring
        Inner product matrix:
        [    x     0     0]
        [    0 x - 1     0]
        [    0     0 x + 1]
        sage: V.basis()
        [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    The base must be a field or a :exc:`TypeError` is raised::

        sage: QuadraticSpace(ZZ, 5, identity_matrix(ZZ,2))
        Traceback (most recent call last):
        ...
        TypeError: argument K (= Integer Ring) must be a field
    """
InnerProductSpace = QuadraticSpace

def is_FreeQuadraticModule(M):
    """
    Return ``True`` if `M` is a free quadratic module.

    EXAMPLES::

        sage: from sage.modules.free_quadratic_module import is_FreeQuadraticModule
        sage: U = FreeModule(QQ,3)
        sage: is_FreeQuadraticModule(U)
        doctest:warning...
        DeprecationWarning: the function is_FreeQuadraticModule is deprecated;
        use 'isinstance(..., FreeQuadraticModule_generic)' instead
        See https://github.com/sagemath/sage/issues/37924 for details.
        False
        sage: V = FreeModule(QQ,3,inner_product_matrix=diagonal_matrix([1,1,1]))
        sage: is_FreeQuadraticModule(V)
        True
        sage: W = FreeModule(QQ,3,inner_product_matrix=diagonal_matrix([2,3,3]))
        sage: is_FreeQuadraticModule(W)
        True
    """

class FreeQuadraticModule_generic(free_module.FreeModule_generic):
    """
    Base class for all free quadratic modules.

    Modules are ordered by inclusion in the same ambient space.

    TESTS:

    We compare rank three free modules over the integers,
    rationals, and complex numbers::

        sage: Q3 = FreeQuadraticModule(QQ,3,matrix.identity(3))
        sage: C3 = FreeQuadraticModule(CC,3,matrix.identity(3))
        sage: Z3 = FreeQuadraticModule(ZZ,3,matrix.identity(3))
        sage: Q3 < C3
        False
        sage: C3 < Q3
        False
        sage: C3 > Q3
        False
        sage: Q3 > Z3
        True
        sage: Q3 < Z3
        False
        sage: Z3 < Q3
        True
        sage: Z3 > Q3
        False
        sage: Q3 == Z3
        False
        sage: Q3 == Q3
        True

        sage: V = Q3.span([[1,2,3], [5,6,7], [8,9,10]])
        sage: V < Q3
        True
        sage: Q3 < V
        False

    The :meth:`inner_product_matrix` is part of the comparison::

        sage: Q3zero = FreeQuadraticModule(QQ,3,matrix.zero(3))
        sage: Q3zero == Q3
        False

    We test that :issue:`23915` is fixed::

        sage: M1 = FreeQuadraticModule(ZZ,1,matrix.identity(1))
        sage: M2 = FreeQuadraticModule(ZZ,1,matrix.identity(1)*2)
        sage: M1 == M2
        False
    """
    def __init__(self, base_ring, rank, degree, inner_product_matrix, sparse: bool = False) -> None:
        """
        Create the free module of given rank over the given ``base_ring``.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``rank`` -- nonnegative integer

        EXAMPLES::

            sage: R = PolynomialRing(QQ,3,'x')
            sage: FreeModule(R,3,inner_product_matrix=diagonal_matrix(list(R.gens())))
            Ambient free quadratic module of rank 3 over the integral domain Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
            Inner product matrix:
            [x0  0  0]
            [ 0 x1  0]
            [ 0  0 x2]
        """
    def ambient_module(self):
        """
        Return the ambient module associated to this module.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: M = FreeModule(R,2)
            sage: M.ambient_module()
            Ambient free module of rank 2 over the integral domain Multivariate Polynomial Ring in x, y over Rational Field

            sage: V = FreeModule(QQ, 4).span([[1,2,3,4], [1,0,0,0]]); V
            Vector space of degree 4 and dimension 2 over Rational Field
            Basis matrix:
            [  1   0   0   0]
            [  0   1 3/2   2]
            sage: V.ambient_module()
            Vector space of dimension 4 over Rational Field
        """
    def determinant(self):
        """
        Return the determinant of this free module.

        EXAMPLES::

            sage: M = FreeModule(ZZ, 3, inner_product_matrix=1)
            sage: M.determinant()
            1
            sage: N = M.span([[1,2,3]])
            sage: N.determinant()
            14
            sage: P = M.span([[1,2,3], [1,1,1]])
            sage: P.determinant()
            6
        """
    def discriminant(self):
        """
        Return the discriminant of this free module.

        This is defined to be `(-1)^r` of the determinant, where `r = n/2`
        (`n` even) or `(n-1)/2` (`n` odd) for a module of rank `n`.

        EXAMPLES::

            sage: M = FreeModule(ZZ, 3)
            sage: M.discriminant()
            1
            sage: N = M.span([[1,2,3]])
            sage: N.discriminant()
            14
            sage: P = M.span([[1,2,3], [1,1,1]])
            sage: P.discriminant()
            6

        TESTS::

            sage: M = FreeQuadraticModule(ZZ, 2, matrix.identity(2))
            sage: M.discriminant()
            -1
            sage: M = FreeQuadraticModule(QQ, 3, matrix.identity(3))
            sage: M.discriminant()
            -1
        """
    def gram_matrix(self):
        """
        Return the Gram matrix associated to this free module.

        This is defined to be ``B*A*B.transpose()``, where ``A`` is the
        inner product matrix (induced from the ambient space), and ``B``
        the basis matrix.

        EXAMPLES::

            sage: V = VectorSpace(QQ,4)
            sage: u = V([1/2,1/2,1/2,1/2])
            sage: v = V([0,1,1,0])
            sage: w = V([0,0,1,1])
            sage: M = span([u,v,w], ZZ)
            sage: M.inner_product_matrix() == V.inner_product_matrix()
            True
            sage: L = M.submodule_with_basis([u,v,w])
            sage: L.inner_product_matrix() == M.inner_product_matrix()
            True
            sage: L.gram_matrix()
            [1 1 1]
            [1 2 1]
            [1 1 2]
        """
    def inner_product_matrix(self):
        """
        Return the inner product matrix associated to this module.

        By definition, this is the inner product matrix of the ambient
        space, hence may be of degree greater than the rank of the
        module.

        .. NOTE:: The inner product does not have to be symmetric (see examples).

        .. TODO::

            Differentiate the image ring of the inner product from the base ring of
            the module and/or ambient space.  E.g. On an integral module over ZZ the inner
            product pairing could naturally take values in ZZ, QQ, RR, or CC.

        EXAMPLES::

            sage: M = FreeModule(ZZ, 3)
            sage: M.inner_product_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]

        The inner product does not have to be symmetric or definite::

            sage: N = FreeModule(ZZ,2,inner_product_matrix=[[1,-1],[2,5]])
            sage: N.inner_product_matrix()
            [ 1 -1]
            [ 2  5]
            sage: u, v = N.basis()
            sage: u.inner_product(v)
            -1
            sage: v.inner_product(u)
            2

        The inner product matrix is defined with respect to the ambient space::

            sage: V = QQ^3
            sage: u = V([1/2,1,1])
            sage: v = V([1,1,1/2])
            sage: M = span([u,v], ZZ)
            sage: M.inner_product_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: M.inner_product_matrix() == V.inner_product_matrix()
            True
            sage: M.gram_matrix()
            [ 1/2 -3/4]
            [-3/4 13/4]
        """

class FreeQuadraticModule_generic_pid(free_module.FreeModule_generic_pid, FreeQuadraticModule_generic):
    """
    Class of all free modules over a PID.
    """
    def __init__(self, base_ring, rank, degree, inner_product_matrix, sparse: bool = False) -> None:
        """
        Create a free module over a PID.

        EXAMPLES::

            sage: FreeModule(ZZ, 2, inner_product_matrix=Matrix([[2,1],[1,2]]))
            Ambient free quadratic module of rank 2 over the principal ideal domain Integer Ring
            Inner product matrix:
            [2 1]
            [1 2]
        """
    def span(self, gens, check: bool = True, already_echelonized: bool = False):
        """
        Return the `R`-span of the given list of gens, where `R`
        is the base ring of ``self``.

        Note that this span need not be a submodule of ``self``, nor even
        of the ambient space.  It must, however, be contained in the
        ambient vector space, i.e., the ambient space tensored with
        the fraction field of `R`.

        EXAMPLES::

            sage: V = FreeModule(ZZ,3)
            sage: W = V.submodule([V.gen(0)])
            sage: W.span([V.gen(1)])
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [0 1 0]
            sage: W.submodule([V.gen(1)])
            Traceback (most recent call last):
            ...
            ArithmeticError: argument gens (= [(0, 1, 0)]) does not generate a submodule of self
        """
    def span_of_basis(self, basis, check: bool = True, already_echelonized: bool = False):
        """
        Return the free `R`-module with the given basis, where `R`
        is the base ring of ``self``.

        Note that this `R`-module need not be a submodule of ``self``, nor
        even of the ambient space.  It must, however, be contained in
        the ambient vector space, i.e., the ambient space tensored
        with the fraction field of `R`.

        EXAMPLES::

            sage: M = FreeModule(ZZ,3)
            sage: W = M.span_of_basis([M([1,2,3])])

        Next we create two free `\\ZZ`-modules, neither of which is a
        submodule of `W`::

            sage: W.span_of_basis([M([2,4,0])])
            Free module of degree 3 and rank 1 over Integer Ring
            User basis matrix:
            [2 4 0]

        The following module is not even in the ambient space::

            sage: Q = QQ
            sage: W.span_of_basis([ Q('1/5')*M([1,2,0]), Q('1/7')*M([1,1,0]) ])
            Free module of degree 3 and rank 2 over Integer Ring
            User basis matrix:
            [1/5 2/5   0]
            [1/7 1/7   0]

        Of course the input basis vectors must be linearly independent::

            sage: W.span_of_basis([ [1,2,0], [2,4,0] ])
            Traceback (most recent call last):
            ...
            ValueError: The given basis vectors must be linearly independent.
        """
    def zero_submodule(self):
        """
        Return the zero submodule of this module.

        EXAMPLES::

            sage: V = FreeModule(ZZ,2)
            sage: V.zero_submodule()
            Free module of degree 2 and rank 0 over Integer Ring
            Echelon basis matrix:
            []
        """

class FreeQuadraticModule_generic_field(free_module.FreeModule_generic_field, FreeQuadraticModule_generic_pid):
    """
    Base class for all free modules over fields.
    """
    def __init__(self, base_field, dimension, degree, inner_product_matrix, sparse: bool = False) -> None:
        """
        Create a vector space over a field.

        EXAMPLES::

            sage: FreeModule(QQ, 2, inner_product_matrix=[[2,1],[1,2]])
            Ambient quadratic space of dimension 2 over Rational Field
            Inner product matrix:
            [2 1]
            [1 2]
            sage: FreeModule(FiniteField(2), 7, inner_product_matrix=1)
            Ambient quadratic space of dimension 7 over Finite Field of size 2
            Inner product matrix:
            [1 0 0 0 0 0 0]
            [0 1 0 0 0 0 0]
            [0 0 1 0 0 0 0]
            [0 0 0 1 0 0 0]
            [0 0 0 0 1 0 0]
            [0 0 0 0 0 1 0]
            [0 0 0 0 0 0 1]
        """
    def span(self, gens, check: bool = True, already_echelonized: bool = False):
        """
        Return the `K`-span of the given list of gens, where `K` is the
        base field of ``self``.

        Note that this span is a subspace of the ambient vector space,
        but need not be a subspace of ``self``.

        INPUT:

        - ``gens`` -- list of vectors

        - ``check`` -- boolean (default: ``True``); whether or not to coerce
          entries of gens into base field

        - ``already_echelonized`` -- boolean (default: ``False``); set this if
          you know the gens are already in echelon form

        EXAMPLES::

            sage: V = VectorSpace(GF(7), 3)
            sage: W = V.subspace([[2,3,4]]); W
            Vector space of degree 3 and dimension 1 over Finite Field of size 7
            Basis matrix:
            [1 5 2]
            sage: W.span([[1,1,1]])
            Vector space of degree 3 and dimension 1 over Finite Field of size 7
            Basis matrix:
            [1 1 1]
        """
    def span_of_basis(self, basis, check: bool = True, already_echelonized: bool = False):
        """
        Return the free `K`-module with the given basis, where `K`
        is the base field of ``self``.

        Note that this span is a subspace of the ambient vector space,
        but need not be a subspace of ``self``.

        INPUT:

        - ``basis`` -- list of vectors

        - ``check`` -- boolean (default: ``True``); whether or not to coerce
          entries of gens into base field

        - ``already_echelonized`` -- boolean (default: ``False``); set this if
          you know the gens are already in echelon form

        EXAMPLES::

            sage: V = VectorSpace(GF(7), 3)
            sage: W = V.subspace([[2,3,4]]); W
            Vector space of degree 3 and dimension 1 over Finite Field of size 7
            Basis matrix:
            [1 5 2]
            sage: W.span_of_basis([[2,2,2], [3,3,0]])
            Vector space of degree 3 and dimension 2 over Finite Field of size 7
            User basis matrix:
            [2 2 2]
            [3 3 0]

        The basis vectors must be linearly independent or a
        :exc:`ValueError` exception is raised::

            sage: W.span_of_basis([[2,2,2], [3,3,3]])
            Traceback (most recent call last):
            ...
            ValueError: The given basis vectors must be linearly independent.
        """

class FreeQuadraticModule_ambient(free_module.FreeModule_ambient, FreeQuadraticModule_generic):
    """
    Ambient free module over a commutative ring.
    """
    def __init__(self, base_ring, rank, inner_product_matrix, sparse: bool = False) -> None:
        """
        The free module of given rank over the given ``base_ring``.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``rank`` -- nonnegative integer

        EXAMPLES::

            sage: FreeModule(ZZ, 4)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
        """

class FreeQuadraticModule_ambient_domain(free_module.FreeModule_ambient_domain, FreeQuadraticModule_ambient):
    """
    Ambient free quadratic module over an integral domain.
    """
    def __init__(self, base_ring, rank, inner_product_matrix, sparse: bool = False) -> None:
        """
        EXAMPLES::

            sage: FreeModule(PolynomialRing(GF(5),'x'), 3)
            Ambient free module of rank 3 over the principal ideal domain
            Univariate Polynomial Ring in x over Finite Field of size 5
        """
    def ambient_vector_space(self):
        """
        Return the ambient vector space, which is this free module tensored
        with its fraction field.

        EXAMPLES::

            sage: M = ZZ^3;  M.ambient_vector_space()
            Vector space of dimension 3 over Rational Field
        """

class FreeQuadraticModule_ambient_pid(free_module.FreeModule_ambient_pid, FreeQuadraticModule_generic_pid, FreeQuadraticModule_ambient_domain):
    """
    Ambient free quadratic module over a principal ideal domain.
    """
    def __init__(self, base_ring, rank, inner_product_matrix, sparse: bool = False) -> None:
        """
        Create the ambient free module of given rank over the given
        principal ideal domain.

        INPUT:

        - ``base_ring`` -- a principal ideal domain

        - ``rank`` -- nonnegative integer

        - ``sparse`` -- boolean (default: ``False``)

        - ``inner_product_matrix`` -- boolean (default: ``None``)

        EXAMPLES::

            sage: ZZ^3
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: FreeModule(ZZ,3,inner_product_matrix=Matrix([[2,-1,0],[-1,2,-1],[0,-1,2]]))
            Ambient free quadratic module of rank 3 over the principal ideal domain Integer Ring
            Inner product matrix:
            [ 2 -1  0]
            [-1  2 -1]
            [ 0 -1  2]
        """

class FreeQuadraticModule_ambient_field(free_module.FreeModule_ambient_field, FreeQuadraticModule_generic_field, FreeQuadraticModule_ambient_pid):
    def __init__(self, base_field, dimension, inner_product_matrix, sparse: bool = False) -> None:
        """
        Create the ambient vector space of given dimension over the given field.

        INPUT:

        - ``base_field`` -- a field

        - ``dimension`` -- nonnegative integer

        - ``sparse`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: VectorSpace(QQ,3,inner_product_matrix=[[2,1,0],[1,2,0],[0,1,2]])
            Ambient quadratic space of dimension 3 over Rational Field
            Inner product matrix:
            [2 1 0]
            [1 2 0]
            [0 1 2]

        TESTS:

        Check for :issue:`10606`::

            sage: D = matrix.diagonal(ZZ, [1,1])
            sage: V = VectorSpace(GF(46349), 2, inner_product_matrix=D)                 # needs sage.rings.finite_rings
            sage: deepcopy(V)                                                           # needs sage.rings.finite_rings
            Ambient quadratic space of dimension 2 over Finite Field
            of size 46349
            Inner product matrix:
            [1 0]
            [0 1]
        """

class FreeQuadraticModule_submodule_with_basis_pid(free_module.FreeModule_submodule_with_basis_pid, FreeQuadraticModule_generic_pid):
    """
    An `R`-submodule of `K^n` with distinguished basis, where `K` is
    the fraction field of a principal ideal domain `R`.

    Modules are ordered by inclusion.

    EXAMPLES:

    First we compare two equal vector spaces::

        sage: A = FreeQuadraticModule(QQ,3,2*matrix.identity(3))
        sage: V = A.span([[1,2,3], [5,6,7], [8,9,10]])
        sage: W = A.span([[5,6,7], [8,9,10]])
        sage: V == W
        True

    Next we compare a one dimensional space to the two dimensional
    space defined above::

        sage: M = A.span([[5,6,7]])
        sage: V == M
        False
        sage: M < V
        True
        sage: V < M
        False

    We compare a `\\ZZ`-module to the one-dimensional space above::

        sage: V = A.span([[5,6,7]])
        sage: V = V.change_ring(ZZ).scale(1/11)
        sage: V < M
        True
        sage: M < V
        False
    """
    def __init__(self, ambient, basis, inner_product_matrix, check: bool = True, echelonize: bool = False, echelonized_basis=None, already_echelonized: bool = False) -> None:
        """
        Create a free module with basis over a PID.

        EXAMPLES::

            sage: A = diagonal_matrix([1,2,2])
            sage: M = FreeQuadraticModule(ZZ,3,inner_product_matrix=A)
            sage: W = M.span_of_basis([[1,2,3],[4,5,6]]); W
            Free quadratic module of degree 3 and rank 2 over Integer Ring
            Basis matrix:
            [1 2 3]
            [4 5 6]
            Inner product matrix:
            [1 0 0]
            [0 2 0]
            [0 0 2]

            sage: W = M.span_of_basis([[1,2,3/2],[4,5,6]]); W
            Free quadratic module of degree 3 and rank 2 over Integer Ring
            Basis matrix:
            [  1   2 3/2]
            [  4   5   6]
            Inner product matrix:
            [1 0 0]
            [0 2 0]
            [0 0 2]

        TESTS:

        We test that :issue:`23703` is fixed::

            sage: A = FreeQuadraticModule(ZZ, 1, matrix.identity(1))
            sage: B = A.span([[1/2]])
            sage: C = B.span([[1]])
            sage: B.intersection(C) == C.intersection(B)
            True
        """
    def change_ring(self, R):
        """
        Return the free module over `R` obtained by coercing each
        element of ``self`` into a vector over the fraction field of `R`,
        then taking the resulting `R`-module.

        This raises a :exc:`TypeError` if coercion is not possible.

        INPUT:

        - ``R`` -- a principal ideal domain

        EXAMPLES:

        Changing rings preserves the inner product and the user basis::

            sage: V = QQ^3
            sage: W = V.subspace([[2, '1/2', 1]]); W
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [  1 1/4 1/2]
            sage: W.change_ring(GF(7))
            Vector space of degree 3 and dimension 1 over Finite Field of size 7
            Basis matrix:
            [1 2 4]

            sage: N = FreeModule(ZZ, 2, inner_product_matrix=[[1,-1], [2,5]])
            sage: N.inner_product_matrix()
            [ 1 -1]
            [ 2  5]
            sage: Np = N.change_ring(RDF)
            sage: Np.inner_product_matrix()
            [ 1.0 -1.0]
            [ 2.0  5.0]
        """

class FreeQuadraticModule_submodule_pid(free_module.FreeModule_submodule_pid, FreeQuadraticModule_submodule_with_basis_pid):
    """
    An `R`-submodule of `K^n` where `K` is the fraction field of a
    principal ideal domain `R`.

    EXAMPLES::

        sage: M = ZZ^3
        sage: W = M.span_of_basis([[1,2,3], [4,5,19]]); W
        Free module of degree 3 and rank 2 over Integer Ring
        User basis matrix:
        [ 1  2  3]
        [ 4  5 19]

    We can save and load submodules and elements::

        sage: loads(W.dumps()) == W
        True
        sage: v = W.0 + W.1
        sage: loads(v.dumps()) == v
        True
    """
    def __init__(self, ambient, gens, inner_product_matrix, check: bool = True, already_echelonized: bool = False) -> None:
        """
        Create an embedded free module over a PID.

        EXAMPLES::

            sage: V = ZZ^3
            sage: W = V.span([[1,2,3],[4,5,6]])
            sage: W
            Free module of degree 3 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1 2 3]
            [0 3 6]
        """

class FreeQuadraticModule_submodule_with_basis_field(free_module.FreeModule_submodule_with_basis_field, FreeQuadraticModule_generic_field, FreeQuadraticModule_submodule_with_basis_pid):
    """
    An embedded vector subspace with a distinguished user basis.

    EXAMPLES::

        sage: M = QQ^3; W = M.submodule_with_basis([[1,2,3], [4,5,19]]); W
        Vector space of degree 3 and dimension 2 over Rational Field
        User basis matrix:
        [ 1  2  3]
        [ 4  5 19]

    Since this is an embedded vector subspace with a distinguished user
    basis possibly different than the echelonized basis, the
    ``echelon_coordinates()`` and user ``coordinates()`` do not agree::

        sage: V = QQ^3
        sage: W = V.submodule_with_basis([[1,2,3], [4,5,6]])
        sage: W
        Vector space of degree 3 and dimension 2 over Rational Field
        User basis matrix:
        [1 2 3]
        [4 5 6]

        sage: v = V([1,5,9])
        sage: W.echelon_coordinates(v)
        [1, 5]
        sage: vector(QQ, W.echelon_coordinates(v)) * W.echelonized_basis_matrix()
        (1, 5, 9)

        sage: v = V([1,5,9])
        sage: W.coordinates(v)
        [5, -1]
        sage: vector(QQ, W.coordinates(v)) * W.basis_matrix()
        (1, 5, 9)

    We can load and save submodules::

        sage: loads(W.dumps()) == W
        True

        sage: K.<x> = FractionField(PolynomialRing(QQ,'x'))
        sage: M = K^3; W = M.span_of_basis([[1,1,x]])
        sage: loads(W.dumps()) == W
        True
    """
    def __init__(self, ambient, basis, inner_product_matrix, check: bool = True, echelonize: bool = False, echelonized_basis=None, already_echelonized: bool = False) -> None:
        """
        Create a vector space with given basis.

        EXAMPLES::

            sage: V = QQ^3
            sage: W = V.span_of_basis([[1,2,3], [4,5,6]])
            sage: W
            Vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 2 3]
            [4 5 6]
            sage: V = VectorSpace(QQ, 3, inner_product_matrix=1)
            sage: V.span_of_basis([[1,2,3], [4,5,6]])
            Quadratic space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [1 2 3]
            [4 5 6]
            Inner product matrix:
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """

class FreeQuadraticModule_submodule_field(free_module.FreeModule_submodule_field, FreeQuadraticModule_submodule_with_basis_field):
    """
    An embedded vector subspace with echelonized basis.

    EXAMPLES:

    Since this is an embedded vector subspace with echelonized basis,
    the methods :meth:`echelon_coordinates` and :meth:`coordinates` return the same
    coordinates::

        sage: V = QQ^3
        sage: W = V.span([[1,2,3], [4,5,6]])
        sage: W
        Vector space of degree 3 and dimension 2 over Rational Field
        Basis matrix:
        [ 1  0 -1]
        [ 0  1  2]

        sage: v = V([1,5,9])
        sage: W.echelon_coordinates(v)
        [1, 5]
        sage: vector(QQ, W.echelon_coordinates(v)) * W.basis_matrix()
        (1, 5, 9)

        sage: v = V([1,5,9])
        sage: W.coordinates(v)
        [1, 5]
        sage: vector(QQ, W.coordinates(v)) * W.basis_matrix()
        (1, 5, 9)
    """
    def __init__(self, ambient, gens, inner_product_matrix, check: bool = True, already_echelonized: bool = False) -> None:
        """
        Create an embedded vector subspace with echelonized basis.

        EXAMPLES::

            sage: V = QQ^3
            sage: W = V.span([[1,2,3], [4,5,6]])
            sage: W
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [ 1  0 -1]
            [ 0  1  2]
        """
