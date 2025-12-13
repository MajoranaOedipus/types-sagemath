from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

class TorsionPoint(ModuleElement):
    """
    An element of a finite subgroup of a modular abelian variety.

    INPUT:

    - ``parent`` -- a finite subgroup of a modular abelian variety

    - ``element`` -- a `\\QQ`-vector space element that represents
      this element in terms of the ambient rational homology

    - ``check`` -- boolean (default: ``True``); whether to check that
      element is in the appropriate vector space

    EXAMPLES:

    The following calls the :class:`TorsionPoint` constructor implicitly::

        sage: J = J0(11)
        sage: G = J.finite_subgroup([[1/3,0], [0,1/5]]); G
        Finite subgroup with invariants [15] over QQbar of Abelian variety J0(11) of dimension 1
        sage: type(G.0)
        <class 'sage.modular.abvar.finite_subgroup.FiniteSubgroup_lattice_with_category.element_class'>
    """
    def __init__(self, parent, element, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: J = J0(11)
            sage: G = J.finite_subgroup([[1/2,0], [0,1/2]])
            sage: TestSuite(G).run() # long time
        """
    def element(self):
        """
        Return a vector over `\\QQ` defining ``self``.

        OUTPUT:

        - A vector in the rational homology of the ambient modular
          Jacobian variety.

        EXAMPLES:

        We create some elements of `J_0(11)`::

            sage: J = J0(11)
            sage: G = J.finite_subgroup([[1/3,0], [0,1/5]]); G
            Finite subgroup with invariants [15] over QQbar of
             Abelian variety J0(11) of dimension 1
            sage: G.0.element()
            (1/3, 0)

        The underlying element is a vector over the rational numbers::

            sage: v = (G.0-G.1).element(); v
            (1/3, -1/5)
            sage: type(v)
            <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>
        """
    def additive_order(self):
        """
        Return the additive order of ``self``.

        EXAMPLES::

            sage: J = J0(11); G = J.finite_subgroup([[1/3,0], [0,1/5]])
            sage: G.0.additive_order()
            3
            sage: G.1.additive_order()
            5
            sage: (G.0 + G.1).additive_order()
            15
            sage: (3*G.0).additive_order()
            1
        """
