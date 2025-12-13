from sage.categories.fields import Fields as Fields
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.curves.projective_curve import ProjectivePlaneCurve_field as ProjectivePlaneCurve_field
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.structure.element import Matrix as Matrix, Vector as Vector
from sage.structure.sequence import Sequence as Sequence

class ProjectiveConic_field(ProjectivePlaneCurve_field):
    """
    Create a projective plane conic curve over a field.
    See ``Conic`` for full documentation.

    EXAMPLES::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
        sage: P.<X, Y, Z> = K[]
        sage: Conic(X^2 + Y^2 - Z^2)
        Projective Conic Curve over Fraction Field of Univariate Polynomial Ring in t
         over Rational Field defined by X^2 + Y^2 - Z^2

    TESTS::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
        sage: Conic([K(1), 1, -1])._test_pickling()
    """
    def __init__(self, A, f) -> None:
        """
        See ``Conic`` for full documentation.

        EXAMPLES:

        ::

            sage: c = Conic([1, 1, 1]); c
            Projective Conic Curve over Rational Field defined by x^2 + y^2 + z^2
        """
    def base_extend(self, S):
        """
        Return the conic over ``S`` given by the same equation as ``self``.

        EXAMPLES::

            sage: c = Conic([1, 1, 1]); c
            Projective Conic Curve over Rational Field defined by x^2 + y^2 + z^2
            sage: c.has_rational_point()                                                # needs sage.libs.pari
            False
            sage: d = c.base_extend(QuadraticField(-1, 'i')); d                         # needs sage.rings.number_field
            Projective Conic Curve over Number Field in i
             with defining polynomial x^2 + 1 with i = 1*I defined by x^2 + y^2 + z^2
            sage: d.rational_point(algorithm='rnfisnorm')                               # needs sage.rings.number_field
            (i : 1 : 0)
        """
    def cache_point(self, p) -> None:
        """
        Replace the point in the cache of ``self`` by ``p`` for use
        by :meth:`rational_point` and :meth:`parametrization`.

        EXAMPLES::

            sage: c = Conic([1, -1, 1])
            sage: c.point([15, 17, 8])
            (15/8 : 17/8 : 1)
            sage: c.rational_point()
            (15/8 : 17/8 : 1)

            sage: # needs sage.libs.pari
            sage: c.cache_point(c.rational_point(read_cache=False))
            sage: c.rational_point()
            (-1 : 1 : 0)
        """
    def coefficients(self):
        """
        Give a the `6` coefficients of the conic ``self``
        in lexicographic order.

        EXAMPLES::

            sage: Conic(QQ, [1,2,3,4,5,6]).coefficients()
            [1, 2, 3, 4, 5, 6]

            sage: P.<x,y,z> = GF(13)[]
            sage: a = Conic(x^2 + 5*x*y + y^2 + z^2).coefficients(); a
            [1, 5, 0, 1, 0, 1]
            sage: Conic(a)
            Projective Conic Curve over Finite Field of size 13
            defined by x^2 + 5*x*y + y^2 + z^2
        """
    def derivative_matrix(self):
        """
        Give the derivative of the defining polynomial of
        the conic ``self``, which is a linear map,
        as a `3 \\times 3` matrix.

        EXAMPLES:

        In characteristic different from `2`, the
        derivative matrix is twice the symmetric matrix:

        ::

            sage: c = Conic(QQ, [1,1,1,1,1,0])
            sage: c.symmetric_matrix()
            [  1 1/2 1/2]
            [1/2   1 1/2]
            [1/2 1/2   0]
            sage: c.derivative_matrix()
            [2 1 1]
            [1 2 1]
            [1 1 0]

        An example in characteristic `2`::

            sage: P.<t> = GF(2)[]
            sage: c = Conic([t, 1, t^2, 1, 1, 0]); c                                    # needs sage.libs.ntl
            Projective Conic Curve over Fraction Field of Univariate
             Polynomial Ring in t over Finite Field of size 2 (using GF2X)
             defined by t*x^2 + x*y + y^2 + (t^2)*x*z + y*z
            sage: c.is_smooth()
            True
            sage: c.derivative_matrix()
            [  0   1 t^2]
            [  1   0   1]
            [t^2   1   0]
        """
    def determinant(self):
        """
        Return the determinant of the symmetric matrix that defines
        the conic ``self``.

        This is defined only if the base field has characteristic
        different from `2`.

        EXAMPLES:

        ::

            sage: C = Conic([1,2,3,4,5,6])
            sage: C.determinant()
            41/4
            sage: C.symmetric_matrix().determinant()
            41/4

        Determinants are only defined in characteristic different from `2`::

            sage: C = Conic(GF(2), [1, 1, 1, 1, 1, 0])
            sage: C.is_smooth()
            True
            sage: C.determinant()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (= Projective Conic Curve over Finite Field
            of size 2 defined by x^2 + x*y + y^2 + x*z + y*z) has no symmetric matrix
            because the base field has characteristic 2
        """
    def diagonal_matrix(self):
        """
        Return a diagonal matrix `D` and a matrix `T` such that `T^t A T = D`
        holds, where `(x, y, z) A (x, y, z)^t` is the defining polynomial
        of the conic ``self``.

        EXAMPLES:

        ::

            sage: c = Conic(QQ, [1,2,3,4,5,6])
            sage: d, t = c.diagonal_matrix(); d, t
            (
            [    1     0     0]  [   1   -1 -7/6]
            [    0     3     0]  [   0    1 -1/3]
            [    0     0 41/12], [   0    0    1]
            )
            sage: t.transpose()*c.symmetric_matrix()*t
            [    1     0     0]
            [    0     3     0]
            [    0     0 41/12]

        Diagonal matrices are only defined in characteristic different
        from `2`:

        ::

            sage: # needs sage.rings.finite_rings
            sage: c = Conic(GF(4, 'a'), [0, 1, 1, 1, 1, 1])
            sage: c.is_smooth()
            True
            sage: c.diagonal_matrix()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (= Projective Conic Curve over Finite Field
            in a of size 2^2 defined by x*y + y^2 + x*z + y*z + z^2) has
            no symmetric matrix because the base field has characteristic 2
        """
    def diagonalization(self, names=None):
        """
        Return a diagonal conic `C`, an isomorphism of schemes `M: C` -> ``self``
        and the inverse `N` of `M`.

        EXAMPLES::

            sage: Conic(GF(5), [1,0,1,1,0,1]).diagonalization()
            (Projective Conic Curve over Finite Field of size 5
              defined by x^2 + y^2 + 2*z^2,
             Scheme morphism:
              From: Projective Conic Curve over Finite Field of size 5
                    defined by x^2 + y^2 + 2*z^2
              To:   Projective Conic Curve over Finite Field of size 5
                    defined by x^2 + y^2 + x*z + z^2
              Defn: Defined on coordinates by sending (x : y : z) to (x + 2*z : y : z),
             Scheme morphism:
              From: Projective Conic Curve over Finite Field of size 5
                    defined by x^2 + y^2 + x*z + z^2
              To:   Projective Conic Curve over Finite Field of size 5
                    defined by x^2 + y^2 + 2*z^2
              Defn: Defined on coordinates by sending (x : y : z) to (x - 2*z : y : z))

        The diagonalization is only defined in characteristic different
        from 2:

        ::

            sage: Conic(GF(2), [1,1,1,1,1,0]).diagonalization()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (= Projective Conic Curve over Finite Field
            of size 2 defined by x^2 + x*y + y^2 + x*z + y*z) has no symmetric matrix
            because the base field has characteristic 2

        An example over a global function field:

        ::

            sage: K = FractionField(PolynomialRing(GF(7), 't'))
            sage: (t,) = K.gens()
            sage: C = Conic(K, [t/2,0, 1, 2, 0, 3])
            sage: C.diagonalization()
            (Projective Conic Curve over Fraction Field of Univariate
              Polynomial Ring in t over Finite Field of size 7
              defined by (-3*t)*x^2 + 2*y^2 + (3*t + 3)/t*z^2,
             Scheme morphism:
               From: Projective Conic Curve over Fraction Field of Univariate
                     Polynomial Ring in t over Finite Field of size 7
                     defined by (-3*t)*x^2 + 2*y^2 + (3*t + 3)/t*z^2
               To:   Projective Conic Curve over Fraction Field of Univariate
                     Polynomial Ring in t over Finite Field of size 7
                     defined by (-3*t)*x^2 + 2*y^2 + x*z + 3*z^2
               Defn: Defined on coordinates by sending (x : y : z) to (x - 1/t*z : y : z),
             Scheme morphism:
               From: Projective Conic Curve over Fraction Field of Univariate
                     Polynomial Ring in t over Finite Field of size 7
                     defined by (-3*t)*x^2 + 2*y^2 + x*z + 3*z^2
               To:   Projective Conic Curve over Fraction Field of Univariate
                     Polynomial Ring in t over Finite Field of size 7
                     defined by (-3*t)*x^2 + 2*y^2 + (3*t + 3)/t*z^2
               Defn: Defined on coordinates by sending (x : y : z) to (x + 1/t*z : y : z))
        """
    def gens(self) -> tuple:
        """
        Return the generators of the coordinate ring of ``self``.

        EXAMPLES:

        ::

            sage: P.<x,y,z> = QQ[]
            sage: c = Conic(x^2 + y^2 + z^2)
            sage: c.gens()                                                              # needs sage.libs.singular
            (xbar, ybar, zbar)
            sage: c.defining_polynomial()(c.gens())                                     # needs sage.libs.singular
            0

        The function ``gens()`` is required for the following construction:

        ::

            sage: C.<a,b,c> = Conic(GF(3), [1, 1, 1]); C                                # needs sage.libs.singular
            Projective Conic Curve over
             Finite Field of size 3 defined by a^2 + b^2 + c^2
        """
    def has_rational_point(self, point: bool = False, algorithm: str = 'default', read_cache: bool = True):
        """
        Return ``True`` if and only if the conic ``self``
        has a point over its base field `B`.

        If ``point`` is ``True``, then returns a second output, which is
        a rational point if one exists.

        Points are cached whenever they are found. Cached information
        is used if and only if ``read_cache`` is ``True``.

        ALGORITHM:

        The parameter ``algorithm`` specifies the algorithm
        to be used:

        - ``'default'`` -- if the base field is real or complex,
          use an elementary native Sage implementation

        - ``'magma'`` (requires Magma to be installed) --
          delegates the task to the Magma computer algebra
          system

        EXAMPLES::

            sage: Conic(RR, [1, 1, 1]).has_rational_point()
            False
            sage: Conic(CC, [1, 1, 1]).has_rational_point()
            True

            sage: Conic(RR, [1, 2, -3]).has_rational_point(point = True)
            (True, (1.73205080756888 : 0.000000000000000 : 1.00000000000000))

        Conics over polynomial rings can be solved internally::

            sage: R.<t> = QQ[]
            sage: C = Conic([-2, t^2 + 1, t^2 - 1])
            sage: C.has_rational_point()                                                # needs sage.libs.pari
            True

        And they can also be solved with Magma::

            sage: C.has_rational_point(algorithm='magma')               # optional - magma
            True
            sage: C.has_rational_point(algorithm='magma', point=True)   # optional - magma
            (True, (-t : 1 : 1))

            sage: D = Conic([t, 1, t^2])
            sage: D.has_rational_point(algorithm='magma')               # optional - magma
            False

        TESTS:

        One of the following fields comes with an embedding into the complex
        numbers, one does not. Check that they are both handled correctly by
        the Magma interface. ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: K.coerce_embedding()
            Generic morphism:
              From: Number Field in i with defining polynomial x^2 + 1 with i = 1*I
              To:   Complex Lazy Field
              Defn: i -> 1*I
            sage: Conic(K, [1,1,1]).rational_point(algorithm='magma')   # optional - magma
            (-i : 1 : 0)

            sage: # needs sage.rings.number_field
            sage: x = QQ['x'].gen()
            sage: L.<i> = NumberField(x^2 + 1, embedding=None)
            sage: Conic(L, [1,1,1]).rational_point(algorithm='magma')   # optional - magma
            (-i : 1 : 0)
            sage: L == K
            False
        """
    def has_singular_point(self, point: bool = False):
        """
        Return ``True`` if and only if the conic ``self`` has a rational
        singular point.

        If ``point`` is ``True``, then also return a rational singular
        point (or ``None`` if no such point exists).

        EXAMPLES:

        ::

            sage: c = Conic(QQ, [1,0,1]); c
            Projective Conic Curve over Rational Field defined by x^2 + z^2
            sage: c.has_singular_point(point = True)
            (True, (0 : 1 : 0))

            sage: P.<x,y,z> = GF(7)[]
            sage: e = Conic((x+y+z)*(x-y+2*z)); e
            Projective Conic Curve over Finite Field of size 7
             defined by x^2 - y^2 + 3*x*z + y*z + 2*z^2
            sage: e.has_singular_point(point = True)
            (True, (2 : 4 : 1))

            sage: Conic([1, 1, -1]).has_singular_point()
            False
            sage: Conic([1, 1, -1]).has_singular_point(point=True)
            (False, None)

        ``has_singular_point`` is not implemented over all fields
        of characteristic `2`. It is implemented over finite fields.

        ::

            sage: F.<a> = FiniteField(8)                                                # needs sage.rings.finite_rings
            sage: Conic([a, a + 1, 1]).has_singular_point(point=True)                   # needs sage.rings.finite_rings
            (True, (a + 1 : 0 : 1))

            sage: P.<t> = GF(2)[]
            sage: C = Conic(P, [t,t,1]); C
            Projective Conic Curve over Fraction Field of Univariate Polynomial Ring
             in t over Finite Field of size 2... defined by t*x^2 + t*y^2 + z^2
            sage: C.has_singular_point(point=False)
            Traceback (most recent call last):
            ...
            NotImplementedError: Sorry, find singular point on conics not implemented
            over all fields of characteristic 2.
        """
    def hom(self, x, Y=None):
        """
        Return the scheme morphism from ``self`` to ``Y`` defined by ``x``.
        Here ``x`` can be a matrix or a sequence of polynomials.
        If ``Y`` is omitted, then a natural image is found if possible.

        EXAMPLES:

        Here are a few morphisms given by matrices. In the first
        example, ``Y`` is omitted, in the second example, ``Y`` is specified.

        ::

            sage: c = Conic([-1, 1, 1])
            sage: h = c.hom(Matrix([[1,1,0],[0,1,0],[0,0,1]])); h
            Scheme morphism:
              From: Projective Conic Curve over Rational Field defined by -x^2 + y^2 + z^2
              To:   Projective Conic Curve over Rational Field defined by -x^2 + 2*x*y + z^2
              Defn: Defined on coordinates by sending (x : y : z) to (x + y : y : z)
            sage: h([-1, 1, 0])                                                         # needs sage.libs.singular
            (0 : 1 : 0)

            sage: c = Conic([-1, 1, 1])
            sage: d = Conic([4, 1, -1])
            sage: c.hom(Matrix([[0, 0, 1/2], [0, 1, 0], [1, 0, 0]]), d)
            Scheme morphism:
              From: Projective Conic Curve over Rational Field defined by -x^2 + y^2 + z^2
              To:   Projective Conic Curve over Rational Field defined by 4*x^2 + y^2 - z^2
              Defn: Defined on coordinates by sending (x : y : z) to (1/2*z : y : x)

        :exc:`ValueError` is raised if the wrong codomain ``Y`` is specified:

        ::

            sage: c = Conic([-1, 1, 1])
            sage: c.hom(Matrix([[0, 0, 1/2], [0, 1, 0], [1, 0, 0]]), c)
            Traceback (most recent call last):
            ...
            ValueError: The matrix x (= [  0   0 1/2]
                                        [  0   1   0]
                                        [  1   0   0]) does not define a map
            from self (= Projective Conic Curve over Rational Field defined by -x^2 + y^2 + z^2)
            to Y (= Projective Conic Curve over Rational Field defined by -x^2 + y^2 + z^2)

        The identity map between two representations of the same conic:

        ::

            sage: C = Conic([1,2,3,4,5,6])
            sage: D = Conic([2,4,6,8,10,12])
            sage: C.hom(identity_matrix(3), D)
            Scheme morphism:
              From: Projective Conic Curve over Rational Field
                    defined by x^2 + 2*x*y + 4*y^2 + 3*x*z + 5*y*z + 6*z^2
              To:   Projective Conic Curve over Rational Field
                    defined by 2*x^2 + 4*x*y + 8*y^2 + 6*x*z + 10*y*z + 12*z^2
              Defn: Defined on coordinates by sending (x : y : z) to (x : y : z)

        An example not over the rational numbers:

        ::

            sage: P.<t> = QQ[]
            sage: C = Conic([1,0,0,t,0,1/t])
            sage: D = Conic([1/t^2, 0, -2/t^2, t, 0, (t + 1)/t^2])
            sage: T = Matrix([[t,0,1], [0,1,0], [0,0,1]])
            sage: C.hom(T, D)
            Scheme morphism:
              From: Projective Conic Curve over Fraction Field of Univariate
                    Polynomial Ring in t over Rational Field defined by x^2 + t*y^2 + 1/t*z^2
              To:   Projective Conic Curve over Fraction Field of Univariate
                    Polynomial Ring in t over Rational Field defined by
                    1/(t^2)*x^2 + t*y^2 - 2/(t^2)*x*z + (t + 1)/(t^2)*z^2
              Defn: Defined on coordinates by sending (x : y : z) to (t*x + z : y : z)
        """
    def is_diagonal(self):
        """
        Return ``True`` if and only if the conic has the form
        `a x^2 + b y^2 + c z^2`.

        EXAMPLES:

        ::

            sage: c = Conic([1,1,0,1,0,1]); c
            Projective Conic Curve over Rational Field defined by x^2 + x*y + y^2 + z^2
            sage: d, t = c.diagonal_matrix()
            sage: c.is_diagonal()
            False
            sage: c.diagonalization()[0].is_diagonal()
            True
        """
    def is_smooth(self):
        """
        Return ``True`` if and only if ``self`` is smooth.

        EXAMPLES:

        ::

            sage: Conic([1,-1,0]).is_smooth()
            False
            sage: Conic(GF(2),[1,1,1,1,1,0]).is_smooth()
            True
        """
    def matrix(self):
        """
        Return a matrix `M` such that `(x, y, z) M (x, y, z)^t`
        is the defining equation of ``self``.

        The matrix `M` is upper triangular if the base field has
        characteristic `2` and symmetric otherwise.

        EXAMPLES::

            sage: R.<x, y, z> = QQ[]
            sage: C = Conic(x^2 + x*y + y^2 + z^2)
            sage: C.matrix()
            [  1 1/2   0]
            [1/2   1   0]
            [  0   0   1]

            sage: R.<x, y, z> = GF(2)[]
            sage: C = Conic(x^2 + x*y + y^2 + x*z + z^2)
            sage: C.matrix()
            [1 1 1]
            [0 1 0]
            [0 0 1]
        """
    def parametrization(self, point=None, morphism: bool = True):
        """
        Return a parametrization `f` of ``self`` together with the
        inverse of `f`.

        If ``point`` is specified, then that point is used
        for the parametrization. Otherwise, use :meth:`rational_point()`
        to find a point.

        If ``morphism`` is True, then `f` is returned in the form
        of a Scheme morphism. Otherwise, it is a tuple of polynomials
        that gives the parametrization.

        EXAMPLES:

        An example over a finite field ::

            sage: # needs sage.libs.pari
            sage: c = Conic(GF(2), [1,1,1,1,1,0])
            sage: f, g = c.parametrization(); f, g
            (Scheme morphism:
              From: Projective Space of dimension 1 over Finite Field of size 2
              To:   Projective Conic Curve over Finite Field of size 2
                    defined by x^2 + x*y + y^2 + x*z + y*z
              Defn: Defined on coordinates by sending (x : y) to ...,
             Scheme morphism:
              From: Projective Conic Curve over Finite Field of size 2
                    defined by x^2 + x*y + y^2 + x*z + y*z
              To:   Projective Space of dimension 1 over Finite Field of size 2
              Defn: Defined on coordinates by sending (x : y : z) to ...)
            sage: set(f(p) for p in f.domain())
            {(0 : 0 : 1), (0 : 1 : 1), (1 : 0 : 1)}

        Verification of the example ::

            sage: # needs sage.libs.pari
            sage: h = g*f; h
            Scheme endomorphism of Projective Space of dimension 1
             over Finite Field of size 2
              Defn: Defined on coordinates by sending (x : y) to ...
            sage: h[0]/h[1]
            x/y
            sage: h.is_one()                    # known bug (see :issue:`31892`)
            True
            sage: (x,y,z) = c.gens()
            sage: x.parent()
            Quotient of Multivariate Polynomial Ring in x, y, z
             over Finite Field of size 2 by the ideal (x^2 + x*y + y^2 + x*z + y*z)
            sage: k = f*g
            sage: k[0]*z-k[2]*x
            0
            sage: k[1]*z-k[2]*y
            0

        The morphisms are mathematically defined in all points,
        but don't work completely in SageMath (see :issue:`31892`) ::

            sage: # needs sage.libs.pari
            sage: f, g = c.parametrization([0,0,1])
            sage: g([0,1,1])
            (1 : 0)
            sage: f([1,0])
            (0 : 1 : 1)
            sage: f([1,1])
            (0 : 0 : 1)
            sage: g([0,0,1])
            (1 : 1)

        An example with ``morphism = False`` ::

            sage: # needs sage.libs.pari
            sage: R.<x,y,z> = QQ[]
            sage: C = Curve(7*x^2 + 2*y*z + z^2)
            sage: (p, i) = C.parametrization(morphism=False); (p, i)
            ([-2*x*y, x^2 + 7*y^2, -2*x^2], [-1/2*x, 1/7*y + 1/14*z])
            sage: C.defining_polynomial()(p)
            0
            sage: i[0](p) / i[1](p)
            x/y

        A :exc:`ValueError` is raised if ``self`` has no rational point ::

            sage: # needs sage.libs.pari
            sage: C = Conic(x^2 + y^2 + 7*z^2)
            sage: C.parametrization()
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Rational Field defined by
            x^2 + y^2 + 7*z^2 has no rational points over Rational Field!

        A :exc:`ValueError` is raised if ``self`` is not smooth ::

            sage: # needs sage.libs.pari
            sage: C = Conic(x^2 + y^2)
            sage: C.parametrization()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (=Projective Conic Curve over Rational Field
            defined by x^2 + y^2) is not smooth, hence does not have a parametrization.
        """
    def point(self, v, check: bool = True):
        """
        Construct a point on ``self`` corresponding to the input ``v``.

        If ``check`` is True, then checks if ``v`` defines a valid
        point on ``self``.

        If no rational point on ``self`` is known yet, then also caches the point
        for use by :meth:`rational_point` and :meth:`parametrization`.

        EXAMPLES::

            sage: c = Conic([1, -1, 1])
            sage: c.point([15, 17, 8])
            (15/8 : 17/8 : 1)
            sage: c.rational_point()
            (15/8 : 17/8 : 1)
            sage: d = Conic([1, -1, 1])
            sage: d.rational_point()                                                    # needs sage.libs.pari
            (-1 : 1 : 0)
        """
    def random_rational_point(self, *args1, **args2):
        """
        Return a random rational point of the conic ``self``.

        ALGORITHM:

        1. Compute a parametrization `f` of ``self`` using :meth:`parametrization`.
        2. Computes a random point `(x:y)` on the projective line.
        3. Output `f(x:y)`.

        The coordinates `x` and `y` are computed using
        ``B.random_element``, where ``B`` is the base field of
        ``self`` and additional arguments to ``random_rational_point``
        are passed to ``random_element``.

        If the base field is a finite field, then the
        output is uniformly distributed over the points of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: c = Conic(GF(2), [1,1,1,1,1,0])
            sage: [c.random_rational_point() for i in range(10)]              # random
            [(1 : 0 : 1), (1 : 0 : 1), (1 : 0 : 1), (0 : 1 : 1), (1 : 0 : 1),
             (0 : 0 : 1), (1 : 0 : 1), (1 : 0 : 1), (0 : 0 : 1), (1 : 0 : 1)]
            sage: d = Conic(QQ, [1, 1, -1])
            sage: d.random_rational_point(den_bound=1, num_bound=5)           # random
            (-24/25 : 7/25 : 1)
            sage: Conic(QQ, [1, 1, 1]).random_rational_point()
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Rational Field defined by
            x^2 + y^2 + z^2 has no rational points over Rational Field!
        """
    def rational_point(self, algorithm: str = 'default', read_cache: bool = True):
        """
        Return a point on ``self`` defined over the base field.

        This raises a :exc:`ValueError` if no rational point exists.

        See ``self.has_rational_point`` for the algorithm used
        and for the use of the parameters ``algorithm`` and ``read_cache``.

        EXAMPLES:

        Examples over `\\QQ` ::

            sage: R.<x,y,z> = QQ[]

            sage: # needs sage.libs.pari
            sage: C = Conic(7*x^2 + 2*y*z + z^2)
            sage: C.rational_point()
            (0 : 1 : 0)
            sage: C = Conic(x^2 + 2*y^2 + z^2)
            sage: C.rational_point()
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Rational Field defined by
            x^2 + 2*y^2 + z^2 has no rational points over Rational Field!

            sage: C = Conic(x^2 + y^2 + 7*z^2)
            sage: C.rational_point(algorithm='rnfisnorm')
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Rational Field defined by
            x^2 + y^2 + 7*z^2 has no rational points over Rational Field!

        Examples over number fields ::

            sage: # needs sage.rings.number_field
            sage: P.<x> = QQ[]
            sage: L.<b> = NumberField(x^3 - 5)
            sage: C = Conic(L, [3, 2, -b])
            sage: p = C.rational_point(algorithm='rnfisnorm')
            sage: p                                         # output is random
            (1/3*b^2 - 4/3*b + 4/3 : b^2 - 2 : 1)
            sage: C.defining_polynomial()(list(p))
            0

            sage: K.<i> = QuadraticField(-1)                                            # needs sage.rings.number_field
            sage: D = Conic(K, [3, 2, 5])                                               # needs sage.rings.number_field
            sage: D.rational_point(algorithm='rnfisnorm')   # output is random          # needs sage.rings.number_field
            (-3 : 4*i : 1)

            sage: # needs sage.libs.pari sage.rings.number_field
            sage: L.<s> = QuadraticField(2)
            sage: Conic(QQ, [1, 1, -3]).has_rational_point()
            False
            sage: E = Conic(L, [1, 1, -3])
            sage: E.rational_point()                        # output is random
            (-1 : -s : 1)

        Currently Magma is better at solving conics over number fields than
        Sage, so it helps to use the algorithm 'magma' if Magma is installed::

            sage: # optional - magma, needs sage.rings.number_field
            sage: q = C.rational_point(algorithm='magma',
            ....:                      read_cache=False)
            sage: q                                         # output is random
            (1/5*b^2 : 1/5*b^2 : 1)
            sage: C.defining_polynomial()(list(q))
            0
            sage: len(str(p)) > 1.5*len(str(q))
            True
            sage: D.rational_point(algorithm='magma',       # random
            ....:                  read_cache=False)
            (1 : 2*i : 1)
            sage: E.rational_point(algorithm='magma',       # random
            ....:                  read_cache=False)
            (-s : 1 : 1)

            sage: # needs sage.libs.pari sage.rings.number_field
            sage: F = Conic([L.gen(), 30, -20])
            sage: q = F.rational_point(algorithm='magma')       # optional - magma
            sage: q  # random                                   # optional - magma
            (-10/7*s + 40/7 : 5/7*s - 6/7 : 1)
            sage: p = F.rational_point(read_cache=False)
            sage: p  # random
            (788210*s - 1114700 : -171135*s + 242022 : 1)
            sage: len(str(p)) > len(str(q))                     # optional - magma
            True

            sage: # needs sage.rings.number_field
            sage: G = Conic([L.gen(), 30, -21])
            sage: G.has_rational_point(algorithm='magma')       # optional - magma
            False
            sage: G.has_rational_point(read_cache=False)        # needs sage.libs.pari
            False
            sage: G.has_rational_point(algorithm='local',
            ....:                      read_cache=False)
            False
            sage: G.rational_point(algorithm='magma')           # optional - magma
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Number Field in s
            with defining polynomial x^2 - 2 with s = 1.414213562373095?
            defined by s*x^2 + 30*y^2 - 21*z^2 has no rational points over
            Number Field in s with defining polynomial x^2 - 2 with s = 1.414213562373095?!
            sage: G.rational_point(algorithm='magma',           # optional - magma
            ....:                  read_cache=False)
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Number Field in s
            with defining polynomial x^2 - 2 with s = 1.414213562373095?
            defined by s*x^2 + 30*y^2 - 21*z^2 has no rational points over
            Number Field in s with defining polynomial x^2 - 2 with s = 1.414213562373095?!

        Examples over finite fields ::

            sage: F.<a> = FiniteField(7^20)                                             # needs sage.rings.finite_rings
            sage: C = Conic([1, a, -5]); C                                              # needs sage.rings.finite_rings
            Projective Conic Curve over Finite Field in a of size 7^20
            defined by x^2 + a*y^2 + 2*z^2
            sage: C.rational_point()                        # output is random          # needs sage.rings.finite_rings
            (4*a^19 + 5*a^18 + 4*a^17 + a^16 + 6*a^15 + 3*a^13 + 6*a^11 + a^9
               + 3*a^8 + 2*a^7 + 4*a^6 + 3*a^5 + 3*a^4 + a^3 + a + 6
             : 5*a^18 + a^17 + a^16 + 6*a^15 + 4*a^14 + a^13 + 5*a^12 + 5*a^10
               + 2*a^9 + 6*a^8 + 6*a^7 + 6*a^6 + 2*a^4 + 3
             : 1)

        Examples over `\\RR` and `\\CC` ::

            sage: Conic(CC, [1, 2, 3]).rational_point()
            (0 : 1.22474487139159*I : 1)

            sage: Conic(RR, [1, 1, 1]).rational_point()
            Traceback (most recent call last):
            ...
            ValueError: Conic Projective Conic Curve over Real Field
            with 53 bits of precision defined by x^2 + y^2 + z^2 has
            no rational points over Real Field with 53 bits of precision!
        """
    def singular_point(self):
        """
        Return a singular rational point of ``self``.

        EXAMPLES:

        ::

            sage: Conic(GF(2), [1,1,1,1,1,1]).singular_point()
            (1 : 1 : 1)

        :exc:`ValueError` is raised if the conic has no rational
        singular point

        ::

            sage: Conic(QQ, [1,1,1,1,1,1]).singular_point()
            Traceback (most recent call last):
            ...
            ValueError: The conic self (= Projective Conic Curve over Rational Field
            defined by x^2 + x*y + y^2 + x*z + y*z + z^2) has no rational singular point
        """
    def symmetric_matrix(self):
        """
        The symmetric matrix `M` such that `(x y z) M (x y z)^t`
        is the defining equation of ``self``.

        EXAMPLES::

            sage: R.<x, y, z> = QQ[]
            sage: C = Conic(x^2 + x*y/2 + y^2 + z^2)
            sage: C.symmetric_matrix()
            [  1 1/4   0]
            [1/4   1   0]
            [  0   0   1]

            sage: C = Conic(x^2 + 2*x*y + y^2 + 3*x*z + z^2)
            sage: v = vector([x, y, z])
            sage: v * C.symmetric_matrix() * v
            x^2 + 2*x*y + y^2 + 3*x*z + z^2
        """
    def upper_triangular_matrix(self):
        """
        The upper-triangular matrix `M` such that `(x y z) M (x y z)^t`
        is the defining equation of ``self``.

        EXAMPLES::

            sage: R.<x, y, z> = QQ[]
            sage: C = Conic(x^2 + x*y + y^2 + z^2)
            sage: C.upper_triangular_matrix()
            [1 1 0]
            [0 1 0]
            [0 0 1]

            sage: C = Conic(x^2 + 2*x*y + y^2 + 3*x*z + z^2)
            sage: v = vector([x, y, z])
            sage: v * C.upper_triangular_matrix() * v
            x^2 + 2*x*y + y^2 + 3*x*z + z^2
        """
    def variable_names(self):
        """
        Return the variable names of the defining polynomial of ``self``.

        EXAMPLES:

        ::

            sage: c = Conic([1,1,0,1,0,1], 'x,y,z')
            sage: c.variable_names()
            ('x', 'y', 'z')
            sage: c.variable_name()
            'x'

        The function ``variable_names()`` is required
        for the following construction:

        ::

            sage: C.<p,q,r> = Conic(QQ, [1, 1, 1]); C                                   # needs sage.libs.singular
            Projective Conic Curve over Rational Field defined by p^2 + q^2 + r^2
        """
