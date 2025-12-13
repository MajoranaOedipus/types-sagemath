from .abvar import ModularAbelianVariety_modsym_abstract as ModularAbelianVariety_modsym_abstract
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modular.abvar import homspace as homspace
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.arithgroup.congroup_gammaH import GammaH_class as GammaH_class
from sage.modular.modform.element import Newform as Newform
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class ModularAbelianVariety_newform(ModularAbelianVariety_modsym_abstract):
    """
    A modular abelian variety attached to a specific newform.
    """
    def __init__(self, f, internal_name: bool = False) -> None:
        """
        Create the modular abelian variety `A_f` attached to the
        newform `f`.

        INPUT:

        - ``f`` -- a newform

        EXAMPLES::

            sage: f = CuspForms(37).newforms('a')[0]
            sage: f.abelian_variety()
            Newform abelian subvariety 37a of dimension 1 of J0(37)

            sage: AbelianVariety(Newforms(1, 12)[0])
            Traceback (most recent call last):
            ...
            TypeError: f must have weight 2
        """
    def newform(self, names=None):
        """
        Return the newform that this modular abelian variety is attached to.

        EXAMPLES::

            sage: f = Newform('37a')
            sage: A = f.abelian_variety()
            sage: A.newform()
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + O(q^6)
            sage: A.newform() is f
            True

        If the a variable name has not been specified, we must specify one::

            sage: A = AbelianVariety('67b')
            sage: A.newform()
            Traceback (most recent call last):
            ...
            TypeError: You must specify the name of the generator.
            sage: A.newform('alpha')
            q + alpha*q^2 + (-alpha - 3)*q^3 + (-3*alpha - 3)*q^4 - 3*q^5 + O(q^6)

        If the eigenform is actually over `\\QQ` then we don't have to specify
        the name::

            sage: A = AbelianVariety('67a')
            sage: A.newform()
            q + 2*q^2 - 2*q^3 + 2*q^4 + 2*q^5 + O(q^6)
        """
    def label(self) -> str:
        """
        Return canonical label that defines this newform modular
        abelian variety.

        OUTPUT: string

        EXAMPLES::

            sage: A = AbelianVariety('43b')
            sage: A.label()
            '43b'
        """
    def factor_number(self):
        """
        Return factor number.

        OUTPUT: int

        EXAMPLES::

            sage: A = AbelianVariety('43b')
            sage: A.factor_number()
            1
        """
    def endomorphism_ring(self):
        """
        Return the endomorphism ring of this newform abelian variety.

        EXAMPLES::

            sage: A = AbelianVariety('23a')
            sage: E = A.endomorphism_ring(); E
            Endomorphism ring of Newform abelian subvariety 23a of dimension 2 of J0(23)

        We display the matrices of these two basis matrices::

            sage: E.0.matrix()
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
            sage: E.1.matrix()
            [ 0  1 -1  0]
            [ 0  1 -1  1]
            [-1  2 -2  1]
            [-1  1  0 -1]

        The result is cached::

            sage: E is A.endomorphism_ring()
            True
        """
