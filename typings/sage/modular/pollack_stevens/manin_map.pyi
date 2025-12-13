from .fund_domain import M2Z as M2Z, t00 as t00, t01 as t01, t10 as t10, t11 as t11
from .sigma0 import Sigma0 as Sigma0
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.continued_fraction import convergents as convergents
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import coercion_model as coercion_model
from typing import Self

def unimod_matrices_to_infty(r, s):
    """
    Return a list of matrices whose associated unimodular paths connect `0` to ``r/s``.

    INPUT:

    - ``r``, ``s`` -- rational numbers

    OUTPUT:

    - a list of matrices in `SL_2(\\ZZ)`

    EXAMPLES::

        sage: v = sage.modular.pollack_stevens.manin_map.unimod_matrices_to_infty(19,23); v
        [
        [1 0]  [ 0  1]  [1 4]  [-4  5]  [ 5 19]
        [0 1], [-1  1], [1 5], [-5  6], [ 6 23]
        ]
        sage: [a.det() for a in v]
        [1, 1, 1, 1, 1]

        sage: sage.modular.pollack_stevens.manin_map.unimod_matrices_to_infty(11,25)
        [
        [1 0]  [ 0  1]  [1 3]  [-3  4]  [ 4 11]
        [0 1], [-1  2], [2 7], [-7  9], [ 9 25]
        ]


    ALGORITHM:

    This is Manin's continued fraction trick, which gives an expression
    `\\{0,r/s\\} = \\{0,\\infty\\} + ... + \\{a,b\\} + ... + \\{*,r/s\\}`, where each `\\{a,b\\}` is
    the image of `\\{0,\\infty\\}` under a matrix in `SL_2(\\ZZ)`.
    """
def unimod_matrices_from_infty(r, s):
    """
    Return a list of matrices whose associated unimodular paths connect `\\infty` to ``r/s``.

    INPUT:

    - ``r``, ``s`` -- rational numbers

    OUTPUT:

    - a list of `SL_2(\\ZZ)` matrices

    EXAMPLES::

        sage: v = sage.modular.pollack_stevens.manin_map.unimod_matrices_from_infty(19,23); v
        [
        [ 0  1]  [-1  0]  [-4  1]  [-5 -4]  [-19   5]
        [-1  0], [-1 -1], [-5  1], [-6 -5], [-23   6]
        ]
        sage: [a.det() for a in v]
        [1, 1, 1, 1, 1]

        sage: sage.modular.pollack_stevens.manin_map.unimod_matrices_from_infty(11,25)
        [
        [ 0  1]  [-1  0]  [-3  1]  [-4 -3]  [-11   4]
        [-1  0], [-2 -1], [-7  2], [-9 -7], [-25   9]
        ]


    ALGORITHM:

    This is Manin's continued fraction trick, which gives an expression
    `\\{\\infty,r/s\\} = \\{\\infty,0\\} + ... + \\{a,b\\} + ... + \\{*,r/s\\}`, where each
    `\\{a,b\\}` is the image of `\\{0,\\infty\\}` under a matrix in `SL_2(\\ZZ)`.
    """

