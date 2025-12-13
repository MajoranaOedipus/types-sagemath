from sage.categories.groups import Groups as Groups
from sage.groups.abelian_gps.dual_abelian_group_element import DualAbelianGroupElement as DualAbelianGroupElement, is_DualAbelianGroupElement as is_DualAbelianGroupElement
from sage.groups.group import AbelianGroup as AbelianGroupBase
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.mrange import mrange as mrange
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_DualAbelianGroup(x):
    '''
    Return ``True`` if `x` is the dual group of an abelian group.

    EXAMPLES::

        sage: from sage.groups.abelian_gps.dual_abelian_group import is_DualAbelianGroup
        sage: F = AbelianGroup(5,[3,5,7,8,9], names=list("abcde"))
        sage: Fd = F.dual_group()
        sage: is_DualAbelianGroup(Fd)
        doctest:warning...
        DeprecationWarning: the function is_DualAbelianGroup is deprecated;
        use \'isinstance(..., DualAbelianGroup_class)\' instead
        See https://github.com/sagemath/sage/issues/37898 for details.
        True
        sage: F = AbelianGroup(3,[1,2,3], names=\'a\')
        sage: Fd = F.dual_group()
        sage: Fd.gens()
        (1, X1, X2)
        sage: F.gens()
        (1, a1, a2)
    '''

class DualAbelianGroup_class(UniqueRepresentation, AbelianGroupBase):
    """
    Dual of abelian group.

    EXAMPLES::

        sage: F = AbelianGroup(5,[3,5,7,8,9], names='abcde')
        sage: F.dual_group()
        Dual of Abelian Group isomorphic to Z/3Z x Z/5Z x Z/7Z x Z/8Z x Z/9Z
        over Cyclotomic Field of order 2520 and degree 576

        sage: F = AbelianGroup(4,[15,7,8,9], names='abcd')
        sage: F.dual_group(base_ring=CC)                                                # needs sage.rings.real_mpfr
        Dual of Abelian Group isomorphic to Z/15Z x Z/7Z x Z/8Z x Z/9Z
        over Complex Field with 53 bits of precision
    """
    Element = DualAbelianGroupElement
    def __init__(self, G, names, base_ring) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: F = AbelianGroup(5,[3,5,7,8,9], names='abcde')
            sage: F.dual_group()
            Dual of Abelian Group isomorphic to Z/3Z x Z/5Z x Z/7Z x Z/8Z x Z/9Z
            over Cyclotomic Field of order 2520 and degree 576
        """
    def group(self):
        '''
        Return the group that ``self`` is the dual of.

        EXAMPLES::

            sage: F = AbelianGroup(3,[5,64,729], names=list("abc"))
            sage: Fd = F.dual_group(base_ring=CC)
            sage: Fd.group() is F
            True
        '''
    def base_ring(self):
        '''
        Return the scalars over which the group is dualized.

        EXAMPLES::

            sage: F = AbelianGroup(3,[5,64,729], names=list("abc"))
            sage: Fd = F.dual_group(base_ring=CC)
            sage: Fd.base_ring()
            Complex Field with 53 bits of precision
        '''
    def random_element(self):
        """
        Return a random element of this dual group.

        EXAMPLES::

            sage: G = AbelianGroup([2,3,9])
            sage: Gd = G.dual_group(base_ring=CC)                                       # needs sage.rings.real_mpfr
            sage: Gd.random_element().parent() is Gd                                    # needs sage.rings.real_mpfr
            True

            sage: # needs sage.rings.real_mpfr
            sage: N = 43^2 - 1
            sage: G = AbelianGroup([N], names='a')
            sage: Gd = G.dual_group(names='A', base_ring=CC)
            sage: a, = G.gens()
            sage: A, = Gd.gens()
            sage: x = a^(N/4); y = a^(N/3); z = a^(N/14)
            sage: found = [False]*4
            sage: while not all(found):
            ....:     X = A*Gd.random_element()
            ....:     found[len([b for b in [x,y,z] if abs(X(b)-1)>10^(-8)])] = True
        """
    def gen(self, i: int = 0):
        """
        The `i`-th generator of the abelian group.

        EXAMPLES::

            sage: F = AbelianGroup(3, [1,2,3], names='a')
            sage: Fd = F.dual_group(names='A')
            sage: Fd.0
            1
            sage: Fd.1
            A1
            sage: Fd.gens_orders()
            (1, 2, 3)
        """
    def gens(self) -> tuple:
        """
        Return the generators for the group.

        OUTPUT: tuple of group elements generating the group

        EXAMPLES::

            sage: F = AbelianGroup([7,11]).dual_group()
            sage: F.gens()
            (X0, X1)
        """
    def ngens(self):
        """
        The number of generators of the dual group.

        EXAMPLES::

            sage: F = AbelianGroup([7]*100)
            sage: Fd = F.dual_group()
            sage: Fd.ngens()
            100
        """
    def gens_orders(self):
        """
        The orders of the generators of the dual group.

        OUTPUT: tuple of integers

        EXAMPLES::

            sage: F = AbelianGroup([5]*1000)
            sage: Fd = F.dual_group()
            sage: invs = Fd.gens_orders(); len(invs)
            1000
        """
    def invariants(self):
        """
        The invariants of the dual group.

        You should use :meth:`gens_orders` instead.

        EXAMPLES::

            sage: F = AbelianGroup([5]*1000)
            sage: Fd = F.dual_group()
            sage: invs = Fd.gens_orders(); len(invs)
            1000
        """
    def __contains__(self, X) -> bool:
        '''
        Implement "in".

        EXAMPLES::

            sage: F = AbelianGroup(5,[2, 3, 5, 7, 8], names=\'abcde\')
            sage: a,b,c,d,e = F.gens()
            sage: Fd = F.dual_group(names=\'ABCDE\')
            sage: A,B,C,D,E = Fd.gens()
            sage: A*B^2*D^7 in Fd
            True
        '''
    def order(self):
        """
        Return the order of this group.

        EXAMPLES::

            sage: G = AbelianGroup([2,3,9])
            sage: Gd = G.dual_group()
            sage: Gd.order()
            54
        """
    def is_commutative(self):
        """
        Return ``True`` since this group is commutative.

        EXAMPLES::

            sage: G = AbelianGroup([2,3,9])
            sage: Gd = G.dual_group()
            sage: Gd.is_commutative()
            True
            sage: Gd.is_abelian()
            True
        """
    @cached_method
    def list(self):
        """
        Return a tuple of all elements of this group.

        EXAMPLES::

            sage: G = AbelianGroup([2,3], names='ab')
            sage: Gd = G.dual_group(names='AB')
            sage: Gd.list()
            (1, B, B^2, A, A*B, A*B^2)
        """
    def __iter__(self):
        """
        Return an iterator over the elements of this group.

        EXAMPLES::

            sage: G = AbelianGroup([2,3], names='ab')
            sage: Gd = G.dual_group(names='AB')
            sage: [X for X in Gd]
            [1, B, B^2, A, A*B, A*B^2]

            sage: # needs sage.rings.real_mpfr
            sage: N = 43^2 - 1
            sage: G = AbelianGroup([N], names='a')
            sage: Gd = G.dual_group(names='A', base_ring=CC)
            sage: a, = G.gens()
            sage: A, = Gd.gens()
            sage: x = a^(N/4)
            sage: y = a^(N/3)
            sage: z = a^(N/14)
            sage: len([X for X in Gd
            ....:      if abs(X(x)-1)>0.01 and abs(X(y)-1)>0.01 and abs(X(z)-1)>0.01])
            880
        """
