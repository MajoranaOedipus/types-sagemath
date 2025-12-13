from _typeshed import Incomplete
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.sf.multiplicative import SymmetricFunctionAlgebra_multiplicative as SymmetricFunctionAlgebra_multiplicative

class HeckeCharacter(SymmetricFunctionAlgebra_multiplicative):
    """
    Basis of the symmetric functions that gives the characters of the
    Hecke algebra in analogy to the Frobenius formula for the
    symmetric group.

    Consider the Hecke algebra `H_n(q)` with quadratic relations

    .. MATH::

        T_i^2 = (q - 1) T_i + q.

    Let `\\mu` be a partition of `n` with length `\\ell`. The character
    `\\chi` of a `H_n(q)`-representation is completely determined by
    the elements `T_{\\gamma_{\\mu}}`, where

    .. MATH::

        \\gamma_{\\mu} = (\\mu_1, \\ldots, 1) (\\mu_2 + \\mu_1, \\ldots, 1 + \\mu_1)
        \\cdots (n, \\ldots, 1 + \\sum_{i < \\ell} \\mu_i),

    (written in cycle notation). We define a basis of the symmetric
    functions by

    .. MATH::

        \\bar{q}_{\\mu} = \\sum_{\\lambda \\vdash n}
        \\chi^{\\lambda}(T_{\\gamma_{\\mu}}) s_{\\lambda}.

    INPUT:

    - ``sym`` -- the ring of symmetric functions
    - ``q`` -- (default: ``'q'``) the parameter `q`

    EXAMPLES::

        sage: q = ZZ['q'].fraction_field().gen()
        sage: Sym = SymmetricFunctions(q.parent())
        sage: qbar = Sym.hecke_character(q)
        sage: qbar[2] * qbar[3] * qbar[3,1]
        qbar[3, 3, 2, 1]

        sage: s = Sym.s()
        sage: s(qbar([2]))
        -s[1, 1] + q*s[2]
        sage: s(qbar([4]))
        -s[1, 1, 1, 1] + q*s[2, 1, 1] - q^2*s[3, 1] + q^3*s[4]
        sage: qbar(s[2])
        (1/(q+1))*qbar[1, 1] + (1/(q+1))*qbar[2]
        sage: qbar(s[1,1])
        (q/(q+1))*qbar[1, 1] - (1/(q+1))*qbar[2]

        sage: s(qbar[2,1])
        -s[1, 1, 1] + (q-1)*s[2, 1] + q*s[3]
        sage: qbar(s[2,1])
        (q/(q^2+q+1))*qbar[1, 1, 1] + ((q-1)/(q^2+q+1))*qbar[2, 1]
         - (1/(q^2+q+1))*qbar[3]

    We compute character tables for Hecke algebras, which correspond
    to the transition matrix from the `\\bar{q}` basis to the Schur
    basis::

        sage: qbar.transition_matrix(s, 1)
        [1]
        sage: qbar.transition_matrix(s, 2)
        [ q -1]
        [ 1  1]
        sage: qbar.transition_matrix(s, 3)
        [  q^2    -q     1]
        [    q q - 1    -1]
        [    1     2     1]
        sage: qbar.transition_matrix(s, 4)
        [      q^3      -q^2         0         q        -1]
        [      q^2   q^2 - q        -q    -q + 1         1]
        [      q^2 q^2 - 2*q   q^2 + 1  -2*q + 1         1]
        [        q   2*q - 1     q - 1     q - 2        -1]
        [        1         3         2         3         1]

    We can do computations with a specialized `q` to a generic element
    of the base ring. We compute some examples with `q = 2`::

        sage: qbar = Sym.qbar(q=2)
        sage: s = Sym.schur()
        sage: qbar(s[2,1])
        2/7*qbar[1, 1, 1] + 1/7*qbar[2, 1] - 1/7*qbar[3]
        sage: s(qbar[2,1])
        -s[1, 1, 1] + s[2, 1] + 2*s[3]

    REFERENCES:

    - [Ram1991]_
    - [RR1997]_
    """
    @staticmethod
    def __classcall__(cls, Sym, q: str = 'q'):
        """
        Normalize the arguments.

        TESTS::

            sage: R.<q, t> = QQ[]
            sage: B1 = SymmetricFunctions(R).qbar()
            sage: B2 = SymmetricFunctions(R).qbar(q)
            sage: B3 = SymmetricFunctions(R).qbar(t)
            sage: B1 is B2
            True
            sage: B1 == B3
            False
        """
    q: Incomplete
    def __init__(self, sym, q) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(ZZ['q']))
            sage: qbar = Sym.qbar()
            sage: TestSuite(qbar).run()

            sage: Sym = SymmetricFunctions(QQ)
            sage: qbar = Sym.qbar(q=2)
            sage: TestSuite(qbar).run()

        Check that the conversion `q \\to p \\to s` agrees with
        the definition of `q \\to s` from [Ram1991]_::

            sage: Sym = SymmetricFunctions(FractionField(ZZ['q']))
            sage: qbar = Sym.qbar()
            sage: s = Sym.s()
            sage: q = qbar.q()
            sage: def to_schur(mu):
            ....:     if not mu:
            ....:        return s.one()
            ....:     mone = -qbar.base_ring().one()
            ....:     return s.prod(sum(mone**(r-m) * q**(m-1)
            ....:                       * s[Partition([m] + [1]*(r-m))]
            ....:                       for m in range(1, r+1))
            ....:                   for r in mu)
            sage: phi = qbar.module_morphism(to_schur, codomain=s)
            sage: all(phi(qbar[mu]) == s(qbar[mu]) for n in range(6)
            ....:     for mu in Partitions(n))
            True
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: qbar = SymmetricFunctions(QQ['q']).qbar('q')
            sage: qbar.construction()
            (SymmetricFunctionsFunctor[Hecke character with q=q],
             Univariate Polynomial Ring in q over Rational Field)
        """
    def coproduct_on_generators(self, r):
        """
        Return the coproduct on the generator `\\bar{q}_r` of ``self``.

        Define the coproduct on `\\bar{q}_r` by

        .. MATH::

            \\Delta(\\bar{q}_r) = \\bar{q}_0 \\otimes \\bar{q}_r
            + (q - 1) \\sum_{j=1}^{r-1} \\bar{q}_j \\otimes \\bar{q}_{r-j}
            + \\bar{q}_r \\otimes \\bar{q}_0.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: Sym = SymmetricFunctions(q.parent())
            sage: qbar = Sym.hecke_character()
            sage: s = Sym.s()
            sage: qbar[2].coproduct()
            qbar[] # qbar[2] + (q-1)*qbar[1] # qbar[1] + qbar[2] # qbar[]
        """
