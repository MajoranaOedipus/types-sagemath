from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent, Realizations as Realizations
from sage.categories.sets_cat import Sets as Sets
from sage.geometry.hyperbolic_space.hyperbolic_model import HyperbolicModelHM as HyperbolicModelHM, HyperbolicModelKM as HyperbolicModelKM, HyperbolicModelPD as HyperbolicModelPD, HyperbolicModelUHP as HyperbolicModelUHP
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def HyperbolicSpace(n):
    """
    Return ``n`` dimensional hyperbolic space.

    EXAMPLES::

        sage: from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicSpace
        sage: HyperbolicSpace(2)
        Hyperbolic plane
    """

class HyperbolicPlane(Parent, UniqueRepresentation):
    """
    The hyperbolic plane `\\mathbb{H}^2`.

    Here are the models currently implemented:

    - ``UHP`` -- upper half plane
    - ``PD`` -- Poincaré disk
    - ``KM`` -- Klein disk
    - ``HM`` -- hyperboloid model
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: TestSuite(H).run()
        """
    def a_realization(self):
        """
        Return a realization of ``self``.

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: H.a_realization()
            Hyperbolic plane in the Upper Half Plane Model
        """
    UHP = HyperbolicModelUHP
    UpperHalfPlane = UHP
    PD = HyperbolicModelPD
    PoincareDisk = PD
    KM = HyperbolicModelKM
    KleinDisk = KM
    HM = HyperbolicModelHM
    Hyperboloid = HM

class HyperbolicModels(Category_realization_of_parent):
    """
    The category of hyperbolic models of hyperbolic space.
    """
    def __init__(self, base) -> None:
        """
        Initialize the hyperbolic models of hyperbolic space.

        INPUT:

        - ``base`` -- a hyperbolic space

        TESTS::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicModels
            sage: H = HyperbolicPlane()
            sage: models = HyperbolicModels(H)
            sage: H.UHP() in models
            True
        """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicModels
            sage: H = HyperbolicPlane()
            sage: models = HyperbolicModels(H)
            sage: models.super_categories()
            [Category of metric spaces,
             Category of realizations of Hyperbolic plane]
        """
    class ParentMethods: ...
