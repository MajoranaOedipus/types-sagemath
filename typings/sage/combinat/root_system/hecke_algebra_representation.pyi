from sage.combinat.subset import Subsets as Subsets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class HeckeAlgebraRepresentation(WithEqualityById, SageObject):
    '''
    A representation of an (affine) Hecke algebra given by the action of the `T` generators.

    Let `F_i` be a family of operators implementing an action of the
    operators `(T_i)_{i\\in I}` of the Hecke algebra on some vector
    space ``domain``, given by their action on the basis of
    ``domain``. This constructs the family of operators `(F_w)_{w\\in
    W}` describing the action of all elements of the basis
    `(T_w)_{w\\in W}` of the Hecke algebra. This is achieved by
    linearity on the first argument, and applying recursively the
    `F_i` along a reduced word for `w=s_{i_1}\\cdots s_{i_k}`:

    .. MATH::

        F_w (x) = F_{i_k}\\circ\\cdots\\circ F_{i_1}(x) .

    INPUT:

    - ``domain`` -- a vector space
    - ``f`` -- a function ``f(l,i)`` taking a basis element `l` of ``domain`` and an index `i`, and returning `F_i`
    - ``cartan_type`` -- the Cartan type of the Hecke algebra
    - ``q1``, ``q2`` -- the eigenvalues of the generators `T` of the Hecke algebra
    - ``side`` -- ``\'left\'`` or ``\'right\'`` (default: ``\'right\'``)
      whether this is a left or right representation

    EXAMPLES::

        sage: K = QQ[\'q1,q2\'].fraction_field()
        sage: q1, q2 = K.gens()
        sage: KW = WeylGroup(["A",3]).algebra(QQ)
        sage: H = KW.demazure_lusztig_operators(q1,q2); H
        A representation of the (q1, q2)-Hecke algebra of type [\'A\', 3, 1]
        on Algebra of Weyl Group of type [\'A\', 3]
        (as a matrix group acting on the ambient space)
        over Rational Field

    Among other things, it implements the `T_w` operators, their
    inverses and compositions thereof::

        sage: H.Tw((1,2))
        Generic endomorphism of Algebra of Weyl Group of type [\'A\', 3]
        (as a matrix group acting on the ambient space) over Rational Field

    and the Cherednik operators `Y^{\\lambda^\\vee}`::

        sage: H.Y()
        Lazy family (...)_{i in Coroot lattice of the Root system of type [\'A\', 3, 1]}

    TESTS::

        sage: from sage.combinat.root_system.hecke_algebra_representation import HeckeAlgebraRepresentation
        sage: W = SymmetricGroup(3)
        sage: domain = W.algebra(QQ)
        sage: action = lambda x,i: domain.monomial(x.apply_simple_reflection(i, side=\'right\'))
        sage: r = HeckeAlgebraRepresentation(domain, action, CartanType(["A",2]), 1, -1)
        sage: hash(r) # random
        3

    REFERENCES:

    - [HST2008]_
    '''
    def __init__(self, domain, on_basis, cartan_type, q1, q2, q=..., side: str = 'right') -> None:
        '''
        TESTS::

            sage: from sage.combinat.root_system.hecke_algebra_representation import HeckeAlgebraRepresentation
            sage: W = SymmetricGroup(3)
            sage: domain = W.algebra(QQ)
            sage: action = lambda x,i: domain.monomial(x.apply_simple_reflection(i, side=\'right\'))
            sage: HeckeAlgebraRepresentation(domain, action, CartanType(["A",2]), 1, -1)
            A representation of the (1, -1)-Hecke algebra of type [\'A\', 2] on Symmetric group algebra of order 3 over Rational Field
        '''
    @cached_method
    def parameters(self, i):
        '''
        Return `q_1,q_2` such that `(T_i-q_1)(T_i-q_2) = 0`.

        EXAMPLES::

            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = WeylGroup(["A",3]).algebra(QQ)
            sage: H = KW.demazure_lusztig_operators(q1,q2)
            sage: H.parameters(1)
            (q1, q2)

            sage: H = KW.demazure_lusztig_operators(1,-1)
            sage: H.parameters(1)
            (1, -1)

        .. TODO::

            At this point, this method is constant. It\'s meant as a
            starting point for implementing parameters depending on
            the node `i` of the Dynkin diagram.
        '''
    def cartan_type(self):
        '''
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.hecke_algebra_representation import HeckeAlgebraRepresentation
            sage: KW = SymmetricGroup(3).algebra(QQ)
            sage: action = lambda x,i: KW.monomial(x.apply_simple_reflection(i, side=\'right\'))
            sage: H = HeckeAlgebraRepresentation(KW, action, CartanType(["A",2]), 1, -1)
            sage: H.cartan_type()
            [\'A\', 2]

            sage: H = WeylGroup(["A",3]).algebra(QQ).demazure_lusztig_operators(-1,1)
            sage: H.cartan_type()
            [\'A\', 3, 1]
        '''
    def domain(self):
        '''
        Return the domain of ``self``.

        EXAMPLES::

            sage: H = WeylGroup(["A",3]).algebra(QQ).demazure_lusztig_operators(-1,1)
            sage: H.domain()
            Algebra of Weyl Group of type [\'A\', 3] (as a matrix group
             acting on the ambient space) over Rational Field
        '''
    def Ti_on_basis(self, x, i):
        '''
        The `T_i` operators, on basis elements.

        INPUT:

        - ``x`` -- the index of a basis element
        - ``i`` -- the index of a generator

        EXAMPLES::

            sage: W = WeylGroup("A3")
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1,q2)
            sage: w = W.an_element()
            sage: rho.Ti_on_basis(w,1)
            q1*1231
        '''
    def Ti_inverse_on_basis(self, x, i):
        '''
        The `T_i^{-1}` operators, on basis elements.

        INPUT:

        - ``x`` -- the index of a basis element
        - ``i`` -- the index of a generator

        EXAMPLES::

            sage: W = WeylGroup("A3")
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1,q2)
            sage: w = W.an_element()
            sage: rho.Ti_inverse_on_basis(w, 1)
            -1/q2*1231 + ((q1+q2)/(q1*q2))*123
        '''
    @cached_method
    def on_basis(self, x, word, signs=None, scalar=None):
        '''
        Action of product of `T_i` and `T_i^{-1}` on `x`.

        INPUT:

        - ``x`` -- the index of a basis element
        - ``word`` -- word of indices of generators
        - ``signs`` -- (default: ``None``) sequence of signs of same length as
          ``word``; determines which operators are supposed to be taken as
          inverses.
        - ``scalar`` -- (default: ``None``) scalar to multiply the answer by

        EXAMPLES::

            sage: from sage.combinat.root_system.hecke_algebra_representation import HeckeAlgebraRepresentation
            sage: W = SymmetricGroup(3)
            sage: domain = W.algebra(QQ)
            sage: action = lambda x,i: domain.monomial(x.apply_simple_reflection(i, side=\'right\'))
            sage: rho = HeckeAlgebraRepresentation(domain, action, CartanType(["A",2]), 1, -1)

            sage: rho.on_basis(W.one(), (1,2,1))
            (1,3)

            sage: word = (1,2)
            sage: u = W.from_reduced_word(word)
            sage: for w in W:  assert rho.on_basis(w, word) == domain.monomial(w*u)

        The next example tests the signs::

            sage: W = WeylGroup("A3")
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1,q2)
            sage: w = W.an_element(); w
            123
            sage: rho.on_basis(w, (1,),  signs=(-1,))
            -1/q2*1231 + ((q1+q2)/(q1*q2))*123
            sage: rho.on_basis(w, (1,),  signs=( 1,))
            q1*1231
            sage: rho.on_basis(w, (1,1), signs=(1,-1))
            123
            sage: rho.on_basis(w, (1,1), signs=(-1,1))
            123
        '''
    def straighten_word(self, word):
        '''
        Return a tuple of indices of generators after some straightening.

        INPUT:

        - ``word`` -- a list/tuple of indices of generators, the index
          of a generator, or an object with a reduced word method

        OUTPUT: a tuple of indices of generators

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: H = W.algebra(QQ).demazure_lusztig_operators(-1,1)
            sage: H.straighten_word(1)
            (1,)
            sage: H.straighten_word((2,1))
            (2, 1)
            sage: H.straighten_word([2,1])
            (2, 1)
            sage: H.straighten_word(W.an_element())
            (1, 2, 3)
        '''
    def Tw(self, word, signs=None, scalar=None):
        '''
        Return `T_w`.

        INPUT:

        - ``word`` -- a word `i_1,\\dots,i_k` for some element `w` of the Weyl group
          See :meth:`straighten_word` for how this word can be specified

        - ``signs`` -- list `\\epsilon_1,\\dots,\\epsilon_k` of the
          same length as ``word`` with `\\epsilon_i =\\pm 1` or
          ``None`` for `1,\\dots,1` (default: ``None``)

        - ``scalar`` -- an element `c` of the base ring or ``None``
          for `1` (default: ``None``)

        OUTPUT: a module morphism implementing

        .. MATH::

            T_w = T_{i_k} \\circ \\cdots \\circ T_{i_1}

        in left action notation; that is `T_{i_1}` is applied first,
        then `T_{i_2}`, etc.

        More generally, if ``scalar`` or ``signs`` is specified, the
        morphism implements

        .. MATH::

            c T_{i_k}^{\\epsilon_k} \\circ \\cdots \\circ T_{i_1}^{\\epsilon_k}.

        EXAMPLES::

            sage: W = WeylGroup("A3")
            sage: W.element_class._repr_=lambda x: (\'e\' if not x.reduced_word()
            ....:               else "".join(str(i) for i in x.reduced_word()))
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: x = KW.an_element(); x
            123 + 3*2312 + 2*31 + e

            sage: T = KW.demazure_lusztig_operators(q1,q2)
            sage: T12 = T.Tw( (1,2) )
            sage: T12(KW.one())
            q1^2*12

        This is `T_2 \\circ T_1`::

            sage: T[2](T[1](KW.one()))
            q1^2*12
            sage: T[1](T[2](KW.one()))
            q1^2*21
            sage: T12(x) == T[2](T[1](x))
            True

        Now with signs and scalar coefficient we construct `3 T_2 \\circ T_1^{-1}`::

            sage: phi = T.Tw((1,2), (-1,1), 3)
            sage: phi(KW.one())
            -3*q1/q2*12 + ((3*q1+3*q2)/q2)*2
            sage: phi(T[1](x)) == 3*T[2](x)
            True

        For debugging purposes, one can recover the input data::

            sage: phi.word
            (1, 2)
            sage: phi.signs
            (-1, 1)
            sage: phi.scalar
            3
        '''
    def Tw_inverse(self, word):
        '''
        Return `T_w^{-1}`.

        This is essentially a shorthand for :meth:`Tw` with all minus signs.

        .. TODO:: Add an example where `T_i\\ne T_i^{-1}`

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_ = lambda x: "".join(str(i) for i in x.reduced_word())
            sage: KW = W.algebra(QQ)
            sage: rho = KW.demazure_lusztig_operators(1, -1)
            sage: x = KW.monomial(W.an_element()); x
            123
            sage: word = [1,2]
            sage: rho.Tw(word)(x)
            12312
            sage: rho.Tw_inverse(word)(x)
            12321

            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1, q2)
            sage: x = KW.monomial(W.an_element()); x
            123
            sage: rho.Tw_inverse(word)(x)
            1/q2^2*12321 - ((q1+q2)/(q1*q2^2))*1231 - ((q1+q2)/(q1*q2^2))*1232
            + ((q1^2+2*q1*q2+q2^2)/(q1^2*q2^2))*123
            sage: rho.Tw(word)(_)
            123
        '''
    __getitem__ = Tw
    def Y_lambdacheck(self, lambdacheck):
        '''
        Return the Cherednik operators `Y^{\\lambda^\\vee}` for this representation of an affine Hecke algebra.

        INPUT:

        - ``lambdacheck`` -- an element of the coroot lattice for this
          Cartan type

        EXAMPLES::

            sage: W = WeylGroup(["B",2])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)

        We take `q_2` and `q_1` as eigenvalues to match with the notations of [HST2008]_ ::

            sage: rho = KW.demazure_lusztig_operators(q2, q1)
            sage: L = rho.Y().keys()
            sage: alpha = L.simple_roots()
            sage: Y0 = rho.Y_lambdacheck(alpha[0])
            sage: Y1 = rho.Y_lambdacheck(alpha[1])
            sage: Y2 = rho.Y_lambdacheck(alpha[2])

            sage: x = KW.monomial(W.an_element()); x
            12
            sage: Y1(x)
            -((q1^2+2*q1*q2+q2^2)/(-q2^2))*2121
            + ((q1^3+q1^2*q2+q1*q2^2+q2^3)/(-q1*q2^2))*121
            + ((q1^2+q1*q2)/(-q2^2))*212 - (q1^2/(-q2^2))*12
            sage: Y2(x)
            -((q1^4+q1^3*q2+q1*q2^3+q2^4)/(-q1^3*q2))*2121
            + ((q1^3+q1^2*q2+q1*q2^2+q2^3)/(-q1^2*q2))*121
            + (q2^3/(-q1^3))*12
            sage: Y1(Y2(x))
            ((q1*q2+q2^2)/q1^2)*212 - q2/q1*12
            sage: Y2(Y1(x))
            ((q1*q2+q2^2)/q1^2)*212 - q2/q1*12

        The `Y` operators commute::

            sage: Y0(Y1(x)) - Y1(Y0(x))
            0
            sage: Y2(Y1(x)) - Y1(Y2(x))
            0

        In the classical root lattice, `\\alpha_0 + \\alpha_1 + \\alpha_2 = 0`::

            sage: Y0(Y1(Y2(x)))
            12

        Lemma 7.2 of [HST2008]_::

            sage: w0 = KW.monomial(W.long_element())
            sage: rho.Tw(0)(w0)
            q2
            sage: rho.Tw_inverse(1)(w0)
            1/q2*212
            sage: rho.Tw_inverse(2)(w0)
            1/q2*121

        Lemma 7.5 of [HST2008]_::

            sage: Y0(w0)
            q1^2/q2^2*2121
            sage: Y1(w0)
            (q2/(-q1))*2121
            sage: Y2(w0)
            (q2/(-q1))*2121

        .. TODO::

            Add more tests

            Add tests in type BC affine where the null coroot
            `\\delta^\\vee` can have non trivial coefficient in term of
            `\\alpha_0`

        .. SEEALSO::

            - [HST2008]_ for the formula in terms of `q_1, q_2`
        '''
    def Y(self, base_ring=...):
        '''
        Return the Cherednik operators `Y` for this representation of an affine Hecke algebra.

        INPUT:

        - ``self`` -- a representation of an affine Hecke algebra
        - ``base_ring`` -- the base ring of the coroot lattice

        This is a family of operators indexed by the coroot lattice
        for this Cartan type. In practice this is currently indexed
        instead by the affine coroot lattice, even if this indexing is
        not one to one, in order to allow for `Y[\\alpha^\\vee_0]`.

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q2, q1)
            sage: Y = rho.Y(); Y
            Lazy family (...(i))_{i in Coroot lattice of the Root system of type [\'A\', 3, 1]}
        '''
    def Y_eigenvectors(self):
        '''
        Return the family of eigenvectors for the Cherednik operators `Y` of this representation of an affine Hecke algebra.

        INPUT:

        - ``self`` -- a representation of an affine Hecke algebra
        - ``base_ring`` -- the base ring of the coroot lattice

        EXAMPLES::

            sage: W = WeylGroup(["B",2])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1, q2, affine=True)
            sage: E = rho.Y_eigenvectors()
            sage: E.keys()
            Weyl Group of type [\'B\', 2] (as a matrix group acting on the ambient space)
            sage: w0 = W.long_element()

        To set the recurrence up properly, one often needs to customize
        the :meth:`CherednikOperatorsEigenvectors.affine_lift`
        and :meth:`CherednikOperatorsEigenvectors.affine_retract`
        methods. This would usually be done by subclassing
        :class:`CherednikOperatorsEigenvectors`; here we just override
        the methods directly.

        In this particular case, we multiply by `w_0` to take into
        account that `w_0` is the seed for the recursion::

            sage: E.affine_lift = w0._mul_
            sage: E.affine_retract = w0._mul_

            sage: E[w0]
            2121
            sage: E.eigenvalues(E[w0])
            [q2^2/q1^2, q1/(-q2), q1/(-q2)]

        This step is taken care of automatically if one instead calls
        the specialization
        :meth:`sage.coxeter_groups.CoxeterGroups.Algebras.demazure_lusztig_eigenvectors`.

        Now we can compute all eigenvectors::

            sage: [E[w] for w in W]
            [2121 - 121 - 212 + 12 + 21 - 1 - 2 + ,
             -2121 + 212,
             (q2/(q1-q2))*2121 + (q2/(-q1+q2))*121 + (q2/(-q1+q2))*212 - 12 - (q2/(-q1+q2))*21 + 2,
             -(q2^2/(-q1^2+q1*q2-q2^2))*2121 - 121 + (q2^2/(-q1^2+q1*q2-q2^2))*212 + 21,
             -((q1^2+q2^2)/(q1^2-q1*q2+q2^2))*2121 - ((q1^2+q2^2)/(-q1^2+q1*q2-q2^2))*121
             - (q2^2/(-q1^2+q1*q2-q2^2))*212 + (q2^2/(-q1^2+q1*q2-q2^2))*12 - 21 + 1,
             2121,
             (q2/(-q1+q2))*2121 - (q2/(-q1+q2))*121 - 212 + 12,
             -2121 + 121]
        '''

