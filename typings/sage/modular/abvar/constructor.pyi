from .abvar_newform import ModularAbelianVariety_newform as ModularAbelianVariety_newform
from sage.modular.abvar import abvar as abvar
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroupBase as CongruenceSubgroupBase
from sage.modular.modsym.space import ModularSymbolsSpace as ModularSymbolsSpace
from sage.rings.integer import Integer as Integer

def J0(N):
    """
    Return the Jacobian `J_0(N)` of the modular curve
    `X_0(N)`.

    EXAMPLES::

        sage: J0(389)
        Abelian variety J0(389) of dimension 32

    The result is cached::

        sage: J0(33) is J0(33)
        True
    """
def J1(N):
    """
    Return the Jacobian `J_1(N)` of the modular curve
    `X_1(N)`.

    EXAMPLES::

        sage: J1(389)
        Abelian variety J1(389) of dimension 6112
    """
def JH(N, H):
    """
    Return the Jacobian `J_H(N)` of the modular curve
    `X_H(N)`.

    EXAMPLES::

        sage: JH(389,[16])
        Abelian variety JH(389,[16]) of dimension 64
    """
def AbelianVariety(X):
    """
    Create the abelian variety corresponding to the given defining
    data.

    INPUT:

    - ``X`` -- integer, string, newform, modsym space,
      congruence subgroup or tuple of congruence subgroups

    OUTPUT: a modular abelian variety

    EXAMPLES::

        sage: AbelianVariety(Gamma0(37))
        Abelian variety J0(37) of dimension 2
        sage: AbelianVariety('37a')
        Newform abelian subvariety 37a of dimension 1 of J0(37)
        sage: AbelianVariety(Newform('37a'))
        Newform abelian subvariety 37a of dimension 1 of J0(37)
        sage: AbelianVariety(ModularSymbols(37).cuspidal_submodule())
        Abelian variety J0(37) of dimension 2
        sage: AbelianVariety((Gamma0(37), Gamma0(11)))
        Abelian variety J0(37) x J0(11) of dimension 3
        sage: AbelianVariety(37)
        Abelian variety J0(37) of dimension 2
        sage: AbelianVariety([1,2,3])
        Traceback (most recent call last):
        ...
        TypeError: X must be an integer, string, newform, modsym space, congruence subgroup or tuple of congruence subgroups
    """
