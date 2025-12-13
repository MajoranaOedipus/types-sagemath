from sage.homology.homology_group import HomologyGroup as HomologyGroup
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix0 import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import ModuleElement as ModuleElement, Vector as Vector, coercion_model as coercion_model
from sage.structure.parent import Parent as Parent

def ChainComplex(data=None, base_ring=None, grading_group=None, degree_of_differential: int = 1, degree: int = 1, check: bool = True):
    """
    Define a chain complex.

    INPUT:

    - ``data`` -- the data defining the chain complex; see below for
      more details

    The following keyword arguments are supported:

    - ``base_ring`` -- a commutative ring (optional); the ring over
      which the chain complex is defined. If this is not specified,
      it is determined by the data defining the chain complex.

    - ``grading_group`` -- a additive free abelian group (optional,
      default ``ZZ``); the group over which the chain complex is
      indexed

    - ``degree_of_differential`` -- element of grading_group
      (default: ``1``); the degree of the differential

    - ``degree`` -- alias for ``degree_of_differential``

    - ``check`` -- boolean (default: ``True``); if ``True``,
      check that each consecutive pair of differentials are
      composable and have composite equal to zero

    OUTPUT: a chain complex

    .. WARNING::

       Right now, homology calculations will only work if the base
       ring is either `\\ZZ` or a field, so please take this into account
       when defining a chain complex.

    Use data to define the chain complex.  This may be in any of the
    following forms.

    1. a dictionary with integers (or more generally, elements of
       grading_group) for keys, and with ``data[n]`` a matrix representing
       (via left multiplication) the differential coming from degree
       `n`.  (Note that the shape of the matrix then determines the
       rank of the free modules `C_n` and `C_{n+d}`.)

    2. a list/tuple/iterable of the form `[C_0, d_0, C_1, d_1, C_2,
       d_2, ...]`, where each `C_i` is a free module and each `d_i` is
       a matrix, as above.  This only makes sense if ``grading_group``
       is `\\ZZ` and ``degree`` is 1.

    3. a list/tuple/iterable of the form `[r_0, d_0, r_1, d_1, r_2,
       d_2, \\ldots]`, where `r_i` is the rank of the free module `C_i`
       and each `d_i` is a matrix, as above.  This only makes sense if
       ``grading_group`` is `\\ZZ` and ``degree`` is 1.

    4. a list/tuple/iterable of the form `[d_0, d_1, d_2, \\ldots]` where
       each `d_i` is a matrix, as above.  This only makes sense if
       ``grading_group`` is `\\ZZ` and ``degree`` is 1.

    .. NOTE::

       In fact, the free modules `C_i` in case 2 and the ranks `r_i`
       in case 3 are ignored: only the matrices are kept, and from
       their shapes, the ranks of the modules are determined.
       (Indeed, if ``data`` is a list or tuple, then any element which
       is not a matrix is discarded; thus the list may have any number
       of different things in it, and all of the non-matrices will be
       ignored.)  No error checking is done to make sure, for
       instance, that the given modules have the appropriate ranks for
       the given matrices.  However, as long as ``check`` is True, the
       code checks to see if the matrices are composable and that each
       appropriate composite is zero.

    If the base ring is not specified, then the matrices are examined
    to determine a ring over which they are all naturally defined, and
    this becomes the base ring for the complex.  If no such ring can
    be found, an error is raised.  If the base ring is specified, then
    the matrices are converted automatically to this ring when
    defining the chain complex.  If some matrix cannot be converted,
    then an error is raised.

    EXAMPLES::

        sage: ChainComplex()
        Trivial chain complex over Integer Ring

        sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
        sage: C
        Chain complex with at most 2 nonzero terms over Integer Ring

        sage: m = matrix(ZZ, 2, 2, [0, 1, 0, 0])
        sage: D = ChainComplex([m, m], base_ring=GF(2)); D
        Chain complex with at most 3 nonzero terms over Finite Field of size 2
        sage: D == loads(dumps(D))
        True
        sage: D.differential(0)==m, m.is_immutable(), D.differential(0).is_immutable()
        (True, False, True)

    Note that when a chain complex is defined in Sage, new
    differentials may be created: every nonzero module in the chain
    complex must have a differential coming from it, even if that
    differential is zero::

        sage: IZ = ChainComplex({0: identity_matrix(ZZ, 1)})
        sage: diff = IZ.differential()  # the differentials in the chain complex
        sage: diff[-1], diff[0], diff[1]
        ([], [1], [])
        sage: IZ.differential(1).parent()
        Full MatrixSpace of 0 by 1 dense matrices over Integer Ring
        sage: mat = ChainComplex({0: matrix(ZZ, 3, 4)}).differential(1)
        sage: mat.nrows(), mat.ncols()
        (0, 3)

    Defining the base ring implicitly::

        sage: ChainComplex([matrix(QQ, 3, 1), matrix(ZZ, 4, 3)])
        Chain complex with at most 3 nonzero terms over Rational Field
        sage: ChainComplex([matrix(GF(125, 'a'), 3, 1), matrix(ZZ, 4, 3)])              # needs sage.rings.finite_rings
        Chain complex with at most 3 nonzero terms over Finite Field in a of size 5^3

    If the matrices are defined over incompatible rings, an error results::

        sage: ChainComplex([matrix(GF(125, 'a'), 3, 1), matrix(QQ, 4, 3)])              # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        TypeError: no common canonical parent for objects with parents:
        'Finite Field in a of size 5^3' and 'Rational Field'

    If the base ring is given explicitly but is not compatible with
    the matrices, an error results::

        sage: ChainComplex([matrix(GF(125, 'a'), 3, 1)], base_ring=QQ)                  # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        TypeError: unable to convert 0 to a rational
    """

