from sage.manifolds.chart import Chart as Chart, RealChart as RealChart
from sage.manifolds.differentiable.chart import DiffChart as DiffChart, RealDiffChart as RealDiffChart
from sage.manifolds.differentiable.manifold_homset import DifferentiableManifoldHomset as DifferentiableManifoldHomset
from sage.manifolds.differentiable.scalarfield_algebra import DiffScalarFieldAlgebra as DiffScalarFieldAlgebra
from sage.manifolds.manifold_homset import TopologicalManifoldHomset as TopologicalManifoldHomset
from sage.manifolds.scalarfield_algebra import ScalarFieldAlgebra as ScalarFieldAlgebra
from sage.misc.fast_methods import Singleton as Singleton

class TopologicalStructure(Singleton):
    """
    The structure of a topological manifold over a general topological field.
    """
    chart = Chart
    name: str
    scalar_field_algebra = ScalarFieldAlgebra
    homset = TopologicalManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import TopologicalStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: TopologicalStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class RealTopologicalStructure(Singleton):
    """
    The structure of a topological manifold over `\\RR`.
    """
    chart = RealChart
    name: str
    scalar_field_algebra = ScalarFieldAlgebra
    homset = TopologicalManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import RealTopologicalStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: RealTopologicalStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class DifferentialStructure(Singleton):
    """
    The structure of a differentiable manifold over a general topological
    field.
    """
    chart = DiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import DifferentialStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: DifferentialStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class RealDifferentialStructure(Singleton):
    """
    The structure of a differentiable manifold over `\\RR`.
    """
    chart = RealDiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import RealDifferentialStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: RealDifferentialStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class PseudoRiemannianStructure(Singleton):
    """
    The structure of a pseudo-Riemannian manifold.
    """
    chart = RealDiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import PseudoRiemannianStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: PseudoRiemannianStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class RiemannianStructure(Singleton):
    """
    The structure of a Riemannian manifold.
    """
    chart = RealDiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import RiemannianStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: RiemannianStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class LorentzianStructure(Singleton):
    """
    The structure of a Lorentzian manifold.
    """
    chart = RealDiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import LorentzianStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: LorentzianStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """

class DegenerateStructure(Singleton):
    """
    The structure of a degenerate manifold.
    """
    chart = RealDiffChart
    name: str
    scalar_field_algebra = DiffScalarFieldAlgebra
    homset = DifferentiableManifoldHomset
    def subcategory(self, cat):
        """
        Return the subcategory of ``cat`` corresponding to the structure
        of ``self``.

        EXAMPLES::

            sage: from sage.manifolds.structure import DegenerateStructure
            sage: from sage.categories.manifolds import Manifolds
            sage: DegenerateStructure().subcategory(Manifolds(RR))
            Category of manifolds over Real Field with 53 bits of precision
        """
