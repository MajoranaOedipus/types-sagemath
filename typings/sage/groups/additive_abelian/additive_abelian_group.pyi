from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.modules.fg_pid.fgp_element import FGP_Element as FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class as FGP_Module_class
from sage.rings.integer_ring import ZZ as ZZ

def AdditiveAbelianGroup(invs, remember_generators: bool = True):
    '''
    Construct a finitely-generated additive abelian group.

    INPUT:

    - ``invs`` -- list of integers; the invariants.
      These should all be greater than or equal to zero.

    - ``remember_generators`` -- boolean (default: ``True``); whether or not
      to fix a set of generators (corresponding to the given invariants, which
      need not be in Smith form)

    OUTPUT: the abelian group `\\bigoplus_i \\ZZ / n_i \\ZZ`, where `n_i` are the
    invariants

    EXAMPLES::

        sage: AdditiveAbelianGroup([0, 2, 4])
        Additive abelian group isomorphic to Z + Z/2 + Z/4

    An example of the ``remember_generators`` switch::

        sage: G = AdditiveAbelianGroup([0, 2, 3]); G
        Additive abelian group isomorphic to Z + Z/2 + Z/3
        sage: G.gens()
        ((1, 0, 0), (0, 1, 0), (0, 0, 1))

        sage: H = AdditiveAbelianGroup([0, 2, 3], remember_generators = False); H
        Additive abelian group isomorphic to Z/6 + Z
        sage: H.gens()
        ((0, 1, 1), (1, 0, 0))

    There are several ways to create elements of an additive abelian group.
    Realize that there are two sets of generators:  the "obvious" ones composed
    of zeros and ones, one for each invariant given to construct the group, the
    other being a set of minimal generators.  Which set is the default varies
    with the use of the ``remember_generators`` switch.

    First with "obvious" generators.  Note that a raw list will use the
    minimal generators and a vector (a module element) will use the generators
    that pair up naturally with the invariants.  We create the same element
    repeatedly. ::

        sage: H = AdditiveAbelianGroup([3,2,0], remember_generators=True)
        sage: H.gens()
        ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        sage: [H.0, H.1, H.2]
        [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        sage: p = H.0+H.1+6*H.2; p
        (1, 1, 6)

        sage: H.smith_form_gens()
        ((2, 1, 0), (0, 0, 1))
        sage: q = H.linear_combination_of_smith_form_gens([5,6]); q
        (1, 1, 6)
        sage: p == q
        True

        sage: r = H(vector([1,1,6])); r
        (1, 1, 6)
        sage: p == r
        True

        sage: s = H(p)
        sage: p == s
        True

    Again, but now where the generators are the minimal set.  Coercing a
    list or a vector works as before, but the default generators are different. ::

        sage: G = AdditiveAbelianGroup([3,2,0], remember_generators=False)
        sage: G.gens()
        ((2, 1, 0), (0, 0, 1))
        sage: [G.0, G.1]
        [(2, 1, 0), (0, 0, 1)]
        sage: p = 5*G.0+6*G.1; p
        (1, 1, 6)

        sage: H.smith_form_gens()
        ((2, 1, 0), (0, 0, 1))
        sage: q = G.linear_combination_of_smith_form_gens([5,6]); q
        (1, 1, 6)
        sage: p == q
        True

        sage: r = G(vector([1,1,6])); r
        (1, 1, 6)
        sage: p == r
        True

        sage: s = H(p)
        sage: p == s
        True
    '''
def cover_and_relations_from_invariants(invs):
    """
    A utility function to construct modules required to initialize the super class.

    Given a list of integers, this routine constructs the obvious pair of
    free modules such that the quotient of the two free modules over `\\ZZ`
    is naturally isomorphic to the corresponding product of cyclic modules
    (and hence isomorphic to a direct sum of cyclic groups).

    EXAMPLES::

        sage: from sage.groups.additive_abelian.additive_abelian_group import cover_and_relations_from_invariants as cr
        sage: cr([0,2,3])
        (Ambient free module of rank 3 over the principal ideal domain Integer Ring, Free module of degree 3 and rank 2 over Integer Ring
        Echelon basis matrix:
        [0 2 0]
        [0 0 3])
    """

