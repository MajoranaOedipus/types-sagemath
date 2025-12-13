from .cartan_type import CartanType_simple as CartanType_simple, CartanType_standard_finite as CartanType_standard_finite

class CartanType(CartanType_standard_finite, CartanType_simple):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['I',5])
            sage: ct
            ['I', 5]
            sage: ct._repr_(compact = True)
            'I5'
            sage: ct.rank()
            2
            sage: ct.index_set()
            (1, 2)

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_crystallographic()
            False
            sage: ct.is_simply_laced()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def rank(self):
        """
        Type `I_2(p)` is of rank 2.

        EXAMPLES::

            sage: CartanType(['I', 5]).rank()
            2
        """
    def index_set(self):
        """
        Type `I_2(p)` is indexed by `\\{1,2\\}`.

        EXAMPLES::

            sage: CartanType(['I', 5]).index_set()
            (1, 2)
        """
    def coxeter_diagram(self):
        """
        Return the Coxeter matrix for this type.

        EXAMPLES::

            sage: ct = CartanType(['I', 4])
            sage: ct.coxeter_diagram()                                                  # needs sage.graphs
            Graph on 2 vertices
            sage: ct.coxeter_diagram().edges(sort=True)                                 # needs sage.graphs
            [(1, 2, 4)]
            sage: ct.coxeter_matrix()                                                   # needs sage.graphs
            [1 4]
            [4 1]
        """
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['I',3]).coxeter_number()
            3
            sage: CartanType(['I',12]).coxeter_number()
            12
        """
