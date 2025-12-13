import sage.structure.sage_object
from sage.misc.latex import latex as latex
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar

class RiggedPartition(sage.structure.sage_object.SageObject):
    """RiggedPartition(shape=None, rigging_list=None, vacancy_nums=None)

    File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 45)

    The RiggedPartition class which is the data structure of a rigged (i.e.
    marked or decorated) Young diagram of a partition.

    Note that this class as a stand-alone object does not make sense since the
    vacancy numbers are calculated using the entire rigged configuration. For
    more, see :class:`RiggedConfigurations`.

    EXAMPLES::

        sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
        sage: RP = RC(partition_list=[[2],[2,2],[2,1],[2]])[2]
        sage: RP
         0[ ][ ]0
        -1[ ]-1
        <BLANKLINE>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    rigging: rigging
    vacancy_numbers: vacancy_numbers
    def __init__(self, shape=..., rigging_list=..., vacancy_nums=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 64)

                Initialize by the rigged partition.

                Note that this only performs checks to see that the sizes match up.

                INPUT:

                - ``shape`` -- (default: ``None``) the shape
                - ``rigging_list`` -- (default: ``None``) the riggings
                - ``vacancy_nums`` -- (default: ``None``) the vacancy numbers

                TESTS::

                    sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
                    sage: RiggedPartition()
                    (/)
                    <BLANKLINE>
                    sage: RP = RiggedPartition([2,1], [0,0], [1, 0])
                    sage: RP
                    1[ ][ ]0
                    0[ ]0
                    <BLANKLINE>
                    sage: TestSuite(RP).run()
        """
    def get_num_cells_to_column(self, intend_column, t=...) -> Any:
        """RiggedPartition.get_num_cells_to_column(self, int end_column, t=1)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 357)

        Get the number of cells in all columns before the ``end_column``.

        INPUT:

        - ``end_column`` -- the index of the column to end at

        - ``t`` -- the scaling factor

        OUTPUT: the number of cells

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: RP = RC(partition_list=[[2],[2,2],[2,1],[2]])[2]
            sage: RP.get_num_cells_to_column(1)
            2
            sage: RP.get_num_cells_to_column(2)
            3
            sage: RP.get_num_cells_to_column(3)
            3
            sage: RP.get_num_cells_to_column(3, 2)
            5"""
    def insert_cell(self, intmax_width) -> Any:
        """RiggedPartition.insert_cell(self, int max_width)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 395)

        Insert a cell given at a singular value as long as its less than the
        specified width.

        Note that :meth:`insert_cell` does not update riggings or vacancy
        numbers, but it does prepare the space for them. Returns the width of
        the row we inserted at.

        INPUT:

        - ``max_width`` -- the maximum width (i.e. row length) that we can
          insert the cell at

        OUTPUT: the width of the row we inserted at

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: RP = RC(partition_list=[[2],[2,2],[2,1],[2]])[2]
            sage: RP.insert_cell(2)
            2
            sage: RP
             0[ ][ ][ ]None
            -1[ ]-1
            <BLANKLINE>"""
    def remove_cell(self, row, intnum_cells=...) -> Any:
        """RiggedPartition.remove_cell(self, row, int num_cells=1)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 445)

        Removes a cell at the specified ``row``.

        Note that :meth:`remove_cell` does not set/update the vacancy numbers
        or the riggings, but guarantees that the location has been allocated
        in the returned index.

        INPUT:

        - ``row`` -- the row to remove the cell from

        - ``num_cells`` -- (default: 1) the number of cells to remove

        OUTPUT:

        - The location of the newly constructed row or ``None`` if unable to
          remove row or if deleted a row.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: RP = RC(partition_list=[[2],[2,2],[2,1],[2]])[2]
            sage: RP.remove_cell(0)
            0
            sage: RP
             None[ ]None
            -1[ ]-1
            <BLANKLINE>"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        """RiggedPartition.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 322)

        TESTS::

            sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
            sage: nu = RiggedPartition([3,2,1])
            sage: nu[2]
            1"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """RiggedPartition.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 279)

        TESTS::

            sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
            sage: nu = RiggedPartition()
            sage: h = hash(nu)
            sage: _ = nu.insert_cell(2)
            sage: h == hash(nu)
            False"""
    def __iter__(self) -> Any:
        """RiggedPartition.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 333)

        TESTS::

            sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
            sage: nu = RiggedPartition([3,2,1])
            sage: list(nu)
            [3, 2, 1]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """RiggedPartition.__len__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 308)

        TESTS::

            sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
            sage: nu = RiggedPartition()
            sage: len(nu)
            0
            sage: nu = RiggedPartition([3,2,2,1])
            sage: len(nu)
            4"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """RiggedPartition.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 344)

        TESTS::

            sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
            sage: nu = RiggedPartition([3,2,1])
            sage: loads(dumps(nu)) == nu
            True"""

class RiggedPartitionTypeB(RiggedPartition):
    """RiggedPartitionTypeB(arg0, arg1=None, arg2=None)

    File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 527)

    Rigged partitions for type `B_n^{(1)}` which has special printing rules
    which comes from the fact that the `n`-th partition can have columns of
    width `\\frac{1}{2}`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, arg0, arg1=..., arg2=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/rigged_configurations/rigged_partition.pyx (starting at line 533)

                Initialize ``self``.

                EXAMPLES::

                    sage: RP = sage.combinat.rigged_configurations.rigged_partition.RiggedPartition([2,1], [0,0], [1, 0])
                    sage: B = sage.combinat.rigged_configurations.rigged_partition.RiggedPartitionTypeB(RP); B
                    1[][]0
                    0[]0
                    <BLANKLINE>
                    sage: TestSuite(B).run()
        """
