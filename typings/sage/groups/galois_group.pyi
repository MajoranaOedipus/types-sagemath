from sage.groups.abelian_gps.abelian_group import AbelianGroup_class as AbelianGroup_class, AbelianGroup_subgroup as AbelianGroup_subgroup
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ

class _GMixin:
    """
    This class provides some methods for Galois groups to be used for both
    permutation groups and abelian groups, subgroups and full Galois groups.

    It is just intended to provide common functionality between various
    different Galois group classes.
    """
    def splitting_field(self):
        """
        The Galois closure of the top field.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 - x + 1, 'a')
            sage: K.galois_group(names='b').splitting_field()
            Number Field in b with defining polynomial x^6 - 6*x^4 + 9*x^2 + 23
            sage: L = QuadraticField(-23, 'c'); L.galois_group().splitting_field() is L
            True
        """

class _GaloisMixin(_GMixin):
    """
    This class provides methods for Galois groups, allowing concrete instances
    to inherit from both permutation group and abelian group classes.
    """
    def top_field(self):
        """
        Return the larger of the two fields in the extension defining this Galois group.

        Note that this field may not be Galois.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^3 + 2*x + 2)
            sage: L = K.galois_closure('b')
            sage: GK = K.galois_group()
            sage: GK.top_field() is K
            True
            sage: GL = L.galois_group()
            sage: GL.top_field() is L
            True
        """
    def transitive_label(self):
        """
        Return the transitive label for the action of this Galois group on the roots of
        the defining polynomial of the field extension.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^8 - x^5 + x^4 - x^3 + 1)                        # needs sage.rings.number_field
            sage: G = K.galois_group()                                                  # needs sage.rings.number_field
            sage: G.transitive_label()                                                  # needs sage.rings.number_field
            '8T44'
        """
    def is_galois(self):
        """
        Return whether the top field is Galois over its base.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^8 - x^5 + x^4 - x^3 + 1)                        # needs sage.rings.number_field
            sage: G = K.galois_group()                                                  # needs sage.rings.number_field
            sage: from sage.groups.galois_group import GaloisGroup_perm
            sage: GaloisGroup_perm.is_galois(G)                                         # needs sage.rings.number_field
            False
        """

class _SubGaloisMixin(_GMixin):
    """
    This class provides methods for subgroups of Galois groups, allowing concrete instances
    to inherit from both permutation group and abelian group classes.
    """
    def fixed_field(self, name=None, polred=None, threshold=None) -> None:
        """
        Return the fixed field of this subgroup (as a subfield of the Galois closure).

        INPUT:

        - ``name`` -- a variable name for the new field

        - ``polred`` -- whether to optimize the generator of the newly created field
            for a simpler polynomial, using Pari's :pari:`polredbest`;
            defaults to ``True`` when the degree of the fixed field is at most 8

        - ``threshold`` -- positive number; polred only performed if the cost
          is at most this threshold

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(3^12)
            sage: g = k.galois_group()([8])
            sage: k0, embed = g.fixed_field()
            sage: k0.cardinality()
            81
        """

class GaloisGroup_ab(_GaloisMixin, AbelianGroup_class):
    """
    Abelian Galois groups
    """
    def __init__(self, field, generator_orders, algorithm=None, gen_names: str = 'sigma') -> None:
        """
        Initialize this Galois group.

        TESTS::

            sage: TestSuite(GF(9).galois_group()).run()                                 # needs sage.rings.finite_rings
        """
    def is_galois(self):
        """
        Abelian extensions are Galois.

        For compatibility with Galois groups of number fields.

        EXAMPLES::

            sage: GF(9).galois_group().is_galois()                                      # needs sage.rings.finite_rings
            True
        """
    @cached_method
    def permutation_group(self):
        """
        Return a permutation group giving the action on the roots of a defining polynomial.

        This is the regular representation for the abelian group, which is
        not necessarily the smallest degree permutation representation.

        EXAMPLES::

            sage: GF(3^10).galois_group().permutation_group()                           # needs sage.libs.gap sage.rings.finite_rings
            Permutation Group with generators [(1,2,3,4,5,6,7,8,9,10)]
        """
    def transitive_number(self, algorithm=None, recompute: bool = False):
        """
        Return the transitive number for the action on the roots of the defining polynomial.

        For abelian groups, there is only one transitive action up to isomorphism
        (left multiplication of the group on itself), so we identify that action.

        EXAMPLES::

            sage: from sage.groups.galois_group import GaloisGroup_ab
            sage: Gtest = GaloisGroup_ab(field=None, generator_orders=(2,2,4))
            sage: Gtest.transitive_number()                                             # needs sage.libs.gap
            2
        """

class GaloisGroup_cyc(GaloisGroup_ab):
    """
    Cyclic Galois groups
    """
    def transitive_number(self, algorithm=None, recompute: bool = False):
        """
        Return the transitive number for the action on the roots of the defining polynomial.

        EXAMPLES::

            sage: GF(2^8).galois_group().transitive_number()                            # needs sage.rings.finite_rings
            1
            sage: GF(3^32).galois_group().transitive_number()                           # needs sage.rings.finite_rings
            33
            sage: GF(2^60).galois_group().transitive_number()                           # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            NotImplementedError: transitive database only computed up to degree 47
        """
    def signature(self):
        """
        Return 1 if contained in the alternating group, -1 otherwise.

        EXAMPLES::

            sage: GF(3^2).galois_group().signature()                                    # needs sage.rings.finite_rings
            -1
            sage: GF(3^3).galois_group().signature()                                    # needs sage.rings.finite_rings
            1
        """

class GaloisSubgroup_ab(AbelianGroup_subgroup, _SubGaloisMixin):
    """
    Subgroups of abelian Galois groups.
    """
