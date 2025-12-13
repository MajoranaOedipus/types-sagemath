from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.crystals import CrystalMorphism as CrystalMorphism
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.homset import Hom as Hom
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.rsk import RSK as RSK
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AffineFactorizationCrystal(UniqueRepresentation, Parent):
    """
    The crystal on affine factorizations with a cut-point, as introduced
    by [MS2015]_.

    INPUT:

    - ``w`` -- an element in an (affine) Weyl group or a skew shape of `k`-bounded partitions (if `k` was specified)

    - ``n`` -- the number of factors in the factorization

    - ``x`` -- (default: ``None``) the cut point; if not specified it is determined as the minimal missing residue in ``w``

    - ``k`` -- (default: ``None``) positive integer, specifies that ``w`` is `k`-bounded or a `k+1`-core when specified

    EXAMPLES::

        sage: W = WeylGroup(['A',3,1], prefix='s')
        sage: w = W.from_reduced_word([2,3,2,1])
        sage: B = crystals.AffineFactorization(w,3); B
        Crystal on affine factorizations of type A2 associated to s2*s3*s2*s1
        sage: B.list()
        [(1, s2, s3*s2*s1),
         (1, s3*s2, s3*s1),
         (1, s3*s2*s1, s3),
         (s3, s2, s3*s1),
         (s3, s2*s1, s3),
         (s3*s2, s1, s3),
         (s3*s2*s1, 1, s3),
         (s3*s2*s1, s3, 1),
         (s3*s2, 1, s3*s1),
         (s3*s2, s3, s1),
         (s3*s2, s3*s1, 1),
         (s2, 1, s3*s2*s1),
         (s2, s3, s2*s1),
         (s2, s3*s2, s1),
         (s2, s3*s2*s1, 1)]

    We can also access the crystal by specifying a skew shape in terms of `k`-bounded partitions::

        sage: crystals.AffineFactorization([[3,1,1],[1]], 3, k=3)
        Crystal on affine factorizations of type A2 associated to s2*s3*s2*s1

    We can compute the highest weight elements::

        sage: hw = [w for w in B if w.is_highest_weight()]
        sage: hw
        [(1, s2, s3*s2*s1)]
        sage: hw[0].weight()
        (3, 1, 0)

    And show that this crystal is isomorphic to the tableau model of the same weight::

        sage: C = crystals.Tableaux(['A',2],shape=[3,1])
        sage: GC = C.digraph()
        sage: GB = B.digraph()
        sage: GC.is_isomorphic(GB, edge_labels=True)
        True

    The crystal operators themselves move elements between adjacent factors::

        sage: b = hw[0];b
        (1, s2, s3*s2*s1)
        sage: b.f(1)
        (1, s3*s2, s3*s1)

    The cut point `x` is not supposed to occur in the reduced words for `w`::

        sage: B = crystals.AffineFactorization([[3,2],[2]],4,x=0,k=3)
        Traceback (most recent call last):
        ...
        ValueError: x cannot be in reduced word of s0*s3*s2
    """
    @staticmethod
    def __classcall_private__(cls, w, n, x=None, k=None):
        """
        Classcall to mend the input.

        TESTS::

            sage: A = crystals.AffineFactorization([[3,1],[1]], 4, k=3); A
            Crystal on affine factorizations of type A3 associated to s3*s2*s1
            sage: AC = crystals.AffineFactorization([Core([4,1],4),Core([1],4)], 4, k=3)
            sage: AC is A
            True
        """
    n: Incomplete
    k: Incomplete
    w: Incomplete
    module_generators: Incomplete
    x: Incomplete
    def __init__(self, w, n, x=None) -> None:
        """
        EXAMPLES::

            sage: B = crystals.AffineFactorization([[3,2],[2]],4,x=0,k=3)
            Traceback (most recent call last):
            ...
            ValueError: x cannot be in reduced word of s0*s3*s2

            sage: B = crystals.AffineFactorization([[3,2],[2]],4,k=3)
            sage: B.x
            1
            sage: B.w
            s0*s3*s2
            sage: B.k
            3
            sage: B.n
            4

        TESTS::

            sage: W = WeylGroup(['A',3,1], prefix='s')
            sage: w = W.from_reduced_word([2,3,2,1])
            sage: B = crystals.AffineFactorization(w,3)
            sage: TestSuite(B).run()  # long time
        """
    class Element(ElementWrapper):
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: B = crystals.AffineFactorization([[3,1],[1]], 4, k=3)
                sage: W = B.w.parent()
                sage: t = B((W.one(),W.one(),W.from_reduced_word([3]),W.from_reduced_word([2,1]))); t
                (1, 1, s3, s2*s1)
                sage: t.e(1)
                (1, 1, 1, s3*s2*s1)
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: B = crystals.AffineFactorization([[3,1],[1]], 4, k=3)
                sage: W = B.w.parent()
                sage: t = B((W.one(),W.one(),W.from_reduced_word([3]),W.from_reduced_word([2,1]))); t
                (1, 1, s3, s2*s1)
                sage: t.f(2)
                (1, s3, 1, s2*s1)
                sage: t.f(1)
                (1, 1, s3*s2, s1)
            """
        def bracketing(self, i):
            """
            Removes all bracketed letters between `i`-th and `i+1`-th entry.

            EXAMPLES::

                sage: B = crystals.AffineFactorization([[3,1],[1]], 3, k=3, x=4)
                sage: W = B.w.parent()
                sage: t = B((W.one(),W.from_reduced_word([3]),W.from_reduced_word([2,1]))); t
                (1, s3, s2*s1)
                sage: t.bracketing(1)
                [[3], [2, 1]]
            """
        def to_tableau(self):
            """
            Return the tableau representation of ``self``.

            Uses the recording tableau of a minor variation of
            Edelman-Greene insertion. See Theorem 4.11 in [MS2015]_.

            EXAMPLES::

                sage: W = WeylGroup(['A',3,1], prefix='s')
                sage: w = W.from_reduced_word([2,1,3,2])
                sage: B = crystals.AffineFactorization(w,3)
                sage: for x in B:
                ....:     x
                ....:     x.to_tableau().pp()
                (1, s2*s1, s3*s2)
                  1  1
                  2  2
                (s2, s1, s3*s2)
                  1  1
                  2  3
                (s2, s3*s1, s2)
                  1  2
                  2  3
                (s2*s1, 1, s3*s2)
                  1  1
                  3  3
                (s2*s1, s3, s2)
                  1  2
                  3  3
                (s2*s1, s3*s2, 1)
                  2  2
                  3  3
            """

def affine_factorizations(w, l, weight=None):
    """
    Return all factorizations of `w` into `l` factors or of weight ``weight``.

    INPUT:

    - ``w`` -- an (affine) permutation or element of the (affine) Weyl group

    - ``l`` -- nonnegative integer

    - ``weight`` -- (default: ``None``) tuple of nonnegative integers
      specifying the length of the factors

    EXAMPLES::

       sage: W = WeylGroup(['A',3,1], prefix='s')
       sage: w = W.from_reduced_word([3,2,3,1,0,1])
       sage: from sage.combinat.crystals.affine_factorization import affine_factorizations
       sage: affine_factorizations(w,4)
       [[s2, s3, s0, s2*s1*s0],
       [s2, s3, s2*s0, s1*s0],
       [s2, s3, s2*s1*s0, s1],
       [s2, s3*s2, s0, s1*s0],
       [s2, s3*s2, s1*s0, s1],
       [s2, s3*s2*s1, s0, s1],
       [s3*s2, s3, s0, s1*s0],
       [s3*s2, s3, s1*s0, s1],
       [s3*s2, s3*s1, s0, s1],
       [s3*s2*s1, s3, s0, s1]]

       sage: W = WeylGroup(['A',2], prefix='s')
       sage: w0 = W.long_element()
       sage: affine_factorizations(w0,3)
       [[1, s1, s2*s1],
       [1, s2*s1, s2],
       [s1, 1, s2*s1],
       [s1, s2, s1],
       [s1, s2*s1, 1],
       [s2, s1, s2],
       [s2*s1, 1, s2],
       [s2*s1, s2, 1]]
       sage: affine_factorizations(w0,3,(0,1,2))
       [[1, s1, s2*s1]]
       sage: affine_factorizations(w0,3,(1,1,1))
       [[s1, s2, s1], [s2, s1, s2]]
       sage: W = WeylGroup(['A',3], prefix='s')
       sage: w0 = W.long_element()
       sage: affine_factorizations(w0,6,(1,1,1,1,1,1))  # long time
       [[s1, s2, s1, s3, s2, s1],
       [s1, s2, s3, s1, s2, s1],
       [s1, s2, s3, s2, s1, s2],
       [s1, s3, s2, s1, s3, s2],
       [s1, s3, s2, s3, s1, s2],
       [s2, s1, s2, s3, s2, s1],
       [s2, s1, s3, s2, s1, s3],
       [s2, s1, s3, s2, s3, s1],
       [s2, s3, s1, s2, s1, s3],
       [s2, s3, s1, s2, s3, s1],
       [s2, s3, s2, s1, s2, s3],
       [s3, s1, s2, s1, s3, s2],
       [s3, s1, s2, s3, s1, s2],
       [s3, s2, s1, s2, s3, s2],
       [s3, s2, s1, s3, s2, s3],
       [s3, s2, s3, s1, s2, s3]]
       sage: affine_factorizations(w0,6,(0,0,0,1,2,3))
       [[1, 1, 1, s1, s2*s1, s3*s2*s1]]
    """

class FactorizationToTableaux(CrystalMorphism):
    def is_isomorphism(self) -> bool:
        """
        Return ``True`` as this is an isomorphism.

        EXAMPLES::

            sage: W = WeylGroup(['A',3,1], prefix='s')
            sage: w = W.from_reduced_word([2,1,3,2])
            sage: B = crystals.AffineFactorization(w,3)
            sage: phi = B._tableaux_isomorphism
            sage: phi.is_isomorphism()
            True

        TESTS::

            sage: W = WeylGroup(['A',4,1], prefix='s')
            sage: w = W.from_reduced_word([2,1,3,2,4,3,2,1])
            sage: B = crystals.AffineFactorization(w, 4)         # long time
            sage: phi = B._tableaux_isomorphism                  # long time
            sage: all(phi(b).e(i) == phi(b.e(i)) and             # long time
            ....:     phi(b).f(i) == phi(b.f(i))
            ....:     for b in B for i in B.index_set())
            True
            sage: set(phi(b) for b in B) == set(phi.codomain())  # long time
            True
        """
    is_embedding = is_isomorphism
    is_surjective = is_isomorphism
