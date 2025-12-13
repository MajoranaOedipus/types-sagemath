from _typeshed import Incomplete
from sage.categories.action import Action as Action
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import LatexExpr as LatexExpr, latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement as IndexedFreeModuleElement
from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial as InfinitePolynomial
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing_dense as InfinitePolynomialRing_dense
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.sets.family import Family as Family
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def repr_from_monomials(monomials, term_repr, use_latex: bool = False) -> str:
    '''
    Return a string representation of an element of a free module
    from the dictionary ``monomials``.

    INPUT:

    - ``monomials`` -- list of pairs ``[m, c]`` where ``m`` is the index
      and ``c`` is the coefficient
    - ``term_repr`` -- a function which returns a string given an index
      (can be ``repr`` or ``latex``, for example)
    - ``use_latex`` -- boolean (default: ``False``); if ``True`` then the
      output is in latex format

    EXAMPLES::

        sage: from sage.algebras.weyl_algebra import repr_from_monomials
        sage: R.<x,y,z> = QQ[]
        sage: d = [(z, 4/7), (y, sqrt(2)), (x, -5)]                                     # needs sage.symbolic
        sage: repr_from_monomials(d, lambda m: repr(m))                                 # needs sage.symbolic
        \'4/7*z + sqrt(2)*y - 5*x\'
        sage: a = repr_from_monomials(d, lambda m: latex(m), True); a                   # needs sage.symbolic
        \\frac{4}{7} z + \\sqrt{2} y - 5 x
        sage: type(a)                                                                   # needs sage.symbolic
        <class \'sage.misc.latex.LatexExpr\'>

    The zero element::

        sage: repr_from_monomials([], lambda m: repr(m))
        \'0\'
        sage: a = repr_from_monomials([], lambda m: latex(m), True); a
        0
        sage: type(a)
        <class \'sage.misc.latex.LatexExpr\'>

    A "unity" element::

        sage: repr_from_monomials([(1, 1)], lambda m: repr(m))
        \'1\'
        sage: a = repr_from_monomials([(1, 1)], lambda m: latex(m), True); a
        1
        sage: type(a)
        <class \'sage.misc.latex.LatexExpr\'>

    ::

        sage: repr_from_monomials([(1, -1)], lambda m: repr(m))
        \'-1\'
        sage: a = repr_from_monomials([(1, -1)], lambda m: latex(m), True); a
        -1
        sage: type(a)
        <class \'sage.misc.latex.LatexExpr\'>

    Leading minus signs are dealt with appropriately::

        sage: # needs sage.symbolic
        sage: d = [(z, -4/7), (y, -sqrt(2)), (x, -5)]
        sage: repr_from_monomials(d, lambda m: repr(m))
        \'-4/7*z - sqrt(2)*y - 5*x\'
        sage: a = repr_from_monomials(d, lambda m: latex(m), True); a
        -\\frac{4}{7} z - \\sqrt{2} y - 5 x
        sage: type(a)
        <class \'sage.misc.latex.LatexExpr\'>

    Indirect doctests using a class that uses this function::

        sage: R.<x,y> = QQ[]
        sage: A = CliffordAlgebra(QuadraticForm(R, 3, [x,0,-1,3,-4,5]))
        sage: a,b,c = A.gens()
        sage: a*b*c
        e0*e1*e2
        sage: b*c
        e1*e2
        sage: (a*a + 2)
        x + 2
        sage: c*(a*a + 2)*b
        (-x - 2)*e1*e2 - 4*x - 8
        sage: latex(c*(a*a + 2)*b)
        \\left( -x - 2 \\right)  e_{1} e_{2} - 4 x - 8
    '''
