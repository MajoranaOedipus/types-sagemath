from sage.combinat.species.species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from sage.combinat.species.structure import SpeciesStructureWrapper as SpeciesStructureWrapper
from sage.rings.rational_field import QQ as QQ

class CombinatorialSpeciesStructure(SpeciesStructureWrapper): ...

class CombinatorialSpecies(GenericCombinatorialSpecies):
    def __init__(self, min=None) -> None:
        """
        EXAMPLES::

            sage: F = CombinatorialSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: loads(dumps(F))
            Combinatorial species

        ::

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            sage: L.define(E+X*L)
            sage: L.generating_series()[0:4]
            [1, 1, 1, 1]
            sage: LL = loads(dumps(L))
            sage: LL.generating_series()[0:4]
            [1, 1, 1, 1]
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: hash(CombinatorialSpecies) #random
            53751280

        ::

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            sage: L.define(E+X*L)
            sage: hash(L) #random
            -826511807095108317
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: A = species.CombinatorialSpecies()
            sage: B = species.CombinatorialSpecies()
            sage: A == B
            False
            sage: X = species.SingletonSpecies()
            sage: A.define(X+A*A)
            sage: B.define(X+B*B)
            sage: A == B
            True

            sage: C = species.CombinatorialSpecies()
            sage: E = species.EmptySetSpecies()
            sage: C.define(E+X*C*C)
            sage: A == C
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: A = species.CombinatorialSpecies()
            sage: B = species.CombinatorialSpecies()
            sage: A != B
            True
            sage: X = species.SingletonSpecies()
            sage: A.define(X+A*A)
            sage: B.define(X+B*B)
            sage: A != B
            False

            sage: C = species.CombinatorialSpecies()
            sage: E = species.EmptySetSpecies()
            sage: C.define(E+X*C*C)
            sage: A != C
            True
        """
    def weight_ring(self):
        """
        EXAMPLES::

            sage: F = species.CombinatorialSpecies()
            sage: F.weight_ring()
            Rational Field

        ::

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            sage: L.define(E+X*L)
            sage: L.weight_ring()
            Rational Field
        """
    def define(self, x) -> None:
        """
        Define ``self`` to be equal to the combinatorial species ``x``.

        This is used to define combinatorial species recursively. All of the
        real work is done by calling the ``.set()`` method for each of the
        series associated to ``self``.

        EXAMPLES: The species of linear orders `L` can be recursively defined
        by `L = 1 + X*L` where 1 represents the empty set species
        and `X` represents the singleton species::

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            sage: L.define(E+X*L)
            sage: L.generating_series()[0:4]
            [1, 1, 1, 1]
            sage: L.structures([1,2,3]).cardinality()
            6
            sage: L.structures([1,2,3]).list()
            [1*(2*(3*{})),
             1*(3*(2*{})),
             2*(1*(3*{})),
             2*(3*(1*{})),
             3*(1*(2*{})),
             3*(2*(1*{}))]

        ::

            sage: L = species.LinearOrderSpecies()
            sage: L.generating_series()[0:4]
            [1, 1, 1, 1]
            sage: L.structures([1,2,3]).cardinality()
            6
            sage: L.structures([1,2,3]).list()
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        TESTS::

            sage: A = CombinatorialSpecies()
            sage: A.define(E+X*A*A)
            sage: A.generating_series()[0:6]
            [1, 1, 2, 5, 14, 42]
            sage: A.generating_series().counts(6)
            [1, 1, 4, 30, 336, 5040]
            sage: len(A.structures([1,2,3,4]).list())
            336
            sage: A.isotype_generating_series()[0:6]
            [1, 1, 2, 5, 14, 42]
            sage: len(A.isotypes([1,2,3,4]).list())
            14

        ::

            sage: A = CombinatorialSpecies(min=1)
            sage: A.define(X+A*A)
            sage: A.generating_series()[0:6]
            [0, 1, 1, 2, 5, 14]
            sage: A.generating_series().counts(6)
            [0, 1, 2, 12, 120, 1680]
            sage: len(A.structures([1,2,3]).list())
            12
            sage: A.isotype_generating_series()[0:6]
            [0, 1, 1, 2, 5, 14]
            sage: len(A.isotypes([1,2,3,4]).list())
            5

        ::

            sage: X2 = X*X
            sage: X5 = X2*X2*X
            sage: A = CombinatorialSpecies(min=1)
            sage: B = CombinatorialSpecies(min=1)
            sage: C = CombinatorialSpecies(min=1)
            sage: A.define(X5+B*B)
            sage: B.define(X5+C*C)
            sage: C.define(X2+C*C+A*A)
            sage: A.generating_series()[0:15]
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 5, 4, 14, 10, 48]
            sage: B.generating_series()[0:15]
            [0, 0, 0, 0, 1, 1, 2, 0, 5, 0, 14, 0, 44, 0, 138]
            sage: C.generating_series()[0:15]
            [0, 0, 1, 0, 1, 0, 2, 0, 5, 0, 15, 0, 44, 2, 142]

        ::

            sage: F = CombinatorialSpecies()
            sage: F.define(E+X+(X*F+X*X*F))
            sage: F.generating_series().counts(10)
            [1, 2, 6, 30, 192, 1560, 15120, 171360, 2217600, 32296320]
            sage: F.generating_series()[0:10]
            [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            sage: F.isotype_generating_series()[0:10]
            [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        Check that :issue:`35071` is fixed::

            sage: X = species.SingletonSpecies()
            sage: E = species.SetSpecies(max=3)
            sage: B = species.CombinatorialSpecies(min=1)
            sage: B.define(X*E(B))
            sage: B.generating_series()
            z + z^2 + 3/2*z^3 + 5/2*z^4 + 9/2*z^5 + 17/2*z^6 + 133/8*z^7 + O(z^8)
        """
