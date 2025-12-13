from .chain_complex import ChainComplex as ChainComplex
from .chain_complex_morphism import ChainComplexMorphism as ChainComplexMorphism
from .chain_homotopy import ChainContraction as ChainContraction
from sage.matrix.constructor import matrix as matrix, zero_matrix as zero_matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.rational_field import QQ as QQ

def algebraic_topological_model(K, base_ring=None):
    """
    Algebraic topological model for cell complex ``K``
    with coefficients in the field ``base_ring``.

    INPUT:

    - ``K`` -- either a simplicial complex or a cubical complex
    - ``base_ring`` -- coefficient ring; must be a field

    OUTPUT: a pair ``(phi, M)`` consisting of

    - chain contraction ``phi``
    - chain complex `M`

    This construction appears in a paper by Pilarczyk and Réal [PR2015]_.
    Given a cell complex `K` and a field `F`, there is a chain complex
    `C` associated to `K` with coefficients in `F`. The *algebraic
    topological model* for `K` is a chain complex `M` with trivial
    differential, along with chain maps `\\pi: C \\to M` and `\\iota: M
    \\to C` such that

    - `\\pi \\iota = 1_M`, and
    - there is a chain homotopy `\\phi` between `1_C` and `\\iota \\pi`.

    In particular, `\\pi` and `\\iota` induce isomorphisms on homology,
    and since `M` has trivial differential, it is its own homology,
    and thus also the homology of `C`. Thus `\\iota` lifts homology
    classes to their cycle representatives.

    The chain homotopy `\\phi` satisfies some additional properties,
    making it a *chain contraction*:

    - `\\phi \\phi = 0`,
    - `\\pi \\phi = 0`,
    - `\\phi \\iota = 0`.

    Given an algebraic topological model for `K`, it is then easy to
    compute cup products and cohomology operations on the cohomology
    of `K`, as described in [GDR2003]_ and [PR2015]_.

    Implementation details: the cell complex `K` must have an
    :meth:`~sage.topology.cell_complex.GenericCellComplex.n_cells`
    method from which we can extract a list of cells in each
    dimension. Combining the lists in increasing order of dimension
    then defines a filtration of the complex: a list of cells in which
    the boundary of each cell consists of cells earlier in the
    list. This is required by Pilarczyk and Réal's algorithm.  There
    must also be a
    :meth:`~sage.topology.cell_complex.GenericCellComplex.chain_complex`
    method, to construct the chain complex `C` associated to this
    chain complex.

    In particular, this works for simplicial complexes and cubical
    complexes. It doesn't work for `\\Delta`-complexes, though: the list
    of their `n`-cells has the wrong format.

    Note that from the chain contraction ``phi``, one can recover the
    chain maps `\\pi` and `\\iota` via ``phi.pi()`` and
    ``phi.iota()``. Then one can recover `C` and `M` from, for
    example, ``phi.pi().domain()`` and ``phi.pi().codomain()``,
    respectively.

    EXAMPLES::

        sage: from sage.homology.algebraic_topological_model import algebraic_topological_model
        sage: RP2 = simplicial_complexes.RealProjectivePlane()
        sage: phi, M = algebraic_topological_model(RP2, GF(2))
        sage: M.homology()
        {0: Vector space of dimension 1 over Finite Field of size 2,
         1: Vector space of dimension 1 over Finite Field of size 2,
         2: Vector space of dimension 1 over Finite Field of size 2}
        sage: T = cubical_complexes.Torus()
        sage: phi, M = algebraic_topological_model(T, QQ)
        sage: M.homology()
        {0: Vector space of dimension 1 over Rational Field,
         1: Vector space of dimension 2 over Rational Field,
         2: Vector space of dimension 1 over Rational Field}

    If you want to work with cohomology rather than homology, just
    dualize the outputs of this function::

        sage: M.dual().homology()
        {0: Vector space of dimension 1 over Rational Field,
         1: Vector space of dimension 2 over Rational Field,
         2: Vector space of dimension 1 over Rational Field}
        sage: M.dual().degree_of_differential()
        1
        sage: phi.dual()
        Chain homotopy between:
          Chain complex endomorphism of
            Chain complex with at most 3 nonzero terms over Rational Field
          and Chain complex morphism:
            From: Chain complex with at most 3 nonzero terms over Rational Field
            To:   Chain complex with at most 3 nonzero terms over Rational Field

    In degree 0, the inclusion of the homology `M` into the chain
    complex `C` sends the homology generator to a single vertex::

        sage: K = simplicial_complexes.Simplex(2)
        sage: phi, M = algebraic_topological_model(K, QQ)
        sage: phi.iota().in_degree(0)
        [0]
        [0]
        [1]

    In cohomology, though, one needs the dual of every degree 0 cell
    to detect the degree 0 cohomology generator::

        sage: phi.dual().iota().in_degree(0)
        [1]
        [1]
        [1]

    TESTS::

        sage: T = cubical_complexes.Torus()
        sage: C = T.chain_complex()
        sage: H, M = T.algebraic_topological_model()
        sage: C.differential(1) * H.iota().in_degree(1).column(0) == 0
        True
        sage: C.differential(1) * H.iota().in_degree(1).column(1) == 0
        True
        sage: coC = T.chain_complex(cochain=True)
        sage: coC.differential(1) * H.dual().iota().in_degree(1).column(0) == 0
        True
        sage: coC.differential(1) * H.dual().iota().in_degree(1).column(1) == 0
        True
    """