class Chain_class(ModuleElement):
    def __init__(self, parent, vectors, check: bool = True) -> None:
        """
        A Chain in a Chain Complex.

        A chain is collection of module elements for each module `C_n`
        of the chain complex `(C_n, d_n)`. There is no restriction on
        how the differentials `d_n` act on the elements of the chain.

        .. NOTE::

            You must use the chain complex to construct chains.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])},
            ....:                  base_ring=GF(7))
            sage: C.category()
            Category of chain complexes over Finite Field of size 7

        TESTS::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([0, 1, 2]), 1: vector([3, 4])})
            sage: TestSuite(c).run()
        """
    def vector(self, degree):
        """
        Return the free module element in ``degree``.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([1, 2, 3]), 1: vector([4, 5])})
            sage: c.vector(0)
            (1, 2, 3)
            sage: c.vector(1)
            (4, 5)
            sage: c.vector(2)
            ()
        """
    def is_cycle(self):
        """
        Return whether the chain is a cycle.

        OUTPUT: boolean; whether the elements of the chain are in the kernel
        of the differentials

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([0, 1, 2]), 1: vector([3, 4])})
            sage: c.is_cycle()
            True
        """
    def is_boundary(self):
        """
        Return whether the chain is a boundary.

        OUTPUT:

        boolean; whether the elements of the chain are in the image of
        the differentials.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([0, 1, 2]), 1: vector([3, 4])})
            sage: c.is_boundary()
            False
            sage: z3 = C({1:(1, 0)})
            sage: z3.is_cycle()
            True
            sage: (2*z3).is_boundary()
            False
            sage: (3*z3).is_boundary()
            True
        """
    def __eq__(self, other):
        """
        Return ``True`` if this chain is equal to ``other``.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([0, 1, 2]), 1: vector([3, 4])})
            sage: c == c
            True
            sage: c == C(0)
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` if this chain is not equal to ``other``.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: c = C({0: vector([0, 1, 2]), 1: vector([3, 4])})
            sage: c != c
            False
            sage: c != C(0)
            True
        """

