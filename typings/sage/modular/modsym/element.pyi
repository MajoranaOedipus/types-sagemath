import sage.modular.hecke.all as hecke
from sage.misc.repr import repr_lincomb as repr_lincomb

def is_ModularSymbolsElement(x) -> bool:
    """
    Return ``True`` if x is an element of a modular symbols space.

    EXAMPLES::

        sage: sage.modular.modsym.element.is_ModularSymbolsElement(ModularSymbols(11, 2).0)
        doctest:warning...
        DeprecationWarning: The function is_ModularSymbolsElement is deprecated;
        use 'isinstance(..., ModularSymbolsElement)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        True
        sage: sage.modular.modsym.element.is_ModularSymbolsElement(13)
        False
    """
def set_modsym_print_mode(mode: str = 'manin') -> None:
    """
    Set the mode for printing of elements of modular symbols spaces.

    INPUT:

    - ``mode`` -- string; the possibilities are as follows:

      - ``'manin'`` -- (the default) formal sums of Manin
        symbols [P(X,Y),(u,v)]

      - ``'modular'`` -- formal sums of Modular symbols
        P(X,Y)\\*alpha,beta, where alpha and beta are cusps

      - ``'vector'`` -- as vectors on the basis for the
        ambient space

    OUTPUT: none

    EXAMPLES::

        sage: M = ModularSymbols(13, 8)
        sage: x = M.0 + M.1 + M.14
        sage: set_modsym_print_mode('manin'); x
        [X^5*Y,(1,11)] + [X^5*Y,(1,12)] + [X^6,(1,11)]
        sage: set_modsym_print_mode('modular'); x
        1610510*X^6*{-1/11, 0} + 893101*X^5*Y*{-1/11, 0} + 206305*X^4*Y^2*{-1/11, 0} + 25410*X^3*Y^3*{-1/11, 0} + 1760*X^2*Y^4*{-1/11, 0} + 65*X*Y^5*{-1/11, 0} - 248832*X^6*{-1/12, 0} - 103680*X^5*Y*{-1/12, 0} - 17280*X^4*Y^2*{-1/12, 0} - 1440*X^3*Y^3*{-1/12, 0} - 60*X^2*Y^4*{-1/12, 0} - X*Y^5*{-1/12, 0} + Y^6*{-1/11, 0}
        sage: set_modsym_print_mode('vector'); x
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
        sage: set_modsym_print_mode()
    """

class ModularSymbolsElement(hecke.HeckeModuleElement):
    """
    An element of a space of modular symbols.

    TESTS::

        sage: x = ModularSymbols(3, 12).cuspidal_submodule().gen(0)
        sage: x == loads(dumps(x))
        True
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        INPUT:

        - ``parent`` -- a space of modular symbols

        - ``x`` -- a free module element that represents the modular
          symbol in terms of a basis for the ambient space (not in
          terms of a basis for parent!)

        EXAMPLES::

            sage: S = ModularSymbols(11, sign=1).cuspidal_submodule()
            sage: S(vector([0,1])) == S.basis()[0]
            True
            sage: S(vector([1,0]))
            Traceback (most recent call last):
            ...
            TypeError: x does not coerce to an element of this Hecke module
        """
    def list(self):
        """
        Return a list of the coordinates of ``self`` in terms of a basis for
        the ambient space.

        EXAMPLES::

            sage: ModularSymbols(37, 2).0.list()
            [1, 0, 0, 0, 0]
        """
    def manin_symbol_rep(self):
        """
        Return a representation of ``self`` as a formal sum of Manin symbols.

        EXAMPLES::

            sage: x = ModularSymbols(37, 4).0
            sage: x.manin_symbol_rep()
            [X^2,(0,1)]

        The result is cached::

            sage: x.manin_symbol_rep() is x.manin_symbol_rep()
            True
        """
    def modular_symbol_rep(self):
        """
        Return a representation of ``self`` as a formal sum of modular symbols.

        EXAMPLES::

            sage: x = ModularSymbols(37, 4).0
            sage: x.modular_symbol_rep()
            X^2*{0, Infinity}

        The result is cached::

            sage: x.modular_symbol_rep() is x.modular_symbol_rep()
            True
        """
