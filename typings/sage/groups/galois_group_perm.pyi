from sage.groups.galois_group import _GaloisMixin, _SubGaloisMixin
from sage.groups.perm_gps.permgroup import PermutationGroup_generic as PermutationGroup_generic, PermutationGroup_subgroup as PermutationGroup_subgroup
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.category_object import normalize_names as normalize_names

class GaloisGroup_perm(_GaloisMixin, PermutationGroup_generic):
    """
    The group of automorphisms of a Galois closure of a given field.

    INPUT:

    - ``field`` -- a field, separable over its base

    - ``names`` -- string or tuple of length 1, giving a variable name for
      the splitting field

    - ``gc_numbering`` -- boolean, whether to express permutations in terms of
      the roots of the defining polynomial of the splitting field (versus the
      defining polynomial of the original extension); the default value may
      vary based on the type of field
    """
    @abstract_method
    def transitive_number(self, algorithm=None, recompute: bool = False) -> None:
        """
        Return the transitive number (as in the GAP and Magma databases of transitive groups)
        for the action on the roots of the defining polynomial of the top field.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^3 + 2*x + 2)                                    # needs sage.rings.number_field
            sage: G = K.galois_group()                                                  # needs sage.rings.number_field
            sage: G.transitive_number()                                                 # needs sage.rings.number_field
            2
        """
    def __init__(self, field, algorithm=None, names=None, gc_numbering: bool = False) -> None:
        """
        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^3 + 2*x + 2)                                    # needs sage.rings.number_field
            sage: G = K.galois_group()                                                  # needs sage.rings.number_field
            sage: TestSuite(G).run()                                                    # needs sage.rings.number_field
        """
    def ngens(self) -> int:
        """
        Return the number of generators of this Galois group.

        EXAMPLES::

            sage: QuadraticField(-23, 'a').galois_group().ngens()                       # needs sage.rings.number_field
            1
        """

class GaloisSubgroup_perm(PermutationGroup_subgroup, _SubGaloisMixin):
    """
    Subgroups of Galois groups (implemented as permutation groups), specified
    by giving a list of generators.

    Unlike ambient Galois groups, where we use a lazy ``_gens`` attribute in order
    to enable creation without determining a list of generators,
    we require that generators for a subgroup be specified during initialization,
    as specified in the ``__init__`` method of permutation subgroups.
    """
