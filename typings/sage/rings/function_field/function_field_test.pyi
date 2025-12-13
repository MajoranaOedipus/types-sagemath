import pytest
from _typeshed import Incomplete
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.function_field.constructor import FunctionField as FunctionField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

@pytest.fixture
def F(): ...
@pytest.fixture
def J(): ...
@pytest.fixture
def K(): ...
@pytest.fixture
def L(F): ...
@pytest.fixture
def M(K, R, S): ...
@pytest.fixture
def N(K): ...
@pytest.fixture
def O(L): ...
@pytest.fixture
def R(K): ...
@pytest.fixture
def S(K, R): ...
@pytest.fixture
def T(F): ...

pairs: Incomplete

def test_function_field_testsuite(ff, max_runs, request) -> None:
    """
    Run the TestSuite() on some function fields that are
    constructed in the documentation. They are slow, random, and not
    intended for end users. All of this makes them more appropriate to
    be run separately, here, than in the doctests.

    INPUT:

    The inputs are essentially all fixtures.

    - ``ff`` -- string; a function field fixture name
    - ``max_runs`` -- integer; the maxmimum number of times to
      repeat the test suite
    - ``request`` -- fixture; a pytest built-in

    """
