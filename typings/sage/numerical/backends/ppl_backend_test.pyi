import pytest
from sage.numerical.backends.generic_backend import GenericBackend as GenericBackend
from sage.numerical.backends.generic_backend_test import GenericBackendTests as GenericBackendTests
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram

class TestPPLBackend(GenericBackendTests):
    @pytest.fixture
    def backend(self) -> GenericBackend: ...
