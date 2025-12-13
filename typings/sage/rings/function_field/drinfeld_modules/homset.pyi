from sage.categories.action import Action as Action
from sage.categories.drinfeld_modules import DrinfeldModules as DrinfeldModules
from sage.categories.homset import Homset as Homset
from sage.misc.latex import latex as latex
from sage.rings.function_field.drinfeld_modules.morphism import DrinfeldModuleMorphism as DrinfeldModuleMorphism

class DrinfeldModuleMorphismAction(Action):
    """
    Action of the function ring on the homset of a Drinfeld module.

    EXAMPLES::

        sage: Fq = GF(5)
        sage: A.<T> = Fq[]
        sage: K.<z> = Fq.extension(3)
        sage: phi = DrinfeldModule(A, [z, 1, z])
        sage: psi = DrinfeldModule(A, [z, z^2 + 4*z + 3, 2*z^2 + 4*z + 4])
        sage: H = Hom(phi, psi)
        sage: t = phi.ore_variable()
        sage: f = H(t + 2)

    Left action::

        sage: (T + 1) * f
        Drinfeld Module morphism:
          From: Drinfeld module defined by T |--> z*t^2 + t + z
          To:   Drinfeld module defined by T |--> (2*z^2 + 4*z + 4)*t^2 + (z^2 + 4*z + 3)*t + z
          Defn: (2*z^2 + 4*z + 4)*t^3 + (2*z + 1)*t^2 + (2*z^2 + 4*z + 2)*t + 2*z + 2

    Right action currently does not work (it is a known bug, due to an
    incompatibility between multiplication of morphisms and the coercion
    system)::

        sage: f * (T + 1)
        Traceback (most recent call last):
        ...
        TypeError: right (=T + 1) must be a map to multiply it by Drinfeld Module morphism:
          From: Drinfeld module defined by T |--> z*t^2 + t + z
          To:   Drinfeld module defined by T |--> (2*z^2 + 4*z + 4)*t^2 + (z^2 + 4*z + 3)*t + z
          Defn: t + 2
    """
    def __init__(self, A, H, is_left, op) -> None:
        """
        Initialize this action.

        INPUT:

        - ``A`` -- the function ring of the underlying Drinfeld module

        - ``H`` -- a homset between Drinfeld modules

        - ``is_left`` -- boolean

        - ``op`` -- an operator

        TESTS::

            sage: Fq = GF(27)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z6, z6, 2])
            sage: psi = DrinfeldModule(A, [z6, 2*z6^5 + 2*z6^4 + 2*z6 + 1, 2])
            sage: H = Hom(phi, psi)

            sage: from sage.rings.function_field.drinfeld_modules.homset import DrinfeldModuleMorphismAction
            sage: left_action = DrinfeldModuleMorphismAction(A, H, True, operator.mul)
            sage: TestSuite(left_action).run(skip='_test_pickling')

            sage: right_action = DrinfeldModuleMorphismAction(A, H, False, operator.mul)
            sage: TestSuite(right_action).run(skip='_test_pickling')
        """

