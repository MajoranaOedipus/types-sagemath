from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class LabelledBranching:
    """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 299)

        This class implements complete labelled branchings.

        To each subgroup of `S_n` we can uniquely assign a directed forest
        on `n` vertices, where the
        edges `(i,j)` fulfill `i<j` and some further conditions on the edge labels
        (which we do not want to state).
        This graph is called a complete labelled branching.

        The edges `(i,j)` will be stored in a vector ``father`` with
        ``father_j = -1`` if `j` is a root of a tree, and
        ``father_j = i`` if `i` is the predecessor of `j`, i.e. is an `(i,j)` is an edge.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.get_order()
            3
            sage: L.small_generating_set()
            [(1,2,3)]
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_gen(self, GapElement_Permutationgen) -> Any:
        """LabelledBranching.add_gen(self, GapElement_Permutation gen)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 358)

        Add a further generator to the group and
        update the complete labeled branching.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.add_gen(libgap.eval('(1,2,3)'))"""
    @overload
    def get_order(self) -> Any:
        """LabelledBranching.get_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 437)

        Return the order of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.get_order()
            1
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.get_order()
            3"""
    @overload
    def get_order(self) -> Any:
        """LabelledBranching.get_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 437)

        Return the order of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.get_order()
            1
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.get_order()
            3"""
    @overload
    def get_order(self) -> Any:
        """LabelledBranching.get_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 437)

        Return the order of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.get_order()
            1
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.get_order()
            3"""
    @overload
    def small_generating_set(self) -> Any:
        """LabelledBranching.small_generating_set(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 420)

        Return a small set of generators of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.small_generating_set()
            [()]
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.small_generating_set()
            [(1,2,3)]"""
    @overload
    def small_generating_set(self) -> Any:
        """LabelledBranching.small_generating_set(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 420)

        Return a small set of generators of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.small_generating_set()
            [()]
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.small_generating_set()
            [(1,2,3)]"""
    @overload
    def small_generating_set(self) -> Any:
        """LabelledBranching.small_generating_set(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 420)

        Return a small set of generators of the group stored by ``self``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import LabelledBranching
            sage: L = LabelledBranching(3)
            sage: L.small_generating_set()
            [()]
            sage: L.add_gen(libgap.eval('(1,2,3)'))
            sage: L.small_generating_set()
            [(1,2,3)]"""

class PartitionRefinement_generic:
    """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 455)

        Implement the partition and refinement framework for
        group actions `G \\rtimes S_n` on `X^n` as described in
        :mod:`sage.groups.perm_gps.partn_ref2.refinement_generic`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def get_autom_gens(self) -> Any:
        """PartitionRefinement_generic.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 578)

        Return a list of generators we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_autom_gens()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def get_autom_gens(self) -> Any:
        """PartitionRefinement_generic.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 578)

        Return a list of generators we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_autom_gens()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def get_autom_order_permutation(self) -> Any:
        """PartitionRefinement_generic.get_autom_order_permutation(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 593)

        Return the order of the automorphism group we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_autom_order_permutation()
            1"""
    @overload
    def get_autom_order_permutation(self) -> Any:
        """PartitionRefinement_generic.get_autom_order_permutation(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 593)

        Return the order of the automorphism group we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_autom_order_permutation()
            1"""
    @overload
    def get_canonical_form(self) -> Any:
        """PartitionRefinement_generic.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 548)

        Return the canonical form we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_canonical_form()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def get_canonical_form(self) -> Any:
        """PartitionRefinement_generic.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 548)

        Return the canonical form we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_canonical_form()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def get_transporter(self) -> Any:
        """PartitionRefinement_generic.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 563)

        Return the transporter element we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_transporter()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def get_transporter(self) -> Any:
        """PartitionRefinement_generic.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 563)

        Return the transporter element we have computed.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref2.refinement_generic import PartitionRefinement_generic
            sage: P = PartitionRefinement_generic(5)
            sage: P.get_transporter()
            Traceback (most recent call last):
            ...
            NotImplementedError"""

class _BestValStore:
    """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx (starting at line 260)

        This class implements a dynamic array of integer vectors of length `n`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
