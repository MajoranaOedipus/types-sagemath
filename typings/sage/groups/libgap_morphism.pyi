from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.categories.morphism import Morphism as Morphism
from sage.groups.libgap_wrapper import ParentLibGAP as ParentLibGAP
from sage.libs.gap.element import GapElement as GapElement
from sage.misc.latex import latex as latex
from sage.rings.integer_ring import ZZ as ZZ

class GroupMorphism_libgap(Morphism):
    """
    This wraps GAP group homomorphisms.

    Checking if the input defines a group homomorphism can be expensive
    if the group is large.

    INPUT:

    - ``homset`` -- the parent
    - ``gap_hom`` -- a :class:`sage.libs.gap.element.GapElement` consisting of
      a group homomorphism
    - ``check`` -- boolean (default: ``True``); check if the ``gap_hom`` is a group
      homomorphism (this can be expensive)

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: A = AbelianGroupGap([2, 4])
        sage: A.hom([g^2 for g in A.gens()])
        Group endomorphism of Abelian group with gap, generator orders (2, 4)

    Homomorphisms can be defined between different kinds of GAP groups::

        sage: G = MatrixGroup([Matrix(ZZ, 2, [0,1,1,0])])
        sage: f = A.hom([G.0, G(1)])
        sage: f
        Group morphism:
        From: Abelian group with gap, generator orders (2, 4)
        To:   Matrix group over Integer Ring with 1 generators (
        [0 1]
        [1 0]
        )
        sage: G.<a,b> = FreeGroup()
        sage: H = G / (G([1]), G([2])^3)
        sage: f = G.hom(H.gens())
        sage: f
        Group morphism:
          From: Free Group on generators {a, b}
          To:   Finitely presented group < a, b | a, b^3 >

    Homomorphisms can be defined between GAP groups and permutation groups::

        sage: S = Sp(4,3)
        sage: P = PSp(4,3)
        sage: pr = S.hom(P.gens())
        sage: E = copy(S.one().matrix())
        sage: E[3,0] = 2; e = S(E)
        sage: pr(e)
        (1,16,15)(3,22,18)(4,19,21)(6,34,24)(7,25,33)(9,40,27)(10,28,39)(12,37,30)(13,31,36)

    TESTS:

    Old tests inherited from MatrixGroupMorphisms::

        sage: F = GF(5); MS = MatrixSpace(F,2,2)
        sage: G = MatrixGroup([MS([1,1,0,1])])
        sage: H = MatrixGroup([MS([1,0,1,1])])
        sage: phi = G.hom(H.gens())
        sage: phi
        Group morphism:
        From: Matrix group over Finite Field of size 5 with 1 generators (
        [1 1]
        [0 1]
        )
        To:   Matrix group over Finite Field of size 5 with 1 generators (
        [1 0]
        [1 1]
        )
        sage: phi(MS([1,1,0,1]))
        [1 0]
        [1 1]
        sage: F = GF(7); MS = MatrixSpace(F,2,2)
        sage: F.multiplicative_generator()                                              # needs sage.libs.pari
        3
        sage: G = MatrixGroup([MS([3,0,0,1])])
        sage: a = G.gens()[0]^2
        sage: phi = G.hom([a])

    Check that :issue:`19406` is fixed::

        sage: G = GL(2, GF(3))
        sage: H = GL(3, GF(2))
        sage: mat1 = H([[-1,0,0],[0,0,-1],[0,-1,0]])
        sage: mat2 = H([[1,1,1],[0,0,-1],[-1,0,0]])
        sage: phi = G.hom([mat1, mat2])
        Traceback (most recent call last):
        ...
        ValueError: images do not define a group homomorphism

        sage: F = GF(5); MS = MatrixSpace(F,2,2)
        sage: G = MatrixGroup([MS([1,1,0,1])])
        sage: H = MatrixGroup([MS([1,0,1,1])])
        sage: phi = G.hom(H.gens())
        sage: phi.gap()
        CompositionMapping( [ (6,7,8,10,9)(11,13,14,12,15)(16,19,20,18,17)(21,25,22,24,23) ]
        -> [ [ [ Z(5)^0, 0*Z(5) ], [ Z(5)^0, Z(5)^0 ] ] ], <action isomorphism> )
        sage: type(_)
        <class 'sage.libs.gap.element.GapElement'>

        sage: F = GF(7); MS = MatrixSpace(F,2,2)
        sage: F.multiplicative_generator()                                              # needs sage.libs.pari
        3
        sage: G = MatrixGroup([MS([3,0,0,1])])
        sage: a = G.gens()[0]^2
        sage: phi = G.hom([a])
        sage: phi.kernel()
        Subgroup with 1 generators (
        [6 0]
        [0 1]
        ) of Matrix group over Finite Field of size 7 with 1 generators (
        [3 0]
        [0 1]
        )

        sage: F = GF(7); MS = MatrixSpace(F,2,2)
        sage: F.multiplicative_generator()                                              # needs sage.libs.pari
        3
        sage: G = MatrixGroup([MS([3,0,0,1])])
        sage: a = G.gens()[0]^2
        sage: phi = G.hom([a])
        sage: phi
        Group endomorphism of Matrix group over Finite Field of size 7 with 1 generators (
        [3 0]
        [0 1]
        )
        sage: g = G.gens()[0]
        sage: phi(g)
        [2 0]
        [0 1]
        sage: H = MatrixGroup([MS(a.list())])
        sage: H
        Matrix group over Finite Field of size 7 with 1 generators (
        [2 0]
        [0 1]
        )

    The following tests against :issue:`10659`::

        sage: phi(H)   # indirect doctest
        Subgroup with 1 generators (
        [4 0]
        [0 1]
        ) of Matrix group over Finite Field of size 7 with 1 generators (
        [3 0]
        [0 1]
        )
        sage: F = GF(5); MS = MatrixSpace(F,2,2)
        sage: g = MS([1,1,0,1])
        sage: G = MatrixGroup([g])
        sage: phi = G.hom(G.gens())
        sage: phi(G.0)
        [1 1]
        [0 1]
        sage: phi(G(g^2))
        [1 2]
        [0 1]

        sage: F = GF(5); MS = MatrixSpace(F,2,2)
        sage: gens = [MS([1,2,  -1,1]),MS([1,1,  0,1])]
        sage: G = MatrixGroup(gens)
        sage: phi = G.hom(G.gens())
        sage: phi(G.0)
        [1 2]
        [4 1]
        sage: phi(G.1)
        [1 1]
        [0 1]

    We check that :issue:`19780` is fixed::

        sage: G = groups.matrix.SO(3, 3)
        sage: H = groups.matrix.GL(3, 3)
        sage: phi = G.hom([H(x) for x in G.gens()])
        sage: phi(G.one()).parent()
        General Linear Group of degree 3 over Finite Field of size 3

        sage: # needs sage.symbolic
        sage: MS = MatrixSpace(SR, 2, 2)
        sage: G = MatrixGroup([MS(1), MS([1,2,3,4])])
        sage: G.Hom(G)
        Set of Morphisms from Matrix group over Symbolic Ring with 2 generators (
        [1 0]  [1 2]
        [0 1], [3 4]
        ) to Matrix group over Symbolic Ring with 2 generators (
        [1 0]  [1 2]
        [0 1], [3 4]
        ) in Category of groups

        sage: G = MatrixGroup([matrix(GF(5), [[1,3],[0,1]])])
        sage: H = MatrixGroup([matrix(GF(5), [[1,2],[0,1]])])
        sage: G.hom([H.gen(0)])
        Group morphism:
        From: Matrix group over Finite Field of size 5 with 1 generators (
        [1 3]
        [0 1]
        )
        To:   Matrix group over Finite Field of size 5 with 1 generators (
        [1 2]
        [0 1]
        )

        sage: G = GO(2,2,e=1)
        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: A = AbelianGroupGap([2])
        sage: G.hom([A.one(),A.gen(0)])
        Group morphism:
        From: General Orthogonal Group of degree 2 and form parameter 1 over Finite Field of size 2
        To:   Abelian group with gap, generator orders (2,)

    Check that :issue:`19407` is fixed::

        sage: G = GL(2, GF(2))
        sage: H = GL(3, ZZ)
        sage: Hom(G, H)
        Set of Morphisms from General Linear Group of degree 2
         over Finite Field of size 2
         to General Linear Group of degree 3 over Integer Ring in Category of groups
    """
    def __init__(self, homset, gap_hom, check: bool = True) -> None:
        """
        Constructor method.

        TESTS::

            sage: G = GL(2, ZZ)
            sage: H = GL(2, GF(2))
            sage: P = Hom(G, H)
            sage: gen1 = [g.gap() for g in G.gens()]
            sage: gen2 = [H(g).gap() for g in G.gens()]
            sage: phi = G.gap().GroupHomomorphismByImagesNC(H,gen1, gen2)
            sage: phi = P.element_class(P,phi)
            sage: phi(G.gen(0))
            [0 1]
            [1 0]
        """
    def __reduce__(self):
        """
        Implement pickling.

        We have to work around the fact that GAP does not provide pickling.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,2,5])
            sage: f = G.hom(G, G.gens())
            sage: f == loads(dumps(f))
            True
        """
    def gap(self):
        """
        Return the underlying LibGAP group homomorphism.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([2,4])
            sage: f = A.hom([g^2 for g in A.gens()])
            sage: f.gap()
            [ f1, f2 ] -> [ <identity> of ..., f3 ]
        """
    def kernel(self):
        """
        Return the kernel of ``self``.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A1 = AbelianGroupGap([6, 6])
            sage: A2 = AbelianGroupGap([3, 3])
            sage: f = A1.hom(A2.gens())
            sage: f.kernel()
            Subgroup of Abelian group with gap, generator orders (6, 6)
             generated by (f1*f2, f3*f4)
            sage: f.kernel().order()
            4
            sage: S = Sp(6,3)
            sage: P = PSp(6,3)
            sage: pr = Hom(S, P).natural_map()
            sage: pr.kernel()
            Subgroup with 1 generators (
            [2 0 0 0 0 0]
            [0 2 0 0 0 0]
            [0 0 2 0 0 0]
            [0 0 0 2 0 0]
            [0 0 0 0 2 0]
            [0 0 0 0 0 2]
            ) of Symplectic Group of degree 6 over Finite Field of size 3
        """
    def pushforward(self, J, *args, **kwds):
        """
        The image of an element or a subgroup.

        INPUT:

        - ``J`` -- a subgroup or an element of the domain of ``self``

        OUTPUT: the image of ``J`` under ``self``

        .. NOTE::

            ``pushforward`` is the method that is used when a map is called
            on anything that is not an element of its domain. For historical
            reasons, we keep the alias ``image()`` for this method.

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: H = G / (G([1]), G([2])^3)
            sage: f = G.hom(H.gens())
            sage: S = G.subgroup([a.gap()])
            sage: f.pushforward(S)
            Group([ a ])
            sage: x = f.image(a)
            sage: x
            a
            sage: x.parent()
            Finitely presented group < a, b | a, b^3 >

            sage: # needs sage.rings.finite_rings
            sage: G = GU(3,2)
            sage: P = PGU(3,2)
            sage: pr = Hom(G, P).natural_map()
            sage: GS = G.subgroup([G.gen(0)])
            sage: pr.pushforward(GS)
            Subgroup generated by [(3,4,5)(10,18,14)(11,19,15)(12,20,16)(13,21,17)] of
            (The projective general unitary group of degree 3 over Finite Field of size 2)
        """
    image = pushforward
    def lift(self, h):
        """
        Return an element of the domain that maps to ``h``.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([2,4])
            sage: f = A.hom([g^2 for g in A.gens()])
            sage: a = A.gens()[1]
            sage: f.lift(a^2)
            f2

        If the element is not in the image, we raise an error::

            sage: f.lift(a)
            Traceback (most recent call last):
            ...
            ValueError: f2 is not an element of the image of Group endomorphism
             of Abelian group with gap, generator orders (2, 4)
        """
    def preimage(self, S):
        """
        Return the preimage of the subgroup ``S``.

        INPUT:

        - ``S`` -- a subgroup of this group

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([2,4])
            sage: B = AbelianGroupGap([4])
            sage: f = A.hom([B.one(), B.gen(0)^2])
            sage: S = B.subgroup([B.one()])
            sage: f.preimage(S) == f.kernel()
            True
            sage: S = Sp(4,3)
            sage: P = PSp(4,3)
            sage: pr = Hom(S, P).natural_map()
            sage: PS = P.subgroup([P.gen(0)])
            sage: pr.preimage(PS)
            Subgroup with 2 generators (
            [2 0 0 0]  [1 0 0 0]
            [0 2 0 0]  [0 2 0 0]
            [0 0 2 0]  [0 0 2 0]
            [0 0 0 2], [0 0 0 1]
            ) of Symplectic Group of degree 4 over Finite Field of size 3
        """
    def section(self):
        """
        Return a section map of ``self`` by use of :meth:`lift`.

        See :meth:`section` of :class:`sage.categories.map.Map`, as well.

        OUTPUT: an instance of :class:`sage.categories.morphism.SetMorphism`
        mapping an element of the codomain of ``self`` to one of its preimages

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: G = GU(3,2)
            sage: P = PGU(3,2)
            sage: pr = Hom(G, P).natural_map()
            sage: sect = pr.section()
            sage: sect(P.an_element())
            [a + 1     a     a]
            [    1     1     0]
            [    a     0     0]
        """

