from . import ambient as ambient
from .cuspidal_submodule import CuspidalSubmodule_R as CuspidalSubmodule_R
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ

class ModularFormsAmbient_R(ambient.ModularFormsAmbient):
    def __init__(self, M, base_ring) -> None:
        """
        Ambient space of modular forms over a ring other than QQ.

        EXAMPLES::

            sage: M = ModularForms(23, 2, base_ring=GF(7)) # indirect doctest
            sage: M
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(23)
             of weight 2 over Finite Field of size 7
            sage: M == loads(dumps(M))
            True
        """
    def modular_symbols(self, sign: int = 0):
        """
        Return the space of modular symbols attached to this space, with the given sign (default 0).

        TESTS::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: chi = DirichletGroup(5, base_ring=K).0
            sage: x = polygen(ZZ, 'x')
            sage: L.<c> = K.extension(x^2 - 402*i)
            sage: M = ModularForms(chi, 7, base_ring=L)
            sage: symbs = M.modular_symbols()
            sage: symbs.character() == chi
            True
            sage: symbs.base_ring() == L
            True
        """
    def cuspidal_submodule(self):
        """
        Return the cuspidal subspace of this space.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: C = CuspForms(7, 4, base_ring=CyclotomicField(5))  # indirect doctest
            sage: type(C)
            <class 'sage.modular.modform.cuspidal_submodule.CuspidalSubmodule_R_with_category'>
        """
    def change_ring(self, R):
        """
        Return this modular forms space with the base ring changed to the ring R.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: chi = DirichletGroup(109, CyclotomicField(3)).0
            sage: M9 = ModularForms(chi, 2, base_ring = CyclotomicField(9))
            sage: M9.change_ring(CyclotomicField(15))
            Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2
             over Cyclotomic Field of order 15 and degree 8
            sage: M9.change_ring(QQ)
            Traceback (most recent call last):
            ...
            ValueError: Space cannot be defined over Rational Field
        """