class CherednikOperatorsEigenvectors(UniqueRepresentation, SageObject):
    """
    A class for the family of eigenvectors of the `Y` Cherednik
    operators for a module over a (Double) Affine Hecke algebra

    INPUT:

    - ``T`` -- a family `(T_i)_{i\\in I}` implementing the action of
      the generators of an affine Hecke algebra on ``self``.
      The intertwiner operators are built from these.

    - ``T_Y`` -- a family `(T^Y_i)_{i\\in I}` implementing the action
      of the generators of an affine Hecke algebra on ``self``. By
      default, this is ``T``. But this can be used to get the action
      of the full Double Affine Hecke Algebra. The `Y` operators are
      built from the ``T_Y``.

    This returns a function `\\mu\\mapsto E_\\mu` which uses intertwining
    operators to calculate recursively eigenvectors `E_\\mu` for the
    action of the torus of the affine Hecke algebra with eigenvalue
    given by `f`. Namely:

    .. MATH::

        E_\\mu.Y^{\\lambda^\\vee} = f(\\lambda^\\vee, \\mu) E_\\mu

    Assumptions:

    - ``seed(mu)`` initializes the recurrence by returning an
      appropriate eigenvector `E_\\mu` for `\\mu` trivial enough. For
      example, for nonsymmetric Macdonald polynomials ``seed(mu)``
      returns the monomial `X^\\mu` for a minuscule weight `\\mu`.

    - `f` is almost equivariant. Namely, `f(\\lambda^\\vee,\\mu) =
      f(\\lambda^\\vee s_i, twist(\\mu,i))` whenever `i` is a descent of
      `\\mu`.

    - `twist(\\mu, i)` maps `\\mu` closer to the dominant
      chamber whenever `i` is a descent of `\\mu`.

    .. TODO::

        Add tests for the above assumptions, and also that the
        classical operators `T_1, \\ldots, T_n` from `T` and `T_Y` coincide.
    """
    def __init__(self, T, T_Y=None, normalized: bool = True) -> None:
        '''
        INPUT:

        - ``T`` -- a family `(T_i)_{i\\in I}` implementing the action of
          the generators of an affine Hecke algebra on ``self``

        - ``T_Y`` -- a family `(T^Y_i)_{i\\in I}` implementing the action
          of the generators of an affine Hecke algebra on ``self``. By
          default, this is ``T``.

        - ``normalized`` -- boolean (default: ``True``); whether the
          eigenvector `E_\\mu` is normalized so that `\\mu` has
          coefficient `1`.

        TESTS::

            sage: from sage.combinat.root_system.hecke_algebra_representation import CherednikOperatorsEigenvectors
            sage: W = WeylGroup(["B",3])
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: rho = KW.demazure_lusztig_operators(q1, q2, affine=True)
            sage: E = CherednikOperatorsEigenvectors(rho); E
            <sage.combinat.root_system.hecke_algebra_representation.CherednikOperatorsEigenvectors object at ...>
            sage: E.keys()
            Weyl Group of type [\'B\', 3] (as a matrix group acting on the ambient space)
            sage: E.domain()
            Algebra of Weyl Group of type [\'B\', 3] (as a matrix group acting on the ambient space)
             over Fraction Field of Multivariate Polynomial Ring in q1, q2 over Rational Field
            sage: E._T == E._T_Y
            True
        '''
    @cached_method
    def cartan_type(self):
        '''
        Return Cartan type of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(["B",3])
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: E.cartan_type()
            [\'B\', 3, 1]

            sage: NonSymmetricMacdonaldPolynomials(["B", 2, 1]).cartan_type()           # needs sage.graphs
            [\'B\', 2, 1]
        '''
    def domain(self):
        '''
        The module on which the affine Hecke algebra acts.

        EXAMPLES::

            sage: W = WeylGroup(["B",3])
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: E.domain()
            Algebra of Weyl Group of type [\'B\', 3]
             (as a matrix group acting on the ambient space)
             over Multivariate Polynomial Ring in q1, q2 over Rational Field
        '''
    def keys(self):
        '''
        The index set for the eigenvectors.

        By default, this assumes that the eigenvectors span the full
        affine Hecke algebra module and that the eigenvectors have
        the same indexing as the basis of this module.

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: E.keys()
            Weyl Group of type [\'A\', 3] (as a matrix group acting on the ambient space)
        '''
    def seed(self, mu):
        '''
        Return the eigenvector for `\\mu` minuscule.

        INPUT:

        - ``mu`` -- an element `\\mu` of the indexing set

        OUTPUT: an element of ``T.domain()``

        This default implementation returns the monomial indexed by `\\mu`.

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: E.seed(W.long_element())
            123121
        '''
    @abstract_method
    def affine_lift(self, mu) -> None:
        '''
        Lift the index ``\\mu`` to a space admitting an action of the affine Weyl group.

        INPUT:

        - ``mu`` -- an element `\\mu` of the indexing set

        In this space, one should have ``first_descent`` and
        ``apply_simple_reflection`` act properly.

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w = W.an_element(); w
            123
            sage: E.affine_lift(w)
            121
        '''
    @abstract_method
    def affine_retract(self, mu) -> None:
        '''
        Retract `\\mu` from a space admitting an action of the affine Weyl group.

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w = W.an_element(); w
            123
            sage: E.affine_retract(E.affine_lift(w)) == w
            True
        '''
    def Y(self):
        '''
        Return the Cherednik operators.

        EXAMPLES::

            sage: W = WeylGroup(["B",2])
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: E.Y()
            Lazy family (...)_{i in Coroot lattice of the Root system of type [\'B\', 2, 1]}
        '''
    def eigenvalues(self, mu):
        '''
        Return the eigenvalues of `Y_{\\alpha_0},\\dots,Y_{\\alpha_n}` on `E_\\mu`.

        INPUT:

        - ``mu`` -- the index `\\mu` of an eigenvector or a tentative eigenvector

        EXAMPLES::

            sage: W = WeylGroup(["B",2])
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w0 = W.long_element()
            sage: E.eigenvalues(w0)
            [q2^2/q1^2, q1/(-q2), q1/(-q2)]
            sage: w = W.an_element()
            sage: E.eigenvalues(w)
            [(-q2)/q1, (-q2^2)/(-q1^2), q1^3/(-q2^3)]
        '''
    @cached_method
    def eigenvalue(self, mu, l):
        '''
        Return the eigenvalue of `Y_{\\lambda^\\vee}` on `E_\\mu` computed by applying `Y_{\\lambda^\\vee}` on `E_\\mu`.

        INPUT:

        - ``mu`` -- the index `\\mu` of an eigenvector, or a tentative eigenvector
        - ``l`` -- the index `\\lambda^\\vee` of a Cherednik operator in ``self.Y_index_set()``

        This default implementation applies explicitly `Y_\\mu` to `E_\\lambda`.

        EXAMPLES::

            sage: W = WeylGroup(["B",2])
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w0 = W.long_element()
            sage: Y = E.Y()
            sage: alphacheck = Y.keys().simple_roots()
            sage: E.eigenvalue(w0, alphacheck[1])
            q1/(-q2)
            sage: E.eigenvalue(w0, alphacheck[2])
            q1/(-q2)
            sage: E.eigenvalue(w0, alphacheck[0])
            q2^2/q1^2

        The following checks that all `E_w` are eigenvectors, with
        eigenvalue given by Lemma 7.5 of [HST2008]_ (checked for
        `A_2`, `A_3`)::

            sage: Pcheck = Y.keys()
            sage: Wcheck = Pcheck.weyl_group()
            sage: P0check = Pcheck.classical()
            sage: def height(root):
            ....:     return sum(P0check(root).coefficients())
            sage: def eigenvalue(w, mu):
            ....:     return (-q2/q1)^height(Wcheck.from_reduced_word(w.reduced_word()).action(mu))
            sage: all(E.eigenvalue(w, a) == eigenvalue(w, a) for w in E.keys() for a in Y.keys().simple_roots()) # long time (2.5s)
            True
        '''
    def twist(self, mu, i):
        '''
        Act by `s_i` on `\\mu`.

        By default, this calls the method ``apply_simple_reflection``.

        EXAMPLES::

            sage: W = WeylGroup(["B",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: T = KW.demazure_lusztig_operators(q1, q2, affine=True)
            sage: E = T.Y_eigenvectors()
            sage: w = W.an_element(); w
            123
            sage: E.twist(w,1)
            1231
        '''
    @cached_method
    def hecke_parameters(self, i):
        '''
        Return the Hecke parameters for index ``i``.

        EXAMPLES::

            sage: W = WeylGroup(["B",3])
            sage: K = QQ[\'q1,q2\']
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: T = KW.demazure_lusztig_operators(q1, q2, affine=True)
            sage: E = T.Y_eigenvectors()
            sage: E.hecke_parameters(1)
            (q1, q2)
            sage: E.hecke_parameters(2)
            (q1, q2)
            sage: E.hecke_parameters(0)
            (q1, q2)
        '''
    @cached_method
    def __getitem__(self, mu):
        '''
        Return the eigenvector `E_\\mu`.

        INPUT:

        - ``mu`` -- the index `\\mu` of an eigenvector

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w0 = W.long_element()
            sage: E[w0]
            123121
        '''
    def recursion(self, mu):
        '''
        Return the indices used in the recursion.

        INPUT:

        - ``mu`` -- the index `\\mu` of an eigenvector

        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: W.element_class._repr_=lambda x: "".join(str(i) for i in x.reduced_word())
            sage: K = QQ[\'q1,q2\'].fraction_field()
            sage: q1, q2 = K.gens()
            sage: KW = W.algebra(K)
            sage: E = KW.demazure_lusztig_eigenvectors(q1, q2)
            sage: w0 = W.long_element()
            sage: E.recursion(w0)
            []
            sage: w = W.an_element(); w
            123
            sage: E.recursion(w)
            [1, 2, 1]
        '''
