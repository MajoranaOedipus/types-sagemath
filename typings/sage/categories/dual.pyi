from sage.categories.covariant_functorial_construction import CovariantConstructionCategory as CovariantConstructionCategory, CovariantFunctorialConstruction as CovariantFunctorialConstruction

class DualFunctor(CovariantFunctorialConstruction):
    """
    A singleton class for the dual functor
    """
    symbol: str

class DualObjectsCategory(CovariantConstructionCategory): ...
