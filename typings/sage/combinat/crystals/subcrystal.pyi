from _typeshed import Incomplete
from sage.categories.crystals import Crystals as Crystals
from sage.categories.finite_crystals import FiniteCrystals as FiniteCrystals
from sage.categories.supercrystals import SuperCrystals as SuperCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Subcrystal(UniqueRepresentation, Parent):
    """
    A subcrystal `X` of an ambient crystal `Y` is a crystal formed by taking a
    subset of `Y` and whose crystal structure is induced by `Y`.

    INPUT:

    - ``ambient`` -- the ambient crystal
    - ``contained`` -- (optional) a set (or function) which specifies when an
      element is contained in the subcrystal; the default is everything
      possible is included
    - ``generators`` -- (optional) the generators for the subcrystal; the
      default is the generators for the ambient crystal
    - ``virtualization``, ``scaling_factors`` -- (optional)
      dictionaries whose key `i` corresponds to the sets `\\sigma_i`
      and `\\gamma_i` respectively used to define virtual crystals; see
      :class:`~sage.combinat.crystals.virtual_crystal.VirtualCrystal`
    - ``cartan_type`` -- (optional) the Cartan type for the subcrystal; the
      default is the Cartan type for the ambient crystal
    - ``index_set`` -- (optional) the index set for the subcrystal; the
      default is the index set for the Cartan type
    - ``category`` -- (optional) the category for the subcrystal; the
      default is the :class:`~sage.categories.crystals.Crystals` category

    .. SEEALSO::

        :meth:`~sage.categories.crystals.Crystals.ParentMethods.subcrystal`

    EXAMPLES:

    We build out a subcrystal starting from an element and only going
    to the lowest weight::

        sage: B = crystals.Tableaux(['A',3], shape=[2,1])
        sage: S = B.subcrystal(generators=[B(3,1,2)], direction='lower')
        sage: S.cardinality()
        11

    Here we build out in both directions starting from an element, but we
    also have restricted ourselves to type `A_2`::

        sage: T = B.subcrystal(index_set=[1,2], generators=[B(3,1,1)])
        sage: T.cardinality()
        8
        sage: list(T)
        [[[1, 1], [3]],
         [[1, 2], [3]],
         [[1, 1], [2]],
         [[2, 2], [3]],
         [[1, 2], [2]],
         [[2, 3], [3]],
         [[1, 3], [2]],
         [[1, 3], [3]]]

    Now we take the crystal corresponding to the intersection of
    the previous two subcrystals::

        sage: U = B.subcrystal(contained=lambda x: x in S and x in T, generators=B)
        sage: list(U)
        [[[2, 3], [3]], [[1, 2], [3]], [[2, 2], [3]]]

    .. TODO::

        Include support for subcrystals which only contains certain arrows.

    TESTS:

    Check that the subcrystal respects being in the category
    of supercrystals (:issue:`27368`)::

        sage: T = crystals.Tableaux(['A',[1,1]], [2,1])
        sage: S = T.subcrystal(max_depth=3)
        sage: S.category()
        Category of finite super crystals
    """
    @staticmethod
    def __classcall_private__(cls, ambient, contained=None, generators=None, virtualization=None, scaling_factors=None, cartan_type=None, index_set=None, category=None):
        """
        Normalize arguments to ensure a (relatively) unique representation.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',4], shape=[2,1])
            sage: S1 = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
            sage: S2 = B.subcrystal(generators=[B(2,1,1), B(5,2,4)], cartan_type=['A',4], index_set=(1,2))
            sage: S1 is S2
            True
        """
    module_generators: Incomplete
    def __init__(self, ambient, contained, generators, cartan_type, index_set, category) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',4], shape=[2,1])
            sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
            sage: TestSuite(S).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is in ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',4], shape=[2,1])
            sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
            sage: B(5,2,4) in S
            True
            sage: mg = B.module_generators[0]
            sage: mg in S
            True
            sage: mg.f(2).f(3) in S
            False
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',4], shape=[2,1])
            sage: S = B.subcrystal(generators=[B(2,1,1)], index_set=[1,2])
            sage: S.cardinality()
            8
            sage: B = crystals.infinity.Tableaux(['A',2])
            sage: S = B.subcrystal(max_depth=4)
            sage: S.cardinality()
            22

        TESTS:

        Check that :issue:`19481` is fixed::

            sage: from sage.combinat.crystals.virtual_crystal import VirtualCrystal
            sage: A = crystals.infinity.Tableaux(['A',3])
            sage: V = VirtualCrystal(A, {1:(1,3), 2:(2,)}, {1:1, 2:2}, cartan_type=['C',2])
            sage: V.cardinality()
            Traceback (most recent call last):
            ...
            NotImplementedError: unknown cardinality
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A',4], shape=[2,1])
            sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
            sage: S.index_set()
            (1, 2)
        """
    class Element(ElementWrapper):
        """
        An element of a subcrystal. Wraps an element in the ambient crystal.
        """
        def e(self, i):
            """
            Return `e_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',4], shape=[2,1])
                sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
                sage: mg = S.module_generators[1]
                sage: mg.e(2)
                sage: mg.e(1)
                [[1, 4], [5]]
            """
        def f(self, i):
            """
            Return `f_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',4], shape=[2,1])
                sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
                sage: mg = S.module_generators[1]
                sage: mg.f(1)
                sage: mg.f(2)
                [[3, 4], [5]]
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',4], shape=[2,1])
                sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
                sage: mg = S.module_generators[1]
                sage: mg.epsilon(1)
                1
                sage: mg.epsilon(2)
                0
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',4], shape=[2,1])
                sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
                sage: mg = S.module_generators[1]
                sage: mg.phi(1)
                0
                sage: mg.phi(2)
                1
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['A',4], shape=[2,1])
                sage: S = B.subcrystal(generators=(B(2,1,1), B(5,2,4)), index_set=[1,2])
                sage: mg = S.module_generators[1]
                sage: mg.weight()
                (0, 1, 0, 1, 1)
            """
