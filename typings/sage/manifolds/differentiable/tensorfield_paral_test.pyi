import pytest
from sage.manifolds.differentiable.examples.euclidean import EuclideanSpace as EuclideanSpace
from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold

class TestR3VectorSpace:
    @pytest.fixture
    def manifold(self): ...
    def test_trace_using_metric_works(self, manifold: DifferentiableManifold): ...
