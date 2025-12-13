from sage.categories.manifolds import Manifolds as Manifolds
from sage.manifolds.differentiable.examples.euclidean import EuclideanSpace as EuclideanSpace
from sage.manifolds.differentiable.symplectic_form import SymplecticForm as SymplecticForm, SymplecticFormParal as SymplecticFormParal
from sage.rings.real_mpfr import RR as RR

class StandardSymplecticSpace(EuclideanSpace):
    """
    The vector space `\\RR^{2n}` equipped with its standard symplectic form.
    """
    def __init__(self, dimension: int, name: str | None = None, latex_name: str | None = None, coordinates: str = 'Cartesian', symbols: str | None = None, symplectic_name: str | None = 'omega', symplectic_latex_name: str | None = None, start_index: int = 1, base_manifold: StandardSymplecticSpace | None = None, names: tuple[str] | None = None) -> None:
        '''
        INPUT:

        - ``dimension`` -- dimension of the space over the real field (has to be even)
        - ``name`` -- name (symbol) given to the underlying vector space;
          if ``None``, the name will be set to ``\'Rn\'``, where ``n`` is the ``dimension``
        - ``latex_name`` -- LaTeX symbol to denote the underlying vector space;
          if ``None``, it is set to ``name``
        - ``coordinates`` -- (default: ``\'Cartesian\'``) the
          type of coordinates to be initialized at the Euclidean space
          creation; allowed values are

            - ``\'Cartesian\'`` (canonical coordinates on `\\RR^{2n}`)
            - ``\'polar\'`` for ``dimension=2`` only (see
                :meth:`~sage.manifolds.differentiable.examples.euclidean.EuclideanPlane.polar_coordinates`)

        - ``symbols`` -- the coordinate text symbols and LaTeX symbols, with the same conventions as the
            argument ``coordinates`` in :class:`~sage.manifolds.differentiable.chart.RealDiffChart`, namely
            ``symbols`` is a string of coordinate fields separated by a blank
            space, where each field contains the coordinate\'s text symbol and
            possibly the coordinate\'s LaTeX symbol (when the latter is different
            from the text symbol), both symbols being separated by a colon
            (``:``); if ``None``, the symbols will be automatically generated
            according to the value of ``coordinates``
        - ``symplectic_name`` -- name (symbol) given to the symplectic form
        - ``symplectic_latex_name`` -- LaTeX symbol to denote the symplectic form;
            if none is provided, it is set to ``symplectic_name``
        - ``start_index`` -- lower value of the range of
            indices used for "indexed objects" in the vector space, e.g.
            coordinates of a chart
        - ``base_manifold`` -- if not ``None``, the created object is then an open subset
            of ``base_manifold``
        - ``names`` -- (default: ``None``) unused argument, except if
            ``symbols`` is not provided; it must then be a tuple containing
            the coordinate symbols (this is guaranteed if the shortcut operator
            ``<,>`` is used)
            If ``names`` is specified, then ``dimension`` does not have to be specified.

        EXAMPLES:

        Standard symplectic form on `\\RR^2`::

            sage: M.<q, p> = manifolds.StandardSymplecticSpace(2, symplectic_name=\'omega\')
            sage: omega = M.symplectic_form()
            sage: omega.display()
            omega = -dq∧dp

        An isomomorphism of its tangent space (at any point) with an indefinite inner product space
        with distinguished basis::

            sage: Q_M_qp = omega[:]; Q_M_qp
            [ 0 -1]
            [ 1  0]
            sage: W_M_qp = VectorSpace(RR, 2, inner_product_matrix=Q_M_qp); W_M_qp
            Ambient quadratic space of dimension 2 over Real Field with 53 bits of precision
            Inner product matrix:
            [0.000000000000000 -1.00000000000000]
            [ 1.00000000000000 0.000000000000000]
            sage: T = M.tangent_space(M.point(), base_ring=RR); T
            Tangent space at Point on the Standard symplectic space R2
            sage: phi_M_qp = T.isomorphism_with_fixed_basis(T.default_basis(), codomain=W_M_qp); phi_M_qp
            Generic morphism:
            From: Tangent space at Point on the Standard symplectic space R2
            To:   Ambient quadratic space of dimension 2 over Real Field with 53 bits of precision
            Inner product matrix:
            [0.000000000000000 -1.00000000000000]
            [ 1.00000000000000 0.000000000000000]
        '''
    def symplectic_form(self) -> SymplecticForm:
        """
        Return the symplectic form.

        EXAMPLES:

        Standard symplectic form on `\\RR^2`::

            sage: M.<q, p> = manifolds.StandardSymplecticSpace(2, symplectic_name='omega')
            sage: omega = M.symplectic_form()
            sage: omega.display()
            omega = -dq∧dp
        """
