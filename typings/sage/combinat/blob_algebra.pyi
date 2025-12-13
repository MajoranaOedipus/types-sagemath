from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.diagram_algebras import TL_diagram_ascii_art as TL_diagram_ascii_art, TemperleyLiebDiagrams as TemperleyLiebDiagrams, diagram_latex as diagram_latex
from sage.combinat.dyck_word import DyckWords as DyckWords
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.subset import powerset as powerset
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element, get_coercion_model as get_coercion_model
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class BlobDiagram(Element):
    """
    A blob diagram.

    A blob diagram consists of a perfect matching of the set
    `\\{1, \\ldots, n\\} \\sqcup \\{-1, \\ldots, -n\\}` such that the result
    is a noncrossing matching (a :class:`Temperley-Lieb diagram
    <sage.combinat.diagram_algebras.TemperleyLiebDiagram>`), divided
    into two sets of pairs: one for the pairs with blobs and one for
    those without. The blobed pairs must either be either the leftmost
    propagating strand or to the left of it and not nested.
    """
    marked: Incomplete
    unmarked: Incomplete
    def __init__(self, parent, marked, unmarked) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: B = BD4([[1,-3]], [[2,-4], [3,4], [-1,-2]])
            sage: TestSuite(B).run()
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: B = BD4([[1,-3]], [[2,-4], [3,4], [-1,-2]])
            sage: hash(B) in [hash(D) for D in BD4]
            True
            sage: len(set([hash(D) for D in BD4])) == len(BD4)
            True
        """
    def temperley_lieb_diagram(self):
        """
        Return the Temperley-Lieb diagram corresponding to ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: B = BD4([[1,-3]], [[2,-4], [3,4], [-1,-2]])
            sage: B.temperley_lieb_diagram()
            {{-4, 2}, {-3, 1}, {-2, -1}, {3, 4}}
        """

class BlobDiagrams(Parent, UniqueRepresentation):
    """
    The set of all blob diagrams.
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: TestSuite(BD4).run()
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: BD4.cardinality()
            70
        """
    def order(self):
        """
        Return the order of ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: BD4.order()
            4
        """
    @cached_method
    def base_set(self):
        """
        Return the base set of ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: sorted(BD4.base_set())
            [-4, -3, -2, -1, 1, 2, 3, 4]
        """
    def __contains__(self, X) -> bool:
        """
        Check if ``X`` is contained in ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD4 = BlobDiagrams(4)
            sage: BD4([[1,-3], [-1,-2]], [[2,-4], [3,4]])  # indirect doctest
            ({{-3, 1}, {-2, -1}}, {{-4, 2}, {3, 4}})
            sage: BD4([[1,4], [-1,-2], [-3,-4]], [[2,3]])  # indirect doctest
            ({{-4, -3}, {-2, -1}, {1, 4}}, {{2, 3}})

            sage: BD4([[1,-2], [-1,-3]], [[2,-4], [3,4]])  # crossing strands
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[1,-4], [-1,-2]], [[2,-3], [3,4]])  # crossing strands
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[1,-2], [-1,-3]], [[3,-4], [2,4]])  # crossing strands
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[1,-3], [-1,-2], [3,4]], [[2,-4]])  # trapped blob cup
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[-1,3], [1,2], [-3,-4]], [[-2,4]])  # trapped blob cap
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[1,4], [-1,-2], [-3,-4], [2,3]], [])  # nested blob cup
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[-1,-4], [1,2], [3,4], [-2,-3]], [])  # nested blob cap
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
            sage: BD4([[3,-3]], [[1,-1],[2,-2],[4,-4]])  # trapped propagating line
            Traceback (most recent call last):
            ...
            ValueError: not a blob diagram of order 4
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: from sage.combinat.blob_algebra import BlobDiagrams
            sage: BD3 = BlobDiagrams(3)
            sage: sorted(BD3)
            [({}, {{-3, -2}, {-1, 1}, {2, 3}}),
             ({}, {{-3, -2}, {-1, 3}, {1, 2}}),
             ({}, {{-3, 1}, {-2, -1}, {2, 3}}),
             ({}, {{-3, 3}, {-2, -1}, {1, 2}}),
             ({}, {{-3, 3}, {-2, 2}, {-1, 1}}),
             ({{-3, 1}}, {{-2, -1}, {2, 3}}),
             ({{-3, 3}}, {{-2, -1}, {1, 2}}),
             ({{-2, -1}}, {{-3, 1}, {2, 3}}),
             ({{-2, -1}}, {{-3, 3}, {1, 2}}),
             ({{-1, 1}}, {{-3, -2}, {2, 3}}),
             ({{-1, 1}}, {{-3, 3}, {-2, 2}}),
             ({{-1, 3}}, {{-3, -2}, {1, 2}}),
             ({{1, 2}}, {{-3, -2}, {-1, 3}}),
             ({{1, 2}}, {{-3, 3}, {-2, -1}}),
             ({{-3, 1}, {-2, -1}}, {{2, 3}}),
             ({{-3, 3}, {-2, -1}}, {{1, 2}}),
             ({{-3, 3}, {1, 2}}, {{-2, -1}}),
             ({{-2, -1}, {1, 2}}, {{-3, 3}}),
             ({{-1, 3}, {1, 2}}, {{-3, -2}}),
             ({{-3, 3}, {-2, -1}, {1, 2}}, {})]
        """
    Element = BlobDiagram

class BlobAlgebra(CombinatorialFreeModule):
    """
    The blob algebra.

    The *blob algebra* (also known as the Temperley-Lieb algebra of type `B`
    in [ILZ2018]_, but is a quotient of the Temperley-Lieb algebra of type `B`
    defined in [Graham1985]_) is a diagram-type algebra introduced in
    [MS1994]_ whose basis consists of :class:`Temperley-Lieb diagrams
    <sage.combinat.diagram_algebras.TemperleyLiebDiagram>`, noncrossing
    perfect matchings, that may contain blobs on strands that can be
    deformed so that the blob touches the left side (which we can think of
    as a frozen pole).

    The form we give here has 3 parameters, the natural one from the
    :class:`Temperley-Lieb algebra <sage.combinat.diagram_algebras.TemperleyLiebAlgebra>`,
    one for the idempotent relation, and one for a loop with a blob.

    INPUT:

    - ``k`` -- the order
    - ``q1`` -- the loop parameter
    - ``q2`` -- the idempotent parameter
    - ``q3`` -- the blob loop parameter

    EXAMPLES::

        sage: R.<q,r,s> = ZZ[]
        sage: B4 = algebras.Blob(4, q, r, s)
        sage: B = sorted(B4.basis())
        sage: B[14]
        B({{-4, -3}}, {{-2, -1}, {1, 2}, {3, 4}})
        sage: B[40]
        B({{3, 4}}, {{-4, -3}, {-2, -1}, {1, 2}})
        sage: B[14] * B[40]
        q*r*s*B({}, {{-4, -3}, {-2, -1}, {1, 2}, {3, 4}})

    REFERENCES:

    - [MS1994]_
    - [ILZ2018]_
    """
    @staticmethod
    def __classcall_private__(cls, k, q1, q2, q3, base_ring=None, prefix: str = 'B'):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: R.<q,r,s> = ZZ[]
            sage: B3 = algebras.Blob(3, q, r, s)
            sage: Bp = algebras.Blob(3, q, r, s, R, prefix='B')
            sage: B3 is Bp
            True
        """
    def __init__(self, k, q1, q2, q3, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q,r,s> = ZZ[]
            sage: B4 = algebras.Blob(4, q, r, s)
            sage: TestSuite(B4).run()

            sage: B3 = algebras.Blob(3, q, r, s)
            sage: B = list(B3.basis())
            sage: TestSuite(B3).run(elements=B)  # long time
        """
    def order(self):
        """
        Return the order of ``self``.

        The order of a partition algebra is defined as half of the number
        of nodes in the diagrams.

        EXAMPLES::

            sage: R.<q,r,s> = ZZ[]
            sage: B4 = algebras.Blob(4, q, r, s)
            sage: B4.order()
            4
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the basis element `1`.

        EXAMPLES::

            sage: R.<q,r,s> = ZZ[]
            sage: B4 = algebras.Blob(4, q, r, s)
            sage: B4.one_basis()
            ({}, {{-4, 4}, {-3, 3}, {-2, 2}, {-1, 1}})
        """
    def product_on_basis(self, top, bot):
        """
        Return the product of the basis elements indexed by ``top``
        and ``bot``.

        EXAMPLES::

            sage: R.<q,r,s> = ZZ[]
            sage: B4 = algebras.Blob(4, q, r, s)
            sage: B = B4.basis()
            sage: BD = sorted(B.keys())
            sage: BD[14]
            ({{-4, -3}}, {{-2, -1}, {1, 2}, {3, 4}})
            sage: BD[40]
            ({{3, 4}}, {{-4, -3}, {-2, -1}, {1, 2}})
            sage: B4.product_on_basis(BD[14], BD[40])
            q*r*s*B({}, {{-4, -3}, {-2, -1}, {1, 2}, {3, 4}})
            sage: all(len((x*y).support()) == 1 for x in B for y in B)
            True
        """
