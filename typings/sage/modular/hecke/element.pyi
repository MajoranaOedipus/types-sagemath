from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import op_NE as op_NE, richcmp as richcmp

def is_HeckeModuleElement(x):
    """
    Return ``True`` if x is a Hecke module element, i.e., of type HeckeModuleElement.

    EXAMPLES::

        sage: sage.modular.hecke.all.is_HeckeModuleElement(0)
        doctest:warning...
        DeprecationWarning: the function is_HeckeModuleElement is deprecated;
        use 'isinstance(..., HeckeModuleElement)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        False
        sage: sage.modular.hecke.all.is_HeckeModuleElement(BrandtModule(37)([1,2,3]))
        True
    """

class HeckeModuleElement(ModuleElement):
    """
    Element of a Hecke module.
    """
    def __init__(self, parent, x=None) -> None:
        """
        INPUT:

        - ``parent`` -- a Hecke module

        - ``x`` -- element of the free module associated to parent

        EXAMPLES::

            sage: v = sage.modular.hecke.all.HeckeModuleElement(BrandtModule(37), vector(QQ,[1,2,3])); v
            (1, 2, 3)
            sage: type(v)
            <class 'sage.modular.hecke.element.HeckeModuleElement'>

        TESTS::

            sage: v = ModularSymbols(37).0
            sage: loads(dumps(v))
            (1,0)
            sage: loads(dumps(v)) == v
            True
        """
    def element(self):
        """
        Return underlying vector space element that defines this Hecke module element.

        EXAMPLES::

            sage: z = BrandtModule(37)([0,1,-1]).element(); z
            (0, 1, -1)
            sage: type(z)
            <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>
        """
    def ambient_module(self):
        """
        Return the ambient Hecke module that contains this element.

        EXAMPLES::

            sage: BrandtModule(37)([0,1,-1]).ambient_module()
            Brandt module of dimension 3 of level 37 of weight 2 over Rational Field
        """
    def is_cuspidal(self) -> bool:
        """
        Return ``True`` if this element is cuspidal.

        EXAMPLES::

            sage: M = ModularForms(2, 22); M.0.is_cuspidal()
            True
            sage: (M.0 + M.4).is_cuspidal()
            False
            sage: EllipticCurve('37a1').newform().is_cuspidal()
            True

        It works for modular symbols too::

            sage: M = ModularSymbols(19,2)
            sage: M.0.is_cuspidal()
            False
            sage: M.1.is_cuspidal()
            True

        TESTS:

        Verify that :issue:`21497` is fixed::

            sage: M = ModularSymbols(Gamma0(3),weight=22,sign=1)
            sage: N = next(S for S in M.decomposition(anemic=False) if S.hecke_matrix(3).trace()==-128844)
            sage: [g.is_cuspidal() for g in N.gens()]
            [True, True]
        """
    def is_eisenstein(self) -> bool:
        """
        Return ``True`` if this element is Eisenstein.

        This makes sense for both modular forms and modular symbols.

        EXAMPLES::

            sage: CuspForms(2,8).0.is_eisenstein()
            False
            sage: M = ModularForms(2,8);(M.0  + M.1).is_eisenstein()
            False
            sage: M.1.is_eisenstein()
            True
            sage: ModularSymbols(19,4).0.is_eisenstein()
            False
            sage: EllipticCurve('37a1').newform().element().is_eisenstein()
            False
        """
    def is_new(self, p=None) -> bool:
        """
        Return ``True`` if this element is `p`-new.

        If `p` is ``None``, return ``True`` if the element is new.

        EXAMPLES::

            sage: CuspForms(22, 2).0.is_new(2)
            False
            sage: CuspForms(22, 2).0.is_new(11)
            True
            sage: CuspForms(22, 2).0.is_new()
            False
        """
    def is_old(self, p=None) -> bool:
        """
        Return ``True`` if this element is `p`-old.

        If `p` is ``None``, return ``True`` if the element is old.

        EXAMPLES::

            sage: CuspForms(22, 2).0.is_old(11)
            False
            sage: CuspForms(22, 2).0.is_old(2)
            True
            sage: CuspForms(22, 2).0.is_old()
            True
            sage: EisensteinForms(144, 2).1.is_old()  # long time (3s on sage.math, 2011)
            False
            sage: EisensteinForms(144, 2).1.is_old(2) # not implemented
            False
        """
