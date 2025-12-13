from sage.categories.category_types import Category_module as Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules as Modules
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory, tensor as tensor
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class QuantumGroupRepresentations(Category_module):
    """
    The category of quantum group representations.
    """
    @cached_method
    def super_categories(self):
        """
        Return the super categories of ``self``.

        EXAMPLES::

            sage: from sage.categories.quantum_group_representations import QuantumGroupRepresentations
            sage: QuantumGroupRepresentations(ZZ['q'].fraction_field()).super_categories()
            [Category of vector spaces over
              Fraction Field of Univariate Polynomial Ring in q over Integer Ring]
        """
    def example(self):
        """
        Return an example of a quantum group representation as per
        :meth:`Category.example <sage.categories.category.Category.example>`.

        EXAMPLES::

            sage: from sage.categories.quantum_group_representations import QuantumGroupRepresentations
            sage: Cat = QuantumGroupRepresentations(ZZ['q'].fraction_field())
            sage: Cat.example()                                                         # needs sage.combinat sage.graphs sage.modules
            V((2, 1, 0))
        """
    class WithBasis(CategoryWithAxiom_over_base_ring):
        """
        The category of quantum group representations with a
        distinguished basis.
        """
        class TensorProducts(TensorProductsCategory):
            """
            The category of quantum group representations with a
            distinguished basis constructed by tensor product of
            quantum group representations with a distinguished basis.
            """
            @cached_method
            def extra_super_categories(self):
                """
                EXAMPLES::

                    sage: from sage.categories.quantum_group_representations import QuantumGroupRepresentations
                    sage: Cat = QuantumGroupRepresentations(ZZ['q'].fraction_field())
                    sage: Cat.WithBasis().TensorProducts().extra_super_categories()
                    [Category of quantum group representations with basis over
                      Fraction Field of Univariate Polynomial Ring in q over Integer Ring]
                """
            class ParentMethods:
                def e_on_basis(self, i, b):
                    """
                    Return the action of `e_i` on the basis element
                    indexed by ``b``.

                    INPUT:

                    - ``i`` -- an element of the index set
                    - ``b`` -- an element of basis keys

                    EXAMPLES::

                        sage: # needs sage.combinat sage.graphs sage.modules
                        sage: from sage.algebras.quantum_groups.representations import (
                        ....:     MinusculeRepresentation, AdjointRepresentation)
                        sage: R = ZZ['q'].fraction_field()
                        sage: CM = crystals.Tableaux(['D',4], shape=[1])
                        sage: VM = MinusculeRepresentation(R, CM)
                        sage: CA = crystals.Tableaux(['D',4], shape=[1,1])
                        sage: VA = AdjointRepresentation(R, CA)
                        sage: v = tensor([VM.an_element(), VA.an_element()]); v
                        4*B[[[1]]] # B[[[1], [2]]] + 4*B[[[1]]] # B[[[1], [3]]]
                         + 6*B[[[1]]] # B[[[2], [3]]] + 4*B[[[2]]] # B[[[1], [2]]]
                         + 4*B[[[2]]] # B[[[1], [3]]] + 6*B[[[2]]] # B[[[2], [3]]]
                         + 6*B[[[3]]] # B[[[1], [2]]] + 6*B[[[3]]] # B[[[1], [3]]]
                         + 9*B[[[3]]] # B[[[2], [3]]]
                        sage: v.e(1)  # indirect doctest
                        4*B[[[1]]] # B[[[1], [2]]]
                         + ((4*q+6)/q)*B[[[1]]] # B[[[1], [3]]]
                         + 6*B[[[1]]] # B[[[2], [3]]]
                         + 6*q*B[[[2]]] # B[[[1], [3]]]
                         + 9*B[[[3]]] # B[[[1], [3]]]
                        sage: v.e(2)  # indirect doctest
                        4*B[[[1]]] # B[[[1], [2]]]
                         + ((6*q+4)/q)*B[[[2]]] # B[[[1], [2]]]
                         + 6*B[[[2]]] # B[[[1], [3]]]
                         + 9*B[[[2]]] # B[[[2], [3]]]
                         + 6*q*B[[[3]]] # B[[[1], [2]]]
                        sage: v.e(3)  # indirect doctest
                        0
                        sage: v.e(4)  # indirect doctest
                        0
                    """
                def f_on_basis(self, i, b):
                    """
                    Return the action of `f_i` on the basis element
                    indexed by ``b``.

                    INPUT:

                    - ``i`` -- an element of the index set
                    - ``b`` -- an element of basis keys

                    EXAMPLES::

                        sage: # needs sage.combinat sage.graphs sage.modules
                        sage: from sage.algebras.quantum_groups.representations import (
                        ....:     MinusculeRepresentation, AdjointRepresentation)
                        sage: R = ZZ['q'].fraction_field()
                        sage: KM = crystals.KirillovReshetikhin(['B',3,1], 3,1)
                        sage: VM = MinusculeRepresentation(R, KM)
                        sage: KA = crystals.KirillovReshetikhin(['B',3,1], 2,1)
                        sage: VA = AdjointRepresentation(R, KA)
                        sage: v = tensor([VM.an_element(), VA.an_element()]); v
                        4*B[[+++, []]] # B[[]] + 4*B[[+++, []]] # B[[[1], [2]]]
                         + 6*B[[+++, []]] # B[[[1], [3]]] + 4*B[[++-, []]] # B[[]]
                         + 4*B[[++-, []]] # B[[[1], [2]]]
                         + 6*B[[++-, []]] # B[[[1], [3]]] + 6*B[[+-+, []]] # B[[]]
                         + 6*B[[+-+, []]] # B[[[1], [2]]]
                         + 9*B[[+-+, []]] # B[[[1], [3]]]
                        sage: v.f(0)  # indirect doctest
                        ((4*q^4+4)/q^2)*B[[+++, []]] # B[[[1], [2]]]
                         + ((4*q^4+4)/q^2)*B[[++-, []]] # B[[[1], [2]]]
                         + ((6*q^4+6)/q^2)*B[[+-+, []]] # B[[[1], [2]]]
                        sage: v.f(1)  # indirect doctest
                        6*B[[+++, []]] # B[[[2], [3]]]
                         + 6*B[[++-, []]] # B[[[2], [3]]]
                         + 9*B[[+-+, []]] # B[[[2], [3]]]
                         + 6*B[[-++, []]] # B[[]]
                         + 6*B[[-++, []]] # B[[[1], [2]]]
                         + 9*q^2*B[[-++, []]] # B[[[1], [3]]]
                        sage: v.f(2)  # indirect doctest
                        4*B[[+++, []]] # B[[[1], [3]]]
                         + 4*B[[++-, []]] # B[[[1], [3]]]
                         + 4*B[[+-+, []]] # B[[]]
                         + 4*q^2*B[[+-+, []]] # B[[[1], [2]]]
                         + ((6*q^2+6)/q^2)*B[[+-+, []]] # B[[[1], [3]]]
                        sage: v.f(3)  # indirect doctest
                        6*B[[+++, []]] # B[[[1], [0]]]
                         + 4*B[[++-, []]] # B[[]]
                         + 4*B[[++-, []]] # B[[[1], [2]]]
                         + 6*q^2*B[[++-, []]] # B[[[1], [3]]]
                         + 6*B[[++-, []]] # B[[[1], [0]]]
                         + 9*B[[+-+, []]] # B[[[1], [0]]]
                         + 6*B[[+--, []]] # B[[]]
                         + 6*B[[+--, []]] # B[[[1], [2]]]
                         + 9*q^2*B[[+--, []]] # B[[[1], [3]]]
                    """
                def K_on_basis(self, i, b, power: int = 1):
                    """
                    Return the action of `K_i` on the basis element indexed by ``b``
                    to the power ``power``.

                    INPUT:

                    - ``i`` -- an element of the index set
                    - ``b`` -- an element of basis keys
                    - ``power`` -- (default: 1) the power of `K_i`

                    EXAMPLES::

                        sage: # needs sage.combinat sage.graphs sage.modules
                        sage: from sage.algebras.quantum_groups.representations import (
                        ....:     MinusculeRepresentation, AdjointRepresentation)
                        sage: R = ZZ['q'].fraction_field()
                        sage: CM = crystals.Tableaux(['A',2], shape=[1])
                        sage: VM = MinusculeRepresentation(R, CM)
                        sage: CA = crystals.Tableaux(['A',2], shape=[2,1])
                        sage: VA = AdjointRepresentation(R, CA)
                        sage: v = tensor([sum(VM.basis()), VA.module_generator()]); v
                        B[[[1]]] # B[[[1, 1], [2]]]
                         + B[[[2]]] # B[[[1, 1], [2]]]
                         + B[[[3]]] # B[[[1, 1], [2]]]
                        sage: v.K(1)  # indirect doctest
                        q^2*B[[[1]]] # B[[[1, 1], [2]]]
                         + B[[[2]]] # B[[[1, 1], [2]]]
                         + q*B[[[3]]] # B[[[1, 1], [2]]]
                        sage: v.K(2, -1)  # indirect doctest
                        1/q*B[[[1]]] # B[[[1, 1], [2]]]
                         + 1/q^2*B[[[2]]] # B[[[1, 1], [2]]]
                         + B[[[3]]] # B[[[1, 1], [2]]]
                    """
        class ParentMethods:
            def tensor(*factors):
                """
                Return the tensor product of ``self`` with the
                representations ``factors``.

                EXAMPLES::

                    sage: # needs sage.combinat sage.graphs sage.modules
                    sage: from sage.algebras.quantum_groups.representations import (
                    ....:     MinusculeRepresentation, AdjointRepresentation)
                    sage: R = ZZ['q'].fraction_field()
                    sage: CM = crystals.Tableaux(['D',4], shape=[1])
                    sage: CA = crystals.Tableaux(['D',4], shape=[1,1])
                    sage: V = MinusculeRepresentation(R, CM)
                    sage: V.tensor(V, V)
                    V((1, 0, 0, 0)) # V((1, 0, 0, 0)) # V((1, 0, 0, 0))
                    sage: A = MinusculeRepresentation(R, CA)
                    sage: V.tensor(A)
                    V((1, 0, 0, 0)) # V((1, 1, 0, 0))
                    sage: B = crystals.Tableaux(['A',2], shape=[1])
                    sage: W = MinusculeRepresentation(R, B)
                    sage: tensor([W,V])
                    Traceback (most recent call last):
                    ...
                    ValueError: all factors must be of the same Cartan type
                    sage: tensor([V,A,W])
                    Traceback (most recent call last):
                    ...
                    ValueError: all factors must be of the same Cartan type
                """
        class ElementMethods:
            def e(self, i):
                """
                Return the action of `e_i` on ``self``.

                INPUT:

                - ``i`` -- an element of the index set

                EXAMPLES::

                    sage: # needs sage.combinat sage.graphs sage.modules
                    sage: from sage.algebras.quantum_groups.representations import AdjointRepresentation
                    sage: C = crystals.Tableaux(['G',2], shape=[1,1])
                    sage: R = ZZ['q'].fraction_field()
                    sage: V = AdjointRepresentation(R, C)
                    sage: v = V.an_element(); v
                    2*B[[[1], [2]]] + 2*B[[[1], [3]]] + 3*B[[[2], [3]]]
                    sage: v.e(1)
                    ((3*q^4+3*q^2+3)/q^2)*B[[[1], [3]]]
                    sage: v.e(2)
                    2*B[[[1], [2]]]
                """
            def f(self, i):
                """
                Return the action of `f_i` on ``self``.

                INPUT:

                - ``i`` -- an element of the index set

                EXAMPLES::

                    sage: # needs sage.combinat sage.graphs sage.modules
                    sage: from sage.algebras.quantum_groups.representations import AdjointRepresentation
                    sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,1)
                    sage: R = ZZ['q'].fraction_field()
                    sage: V = AdjointRepresentation(R, K)
                    sage: v = V.an_element(); v
                    2*B[[]] + 2*B[[[1], [2]]] + 3*B[[[1], [3]]]
                    sage: v.f(0)
                    ((2*q^2+2)/q)*B[[[1], [2]]]
                    sage: v.f(1)
                    3*B[[[2], [3]]]
                    sage: v.f(2)
                    2*B[[[1], [3]]]
                    sage: v.f(3)
                    3*B[[[1], [4]]]
                    sage: v.f(4)
                    3*B[[[1], [-4]]]
                """
            def K(self, i, power: int = 1):
                """
                Return the action of `K_i` on ``self`` to the power ``power``.

                INPUT:

                - ``i`` -- an element of the index set
                - ``power`` -- (default: 1) the power of `K_i`

                EXAMPLES::

                    sage: # needs sage.combinat sage.graphs sage.modules
                    sage: from sage.algebras.quantum_groups.representations import AdjointRepresentation
                    sage: K = crystals.KirillovReshetikhin(['D',4,2], 1,1)
                    sage: R = ZZ['q'].fraction_field()
                    sage: V = AdjointRepresentation(R, K)
                    sage: v = V.an_element(); v
                    2*B[[]] + 2*B[[[1]]] + 3*B[[[2]]]
                    sage: v.K(0)
                    2*B[[]] + 2/q^2*B[[[1]]] + 3*B[[[2]]]
                    sage: v.K(1)
                    2*B[[]] + 2*q^2*B[[[1]]] + 3/q^2*B[[[2]]]
                    sage: v.K(1, 2)
                    2*B[[]] + 2*q^4*B[[[1]]] + 3/q^4*B[[[2]]]
                    sage: v.K(1, -1)
                    2*B[[]] + 2/q^2*B[[[1]]] + 3*q^2*B[[[2]]]
                """
    class TensorProducts(TensorProductsCategory):
        """
        The category of quantum group representations constructed
        by tensor product of quantum group representations.

        .. WARNING::

            We use the reversed coproduct in order to match the
            tensor product rule on crystals.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: from sage.categories.quantum_group_representations import QuantumGroupRepresentations
                sage: Cat = QuantumGroupRepresentations(ZZ['q'].fraction_field())
                sage: Cat.TensorProducts().extra_super_categories()
                [Category of quantum group representations over
                 Fraction Field of Univariate Polynomial Ring in q over Integer Ring]
            """
        class ParentMethods:
            def cartan_type(self):
                """
                Return the Cartan type of ``self``.

                EXAMPLES::

                    sage: # needs sage.combinat sage.graphs sage.modules
                    sage: from sage.algebras.quantum_groups.representations import MinusculeRepresentation
                    sage: C = crystals.Tableaux(['C',2], shape=[1])
                    sage: R = ZZ['q'].fraction_field()
                    sage: V = MinusculeRepresentation(R, C)
                    sage: T = tensor([V,V])
                    sage: T.cartan_type()
                    ['C', 2]
                """
    class ParentMethods:
        @abstract_method
        def cartan_type(self) -> None:
            """
            Return the Cartan type of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.modules
                sage: from sage.algebras.quantum_groups.representations import MinusculeRepresentation
                sage: C = crystals.Tableaux(['C',4], shape=[1])
                sage: R = ZZ['q'].fraction_field()
                sage: V = MinusculeRepresentation(R, C)
                sage: V.cartan_type()
                ['C', 4]
            """
        @cached_method
        def index_set(self):
            """
            Return the index set of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.modules
                sage: from sage.algebras.quantum_groups.representations import MinusculeRepresentation
                sage: C = crystals.Tableaux(['C',4], shape=[1])
                sage: R = ZZ['q'].fraction_field()
                sage: V = MinusculeRepresentation(R, C)
                sage: V.index_set()
                (1, 2, 3, 4)
            """
        def q(self):
            """
            Return the quantum parameter `q` of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.graphs sage.modules
                sage: from sage.algebras.quantum_groups.representations import MinusculeRepresentation
                sage: C = crystals.Tableaux(['C',4], shape=[1])
                sage: R = ZZ['q'].fraction_field()
                sage: V = MinusculeRepresentation(R, C)
                sage: V.q()
                q
            """
