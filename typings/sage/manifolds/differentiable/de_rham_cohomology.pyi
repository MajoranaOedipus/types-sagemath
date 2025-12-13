from sage.categories.algebras import Algebras as Algebras
from sage.manifolds.differentiable.characteristic_cohomology_class import CharacteristicCohomologyClassRing as CharacteristicCohomologyClassRing, CharacteristicCohomologyClassRingElement as CharacteristicCohomologyClassRingElement
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import AlgebraElement as AlgebraElement
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DeRhamCohomologyClass(AlgebraElement):
    """
    Define a cohomology class in the de Rham cohomology ring.

    INPUT:

    - ``parent`` -- de Rham cohomology ring represented by an instance of
      :class:`DeRhamCohomologyRing`
    - ``representative`` -- a closed (mixed) differential form representing the
      cohomology class

    .. NOTE::

        The current implementation only provides basic features. Comparison via
        exact forms are not supported at the time being.

    EXAMPLES::

        sage: M = Manifold(2, 'M')
        sage: X.<x,y> = M.chart()
        sage: C = M.de_rham_complex()
        sage: H = C.cohomology()
        sage: omega = M.diff_form(1, [1,1], name='omega')
        sage: u = H(omega); u
        [omega]

    Cohomology classes can be lifted to the algebra of mixed differential
    forms::

        sage: u.lift()
        Mixed differential form omega on the 2-dimensional differentiable
         manifold M

    However, comparison of two cohomology classes is limited the time being::

        sage: eta = M.diff_form(1, [1,1], name='eta')
        sage: H(eta) == u
        True
        sage: H.one() == u
        Traceback (most recent call last):
        ...
        NotImplementedError: comparison via exact forms is currently not supported
    """
    def __init__(self, parent, representative) -> None:
        """
        Construct an element of the de Rham cohomology ring.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: omega = M.diff_form(1, [1,1], name='omega', latex_name=r'\\omega')
            sage: u = H(omega)
            sage: TestSuite(u).run(skip=['_test_eq', '_test_nonzero_equal'])  # equality not fully supported yet
        """
    def representative(self):
        """
        Return a representative of ``self`` in the associated de Rham
        complex.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: omega = M.diff_form(2, name='omega')
            sage: omega[0,1] = x
            sage: omega.display()
            omega = x dx∧dy
            sage: u = H(omega); u
            [omega]
            sage: u.representative()
            Mixed differential form omega on the 2-dimensional differentiable
             manifold M
        """
    lift = representative
    def cup(self, other):
        """
        Cup product of two cohomology classes.

        INPUT:

        - ``other`` -- another cohomology class in the de Rham cohomology

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: omega = M.diff_form(1, [1,1], name='omega')
            sage: eta = M.diff_form(1, [1,-1], name='eta')
            sage: H(omega).cup(H(eta))
            [omega∧eta]
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        .. WARNING::

            At current stage, the equality operator only checks whether the
            representatives are equal. No further checks are supported so far.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: omega = M.diff_form(1, [1,1], name='omega')
            sage: eta = M.diff_form(1, [1,1], name='eta')
            sage: H(omega) == H(eta)
            True
            sage: H(omega) == H.one()
            Traceback (most recent call last):
            ...
            NotImplementedError: comparison via exact forms is currently not supported
        """

class DeRhamCohomologyRing(Parent, UniqueRepresentation):
    """
    The de Rham cohomology ring of a de Rham complex.

    This ring is naturally endowed with a multiplication induced by the wedge
    product, called *cup product*, see :meth:`DeRhamCohomologyClass.cup`.

    .. NOTE::

        The current implementation only provides basic features. Comparison via
        exact forms are not supported at the time being.

    INPUT:

    - ``de_rham_complex`` -- a de Rham complex, typically an instance of
      :class:`~sage.manifolds.differentiable.mixed_form_algebra.MixedFormAlgebra`

    EXAMPLES:

    We define the de Rham cohomology ring on a parallelizable manifold `M`::

        sage: M = Manifold(2, 'M')
        sage: X.<x,y> = M.chart()
        sage: C = M.de_rham_complex()
        sage: H = C.cohomology(); H
        De Rham cohomology ring on the 2-dimensional differentiable manifold M

    Its elements are induced by closed differential forms on `M`::

        sage: beta = M.diff_form(1, [1,0], name='beta')
        sage: beta.display()
        beta = dx
        sage: d1 = C.differential(1)
        sage: d1(beta).display()
        dbeta = 0
        sage: b = H(beta); b
        [beta]

    Cohomology classes can be lifted to the algebra of mixed differential
    forms::

        sage: b.representative()
        Mixed differential form beta on the 2-dimensional differentiable
         manifold M

    The ring admits a zero and unit element::

        sage: H.zero()
        [zero]
        sage: H.one()
        [one]
    """
    def __init__(self, de_rham_complex) -> None:
        """
        Construct the de Rham cohomology ring.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology(); H
            De Rham cohomology ring on the 2-dimensional differentiable
             manifold M
            sage: TestSuite(H).run(skip=['_test_elements',
            ....:                        '_test_elements_eq_symmetric',
            ....:                       '_test_elements_eq_transitive',
            ....:                       '_test_elements_neq'])  # equality not fully supported yet
        """
    Element = DeRhamCohomologyClass
    @cached_method
    def zero(self):
        """
        Return the zero element of ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: H.zero()
            [zero]
            sage: H.zero().representative()
            Mixed differential form zero on the 2-dimensional differentiable
             manifold M
        """
    @cached_method
    def one(self):
        """
        Return the one element of ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: C = M.de_rham_complex()
            sage: H = C.cohomology()
            sage: H.one()
            [one]
            sage: H.one().representative()
            Mixed differential form one on the 2-dimensional differentiable
             manifold M
        """