def repr_factored(w, latex_output: bool = False) -> str:
    """
    Return a string representation of ``w`` with the `dx_i` generators
    factored on the right.

    EXAMPLES::

        sage: from sage.algebras.weyl_algebra import repr_factored
        sage: R.<t> = QQ[]
        sage: D = DifferentialWeylAlgebra(R)
        sage: t, dt = D.gens()
        sage: x = dt^3*t^3 + dt^2*t^4
        sage: x
        t^3*dt^3 + t^4*dt^2 + 9*t^2*dt^2 + 8*t^3*dt + 18*t*dt + 12*t^2 + 6
        sage: print(repr_factored(x))
        (12*t^2 + 6) + (8*t^3 + 18*t)*dt + (t^4 + 9*t^2)*dt^2 + (t^3)*dt^3
        sage: repr_factored(x, True)
        (12 t^{2} + 6) + (8 t^{3} + 18 t) \\frac{\\partial}{\\partial t}
         + (t^{4} + 9 t^{2}) \\frac{\\partial^{2}}{\\partial t^{2}}
         + (t^{3}) \\frac{\\partial^{3}}{\\partial t^{3}}
        sage: repr_factored(D.zero())
        '0'

    With multiple variables::

        sage: R.<x,y,z> = QQ[]
        sage: D = DifferentialWeylAlgebra(R)
        sage: x, y, z, dx, dy, dz = D.gens()
        sage: elt = dx^3*x^3 + (y^3-z*x)*dx^3 + dy^3*x^3 + dx*dy*dz*x*y*z
        sage: elt
        x^3*dy^3 + x*y*z*dx*dy*dz + y^3*dx^3 + x^3*dx^3 - x*z*dx^3 + y*z*dy*dz
         + x*z*dx*dz + x*y*dx*dy + 9*x^2*dx^2 + z*dz + y*dy + 19*x*dx + 7
        sage: print(repr_factored(elt))
        (7) + (z)*dz + (y)*dy + (y*z)*dy*dz + (x^3)*dy^3 + (19*x)*dx
         + (x*z)*dx*dz + (x*y)*dx*dy + (x*y*z)*dx*dy*dz
         + (9*x^2)*dx^2 + (x^3 + y^3 - x*z)*dx^3
        sage: repr_factored(D.zero(), True)
        0
    """

