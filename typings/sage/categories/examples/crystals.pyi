from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.graphs.digraph import DiGraph as DiGraph
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class HighestWeightCrystalOfTypeA(UniqueRepresentation, Parent):
    """
    An example of a crystal: the highest weight crystal of type `A_n`
    of highest weight `\\omega_1`.

    The purpose of this class is to provide a minimal template for
    implementing crystals. See
    :class:`~sage.combinat.crystals.letters.CrystalOfLetters` for a
    full featured and optimized implementation.

    EXAMPLES::

        sage: C = Crystals().example()
        sage: C
        Highest weight crystal of type A_3 of highest weight omega_1
        sage: C.category()
        Category of classical crystals

    The elements of this crystal are in the set `\\{1,\\ldots,n+1\\}`::

        sage: C.list()
        [1, 2, 3,  4]
        sage: C.module_generators[0]
        1

    The crystal operators themselves correspond to the elementary
    transpositions::

        sage: b = C.module_generators[0]
        sage: b.f(1)
        2
        sage: b.f(1).e(1) == b
        True

    Only the following basic operations are implemented:

    - :meth:`~sage.categories.crystals.Crystals.cartan_type` or an attribute _cartan_type
    - an attribute module_generators
    - :meth:`.Element.e`
    - :meth:`.Element.f`

    All the other usual crystal operations are inherited from the
    categories; for example::

        sage: C.cardinality()
        4

    TESTS::

        sage: C = Crystals().example()
        sage: TestSuite(C).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          running ._test_stembridge_local_axioms() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_fast_iter() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
        running ._test_stembridge_local_axioms() . . . pass
    """
    n: Incomplete
    module_generators: Incomplete
    def __init__(self, n: int = 3) -> None:
        """
        EXAMPLES::

            sage: C = sage.categories.examples.crystals.HighestWeightCrystalOfTypeA(n=4)
            sage: C == Crystals().example(n=4)
            True
        """
    class Element(ElementWrapper):
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: C = Crystals().example(4)
                sage: [[c,i,c.e(i)] for i in C.index_set() for c in C if c.e(i) is not None]
                [[2, 1, 1], [3, 2, 2], [4, 3, 3], [5, 4, 4]]
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: C = Crystals().example(4)
                sage: [[c,i,c.f(i)] for i in C.index_set() for c in C if c.f(i) is not None]
                [[1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5]]
            """

class NaiveCrystal(UniqueRepresentation, Parent):
    '''
    This is an example of a "crystal" which does not come from any kind of
    representation, designed primarily to test the Stembridge local rules with.
    The crystal has vertices labeled 0 through 5, with 0 the highest weight.

    The code here could also possibly be generalized to create a class that
    automatically builds a crystal from an edge-colored digraph, if someone
    feels adventurous.

    Currently, only the methods :meth:`highest_weight_vector`, :meth:`e`, and :meth:`f` are
    guaranteed to work.

    EXAMPLES::

        sage: C = Crystals().example(choice=\'naive\')
        sage: C.highest_weight_vector()
        0
    '''
    n: int
    G: Incomplete
    module_generators: Incomplete
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: C = sage.categories.examples.crystals.NaiveCrystal()
            sage: C == Crystals().example(choice='naive')
            True
        """
    class Element(ElementWrapper):
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: C = Crystals().example(choice='naive')
                sage: [[c,i,c.e(i)] for i in C.index_set() for c in [C(j) for j in [0..5]] if c.e(i) is not None]
                [[1, 1, 0], [2, 1, 1], [3, 1, 2], [5, 1, 3], [4, 2, 0], [5, 2, 4]]
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: C = Crystals().example(choice='naive')
                sage: [[c,i,c.f(i)] for i in C.index_set() for c in [C(j) for j in [0..5]] if c.f(i) is not None]
                [[0, 1, 1], [1, 1, 2], [2, 1, 3], [3, 1, 5], [0, 2, 4], [4, 2, 5]]
            """
