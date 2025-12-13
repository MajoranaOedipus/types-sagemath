from sage.categories.algebras import Algebras as Algebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.modules.free_module import FreeModule as FreeModule
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid as FreeAbelianMonoid
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.element import Matrix as Matrix

class qCommutingPolynomials_generic(CombinatorialFreeModule):
    """
    Base class for algebra of `q`-commuting (Laurent, etc.) polynomials.

    Let `R` be a commutative ring, and fix an element `q \\in R`. Let
    `B = (B_{xy})_{x,y \\in I}`  be a skew-symmetric bilinear form with
    index set `I`. Let `R[I]_{q,B}` denote the polynomial ring in the variables
    `I` such that we have the `q`-*commuting* relation for `x, y \\in I`:

    .. MATH::

        y x = q^{B_{xy}} \\cdot x y.

    This is a graded `R`-algebra with a natural basis given by monomials
    written in increasing order with respect to some total order on `I`.
    """
    @staticmethod
    def __classcall__(cls, q, n=None, B=None, base_ring=None, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R1.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R2 = algebras.qCommutingPolynomials(q, base_ring=q.parent(), names='x,y,z')
            sage: R3 = algebras.qCommutingPolynomials(q, names=['x', 'y', 'z'])
            sage: R1 is R2 is R3
            True
        """
    def __init__(self, q, B, indices, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: TestSuite(R).run()
        """
    def gen(self, i):
        """
        Return the ``i``-generator of ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.gen(0)
            x
            sage: R.gen(2)
            z
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.gens()
            (x, y, z)
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.algebra_generators()
            Finite family {'x': x, 'y': y, 'z': z}
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the monomial index by ``m``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.degree_on_basis(R.one_basis())
            0
            sage: f = (x + y)^3 + z^3
            sage: f.degree()
            3
        """
    def dimension(self):
        """
        Return the dimension of ``self``, which is `\\infty`.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.dimension()
            +Infinity
        """
    def q(self):
        """
        Return the parameter `q`.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.q() == q
            True
        """

class qCommutingPolynomials(qCommutingPolynomials_generic):
    """
    The algebra of `q`-commuting polynomials.

    Let `R` be a commutative ring, and fix an element `q \\in R`. Let
    `B = (B_{xy})_{x,y \\in I}`  be a skew-symmetric bilinear form with
    index set `I`. Let `R[I]_{q,B}` denote the polynomial ring in the variables
    `I` such that we have the `q`-*commuting* relation for `x, y \\in I`:

    .. MATH::

        y x = q^{B_{xy}} \\cdot x y.

    This is a graded `R`-algebra with a natural basis given by monomials
    written in increasing order with respect to some total order on `I`.

    When `B_{xy} = 1` and `B_{yx} = -1` for all `x < y`, then we have
    a `q`-analog of the classical binomial coefficient theorem:

    .. MATH::

        (x + y)^n = \\sum_{k=0}^n \\binom{n}{k}_q x^k y^{n-k}.

    EXAMPLES::

        sage: q = ZZ['q'].fraction_field().gen()
        sage: R.<x,y> = algebras.qCommutingPolynomials(q)

    We verify a case of the `q`-binomial theorem::

        sage: f = (x + y)^10
        sage: all(f[b] == q_binomial(10, b.list()[0]) for b in f.support())
        True

    We now do a computation with a non-standard `B` matrix::

        sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
        sage: B
        [ 0  1  2]
        [-1  0  3]
        [-2 -3  0]
        sage: q = ZZ['q'].gen()
        sage: R.<x,y,z> = algebras.qCommutingPolynomials(q, B)
        sage: y * x
        q*x*y
        sage: z * x
        q^2*x*z
        sage: z * y
        q^3*y*z

        sage: f = (x + z)^10
        sage: all(f[b] == q_binomial(10, b.list()[0], q^2) for b in f.support())
        True

        sage: f = (y + z)^10
        sage: all(f[b] == q_binomial(10, b.list()[1], q^3) for b in f.support())
        True
    """
    def __init__(self, q, B, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: TestSuite(R).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis index of the element `1`.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.one_basis()
            1
        """
    def product_on_basis(self, x, y):
        """
        Return the product of two monomials given by ``x`` and ``y``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y> = algebras.qCommutingPolynomials(q)
            sage: R.product_on_basis(x.leading_support(), y.leading_support())
            x*y
            sage: R.product_on_basis(y.leading_support(), x.leading_support())
            q*x*y

            sage: x * y
            x*y
            sage: y * x
            q*x*y
            sage: y^2 * x
            q^2*x*y^2
            sage: y * x^2
            q^2*x^2*y
            sage: x * y * x
            q*x^2*y
            sage: y^2 * x^2
            q^4*x^2*y^2
            sage: (x + y)^2
            x^2 + (q+1)*x*y + y^2
            sage: (x + y)^3
            x^3 + (q^2+q+1)*x^2*y + (q^2+q+1)*x*y^2 + y^3
            sage: (x + y)^4
            x^4 + (q^3+q^2+q+1)*x^3*y + (q^4+q^3+2*q^2+q+1)*x^2*y^2 + (q^3+q^2+q+1)*x*y^3 + y^4

        With a non-standard `B` matrix::

            sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q, B=B)
            sage: x * y
            x*y
            sage: y * x^2
            q^2*x^2*y
            sage: z^2 * x
            q^4*x*z^2
            sage: z^2 * x^3
            q^12*x^3*z^2
            sage: z^2 * y
            q^6*y*z^2
            sage: z^2 * y^3
            q^18*y^3*z^2
        """

class qCommutingLaurentPolynomials(qCommutingPolynomials_generic):
    """
    The algebra of `q`-commuting Laurent polynomials.

    Let `R` be a commutative ring, and fix an element `q \\in R`. Let
    `B = (B_{xy})_{x,y \\in I}`  be a skew-symmetric bilinear form with
    index set `I`. Let `R[I]_{q,B}` denote the Laurent polynomial ring in
    the variables `I` such that we have the `q`-*commuting* relation
    for `x, y \\in I`:

    .. MATH::

        y x = q^{B_{xy}} \\cdot x y.

    This is a graded `R`-algebra with a natural basis given by monomials
    written in increasing order with respect to some total order on `I`.

    EXAMPLES::

        sage: q = ZZ['q'].fraction_field().gen()
        sage: R.<x,y> = algebras.qCommutingLaurentPolynomials(q)

    We verify a case of the `q`-binomial theorem using inverse variables::

        sage: f = (x^-1 + y^-1)^10
        sage: all(f[b] == q_binomial(10, -b.list()[0]) for b in f.support())
        True

    We now do a computation with a non-standard `B` matrix::

        sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
        sage: B
        [ 0  1  2]
        [-1  0  3]
        [-2 -3  0]
        sage: q = ZZ['q'].gen()
        sage: R.<x,y,z> = algebras.qCommutingLaurentPolynomials(q, B)
        sage: y^-1 * x
        1/q*x*y^-1
        sage: z^-1 * x
        1/q^2*x*z^-1
        sage: z^-1 * y^-1
        q^3*y^-1*z^-1

        sage: f = (x + z^-1)^10
        sage: all(f[b] == q_binomial(10, b.list()[0], q^-2) for b in f.support())
        True

        sage: f = (y^-1 + z^-1)^10
        sage: all(f[b] == q_binomial(10, -b.list()[1], q^3) for b in f.support())
        True
    """
    def __init__(self, q, B, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingLaurentPolynomials(q)
            sage: TestSuite(R).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis index of the element `1`.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingPolynomials(q)
            sage: R.one_basis()
            1
        """
    def product_on_basis(self, x, y):
        """
        Return the product of two monomials given by ``x`` and ``y``.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y> = algebras.qCommutingLaurentPolynomials(q)
            sage: R.product_on_basis(x.leading_support(), y.leading_support())
            x*y
            sage: R.product_on_basis(y.leading_support(), x.leading_support())
            q*x*y

            sage: x * y
            x*y
            sage: y * x
            q*x*y
            sage: y^2 * x
            q^2*x*y^2
            sage: y * x^2
            q^2*x^2*y
            sage: y^-2 * x
            1/q^2*x*y^-2
            sage: y * x^-2
            1/q^2*x^-2*y
            sage: x * y * x
            q*x^2*y
            sage: x * y * ~x
            1/q*y
            sage: y^2 * x^2
            q^4*x^2*y^2
            sage: y^-2 * x^2
            1/q^4*x^2*y^-2
            sage: y^-2 * x^-2
            q^4*x^-2*y^-2
            sage: (x + y)^4
            x^4 + (q^3+q^2+q+1)*x^3*y + (q^4+q^3+2*q^2+q+1)*x^2*y^2 + (q^3+q^2+q+1)*x*y^3 + y^4

        With a non-standard `B` matrix::

            sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
            sage: q = ZZ['q'].fraction_field().gen()
            sage: R.<x,y,z> = algebras.qCommutingLaurentPolynomials(q, B=B)
            sage: x * y
            x*y
            sage: y * x^2
            q^2*x^2*y
            sage: z^2 * x
            q^4*x*z^2
            sage: z^2 * x^3
            q^12*x^3*z^2
            sage: z^2 * y
            q^6*y*z^2
            sage: z^2 * y^3
            q^18*y^3*z^2
            sage: x * y^-1
            x*y^-1
            sage: y * x^-2
            1/q^2*x^-2*y
            sage: z^-2 * x
            1/q^4*x*z^-2
            sage: z^-2 * x^-3
            q^12*x^-3*z^-2
            sage: z^2 * y^-1
            1/q^6*y^-1*z^2
            sage: z^2 * y^-3
            1/q^18*y^-3*z^2
        """
    class Element(qCommutingPolynomials_generic.Element):
        def __invert__(self):
            """
            Return the (multiplicative) inverse of ``self``.

            EXAMPLES::

                sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
                sage: q = ZZ['q'].fraction_field().gen()
                sage: R.<x,y,z> = algebras.qCommutingLaurentPolynomials(q, B=B)
                sage: ~x
                x^-1
                sage: ~(x * y^-2)
                1/q^2*x^-1*y^2
                sage: for a, b in cartesian_product([R.gens(), R.gens()]):
                ....:     elt = a * b
                ....:     assert ~elt * elt == R.one(), elt
                ....:     assert elt * ~elt == R.one(), elt
                sage: elt = x^2 * y^-3 * z
                sage: ~elt
                1/q^11*x^-2*y^3*z^-1
                sage: elt * ~elt == ~elt * elt == R.one()
                True
            """
