import _cython_3_2_1
import sage.structure.element
import sage.structure.parent
import sage.structure.unique_representation
from _typeshed import Incomplete
from sage.categories.category import ZZ as ZZ
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.typeset.ascii_art import AsciiArt as AsciiArt
from sage.typeset.unicode_art import UnicodeArt as UnicodeArt
from typing import Any, ClassVar, overload

CrystalOfSpins: _cython_3_2_1.cython_function_or_method
CrystalOfSpinsMinus: _cython_3_2_1.cython_function_or_method
CrystalOfSpinsPlus: _cython_3_2_1.cython_function_or_method

class GenericCrystalOfSpins(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 174)

        A generic crystal of spins.
    """
    def __init__(self, ct, element_class, case) -> Any:
        """GenericCrystalOfSpins.__init__(self, ct, element_class, case)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 178)

        EXAMPLES::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: TestSuite(E).run()"""
    @overload
    def lt_elements(self, x, y) -> Any:
        """GenericCrystalOfSpins.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 231)

        Return ``True`` if and only if there is a path from ``x`` to ``y``
        in the crystal graph.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: x = C([1,1,1])
            sage: y = C([-1,-1,-1])
            sage: C.lt_elements(x, y)
            True
            sage: C.lt_elements(y, x)
            False
            sage: C.lt_elements(x, x)
            False"""
    @overload
    def lt_elements(self, x, y) -> Any:
        """GenericCrystalOfSpins.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 231)

        Return ``True`` if and only if there is a path from ``x`` to ``y``
        in the crystal graph.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: x = C([1,1,1])
            sage: y = C([-1,-1,-1])
            sage: C.lt_elements(x, y)
            True
            sage: C.lt_elements(y, x)
            False
            sage: C.lt_elements(x, x)
            False"""
    @overload
    def lt_elements(self, y, x) -> Any:
        """GenericCrystalOfSpins.lt_elements(self, x, y)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 231)

        Return ``True`` if and only if there is a path from ``x`` to ``y``
        in the crystal graph.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: x = C([1,1,1])
            sage: y = C([-1,-1,-1])
            sage: C.lt_elements(x, y)
            True
            sage: C.lt_elements(y, x)
            False
            sage: C.lt_elements(x, x)
            False"""

class Spin(sage.structure.element.Element):
    """Spin(parent, tuple val)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 257)

    A spin letter in the crystal of spins.

    EXAMPLES::

        sage: C = crystals.Spins(['B',3])
        sage: c = C([1,1,1])
        sage: c
        +++
        sage: c.parent()
        The crystal of spins for type ['B', 3]

        sage: D = crystals.Spins(['B',4])
        sage: a = C([1,1,1])
        sage: b = C([-1,-1,-1])
        sage: c = D([1,1,1,1])
        sage: a == a
        True
        sage: a == b
        False
        sage: b == c
        False"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: Incomplete
    def __init__(self, parent, tupleval) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 283)

                Initialize ``self``.

                TESTS::

                    sage: C = crystals.Spins(['B',3])
                    sage: c = C([1,1,1])
                    sage: TestSuite(c).run()
        """
    @overload
    def pp(self) -> Any:
        """Spin.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 480)

        Pretty print ``self`` as a column.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: b = C([1,1,-1])
            sage: b.pp()
            +
            +
            -"""
    @overload
    def pp(self) -> Any:
        """Spin.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 480)

        Pretty print ``self`` as a column.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: b = C([1,1,-1])
            sage: b.pp()
            +
            +
            -"""
    @overload
    def signature(self) -> Any:
        """Spin.signature(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 415)

        Return the signature of ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: C([1,1,1]).signature()
            '+++'
            sage: C([1,1,-1]).signature()
            '++-'"""
    @overload
    def signature(self) -> Any:
        """Spin.signature(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 415)

        Return the signature of ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: C([1,1,1]).signature()
            '+++'
            sage: C([1,1,-1]).signature()
            '++-'"""
    @overload
    def signature(self) -> Any:
        """Spin.signature(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 415)

        Return the signature of ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: C([1,1,1]).signature()
            '+++'
            sage: C([1,1,-1]).signature()
            '++-'"""
    @overload
    def weight(self) -> Any:
        """Spin.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 514)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Spins(['B',3])]
            [(1/2, 1/2, 1/2), (1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2), (-1/2, 1/2, 1/2),
             (1/2, -1/2, -1/2), (-1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2), (-1/2, -1/2, -1/2)]"""
    @overload
    def weight(self) -> Any:
        """Spin.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 514)

        Return the weight of ``self``.

        EXAMPLES::

            sage: [v.weight() for v in crystals.Spins(['B',3])]
            [(1/2, 1/2, 1/2), (1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2), (-1/2, 1/2, 1/2),
             (1/2, -1/2, -1/2), (-1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2), (-1/2, -1/2, -1/2)]"""
    def __hash__(self) -> Any:
        """Spin.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 323)

        Return the hash of ``self``.

        TESTS::

            sage: C = crystals.Spins(['B',3])
            sage: len(set(C)) == len(set([hash(x) for x in C]))
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Spin.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 338)

        Used to pickle ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: a = C([1,-1,1])
            sage: a.__reduce__()
            (The crystal of spins for type ['B', 3], ((1, -1, 1),))"""
    @overload
    def __reduce__(self) -> Any:
        """Spin.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 338)

        Used to pickle ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: a = C([1,-1,1])
            sage: a.__reduce__()
            (The crystal of spins for type ['B', 3], ((1, -1, 1),))"""

class Spin_crystal_type_B_element(Spin):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 533)

        Type B spin representation crystal element
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def e(self, inti) -> Spin:
        """Spin_crystal_type_B_element.e(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 537)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, +++], [None, ++-, None], [+-+, None, None],
             [None, None, +-+], [+--, None, -++], [None, -+-, None], [None, None, --+]]"""
    @overload
    def e(self, i) -> Any:
        """Spin_crystal_type_B_element.e(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 537)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, +++], [None, ++-, None], [+-+, None, None],
             [None, None, +-+], [+--, None, -++], [None, -+-, None], [None, None, --+]]"""
    def epsilon(self, inti) -> int:
        """Spin_crystal_type_B_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 603)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].epsilon(i) for i in range(1,4)] for m in range(8)]
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0],
             [0, 0, 1], [1, 0, 1], [0, 1, 0], [0, 0, 1]]"""
    @overload
    def f(self, inti) -> Spin:
        """Spin_crystal_type_B_element.f(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 570)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, ++-], [None, +-+, None], [-++, None, +--], [None, None, -+-],
             [-+-, None, None], [None, --+, None], [None, None, ---], [None, None, None]]"""
    @overload
    def f(self, i) -> Any:
        """Spin_crystal_type_B_element.f(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 570)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, ++-], [None, +-+, None], [-++, None, +--], [None, None, -+-],
             [-+-, None, None], [None, --+, None], [None, None, ---], [None, None, None]]"""
    def phi(self, inti) -> int:
        """Spin_crystal_type_B_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 620)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Spins(['B',3])
            sage: [[C[m].phi(i) for i in range(1,4)] for m in range(8)]
            [[0, 0, 1], [0, 1, 0], [1, 0, 1], [0, 0, 1],
             [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]"""

class Spin_crystal_type_D_element(Spin):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 637)

        Type D spin representation crystal element
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def e(self, inti) -> Spin:
        """Spin_crystal_type_D_element.e(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 641)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, None], [None, ++--, None], [+-+-, None, None],
             [None, None, +-+-], [+--+, None, -++-], [None, -+-+, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, +++-], [None, ++-+, None], [+-++, None, None],
             [None, None, None], [+---, None, None], [None, -+--, None], [None, None, --+-]]"""
    @overload
    def e(self, i) -> Any:
        """Spin_crystal_type_D_element.e(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 641)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, None], [None, ++--, None], [+-+-, None, None],
             [None, None, +-+-], [+--+, None, -++-], [None, -+-+, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, +++-], [None, ++-+, None], [+-++, None, None],
             [None, None, None], [+---, None, None], [None, -+--, None], [None, None, --+-]]"""
    @overload
    def e(self, i) -> Any:
        """Spin_crystal_type_D_element.e(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 641)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, None], [None, ++--, None], [+-+-, None, None],
             [None, None, +-+-], [+--+, None, -++-], [None, -+-+, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].e(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, None, +++-], [None, ++-+, None], [+-++, None, None],
             [None, None, None], [+---, None, None], [None, -+--, None], [None, None, --+-]]"""
    def epsilon(self, inti) -> int:
        """Spin_crystal_type_D_element.epsilon(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 723)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.SpinsMinus(['D',4])
            sage: [[C[m].epsilon(i) for i in C.index_set()] for m in range(8)]
            [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],
             [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]]"""
    @overload
    def f(self, inti) -> Spin:
        """Spin_crystal_type_D_element.f(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 682)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, +-+-, None], [-++-, None, +--+], [None, None, -+-+],
             [-+-+, None, None], [None, --++, None], [None, None, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, ++-+], [None, +-++, None], [-+++, None, None], [None, None, None],
             [-+--, None, None], [None, --+-, None], [None, None, ---+], [None, None, None]]"""
    @overload
    def f(self, i) -> Any:
        """Spin_crystal_type_D_element.f(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 682)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, +-+-, None], [-++-, None, +--+], [None, None, -+-+],
             [-+-+, None, None], [None, --++, None], [None, None, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, ++-+], [None, +-++, None], [-+++, None, None], [None, None, None],
             [-+--, None, None], [None, --+-, None], [None, None, ---+], [None, None, None]]"""
    @overload
    def f(self, i) -> Any:
        """Spin_crystal_type_D_element.f(self, int i) -> Spin

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 682)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: D = crystals.SpinsPlus(['D',4])
            sage: [[D.list()[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, None], [None, +-+-, None], [-++-, None, +--+], [None, None, -+-+],
             [-+-+, None, None], [None, --++, None], [None, None, None], [None, None, None]]

        ::

            sage: E = crystals.SpinsMinus(['D',4])
            sage: [[E[m].f(i) for i in range(1,4)] for m in range(8)]
            [[None, None, ++-+], [None, +-++, None], [-+++, None, None], [None, None, None],
             [-+--, None, None], [None, --+-, None], [None, None, ---+], [None, None, None]]"""
    def phi(self, inti) -> int:
        """Spin_crystal_type_D_element.phi(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/spins.pyx (starting at line 740)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.SpinsPlus(['D',4])
            sage: [[C[m].phi(i) for i in C.index_set()] for m in range(8)]
            [[0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0],
             [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]"""