class AdditiveAbelianGroupElement(FGP_Element):
    """
    An element of an :class:`AdditiveAbelianGroup_class`.
    """

class AdditiveAbelianGroup_class(FGP_Module_class):
    """
    An additive abelian group, implemented using the `\\ZZ`-module machinery.

    INPUT:

    - ``cover`` -- the covering group as `\\ZZ`-module

    - ``relations`` -- the relations as submodule of ``cover``
    """
    Element = AdditiveAbelianGroupElement
    def __init__(self, cover, relations) -> None:
        """
        EXAMPLES::

            sage: G = AdditiveAbelianGroup([0]); G # indirect doctest
            Additive abelian group isomorphic to Z
            sage: G == loads(dumps(G))
            True
            sage: G.category()
            Category of modules over Integer Ring
            sage: G in CommutativeAdditiveGroups()
            True
        """
    def short_name(self):
        """
        Return a name for the isomorphism class of this group.

        EXAMPLES::

            sage: AdditiveAbelianGroup([0, 2,4]).short_name()
            'Z + Z/2 + Z/4'
            sage: AdditiveAbelianGroup([0, 2, 3]).short_name()
            'Z + Z/2 + Z/3'
        """
    def order(self):
        """
        Return the order of this group (integer or infinity).

        EXAMPLES::

            sage: AdditiveAbelianGroup([2,4]).order()
            8
            sage: AdditiveAbelianGroup([0, 2,4]).order()
            +Infinity
            sage: AdditiveAbelianGroup([]).order()
            1
        """
    def exponent(self):
        """
        Return the exponent of this group (the smallest positive integer `N`
        such that `Nx = 0` for all `x` in the group). If there is no such
        integer, return 0.

        EXAMPLES::

            sage: AdditiveAbelianGroup([2,4]).exponent()
            4
            sage: AdditiveAbelianGroup([0, 2,4]).exponent()
            0
            sage: AdditiveAbelianGroup([]).exponent()
            1
        """
    def is_multiplicative(self):
        """
        Return ``False`` since this is an additive group.

        EXAMPLES::

            sage: AdditiveAbelianGroup([0]).is_multiplicative()
            False
        """
    def is_cyclic(self):
        """
        Return ``True`` if the group is cyclic.

        EXAMPLES:

        With no common factors between the orders of the generators,
        the group will be cyclic. ::

            sage: G = AdditiveAbelianGroup([6, 7, 55])
            sage: G.is_cyclic()
            True

        Repeating primes in the orders will create a non-cyclic group. ::

            sage: G = AdditiveAbelianGroup([6, 15, 21, 33])
            sage: G.is_cyclic()
            False

        A trivial group is trivially cyclic. ::

            sage: T = AdditiveAbelianGroup([1])
            sage: T.is_cyclic()
            True
        """

class AdditiveAbelianGroup_fixed_gens(AdditiveAbelianGroup_class):
    """
    A variant which fixes a set of generators, which need not be in Smith form
    (or indeed independent).
    """
    def __init__(self, cover, rels, gens) -> None:
        """
        Standard initialisation function.

        EXAMPLES::

            sage: AdditiveAbelianGroup([3]) # indirect doctest
            Additive abelian group isomorphic to Z/3
        """
    def gens(self) -> tuple:
        """
        Return the specified generators for ``self`` (as a tuple). Compare
        ``self.smithform_gens()``.

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([2,3])
            sage: G.gens()
            ((1, 0), (0, 1))
            sage: G.smith_form_gens()
            ((1, 2),)
        """
    def identity(self):
        """
        Return the identity (zero) element of this group.

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([2, 3])
            sage: G.identity()
            (0, 0)
        """
    def permutation_group(self):
        """
        Return the permutation group attached to this group.

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([2, 3])
            sage: G.permutation_group()                                                 # needs sage.groups
            Permutation Group with generators [(1,2), (3,4,5)]

        TESTS:

        Check that :issue:`25692` is fixed::

            sage: G = AdditiveAbelianGroup([0])
            sage: G.permutation_group()
            Traceback (most recent call last):
            ...
            TypeError: Additive Abelian group must be finite
        """
