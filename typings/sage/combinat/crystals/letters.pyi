import _cython_3_2_1
import sage.structure.element
import sage.structure.parent
import sage.structure.unique_representation
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.regular_supercrystals import RegularSuperCrystals as RegularSuperCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

CrystalOfLetters: _cython_3_2_1.cython_function_or_method

class BKKLetter(Letter):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """BKKLetter.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2398)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: c = C(-2)
            sage: c.e(-2)
            -3
            sage: c = C(1)
            sage: c.e(0)
            -1
            sage: c = C(2)
            sage: c.e(1)
            1
            sage: c.e(-2)"""
    def f(self, inti) -> Letter:
        """BKKLetter.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2438)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: c = C.an_element()
            sage: c.f(-2)
            -2
            sage: c = C(-1)
            sage: c.f(0)
            1
            sage: c = C(1)
            sage: c.f(1)
            2
            sage: c.f(-2)"""
    @overload
    def weight(self) -> Any:
        """BKKLetter.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

        Return weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: c = C(-1)
            sage: c.weight()
            (0, 0, 1, 0, 0)
            sage: c = C(2)
            sage: c.weight()
            (0, 0, 0, 0, 1)"""
    @overload
    def weight(self) -> Any:
        """BKKLetter.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

        Return weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: c = C(-1)
            sage: c.weight()
            (0, 0, 1, 0, 0)
            sage: c = C(2)
            sage: c.weight()
            (0, 0, 0, 0, 1)"""
    @overload
    def weight(self) -> Any:
        """BKKLetter.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

        Return weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: c = C(-1)
            sage: c.weight()
            (0, 0, 1, 0, 0)
            sage: c = C(2)
            sage: c.weight()
            (0, 0, 0, 0, 1)"""

class ClassicalCrystalOfLetters(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 120)

        A generic class for classical crystals of letters.

        All classical crystals of letters should be instances of this class
        or of subclasses. To define a new crystal of letters, one only
        needs to implement a class for the elements (which subclasses
        :class:`~sage.combinat.crystals.Letter`), with appropriate
        `e_i` and `f_i` operations. If the module generator is not `1`, one also
        needs to define the subclass
        :class:`~sage.combinat.crystals.letters.ClassicalCrystalOfLetters` for the
        crystal itself.

        The basic assumption is that crystals of letters are small, but
        used intensively as building blocks. Therefore, we explicitly build
        in memory the list of all elements, the crystal graph and its
        transitive closure, so as to make the following operations constant
        time: ``list``, ``cmp``, (todo: ``phi``, ``epsilon``, ``e``, and
        ``f`` with caching)
    """
    def __init__(self, cartan_type, element_class, element_print_style=..., dual=...) -> Any:
        """ClassicalCrystalOfLetters.__init__(self, cartan_type, element_class, element_print_style=None, dual=None)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 140)

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: C.category()
            Category of classical crystals
            sage: TestSuite(C).run()"""
    @overload
    def list(self) -> Any:
        """ClassicalCrystalOfLetters.list(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 251)

        Return a list of the elements of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: C.list()
            [1, 2, 3, 4, 5, 6]"""
    @overload
    def list(self) -> Any:
        """ClassicalCrystalOfLetters.list(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 251)

        Return a list of the elements of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: C.list()
            [1, 2, 3, 4, 5, 6]"""
    @overload
    def lt_elements(self, x, y) -> Any:
        """ClassicalCrystalOfLetters.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 287)

        Return ``True`` if and only if there is a path from ``x`` to ``y`` in
        the crystal graph, when ``x`` is not equal to ``y``.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Letters(['A', 5])
            sage: x = C(1)
            sage: y = C(2)
            sage: C.lt_elements(x,y)
            True
            sage: C.lt_elements(y,x)
            False
            sage: C.lt_elements(x,x)
            False
            sage: C = crystals.Letters(['D', 4])
            sage: C.lt_elements(C(4),C(-4))
            False
            sage: C.lt_elements(C(-4),C(4))
            False"""
    @overload
    def lt_elements(self, x, y) -> Any:
        """ClassicalCrystalOfLetters.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 287)

        Return ``True`` if and only if there is a path from ``x`` to ``y`` in
        the crystal graph, when ``x`` is not equal to ``y``.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Letters(['A', 5])
            sage: x = C(1)
            sage: y = C(2)
            sage: C.lt_elements(x,y)
            True
            sage: C.lt_elements(y,x)
            False
            sage: C.lt_elements(x,x)
            False
            sage: C = crystals.Letters(['D', 4])
            sage: C.lt_elements(C(4),C(-4))
            False
            sage: C.lt_elements(C(-4),C(4))
            False"""
    @overload
    def lt_elements(self, y, x) -> Any:
        """ClassicalCrystalOfLetters.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 287)

        Return ``True`` if and only if there is a path from ``x`` to ``y`` in
        the crystal graph, when ``x`` is not equal to ``y``.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Letters(['A', 5])
            sage: x = C(1)
            sage: y = C(2)
            sage: C.lt_elements(x,y)
            True
            sage: C.lt_elements(y,x)
            False
            sage: C.lt_elements(x,x)
            False
            sage: C = crystals.Letters(['D', 4])
            sage: C.lt_elements(C(4),C(-4))
            False
            sage: C.lt_elements(C(-4),C(4))
            False"""
    def __call__(self, value) -> Any:
        """ClassicalCrystalOfLetters.__call__(self, value)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 202)

        Parse input to valid values to give to ``_element_constructor_()``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: c = C((1,))
            sage: C([1]) == c
            True"""
    def __contains__(self, x) -> Any:
        """ClassicalCrystalOfLetters.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 275)

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: 1 in C
            False
            sage: C(1) in C
            True"""
    def __iter__(self) -> Any:
        """ClassicalCrystalOfLetters.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 239)

        Iterate through ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: [x for x in C]
            [1, 2, 3, 4, 5, 6]"""

class ClassicalCrystalOfLettersWrapped(ClassicalCrystalOfLetters):
    '''File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2987)

        Crystal of letters by wrapping another crystal.

        This is used for a crystal of letters of type `E_8` and `F_4`.

        This class follows the same output as the other crystal of letters,
        where `b` is represented by the "letter" with `\\varphi_i(b)` (resp.,
        `\\varepsilon_i`) number of `i`\'s (resp., `-i`\'s or `\\bar{i}`\'s).
        However, this uses an auxiliary crystal to construct these letters
        to avoid hardcoding the crystal elements and the corresponding edges;
        in particular, the 248 nodes of `E_8`.
    '''
    def __init__(self, cartan_type) -> Any:
        """ClassicalCrystalOfLettersWrapped.__init__(self, cartan_type)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 3000)

        Initialize ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: TestSuite(C).run()  # long time

            sage: C = crystals.Letters(['F', 4])
            sage: TestSuite(C).run()"""
    def __call__(self, value) -> Any:
        """ClassicalCrystalOfLettersWrapped.__call__(self, value)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 3014)

        Parse input to valid values to give to ``_element_constructor_()``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: c = C((8,))
            sage: c == C.module_generators[0]
            True
            sage: C([8]) == c
            True"""

class CrystalOfBKKLetters(ClassicalCrystalOfLetters):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2500)

        Crystal of letters for Benkart-Kang-Kashiwara supercrystals.

        This implements the `\\mathfrak{gl}(m|n)` crystal of
        Benkart, Kang and Kashiwara [BKK2000]_.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [1, 1]]); C
            The crystal of letters for type ['A', [1, 1]]

            sage: C = crystals.Letters(['A', [2,4]], dual=True); C
            The crystal of letters for type ['A', [2, 4]] (dual)
    """

    class Element(Letter):
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def e(self, inti) -> Letter:
            """BKKLetter.e(self, int i) -> Letter

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2398)

            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', [2, 1]])
                sage: c = C(-2)
                sage: c.e(-2)
                -3
                sage: c = C(1)
                sage: c.e(0)
                -1
                sage: c = C(2)
                sage: c.e(1)
                1
                sage: c.e(-2)"""
        def f(self, inti) -> Letter:
            """BKKLetter.f(self, int i) -> Letter

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2438)

            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', [2, 1]])
                sage: c = C.an_element()
                sage: c.f(-2)
                -2
                sage: c = C(-1)
                sage: c.f(0)
                1
                sage: c = C(1)
                sage: c.f(1)
                2
                sage: c.f(-2)"""
        @overload
        def weight(self) -> Any:
            """BKKLetter.weight(self)

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

            Return weight of ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', [2, 1]])
                sage: c = C(-1)
                sage: c.weight()
                (0, 0, 1, 0, 0)
                sage: c = C(2)
                sage: c.weight()
                (0, 0, 0, 0, 1)"""
        @overload
        def weight(self) -> Any:
            """BKKLetter.weight(self)

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

            Return weight of ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', [2, 1]])
                sage: c = C(-1)
                sage: c.weight()
                (0, 0, 1, 0, 0)
                sage: c = C(2)
                sage: c.weight()
                (0, 0, 0, 0, 1)"""
        @overload
        def weight(self) -> Any:
            """BKKLetter.weight(self)

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2478)

            Return weight of ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A', [2, 1]])
                sage: c = C(-1)
                sage: c.weight()
                (0, 0, 1, 0, 0)
                sage: c = C(2)
                sage: c.weight()
                (0, 0, 0, 0, 1)"""
    def __init__(self, ct, dual) -> Any:
        """CrystalOfBKKLetters.__init__(self, ct, dual)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2528)

        Initialize ``self``.

        EXAMPLES::

            sage: crystals.Letters(['A', [2, 1]])
            The crystal of letters for type ['A', [2, 1]]"""
    @staticmethod
    def __classcall_private__(cls, ct, dual=...) -> Any:
        """CrystalOfBKKLetters.__classcall_private__(cls, ct, dual=None)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2515)

        TESTS::

            sage: crystals.Letters(['A', [1, 1]])
            The crystal of letters for type ['A', [1, 1]]"""
    def __iter__(self) -> Any:
        """CrystalOfBKKLetters.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2543)

        Iterate through ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: [x for x in C]
            [-3, -2, -1, 1, 2]"""

