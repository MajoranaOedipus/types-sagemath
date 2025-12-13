from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup_fixed_gens as AdditiveAbelianGroup_fixed_gens
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.rings.integer_ring import ZZ as ZZ

class HomologyGroup_class(AdditiveAbelianGroup_fixed_gens):
    """
    Discrete Abelian group on `n` generators. This class inherits from
    :class:`~sage.groups.additive_abelian.additive_abelian_group.AdditiveAbelianGroup_fixed_gens`;
    see :mod:`sage.groups.additive_abelian.additive_abelian_group` for more
    documentation. The main difference between the classes is in the print
    representation.

    EXAMPLES::

        sage: from sage.homology.homology_group import HomologyGroup
        sage: G = AbelianGroup(5, [5,5,7,8,9]); G                                       # needs sage.groups
        Multiplicative Abelian group isomorphic to C5 x C5 x C7 x C8 x C9
        sage: H = HomologyGroup(5, ZZ, [5,5,7,8,9]); H
        C5 x C5 x C7 x C8 x C9
        sage: G == loads(dumps(G))                                                      # needs sage.groups
        True
        sage: AbelianGroup(4)                                                           # needs sage.groups
        Multiplicative Abelian group isomorphic to Z x Z x Z x Z
        sage: HomologyGroup(4, ZZ)
        Z x Z x Z x Z
        sage: HomologyGroup(100, ZZ)
        Z^100
    """
    def __init__(self, n, invfac) -> None:
        """
        See :func:`HomologyGroup` for full documentation.

        EXAMPLES::

            sage: from sage.homology.homology_group import HomologyGroup
            sage: H = HomologyGroup(5, ZZ, [5,5,7,8,9]); H
            C5 x C5 x C7 x C8 x C9
        """

def HomologyGroup(n, base_ring, invfac=None):
    """
    Abelian group on `n` generators which represents a homology group in a
    fixed degree.

    INPUT:

    - ``n`` -- integer; the number of generators

    - ``base_ring`` -- ring; the base ring over which the homology is computed

    - ``inv_fac`` -- list of integers; the invariant factors -- ignored
      if the base ring is a field

    OUTPUT:

    A class that can represent the homology group in a fixed
    homological degree.

    EXAMPLES::

        sage: from sage.homology.homology_group import HomologyGroup
        sage: G = AbelianGroup(5, [5,5,7,8,9]); G                                       # needs sage.groups
        Multiplicative Abelian group isomorphic to C5 x C5 x C7 x C8 x C9
        sage: H = HomologyGroup(5, ZZ, [5,5,7,8,9]); H
        C5 x C5 x C7 x C8 x C9
        sage: AbelianGroup(4)                                                           # needs sage.groups
        Multiplicative Abelian group isomorphic to Z x Z x Z x Z
        sage: HomologyGroup(4, ZZ)
        Z x Z x Z x Z

        sage: # needs sage.libs.flint (otherwise timeout)
        sage: HomologyGroup(100, ZZ)
        Z^100
    """
