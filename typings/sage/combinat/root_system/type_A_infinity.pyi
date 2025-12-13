from .cartan_type import CartanType_simple as CartanType_simple, CartanType_standard as CartanType_standard
from _typeshed import Incomplete
from sage.rings.integer_ring import ZZ as ZZ

class CartanType(CartanType_standard, CartanType_simple):
    """
    The Cartan type `A_{\\infty}`.

    We use ``NN`` and ``ZZ`` to explicitly differentiate between the
    `A_{+\\infty}` and `A_{\\infty}` root systems, respectively.
    While ``oo`` is the same as ``+Infinity`` in Sage, it is used as
    an alias for ``ZZ``.
    """
    letter: str
    n: Incomplete
    def __init__(self, index_set) -> None:
        """
        EXAMPLES::

            sage: CartanType(['A',oo]) is CartanType(['A', ZZ])
            True
            sage: CartanType(['A',oo]) is CartanType(['A', NN])
            False
            sage: ct=CartanType(['A',ZZ])
            sage: ct
            ['A', ZZ]
            sage: ct._repr_(compact = True)
            'A_ZZ'
            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            False
            sage: ct.is_affine()
            False
            sage: ct.is_untwisted_affine()
            False
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            True
            sage: ct.dual()
            ['A', ZZ]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['A', ZZ]).ascii_art())
            ..---O---O---O---O---O---O---O---..
                -3  -2  -1   0   1   2   3
            sage: print(CartanType(['A', NN]).ascii_art())
            O---O---O---O---O---O---O---..
            0   1   2   3   4   5   6
        """
    def dual(self):
        '''
        Simply laced Cartan types are self-dual, so return ``self``.

        EXAMPLES::

            sage: CartanType(["A", NN]).dual()
            [\'A\', NN]
            sage: CartanType(["A", ZZ]).dual()
            [\'A\', ZZ]
        '''
    def is_simply_laced(self):
        """
        Return ``True`` because ``self`` is simply laced.

        EXAMPLES::

            sage: CartanType(['A', NN]).is_simply_laced()
            True
            sage: CartanType(['A', ZZ]).is_simply_laced()
            True
        """
    def is_crystallographic(self):
        """
        Return ``False`` because ``self`` is not crystallographic.

        EXAMPLES::

            sage: CartanType(['A', NN]).is_crystallographic()
            True
            sage: CartanType(['A', ZZ]).is_crystallographic()
            True
        """
    def is_finite(self):
        """
        Return ``True`` because ``self`` is not finite.

        EXAMPLES::

            sage: CartanType(['A', NN]).is_finite()
            False
            sage: CartanType(['A', ZZ]).is_finite()
            False
        """
    def is_affine(self):
        """
        Return ``False`` because ``self`` is not (untwisted) affine.

        EXAMPLES::

            sage: CartanType(['A', NN]).is_affine()
            False
            sage: CartanType(['A', ZZ]).is_affine()
            False
        """
    def is_untwisted_affine(self):
        """
        Return ``False`` because ``self`` is not (untwisted) affine.

        EXAMPLES::

            sage: CartanType(['A', NN]).is_untwisted_affine()
            False
            sage: CartanType(['A', ZZ]).is_untwisted_affine()
            False
        """
    def rank(self):
        """
        Return the rank of ``self`` which for type `X_n` is `n`.

        EXAMPLES::

            sage: CartanType(['A', NN]).rank()
            +Infinity
            sage: CartanType(['A', ZZ]).rank()
            +Infinity

        As this example shows, the rank is slightly ambiguous because the root
        systems of type `['A',NN]` and type `['A',ZZ]` have the same rank.
        Instead, it is better ot use :meth:`index_set` to differentiate between
        these two root systems.
        """
    def type(self):
        """
        Return the type of ``self``.

        EXAMPLES::

            sage: CartanType(['A', NN]).type()
            'A'
            sage: CartanType(['A', ZZ]).type()
            'A'
        """
    def index_set(self):
        """
        Return the index set for the Cartan type ``self``.

        The index set for all standard finite Cartan types is of the form
        `\\{1, \\ldots, n\\}`. (See :mod:`~sage.combinat.root_system.type_I`
        for a slight abuse of this).

        EXAMPLES::

            sage: CartanType(['A', NN]).index_set()
            Non negative integer semiring
            sage: CartanType(['A', ZZ]).index_set()
            Integer Ring
        """