class DifferentialWeylAlgebraElement(IndexedFreeModuleElement):
    """
    An element in a differential Weyl algebra.

    TESTS:

    Some computations in the Weyl algebra, using the implicit
    coercion from the polynomial ring into the Weyl algebra::

        sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
        sage: dx,dy,dz = W.differentials()
        sage: elt = ((x^3-z)*dx + dy)^2
        sage: TestSuite(elt).run()

        sage: R.<x,y,z> =  QQ[]
        sage: W = DifferentialWeylAlgebra(R)
        sage: dx,dy,dz = W.differentials()
        sage: dy*(x^3-y*z)*dx == -z*dx + x^3*dx*dy - y*z*dx*dy
        True
        sage: W.zero() == 0
        True
        sage: W.one() == 1
        True
        sage: x == 1
        False
        sage: x + 1 == 1
        False
        sage: a = (x*y + z) * dx
        sage: 3/2 * a
        3/2*x*y*dx + 3/2*z*dx
        sage: a * 3/2
        3/2*x*y*dx + 3/2*z*dx
        sage: a / 2
        1/2*x*y*dx + 1/2*z*dx
        sage: W(x^3 - y*z) == x^3 - y*z
        True
        sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
        sage: dx,dy,dz = W.differentials()
        sage: dx != dy
        True
        sage: W.one() != 1
        False
        sage: dy - (3*x - z)*dx
        dy + z*dx - 3*x*dx
        sage: (dx*dy) + dz + x^3 - 2
        dx*dy + dz + x^3 - 2
        sage: elt = (dy - (3*x - z)*dx)
        sage: sorted(elt.monomial_coefficients().items())
        [(((0, 0, 0), (0, 1, 0)), 1),
         (((0, 0, 1), (1, 0, 0)), 1),
         (((1, 0, 0), (1, 0, 0)), -3)]
        sage: elt = dy - (3*x - z)*dx + 1
        sage: sorted(elt.support())
        [((0, 0, 0), (0, 0, 0)),
         ((0, 0, 0), (0, 1, 0)),
         ((0, 0, 1), (1, 0, 0)),
         ((1, 0, 0), (1, 0, 0))]

    Hashing works::

        sage: hash(dx) == hash(dx) # hashing works
        True

    Comparison works, even if mathematically meaningless
    (but useful e.g. for sorting)::

        sage: dx < dy or dy < dx
        True
    """
    def __iter__(self):
        """
        Return an iterator of ``self``.

        This is the iterator of ``self.list()``.

        EXAMPLES::

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: dx,dy,dz = W.differentials()
            sage: list(dy - (3*x - z)*dx)
            [(((0, 0, 0), (0, 1, 0)), 1),
             (((0, 0, 1), (1, 0, 0)), 1),
             (((1, 0, 0), (1, 0, 0)), -3)]
        """
    def list(self) -> list:
        """
        Return ``self`` as a list.

        This list consists of pairs `(m, c)`, where `m` is a pair of
        tuples indexing a basis element of ``self``, and `c` is the
        coordinate of ``self`` corresponding to this basis element.
        (Only nonzero coordinates are shown.)

        EXAMPLES::

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: dx,dy,dz = W.differentials()
            sage: elt = dy - (3*x - z)*dx
            sage: elt.list()
            [(((0, 0, 0), (0, 1, 0)), 1),
             (((0, 0, 1), (1, 0, 0)), 1),
             (((1, 0, 0), (1, 0, 0)), -3)]
        """
    def __truediv__(self, x):
        """
        Division by coefficients.

        EXAMPLES::

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: x / 2
            1/2*x
            sage: W.<x,y,z> = DifferentialWeylAlgebra(ZZ)
            sage: a = 2*x + 4*y*z
            sage: a / 2
            2*y*z + x
        """
    def factor_differentials(self) -> dict:
        """
        Return a dict representing ``self`` with the differentials
        factored out.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: D = DifferentialWeylAlgebra(R)
            sage: t, dt = D.gens()
            sage: x = dt^3*t^3 + dt^2*t^4
            sage: x
            t^3*dt^3 + t^4*dt^2 + 9*t^2*dt^2 + 8*t^3*dt + 18*t*dt + 12*t^2 + 6
            sage: x.factor_differentials()
            {(0,): 12*t^2 + 6, (1,): 8*t^3 + 18*t, (2,): t^4 + 9*t^2, (3,): t^3}
            sage: D.zero().factor_differentials()
            {}

            sage: R.<x,y,z> = QQ[]
            sage: D = DifferentialWeylAlgebra(R)
            sage: x, y, z, dx, dy, dz = D.gens()
            sage: elt = dx^3*x^3 + (y^3-z*x)*dx^3 + dy^3*x^3 + dx*dy*dz*x*y*z
            sage: elt
            x^3*dy^3 + x*y*z*dx*dy*dz + y^3*dx^3 + x^3*dx^3 - x*z*dx^3 + y*z*dy*dz
             + x*z*dx*dz + x*y*dx*dy + 9*x^2*dx^2 + z*dz + y*dy + 19*x*dx + 7
            sage: elt.factor_differentials()
            {(0, 0, 0): 7,
             (0, 0, 1): z,
             (0, 1, 0): y,
             (0, 1, 1): y*z,
             (0, 3, 0): x^3,
             (1, 0, 0): 19*x,
             (1, 0, 1): x*z,
             (1, 1, 0): x*y,
             (1, 1, 1): x*y*z,
             (2, 0, 0): 9*x^2,
             (3, 0, 0): x^3 + y^3 - x*z}
        """
    def diff(self, p):
        """
        Apply this differential operator to a polynomial.

        INPUT:

        - ``p`` -- polynomial of the underlying polynomial ring

        OUTPUT:

        The result of the left action of the Weyl algebra on the polynomial
        ring via differentiation.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: W = R.weyl_algebra()
            sage: dx, dy = W.differentials()
            sage: dx.diff(x^3)
            3*x^2
            sage: (dx*dy).diff(W(x^3*y^3))
            9*x^2*y^2
            sage: (x*dx + dy + 1).diff(x^4*y^4 + 1)
            5*x^4*y^4 + 4*x^4*y^3 + 1
        """

