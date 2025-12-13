from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.chain_complexes import ChainComplexes as ChainComplexes
from sage.categories.graded_algebras import GradedAlgebras as GradedAlgebras
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.manifolds.differentiable.mixed_form import MixedForm as MixedForm
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.symbolic.ring import SR as SR

class MixedFormAlgebra(Parent, UniqueRepresentation):
    """
    An instance of this class represents the graded algebra of mixed forms.
    That is, if `\\varphi: M \\to N` is a differentiable map between two
    differentiable manifolds `M` and `N`, the *graded algebra of mixed forms*
    `\\Omega^*(M,\\varphi)` *along* `\\varphi` is defined via the direct sum
    `\\bigoplus^{n}_{j=0} \\Omega^j(M,\\varphi)` consisting of differential form
    modules
    (cf. :class:`~sage.manifolds.differentiable.diff_form_module.DiffFormModule`),
    where `n` is the dimension of `N`. Hence, `\\Omega^*(M,\\varphi)` is a module
    over `C^k(M)` and a vector space over `\\RR` or `\\CC`. Furthermore notice,
    that

    .. MATH::

        \\Omega^*(M,\\varphi) \\cong C^k \\left( \\bigoplus^n_{j=0} \\Lambda^j(\\varphi^*T^*N) \\right),

    where `C^k` denotes the global section functor for differentiable sections
    of order `k` here.

    The wedge product induces a multiplication on `\\Omega^*(M,\\varphi)` and
    gives it the structure of a graded algebra since

    .. MATH::

        \\Omega^k(M,\\varphi) \\wedge \\Omega^l(M,\\varphi) \\subset \\Omega^{k+l}(M,\\varphi).

    Moreover, `\\Omega^*(M,\\varphi)` inherits the structure of a chain complex,
    called *de Rham complex*, with the exterior derivative as boundary map,
    that is

    .. MATH::

        0 \\rightarrow \\Omega^0(M,\\varphi) \\xrightarrow{\\mathrm{d}_0}
            \\Omega^1(M,\\varphi) \\xrightarrow{\\mathrm{d}_1} \\dots
            \\xrightarrow{\\mathrm{d}_{n-1}} \\Omega^n(M,\\varphi)
            \\xrightarrow{\\mathrm{d}_{n}} 0.

    The induced cohomology is called *de Rham cohomology*, see
    :meth:`cohomology` or
    :class:`~sage.manifolds.differentiable.de_rham_cohomology.DeRhamCohomologyRing`
    respectively.

    INPUT:

    - ``vector_field_module`` -- module `\\mathfrak{X}(M,\\varphi)` of vector
      fields along `M` associated with the map `\\varphi: M \\rightarrow N`

    EXAMPLES:

    Graded algebra of mixed forms on a 3-dimensional manifold::

        sage: M = Manifold(3, 'M')
        sage: X.<x,y,z> = M.chart()
        sage: Omega = M.mixed_form_algebra(); Omega
        Graded algebra Omega^*(M) of mixed differential forms on the
         3-dimensional differentiable manifold M
        sage: Omega.category()
        Join of Category of graded algebras over Symbolic Ring and Category of
         chain complexes over Symbolic Ring
        sage: Omega.base_ring()
        Symbolic Ring
        sage: Omega.vector_field_module()
        Free module X(M) of vector fields on the 3-dimensional differentiable
         manifold M

    Elements can be created from scratch::

        sage: A = Omega(0); A
        Mixed differential form zero on the 3-dimensional differentiable
         manifold M
        sage: A is Omega.zero()
        True
        sage: B = Omega(1); B
        Mixed differential form one on the 3-dimensional differentiable
         manifold M
        sage: B is Omega.one()
        True
        sage: C = Omega([2,0,0,0]); C
        Mixed differential form on the 3-dimensional differentiable manifold M

    There are some important coercions implemented::

        sage: Omega0 = M.scalar_field_algebra(); Omega0
        Algebra of differentiable scalar fields on the 3-dimensional
         differentiable manifold M
        sage: Omega.has_coerce_map_from(Omega0)
        True
        sage: Omega2 = M.diff_form_module(2); Omega2
        Free module Omega^2(M) of 2-forms on the 3-dimensional differentiable
         manifold M
        sage: Omega.has_coerce_map_from(Omega2)
        True

    Restrictions induce coercions as well::

        sage: U = M.open_subset('U'); U
        Open subset U of the 3-dimensional differentiable manifold M
        sage: OmegaU = U.mixed_form_algebra(); OmegaU
        Graded algebra Omega^*(U) of mixed differential forms on the Open
         subset U of the 3-dimensional differentiable manifold M
        sage: OmegaU.has_coerce_map_from(Omega)
        True
    """
    Element = MixedForm
    def __init__(self, vector_field_module) -> None:
        """
        Construct a graded algebra of mixed forms.

        TESTS:

        Graded algebra of mixed forms on a non-parallelizable 2-dimensional
        manifold::

            sage: M = Manifold(2, 'M')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: transf = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                   intersection_name='W', restrictions1= x>0,
            ....:                   restrictions2= u+v>0)
            sage: inv = transf.inverse()
            sage: from sage.manifolds.differentiable.mixed_form_algebra \\\n            ....:                                       import MixedFormAlgebra
            sage: A = MixedFormAlgebra(M.vector_field_module())
            sage: TestSuite(A).run()
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: A = M.mixed_form_algebra()
            sage: A.zero()
            Mixed differential form zero on the 3-dimensional differentiable
             manifold M
        """
    @cached_method
    def one(self):
        """
        Return the one of ``self``.

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: A = M.mixed_form_algebra()
            sage: A.one()
            Mixed differential form one on the 3-dimensional differentiable
             manifold M
        """
    def vector_field_module(self):
        """
        Return the underlying vector field module.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: N = Manifold(3, 'N')
            sage: Phi = M.diff_map(N, name='Phi'); Phi
            Differentiable map Phi from the 2-dimensional differentiable
             manifold M to the 3-dimensional differentiable manifold N
            sage: A = M.mixed_form_algebra(Phi); A
            Graded algebra Omega^*(M,Phi) of mixed differential forms along the
             2-dimensional differentiable manifold M mapped into the
             3-dimensional differentiable manifold N via Phi
            sage: A.vector_field_module()
            Module X(M,Phi) of vector fields along the 2-dimensional
             differentiable manifold M mapped into the 3-dimensional
             differentiable manifold N
        """
    def differential(self, degree=None):
        """
        Return the differential of the de Rham complex ``self`` given by the
        exterior derivative.

        INPUT:

        - ``degree`` -- (default: ``None``) degree of the differential
          operator; if none is provided, the differential operator on
          ``self`` is returned.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: d = C.differential(); d
            Generic endomorphism of Graded algebra Omega^*(M) of mixed
             differential forms on the 2-dimensional differentiable manifold M
            sage: d0 = C.differential(0); d0
            Generic morphism:
              From: Algebra of differentiable scalar fields on the
               2-dimensional differentiable manifold M
              To:   Free module Omega^1(M) of 1-forms on the 2-dimensional
               differentiable manifold M
            sage: f = M.scalar_field(x, name='f'); f.display()
            f: M → ℝ
               (x, y) ↦ x
            sage: d0(f).display()
            df = dx
        """
    def cohomology(self, *args, **kwargs):
        """
        Return the de Rham cohomology of the de Rham complex ``self``.

        The `k`-th de Rham cohomology is given by

        .. MATH::

            H^k_{\\mathrm{dR}}(M, \\varphi) =
                \\left. \\mathrm{ker}(\\mathrm{d}_k) \\middle/
                \\mathrm{im}(\\mathrm{d}_{k-1}) \\right. .

        The corresponding ring is given by

        .. MATH::

            H^*_{\\mathrm{dR}}(M, \\varphi) = \\bigoplus^n_{k=0} H^k_{\\mathrm{dR}}(M, \\varphi),

        endowed with the cup product as multiplication induced by the wedge
        product.

        .. SEEALSO::

            See :class:`~sage.manifolds.differentiable.de_rham_cohomology.DeRhamCohomologyRing`
            for details.

        EXAMPLES::

            sage: M = Manifold(3, 'M', latex_name=r'\\mathcal{M}')
            sage: A = M.mixed_form_algebra()
            sage: A.cohomology()
            De Rham cohomology ring on the 3-dimensional differentiable
             manifold M
        """
    homology = cohomology
    def irange(self, start=None) -> Generator[Incomplete]:
        """
        Single index generator.

        INPUT:

        - ``start`` -- (default: ``None``) initial value `i_0` of the index
          between 0 and `n`, where `n` is the manifold's dimension; if none is
          provided, the value 0 is assumed

        OUTPUT:

        - an iterable index, starting from `i_0` and ending at
          `n`, where `n` is the manifold's dimension

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: A = M.mixed_form_algebra()
            sage: list(A.irange())
            [0, 1, 2, 3]
            sage: list(A.irange(2))
            [2, 3]
        """
    def lift_from_homology(self, x):
        """
        Lift a cohomology class to the algebra of mixed differential forms.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: alpha = M.diff_form(1, [1,1], name='alpha')
            sage: alpha.display()
            alpha = dx + dy
            sage: a = H(alpha); a
            [alpha]
            sage: C.lift_from_homology(a)
            Mixed differential form alpha on the 2-dimensional differentiable
             manifold M
        """