class ManinMap:
    """
    Map from a set of right coset representatives of `\\Gamma_0(N)` in
    `SL_2(\\ZZ)` to a coefficient module that satisfies the Manin
    relations.

    INPUT:

    - ``codomain`` -- coefficient module
    - ``manin_relations`` -- a :class:`sage.modular.pollack_stevens.fund_domain.ManinRelations`
      object
    - ``defining_data`` -- dictionary whose keys are a superset of
      ``manin_relations.gens()`` and a subset of ``manin_relations.reps()``,
      and whose values are in the codomain
    - ``check`` -- do numerous (slow) checks and transformations to
      ensure that the input data is perfect

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
        sage: D = OverconvergentDistributions(0, 11, 10)
        sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
        sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
        sage: f = ManinMap(D, manin, data); f # indirect doctest
        Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
        sage: f(M2Z([1,0,0,1]))
        (1 + O(11^2), 2 + O(11))
    """
    def __init__(self, codomain, manin_relations, defining_data, check: bool = True) -> None:
        """
        INPUT:

        - ``codomain`` -- coefficient module
        - ``manin_relations`` -- a :class:`ManinRelations` object
        - ``defining_data`` -- dictionary whose keys are a superset of
          :meth:`manin_relations.gens()` and a subset of manin_relations.reps(),
          and whose values are in the codomain
        - ``check`` -- do numerous (slow) checks and transformations to
          ensure that the input data is perfect

        TESTS:

        Test that it fails gracefully on some bogus inputs::

            sage: from sage.modular.pollack_stevens.manin_map import  ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: rels = ManinRelations(37)
            sage: ManinMap(ZZ, rels, {})
            Traceback (most recent call last):
            ...
            ValueError: Codomain must have an action of Sigma0(N)
            sage: ManinMap(Symk(0), rels, [])
            Traceback (most recent call last):
            ...
            ValueError: length of defining data must be the same as number of Manin generators
        """
    def extend_codomain(self, new_codomain, check: bool = True):
        """
        Extend the codomain of ``self`` to ``new_codomain``. There must be a
        valid conversion operation from the old to the new codomain. This is
        most often used for extension of scalars from `\\QQ` to `\\QQ_p`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import ManinMap, M2Z
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37)
            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: m = ManinMap(S, MR, data); m
            Map from the set of right cosets of Gamma0(37) in SL_2(Z) to Sym^0 Q^2
            sage: m.extend_codomain(Symk(0, Qp(11)))
            Map from the set of right cosets of Gamma0(37) in SL_2(Z) to Sym^0 Q_11^2
        """
    def __getitem__(self, B):
        """

        Compute the image of ``B`` under ``self``.

        INPUT:

        - ``B`` -- coset representative of Manin relations

        OUTPUT:

        An element in the codomain of ``self`` (e.g. a distribution), the image
        of ``B`` under ``self``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37); MR.gens()
            (
            [1 0]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -3]  [-3 -1]  [-1 -4]  [-4 -3]
            [0 1], [ 1  4], [ 4  3], [ 3  5], [ 5  7], [ 7  2], [ 2  7], [ 7  5],
            <BLANKLINE>
            [-2 -3]
            [ 3  4]
            )

            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: D = OverconvergentDistributions(2, 37, 40)
            sage: f = ManinMap(D, MR, data)
            sage: f.__getitem__(MR.gens()[1])
            1 + O(37)
            sage: f.__getitem__(MR.gens()[3])
            O(37^40)
            sage: f.__getitem__(MR.gens()[5])
            36 + O(37)
            sage: f[MR.gens()[5]]
            36 + O(37)
        """
    def compute_full_data(self) -> None:
        """
        Compute the values of ``self`` on all coset reps from its values on our
        generating set.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37); MR.gens()
            (
            [1 0]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -3]  [-3 -1]  [-1 -4]  [-4 -3]
            [0 1], [ 1  4], [ 4  3], [ 3  5], [ 5  7], [ 7  2], [ 2  7], [ 7  5],
            <BLANKLINE>
            [-2 -3]
            [ 3  4]
            )

            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: f = ManinMap(S,MR,data)
            sage: len(f._dict)
            9
            sage: f.compute_full_data()
            sage: len(f._dict)
            38
        """
    def __add__(self, right):
        """
        Return sum ``self + right``, where ``self`` and ``right`` are
        assumed to have identical codomains and Manin relations.

        INPUT:

        - ``self``, ``right`` -- two Manin maps with the same codomain and
          Manin relations

        OUTPUT: the sum of ``self`` and ``right`` -- a Manin map

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10); D
            Space of 11-adic distributions with k=0 action and precision cap 10
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data); f
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: f(M2Z([1,0,0,1]))
            (1 + O(11^2), 2 + O(11))
            sage: f+f # indirect doctest
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: (f+f)(M2Z([1,0,0,1]))
            (2 + O(11^2), 4 + O(11))
        """
    def __sub__(self, right):
        """
        Return difference ``self`` - right, where ``self`` and ``right`` are
        assumed to have identical codomains and Manin relations.

        INPUT:

        - ``self``, ``right`` -- two Manin maps with the same codomain and
          Manin relations

        OUTPUT: the difference of ``self`` and ``right`` -- a Manin map

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10); D
            Space of 11-adic distributions with k=0 action and precision cap 10
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data); f
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: f(M2Z([1,0,0,1]))
            (1 + O(11^2), 2 + O(11))
            sage: f-f
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: (f-f)(M2Z([1,0,0,1]))
            (O(11^2), O(11))
        """
    def __mul__(self, right):
        """
        Return scalar multiplication ``self * right``, where ``right`` is in
        the base ring of the codomain.

        INPUT:

        - ``self`` -- a Manin map
        - ``right`` -- an element of the base ring of the codomain of self

        OUTPUT: the sum ``self`` and ``right`` -- a Manin map

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10)
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data)
            sage: f(M2Z([1,0,0,1]))
            (1 + O(11^2), 2 + O(11))
            sage: f*2
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: (f*2)(M2Z([1,0,0,1]))
            (2 + O(11^2), 4 + O(11))
        """
    def __call__(self, A):
        """
        Evaluate ``self`` at A.

        INPUT:

        - ``A`` -- a `2 \times 2` matrix

        OUTPUT: the value of ``self`` on the divisor corresponding to ``A`` --
        an element of the codomain of self

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: D = OverconvergentDistributions(0, 11, 10); D
            Space of 11-adic distributions with k=0 action and precision cap 10
            sage: manin = ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data); f
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Space of 11-adic distributions with k=0 action and precision cap 10
            sage: f(M2Z([1,0,0,1]))
            (1 + O(11^2), 2 + O(11))

            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37)
            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: f = ManinMap(S,MR,data)
            sage: f(M2Z([2,3,4,5]))
            1
        """
    def apply(self, f, codomain=None, to_moments: bool = False):
        """
        Return Manin map given by `x \\mapsto f(self(x))`, where `f` is
        anything that can be called with elements of the coefficient
        module.

        This might be used to normalize, reduce modulo a prime, change
        base ring, etc.

        INPUT:

        - ``f`` -- anything that can be called with elements of the coefficient
          module
        - ``codomain`` -- (default: ``None``) the codomain of the return map
        - ``to_moments`` -- boolean (default: ``False``); if ``True``, will
          apply ``f`` to each of the moments instead

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37)
            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: f = ManinMap(S,MR,data)
            sage: list(f.apply(lambda t:2*t))
            [0, 2, 0, 0, 0, -2, 2, 0, 0]
        """
    def __iter__(self):
        """
        Return iterator over the values of this map on the reduced
        representatives.

        This might be used to compute the valuation.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: S = Symk(0,QQ)
            sage: MR = ManinRelations(37)
            sage: data  = {M2Z([-2,-3,5,7]): S(0), M2Z([1,0,0,1]): S(0), M2Z([-1,-2,3,5]): S(0), M2Z([-1,-4,2,7]): S(1), M2Z([0,-1,1,4]): S(1), M2Z([-3,-1,7,2]): S(-1), M2Z([-2,-3,3,4]): S(0), M2Z([-4,-3,7,5]): S(0), M2Z([-1,-1,4,3]): S(0)}
            sage: f = ManinMap(S,MR,data)
            sage: [a for a in f]
            [0, 1, 0, 0, 0, -1, 1, 0, 0]
        """
    def normalize(self) -> Self:
        """
        Normalize every value of ``self`` -- e.g., reduce each value's
        `j`-th moment modulo `p^{N-j}`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10)
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data)
            sage: f._dict[M2Z([1,0,0,1])]
            (1 + O(11^2), 2 + O(11))
            sage: g = f.normalize()
            sage: g._dict[M2Z([1,0,0,1])]
            (1 + O(11^2), 2 + O(11))
        """
    def reduce_precision(self, M):
        """
        Reduce the precision of all the values of the Manin map.

        INPUT:

        - ``M`` -- integer; the new precision

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10)
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data)
            sage: f._dict[M2Z([1,0,0,1])]
            (1 + O(11^2), 2 + O(11))
            sage: g = f.reduce_precision(1)
            sage: g._dict[M2Z([1,0,0,1])]
            1 + O(11^2)
        """
    def specialize(self, *args):
        """
        Specialize all the values of the Manin map to a new coefficient
        module. Assumes that the codomain has a ``specialize`` method, and
        passes all its arguments to that method.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.manin_map import M2Z, ManinMap
            sage: D = OverconvergentDistributions(0, 11, 10)
            sage: manin = sage.modular.pollack_stevens.fund_domain.ManinRelations(11)
            sage: data  = {M2Z([1,0,0,1]):D([1,2]), M2Z([0,-1,1,3]):D([3,5]), M2Z([-1,-1,3,2]):D([1,1])}
            sage: f = ManinMap(D, manin, data)
            sage: g = f.specialize()
            sage: g._codomain
            Sym^0 Z_11^2
        """
    def hecke(self, ell, algorithm: str = 'prep'):
        """
        Return the image of this Manin map under the Hecke operator `T_{\\ell}`.

        INPUT:

        - ``ell`` -- a prime

        - ``algorithm`` -- string; either ``'prep'`` (default) or ``'naive'``

        OUTPUT: the image of this ManinMap under the Hecke operator `T_{\\ell}`

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: phi.is_Tq_eigensymbol(7,7,10)
            True
            sage: phi.hecke(7).values()
            [2/5, -2, 0]
            sage: phi.Tq_eigenvalue(7,7,10)
            -2
        """
    def p_stabilize(self, p, alpha, V):
        """
        Return the `p`-stabilization of ``self`` to level `N*p` on which
        `U_p` acts by `\\alpha`.

        INPUT:

        - ``p`` -- a prime

        - ``alpha`` -- a `U_p`-eigenvalue

        - ``V`` -- a space of modular symbols

        OUTPUT: the image of this ManinMap under the Hecke operator `T_{\\ell}`

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: f = phi._map
            sage: V = phi.parent()
            sage: f.p_stabilize(5,1,V)
            Map from the set of right cosets of Gamma0(11) in SL_2(Z) to Sym^0 Q^2
        """
