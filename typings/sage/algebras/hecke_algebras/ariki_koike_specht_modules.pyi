from sage.categories.modules import Modules as Modules
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.partition_tuple import PartitionTuples as PartitionTuples
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.tableau_tuple import StandardTableauTuples as StandardTableauTuples
from sage.misc.latex import latex as latex
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ

class SpechtModule(CombinatorialFreeModule):
    """
    Specht module of the Ariki-Koike algebra.

    Let `H_{r,n}(q, u)` be the Ariki-Koike algebra with parameters `q`
    and `u = (u_1, \\ldots, u_r)` (note our indexing convention for
    the `u` parameters differs from
    :mod:`sage.algebras.hecke_algebras.ariki_koike_algebra`) over a
    commutative ring `R`. Let `\\lambda` be a partition tuple of level
    `r` and size `n`. The *Specht module* of shape `\\lambda` is the (right)
    `H_{r,n}(q,u)`-representation `S^{\\lambda}` given as free `R`-module
    with basis given by the standard tableau (tuples) of shape `\\lambda`.

    We will now describe the right action of the Ariki-Koike algebra,
    but we first need to set some notation and definitions.
    Let `t` be a standard tableau tuple of level `r` and size `n`.
    Define the *residue* of `i` in `t` to be `r_t(i) = q^{c-r} u_k`,
    where `i` is in cell `(r, c)` of the `k`-th tableau.

    The action of `L_i` is given by `t \\cdot L_i = r_T(i) t`. For `T_i`,
    we need to consider the following cases. If `i, i+1` are in the same
    row (resp. column), then `t \\cdot T_i = q t` (resp. `t \\cdot T_i = -t`).
    Otherwise if we swap `i, i+1`, the resulting tableau tuple `s` is again
    standard and the action is given by

    .. MATH::

        t \\cdot T_i = \\frac{(q - 1) r_t(i)}{r_s(i) - r_t(i)} t
        + \\frac{q r_t(i) - r_s(i)}{r_s(i) - r_t(i)} s.

    Note that `r_s(i) = r_t(i+1)`.

    Over a field of characteristic `0`, the set of Specht modules for all
    partition tuples of level `r` and size `n` form the complete set
    of irreducible modules for `H_{r,n}(q, u)` [AK1994]_. (The condition
    on the base ring can be weakened; see Theorem 3.2 of [Mathas2002]_.)

    EXAMPLES:

    We construct the Specht module `S^{(2,1,21)}` for `H_{3,6}(q, u)` with
    generic parameters `q, u` over `\\GF(3)` and perform some basic
    computations. We change the tableaux to use the compact representation
    to condense the output::

        sage: TableauTuples.options.display = 'compact'

        sage: R = PolynomialRing(GF(3), 'u', 3)
        sage: u = R.gens()
        sage: q = R['q'].gen()
        sage: H = algebras.ArikiKoike(3, 6, q, u, use_fraction_field=True)
        sage: LT = H.LT()
        sage: T0, T1, T2, T3, T4, T5 = LT.T()
        sage: S = H.specht_module([[2], [1], [2,1]])
        sage: S.dimension()
        120
        sage: elt = S.an_element(); elt
        S[1,2|3|4,5/6] - S[1,3|2|4,5/6] + S[1,3|4|2,5/6]
        sage: elt * LT.L(3)
        u1*S[1,2|3|4,5/6] + (-u0*q)*S[1,3|2|4,5/6] + u0*q*S[1,3|4|2,5/6]
        sage: elt * T2
        (((-u0-u1)*q-u1)/(-u0*q+u1))*S[1,2|3|4,5/6]
         + (((-u0+u2)*q)/(u0*q-u2))*S[1,2|4|3,5/6]
         + ((-u0*q^2-u0*q-u1)/(-u0*q+u1))*S[1,3|2|4,5/6]
         + ((u0*q^2-u0*q)/(u0*q-u2))*S[1,3|4|2,5/6]
        sage: (elt * T3) * T2 == elt * (T3 * T2)
        True
        sage: elt * T2 * T3 * T2 == elt * T3 * T2 * T3
        True
        sage: elt * T0 * T1 * T0 * T1 == elt * T1 * T0 * T1 * T0
        True
        sage: elt * T2 * T5 == elt * T5 * T2
        True

        sage: TableauTuples.options._reset()

    REFERENCES:

    - [AK1994]_
    - [DJM1998]_
    - [DR2001]_
    - [Mathas2002]_
    - [Mathas2004]_
    """
    @staticmethod
    def __classcall_private__(cls, AK, la):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: AK = algebras.ArikiKoike(3, 6)
            sage: S1 = AK.specht_module([[3], [1], [1,1]])
            sage: S2 = AK.specht_module(PartitionTuple([[3], [1], [1,1]]))
            sage: S1 is S2
            True
        """
    def __init__(self, AK, la) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: AK = algebras.ArikiKoike(3, 6, use_fraction_field=True)
            sage: S = AK.specht_module([[3], [1], [1,1]])
            sage: TestSuite(S).run()  # long time
            sage: Sp = AK.specht_module([[], [2,1,1], [2]])
            sage: TestSuite(Sp).run()  # long time
        """
    def ariki_koike_algebra(self):
        """
        Return the Ariki-Koike algebra that ``self`` is a representation of.

        EXAMPLES::

            sage: AK = algebras.ArikiKoike(3, 6)
            sage: S = AK.specht_module([[2], [], [3,1]])
            sage: S.ariki_koike_algebra() is AK
            True
        """
    class Element(CombinatorialFreeModule.Element):
        def L(self, i):
            """
            Return the (right) action of `L_i` on ``self``.

            INPUT:

            - ``i`` -- an integer or a list of integers

            EXAMPLES::

                sage: TableauTuples.options.display = 'compact'  # compact tableau printing
                sage: AK = algebras.ArikiKoike(3, 6, use_fraction_field=True)
                sage: S = AK.specht_module([[2], [], [3,1]])
                sage: elt = S.an_element(); elt
                S[1,2|-|3,4,5/6] + 2*S[1,3|-|2,4,5/6]
                 + 3*S[2,3|-|1,4,5/6] + S[2,4|-|1,3,5/6]
                sage: elt.L(1)
                u0*S[1,2|-|3,4,5/6] + 2*u0*S[1,3|-|2,4,5/6]
                 + 3*u2*S[2,3|-|1,4,5/6] + u2*S[2,4|-|1,3,5/6]
                sage: elt.L(2)
                u0*q*S[1,2|-|3,4,5/6] + 2*u2*S[1,3|-|2,4,5/6]
                 + 3*u0*S[2,3|-|1,4,5/6] + u0*S[2,4|-|1,3,5/6]
                sage: elt.L(6)
                u2/q*S[1,2|-|3,4,5/6] + 2*u2/q*S[1,3|-|2,4,5/6]
                 + 3*u2/q*S[2,3|-|1,4,5/6] + u2/q*S[2,4|-|1,3,5/6]
                sage: elt.L([3,3,3])
                u2^3*S[1,2|-|3,4,5/6] + 2*u0^3*q^3*S[1,3|-|2,4,5/6]
                + 3*u0^3*q^3*S[2,3|-|1,4,5/6] + u2^3*q^3*S[2,4|-|1,3,5/6]
                sage: LT = AK.LT()
                sage: elt.L([3,3,3]) == elt * (LT.L(3)^3)
                True
                sage: TableauTuples.options._reset()  # reset
            """
        def T(self, i):
            """
            Return the (right) action of `T_i` on ``self``.

            INPUT:

            - ``i`` -- an integer or a list of integers

            EXAMPLES::

                sage: TableauTuples.options.display = 'compact'  # compact tableau printing
                sage: AK = algebras.ArikiKoike(3, 10, use_fraction_field=True)
                sage: q = AK.q()
                sage: S = AK.specht_module([[2,1], [], [3,2,2]])
                sage: P = S.basis().keys()
                sage: t = P([[[2,4],[8]], [], [[1,5,7],[3,6],[9,10]]])
                sage: b = S.basis()[t]
                sage: b.T(2)
                ((u2*q-u2)/(-u0*q+u2))*S[2,4/8|-|1,5,7/3,6/9,10]
                 + ((u0*q^2-u2)/(-u0*q+u2))*S[3,4/8|-|1,5,7/2,6/9,10]
                sage: b.T(6)
                ((-q)/(q+1))*S[2,4/8|-|1,5,6/3,7/9,10]
                 + (q^2/(q+1))*S[2,4/8|-|1,5,7/3,6/9,10]
                sage: b.T([2,1,2]) == b.T([1,2,1])
                True
                sage: b.T(9)
                q*S[2,4/8|-|1,5,7/3,6/9,10]
                sage: all(b.T([i,i]) == (q-1)*b.T(i) + q*b for i in range(1,10))
                True
                sage: b.T(0)
                u2*S[2,4/8|-|1,5,7/3,6/9,10]
                sage: b.T([0,1,0,1]) == b.T([1,0,1,0])
                True
                sage: TableauTuples.options._reset()  # reset
            """
