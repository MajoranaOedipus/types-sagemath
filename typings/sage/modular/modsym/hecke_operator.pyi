import sage.modular.hecke.hecke_operator
from . import heilbronn as heilbronn
from sage.arith.misc import is_prime as is_prime

class HeckeOperator(sage.modular.hecke.hecke_operator.HeckeOperator):
    def apply_sparse(self, x):
        """
        Return the image of ``x`` under ``self``.

        If ``x`` is not in ``self.domain()``, raise a :exc:`TypeError`.

        EXAMPLES::

            sage: M = ModularSymbols(17,4,-1)
            sage: T = M.hecke_operator(4)
            sage: T.apply_sparse(M.0)
            -27*[X^2,(1,7)] - 167/2*[X^2,(1,9)] - 21/2*[X^2,(1,13)] + 53/2*[X^2,(1,15)]
            sage: [T.apply_sparse(x) == T.hecke_module_morphism()(x) for x in M.basis()]
            [True, True, True, True]
            sage: N = ModularSymbols(17,4,1)
            sage: T.apply_sparse(N.0)
            Traceback (most recent call last):
            ...
            TypeError: x (=[X^2,(0,1)]) must be in Modular Symbols space
            of dimension 4 for Gamma_0(17) of weight 4 with sign -1
            over Rational Field
        """