class ChainComplex_class(Parent):
    """
    See :func:`ChainComplex` for full documentation.

    The differentials are required to be in the following canonical form:

    * All differentials that are not `0 \\times 0` must be specified
      (even if they have zero rows or zero columns), and

    * Differentials that are `0 \\times 0` must not be specified.

    * Immutable matrices over the ``base_ring``

    This and more is ensured by the assertions in the
    constructor. The :func:`ChainComplex` factory function must
    ensure that only valid input is passed.

    EXAMPLES::

        sage: C = ChainComplex(); C
        Trivial chain complex over Integer Ring

        sage: D = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
        sage: D
        Chain complex with at most 2 nonzero terms over Integer Ring
    """
    def __init__(self, grading_group, degree_of_differential, base_ring, differentials) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: ChainComplex().base_ring()
            Integer Ring

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: TestSuite(C).run()
        """
    Element = Chain_class
    def random_element(self):
        """
        Return a random element.

        EXAMPLES::

            sage: D = ChainComplex({0: matrix(ZZ, 2, 2, [1,0,0,2])})
            sage: D.random_element()    # random output
            Chain with 1 nonzero terms over Integer Ring
        """
    @cached_method
    def rank(self, degree, ring=None):
        """
        Return the rank of a differential.

        INPUT:

        - ``degree`` -- an element `\\delta` of the grading
          group. Which differential `d_{\\delta}` we want to know the
          rank of

        - ``ring`` -- (optional) a commutative ring `S`;
          if specified, the rank is computed after changing to this ring

        OUTPUT:

        The rank of the differential `d_{\\delta} \\otimes_R S`, where
        `R` is the base ring of the chain complex.

        EXAMPLES::

            sage: C = ChainComplex({0:matrix(ZZ, [[2]])})
            sage: C.differential(0)
            [2]
            sage: C.rank(0)
            1
            sage: C.rank(0, ring=GF(2))
            0
        """
    def grading_group(self):
        """
        Return the grading group.

        OUTPUT:

        The discrete abelian group that indexes the individual modules
        of the complex. Usually `\\ZZ`.

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([0, 3])
            sage: C = ChainComplex(grading_group=G, degree=G(vector([1,2])))
            sage: C.grading_group()
            Additive abelian group isomorphic to Z + Z/3
            sage: C.degree_of_differential()
            (1, 2)
        """
    @cached_method
    def nonzero_degrees(self):
        """
        Return the degrees in which the module is non-trivial.

        See also :meth:`ordered_degrees`.

        OUTPUT:

        The tuple containing all degrees `n` (grading group elements)
        such that the module `C_n` of the chain is non-trivial.

        EXAMPLES::

            sage: one = matrix(ZZ, [[1]])
            sage: D = ChainComplex({0: one, 2: one, 6:one})
            sage: ascii_art(D)
                       [1]                             [1]       [0]       [1]
            0 <-- C_7 <---- C_6 <-- 0  ...  0 <-- C_3 <---- C_2 <---- C_1 <---- C_0 <-- 0
            sage: D.nonzero_degrees()
            (0, 1, 2, 3, 6, 7)
        """
    @cached_method
    def ordered_degrees(self, start=None, exclude_first: bool = False):
        """
        Sort the degrees in the order determined by the differential.

        INPUT:

        - ``start`` -- (default: ``None``) a degree (element of the grading
          group) or ``None``

        - ``exclude_first`` -- boolean (optional; default:
          ``False``); whether to exclude the lowest degree -- this is a
          handy way to just get the degrees of the nonzero modules,
          as the domain of the first differential is zero.

        OUTPUT: if ``start`` has been specified, the longest tuple of degrees

        * containing ``start`` (unless ``start`` would be the first
          and ``exclude_first=True``),

        * in ascending order relative to :meth:`degree_of_differential`, and

        * such that none of the corresponding differentials are `0\\times 0`.

        If ``start`` has not been specified, a tuple of such tuples of
        degrees. One for each sequence of nonzero differentials. They
        are returned in sort order.

        EXAMPLES::

            sage: one = matrix(ZZ, [[1]])
            sage: D = ChainComplex({0: one, 2: one, 6:one})
            sage: ascii_art(D)
                       [1]                             [1]       [0]       [1]
            0 <-- C_7 <---- C_6 <-- 0  ...  0 <-- C_3 <---- C_2 <---- C_1 <---- C_0 <-- 0
            sage: D.ordered_degrees()
            ((-1, 0, 1, 2, 3), (5, 6, 7))
            sage: D.ordered_degrees(exclude_first=True)
            ((0, 1, 2, 3), (6, 7))
            sage: D.ordered_degrees(6)
            (5, 6, 7)
            sage: D.ordered_degrees(5, exclude_first=True)
            (6, 7)
        """
    def degree_of_differential(self):
        """
        Return the degree of the differentials of the complex.

        OUTPUT: an element of the grading group

        EXAMPLES::

            sage: D = ChainComplex({0: matrix(ZZ, 2, 2, [1,0,0,2])})
            sage: D.degree_of_differential()
            1
        """
    def differential(self, dim=None):
        """
        The differentials which make up the chain complex.

        INPUT:

        - ``dim`` -- element of the grading group (default:
          ``None``); if this is ``None``, return a dictionary of all
          of the differentials, or if this is a single element, return
          the differential starting in that dimension

        OUTPUT:

        Either a dictionary of all of the differentials or a single
        differential (i.e., a matrix).

        EXAMPLES::

            sage: D = ChainComplex({0: matrix(ZZ, 2, 2, [1,0,0,2])})
            sage: D.differential(0)
            [1 0]
            [0 2]
            sage: D.differential(-1)
            []
            sage: C = ChainComplex({0: identity_matrix(ZZ, 40)})
            sage: diff = C.differential()
            sage: diff[-1]
            40 x 0 dense matrix over Integer Ring (use the '.str()' method to see the entries)
            sage: diff[0]
            40 x 40 dense matrix over Integer Ring (use the '.str()' method to see the entries)
            sage: diff[1]
            []
        """
    def dual(self):
        """
        The dual chain complex to ``self``.

        Since all modules in ``self`` are free of finite rank, the
        dual in dimension `n` is isomorphic to the original chain
        complex in dimension `n`, and the corresponding boundary
        matrix is the transpose of the matrix in the original complex.
        This converts a chain complex to a cochain complex and vice versa.

        EXAMPLES::

            sage: C = ChainComplex({2: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: C.degree_of_differential()
            1
            sage: C.differential(2)
            [3 0 0]
            [0 0 0]
            sage: C.dual().degree_of_differential()
            -1
            sage: C.dual().differential(3)
            [3 0]
            [0 0]
            [0 0]
        """
    def free_module_rank(self, degree):
        """
        Return the rank of the free module at the given ``degree``.

        INPUT:

        - ``degree`` -- an element of the grading group

        OUTPUT:

        Integer. The rank of the free module `C_n` at the given degree
        `n`.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0]), 1: matrix(ZZ, [[0, 1]])})
            sage: [C.free_module_rank(i) for i in range(-2, 5)]
            [0, 0, 3, 2, 1, 0, 0]
        """
    def free_module(self, degree=None):
        """
        Return the free module at fixed ``degree``, or their sum.

        INPUT:

        - ``degree`` -- an element of the grading group or ``None`` (default)

        OUTPUT:

        The free module `C_n` at the given degree `n`. If the degree
        is not specified, the sum `\\bigoplus C_n` is returned.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0]), 1: matrix(ZZ, [[0, 1]])})
            sage: C.free_module()
            Ambient free module of rank 6 over the principal ideal domain Integer Ring
            sage: C.free_module(0)
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: C.free_module(1)
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: C.free_module(2)
            Ambient free module of rank 1 over the principal ideal domain Integer Ring
        """
    def __hash__(self):
        """
        The hash is formed by combining the hashes of.

        - the base ring
        - the differentials -- the matrices and their degrees
        - the degree of the differential of the chain complex

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: D = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: hash(C) == hash(D)
            True
        """
    def __eq__(self, other):
        """
        Return ``True`` iff this chain complex is the same as other: that
        is, if the base rings and the matrices of the two are the
        same.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])},
            ....:                  base_ring=GF(2))
            sage: D = ChainComplex({0: matrix(GF(2), 2, 3, [1, 0, 0, 0, 0, 0]),
            ....:                   1: matrix(ZZ, 0, 2),
            ....:                   3: matrix(ZZ, 0, 0)})  # base_ring determined from the matrices
            sage: C == D
            True
        """
    def __ne__(self, other):
        """
        Return ``True`` iff this chain complex is not the same as other.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])},
            ....:                  base_ring=GF(2))
            sage: D = ChainComplex({0: matrix(GF(2), 2, 3, [1, 0, 0, 0, 0, 0]),
            ....:                   1: matrix(ZZ, 0, 2),
            ....:                   3: matrix(ZZ, 0, 0)})  # base_ring determined from the matrices
            sage: C != D
            False
            sage: E = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])},
            ....:                  base_ring=ZZ)
            sage: C != E
            True
        """
    def homology(self, deg=None, base_ring=None, generators: bool = False, verbose: bool = False, algorithm: str = 'pari'):
        """
        The homology of the chain complex.

        INPUT:

        - ``deg`` -- an element of the grading group for the chain
          complex (default: ``None``); the degree in which
          to compute homology -- if this is ``None``, return the
          homology in every degree in which the chain complex is
          possibly nonzero.

        - ``base_ring`` -- a commutative ring (default: the
          base ring for the chain complex); must be either the
          integers `\\ZZ` or a field

        - ``generators`` -- boolean (default: ``False``); if
          ``True``, return generators for the homology groups along with
          the groups. See :issue:`6100`

        - ``verbose`` -- boolean (default: ``False``); if
          ``True``, print some messages as the homology is computed

        - ``algorithm`` -- string (default: ``'pari'``); the
          options are:

          * ``'auto'``
          * ``'dhsw'``
          * ``'pari'``

          See below for descriptions.

        OUTPUT:

        If the degree is specified, the homology in degree ``deg``.
        Otherwise, the homology in every dimension as a dictionary
        indexed by dimension.

        ALGORITHM:

        Over a
        field, just compute ranks and nullities, thus obtaining
        dimensions of the homology groups as vector spaces.  Over the
        integers, compute Smith normal form of the boundary matrices
        defining the chain complex according to the value of
        ``algorithm``.  If ``algorithm`` is ``'auto'``,
        then for each relatively small matrix, use the standard Sage
        method, which calls the Pari package.  For any large matrix,
        reduce it using the Dumas, Heckenbach, Saunders, and Welker
        elimination algorithm [DHSW2003]_: see
        :func:`~sage.homology.matrix_utils.dhsw_snf` for details.

        ``'no_chomp'`` is a synonym for ``'auto'``, maintained for
        backward-compatibility.

        ``algorithm`` may also be ``'pari'`` or ``'dhsw'``, which
        forces the named algorithm to be used regardless of the size
        of the matrices.

        As of this writing, ``'pari'`` is the fastest standard option.

        .. WARNING::

           This only works if the base ring is the integers or a
           field.  Other values will return an error.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: C.homology()
            {0: Z x Z, 1: Z x C3}
            sage: C.homology(deg=1, base_ring=GF(3))
            Vector space of dimension 2 over Finite Field of size 3
            sage: D = ChainComplex({0: identity_matrix(ZZ, 4), 4: identity_matrix(ZZ, 30)})
            sage: D.homology()
            {0: 0, 1: 0, 4: 0, 5: 0}

        Generators: generators are given as a list of cycles, each of
        which is an element in the appropriate free module, and hence
        is represented as a vector. Each summand of the homology is
        listed separately, with a corresponding generator::

            sage: C.homology(1, generators=True)
            [(C3, Chain(1:(1, 0))), (Z, Chain(1:(0, 1)))]

        Tests for :issue:`6100`, the Klein bottle with generators::

            sage: d0 = matrix(ZZ, 0,1)
            sage: d1 = matrix(ZZ, 1,3, [[0,0,0]])
            sage: d2 = matrix(ZZ, 3,2, [[1,1], [1,-1], [-1,1]])
            sage: C_k = ChainComplex({0:d0, 1:d1, 2:d2}, degree=-1)
            sage: C_k.homology(generators=true)
            {0: [(Z, Chain(0:(1)))],
             1: [(C2, Chain(1:(0, 1, -1))), (Z, Chain(1:(0, 1, 0)))],
             2: []}

        From a torus using a field::

            sage: T = simplicial_complexes.Torus()                                      # needs sage.graphs
            sage: C_t = T.chain_complex()                                               # needs sage.graphs
            sage: C_t.homology(base_ring=QQ, generators=True)                           # needs sage.graphs
            {0: [(Vector space of dimension 1 over Rational Field,
               Chain(0:(0, 0, 0, 0, 0, 0, 1)))],
             1: [(Vector space of dimension 1 over Rational Field,
               Chain(1:(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 1))),
              (Vector space of dimension 1 over Rational Field,
               Chain(1:(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0)))],
             2: [(Vector space of dimension 1 over Rational Field,
               Chain(2:(1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1)))]}
        """
    def betti(self, deg=None, base_ring=None):
        """
        The Betti number of the chain complex.

        That is, write the homology in this degree as a direct sum
        of a free module and a torsion module; the Betti number is the
        rank of the free summand.

        INPUT:

        - ``deg`` -- an element of the grading group for the chain
          complex or ``None`` (default: ``None``); if ``None``,
          then return every Betti number, as a dictionary indexed by
          degree, or if an element of the grading group, then return
          the Betti number in that degree

        - ``base_ring`` -- a commutative ring (default: the
          base ring for the chain complex); compute homology with
          these coefficients -- must be either the integers or a
          field

        OUTPUT:

        The Betti number in degree ``deg`` -- the rank of the free
        part of the homology module in this degree.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: C.betti(0)
            2
            sage: [C.betti(n) for n in range(5)]
            [2, 1, 0, 0, 0]
            sage: C.betti()
            {0: 2, 1: 1}

            sage: D = ChainComplex({0: matrix(GF(5), [[3, 1],[1, 2]])})
            sage: D.betti()
            {0: 1, 1: 1}
        """
    def torsion_list(self, max_prime, min_prime: int = 2):
        """
        Look for torsion in this chain complex by computing its mod `p`
        homology for a range of primes `p`.

        INPUT:

        - ``max_prime`` -- prime number; search for torsion mod `p` for
          all `p` strictly less than this number

        - ``min_prime`` -- prime (default: 2); search for
          torsion mod `p` for primes at least as big as this

        Return a list of pairs `(p, d)` where `p` is a prime at which
        there is torsion and `d` is a list of dimensions in which this
        torsion occurs.

        The base ring for the chain complex must be the integers; if
        not, an error is raised.

        ALGORITHM:

        Let `C` denote the chain complex.  Let `P` equal
        ``max_prime``.  Compute the mod `P` homology of `C`, and use
        this as the base-line computation: the assumption is that this
        is isomorphic to the integral homology tensored with
        `\\GF{P}`.  Then compute the mod `p` homology for a range of
        primes `p`, and record whenever the answer differs from the
        base-line answer.

        EXAMPLES::

            sage: C = ChainComplex({0: matrix(ZZ, 2, 3, [3, 0, 0, 0, 0, 0])})
            sage: C.homology()
            {0: Z x Z, 1: Z x C3}
            sage: C.torsion_list(11)                                                    # needs sage.rings.finite_rings
            [(3, [1])]
            sage: C = ChainComplex([matrix(ZZ, 1, 1, [2]), matrix(ZZ, 1, 1), matrix(1, 1, [3])])
            sage: C.homology(1)
            C2
            sage: C.homology(3)
            C3
            sage: C.torsion_list(5)                                                     # needs sage.rings.finite_rings
            [(2, [1]), (3, [3])]
        """
    def shift(self, n: int = 1):
        """
        Shift this chain complex `n` times.

        INPUT:

        - ``n`` -- integer (default: 1)

        The *shift* operation is also sometimes called *translation* or
        *suspension*.

        To shift a chain complex by `n`, shift its entries up by `n`
        (if it is a chain complex) or down by `n` (if it is a cochain
        complex); that is, shifting by 1 always shifts in the opposite
        direction of the differential. In symbols, if `C` is a chain
        complex and `C[n]` is its `n`-th shift, then `C[n]_j =
        C_{j-n}`. The differential in the shift `C[n]` is obtained by
        multiplying each differential in `C` by `(-1)^n`.

        Caveat: different sources use different conventions for
        shifting: what we call `C[n]` might be called `C[-n]` in some
        places. See for example.
        https://ncatlab.org/nlab/show/suspension+of+a+chain+complex
        (which uses `C[n]` as we do but acknowledges `C[-n]`) or 1.2.8
        in [Wei1994]_ (which uses `C[-n]`).

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S1 = simplicial_complexes.Sphere(1).chain_complex()
            sage: S1.shift(1).differential(2) == -S1.differential(1)
            True
            sage: S1.shift(2).differential(3) == S1.differential(1)
            True
            sage: S1.shift(3).homology(4)
            Z

        For cochain complexes, shifting goes in the other
        direction. Topologically, this makes sense if we grade the
        cochain complex for a space negatively::

            sage: # needs sage.graphs
            sage: T = simplicial_complexes.Torus()
            sage: co_T = T.chain_complex()._flip_()
            sage: co_T.homology()
            {-2: Z, -1: Z x Z, 0: Z}
            sage: co_T.degree_of_differential()
            1
            sage: co_T.shift(2).homology()
            {-4: Z, -3: Z x Z, -2: Z}

        You can achieve the same result by tensoring (on the left, to
        get the signs right) with a rank one free module in degree
        ``-n * deg``, if ``deg`` is the degree of the differential::

            sage: C = ChainComplex({-2: matrix(ZZ, 0, 1)})
            sage: C.tensor(co_T).homology()                                             # needs sage.graphs
            {-4: Z, -3: Z x Z, -2: Z}
        """
    def cartesian_product(self, *factors, **kwds):
        """
        Return the direct sum (Cartesian product) of ``self`` with ``D``.

        Let `C` and `D` be two chain complexes with differentials
        `\\partial_C` and `\\partial_D`, respectively, of the same degree (so
        they must also have the same grading group).
        The direct sum `S = C \\oplus D` is a chain complex given by
        `S_i = C_i \\oplus D_i` with differential
        `\\partial = \\partial_C \\oplus \\partial_D`.

        INPUT:

        - ``subdivide`` -- boolean (default: ``False``); whether to subdivide the
          the differential matrices

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = ChainComplex([matrix([[-y],[x]]), matrix([[x, y]])])
            sage: D = ChainComplex([matrix([[x-y]]), matrix([[0], [0]])])
            sage: ascii_art(C.cartesian_product(D))
                        [x y 0]       [   -y     0]
                        [0 0 0]       [    x     0]
                        [0 0 0]       [    0 x - y]
             0 <-- C_2 <-------- C_1 <-------------- C_0 <-- 0

            sage: D = ChainComplex({1:matrix([[x-y]]), 4:matrix([[x], [y]])})
            sage: ascii_art(D)
                        [x]
                        [y]                     [x - y]
             0 <-- C_5 <---- C_4 <-- 0 <-- C_2 <-------- C_1 <-- 0
            sage: ascii_art(cartesian_product([C, D]))
                                                                          [-y]
                        [x]                     [    x     y     0]       [ x]
                        [y]                     [    0     0 x - y]       [ 0]
             0 <-- C_5 <---- C_4 <-- 0 <-- C_2 <-------------------- C_1 <----- C_0 <-- 0

        The degrees of the differentials must agree::

            sage: C = ChainComplex({1:matrix([[x]])}, degree_of_differential=-1)
            sage: D = ChainComplex({1:matrix([[x]])}, degree_of_differential=1)
            sage: C.cartesian_product(D)
            Traceback (most recent call last):
            ...
            ValueError: the degrees of the differentials must match

        TESTS::

            sage: C = ChainComplex({2:matrix([[-1],[2]]), 1:matrix([[2, 1]])},
            ....:                  degree_of_differential=-1)
            sage: ascii_art(C.cartesian_product(C, subdivide=True))
                                        [-1| 0]
                                        [ 2| 0]
                        [2 1|0 0]       [--+--]
                        [---+---]       [ 0|-1]
                        [0 0|2 1]       [ 0| 2]
             0 <-- C_0 <---------- C_1 <-------- C_2 <-- 0

        ::

            sage: R.<x,y,z> = QQ[]
            sage: C1 = ChainComplex({1:matrix([[x]])})
            sage: C2 = ChainComplex({1:matrix([[y]])})
            sage: C3 = ChainComplex({1:matrix([[z]])})
            sage: ascii_art(cartesian_product([C1, C2, C3]))
                        [x 0 0]
                        [0 y 0]
                        [0 0 z]
             0 <-- C_2 <-------- C_1 <-- 0
            sage: ascii_art(C1.cartesian_product([C2, C3], subdivide=True))
                        [x|0|0]
                        [-+-+-]
                        [0|y|0]
                        [-+-+-]
                        [0|0|z]
             0 <-- C_2 <-------- C_1 <-- 0

        ::

            sage: R.<x> = ZZ[]
            sage: G = AdditiveAbelianGroup([0,7])
            sage: d = {G(vector([1,1])):matrix([[x]])}
            sage: C = ChainComplex(d, grading_group=G, degree=G(vector([2,1])))
            sage: ascii_art(C.cartesian_product(C))
                             [x 0]
                             [0 x]
             0 <-- C_(3, 2) <------ C_(1, 1) <-- 0
        """
    def tensor(self, *factors, **kwds):
        """
        Return the tensor product of ``self`` with ``D``.

        Let `C` and `D` be two chain complexes with differentials
        `\\partial_C` and `\\partial_D`, respectively, of the same degree (so
        they must also have the same grading group).
        The tensor product `S = C \\otimes D` is a chain complex given by

        .. MATH::

            S_i = \\bigoplus_{a+b=i} C_a \\otimes D_b

        with differential

        .. MATH::

            \\partial(x \\otimes y) = \\partial_C x \\otimes y
            + (-1)^{|a| \\cdot |\\partial_D|} x \\otimes \\partial_D y

        for `x \\in C_a` and `y \\in D_b`, where `|a|` is the degree of `a` and
        `|\\partial_D|` is the degree of `\\partial_D`.

        .. WARNING::

            If the degree of the differential is even, then this may not
            result in a valid chain complex.

        INPUT:

        - ``subdivide`` -- boolean (default: ``False``); whether to subdivide the
          the differential matrices

        .. TODO::

            Make subdivision work correctly on multiple factors.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: C1 = ChainComplex({1:matrix([[x]])}, degree_of_differential=-1)
            sage: C2 = ChainComplex({1:matrix([[y]])}, degree_of_differential=-1)
            sage: C3 = ChainComplex({1:matrix([[z]])}, degree_of_differential=-1)
            sage: ascii_art(C1.tensor(C2))
                                    [ x]
                        [y x]       [-y]
             0 <-- C_0 <------ C_1 <----- C_2 <-- 0
            sage: ascii_art(C1.tensor(C2).tensor(C3))
                                      [ y  x  0]       [ x]
                                      [-z  0  x]       [-y]
                        [z y x]       [ 0 -z -y]       [ z]
             0 <-- C_0 <-------- C_1 <----------- C_2 <----- C_3 <-- 0

        ::

            sage: C = ChainComplex({2:matrix([[-y],[x]]), 1:matrix([[x, y]])},
            ....:                  degree_of_differential=-1); ascii_art(C)
                                    [-y]
                        [x y]       [ x]
             0 <-- C_0 <------ C_1 <----- C_2 <-- 0
            sage: T = C.tensor(C)
            sage: T.differential(1)
            [x y x y]
            sage: T.differential(2)
            [-y  x  0  y  0  0]
            [ x  0  x  0  y  0]
            [ 0 -x -y  0  0 -y]
            [ 0  0  0 -x -y  x]
            sage: T.differential(3)
            [ x  y  0  0]
            [ y  0 -y  0]
            [-x  0  0 -y]
            [ 0  y  x  0]
            [ 0 -x  0  x]
            [ 0  0  x  y]
            sage: T.differential(4)
            [-y]
            [ x]
            [-y]
            [ x]

        The degrees of the differentials must agree::

            sage: C1p = ChainComplex({1:matrix([[x]])}, degree_of_differential=1)
            sage: C1.tensor(C1p)
            Traceback (most recent call last):
            ...
            ValueError: the degrees of the differentials must match

        TESTS::

            sage: R.<x,y,z> = QQ[]
            sage: C1 = ChainComplex({1:matrix([[x]])})
            sage: C2 = ChainComplex({1:matrix([[y]])})
            sage: C3 = ChainComplex({1:matrix([[z]])})
            sage: ascii_art(tensor([C1, C2, C3]))
                                      [-y -z  0]       [ z]
                                      [ x  0 -z]       [-y]
                        [x y z]       [ 0  x  y]       [ x]
             0 <-- C_6 <-------- C_5 <----------- C_4 <----- C_3 <-- 0

        ::

            sage: R.<x,y> = ZZ[]
            sage: G = AdditiveAbelianGroup([0,7])
            sage: d1 = {G(vector([1,1])):matrix([[x]])}
            sage: C1 = ChainComplex(d1, grading_group=G, degree=G(vector([2,1])))
            sage: d2 = {G(vector([3,0])):matrix([[y]])}
            sage: C2 = ChainComplex(d2, grading_group=G, degree=G(vector([2,1])))
            sage: ascii_art(C1.tensor(C2))
                                                [y]
                             [ x -y]            [x]
             0 <-- C_(8, 3) <-------- C_(6, 2) <---- C_(4, 1) <-- 0

        Check that :issue:`21760` is fixed::

            sage: C = ChainComplex({0: matrix(ZZ, 0, 2)}, degree=-1)
            sage: ascii_art(C)
             0 <-- C_0 <-- 0
            sage: T = C.tensor(C)
            sage: ascii_art(T)
             0 <-- C_0 <-- 0
            sage: T.free_module_rank(0)
            4
        """