class DifferentialWeylAlgebra(UniqueRepresentation, Parent):
    """
    The differential Weyl algebra of a polynomial ring.

    Let `R` be a commutative ring. The (differential) Weyl algebra `W` is
    the algebra generated by `x_1, x_2, \\ldots x_n, \\partial_{x_1},
    \\partial_{x_2}, \\ldots, \\partial_{x_n}` subject to the relations:
    `[x_i, x_j] = 0`, `[\\partial_{x_i}, \\partial_{x_j}] = 0`, and
    `\\partial_{x_i} x_j = x_j \\partial_{x_i} + \\delta_{ij}`. Therefore
    `\\partial_{x_i}` is acting as the partial differential operator on `x_i`.

    The Weyl algebra can also be constructed as an iterated Ore extension
    of the polynomial ring `R[x_1, x_2, \\ldots, x_n]` by adding `x_i` at
    each step. It can also be seen as a quantization of the symmetric algebra
    `Sym(V)`, where `V` is a finite dimensional vector space over a field
    of characteristic zero, by using a modified Groenewold-Moyal
    product in the symmetric algebra.

    The Weyl algebra (even for `n = 1`) over a field of characteristic 0
    has many interesting properties.

    - It's a non-commutative domain.
    - It's a simple ring (but not in positive characteristic) that is not
      a matrix ring over a division ring.
    - It has no finite-dimensional representations.
    - It's a quotient of the universal enveloping algebra of the
      Heisenberg algebra `\\mathfrak{h}_n`.

    REFERENCES:

    - :wikipedia:`Weyl_algebra`

    INPUT:

    - ``R`` -- a (polynomial) ring
    - ``names`` -- (default: ``None``) if ``None`` and ``R`` is a
      polynomial ring, then the variable names correspond to
      those of ``R``; otherwise if ``names`` is specified, then ``R``
      is the base ring

    EXAMPLES:

    There are two ways to create a Weyl algebra, the first is from
    a polynomial ring::

        sage: R.<x,y,z> = QQ[]
        sage: W = DifferentialWeylAlgebra(R); W
        Differential Weyl algebra of polynomials in x, y, z over Rational Field

    We can call ``W.inject_variables()`` to give the polynomial ring
    variables, now as elements of ``W``, and the differentials::

        sage: W.inject_variables()
        Defining x, y, z, dx, dy, dz
        sage: (dx * dy * dz) * (x^2 * y * z + x * z * dy + 1)
        x*z*dx*dy^2*dz + z*dy^2*dz + x^2*y*z*dx*dy*dz + dx*dy*dz
         + x*dx*dy^2 + 2*x*y*z*dy*dz + dy^2 + x^2*z*dx*dz + x^2*y*dx*dy
         + 2*x*z*dz + 2*x*y*dy + x^2*dx + 2*x

    Or directly by specifying a base ring and variable names::

        sage: W.<a,b> = DifferentialWeylAlgebra(QQ); W
        Differential Weyl algebra of polynomials in a, b over Rational Field

    .. TODO::

        Implement the :meth:`graded_algebra` as a polynomial ring once
        they are considered to be graded rings (algebras).
    """
    @staticmethod
    def __classcall_private__(cls, R, names=None, n=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: W1.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: W2 = DifferentialWeylAlgebra(QQ['x,y,z'])
            sage: W1 is W2
            True
        """
    def __init__(self, R, names=None, n=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: TestSuite(W).run()
        """
    class options(GlobalOptions):
        """
        Set the global options for elements of the differential Weyl
        algebra class. The default is to have the factored
        representations turned off.

        @OPTIONS@

        If no parameters are set, then the function returns a copy of the
        options dictionary.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: D = DifferentialWeylAlgebra(R)
            sage: t,dt = D.gens()
            sage: x = dt^3*t^3 + dt^2*t^4
            sage: x
            t^3*dt^3 + t^4*dt^2 + 9*t^2*dt^2 + 8*t^3*dt + 18*t*dt + 12*t^2 + 6

            sage: D.options.factor_representation = True
            sage: x
            (12*t^2 + 6) + (8*t^3 + 18*t)*dt + (t^4 + 9*t^2)*dt^2 + (t^3)*dt^3

            sage: D.options._reset()
        """
        NAME: str
        module: str
        factor_representation: Incomplete
    def degree_on_basis(self, i):
        """
        Return the degree of the basis element indexed by ``i``.

        EXAMPLES::

            sage: W.<a,b> = DifferentialWeylAlgebra(QQ)
            sage: W.degree_on_basis( ((1, 3, 2), (0, 1, 3)) )
            10

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: dx,dy,dz = W.differentials()
            sage: elt = y*dy - (3*x - z)*dx
            sage: elt.degree()
            2
        """
    def polynomial_ring(self):
        """
        Return the associated polynomial ring of ``self``.

        EXAMPLES::

            sage: W.<a,b> = DifferentialWeylAlgebra(QQ)
            sage: W.polynomial_ring()
            Multivariate Polynomial Ring in a, b over Rational Field

        ::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: W.polynomial_ring() == R
            True
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: W.<x,y> = DifferentialWeylAlgebra(QQ)
            sage: B = W.basis()
            sage: it = iter(B)
            sage: [next(it) for i in range(20)]
            [1, x, y, dx, dy, x^2, x*y, x*dx, x*dy, y^2, y*dx, y*dy,
             dx^2, dx*dy, dy^2, x^3, x^2*y, x^2*dx, x^2*dy, x*y^2]
            sage: dx, dy = W.differentials()
            sage: sorted((dx*x).monomials(), key=str)
            [1, x*dx]
            sage: B[(x*y).support()[0]]
            x*y
            sage: sorted((dx*x).monomial_coefficients().items())
            [(((0, 0), (0, 0)), 1), (((1, 0), (1, 0)), 1)]
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        .. SEEALSO::

            :meth:`variables`, :meth:`differentials`

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: W.algebra_generators()
            Finite family {'x': x, 'y': y, 'z': z, 'dx': dx, 'dy': dy, 'dz': dz}
        """
    gens = algebra_generators
    @cached_method
    def variables(self):
        """
        Return the variables of ``self``.

        .. SEEALSO::

            :meth:`algebra_generators`, :meth:`differentials`

        EXAMPLES::

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: W.variables()
            Finite family {'x': x, 'y': y, 'z': z}
        """
    @cached_method
    def differentials(self):
        """
        Return the differentials of ``self``.

        .. SEEALSO::

            :meth:`algebra_generators`, :meth:`variables`

        EXAMPLES::

            sage: W.<x,y,z> = DifferentialWeylAlgebra(QQ)
            sage: W.differentials()
            Finite family {'dx': dx, 'dy': dy, 'dz': dz}
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        .. SEEALSO::

            :meth:`algebra_generators`

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: [W.gen(i) for i in range(6)]
            [x, y, z, dx, dy, dz]
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: W.ngens()
            6
        """
    @cached_method
    def one(self):
        """
        Return the multiplicative identity element `1`.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: W.one()
            1
        """
    @cached_method
    def zero(self):
        """
        Return the additive identity element `0`.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: W = DifferentialWeylAlgebra(R)
            sage: W.zero()
            0
        """
    @lazy_attribute
    def diff_action(self):
        """
        Left action of this Weyl algebra on the underlying polynomial ring by
        differentiation.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: W = R.weyl_algebra()
            sage: dx, dy = W.differentials()
            sage: W.diff_action
            Left action by Differential Weyl algebra of polynomials in x, y
            over Rational Field on Multivariate Polynomial Ring in x, y over
            Rational Field
            sage: W.diff_action(dx^2 + dy + 1, x^3*y^3)
            x^3*y^3 + 3*x^3*y^2 + 6*x*y^3
        """
    Element = DifferentialWeylAlgebraElement

class DifferentialWeylAlgebraAction(Action):
    """
    Left action of a Weyl algebra on its underlying polynomial ring by
    differentiation.

    EXAMPLES::

        sage: R.<x,y> = QQ[]
        sage: W = R.weyl_algebra()
        sage: dx, dy = W.differentials()
        sage: W.diff_action
        Left action by Differential Weyl algebra of polynomials in x, y
        over Rational Field on Multivariate Polynomial Ring in x, y over
        Rational Field

    ::

        sage: g = dx^2 + x*dy
        sage: p = x^5 + x^3 + y^2*x^2 + 1
        sage: W.diff_action(g, p)
        2*x^3*y + 20*x^3 + 2*y^2 + 6*x

    The action is a left action::

        sage: h = dx*x + x*y
        sage: W.diff_action(h, W.diff_action(g, p)) == W.diff_action(h*g, p)
        True

    The action endomorphism of a differential operator::

        sage: dg = W.diff_action(g); dg
        Action of dx^2 + x*dy on Multivariate Polynomial Ring in x, y over
        Rational Field under Left action by Differential Weyl algebra...
        sage: dg(p) == W.diff_action(g, p) == g.diff(p)
        True
    """
    def __init__(self, G) -> None:
        """
        INPUT:

        - ``G`` -- Weyl algebra

        EXAMPLES::

            sage: from sage.algebras.weyl_algebra import DifferentialWeylAlgebraAction
            sage: W.<x,y> = DifferentialWeylAlgebra(QQ)
            sage: DifferentialWeylAlgebraAction(W)
            Left action by Differential Weyl algebra of polynomials in x, y
            over Rational Field on Multivariate Polynomial Ring in x, y over
            Rational Field
        """

class InfGenDifferentialWeylAlgebraElement(IndexedFreeModuleElement):
    """
    An element of an infinitely generated differential Weyl algebra.

    EXAMPLES::

        sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
        sage: W.inject_variables(verbose=False)
        sage: W.zero() == 0
        True
        sage: W.one() == 1
        True
        sage: W.zero() == 1
        False
        sage: x[1] == 1
        False
        sage: W(x[1]) == x[1]
        True
        sage: W(dx[1]) == dx[1]
        True
        sage: W(x[1] + dx[2]^2) == x[1] + dx[2]^2
        True
        sage: x[1] == x[11]
        False
        sage: x[1] / 2
        1/2*x[1]
        sage: W(2) / 2
        1
        sage: (x[1] + dx[1]) * (-4/3)
        -4/3*dx[1] - 4/3*x[1]
        sage: (-4/3) * (x[1] + dx[1])
        -4/3*dx[1] - 4/3*x[1]
    """
    def __iter__(self):
        """
        Return an iterator of ``self``.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ,n=oo)
            sage: dx = W.differentials()
            sage: p = x[5] + dx[1]*x[1]
            sage: list(p)
            [((x[1], dx[1]), 1), ((x[5], 1), 1), ((1, 1), 1)]
        """
    def list(self):
        """
        Return ``self`` as a list.

        This list consists of pairs `(m, c)` where `m` is a pair of
        :class:`IndexedFreeAbelianMonoid<sage.monoids.indexed_free_monoid.IndexedFreeAbelianMonoid>`
        elements indexing a basis element of ``self``, and `c` is the
        corresponding (nonzero) coefficient. The list is sorted using graded lex
        order on the differentials, followed by graded lex order on the
        polynomial generators.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: dx = W.differentials()
            sage: p = x[5] + dx[1]*x[1]
            sage: p.list()
            [((x[1], dx[1]), 1), ((x[5], 1), 1), ((1, 1), 1)]
        """

class InfGenDifferentialWeylAlgebra(UniqueRepresentation, Parent):
    """
    The differential Weyl algebra of the polynomial ring in countably many
    variables.

    Let `R` be a commutative ring, and `\\{x_i\\}` a countable family of
    indeterminants. The differential Weyl algebra `W` is an `R`-algebra
    generated by symbols `x_i`, and `\\partial_{x_i}`, subject to the relations
    `[x_i,x_j] = [\\partial_{x_i}, \\partial_{x_j}] = 0`, and
    `[\\partial_{x_i}, x_j] = \\delta_{ij}`.

    INPUT:

    - ``R`` -- a commutative ring
    - ``names`` -- length 1 tuple of strings denoting the prefix
      for the variable names

    EXAMPLES:

    We construct an infinite Weyl algebra by using ``n=oo`` in
    :class:`DifferentialWeylAlgebra`::

        sage: W.<y> = DifferentialWeylAlgebra(QQ, n=oo); W
        Differential Weyl algebra in countably many variables y over Rational Field

    Alternatively, one can first define an
    :class:`InfinitePolynomialRing`<sage.rings.infinite_polynomial_ring.InfinitePolynomialRing_dense>`
    and then define the differential Weyl algebra of that ring::

        sage: R.<x> = InfinitePolynomialRing(QQ)
        sage: W = DifferentialWeylAlgebra(R); W
        Differential Weyl algebra in countably many variables x over Rational Field

    .. WARNING::

        Due to a bug in ``InfinitePolynomialRing`` (:issue:`36788`) trying to define the infinite Weyl
        algebra of an infinite polynomial ring with coefficients in another infinite
        polynomial ring will result in unexpected behavior::

            sage: R.<x> = InfinitePolynomialRing(QQ)
            sage: R2.<y> = InfinitePolynomialRing(R)
            sage: W = DifferentialWeylAlgebra(R2); W # known bug
            Differential Weyl algebra in countably many variables y over Infinite
            polynomial ring in x over Rational Field


    To access the variables, we can call ``W.inject_variables()``. The symbols
    defined are families that allow you to access the `i`'th polynomial or differential
    generator for each nonnegative integer `i`. Alternatively, we can access the families
    directly using the :meth:`polynomial_gens` and :meth:`differentials` methods
    respectively::

        sage: W.inject_variables()
        Defining x, dx
        sage: dx
        Lazy family (dx(i))_{i in Non negative integers}
        sage: dx[1]*x[1] - x[1]*dx[1]
        1
        sage: (dx[1] + x[1]*dx[2])*(x[5]*dx[1] + 1)
        x[5]*dx[1]^2 + x[1]*x[5]*dx[1]*dx[2] + dx[1] + x[1]*dx[2]

    TESTS::

        sage: R1.<x> = InfinitePolynomialRing(QQ)
        sage: W = DifferentialWeylAlgebra(R1['y']); W
        Differential Weyl algebra of polynomials in y over Infinite polynomial
         ring in x over Rational Field
        sage: W.inject_variables(verbose=False); R1.inject_variables(verbose=False)
        sage: dy*x[1]*y
        x_1*y*dy + x_1
        sage: R2.<x> = InfinitePolynomialRing(QQ['y'])
        sage: W = DifferentialWeylAlgebra(R2); W
        Differential Weyl algebra in countably many variables x over Univariate
         Polynomial Ring in y over Rational Field
        sage: W.differential(1)*R2.base_ring()('y')*W.gen(1)
        y*x[1]*dx[1] + y
    """
    @staticmethod
    def __classcall_private__(cls, R, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: W1.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: R = InfinitePolynomialRing(QQ)
            sage: W2 = DifferentialWeylAlgebra(R, n=oo)
            sage: W1 is W2
            True
        """
    def __init__(self, R, names=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R = InfinitePolynomialRing(QQ)
            sage: W = DifferentialWeylAlgebra(R, n=oo)
            sage: W.inject_variables()
            Defining x, dx
            sage: TestSuite(W).run()
        """
    def gen(self, i):
        """
        Return the ``i``-th polynomial generator of ``self``.

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: The polynomial generator `x_i`

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: W.gen(1)
            x[1]
            sage: W.gen(1) == x[1]
            True
        """
    @cached_method
    def polynomial_gens(self):
        """
        Return the polynomial generators of ``self``.

        OUTPUT: A (lazy) family containing the polynomial generators `x_i`.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: x = W.polynomial_gens(); x
            Lazy family (x(i))_{i in Non negative integers}
            sage: x[3] == W.gen(3)
            True
        """
    @cached_method
    def gens(self):
        """
        Return the algebra generators of ``self``.

        OUTPUT: an ordered pair (x, dx) containing families indexing each set
        of generators.

        EXAMPLES::

            sage: R = InfinitePolynomialRing(QQ)
            sage: W = DifferentialWeylAlgebra(R, n=oo)
            sage: x, dx = W.gens()
        """
    def differential(self, i):
        """
        Return the ``i``-th differential of ``self``.

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: The differential generator `\\partial_{x_i}`

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: W.inject_variables()
            Defining x, dx
            sage: W.differential(1)
            dx[1]
            sage: W.differential(1) == dx[1]
            True
        """
    @cached_method
    def differentials(self):
        """
        Return the differential generators of ``self``.

        OUTPUT: A (lazy) family containing the differential generators `\\partial_{x_i}`

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: dx = W.differentials(); dx
            Lazy family (dx(i))_{i in Non negative integers}
            sage: dx[3] == W.differential(3)
            True
        """
    @cached_method
    def zero(self):
        """
        Return the additive identity element `0` of ``self``.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: x[1] + W.zero() == x[1]
            True
            sage: x[1]*W.zero() == W.zero()
            True
        """
    @cached_method
    def one_basis(self):
        """
        Return the multiplicative identity element `1` of ``self``.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: W.one_basis() == W.one().leading_support()
            True
            sage: x[1]*W.one() == x[1]
            True
        """
    @cached_method
    def basis(self):
        """
        Return a basis for ``self``.

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: B = W.basis(); B
            Lazy family (basis map(i))_{i in The Cartesian product of
             (Free abelian monoid indexed by Non negative integers,
             Free abelian monoid indexed by Non negative integers)}
            sage: idx = W._var_index
            sage: B[(idx.an_element(), idx.one())]
            x[0]*x[1]^2*x[2]^3*x[42]
        """
    def degree_on_basis(self, x):
        """
        Return the degree of basis element indexed by ``x``. This is the total
         degree of the polynomial and differential parts of ``x``.

        INPUT:

        - ``x`` -- an index for a basis element

        OUTPUT: A nonnegative integer

        EXAMPLES::

            sage: W.<x> = DifferentialWeylAlgebra(QQ, n=oo)
            sage: W.inject_variables(verbose=False);
            sage: f = x[2]*x[3]*dx[1]^2; f.degree()
            4
        """
    Element = InfGenDifferentialWeylAlgebraElement
