from _typeshed import Incomplete
from sage.arith.misc import factorial as factorial
from sage.categories.fields import Fields as Fields
from sage.categories.graded_hopf_algebras import GradedHopfAlgebras as GradedHopfAlgebras
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.ncsym.bases import NCSymBasis_abstract as NCSymBasis_abstract, NCSymDualBases as NCSymDualBases
from sage.combinat.partition import Partition as Partition
from sage.combinat.set_partition import SetPartitions as SetPartitions
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.combinat.subset import Subsets as Subsets
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SymmetricFunctionsNonCommutingVariablesDual(UniqueRepresentation, Parent):
    """
    The Hopf dual to the symmetric functions in non-commuting variables.

    See Section 2.3 of [BZ05]_ for a study.
    """
    to_symmetric_function: Incomplete
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: NCSymD1 = SymmetricFunctionsNonCommutingVariablesDual(FiniteField(23))
            sage: NCSymD2 = SymmetricFunctionsNonCommutingVariablesDual(Integers(23))
            sage: TestSuite(SymmetricFunctionsNonCommutingVariables(QQ).dual()).run()
        """
    def a_realization(self):
        """
        Return the realization of the `\\mathbf{w}` basis of ``self``.

        EXAMPLES::

            sage: SymmetricFunctionsNonCommutingVariables(QQ).dual().a_realization()
            Dual symmetric functions in non-commuting variables over the Rational Field in the w basis
        """
    def dual(self):
        """
        Return the dual Hopf algebra of the dual symmetric functions in
        non-commuting variables.

        EXAMPLES::

            sage: NCSymD = SymmetricFunctionsNonCommutingVariables(QQ).dual()
            sage: NCSymD.dual()
            Symmetric functions in non-commuting variables over the Rational Field
        """
    class w(NCSymBasis_abstract):
        """
        The dual Hopf algebra of symmetric functions in non-commuting variables
        in the `\\mathbf{w}` basis.

        EXAMPLES::

            sage: NCSymD = SymmetricFunctionsNonCommutingVariables(QQ).dual()
            sage: w = NCSymD.w()

        We have the embedding `\\chi^*` of `Sym` into `NCSym^*` available as
        a coercion::

            sage: h = SymmetricFunctions(QQ).h()
            sage: w(h[2,1])
            w{{1}, {2, 3}} + w{{1, 2}, {3}} + w{{1, 3}, {2}}

        Similarly we can pull back when we are in the image of `\\chi^*`::

            sage: elt = 3*(w[[1],[2,3]] + w[[1,2],[3]] + w[[1,3],[2]])
            sage: h(elt)
            3*h[2, 1]
        """
        def __init__(self, NCSymD) -> None:
            """
            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: TestSuite(w).run()
            """
        @lazy_attribute
        def to_symmetric_function(self):
            """
            The preimage of `\\chi^*` in the `\\mathbf{w}` basis.

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: w.to_symmetric_function
                Generic morphism:
                  From: Dual symmetric functions in non-commuting variables over the Rational Field in the w basis
                  To:   Symmetric Functions over Rational Field in the homogeneous basis
            """
        def dual_basis(self):
            """
            Return the dual basis to the `\\mathbf{w}` basis.

            The dual basis to the `\\mathbf{w}` basis is the monomial basis
            of the symmetric functions in non-commuting variables.

            OUTPUT: the monomial basis of the symmetric functions in
            non-commuting variables

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: w.dual_basis()
                Symmetric functions in non-commuting variables over the Rational Field in the monomial basis
            """
        def product_on_basis(self, A, B):
            """
            The product on `\\mathbf{w}` basis elements.

            The product on the `\\mathbf{w}` is the dual to the coproduct on the
            `\\mathbf{m}` basis.  On the basis `\\mathbf{w}` it is defined as

            .. MATH::

                \\mathbf{w}_A \\mathbf{w}_B = \\sum_{S \\subseteq [n]}
                \\mathbf{w}_{A\\uparrow_S \\cup B\\uparrow_{S^c}}

            where the sum is over all possible subsets `S` of `[n]` such that
            `|S| = |A|` with a term indexed the union of `A \\uparrow_S` and
            `B \\uparrow_{S^c}`. The notation `A \\uparrow_S` represents the
            unique set partition of the set `S` such that the standardization
            is `A`.  This product is commutative.

            INPUT:

            - ``A``, ``B`` -- set partitions

            OUTPUT: an element of the `\\mathbf{w}` basis

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: A = SetPartition([[1], [2,3]])
                sage: B = SetPartition([[1, 2, 3]])
                sage: w.product_on_basis(A, B)
                w{{1}, {2, 3}, {4, 5, 6}} + w{{1}, {2, 3, 4}, {5, 6}}
                 + w{{1}, {2, 3, 5}, {4, 6}} + w{{1}, {2, 3, 6}, {4, 5}}
                 + w{{1}, {2, 4}, {3, 5, 6}} + w{{1}, {2, 4, 5}, {3, 6}}
                 + w{{1}, {2, 4, 6}, {3, 5}} + w{{1}, {2, 5}, {3, 4, 6}}
                 + w{{1}, {2, 5, 6}, {3, 4}} + w{{1}, {2, 6}, {3, 4, 5}}
                 + w{{1, 2, 3}, {4}, {5, 6}} + w{{1, 2, 4}, {3}, {5, 6}}
                 + w{{1, 2, 5}, {3}, {4, 6}} + w{{1, 2, 6}, {3}, {4, 5}}
                 + w{{1, 3, 4}, {2}, {5, 6}} + w{{1, 3, 5}, {2}, {4, 6}}
                 + w{{1, 3, 6}, {2}, {4, 5}} + w{{1, 4, 5}, {2}, {3, 6}}
                 + w{{1, 4, 6}, {2}, {3, 5}} + w{{1, 5, 6}, {2}, {3, 4}}
                sage: B = SetPartition([[1], [2]])
                sage: w.product_on_basis(A, B)
                3*w{{1}, {2}, {3}, {4, 5}} + 2*w{{1}, {2}, {3, 4}, {5}}
                 + 2*w{{1}, {2}, {3, 5}, {4}} + w{{1}, {2, 3}, {4}, {5}}
                 + w{{1}, {2, 4}, {3}, {5}} + w{{1}, {2, 5}, {3}, {4}}
                sage: w.product_on_basis(A, SetPartition([]))
                w{{1}, {2, 3}}
            """
        def coproduct_on_basis(self, A):
            """
            Return the coproduct of a `\\mathbf{w}` basis element.

            The coproduct on the basis element `\\mathbf{w}_A` is the sum over
            tensor product terms `\\mathbf{w}_B \\otimes \\mathbf{w}_C` where
            `B` is the restriction of `A` to `\\{1,2,\\ldots,k\\}` and `C` is
            the restriction of `A` to `\\{k+1, k+2, \\ldots, n\\}`.

            INPUT:

            - ``A`` -- set partition

            OUTPUT:

            - The coproduct applied to the `\\mathbf{w}` dual symmetric function
              in non-commuting variables indexed by ``A`` expressed in the
              `\\mathbf{w}` basis.

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: w[[1], [2,3]].coproduct()
                w{} # w{{1}, {2, 3}} + w{{1}} # w{{1, 2}}
                 + w{{1}, {2}} # w{{1}} + w{{1}, {2, 3}} # w{}
                sage: w.coproduct_on_basis(SetPartition([]))
                w{} # w{}
            """
        def antipode_on_basis(self, A):
            """
            Return the antipode applied to the basis element indexed by ``A``.

            INPUT:

            - ``A`` -- set partition

            OUTPUT: an element in the basis ``self``

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: w.antipode_on_basis(SetPartition([[1],[2,3]]))
                -3*w{{1}, {2}, {3}} + w{{1, 2}, {3}} + w{{1, 3}, {2}}
                sage: F = w[[1,3],[5],[2,4]].coproduct()
                sage: F.apply_multilinear_morphism(lambda x,y: x.antipode()*y)
                0
            """
        def duality_pairing(self, x, y):
            """
            Compute the pairing between an element of ``self`` and an
            element of the dual.

            INPUT:

            - ``x`` -- an element of the dual of symmetric functions in
              non-commuting variables
            - ``y`` -- an element of the symmetric functions in non-commuting
              variables

            OUTPUT: an element of the base ring of ``self``

            EXAMPLES::

                sage: DNCSym = SymmetricFunctionsNonCommutingVariablesDual(QQ)
                sage: w = DNCSym.w()
                sage: m = w.dual_basis()
                sage: matrix([[w(A).duality_pairing(m(B)) for A in SetPartitions(3)] for B in SetPartitions(3)])
                [1 0 0 0 0]
                [0 1 0 0 0]
                [0 0 1 0 0]
                [0 0 0 1 0]
                [0 0 0 0 1]
                sage: (w[[1,2],[3]] + 3*w[[1,3],[2]]).duality_pairing(2*m[[1,3],[2]] + m[[1,2,3]] + 2*m[[1,2],[3]])
                8
                sage: h = SymmetricFunctionsNonCommutingVariables(QQ).h()
                sage: matrix([[w(A).duality_pairing(h(B)) for A in SetPartitions(3)] for B in SetPartitions(3)])
                [6 2 2 2 1]
                [2 2 1 1 1]
                [2 1 2 1 1]
                [2 1 1 2 1]
                [1 1 1 1 1]
                sage: (2*w[[1,3],[2]] + w[[1,2,3]] + 2*w[[1,2],[3]]).duality_pairing(h[[1,2],[3]] + 3*h[[1,3],[2]])
                32
            """
        def sum_of_partitions(self, la):
            """
            Return the sum over all sets partitions whose shape is ``la``,
            scaled by `\\prod_i m_i!` where `m_i` is the multiplicity
            of `i` in ``la``.

            INPUT:

            - ``la`` -- integer partition

            OUTPUT: an element of ``self``

            EXAMPLES::

                sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                sage: w.sum_of_partitions([2,1,1])
                2*w{{1}, {2}, {3, 4}} + 2*w{{1}, {2, 3}, {4}} + 2*w{{1}, {2, 4}, {3}}
                 + 2*w{{1, 2}, {3}, {4}} + 2*w{{1, 3}, {2}, {4}} + 2*w{{1, 4}, {2}, {3}}
            """
        class Element(CombinatorialFreeModule.Element):
            """
            An element in the `\\mathbf{w}` basis.
            """
            def expand(self, n, letter: str = 'x'):
                """
                Expand ``self`` written in the `\\mathbf{w}` basis in `n^2`
                commuting variables which satisfy the relation
                `x_{ij} x_{ik} = 0` for all `i`, `j`, and `k`.

                The expansion of an element of the `\\mathbf{w}` basis is
                given by equations (26) and (55) in [HNT06]_.

                INPUT:

                - ``n`` -- integer
                - ``letter`` -- string (default: ``'x'``)

                OUTPUT:

                - The symmetric function of ``self`` expressed in the ``n*n``
                  non-commuting variables described by ``letter``.

                REFERENCES:

                .. [HNT06] \\F. Hivert, J.-C. Novelli, J.-Y. Thibon.
                   *Commutative combinatorial Hopf algebras*. (2006).
                   :arxiv:`0605262v1`.

                EXAMPLES::

                    sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                    sage: w[[1,3],[2]].expand(4)
                    x02*x11*x20 + x03*x11*x30 + x03*x22*x30 + x13*x22*x31

                One can use a different set of variable by using the
                optional argument ``letter``::

                    sage: w[[1,3],[2]].expand(3, letter='y')
                    y02*y11*y20
                """
            def is_symmetric(self):
                """
                Determine if a `NCSym^*` function, expressed in the
                `\\mathbf{w}` basis, is symmetric.

                A function `f` in the `\\mathbf{w}` basis is a symmetric
                function if it is in the image of `\\chi^*`. That is to say we
                have

                .. MATH::

                    f = \\sum_{\\lambda} c_{\\lambda} \\prod_i m_i(\\lambda)!
                    \\sum_{\\lambda(A) = \\lambda} \\mathbf{w}_A

                where the second sum is over all set partitions `A` whose
                shape `\\lambda(A)` is equal to `\\lambda` and `m_i(\\mu)` is
                the multiplicity of `i` in the partition `\\mu`.

                OUTPUT:

                - ``True`` if `\\lambda(A)=\\lambda(B)` implies the coefficients of
                  `\\mathbf{w}_A` and `\\mathbf{w}_B` are equal, ``False`` otherwise

                EXAMPLES::

                    sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                    sage: elt = w.sum_of_partitions([2,1,1])
                    sage: elt.is_symmetric()
                    True
                    sage: elt -= 3*w.sum_of_partitions([1,1])
                    sage: elt.is_symmetric()
                    True
                    sage: w = SymmetricFunctionsNonCommutingVariables(ZZ).dual().w()
                    sage: elt = w.sum_of_partitions([2,1,1]) / 2
                    sage: elt.is_symmetric()
                    False
                    sage: elt = w[[1,3],[2]]
                    sage: elt.is_symmetric()
                    False
                    sage: elt = w[[1],[2,3]] + w[[1,2],[3]] + 2*w[[1,3],[2]]
                    sage: elt.is_symmetric()
                    False
                """
            def to_symmetric_function(self):
                """
                Take a function in the `\\mathbf{w}` basis, and return its
                symmetric realization, when possible, expressed in the
                homogeneous basis of symmetric functions.

                OUTPUT:

                - If ``self`` is a symmetric function, then the expansion
                  in the homogeneous basis of the symmetric functions is returned.
                  Otherwise an error is raised.

                EXAMPLES::

                    sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                    sage: elt = w[[1],[2,3]] + w[[1,2],[3]] + w[[1,3],[2]]
                    sage: elt.to_symmetric_function()
                    h[2, 1]
                    sage: elt = w.sum_of_partitions([2,1,1]) / 2
                    sage: elt.to_symmetric_function()
                    1/2*h[2, 1, 1]

                TESTS::

                    sage: w = SymmetricFunctionsNonCommutingVariables(QQ).dual().w()
                    sage: w(0).to_symmetric_function()
                    0
                    sage: w([]).to_symmetric_function()
                    h[]
                    sage: (2*w([])).to_symmetric_function()
                    2*h[]
                """
