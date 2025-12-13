import pytest
from sage.numerical.backends.generic_backend import GenericBackend as GenericBackend
from sage.numerical.backends.generic_backend_test import GenericBackendTests as GenericBackendTests
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram
from sage.structure.sage_object import SageObject as SageObject

class TestCVXOPTBackend(GenericBackendTests):
    @pytest.fixture
    def backend(self) -> GenericBackend: ...
    def test_sage_unittest_testsuite(self, sage_object: SageObject): ...
