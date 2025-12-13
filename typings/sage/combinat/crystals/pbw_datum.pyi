import _cython_3_2_1
from sage.combinat.root_system.braid_move_calculator import BraidMoveCalculator as BraidMoveCalculator
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_method as cached_method
from typing import Any, overload

__pyx_capi__: dict
compute_new_lusztig_datum: _cython_3_2_1.cython_function_or_method
enhance_braid_move_chain: _cython_3_2_1.cython_function_or_method
tropical_plucker_relation: _cython_3_2_1.cython_function_or_method

class PBWData:
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 186)

        Helper class for the set of PBW data.
    """
    def __init__(self, cartan_type) -> Any:
        '''PBWData.__init__(self, cartan_type)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 190)

        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData
            sage: P = PBWData(["A",2])
            sage: TestSuite(P).run(skip=\'_test_pickling\')'''
    def convert_to_new_long_word(self, pbw_datum, new_long_word) -> Any:
        '''PBWData.convert_to_new_long_word(self, pbw_datum, new_long_word)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 206)

        Convert the PBW datum ``pbw_datum`` from its long word to
        ``new_long_word``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: datum = PBWDatum(P, (1,2,1), (1,0,1))
            sage: new_datum = P.convert_to_new_long_word(datum,(2,1,2))
            sage: new_datum
            PBW Datum element of type [\'A\', 2] with long word (2, 1, 2)
             and Lusztig datum (0, 1, 0)
            sage: new_datum.long_word
            (2, 1, 2)
            sage: new_datum.lusztig_datum
            (0, 1, 0)'''

class PBWDatum:
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 34)

        Helper class which represents a PBW datum.
    """
    def __init__(self, parent, long_word, lusztig_datum) -> Any:
        '''PBWDatum.__init__(self, parent, long_word, lusztig_datum)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 38)

        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L = PBWDatum(P, (1,2,1), (1,4,7))
            sage: TestSuite(L).run(skip=\'_test_pickling\')'''
    def convert_to_long_word_with_first_letter(self, i) -> Any:
        '''PBWDatum.convert_to_long_word_with_first_letter(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 110)

        Return a new PBWDatum equivalent to ``self``
        whose long word begins with ``i``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A3")
            sage: datum = PBWDatum(P, (1,2,1,3,2,1), (1,0,1,4,2,3))
            sage: datum.convert_to_long_word_with_first_letter(1)
            PBW Datum element of type [\'A\', 3] with long word (1, 2, 3, 1, 2, 1)
             and Lusztig datum (1, 0, 4, 1, 2, 3)
            sage: datum.convert_to_long_word_with_first_letter(2)
            PBW Datum element of type [\'A\', 3] with long word (2, 1, 2, 3, 2, 1)
             and Lusztig datum (0, 1, 0, 4, 2, 3)
            sage: datum.convert_to_long_word_with_first_letter(3)
            PBW Datum element of type [\'A\', 3] with long word (3, 1, 2, 3, 1, 2)
             and Lusztig datum (8, 1, 0, 4, 1, 2)'''
    def convert_to_new_long_word(self, new_long_word) -> Any:
        '''PBWDatum.convert_to_new_long_word(self, new_long_word)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 132)

        Return a new PBWDatum equivalent to ``self``
        whose long word is ``new_long_word``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: datum = PBWDatum(P, (1,2,1), (1,0,1))
            sage: new_datum = datum.convert_to_new_long_word((2,1,2))
            sage: new_datum.long_word
            (2, 1, 2)
            sage: new_datum.lusztig_datum
            (0, 1, 0)'''
    @overload
    def is_equivalent_to(self, other_pbw_datum) -> Any:
        '''PBWDatum.is_equivalent_to(self, other_pbw_datum)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 89)

        Return whether ``self`` is equivalent to ``other_pbw_datum``.
        modulo the tropical Plücker relations.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L1 = PBWDatum(P, (1,2,1), (1,0,1))
            sage: L2 = PBWDatum(P, (2,1,2), (0,1,0))
            sage: L1.is_equivalent_to(L2)
            True
            sage: L1 == L2
            False'''
    @overload
    def is_equivalent_to(self, L2) -> Any:
        '''PBWDatum.is_equivalent_to(self, other_pbw_datum)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 89)

        Return whether ``self`` is equivalent to ``other_pbw_datum``.
        modulo the tropical Plücker relations.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L1 = PBWDatum(P, (1,2,1), (1,0,1))
            sage: L2 = PBWDatum(P, (2,1,2), (0,1,0))
            sage: L1.is_equivalent_to(L2)
            True
            sage: L1 == L2
            False'''
    @overload
    def star(self) -> Any:
        '''PBWDatum.star(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 167)

        Return the starred version of ``self``, i.e.,
        with reversed ``long_word`` and ``lusztig_datum``

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L1 = PBWDatum(P, (1,2,1), (1,2,3))
            sage: L1.star() == PBWDatum(P, (2,1,2), (3,2,1))
            True'''
    @overload
    def star(self) -> Any:
        '''PBWDatum.star(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 167)

        Return the starred version of ``self``, i.e.,
        with reversed ``long_word`` and ``lusztig_datum``

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L1 = PBWDatum(P, (1,2,1), (1,2,3))
            sage: L1.star() == PBWDatum(P, (2,1,2), (3,2,1))
            True'''
    @overload
    def weight(self) -> Any:
        '''PBWDatum.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 150)

        Return the weight of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L = PBWDatum(P, (1,2,1), (1,1,1))
            sage: L.weight()
            -2*alpha[1] - 2*alpha[2]'''
    @overload
    def weight(self) -> Any:
        '''PBWDatum.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 150)

        Return the weight of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L = PBWDatum(P, (1,2,1), (1,1,1))
            sage: L.weight()
            -2*alpha[1] - 2*alpha[2]'''
    def __eq__(self, other_PBWDatum) -> Any:
        '''PBWDatum.__eq__(self, other_PBWDatum)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/pbw_datum.pyx (starting at line 72)

        Check equality.

        EXAMPLES::

            sage: from sage.combinat.crystals.pbw_datum import PBWData, PBWDatum
            sage: P = PBWData("A2")
            sage: L1 = PBWDatum(P, (1,2,1), (1,4,7))
            sage: L2 = PBWDatum(P, (1,2,1), (1,4,7))
            sage: L1 == L2
            True'''
