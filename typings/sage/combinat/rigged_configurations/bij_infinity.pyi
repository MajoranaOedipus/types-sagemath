from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.combinat.crystals.letters import CrystalOfLetters as CrystalOfLetters
from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_B import KRTToRCBijectionTypeB as KRTToRCBijectionTypeB, RCToKRTBijectionTypeB as RCToKRTBijectionTypeB
from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC as KRTToRCBijectionTypeC, RCToKRTBijectionTypeC as RCToKRTBijectionTypeC
from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD as KRTToRCBijectionTypeD, RCToKRTBijectionTypeD as RCToKRTBijectionTypeD
from sage.combinat.rigged_configurations.rigged_configurations import RiggedConfigurations as RiggedConfigurations
from sage.combinat.rigged_configurations.tensor_product_kr_tableaux import TensorProductOfKirillovReshetikhinTableaux as TensorProductOfKirillovReshetikhinTableaux
from sage.misc.flatten import flatten as flatten

class FromTableauIsomorphism(Morphism):
    """
    Crystal isomorphism of `B(\\infty)` in the tableau model to the
    rigged configuration model.
    """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: RC = crystals.infinity.RiggedConfigurations(['A',3])
            sage: T = crystals.infinity.Tableaux(['A',3])
            sage: phi = RC.coerce_map_from(T)
            sage: ~phi
            Crystal Isomorphism morphism:
              From: The infinity crystal of rigged configurations of type ['A', 3]
              To:   The infinity crystal of tableaux of type ['A', 3]
        """

class FromRCIsomorphism(Morphism):
    """
    Crystal isomorphism of `B(\\infty)` in the rigged configuration model
    to the tableau model.
    """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: T = crystals.infinity.Tableaux(['A',3])
            sage: RC = crystals.infinity.RiggedConfigurations(['A',3])
            sage: phi = T.coerce_map_from(RC)
            sage: ~phi
            Crystal Isomorphism morphism:
              From: The infinity crystal of tableaux of type ['A', 3]
              To:   The infinity crystal of rigged configurations of type ['A', 3]
        """

class MLTToRCBijectionTypeB(KRTToRCBijectionTypeB):
    def run(self):
        """
        Run the bijection from a marginally large tableaux to a rigged
        configuration.

        EXAMPLES::

            sage: vct = CartanType(['B',4]).as_folding()
            sage: RC = crystals.infinity.RiggedConfigurations(vct)
            sage: T = crystals.infinity.Tableaux(['B',4])
            sage: Psi = T.crystal_morphism({T.module_generators[0]: RC.module_generators[0]})
            sage: TS = [x.value for x in T.subcrystal(max_depth=4)]
            sage: all(Psi(b) == RC(b) for b in TS) # long time # indirect doctest
            True
        """

class RCToMLTBijectionTypeB(RCToKRTBijectionTypeB):
    def run(self):
        """
        Run the bijection from rigged configurations to a marginally large
        tableau.

        EXAMPLES::

            sage: vct = CartanType(['B',4]).as_folding()
            sage: RC = crystals.infinity.RiggedConfigurations(vct)
            sage: T = crystals.infinity.Tableaux(['B',4])
            sage: Psi = RC.crystal_morphism({RC.module_generators[0]: T.module_generators[0]})
            sage: RCS = [x.value for x in RC.subcrystal(max_depth=4)]
            sage: all(Psi(nu) == T(nu) for nu in RCS) # long time # indirect doctest
            True
        """

class MLTToRCBijectionTypeD(KRTToRCBijectionTypeD):
    def run(self):
        """
        Run the bijection from a marginally large tableaux to a rigged
        configuration.

        EXAMPLES::

            sage: RC = crystals.infinity.RiggedConfigurations(['D',4])
            sage: T = crystals.infinity.Tableaux(['D',4])
            sage: Psi = T.crystal_morphism({T.module_generators[0]: RC.module_generators[0]})
            sage: TS = [x.value for x in T.subcrystal(max_depth=4)]
            sage: all(Psi(b) == RC(b) for b in TS) # long time # indirect doctest
            True
        """

class RCToMLTBijectionTypeD(RCToKRTBijectionTypeD):
    def run(self):
        """
        Run the bijection from rigged configurations to a marginally large
        tableau.

        EXAMPLES::

            sage: RC = crystals.infinity.RiggedConfigurations(['D',4])
            sage: T = crystals.infinity.Tableaux(['D',4])
            sage: Psi = RC.crystal_morphism({RC.module_generators[0]: T.module_generators[0]})
            sage: RCS = [x.value for x in RC.subcrystal(max_depth=4)]
            sage: all(Psi(nu) == T(nu) for nu in RCS) # long time # indirect doctest
            True
        """
