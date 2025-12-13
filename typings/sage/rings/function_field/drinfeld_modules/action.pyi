from sage.categories.action import Action as Action
from sage.misc.latex import latex as latex
from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule as DrinfeldModule

class DrinfeldModuleAction(Action):
    """
    This class implements the module action induced by a Drinfeld
    `\\mathbb{F}_q[T]`-module.

    Let `\\phi` be a Drinfeld `\\mathbb{F}_q[T]`-module over a field `K`
    and let `L/K` be a field extension. Let `x \\in L` and let `a` be a
    function ring element; the action is defined as `(a, x) \\mapsto
    \\phi_a(x)`.

    .. NOTE::

        In this implementation, `L` is `K`.

    .. NOTE::

        The user should never explicitly instantiate the class
        `DrinfeldModuleAction`.

    .. WARNING::

        This class may be replaced later on. See issues #34833 and
        #34834.

    INPUT: the Drinfeld module

    EXAMPLES::

        sage: Fq.<z2> = GF(11)
        sage: A.<T> = Fq[]
        sage: K.<z> = Fq.extension(2)
        sage: phi = DrinfeldModule(A, [z, 0, 0, 1])
        sage: action = phi.action()
        sage: action
        Action on Finite Field in z of size 11^2 over its base
         induced by Drinfeld module defined by T |--> t^3 + z

    The action on elements is computed as follows::

        sage: P = T + 1
        sage: a = z
        sage: action(P, a)
        ...
        4*z + 2
        sage: action(0, K.random_element())
        0
        sage: action(A.random_element(), 0)
        0

    Finally, given a Drinfeld module action, it is easy to recover the
    corresponding Drinfeld module::

        sage: action.drinfeld_module() is phi
        True
    """
    def __init__(self, drinfeld_module) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``drinfeld_module`` -- the Drinfeld module

        TESTS::

            sage: Fq.<z2> = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z, 0, 0, 1])
            sage: action = phi.action()
            sage: action._drinfeld_module is phi
            True
            sage: action._base is phi.base()
            True
        """
    def drinfeld_module(self):
        """
        Return the Drinfeld module defining the action.

        OUTPUT: a Drinfeld module

        EXAMPLES::

            sage: Fq.<z2> = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z, 0, 0, 1])
            sage: action = phi.action()
            sage: action.drinfeld_module() is phi
            True
        """
