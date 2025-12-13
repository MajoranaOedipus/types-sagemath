from sage.categories.morphism import Morphism as Morphism
from sage.modules.matrix_morphism import MatrixMorphism as MatrixMorphism

def is_HeckeModuleMorphism(x):
    """
    Return ``True`` if x is of type HeckeModuleMorphism.

    EXAMPLES::

        sage: sage.modular.hecke.morphism.is_HeckeModuleMorphism(ModularSymbols(6).hecke_operator(7).hecke_module_morphism())
        doctest:warning...
        DeprecationWarning: the function is_HeckeModuleMorphism is deprecated;
        use 'isinstance(..., HeckeModuleMorphism)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
    """
def is_HeckeModuleMorphism_matrix(x):
    """

    EXAMPLES::

        sage: sage.modular.hecke.morphism.is_HeckeModuleMorphism_matrix(ModularSymbols(6).hecke_operator(7).matrix_form().hecke_module_morphism())
        doctest:warning...
        DeprecationWarning: the function is_HeckeModuleMorphism_matrix is deprecated;
        use 'isinstance(..., HeckeModuleMorphism_matrix)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
    """

class HeckeModuleMorphism(Morphism):
    """
    Abstract base class for morphisms of Hecke modules.
    """

class HeckeModuleMorphism_matrix(MatrixMorphism, HeckeModuleMorphism):
    """
    Morphisms of Hecke modules when the morphism is given by a matrix.

    Note that care is needed when composing morphisms, because morphisms in
    Sage act on the left, but their matrices act on the right (!). So if F: A
    -> B and G : B -> C are morphisms, the composition A -> C is G*F, but its
    matrix is F.matrix() * G.matrix().

    EXAMPLES::

        sage: A = ModularForms(1, 4)
        sage: B = ModularForms(1, 16)
        sage: C = ModularForms(1, 28)
        sage: F = A.Hom(B)(matrix(QQ,1,2,srange(1, 3)))
        sage: G = B.Hom(C)(matrix(QQ,2,3,srange(1, 7)))
        sage: G * F
        Hecke module morphism defined by the matrix
        [ 9 12 15]
        Domain: Modular Forms space of dimension 1 for Modular Group SL(2,Z) ...
        Codomain: Modular Forms space of dimension 3 for Modular Group SL(2,Z) ...
        sage: F * G
        Traceback (most recent call last):
        ...
        TypeError: Incompatible composition of morphisms: domain of left morphism must be codomain of right.
    """
    def __init__(self, parent, A, name: str = '', side: str = 'left') -> None:
        """
        INPUT:

        -  ``parent`` -- ModularSymbolsHomspace

        - ``A`` -- matrix

        - ``name`` -- string (default: ``''``); name of the morphism
           (used for printing)

        - ``side`` -- string (default: ``'left'``)

        EXAMPLES::

            sage: M = ModularSymbols(6)
            sage: t = M.Hom(M)(matrix(QQ,3,3,srange(9)), name='spam'); t
            Hecke module morphism spam defined by the matrix
            [0 1 2]
            [3 4 5]
            [6 7 8]
            Domain: Modular Symbols space of dimension 3 for Gamma_0(6) of weight ...
            Codomain: Modular Symbols space of dimension 3 for Gamma_0(6) of weight ...
            sage: t == loads(dumps(t))
            True
        """
    def name(self, new=None):
        '''
        Return the name of this operator, or set it to a new name.

        EXAMPLES::

            sage: M = ModularSymbols(6)
            sage: t = M.Hom(M)(matrix(QQ,3,3,srange(9)), name=\'spam\'); t
            Hecke module morphism spam defined by ...
            sage: t.name()
            \'spam\'
            sage: t.name("eggs"); t
            Hecke module morphism eggs defined by ...
        '''
