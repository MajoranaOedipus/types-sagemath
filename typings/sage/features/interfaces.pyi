from . import Feature as Feature, FeatureTestResult as FeatureTestResult, PythonModule as PythonModule
from _typeshed import Incomplete

class InterfaceFeature(Feature):
    '''
    A :class:`~sage.features.Feature` describing whether an :class:`~sage.interfaces.interface.Interface` is present and functional.

    TESTS::

        sage: from sage.features.interfaces import InterfaceFeature
        sage: broken = InterfaceFeature("broken_interface", "sage.interfaces.does_not_exist")
        sage: broken.is_present()
        FeatureTestResult(\'sage.interfaces.does_not_exist\', False)
        sage: _.reason
        "Failed to import `sage.interfaces.does_not_exist`: No module named \'sage.interfaces.does_not_exist\'"

        sage: also_broken = InterfaceFeature("also_broken_interface", "sage.interfaces.interface")
        sage: also_broken.is_present()
        FeatureTestResult(\'also_broken_interface\', False)
        sage: _.reason
        "Interface also_broken_interface cannot be imported: module \'sage.interfaces.interface\' has no attribute \'also_broken_interface\'"
    '''
    @staticmethod
    def __classcall__(cls, name, module, description=None):
        '''
        TESTS::

            sage: from sage.features import PythonModule
            sage: from sage.features.interfaces import InterfaceFeature
            sage: f = InterfaceFeature("test_interface", "sage.interfaces.interface")
            sage: f is InterfaceFeature("test_interface", PythonModule("sage.interfaces.interface"))
            True
        '''
    module: Incomplete
    def __init__(self, name, module, description) -> None:
        '''
        TESTS::

            sage: from sage.features.interfaces import InterfaceFeature
            sage: f = InterfaceFeature("test_interface", "sage.interfaces.interface")
            sage: isinstance(f, InterfaceFeature)
            True
        '''

class Mathics(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.mathics.Mathics`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Mathics
        sage: Mathics().is_present()  # not tested
        FeatureTestResult('mathics', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Magma(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.magma.Magma`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Magma
        sage: Magma().is_present()  # random
        FeatureTestResult('magma', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Matlab(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.matlab.Matlab`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Matlab
        sage: Matlab().is_present()  # random
        FeatureTestResult('matlab', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Mathematica(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.mathematica.Mathematica`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Mathematica
        sage: Mathematica().is_present()  # not tested
        FeatureTestResult('mathematica', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Maple(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.maple.Maple`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Maple
        sage: Maple().is_present()  # random
        FeatureTestResult('maple', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Macaulay2(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.macaulay2.Macaulay2`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Macaulay2
        sage: Macaulay2().is_present()  # random
        FeatureTestResult('macaulay2', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Octave(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.octave.Octave`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Octave
        sage: Octave().is_present()  # random
        FeatureTestResult('octave', False)
    """
    @staticmethod
    def __classcall__(cls): ...

class Scilab(InterfaceFeature):
    """
    A :class:`~sage.features.Feature` describing whether :class:`sage.interfaces.scilab.Scilab`
    is present and functional.

    EXAMPLES::

        sage: from sage.features.interfaces import Scilab
        sage: Scilab().is_present()  # random
        FeatureTestResult('scilab', False)
    """
    @staticmethod
    def __classcall__(cls): ...

def all_features():
    """
    Return features corresponding to interpreter interfaces.

    EXAMPLES::

        sage: from sage.features.interfaces import all_features
        sage: list(all_features())
        [Feature('magma'),
         Feature('matlab'),
         Feature('mathematica'),
         Feature('mathics'),
         Feature('maple'),
         Feature('macaulay2'),
         Feature('octave'),
         Feature('scilab')]
    """