class CrystalOfQueerLetters(ClassicalCrystalOfLetters):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2580)

        Queer crystal of letters elements.

        The index set is of the form `\\{-n, \\ldots, -1, 1, \\ldots, n\\}`.
        For `1 < i \\leq n`, the operators `e_{-i}` and `f_{-i}` are defined as

        .. MATH::

            f_{-i} = s_{w^{-1}_i} f_{-1} s_{w_i}, \\quad
            e_{-i} = s_{w^{-1}_i} e_{-1} s_{w_i},

        where `w_i = s_2 \\cdots s_i s_1 \\cdots s_{i-1}` and `s_i` is the
        reflection along the `i`-string in the crystal. See [GJK+2014]_.

        TESTS::

            sage: Q = crystals.Letters(['Q',4])
            sage: Q.list()
            [1, 2, 3, 4]
            sage: [ [x < y for y in Q] for x in Q ]
            [[False, True, True, True],
             [False, False, True, True],
             [False, False, False, True],
             [False, False, False, False]]
            sage: Q.module_generators
            (1,)
            sage: TestSuite(Q).run()
    """

    class Element(Letter):
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2685)

            Queer supercrystal letters elements.

            TESTS::

                sage: Q = crystals.Letters(['Q',3])
                sage: Q.list()
                [1, 2, 3]
                sage: [ [x < y for y in Q] for x in Q ]
                [[False, True, True], [False, False, True], [False, False, False]]

            ::

                sage: Q = crystals.Letters(['Q',3])
                sage: Q(1) < Q(1), Q(1) < Q(2), Q(2)< Q(1)
                (False, True, False)

            ::

                sage: TestSuite(Q).run()
    """
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def e(self, inti) -> Letter:
            """QueerLetter_element.e(self, int i) -> Letter

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2718)

            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: Q = crystals.Letters(['Q',3])
                sage: [(c,i,c.e(i)) for i in Q.index_set() for c in Q if c.e(i) is not None]
                [(2, 1, 1), (3, 2, 2), (3, -2, 2), (2, -1, 1)]"""
        def epsilon(self, inti) -> int:
            """QueerLetter_element.epsilon(self, int i) -> int

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2750)

            Return `\\varepsilon_i` of ``self``.

            EXAMPLES::

                sage: Q = crystals.Letters(['Q',3])
                sage: [(c,i) for i in Q.index_set() for c in Q if c.epsilon(i) != 0]
                [(2, 1), (3, 2), (3, -2), (2, -1)]"""
        def f(self, inti) -> Letter:
            """QueerLetter_element.f(self, int i) -> Letter

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2734)

            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: Q = crystals.Letters(['Q',3])
                sage: [(c,i,c.f(i)) for i in Q.index_set() for c in Q if c.f(i) is not None]
                [(1, 1, 2), (2, 2, 3), (2, -2, 3), (1, -1, 2)]"""
        def phi(self, inti) -> int:
            """QueerLetter_element.phi(self, int i) -> int

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2764)

            Return `\\varphi_i` of ``self``.

            EXAMPLES::

                sage: Q = crystals.Letters(['Q',3])
                sage: [(c,i) for i in Q.index_set() for c in Q if c.phi(i) != 0]
                [(1, 1), (2, 2), (2, -2), (1, -1)]"""
        @overload
        def weight(self) -> Any:
            """QueerLetter_element.weight(self)

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2707)

            Return the weight of ``self``.

            EXAMPLES::

                sage: [v.weight() for v in crystals.Letters(['Q',4])]
                [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""
        @overload
        def weight(self) -> Any:
            """QueerLetter_element.weight(self)

            File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2707)

            Return the weight of ``self``.

            EXAMPLES::

                sage: [v.weight() for v in crystals.Letters(['Q',4])]
                [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""
    def __init__(self, ct) -> Any:
        """CrystalOfQueerLetters.__init__(self, ct)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2622)

        Initialize ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3]); Q
            The queer crystal of letters for q(3)
            sage: Q.module_generators
            (1,)
            sage: Q._index_set
            (1, 2, -2, -1)
            sage: Q._list
            [1, 2, 3]"""
    @overload
    def index_set(self) -> Any:
        """CrystalOfQueerLetters.index_set(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2667)

        Return index set of ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: Q.index_set()
            (1, 2, -2, -1)"""
    @overload
    def index_set(self) -> Any:
        """CrystalOfQueerLetters.index_set(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2667)

        Return index set of ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: Q.index_set()
            (1, 2, -2, -1)"""
    @staticmethod
    def __classcall_private__(cls, ct) -> Any:
        """CrystalOfQueerLetters.__classcall_private__(cls, ct)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2609)

        Normalize input to ensure a unique representation.

        TESTS::

            sage: crystals.Letters(['Q',3])
            The queer crystal of letters for q(3)"""
    def __iter__(self) -> Any:
        """CrystalOfQueerLetters.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2643)

        Iterate through ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: [x for x in Q]
            [1, 2, 3]"""

class Crystal_of_letters_type_A_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 678)

        Type `A` crystal of letters elements.

        TESTS::

            sage: C = crystals.Letters(['A',3])
            sage: C.list()
            [1, 2, 3, 4]
            sage: [ [x < y for y in C] for x in C ]
            [[False, True, True, True],
             [False, False, True, True],
             [False, False, False, True],
             [False, False, False, False]]

        ::

            sage: C = crystals.Letters(['A',5])
            sage: C(1) < C(1), C(1) < C(2), C(1) < C(3), C(2) < C(1)
            (False, True, True, False)

        ::

            sage: TestSuite(C).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """Crystal_of_letters_type_A_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 714)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',4])
            sage: [(c,i,c.e(i)) for i in C.index_set() for c in C if c.e(i) is not None]
            [(2, 1, 1), (3, 2, 2), (4, 3, 3), (5, 4, 4)]"""
    def epsilon(self, inti) -> int:
        """Crystal_of_letters_type_A_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 744)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',4])
            sage: [(c,i) for i in C.index_set() for c in C if c.epsilon(i) != 0]
            [(2, 1), (3, 2), (4, 3), (5, 4)]"""
    def f(self, inti) -> Letter:
        """Crystal_of_letters_type_A_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 729)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',4])
            sage: [(c,i,c.f(i)) for i in C.index_set() for c in C if c.f(i) is not None]
            [(1, 1, 2), (2, 2, 3), (3, 3, 4), (4, 4, 5)]"""
    def phi(self, inti) -> int:
        """Crystal_of_letters_type_A_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 758)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',4])
            sage: [(c,i) for i in C.index_set() for c in C if c.phi(i) != 0]
            [(1, 1), (2, 2), (3, 3), (4, 4)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_A_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 703)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['A',3])]
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_A_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 703)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['A',3])]
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""

class Crystal_of_letters_type_B_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 776)

        Type `B` crystal of letters elements.

        TESTS::

            sage: C = crystals.Letters(['B',3])
            sage: TestSuite(C).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """Crystal_of_letters_type_B_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 807)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['B',4])
            sage: [(c,i,c.e(i)) for i in C.index_set() for c in C if c.e(i) is not None]
            [(2, 1, 1),
             (-1, 1, -2),
             (3, 2, 2),
             (-2, 2, -3),
             (4, 3, 3),
             (-3, 3, -4),
             (0, 4, 4),
             (-4, 4, 0)]"""
    def epsilon(self, inti) -> int:
        """Crystal_of_letters_type_B_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 865)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['B',3])
            sage: [(c,i) for i in C.index_set() for c in C if c.epsilon(i) != 0]
            [(2, 1), (-1, 1), (3, 2), (-2, 2), (0, 3), (-3, 3)]"""
    def f(self, inti) -> Letter:
        """Crystal_of_letters_type_B_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 836)

        Return the actions of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['B',4])
            sage: [(c,i,c.f(i)) for i in C.index_set() for c in C if c.f(i) is not None]
            [(1, 1, 2),
             (-2, 1, -1),
             (2, 2, 3),
             (-3, 2, -2),
             (3, 3, 4),
             (-4, 3, -3),
             (4, 4, 0),
             (0, 4, -4)]"""
    def phi(self, inti) -> int:
        """Crystal_of_letters_type_B_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 886)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['B',3])
            sage: [(c,i) for i in C.index_set() for c in C if c.phi(i) != 0]
            [(1, 1), (-2, 1), (2, 2), (-3, 2), (3, 3), (0, 3)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_B_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 785)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['B',3])]
            [(1, 0, 0),
             (0, 1, 0),
             (0, 0, 1),
             (0, 0, 0),
             (0, 0, -1),
             (0, -1, 0),
             (-1, 0, 0)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_B_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 785)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['B',3])]
            [(1, 0, 0),
             (0, 1, 0),
             (0, 0, 1),
             (0, 0, 0),
             (0, 0, -1),
             (0, -1, 0),
             (-1, 0, 0)]"""

class Crystal_of_letters_type_C_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 911)

        Type `C` crystal of letters elements.

        TESTS::

            sage: C = crystals.Letters (['C',3])
            sage: C.list()
            [1, 2, 3, -3, -2, -1]
            sage: [ [x < y for y in C] for x in C ]
            [[False, True, True, True, True, True],
             [False, False, True, True, True, True],
             [False, False, False, True, True, True],
             [False, False, False, False, True, True],
             [False, False, False, False, False, True],
             [False, False, False, False, False, False]]
            sage: TestSuite(C).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """Crystal_of_letters_type_C_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 945)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C',4])
            sage: [(c,i,c.e(i)) for i in C.index_set() for c in C if c.e(i) is not None]
            [(2, 1, 1),
             (-1, 1, -2),
             (3, 2, 2),
             (-2, 2, -3),
             (4, 3, 3),
             (-3, 3, -4),
             (-4, 4, 4)]"""
    def epsilon(self, inti) -> int:
        """Crystal_of_letters_type_C_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 986)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C',3])
            sage: [(c,i) for i in C.index_set() for c in C if c.epsilon(i) != 0]
            [(2, 1), (-1, 1), (3, 2), (-2, 2), (-3, 3)]"""
    def f(self, inti) -> Letter:
        """Crystal_of_letters_type_C_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 968)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C',4])
            sage: [(c,i,c.f(i)) for i in C.index_set() for c in C if c.f(i) is not None]
            [(1, 1, 2), (-2, 1, -1), (2, 2, 3),
             (-3, 2, -2), (3, 3, 4), (-4, 3, -3), (4, 4, -4)]"""
    def phi(self, inti) -> int:
        """Crystal_of_letters_type_C_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1000)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C',3])
            sage: [(c,i) for i in C.index_set() for c in C if c.phi(i) != 0]
            [(1, 1), (-2, 1), (2, 2), (-3, 2), (3, 3)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_C_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 929)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['C',3])]
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_C_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 929)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['C',3])]
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]"""

class Crystal_of_letters_type_D_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1018)

        Type `D` crystal of letters elements.

        TESTS::

            sage: C = crystals.Letters(['D',4])
            sage: C.list()
            [1, 2, 3, 4, -4, -3, -2, -1]
            sage: TestSuite(C).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """Crystal_of_letters_type_D_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1052)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D',5])
            sage: [(c,i,c.e(i)) for i in C.index_set() for c in C if c.e(i) is not None]
            [(2, 1, 1),
             (-1, 1, -2),
             (3, 2, 2),
             (-2, 2, -3),
             (4, 3, 3),
             (-3, 3, -4),
             (5, 4, 4),
             (-4, 4, -5),
             (-5, 5, 4),
             (-4, 5, 5)]"""
    def epsilon(self, inti) -> int:
        """Crystal_of_letters_type_D_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1116)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D',4])
            sage: [(c,i) for i in C.index_set() for c in C if c.epsilon(i) != 0]
            [(2, 1), (-1, 1), (3, 2), (-2, 2), (4, 3), (-3, 3), (-4, 4), (-3, 4)]"""
    def f(self, inti) -> Letter:
        """Crystal_of_letters_type_D_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1085)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D',5])
            sage: [(c,i,c.f(i)) for i in C.index_set() for c in C if c.f(i) is not None]
            [(1, 1, 2),
             (-2, 1, -1),
             (2, 2, 3),
             (-3, 2, -2),
             (3, 3, 4),
             (-4, 3, -3),
             (4, 4, 5),
             (-5, 4, -4),
             (4, 5, -5),
             (5, 5, -4)]"""
    def phi(self, inti) -> int:
        """Crystal_of_letters_type_D_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1133)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D',4])
            sage: [(c,i) for i in C.index_set() for c in C if c.phi(i) != 0]
            [(1, 1), (-2, 1), (2, 2), (-3, 2), (3, 3), (-4, 3), (3, 4), (4, 4)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_D_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1029)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['D',4])]
            [(1, 0, 0, 0),
             (0, 1, 0, 0),
             (0, 0, 1, 0),
             (0, 0, 0, 1),
             (0, 0, 0, -1),
             (0, 0, -1, 0),
             (0, -1, 0, 0),
             (-1, 0, 0, 0)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_D_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1029)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['D',4])]
            [(1, 0, 0, 0),
             (0, 1, 0, 0),
             (0, 0, 1, 0),
             (0, 0, 0, 1),
             (0, 0, 0, -1),
             (0, 0, -1, 0),
             (0, -1, 0, 0),
             (-1, 0, 0, 0)]"""

class Crystal_of_letters_type_E6_element(LetterTuple):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1477)

        Type `E_6` crystal of letters elements. This crystal corresponds to the highest weight
        crystal `B(\\Lambda_1)`.

        TESTS::

            sage: C = crystals.Letters(['E',6])
            sage: C.module_generators
            ((1,),)
            sage: C.list()
            [(1,), (-1, 3), (-3, 4), (-4, 2, 5), (-2, 5), (-5, 2, 6), (-2, -5, 4, 6),
            (-4, 3, 6), (-3, 1, 6), (-1, 6), (-6, 2), (-2, -6, 4), (-4, -6, 3, 5),
            (-3, -6, 1, 5), (-1, -6, 5), (-5, 3), (-3, -5, 1, 4), (-1, -5, 4), (-4, 1, 2),
            (-1, -4, 2, 3), (-3, 2), (-2, -3, 4), (-4, 5), (-5, 6), (-6,), (-2, 1), (-1, -2, 3)]
            sage: TestSuite(C).run()
            sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None)
            True
            sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None)
            True
            sage: G = C.digraph()
            sage: G.show(edge_labels=true, figsize=12, vertex_size=1)                       # needs sage.plot
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E6_element.e(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1558)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: C((-1,3)).e(1)
            (1,)
            sage: C((-2,-3,4)).e(2)
            (-3, 2)
            sage: C((1,)).e(1)"""
    def f(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E6_element.f(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1646)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: C((1,)).f(1)
            (-1, 3)
            sage: C((-6,)).f(1)"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E6_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1520)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['E',6])]
            [(0, 0, 0, 0, 0, -2/3, -2/3, 2/3),
             (-1/2, 1/2, 1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, 1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, 1/2, -1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, -1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, 1/2, 1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, 1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, 1/2, -1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, -1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (0, 0, 0, 0, 1, 1/3, 1/3, -1/3),
             (1/2, 1/2, 1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, 1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (-1/2, 1/2, -1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, -1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 0, 0, 1, 0, 1/3, 1/3, -1/3),
             (-1/2, 1/2, 1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, 1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 0, 1, 0, 0, 1/3, 1/3, -1/3),
             (1/2, 1/2, -1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 1, 0, 0, 0, 1/3, 1/3, -1/3),
             (1, 0, 0, 0, 0, 1/3, 1/3, -1/3),
             (0, -1, 0, 0, 0, 1/3, 1/3, -1/3),
             (0, 0, -1, 0, 0, 1/3, 1/3, -1/3),
             (0, 0, 0, -1, 0, 1/3, 1/3, -1/3),
             (0, 0, 0, 0, -1, 1/3, 1/3, -1/3),
             (-1/2, -1/2, -1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (-1, 0, 0, 0, 0, 1/3, 1/3, -1/3)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E6_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1520)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['E',6])]
            [(0, 0, 0, 0, 0, -2/3, -2/3, 2/3),
             (-1/2, 1/2, 1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, 1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, 1/2, -1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, -1/2, 1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, 1/2, 1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, 1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (-1/2, 1/2, -1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, -1/2, -1/2, 1/2, -1/6, -1/6, 1/6),
             (0, 0, 0, 0, 1, 1/3, 1/3, -1/3),
             (1/2, 1/2, 1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (-1/2, -1/2, 1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (-1/2, 1/2, -1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, -1/2, 1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 0, 0, 1, 0, 1/3, 1/3, -1/3),
             (-1/2, 1/2, 1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (1/2, -1/2, 1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 0, 1, 0, 0, 1/3, 1/3, -1/3),
             (1/2, 1/2, -1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (0, 1, 0, 0, 0, 1/3, 1/3, -1/3),
             (1, 0, 0, 0, 0, 1/3, 1/3, -1/3),
             (0, -1, 0, 0, 0, 1/3, 1/3, -1/3),
             (0, 0, -1, 0, 0, 1/3, 1/3, -1/3),
             (0, 0, 0, -1, 0, 1/3, 1/3, -1/3),
             (0, 0, 0, 0, -1, 1/3, 1/3, -1/3),
             (-1/2, -1/2, -1/2, -1/2, -1/2, -1/6, -1/6, 1/6),
             (-1, 0, 0, 0, 0, 1/3, 1/3, -1/3)]"""

class Crystal_of_letters_type_E6_element_dual(LetterTuple):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1732)

        Type `E_6` crystal of letters elements. This crystal corresponds to the highest weight
        crystal `B(\\Lambda_6)`. This crystal is dual to `B(\\Lambda_1)` of type `E_6`.

        TESTS::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: C.module_generators
            ((6,),)
            sage: all(b==b.retract(b.lift()) for b in C)
            True
            sage: C.list()
            [(6,), (5, -6), (4, -5), (2, 3, -4), (3, -2), (1, 2, -3), (2, -1), (1, 4, -2, -3),
             (4, -1, -2), (1, 5, -4), (3, 5, -1, -4), (5, -3), (1, 6, -5), (3, 6, -1, -5), (4, 6, -3, -5),
             (2, 6, -4), (6, -2), (1, -6), (3, -1, -6), (4, -3, -6), (2, 5, -4, -6), (5, -2, -6), (2, -5),
             (4, -2, -5), (3, -4), (1, -3), (-1,)]
            sage: TestSuite(C).run()
            sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None)
            True
            sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None)
            True
            sage: G = C.digraph()
            sage: G.show(edge_labels=true, figsize=12, vertex_size=1)                       # needs sage.plot
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E6_element_dual.e(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1817)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: C((-1,)).e(1)
            (1, -3)"""
    def f(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E6_element_dual.f(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1829)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: C((6,)).f(6)
            (5, -6)
            sage: C((6,)).f(1)"""
    @overload
    def lift(self) -> LetterTuple:
        """Crystal_of_letters_type_E6_element_dual.lift(self) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1777)

        Lift an element of ``self`` to the crystal of letters
        ``crystals.Letters(['E',6])`` by taking its inverse weight.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: b = C.module_generators[0]
            sage: b.lift()
            (-6,)"""
    @overload
    def lift(self) -> Any:
        """Crystal_of_letters_type_E6_element_dual.lift(self) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1777)

        Lift an element of ``self`` to the crystal of letters
        ``crystals.Letters(['E',6])`` by taking its inverse weight.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: b = C.module_generators[0]
            sage: b.lift()
            (-6,)"""
    @overload
    def retract(self, LetterTuplep) -> LetterTuple:
        """Crystal_of_letters_type_E6_element_dual.retract(self, LetterTuple p) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1794)

        Retract element ``p``, which is an element in
        ``crystals.Letters(['E',6])`` to an element in
        ``crystals.Letters(['E',6], dual=True)`` by taking its inverse weight.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: Cd = crystals.Letters(['E',6], dual = True)
            sage: b = Cd.module_generators[0]
            sage: p = C((-1,3))
            sage: b.retract(p)
            (1, -3)
            sage: b.retract(None)"""
    @overload
    def retract(self, p) -> Any:
        """Crystal_of_letters_type_E6_element_dual.retract(self, LetterTuple p) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1794)

        Retract element ``p``, which is an element in
        ``crystals.Letters(['E',6])`` to an element in
        ``crystals.Letters(['E',6], dual=True)`` by taking its inverse weight.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: Cd = crystals.Letters(['E',6], dual = True)
            sage: b = Cd.module_generators[0]
            sage: p = C((-1,3))
            sage: b.retract(p)
            (1, -3)
            sage: b.retract(None)"""
    @overload
    def retract(self, _None) -> Any:
        """Crystal_of_letters_type_E6_element_dual.retract(self, LetterTuple p) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1794)

        Retract element ``p``, which is an element in
        ``crystals.Letters(['E',6])`` to an element in
        ``crystals.Letters(['E',6], dual=True)`` by taking its inverse weight.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: Cd = crystals.Letters(['E',6], dual = True)
            sage: b = Cd.module_generators[0]
            sage: p = C((-1,3))
            sage: b.retract(p)
            (1, -3)
            sage: b.retract(None)"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E6_element_dual.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1842)

        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: b=C.module_generators[0]
            sage: b.weight()
            (0, 0, 0, 0, 1, -1/3, -1/3, 1/3)
            sage: [v.weight() for v in C]
            [(0, 0, 0, 0, 1, -1/3, -1/3, 1/3),
            (0, 0, 0, 1, 0, -1/3, -1/3, 1/3),
            (0, 0, 1, 0, 0, -1/3, -1/3, 1/3),
            (0, 1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1/2, 1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, -1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, -1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, -1, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, -1, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, -1, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, 1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, 0, 2/3, 2/3, -2/3)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E6_element_dual.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1842)

        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: b=C.module_generators[0]
            sage: b.weight()
            (0, 0, 0, 0, 1, -1/3, -1/3, 1/3)
            sage: [v.weight() for v in C]
            [(0, 0, 0, 0, 1, -1/3, -1/3, 1/3),
            (0, 0, 0, 1, 0, -1/3, -1/3, 1/3),
            (0, 0, 1, 0, 0, -1/3, -1/3, 1/3),
            (0, 1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1/2, 1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, -1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, -1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, -1, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, -1, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, -1, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, 1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, 0, 2/3, 2/3, -2/3)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E6_element_dual.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1842)

        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6], dual = True)
            sage: b=C.module_generators[0]
            sage: b.weight()
            (0, 0, 0, 0, 1, -1/3, -1/3, 1/3)
            sage: [v.weight() for v in C]
            [(0, 0, 0, 0, 1, -1/3, -1/3, 1/3),
            (0, 0, 0, 1, 0, -1/3, -1/3, 1/3),
            (0, 0, 1, 0, 0, -1/3, -1/3, 1/3),
            (0, 1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1, 0, 0, 0, 0, -1/3, -1/3, 1/3),
            (1/2, 1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, -1, 0, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, -1/2, 1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, -1, 0, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, 1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, -1, 0, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, -1/2, 1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, -1, -1/3, -1/3, 1/3),
            (-1/2, 1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, 1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, -1/2, 1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, 1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, -1/2, 1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (-1/2, 1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (1/2, -1/2, -1/2, -1/2, -1/2, 1/6, 1/6, -1/6),
            (0, 0, 0, 0, 0, 2/3, 2/3, -2/3)]"""

class Crystal_of_letters_type_E7_element(LetterTuple):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1888)

        Type `E_7` crystal of letters elements. This crystal corresponds to the highest weight
        crystal `B(\\Lambda_7)`.

        TESTS::

            sage: C = crystals.Letters(['E',7])
            sage: C.module_generators
            ((7,),)
            sage: C.list()
            [(7,), (-7, 6), (-6, 5), (-5, 4), (-4, 2, 3), (-2, 3), (-3, 1, 2), (-1,
            2), (-3, -2, 1, 4), (-1, -2, 4), (-4, 1, 5), (-4, -1, 3, 5), (-3, 5),
            (-5, 6, 1), (-5, -1, 3, 6), (-5, -3, 4, 6), (-4, 2, 6), (-2, 6), (-6, 7,
            1), (-1, -6, 3, 7), (-6, -3, 7, 4), (-6, -4, 2, 7, 5), (-6, -2, 7, 5),
            (-5, 7, 2), (-5, -2, 4, 7), (-4, 7, 3), (-3, 1, 7), (-1, 7), (-7, 1),
            (-1, -7, 3), (-7, -3, 4), (-4, -7, 2, 5), (-7, -2, 5), (-5, -7, 6, 2),
            (-5, -2, -7, 4, 6), (-7, -4, 6, 3), (-3, -7, 1, 6), (-7, -1, 6), (-6,
            2), (-2, -6, 4), (-6, -4, 5, 3), (-3, -6, 1, 5), (-6, -1, 5), (-5, 3),
            (-3, -5, 4, 1), (-5, -1, 4), (-4, 1, 2), (-1, -4, 3, 2), (-3, 2), (-2,
            -3, 4), (-4, 5), (-5, 6), (-6, 7), (-7,), (-2, 1), (-2, -1, 3)]
            sage: TestSuite(C).run()
            sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None)
            True
            sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None)
            True
            sage: G = C.digraph()
            sage: G.show(edge_labels=true, figsize=12, vertex_size=1)                       # needs sage.plot
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E7_element.e(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1959)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',7])
            sage: C((7,)).e(7)
            sage: C((-7,6)).e(7)
            (7,)"""
    def f(self, inti) -> LetterTuple:
        """Crystal_of_letters_type_E7_element.f(self, int i) -> LetterTuple

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2141)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',7])
            sage: C((-7,)).f(7)
            sage: C((7,)).f(7)
            (-7, 6)"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E7_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1918)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['E',7])]
            [(0, 0, 0, 0, 0, 1, -1/2, 1/2), (0, 0, 0, 0, 1, 0, -1/2, 1/2), (0, 0, 0,
            1, 0, 0, -1/2, 1/2), (0, 0, 1, 0, 0, 0, -1/2, 1/2), (0, 1, 0, 0, 0, 0,
            -1/2, 1/2), (-1, 0, 0, 0, 0, 0, -1/2, 1/2), (1, 0, 0, 0, 0, 0, -1/2,
            1/2), (1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, -1, 0, 0, 0, 0, -1/2,
            1/2), (-1/2, -1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, 0, -1, 0, 0, 0, -1/2,
            1/2), (-1/2, 1/2, -1/2, 1/2, 1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, 1/2,
            1/2, 1/2, 0, 0), (0, 0, 0, -1, 0, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, -1/2,
            1/2, 1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, 1/2, 1/2, 0, 0), (1/2, 1/2,
            -1/2, -1/2, 1/2, 1/2, 0, 0), (-1/2, -1/2, -1/2, -1/2, 1/2, 1/2, 0, 0),
            (0, 0, 0, 0, -1, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, 1/2, -1/2, 1/2, 0, 0),
            (1/2, -1/2, 1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, -1/2, 1/2, -1/2, 1/2,
            0, 0), (-1/2, -1/2, -1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, 1/2, -1/2,
            -1/2, 1/2, 0, 0), (-1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 0, 0), (-1/2, 1/2,
            -1/2, -1/2, -1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, -1/2, -1/2, 1/2, 0, 0),
            (0, 0, 0, 0, 0, 1, 1/2, -1/2), (0, 0, 0, 0, 0, -1, -1/2, 1/2), (-1/2,
            1/2, 1/2, 1/2, 1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, 1/2, 1/2, -1/2, 0, 0),
            (1/2, 1/2, -1/2, 1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, -1/2, 1/2, 1/2,
            -1/2, 0, 0), (1/2, 1/2, 1/2, -1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2,
            -1/2, 1/2, -1/2, 0, 0), (-1/2, 1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (1/2,
            -1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (0, 0, 0, 0, 1, 0, 1/2, -1/2), (1/2,
            1/2, 1/2, 1/2, -1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 0,
            0), (-1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 0, 0), (1/2, -1/2, -1/2, 1/2,
            -1/2, -1/2, 0, 0), (0, 0, 0, 1, 0, 0, 1/2, -1/2), (-1/2, 1/2, 1/2, -1/2,
            -1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 0, 0), (0, 0, 1,
            0, 0, 0, 1/2, -1/2), (1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (0, 1, 0,
            0, 0, 0, 1/2, -1/2), (1, 0, 0, 0, 0, 0, 1/2, -1/2), (0, -1, 0, 0, 0, 0,
            1/2, -1/2), (0, 0, -1, 0, 0, 0, 1/2, -1/2), (0, 0, 0, -1, 0, 0, 1/2,
            -1/2), (0, 0, 0, 0, -1, 0, 1/2, -1/2), (0, 0, 0, 0, 0, -1, 1/2, -1/2),
            (-1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (-1, 0, 0, 0, 0, 0, 1/2,
            -1/2)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_E7_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1918)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['E',7])]
            [(0, 0, 0, 0, 0, 1, -1/2, 1/2), (0, 0, 0, 0, 1, 0, -1/2, 1/2), (0, 0, 0,
            1, 0, 0, -1/2, 1/2), (0, 0, 1, 0, 0, 0, -1/2, 1/2), (0, 1, 0, 0, 0, 0,
            -1/2, 1/2), (-1, 0, 0, 0, 0, 0, -1/2, 1/2), (1, 0, 0, 0, 0, 0, -1/2,
            1/2), (1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, -1, 0, 0, 0, 0, -1/2,
            1/2), (-1/2, -1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, 0, -1, 0, 0, 0, -1/2,
            1/2), (-1/2, 1/2, -1/2, 1/2, 1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, 1/2,
            1/2, 1/2, 0, 0), (0, 0, 0, -1, 0, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, -1/2,
            1/2, 1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, 1/2, 1/2, 0, 0), (1/2, 1/2,
            -1/2, -1/2, 1/2, 1/2, 0, 0), (-1/2, -1/2, -1/2, -1/2, 1/2, 1/2, 0, 0),
            (0, 0, 0, 0, -1, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, 1/2, -1/2, 1/2, 0, 0),
            (1/2, -1/2, 1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, -1/2, 1/2, -1/2, 1/2,
            0, 0), (-1/2, -1/2, -1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, 1/2, -1/2,
            -1/2, 1/2, 0, 0), (-1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 0, 0), (-1/2, 1/2,
            -1/2, -1/2, -1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, -1/2, -1/2, 1/2, 0, 0),
            (0, 0, 0, 0, 0, 1, 1/2, -1/2), (0, 0, 0, 0, 0, -1, -1/2, 1/2), (-1/2,
            1/2, 1/2, 1/2, 1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, 1/2, 1/2, -1/2, 0, 0),
            (1/2, 1/2, -1/2, 1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, -1/2, 1/2, 1/2,
            -1/2, 0, 0), (1/2, 1/2, 1/2, -1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2,
            -1/2, 1/2, -1/2, 0, 0), (-1/2, 1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (1/2,
            -1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (0, 0, 0, 0, 1, 0, 1/2, -1/2), (1/2,
            1/2, 1/2, 1/2, -1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 0,
            0), (-1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 0, 0), (1/2, -1/2, -1/2, 1/2,
            -1/2, -1/2, 0, 0), (0, 0, 0, 1, 0, 0, 1/2, -1/2), (-1/2, 1/2, 1/2, -1/2,
            -1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 0, 0), (0, 0, 1,
            0, 0, 0, 1/2, -1/2), (1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (0, 1, 0,
            0, 0, 0, 1/2, -1/2), (1, 0, 0, 0, 0, 0, 1/2, -1/2), (0, -1, 0, 0, 0, 0,
            1/2, -1/2), (0, 0, -1, 0, 0, 0, 1/2, -1/2), (0, 0, 0, -1, 0, 0, 1/2,
            -1/2), (0, 0, 0, 0, -1, 0, 1/2, -1/2), (0, 0, 0, 0, 0, -1, 1/2, -1/2),
            (-1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (-1, 0, 0, 0, 0, 0, 1/2,
            -1/2)]"""

class Crystal_of_letters_type_G_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1154)

        Type `G_2` crystal of letters elements.

        TESTS::

            sage: C = crystals.Letters(['G',2])
            sage: C.list()
            [1, 2, 3, 0, -3, -2, -1]
            sage: TestSuite(C).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """Crystal_of_letters_type_G_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1191)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['G',2])
            sage: [(c,i,c.e(i)) for i in C.index_set() for c in C if c.e(i) is not None]
            [(2, 1, 1),
             (0, 1, 3),
             (-3, 1, 0),
             (-1, 1, -2),
             (3, 2, 2),
             (-2, 2, -3)]"""
    def epsilon(self, inti) -> int:
        """Crystal_of_letters_type_G_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1259)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['G',2])
            sage: [(c,i,c.epsilon(i)) for i in C.index_set() for c in C if c.epsilon(i) != 0]
            [(2, 1, 1), (0, 1, 1), (-3, 1, 2), (-1, 1, 1), (3, 2, 1), (-2, 2, 1)]"""
    def f(self, inti) -> Letter:
        """Crystal_of_letters_type_G_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1225)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['G',2])
            sage: [(c,i,c.f(i)) for i in C.index_set() for c in C if c.f(i) is not None]
            [(1, 1, 2),
             (3, 1, 0),
             (0, 1, -3),
             (-2, 1, -1),
             (2, 2, 3),
             (-3, 2, -2)]"""
    def phi(self, inti) -> int:
        """Crystal_of_letters_type_G_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1279)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['G',2])
            sage: [(c,i,c.phi(i)) for i in C.index_set() for c in C if c.phi(i) != 0]
            [(1, 1, 1), (3, 1, 2), (0, 1, 1), (-2, 1, 1), (2, 2, 1), (-3, 2, 1)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_G_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1165)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['G',2])]
            [(1, 0, -1), (1, -1, 0), (0, 1, -1), (0, 0, 0), (0, -1, 1), (-1, 1, 0), (-1, 0, 1)]"""
    @overload
    def weight(self) -> Any:
        """Crystal_of_letters_type_G_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1165)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['G',2])]
            [(1, 0, -1), (1, -1, 0), (0, 1, -1), (0, 0, 0), (0, -1, 1), (-1, 1, 0), (-1, 0, 1)]"""

class EmptyLetter(sage.structure.element.Element):
    """EmptyLetter(parent)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 516)

    The affine letter `\\emptyset` thought of as a classical crystal letter
    in classical type `B_n` and `C_n`.

    .. WARNING::

        This is not a classical letter.

    Used in the rigged configuration bijections."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: File
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 527)

                Initialize ``self``.

                EXAMPLES::

                    sage: C = crystals.Letters(['C', 3])
                    sage: TestSuite(C('E')).run()
        """
    def e(self, inti) -> Any:
        """EmptyLetter.e(self, int i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 628)

        Return `e_i` of ``self`` which is ``None``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').e(1)"""
    def epsilon(self, inti) -> int:
        """EmptyLetter.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 650)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').epsilon(1)
            0"""
    def f(self, inti) -> Any:
        """EmptyLetter.f(self, int i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 639)

        Return `f_i` of ``self`` which is ``None``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').f(1)"""
    def phi(self, inti) -> int:
        """EmptyLetter.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 662)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').phi(1)
            0"""
    @overload
    def weight(self) -> Any:
        """EmptyLetter.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 616)

        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').weight()
            (0, 0, 0)"""
    @overload
    def weight(self) -> Any:
        """EmptyLetter.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 616)

        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['C', 3])
            sage: C('E').weight()
            (0, 0, 0)"""
    def __hash__(self) -> Any:
        """EmptyLetter.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 576)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D', 4])
            sage: hash(C('E')) == hash('E')
            True"""
    @overload
    def __reduce__(self) -> Any:
        """EmptyLetter.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 539)

        Used in pickling crystal of letters elements.

        EXAMPLES::

            sage: C = crystals.Letters(['C',3])
            sage: a = C('E')
            sage: a.__reduce__()
            (The crystal of letters for type ['C', 3], ('E',))"""
    @overload
    def __reduce__(self) -> Any:
        """EmptyLetter.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 539)

        Used in pickling crystal of letters elements.

        EXAMPLES::

            sage: C = crystals.Letters(['C',3])
            sage: a = C('E')
            sage: a.__reduce__()
            (The crystal of letters for type ['C', 3], ('E',))"""

class Letter(sage.structure.element.Element):
    """Letter(parent, int value)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 324)

    A class for letters.

    Like :class:`ElementWrapper`, plus delegates ``__lt__`` (comparison)
    to the parent.

    EXAMPLES::

        sage: from sage.combinat.crystals.letters import Letter
        sage: a = Letter(ZZ, 1)
        sage: Letter(ZZ, 1).parent()
        Integer Ring

        sage: Letter(ZZ, 1)._repr_()
        '1'

        sage: parent1 = ZZ  # Any fake value ...
        sage: parent2 = QQ  # Any fake value ...
        sage: l11 = Letter(parent1, 1)
        sage: l12 = Letter(parent1, 2)
        sage: l21 = Letter(parent2, 1)
        sage: l22 = Letter(parent2, 2)
        sage: l11 == l11
        True
        sage: l11 == l12
        False
        sage: l11 == l21 # not tested
        False

        sage: C = crystals.Letters(['B', 3])
        sage: C(0) != C(0)
        False
        sage: C(1) != C(-1)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: File
    def __init__(self, parent, intvalue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 360)

                EXAMPLES::

                    sage: C = crystals.Letters(['B',4])
                    sage: a = C(3)
                    sage: TestSuite(a).run()
        """
    def __hash__(self) -> Any:
        """Letter.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 455)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['D', 4])
            sage: hash(C(4)) == hash(4)
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Letter.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 387)

        Used in pickling crystal of letters elements.

        EXAMPLES::

            sage: C = crystals.Letters(['A',3])
            sage: a = C(1)
            sage: a.__reduce__()
            (The crystal of letters for type ['A', 3], (1,))"""
    @overload
    def __reduce__(self) -> Any:
        """Letter.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 387)

        Used in pickling crystal of letters elements.

        EXAMPLES::

            sage: C = crystals.Letters(['A',3])
            sage: a = C(1)
            sage: a.__reduce__()
            (The crystal of letters for type ['A', 3], (1,))"""

class LetterTuple(sage.structure.element.Element):
    """LetterTuple(parent, tuple value)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1303)

    Abstract class for type `E` letters."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: File
    def __init__(self, parent, tuplevalue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1307)

                Initialize ``self``.

                EXAMPLES::

                    sage: C = crystals.Letters(['E',6])
                    sage: a = C((1,-3))
                    sage: TestSuite(a).run()
        """
    def epsilon(self, inti) -> int:
        """LetterTuple.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1441)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: C((-6,)).epsilon(1)
            0
            sage: C((-6,)).epsilon(6)
            1"""
    def phi(self, inti) -> int:
        """LetterTuple.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1457)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: C((1,)).phi(1)
            1
            sage: C((1,)).phi(6)
            0"""
    def __hash__(self) -> Any:
        """LetterTuple.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1349)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 6])
            sage: hash(C((1, -3))) == hash((1, -3))
            True"""
    @overload
    def __reduce__(self) -> Any:
        """LetterTuple.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1336)

        Used in pickling of letters.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: a = C((1,-3))
            sage: a.__reduce__()
            (The crystal of letters for type ['E', 6], ((1, -3),))"""
    @overload
    def __reduce__(self) -> Any:
        """LetterTuple.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 1336)

        Used in pickling of letters.

        EXAMPLES::

            sage: C = crystals.Letters(['E',6])
            sage: a = C((1,-3))
            sage: a.__reduce__()
            (The crystal of letters for type ['E', 6], ((1, -3),))"""

class LetterWrapped(sage.structure.element.Element):
    """LetterWrapped(parent, Element value)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2782)

    Element which uses another crystal implementation and converts
    those elements to a tuple with `\\pm i`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: File
    def __init__(self, parent, Elementvalue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2787)

                Initialize ``self``.

                EXAMPLES::

                    sage: C = crystals.Letters(['E', 8])
                    sage: a = C((1,-4,5))
                    sage: TestSuite(a).run()
        """
    def e(self, inti) -> LetterWrapped:
        """LetterWrapped.e(self, int i) -> LetterWrapped

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2926)

        Return `e_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: C((-8,)).e(1)
            sage: C((-8,)).e(8)
            (-7, 8)"""
    def epsilon(self, inti) -> int:
        """LetterWrapped.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2958)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: C((-8,)).epsilon(1)
            0
            sage: C((-8,)).epsilon(8)
            1"""
    def f(self, inti) -> LetterWrapped:
        """LetterWrapped.f(self, int i) -> LetterWrapped

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2942)

        Return `f_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: C((8,)).f(6)
            sage: C((8,)).f(8)
            (7, -8)"""
    def phi(self, inti) -> int:
        """LetterWrapped.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2972)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: C((8,)).phi(8)
            1
            sage: C((8,)).phi(6)
            0"""
    def __hash__(self) -> Any:
        """LetterWrapped.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2813)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: c = C((1,-4,5))
            sage: hash(c) == hash(c.value)
            True"""
    @overload
    def __reduce__(self) -> Any:
        """LetterWrapped.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2800)

        Used in pickling of letters.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: a = C((1,-4,5))
            sage: a.__reduce__()
            (The crystal of letters for type ['E', 8], (Y(1,6) Y(4,6)^-1 Y(5,5),))"""
    @overload
    def __reduce__(self) -> Any:
        """LetterWrapped.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2800)

        Used in pickling of letters.

        EXAMPLES::

            sage: C = crystals.Letters(['E', 8])
            sage: a = C((1,-4,5))
            sage: a.__reduce__()
            (The crystal of letters for type ['E', 8], (Y(1,6) Y(4,6)^-1 Y(5,5),))"""

class QueerLetter_element(Letter):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2685)

        Queer supercrystal letters elements.

        TESTS::

            sage: Q = crystals.Letters(['Q',3])
            sage: Q.list()
            [1, 2, 3]
            sage: [ [x < y for y in Q] for x in Q ]
            [[False, True, True], [False, False, True], [False, False, False]]

        ::

            sage: Q = crystals.Letters(['Q',3])
            sage: Q(1) < Q(1), Q(1) < Q(2), Q(2)< Q(1)
            (False, True, False)

        ::

            sage: TestSuite(Q).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, inti) -> Letter:
        """QueerLetter_element.e(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2718)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: [(c,i,c.e(i)) for i in Q.index_set() for c in Q if c.e(i) is not None]
            [(2, 1, 1), (3, 2, 2), (3, -2, 2), (2, -1, 1)]"""
    def epsilon(self, inti) -> int:
        """QueerLetter_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2750)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: [(c,i) for i in Q.index_set() for c in Q if c.epsilon(i) != 0]
            [(2, 1), (3, 2), (3, -2), (2, -1)]"""
    def f(self, inti) -> Letter:
        """QueerLetter_element.f(self, int i) -> Letter

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2734)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: [(c,i,c.f(i)) for i in Q.index_set() for c in Q if c.f(i) is not None]
            [(1, 1, 2), (2, 2, 3), (2, -2, 3), (1, -1, 2)]"""
    def phi(self, inti) -> int:
        """QueerLetter_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2764)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q',3])
            sage: [(c,i) for i in Q.index_set() for c in Q if c.phi(i) != 0]
            [(1, 1), (2, 2), (2, -2), (1, -1)]"""
    @overload
    def weight(self) -> Any:
        """QueerLetter_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2707)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['Q',4])]
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""
    @overload
    def weight(self) -> Any:
        """QueerLetter_element.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/letters.pyx (starting at line 2707)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Letters(['Q',4])]
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]"""
