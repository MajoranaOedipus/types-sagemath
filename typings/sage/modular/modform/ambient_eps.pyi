from . import ambient_R as ambient_R, cuspidal_submodule as cuspidal_submodule, eisenstein_submodule as eisenstein_submodule
from .ambient import ModularFormsAmbient as ModularFormsAmbient
from sage.misc.cachefunc import cached_method as cached_method
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_constructor as Gamma1_constructor
from sage.rings.integer import Integer as Integer

class ModularFormsAmbient_eps(ModularFormsAmbient):
    """
    A space of modular forms with character.
    """
    def __init__(self, character, weight: int = 2, base_ring=None, eis_only: bool = False) -> None:
        """
        Create an ambient modular forms space with character.

        .. NOTE::

           The base ring must be of characteristic 0.  The ambient_R
           Python module is used for computing in characteristic p,
           which we view as the reduction of characteristic 0.

        INPUT:

        - ``weight`` -- integer

        - ``character`` -- dirichlet.DirichletCharacter

        - ``base_ring`` -- base field

        EXAMPLES::

            sage: m = ModularForms(DirichletGroup(11).0,3); m
            Modular Forms space of dimension 3, character [zeta10] and weight 3 over
             Cyclotomic Field of order 10 and degree 4
            sage: type(m)
            <class 'sage.modular.modform.ambient_eps.ModularFormsAmbient_eps_with_category'>
        """
    @cached_method
    def cuspidal_submodule(self):
        """
        Return the cuspidal submodule of this ambient space of modular forms.

        EXAMPLES::

            sage: eps = DirichletGroup(4).0
            sage: M = ModularForms(eps, 5); M
            Modular Forms space of dimension 3, character [-1] and weight 5
             over Rational Field
            sage: M.cuspidal_submodule()
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 3,
             character [-1] and weight 5 over Rational Field
        """
    def change_ring(self, base_ring):
        """
        Return space with same defining parameters as this ambient
        space of modular symbols, but defined over a different base
        ring.

        EXAMPLES::

            sage: m = ModularForms(DirichletGroup(13).0^2,2); m
            Modular Forms space of dimension 3, character [zeta6] and weight 2 over
             Cyclotomic Field of order 6 and degree 2
            sage: m.change_ring(CyclotomicField(12))
            Modular Forms space of dimension 3, character [zeta6] and weight 2 over
             Cyclotomic Field of order 12 and degree 4

        It must be possible to change the ring of the underlying Dirichlet character::

            sage: m.change_ring(QQ)
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce zeta6 to a rational
        """
    def modular_symbols(self, sign: int = 0):
        """
        Return corresponding space of modular symbols with given sign.

        EXAMPLES::

            sage: eps = DirichletGroup(13).0
            sage: M = ModularForms(eps^2, 2)
            sage: M.modular_symbols()
            Modular Symbols space of dimension 4 and level 13, weight 2,
             character [zeta6], sign 0, over Cyclotomic Field of order 6 and degree 2
            sage: M.modular_symbols(1)
            Modular Symbols space of dimension 3 and level 13, weight 2,
             character [zeta6], sign 1, over Cyclotomic Field of order 6 and degree 2
            sage: M.modular_symbols(-1)
            Modular Symbols space of dimension 1 and level 13, weight 2,
             character [zeta6], sign -1, over Cyclotomic Field of order 6 and degree 2
            sage: M.modular_symbols(2)
            Traceback (most recent call last):
            ...
            ValueError: sign must be -1, 0, or 1
        """
    @cached_method
    def eisenstein_submodule(self):
        """
        Return the submodule of this ambient module with character that is
        spanned by Eisenstein series.  This is the Hecke stable complement
        of the cuspidal submodule.

        EXAMPLES::

            sage: m = ModularForms(DirichletGroup(13).0^2,2); m
            Modular Forms space of dimension 3, character [zeta6] and weight 2 over
             Cyclotomic Field of order 6 and degree 2
            sage: m.eisenstein_submodule()
            Eisenstein subspace of dimension 2 of Modular Forms space of dimension 3,
             character [zeta6] and weight 2 over Cyclotomic Field of order 6 and degree 2
        """
    def hecke_module_of_level(self, N):
        """
        Return the Hecke module of level N corresponding to ``self``, which is the
        domain or codomain of a degeneracy map from ``self``. Here N must be either
        a divisor or a multiple of the level of ``self``, and a multiple of the
        conductor of the character of ``self``.

        EXAMPLES::

            sage: M = ModularForms(DirichletGroup(15).0, 3); M.character().conductor()
            3
            sage: M.hecke_module_of_level(3)
            Modular Forms space of dimension 2, character [-1] and weight 3
             over Rational Field
            sage: M.hecke_module_of_level(5)
            Traceback (most recent call last):
            ...
            ValueError: conductor(=3) must divide M(=5)
            sage: M.hecke_module_of_level(30)
            Modular Forms space of dimension 16, character [-1, 1] and weight 3
             over Rational Field
        """
