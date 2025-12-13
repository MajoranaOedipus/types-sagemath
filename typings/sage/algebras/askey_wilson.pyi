from sage.categories.algebras import Algebras as Algebras
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.with_basis.morphism import ModuleMorphismByLinearity as ModuleMorphismByLinearity
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

class AskeyWilsonAlgebra(CombinatorialFreeModule):
    """
    The (universal) Askey-Wilson algebra.

    Let `R` be a commutative ring. The *universal Askey-Wilson* algebra
    is an associative unital algebra `\\Delta_q` over `R[q,q^-1]` given
    by the generators `A, B, C, \\alpha, \\beta, \\gamma` that satisfy the
    following relations:

    .. MATH::

        \\begin{aligned}
        (q-q^{-1}) \\alpha &= (q^2-q^{-2}) A + qBC - q^{-1}CB, \\\\\n        (q-q^{-1}) \\beta  &= (q^2-q^{-2}) B + qCA - q^{-1}AC, \\\\\n        (q-q^{-1}) \\gamma &= (q^2-q^{-2}) C + qAB - q^{-1}BA.
        \\end{aligned}

    The universal Askey-Wilson contains a
    :meth:`Casimir element <casimir_element>` `\\Omega`, and the elements
    `\\alpha`, `\\beta`, `\\gamma`, `\\Omega` generate the center of `\\Delta_q`,
    which is isomorphic to the polynomial ring
    `(R[q,q^-1])[\\alpha,\\beta,\\gamma,\\Omega]` (assuming `q` is not a root
    of unity). Furthermore, the relations imply that `\\Delta_q` has a basis
    given by monomials `A^i B^j C^k \\alpha^r \\beta^s \\gamma^t`, where
    `i, j, k, r, s, t \\in \\ZZ_{\\geq 0}`.

    The universal Askey-Wilson algebra also admits a faithful action
    of `PSL_2(\\ZZ)` given by the automorphisms `\\rho`
    (:meth:`permutation_automorphism`):

    .. MATH::

        A \\mapsto B \\mapsto C \\mapsto A,
        \\qquad
        \\alpha \\mapsto \\beta \\mapsto \\gamma \\mapsto \\alpha.

    and `\\sigma` (:meth:`reflection_automorphism`):

    .. MATH::

        A \\mapsto B \\mapsto A,
        C \\mapsto C + \\frac{AB - BA}{q-q^{-1}},
        \\qquad
        \\alpha \\mapsto \\beta \\mapsto \\alpha,
        \\gamma \\mapsto \\gamma.

    Note that `\\rho^3 = \\sigma^2 = 1` and

    .. MATH::

        \\sigma(C) = C - q AB - (1+q^2) C + q \\gamma
                  = C - q AB - q^2 C + q \\gamma.

    The Askey-Wilson `AW_q(a,b,c)` algebra is a specialization of the
    universal Askey-Wilson algebra by `\\alpha = a`, \\beta = b`,
    `\\gamma = c`, where `a,b,c \\in R`. `AW_q(a,b,c)` was first introduced
    by [Zhedanov1991]_ to describe the Askey-Wilson polynomials. The
    Askey-Wilson algebra has a central extension of `\\Delta_q`.

    INPUT:

    - ``R`` -- a commutative ring
    - ``q`` -- (optional) the parameter `q`; must be invertible in ``R``

    If ``q`` is not specified, then ``R`` is taken to be the base
    ring of a Laurent polynomial ring with variable `q`. Otherwise
    the element ``q`` must be an element of ``R``.

    .. NOTE::

        No check is performed to ensure ``q`` is not a root of unity,
        which may lead to violations of the results in [Terwilliger2011]_.

    EXAMPLES:

    We create the universal Askey-Wilson algebra and check
    the defining relations::

        sage: AW = algebras.AskeyWilson(QQ)
        sage: AW.inject_variables()
        Defining A, B, C, a, b, g
        sage: q = AW.q()
        sage: (q^2-q^-2)*A + q*B*C - q^-1*C*B == (q-q^-1)*a
        True
        sage: (q^2-q^-2)*B + q*C*A - q^-1*A*C == (q-q^-1)*b
        True
        sage: (q^2-q^-2)*C + q*A*B - q^-1*B*A == (q-q^-1)*g
        True

    Next, we perform some computations::

        sage: C * A
        (q^-2)*A*C + (q^-3-q)*B - (q^-2-1)*b
        sage: B^2 * g^2 * A
        q^4*A*B^2*g^2 - (q^-1-q^7)*B*C*g^2 + (1-q^4)*B*g^3
         + (1-2*q^4+q^8)*A*g^2 - (q-q^3-q^5+q^7)*a*g^2
        sage: (B^3 - A) * (C^2 + q*A*B)
        q^7*A*B^4 + B^3*C^2 - (q^2-q^14)*B^3*C + (q-q^7)*B^3*g - q*A^2*B
         + (3*q^3-4*q^7+q^19)*A*B^2 - A*C^2 - (1-q^6-q^8+q^14)*B^2*a
         - (q^-2-3*q^6+3*q^14-q^22)*B*C
         + (q^-1+q-3*q^3-q^5+2*q^7-q^9+q^13+q^15-q^19)*B*g
         + (2*q^-1-6*q^3+5*q^7-2*q^19+q^23)*A
         - (2-2*q^2-4*q^4+4*q^6+q^8-q^10+q^12-q^14+q^16-q^18-q^20+q^22)*a

    We check the elements `\\alpha`, `\\beta`, and `\\gamma`
    are in the center::

        sage: all(x * gen == gen * x for gen in AW.algebra_generators() for x in [a,b,g])
        True

    We verify that the :meth:`Casimir element <casimir_element>`
    is in the center::

        sage: Omega = AW.casimir_element()
        sage: all(x * Omega == Omega * x for x in [A,B,C])
        True

        sage: x = AW.an_element()
        sage: O2 = Omega^2
        sage: x * O2 == O2 * x
        True

    We prove Lemma 2.1 in [Terwilliger2011]_::

        sage: (q^2-q^-2) * C == (q-q^-1) * g - (q*A*B - q^-1*B*A)
        True
        sage: (q-q^-1) * (q^2-q^-2) * a == (B^2*A - (q^2+q^-2)*B*A*B + A*B^2
        ....:                               + (q^2-q^-2)^2*A + (q-q^-1)^2*B*g)
        True
        sage: (q-q^-1) * (q^2-q^-2) * b == (A^2*B - (q^2+q^-2)*A*B*A + B*A^2
        ....:                               + (q^2-q^-2)^2*B + (q-q^-1)^2*A*g)
        True

    We prove Theorem 2.2 in [Terwilliger2011]_::

        sage: q3 = q^-2 + 1 + q^2
        sage: A^3*B - q3*A^2*B*A + q3*A*B*A^2 - B*A^3 == -(q^2-q^-2)^2 * (A*B - B*A)
        True
        sage: B^3*A - q3*B^2*A*B + q3*B*A*B^2 - A*B^3 == -(q^2-q^-2)^2 * (B*A - A*B)
        True
        sage: (A^2*B^2 - B^2*A^2 + (q^2+q^-2)*(B*A*B*A-A*B*A*B)
        ....:  == -(q^1-q^-1)^2 * (A*B - B*A) * g)
        True

    We construct an Askey-Wilson algebra over `\\GF{5}` at `q=2`::

        sage: AW = algebras.AskeyWilson(GF(5), q=2)
        sage: A,B,C,a,b,g = AW.algebra_generators()
        sage: q = AW.q()
        sage: Omega = AW.casimir_element()

        sage: B * A
        4*A*B + 2*g
        sage: C * A
        4*A*C + 2*b
        sage: C * B
        4*B*C + 2*a
        sage: Omega^2
        A^2*B^2*C^2 + A^3*B*C + A*B^3*C + A*B*C^3 + A^4 + 4*A^3*a
         + 2*A^2*B^2 + A^2*B*b + 2*A^2*C^2 + 4*A^2*C*g + 4*A^2*a^2
         + 4*A*B^2*a + 4*A*C^2*a + B^4 + B^3*b + 2*B^2*C^2 + 4*B^2*C*g
         + 4*B^2*b^2 + B*C^2*b + C^4 + 4*C^3*g + 4*C^2*g^2 + 2*a*b*g

        sage: (q^2-q^-2)*A + q*B*C - q^-1*C*B == (q-q^-1)*a
        True
        sage: (q^2-q^-2)*B + q*C*A - q^-1*A*C == (q-q^-1)*b
        True
        sage: (q^2-q^-2)*C + q*A*B - q^-1*B*A == (q-q^-1)*g
        True
        sage: all(x * Omega == Omega * x for x in [A,B,C])
        True

    REFERENCES:

    - [Terwilliger2011]_
    """
    @staticmethod
    def __classcall_private__(cls, R, q=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: R.<q> = LaurentPolynomialRing(QQ)
            sage: AW1 = algebras.AskeyWilson(QQ)
            sage: AW2 = algebras.AskeyWilson(R, q)
            sage: AW1 is AW2
            True

            sage: AW = algebras.AskeyWilson(ZZ, 0)
            Traceback (most recent call last):
            ...
            ValueError: q cannot be 0

            sage: AW = algebras.AskeyWilson(ZZ, 3)
            Traceback (most recent call last):
            ...
            ValueError: q=3 is not invertible in Integer Ring
        """
    def __init__(self, R, q) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: TestSuite(AW).run()  # long time
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: G = AW.algebra_generators()
            sage: G['A']
            A
            sage: G['a']
            a
            sage: list(G)
            [A, B, C, a, b, g]
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: AW.gens()
            (A, B, C, a, b, g)
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the basis element `1` of ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: AW.one_basis()
            (0, 0, 0, 0, 0, 0)
        """
    def q(self):
        """
        Return the parameter `q` of ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: q = AW.q()
            sage: q
            q
            sage: q.parent()
            Univariate Laurent Polynomial Ring in q over Rational Field
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: AW.some_elements()
            (A, B, C, a, b, g, 1,
             (q^-3+3+2*q+q^2)*a*b*g^3 + q*A*C^2*b + 3*q^2*B*a^2*g + A,
             q*A*B*C + q^2*A^2 - q*A*a + (q^-2)*B^2 - (q^-1)*B*b + q^2*C^2 - q*C*g)
        """
    @cached_method
    def casimir_element(self):
        """
        Return the Casimir element of ``self``.

        The Casimir element of the Askey-Wilson algebra `\\Delta_q` is

        .. MATH::

            \\Omega = q ABC + q^2 A^2 + q^{-2} B^2 + q^2 C^2
                     - q A\\alpha - q^{-1} B\\beta - q C\\gamma.

        The center `Z(\\Delta_q)` is generated by `\\alpha`, `\\beta`,
        `\\gamma`, and `\\Omega`.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: AW.casimir_element()
            q*A*B*C + q^2*A^2 - q*A*a + (q^-2)*B^2 - (q^-1)*B*b + q^2*C^2 - q*C*g

        We check that the Casimir element is in the center::

            sage: Omega = AW.casimir_element()
            sage: all(Omega * gen == gen * Omega for gen in AW.algebra_generators())
            True
        """
    @cached_method
    def product_on_basis(self, x, y):
        """
        Return the product of the basis elements indexed by ``x`` and ``y``.

        INPUT:

        - ``x``, ``y`` -- tuple of length 6

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: AW.product_on_basis((0,0,0,0,0,0), (3,5,2,0,12,3))
            A^3*B^5*C^2*b^12*g^3
            sage: AW.product_on_basis((0,0,0,5,3,5), (3,5,2,0,12,3))
            A^3*B^5*C^2*a^5*b^15*g^8
            sage: AW.product_on_basis((7,0,0,5,3,5), (0,5,2,0,12,3))
            A^7*B^5*C^2*a^5*b^15*g^8
            sage: AW.product_on_basis((7,3,0,5,3,5), (0,2,2,0,12,3))
            A^7*B^5*C^2*a^5*b^15*g^8
            sage: AW.product_on_basis((0,1,0,5,3,5), (2,0,0,0,5,3))
            q^4*A^2*B*a^5*b^8*g^8 - (q^-3-q^5)*A*C*a^5*b^8*g^8
             + (1-q^4)*A*a^5*b^8*g^9 - (q^-4-2+q^4)*B*a^5*b^8*g^8
             + (q^-3-q^-1-q+q^3)*a^5*b^9*g^8
            sage: AW.product_on_basis((0,2,1,0,2,0), (1,1,0,2,1,0))
            q^4*A*B^3*C*a^2*b^3 - (q^5-q^9)*A^2*B^2*a^2*b^3
             + (q^2-q^4)*A*B^2*a^3*b^3 + (q^-3-q)*B^4*a^2*b^3
             - (q^-2-1)*B^3*a^2*b^4 - (q-q^9)*B^2*C^2*a^2*b^3
             + (1-q^4)*B^2*C*a^2*b^3*g + (q^-4+2-5*q^4+2*q^12)*A*B*C*a^2*b^3
             - (q^-1+q-2*q^3-2*q^5+q^7+q^9)*A*B*a^2*b^3*g
             - (q^-3-q^3-2*q^5+q^7+q^9)*B*C*a^3*b^3
             + (q^-2-1-q^2+q^4)*B*a^3*b^3*g
             - (q^-3-2*q+2*q^9-q^13)*A^2*a^2*b^3
             + (2*q^-2-2-3*q^2+3*q^4+q^10-q^12)*A*a^3*b^3
             + (q^-7-2*q^-3+2*q^5-q^9)*B^2*a^2*b^3
             - (q^-6-q^-4-q^-2+1-q^2+q^4+q^6-q^8)*B*a^2*b^4
             - (q^-7-q^-3-2*q+2*q^5+q^9-q^13)*C^2*a^2*b^3
             + (q^-6-3-2*q^2+5*q^4-q^8+q^10-q^12)*C*a^2*b^3*g
             - (q^-1-2*q+2*q^5-q^7)*a^4*b^3
             - (q^-3-q^-1-2*q+2*q^3+q^5-q^7)*a^2*b^3*g^2
        """
    def permutation_automorphism(self):
        """
        Return the permutation automorphism `\\rho` of ``self``.

        We define the automorphism `\\rho` by

        .. MATH::

            A \\mapsto B \\mapsto C \\mapsto A,
            \\qquad
            \\alpha \\mapsto \\beta \\mapsto \\gamma \\mapsto \\alpha.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: rho = AW.permutation_automorphism()
            sage: [rho(gen) for gen in AW.algebra_generators()]
            [B, C, A, b, g, a]

            sage: AW.an_element()
            (q^-3+3+2*q+q^2)*a*b*g^3 + q*A*C^2*b + 3*q^2*B*a^2*g + A
            sage: rho(AW.an_element())
            (q^-3+3+2*q+q^2)*a^3*b*g + q^5*A^2*B*g + 3*q^2*C*a*b^2
             - (q^-2-q^6)*A*C*g + (q-q^5)*A*g^2 - (q^-3-2*q+q^5)*B*g
             + (q^-2-1-q^2+q^4)*b*g + B

            sage: r3 = rho * rho * rho
            sage: [r3(gen) for gen in AW.algebra_generators()]
            [A, B, C, a, b, g]
            sage: r3(AW.an_element()) == AW.an_element()
            True
        """
    rho = permutation_automorphism
    def reflection_automorphism(self):
        """
        Return the reflection automorphism `\\sigma` of ``self``.

        We define the automorphism `\\sigma` by

        .. MATH::

            A \\mapsto B \\mapsto A,
            \\qquad
            C \\mapsto C + \\frac{AB - BA}{q-q^{-1}}
            = C - qAB - (1+q^2) C + q \\gamma,

        .. MATH::

            \\alpha \\mapsto \\beta \\mapsto \\alpha,
            \\gamma \\mapsto \\gamma.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: sigma = AW.reflection_automorphism()
            sage: [sigma(gen) for gen in AW.algebra_generators()]
            [B, A, -q*A*B - q^2*C + q*g, b, a, g]

            sage: AW.an_element()
            (q^-3+3+2*q+q^2)*a*b*g^3 + q*A*C^2*b + 3*q^2*B*a^2*g + A
            sage: sigma(AW.an_element())
            q^9*A^2*B^3*a + (q^10+q^14)*A*B^2*C*a - (q^7+q^9)*A*B^2*a*g
             + (q^-3+3+2*q+q^2)*a*b*g^3 + (q-3*q^9+q^13+q^17)*A^2*B*a
             - (q^2-q^6-q^8+q^14)*A*B*a^2 + 3*q^2*A*b^2*g + (q^5-q^9)*B^3*a
             - (q^6-q^8)*B^2*a*b + q^13*B*C^2*a - 2*q^10*B*C*a*g + q^7*B*a*g^2
             + (q^2-2*q^10+q^18)*A*C*a - (q-q^7-2*q^9+2*q^11-q^15+q^17)*A*a*g
             - (q^3-q^7-q^9+q^13)*C*a^2 + (q^2-q^6-2*q^8+2*q^10)*a^2*g
             + (q-3*q^5+3*q^9-q^13)*B*a - (q^2-q^4-2*q^6+2*q^8+q^10-q^12)*a*b + B

            sage: s2 = sigma * sigma
            sage: [s2(gen) for gen in AW.algebra_generators()]
            [A, B, C, a, b, g]
            sage: s2(AW.an_element()) == AW.an_element()
            True
        """
    sigma = reflection_automorphism
    def loop_representation(self):
        """
        Return the map `\\pi` from ``self`` to `2 \\times 2` matrices
        over `R[\\lambda,\\lambda^{-1}]`, where `F` is the fraction field
        of the base ring of ``self``.

        Let `AW` be the Askey-Wilson algebra over `R`, and let `F` be
        the fraction field of `R`. Let `M` be the space of `2 \\times 2`
        matrices over `F[\\lambda, \\lambda^{-1}]`. Consider the following
        elements of `M`:

        .. MATH::

            \\mathcal{A} = \\begin{pmatrix}
                \\lambda & 1 - \\lambda^{-1} \\\\ 0 & \\lambda^{-1}
            \\end{pmatrix},
            \\qquad
            \\mathcal{B} = \\begin{pmatrix}
                \\lambda^{-1} & 0 \\\\ \\lambda - 1 & \\lambda
            \\end{pmatrix},
            \\qquad
            \\mathcal{C} = \\begin{pmatrix}
                1 & \\lambda - 1 \\\\ 1 - \\lambda^{-1} & \\lambda + \\lambda^{-1} - 1
            \\end{pmatrix}.

        From Lemma 3.11 of [Terwilliger2011]_, we define a
        representation `\\pi: AW \\to M` by

        .. MATH::

            A \\mapsto q \\mathcal{A} + q^{-1} \\mathcal{A}^{-1},
            \\qquad
            B \\mapsto q \\mathcal{B} + q^{-1} \\mathcal{B}^{-1},
            \\qquad
            C \\mapsto q \\mathcal{C} + q^{-1} \\mathcal{C}^{-1},

        .. MATH::

            \\alpha, \\beta, \\gamma \\mapsto \\nu I,

        where `\\nu = (q^2 + q^-2)(\\lambda + \\lambda^{-1})
        + (\\lambda + \\lambda^{-1})^2`.

        We call this representation the *loop representation* as
        it is a representation using the loop group
        `SL_2(F[\\lambda,\\lambda^{-1}])`.

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: q = AW.q()
            sage: pi = AW.loop_representation()
            sage: A,B,C,a,b,g = [pi(gen) for gen in AW.algebra_generators()]
            sage: A
            [                1/q*lambda^-1 + q*lambda ((-q^2 + 1)/q)*lambda^-1 + ((q^2 - 1)/q)]
            [                                       0                 q*lambda^-1 + 1/q*lambda]
            sage: B
            [             q*lambda^-1 + 1/q*lambda                                     0]
            [((-q^2 + 1)/q) + ((q^2 - 1)/q)*lambda              1/q*lambda^-1 + q*lambda]
            sage: C
            [1/q*lambda^-1 + ((q^2 - 1)/q) + 1/q*lambda      ((q^2 - 1)/q) + ((-q^2 + 1)/q)*lambda]
            [  ((q^2 - 1)/q)*lambda^-1 + ((-q^2 + 1)/q)    q*lambda^-1 + ((-q^2 + 1)/q) + q*lambda]
            sage: a
            [lambda^-2 + ((q^4 + 1)/q^2)*lambda^-1 + 2 + ((q^4 + 1)/q^2)*lambda + lambda^2                                                                             0]
            [                                                                            0 lambda^-2 + ((q^4 + 1)/q^2)*lambda^-1 + 2 + ((q^4 + 1)/q^2)*lambda + lambda^2]
            sage: a == b
            True
            sage: a == g
            True

            sage: AW.an_element()
            (q^-3+3+2*q+q^2)*a*b*g^3 + q*A*C^2*b + 3*q^2*B*a^2*g + A
            sage: x = pi(AW.an_element())
            sage: y = (q^-3+3+2*q+q^2)*a*b*g^3 + q*A*C^2*b + 3*q^2*B*a^2*g + A
            sage: x == y
            True

        We check the defining relations of the Askey-Wilson algebra::

            sage: A + (q*B*C - q^-1*C*B) / (q^2 - q^-2) == a / (q + q^-1)
            True
            sage: B + (q*C*A - q^-1*A*C) / (q^2 - q^-2) == b / (q + q^-1)
            True
            sage: C + (q*A*B - q^-1*B*A) / (q^2 - q^-2) == g / (q + q^-1)
            True

        We check Lemma 3.12 in [Terwilliger2011]_::

            sage: M = pi.codomain()
            sage: la = M.base_ring().gen()
            sage: p = M([[0,-1],[1,1]])
            sage: s = M([[0,1],[la,0]])
            sage: rho = AW.rho()
            sage: sigma = AW.sigma()
            sage: all(p*pi(gen)*~p == pi(rho(gen)) for gen in AW.algebra_generators())
            True
            sage: all(s*pi(gen)*~s == pi(sigma(gen)) for gen in AW.algebra_generators())
            True
        """
    pi = loop_representation

class AlgebraMorphism(ModuleMorphismByLinearity):
    """
    An algebra morphism of the Askey-Wilson algebra defined by
    the images of the generators.
    """
    def __init__(self, domain, on_generators, position: int = 0, codomain=None, category=None) -> None:
        """
        Given a map on the multiplicative basis of a free algebra, this method
        returns the algebra morphism that is the linear extension of its image
        on generators.

        INPUT:

        - ``domain`` -- an Askey-Wilson algebra
        - ``on_generators`` -- list of length 6 corresponding to
          the images of the generators
        - ``codomain`` -- (optional) the codomain
        - ``position`` -- integer (default: 0)
        - ``category`` -- (optional) category

        OUTPUT: module morphism

        EXAMPLES::

            sage: AW = algebras.AskeyWilson(QQ)
            sage: sigma = AW.sigma()
            sage: TestSuite(sigma).run()
        """
    def __eq__(self, other):
        """
        Check equality.

        EXAMPLES::

            sage: from sage.algebras.askey_wilson import AlgebraMorphism
            sage: AW = algebras.AskeyWilson(QQ)
            sage: rho = AW.rho()
            sage: sigma = AW.sigma()
            sage: id = AlgebraMorphism(AW, AW.gens(), codomain=AW)
            sage: sigma * sigma == id
            True
            sage: id == rho * rho * rho
            True
        """