class DrinfeldModuleHomset(Homset):
    """
    This class implements the set of morphisms between two Drinfeld
    `\\mathbb{F}_q[T]`-modules.

    INPUT:

    - ``X`` -- the domain

    - ``Y`` -- the codomain

    EXAMPLES::

        sage: Fq = GF(27)
        sage: A.<T> = Fq[]
        sage: K.<z6> = Fq.extension(2)
        sage: phi = DrinfeldModule(A, [z6, z6, 2])
        sage: psi = DrinfeldModule(A, [z6, 2*z6^5 + 2*z6^4 + 2*z6 + 1, 2])
        sage: H = Hom(phi, psi)
        sage: H
        Set of Drinfeld module morphisms
         from (gen) 2*t^2 + z6*t + z6
           to (gen) 2*t^2 + (2*z6^5 + 2*z6^4 + 2*z6 + 1)*t + z6

    ::

        sage: from sage.rings.function_field.drinfeld_modules.homset import DrinfeldModuleHomset
        sage: isinstance(H, DrinfeldModuleHomset)
        True

    There is a simpler syntax for endomorphisms sets::

        sage: E = End(phi)
        sage: E
        Set of Drinfeld module morphisms from (gen) 2*t^2 + z6*t + z6 to (gen) 2*t^2 + z6*t + z6
        sage: E is Hom(phi, phi)
        True

    The domain and codomain must have the same Drinfeld modules
    category::

        sage: rho = DrinfeldModule(A, [Frac(A)(T), 1])
        sage: Hom(phi, rho)
        Traceback (most recent call last):
        ...
        ValueError: Drinfeld modules must be in the same category

    ::

        sage: sigma = DrinfeldModule(A, [1, z6, 2])
        sage: Hom(phi, sigma)
        Traceback (most recent call last):
        ...
        ValueError: Drinfeld modules must be in the same category

    One can create morphism objects by calling the homset::

        sage: identity_morphism = E(1)
        sage: identity_morphism
        Identity morphism of Drinfeld module defined by T |--> 2*t^2 + z6*t + z6

    ::

        sage: t = phi.ore_polring().gen()
        sage: frobenius_endomorphism = E(t^6)
        sage: frobenius_endomorphism
        Endomorphism of Drinfeld module defined by T |--> 2*t^2 + z6*t + z6
          Defn: t^6

    ::

        sage: isogeny = H(t + 1)
        sage: isogeny
        Drinfeld Module morphism:
          From: Drinfeld module defined by T |--> 2*t^2 + z6*t + z6
          To:   Drinfeld module defined by T |--> 2*t^2 + (2*z6^5 + 2*z6^4 + 2*z6 + 1)*t + z6
          Defn: t + 1

    And one can test if an Ore polynomial defines a morphism using the
    ``in`` syntax::

        sage: 1 in H
        False
        sage: t^6 in H
        False
        sage: t + 1 in H
        True
        sage: 1 in E
        True
        sage: t^6 in E
        True
        sage: t + 1 in E
        False

    This also works if the candidate is a morphism object::

        sage: isogeny in H
        True
        sage: E(0) in E
        True
        sage: identity_morphism in H
        False
        sage: frobenius_endomorphism in H
        False
    """
    Element = DrinfeldModuleMorphism
    def __init__(self, X, Y, category=None, check: bool = True) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``X`` -- the domain of the homset

        - ``Y`` -- the codomain of the homset

        - ``category`` -- (default: ``None``) the Drinfeld modules category of
          the domain and codomain

        - ``check`` -- boolean (default: ``True``); check the validity of the
          category

        TESTS::

            sage: Fq = GF(27)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z6, z6, 2])
            sage: psi = DrinfeldModule(A, [z6, 2*z6^5 + 2*z6^4 + 2*z6 + 1, 2])
            sage: H = Hom(phi, psi)
            sage: H.domain() is phi
            True
            sage: H.codomain() is psi
            True
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if the input defines a morphism in the homset.

        INPUT:

        - ``x`` -- an Ore polynomial or a Drinfeld module morphism

        EXAMPLES:

        In the next examples, the input is an Ore polynomial::

            sage: Fq = GF(27)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z6, z6, 2])
            sage: psi = DrinfeldModule(A, [z6, 2*z6^5 + 2*z6^4 + 2*z6 + 1, 2])
            sage: H = Hom(phi, psi)
            sage: E = End(phi)
            sage: t = phi.ore_polring().gen()
            sage: 1 in H
            False
            sage: t^6 in H
            False
            sage: t + 1 in H
            True
            sage: 1 in E
            True
            sage: t^6 in E
            True
            sage: t + 1 in E
            False

        Whereas the input is now a Drinfeld module morphism::

            sage: isogeny = H(t + 1)
            sage: isogeny in H
            True
            sage: E(0) in E
            True
            sage: identity_morphism = E(1)
            sage: identity_morphism in H
            False
            sage: frobenius_endomorphism = phi.frobenius_endomorphism()
            sage: frobenius_endomorphism in H
            False
        """