def algebraic_topological_model_delta_complex(K, base_ring=None):
    '''
    Algebraic topological model for cell complex ``K``
    with coefficients in the field ``base_ring``.

    This has the same basic functionality as
    :func:`algebraic_topological_model`, but it also works for
    `\\Delta`-complexes. For simplicial and cubical complexes it is
    somewhat slower, though.

    INPUT:

    - ``K`` -- a simplicial complex, a cubical complex, or a
      `\\Delta`-complex
    - ``base_ring`` -- coefficient ring; must be a field

    OUTPUT: a pair ``(phi, M)`` consisting of

    - chain contraction ``phi``
    - chain complex `M`

    See :func:`algebraic_topological_model` for the main
    documentation. The difference in implementation between the two:
    this uses matrix and vector algebra. The other function does more
    of the computations "by hand" and uses cells (given as simplices
    or cubes) to index various dictionaries. Since the cells in
    `\\Delta`-complexes are not as nice, the other function does not
    work for them, while this function relies almost entirely on the
    structure of the associated chain complex.

    EXAMPLES::

        sage: from sage.homology.algebraic_topological_model import algebraic_topological_model_delta_complex as AT_model
        sage: RP2 = simplicial_complexes.RealProjectivePlane()
        sage: phi, M = AT_model(RP2, GF(2))
        sage: M.homology()
        {0: Vector space of dimension 1 over Finite Field of size 2,
         1: Vector space of dimension 1 over Finite Field of size 2,
         2: Vector space of dimension 1 over Finite Field of size 2}
        sage: T = delta_complexes.Torus()
        sage: phi, M = AT_model(T, QQ)
        sage: M.homology()
        {0: Vector space of dimension 1 over Rational Field,
         1: Vector space of dimension 2 over Rational Field,
         2: Vector space of dimension 1 over Rational Field}

    If you want to work with cohomology rather than homology, just
    dualize the outputs of this function::

        sage: M.dual().homology()
        {0: Vector space of dimension 1 over Rational Field,
         1: Vector space of dimension 2 over Rational Field,
         2: Vector space of dimension 1 over Rational Field}
        sage: M.dual().degree_of_differential()
        1
        sage: phi.dual()
        Chain homotopy between:
          Chain complex endomorphism of Chain complex with at most 3 nonzero terms over Rational Field
          and Chain complex morphism:
            From: Chain complex with at most 3 nonzero terms over Rational Field
            To:   Chain complex with at most 3 nonzero terms over Rational Field

    In degree 0, the inclusion of the homology `M` into the chain
    complex `C` sends the homology generator to a single vertex::

        sage: K = delta_complexes.Simplex(2)
        sage: phi, M = AT_model(K, QQ)
        sage: phi.iota().in_degree(0)
        [0]
        [0]
        [1]

    In cohomology, though, one needs the dual of every degree 0 cell
    to detect the degree 0 cohomology generator::

        sage: phi.dual().iota().in_degree(0)
        [1]
        [1]
        [1]

    TESTS::

        sage: T = cubical_complexes.Torus()
        sage: C = T.chain_complex()
        sage: H, M = AT_model(T, QQ)
        sage: C.differential(1) * H.iota().in_degree(1).column(0) == 0
        True
        sage: C.differential(1) * H.iota().in_degree(1).column(1) == 0
        True
        sage: coC = T.chain_complex(cochain=True)
        sage: coC.differential(1) * H.dual().iota().in_degree(1).column(0) == 0
        True
        sage: coC.differential(1) * H.dual().iota().in_degree(1).column(1) == 0
        True
    '''