class GroupHomset_libgap(HomsetWithBase):
    """
    Homsets of groups with a libgap backend.

    Do not call this directly instead use :func:`Hom`.

    INPUT:

    - ``G`` -- a libgap group
    - ``H`` -- a libgap group
    - ``category`` -- a category

    OUTPUT: the homset of two libgap groups

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: A = AbelianGroupGap([2,4])
        sage: H = A.Hom(A)
        sage: H
        Set of Morphisms from Abelian group with gap, generator orders (2, 4)
         to Abelian group with gap, generator orders (2, 4)
         in Category of finite enumerated commutative groups
    """
    def __init__(self, G, H, category=None, check: bool = True) -> None:
        """
        Return the homset of two libgap groups.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([2,4])
            sage: H = A.Hom(A)
            sage: TestSuite(H).run()
        """
    Element = GroupMorphism_libgap
    def natural_map(self):
        """
        This method from :class:`HomsetWithBase` is overloaded here for cases in which
        both groups have corresponding lists of generators.

        OUTPUT:

        An instance of the element class of ``self`` if there exists a group
        homomorphism mapping the generators of the domain of ``self`` to the
        according generators of the codomain. Otherwise, the method falls back
        to the default.

        EXAMPLES::

            sage: G = GL(3,2)
            sage: P = PGL(3,2)
            sage: nat = Hom(G, P).natural_map()
            sage: type(nat)
            <class 'sage.groups.libgap_morphism.GroupHomset_libgap_with_category.element_class'>
            sage: g1, g2 = G.gens()
            sage: nat(g1*g2)
            (1,2,4,5,7,3,6)
        """
