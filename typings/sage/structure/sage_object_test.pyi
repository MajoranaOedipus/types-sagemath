import pytest
from sage.structure.sage_object import SageObject as SageObject

class SageObjectTests:
    @pytest.fixture
    def sage_object(self, *args, **kwargs) -> SageObject: ...
    def test_sage_unittest_testsuite(self, sage_object: SageObject):
        """
        Subclasses should override this method if they need to skip some tests.
        """
