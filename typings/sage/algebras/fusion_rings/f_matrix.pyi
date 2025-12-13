from _typeshed import Incomplete
from sage.algebras.fusion_rings.fast_parallel_fmats_methods import executor as executor
from sage.algebras.fusion_rings.poly_tup_engine import apply_coeff_map as apply_coeff_map, compute_known_powers as compute_known_powers, constant_coeff as constant_coeff, get_variables_degrees as get_variables_degrees, poly_to_tup as poly_to_tup, poly_tup_sortkey as poly_tup_sortkey, resize as resize, tup_to_univ_poly as tup_to_univ_poly, variables as variables
from sage.algebras.fusion_rings.shm_managers import FvarsHandler as FvarsHandler, KSHandler as KSHandler
from sage.graphs.graph import Graph as Graph
from sage.matrix.constructor import matrix as matrix
from sage.misc.misc import get_main_globals as get_main_globals
from sage.rings.ideal import Ideal as Ideal
from sage.rings.polynomial.polydict import ETuple as ETuple
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar import AA as AA, QQbar as QQbar, number_field_elements_from_algebraics as number_field_elements_from_algebraics
from sage.structure.sage_object import SageObject as SageObject

class FMatrix(SageObject):
    '''
    An F-matrix for a :class:`FusionRing`.

    INPUT:

    - ``FR`` -- a :class:`FusionRing`
    - ``fusion_label`` -- (optional) a string used to label basis elements
      of the :class:`FusionRing` associated to ``self``
      (see :meth:`FusionRing.fusion_labels`)
    - ``var_prefix`` -- (optional) a string indicating the desired prefix
      for variables denoting F-symbols to be solved
    - ``inject_variables`` -- boolean (default: ``False``); whether to inject
      variables (:class:`FusionRing` basis element labels and F-symbols) into
      the global namespace

    The :class:`FusionRing` or Verlinde algebra is the
    Grothendieck ring of a modular tensor category [BaKi2001]_.
    Such categories arise in conformal field theory or in the
    representation theories of affine Lie algebras, or
    quantum groups at roots of unity. They have applications
    to low dimensional topology and knot theory, to conformal
    field theory and to topological quantum computing. The
    :class:`FusionRing` captures much information about a fusion
    category, but to complete the picture, the F-matrices or
    6j-symbols are needed. For example these are required in
    order to construct braid group representations. This
    can be done using the :class:`FusionRing` method
    :meth:`FusionRing.get_braid_generators`, which uses
    the F-matrix.

    We only undertake to compute the F-matrix if the
    :class:`FusionRing` is *multiplicity free* meaning that
    the Fusion coefficients `N^{ij}_k` are bounded
    by 1. For Cartan Types `X_r` and level `k`,
    the multiplicity-free cases are given by the
    following table.

    +------------------------+----------+
    | Cartan Type            | `k`      |
    +========================+==========+
    | `A_1`                  | any      |
    +------------------------+----------+
    | `A_r, r\\geq 2`         | `\\leq 2` |
    +------------------------+----------+
    | `B_r, r\\geq 2`         | `\\leq 2` |
    +------------------------+----------+
    | `C_2`                  | `\\leq 2` |
    +------------------------+----------+
    | `C_r, r\\geq 3`         | `\\leq 1` |
    +------------------------+----------+
    | `D_r, r\\geq 4`         | `\\leq 2` |
    +------------------------+----------+
    | `G_2, F_4, E_6, E_7`   | `\\leq 2` |
    +------------------------+----------+
    | `E_8`                  | `\\leq 3` |
    +------------------------+----------+

    Beyond this limitation, computation of the F-matrix
    can involve very large systems of equations. A
    rule of thumb is that this code can compute the
    F-matrix for systems with `\\leq 14` simple objects
    (primary fields) on a machine with 16 GB of memory.
    (Larger examples can be quite time consuming.)

    The :class:`FusionRing` and its methods capture much
    of the structure of the underlying tensor category.
    But an important aspect that is not encoded in the
    fusion ring is the associator, which is a homomorphism
    `(A\\otimes B)\\otimes C\\to A\\otimes(B\\otimes C)` that
    requires an additional tool, the F-matrix or 6j-symbol.
    To specify this, we fix a simple object `D`
    and represent the transformation

    .. MATH::

        \\text{Hom}(D, (A\\otimes B)\\otimes C)
        \\to \\text{Hom}(D, A\\otimes(B\\otimes C))

    by a matrix `F^{ABC}_D`. This depends on a pair of
    additional simple objects `X` and `Y`. Indeed, we can
    get a basis for `\\text{Hom}(D, (A\\otimes B)\\otimes C)`
    indexed by simple objects `X` in which the corresponding
    homomorphism factors through `X\\otimes C`, and similarly
    `\\text{Hom}(D, A\\otimes(B\\otimes C))` has a basis indexed
    by `Y`, in which the basis vector factors through `A\\otimes Y`.

    See [TTWL2009]_ for an introduction to this topic,
    [EGNO2015]_ Section 4.9 for a precise mathematical
    definition, and [Bond2007]_ Section 2.5 and [Ab2022]_ for discussions
    of how to compute the F-matrix. In addition to
    [Bond2007]_, worked out F-matrices may be found in
    [RoStWa2009]_ and [CHW2015]_.

    The F-matrix is only determined up to a *gauge*. This
    is a family of embeddings `C \\to A\\otimes B` for
    simple objects `A, B, C` such that `\\text{Hom}(C, A\\otimes B)`
    is nonzero. Changing the gauge changes the F-matrix though
    not in a very essential way. By varying the gauge it is
    possible to make the F-matrices unitary, or it is possible
    to make them cyclotomic.

    Due to the large number of equations we may fail to find a
    Groebner basis if there are too many variables.

    EXAMPLES::

        sage: I = FusionRing("E8", 2, conjugate=True)
        sage: I.fusion_labels(["i0", "p", "s"], inject_variables=True)
        sage: f = I.get_fmatrix(inject_variables=True); f
        creating variables fx1..fx14
        Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx13
        F-Matrix factory for The Fusion Ring of Type E8 and level 2 with Integer Ring coefficients

    We have injected two sets of variables to the global namespace.
    We created three variables ``i0, p, s`` to represent the
    primary fields (simple elements) of the :class:`FusionRing`. Creating
    the :class:`FMatrix` factory also created variables
    ``fx1, fx2, ..., fx14`` in order to solve the hexagon and pentagon
    equations describing the F-matrix. Since we called :class:`FMatrix`
    with the parameter ``inject_variables=True``, these have been injected
    into the global namespace. This is not necessary for the code to work
    but if you want to run the code experimentally you may want access
    to these variables.

    EXAMPLES::

        sage: f.fmatrix(s, s, s, s)
        [fx10 fx11]
        [fx12 fx13]

    The F-matrix has not been computed at this stage, so
    the F-matrix `F^{sss}_s` is filled with variables
    ``fx10``, ``fx11``, ``fx12``, ``fx13``. The task is
    to solve for these.

    As explained above The F-matrix `(F^{ABC}_D)_{X, Y}`
    two other variables `X` and `Y`. We have methods to
    tell us (depending on `A, B, C, D`) what the possibilities
    for these are. In this example with `A=B=C=D=s`
    both `X` and `Y` are allowed to be `i_0` or `s`.

    ::

        sage: f.f_from(s, s, s, s), f.f_to(s, s, s, s)
        ([i0, p], [i0, p])

    The last two statements show that the possible values of
    `X` and `Y` when `A = B = C = D = s` are `i_0` and `p`.

    The F-matrix is computed by solving the so-called
    pentagon and hexagon equations. The *pentagon equations*
    reflect the Mac Lane pentagon axiom in the definition
    of a monoidal category. The hexagon relations
    reflect the axioms of a *braided monoidal category*,
    which are constraints on both the F-matrix and on
    the R-matrix. Optionally, orthogonality constraints
    may be imposed to obtain an orthogonal F-matrix.

    ::

        sage: sorted(f.get_defining_equations("pentagons"))[1:3]
        [fx9*fx12 - fx2*fx13, fx4*fx11 - fx2*fx13]
        sage: sorted(f.get_defining_equations("hexagons"))[1:3]
        [fx6 - 1, fx2 + 1]
        sage: sorted(f.get_orthogonality_constraints())[1:3]
        [fx10*fx11 + fx12*fx13, fx10*fx11 + fx12*fx13]

    There are two methods available to compute an F-matrix.
    The first, :meth:`find_cyclotomic_solution` uses only
    the pentagon and hexagon relations. The second,
    :meth:`find_orthogonal_solution` uses additionally
    the orthogonality relations. There are some differences
    that should be kept in mind.

    :meth:`find_cyclotomic_solution` currently works only with
    smaller examples. For example the :class:`FusionRing` for `G_2`
    at level 2 is too large. When it is available, this method
    produces an F-matrix whose entries are in the same
    cyclotomic field as the underlying :class:`FusionRing`. ::

        sage: f.find_cyclotomic_solution()
        Setting up hexagons and pentagons...
        Finding a Groebner basis...
        Solving...
        Fixing the gauge...
        adding equation... fx1 - 1
        adding equation... fx11 - 1
        Done!

    We now have access to the values of the F-matrix using
    the methods :meth:`fmatrix` and :meth:`fmat`::

        sage: f.fmatrix(s, s, s, s)
        [(-1/2*zeta128^48 + 1/2*zeta128^16)                                  1]
        [                               1/2  (1/2*zeta128^48 - 1/2*zeta128^16)]
        sage: f.fmat(s, s, s, s, p, p)
        (1/2*zeta128^48 - 1/2*zeta128^16)

    :meth:`find_orthogonal_solution` is much more powerful
    and is capable of handling large cases, sometimes
    quickly but sometimes (in larger cases) after hours of
    computation. Its F-matrices are not always in the
    cyclotomic field that is the base ring of the underlying
    :class:`FusionRing`, but sometimes in an extension field adjoining
    some square roots. When this happens, the :class:`FusionRing` is
    modified, adding an attribute ``_basecoer`` that is
    a coercion from the cyclotomic field to the field
    containing the F-matrix. The field containing the F-matrix
    is available through :meth:`field`. ::

        sage: f = FusionRing("B3", 2).get_fmatrix()
        sage: f.find_orthogonal_solution(verbose=False, checkpoint=True)     # not tested (~100 s)
        sage: all(v in CyclotomicField(56) for v in f.get_fvars().values())  # not tested
        True

        sage: f = FusionRing("G2", 2).get_fmatrix()
        sage: f.find_orthogonal_solution(verbose=False) # long time (~11 s)
        sage: f.field()                                 # long time
        Algebraic Field
    '''
    mp_thresh: int
    pool: Incomplete
    def __init__(self, fusion_ring, fusion_label: str = 'f', var_prefix: str = 'fx', inject_variables: bool = False) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: f = FusionRing("B3", 2).get_fmatrix()
            sage: TestSuite(f).run(skip=\'_test_pickling\')
        '''
    ideal_basis: Incomplete
    def clear_equations(self) -> None:
        '''
        Clear the list of equations to be solved.

        EXAMPLES::

            sage: f = FusionRing("E6", 1).get_fmatrix()
            sage: f.get_defining_equations(\'hexagons\', output=False)
            sage: len(f.ideal_basis)
            6
            sage: f.clear_equations()
            sage: len(f.ideal_basis) == 0
            True
        '''
    def clear_vars(self) -> None:
        '''
        Reset the F-symbols.

        EXAMPLES::

            sage: f = FusionRing("C4", 1).get_fmatrix()
            sage: fvars = f.get_fvars()
            sage: some_key = sorted(fvars)[0]
            sage: fvars[some_key]
            fx0
            sage: fvars[some_key] = 1
            sage: f.get_fvars()[some_key]
            1
            sage: f.clear_vars()
            sage: f.get_fvars()[some_key]
            fx0
        '''
    def fmat(self, a, b, c, d, x, y, data: bool = True):
        '''
        Return the F-Matrix coefficient `(F^{a, b, c}_d)_{x, y}`.

        EXAMPLES::

            sage: fr = FusionRing("G2", 1, fusion_labels=("i0", "t"), inject_variables=True)
            sage: f = fr.get_fmatrix()
            sage: [f.fmat(t, t, t, t, x, y) for x in fr.basis() for y in fr.basis()]
            [fx1, fx2, fx3, fx4]
            sage: f.find_cyclotomic_solution(output=True)
            Setting up hexagons and pentagons...
            Finding a Groebner basis...
            Solving...
            Fixing the gauge...
            adding equation... fx2 - 1
            Done!
            {(t, t, t, i0, t, t): 1,
             (t, t, t, t, i0, i0): (-zeta60^14 + zeta60^6 + zeta60^4 - 1),
             (t, t, t, t, i0, t): 1,
             (t, t, t, t, t, i0): (-zeta60^14 + zeta60^6 + zeta60^4 - 1),
             (t, t, t, t, t, t): (zeta60^14 - zeta60^6 - zeta60^4 + 1)}
            sage: [f.fmat(t, t, t, t, x, y) for x in f._FR.basis() for y in f._FR.basis()]
            [(-zeta60^14 + zeta60^6 + zeta60^4 - 1),
             1,
             (-zeta60^14 + zeta60^6 + zeta60^4 - 1),
             (zeta60^14 - zeta60^6 - zeta60^4 + 1)]
        '''
    def fmatrix(self, a, b, c, d):
        '''
        Return the F-Matrix `F^{a, b, c}_d`.

        INPUT:

        - ``a``, ``b``, ``c``, ``d`` -- basis elements of the associated
          :class:`FusionRing`

        EXAMPLES::

            sage: fr = FusionRing("A1", 2, fusion_labels=\'c\', inject_variables=True)
            sage: f = fr.get_fmatrix(new=True)
            sage: f.fmatrix(c1, c1, c1, c1)
            [fx0 fx1]
            [fx2 fx3]
            sage: f.find_cyclotomic_solution(verbose=False);
            adding equation... fx4 - 1
            adding equation... fx10 - 1
            sage: f.f_from(c1, c1, c1, c1)
            [c0, c2]
            sage: f.f_to(c1, c1, c1, c1)
            [c0, c2]
            sage: f.fmatrix(c1, c1, c1, c1)
            [ (1/2*zeta32^12 - 1/2*zeta32^4) (-1/2*zeta32^12 + 1/2*zeta32^4)]
            [ (1/2*zeta32^12 - 1/2*zeta32^4)  (1/2*zeta32^12 - 1/2*zeta32^4)]
        '''
    def field(self):
        '''
        Return the base field containing the F-symbols.

        When ``self`` is initialized, the field is set to be the
        cyclotomic field of the :class:`FusionRing` associated
        to ``self``.

        The field may change after running :meth:`find_orthogonal_solution`.
        At that point, this method could return the
        associated :class:`FusionRing`\'s cyclotomic field, an
        appropriate :func:`NumberField` that was computed on the fly
        by the F-matrix solver, or the :class:`QQbar<AlgebraicField>`.

        Depending on the ``CartanType`` of ``self``, the solver may need
        to compute an extension field containing certain square roots that
        do not belong to the associated :class:`FusionRing`\'s cyclotomic field.

        In certain cases we revert to :class:`QQbar<AlgebraicField>` because
        the extension field computation does not seem to terminate. See
        :meth:`attempt_number_field_computation` for more details.

        The method :meth:`get_non_cyclotomic_roots` returns a list of
        roots defining the extension of the :class:`FusionRing`\'s
        cyclotomic field needed to contain all F-symbols.

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix()
            sage: f.field()
            Cyclotomic Field of order 60 and degree 16
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.field()
            Number Field in a with defining polynomial y^32 - ... - 22*y^2 + 1
            sage: phi = f.get_qqbar_embedding()
            sage: [phi(r).n() for r in f.get_non_cyclotomic_roots()]
            [-0.786151377757423 - 8.92806368517581e-31*I]

        .. NOTE::

            Consider using ``self.field().optimized_representation()`` to
            obtain an equivalent :func:`NumberField` with a defining
            polynomial with smaller coefficients, for a more efficient
            element representation.
        '''
    def FR(self):
        '''
        Return the :class:`FusionRing` associated to ``self``.

        EXAMPLES::

            sage: f = FusionRing("D3", 1).get_fmatrix()
            sage: f.FR()
            The Fusion Ring of Type D3 and level 1 with Integer Ring coefficients
        '''
    def findcases(self, output: bool = False):
        '''
        Return unknown F-matrix entries.

        If run with ``output=True``,
        this returns two dictionaries; otherwise it just returns the
        number of unknown values.

        EXAMPLES::

            sage: f = FusionRing("G2", 1, fusion_labels=("i0", "t")).get_fmatrix()
            sage: f.findcases()
            5
            sage: f.findcases(output=True)
             ({0: (t, t, t, i0, t, t),
              1: (t, t, t, t, i0, i0),
              2: (t, t, t, t, i0, t),
              3: (t, t, t, t, t, i0),
              4: (t, t, t, t, t, t)},
             {(t, t, t, i0, t, t): fx0,
              (t, t, t, t, i0, i0): fx1,
              (t, t, t, t, i0, t): fx2,
              (t, t, t, t, t, i0): fx3,
              (t, t, t, t, t, t): fx4})
        '''
    def f_from(self, a, b, c, d):
        '''
        Return the possible `x` such that there are morphisms
        `d \\to x \\otimes c \\to (a \\otimes b) \\otimes c`.

        INPUT:

        - ``a``, ``b``, ``c``, ``d`` -- basis elements of the associated
          :class:`FusionRing`

        EXAMPLES::

            sage: fr = FusionRing("A1", 3, fusion_labels=\'a\', inject_variables=True)
            sage: f = fr.get_fmatrix()
            sage: f.fmatrix(a1, a1, a2, a2)
            [fx6 fx7]
            [fx8 fx9]
            sage: f.f_from(a1, a1, a2, a2)
            [a0, a2]
            sage: f.f_to(a1, a1, a2, a2)
            [a1, a3]
        '''
    def f_to(self, a, b, c, d):
        '''
        Return the possible `y` such that there are morphisms
        `d \\to a \\otimes y \\to a \\otimes (b \\otimes c)`.

        INPUT:

        - ``a``, ``b``, ``c``, ``d`` -- basis elements of the associated
          :class:`FusionRing`

        EXAMPLES::

            sage: b22 = FusionRing("B2", 2)
            sage: b22.fusion_labels("b", inject_variables=True)
            sage: B = b22.get_fmatrix()
            sage: B.fmatrix(b2, b4, b2, b4)
            [fx266 fx267 fx268]
            [fx269 fx270 fx271]
            [fx272 fx273 fx274]
            sage: B.f_from(b2, b4, b2, b4)
            [b1, b3, b5]
            sage: B.f_to(b2, b4, b2, b4)
            [b1, b3, b5]
        '''
    def get_fvars(self):
        '''
        Return a dictionary of F-symbols.

        The keys are sextuples `(a, b, c, d, x, y)` of basis elements of
        ``self.FR()`` and the values are the corresponding F-symbols
        `(F^{a, b, c}_d)_{xy}`.

        These values reflect the current state of a solver\'s computation.

        EXAMPLES::

            sage: f = FusionRing("A2", 1).get_fmatrix(inject_variables=True)
            creating variables fx1..fx8
            Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7
            sage: f.get_fvars()[(f1, f1, f1, f0, f2, f2)]
            fx0
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.get_fvars()[(f1, f1, f1, f0, f2, f2)]
            1
        '''
    def get_poly_ring(self):
        '''
        Return the polynomial ring whose generators denote the desired F-symbols.

        EXAMPLES::

            sage: f = FusionRing("B6", 1).get_fmatrix()
            sage: f.get_poly_ring()
            Multivariate Polynomial Ring in fx0, ..., fx13 over
             Cyclotomic Field of order 96 and degree 32
        '''
    def get_non_cyclotomic_roots(self):
        '''
        Return a list of roots that define the extension of the associated
        :class:`FusionRing`\'s base
        :class:`Cyclotomic field<sage.rings.number_field.number_field.CyclotomicFieldFactory>`,
        containing all the F-symbols.

        OUTPUT:

        The list of non-cyclotomic roots is given as a list of elements of the
        field returned by :meth:`field()`.

        If ``self.field() == self.FR().field()`` then this method
        returns an empty list.

        EXAMPLES::

            sage: f = FusionRing("E6", 1).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.field() == f.FR().field()
            True
            sage: f.get_non_cyclotomic_roots()
            []
            sage: f = FusionRing("G2", 1).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.field() == f.FR().field()
            False
            sage: phi = f.get_qqbar_embedding()
            sage: [phi(r).n() for r in f.get_non_cyclotomic_roots()]
            [-0.786151377757423 - 8.92806368517581e-31*I]

        When ``self.field()`` is a ``NumberField``, one may use
        :meth:`get_qqbar_embedding` to embed the resulting values into
        :class:`QQbar<AlgebraicField>`.
        '''
    def get_qqbar_embedding(self):
        '''
        Return an embedding from the base field containing F-symbols (the
        associated :class:`FusionRing`\'s
        :class:`Cyclotomic field<sage.rings.number_field.number_field.CyclotomicFieldFactory>`,
        a :func:`NumberField`, or :class:`QQbar<AlgebraicField>`) into
        :class:`QQbar<AlgebraicField>`.

        This embedding is useful for getting a better sense for the
        F-symbols, particularly when they are computed as elements of a
        :func:`NumberField`. See also :meth:`get_non_cyclotomic_roots`.

        EXAMPLES::

            sage: fr = FusionRing("G2", 1)
            sage: f = fr.get_fmatrix(fusion_label=\'g\', inject_variables=True, new=True)
            creating variables fx1..fx5
            Defining fx0, fx1, fx2, fx3, fx4
            sage: f.find_orthogonal_solution()
            Computing F-symbols for The Fusion Ring of Type G2 and level 1 with Integer Ring coefficients with 5 variables...
            Set up 10 hex and orthogonality constraints...
            Partitioned 10 equations into 2 components of size:
            [4, 1]
            Elimination epoch completed... 0 eqns remain in ideal basis
            Hex elim step solved for 4 / 5 variables
            Set up 0 reduced pentagons...
            Pent elim step solved for 4 / 5 variables
            Partitioned 0 equations into 0 components of size:
            []
            Partitioned 1 equations into 1 components of size:
            [1]
            Computing appropriate NumberField...
            sage: phi = f.get_qqbar_embedding()
            sage: phi(f.fmat(g1, g1, g1, g1, g1, g1)).n()
            -0.618033988749895 + 1.46674215951686e-29*I
        '''
    def get_coerce_map_from_fr_cyclotomic_field(self):
        '''
        Return a coercion map from the associated :class:`FusionRing`\'s
        cyclotomic field into the base field containing all F-symbols
        (this could be the :class:`FusionRing`\'s
        :class:`Cyclotomic field<sage.rings.number_field.number_field.CyclotomicFieldFactory>`,
        a :func:`NumberField`, or :class:`QQbar<AlgebraicField>`).

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.FR().field()
            Cyclotomic Field of order 60 and degree 16
            sage: f.field()
            Number Field in a with defining polynomial y^32 - ... - 22*y^2 + 1
            sage: phi = f.get_coerce_map_from_fr_cyclotomic_field()
            sage: phi.domain() == f.FR().field()
            True
            sage: phi.codomain() == f.field()
            True

        When F-symbols are computed as elements of the associated
        :class:`FusionRing`\'s base
        :class:`Cyclotomic field<sage.rings.number_field.number_field.CyclotomicFieldFactory>`,
        we have ``self.field() == self.FR().field()`` and this
        returns the identity map on ``self.field()``. ::

            sage: f = FusionRing("A2", 1).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False)
            sage: phi = f.get_coerce_map_from_fr_cyclotomic_field()
            sage: f.field()
            Cyclotomic Field of order 48 and degree 16
            sage: f.field() == f.FR().field()
            True
            sage: phi.domain() == f.field()
            True
            sage: phi.is_identity()
            True
        '''
    def get_fvars_in_alg_field(self):
        '''
        Return F-symbols as elements of the :class:`QQbar<AlgebraicField>`.

        This method uses the embedding defined by
        :meth:`get_qqbar_embedding` to coerce
        F-symbols into :class:`QQbar<AlgebraicField>`.

        EXAMPLES::

            sage: fr = FusionRing("G2", 1)
            sage: f = fr.get_fmatrix(fusion_label=\'g\', inject_variables=True, new=True)
            creating variables fx1..fx5
            Defining fx0, fx1, fx2, fx3, fx4
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.field()
            Number Field in a with defining polynomial y^32 - ... - 22*y^2 + 1
            sage: f.get_fvars_in_alg_field()
            {(g1, g1, g1, g0, g1, g1): 1,
             (g1, g1, g1, g1, g0, g0): 0.61803399? + 0.?e-8*I,
             (g1, g1, g1, g1, g0, g1): -0.7861514? + 0.?e-8*I,
             (g1, g1, g1, g1, g1, g0): -0.7861514? + 0.?e-8*I,
             (g1, g1, g1, g1, g1, g1): -0.61803399? + 0.?e-8*I}
        '''
    def get_radical_expression(self):
        '''
        Return a radical expression of F-symbols.

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix()
            sage: f.FR().fusion_labels("g", inject_variables=True)
            sage: f.find_orthogonal_solution(verbose=False)
            sage: radical_fvars = f.get_radical_expression()       # long time (~1.5s)
            sage: radical_fvars[g1, g1, g1, g1, g1, g0]            # long time
            -sqrt(1/2*sqrt(5) - 1/2)
        '''
    def largest_fmat_size(self):
        '''
        Get the size of the largest F-matrix `F^{abc}_d`.

        EXAMPLES::

            sage: f = FusionRing("B3", 2).get_fmatrix()
            sage: f.largest_fmat_size()
            4
        '''
    def get_fvars_by_size(self, n, indices: bool = False):
        '''
        Return the set of F-symbols that are entries of an `n \\times n` matrix
        `F^{a, b, c}_d`.

        INPUT:

        - ``n`` -- positive integer
        - ``indices`` -- boolean (default: ``False``)

        If ``indices`` is ``False`` (default),
        this method returns a set of sextuples `(a, b, c, d, x, y)` identifying
        the corresponding F-symbol. Each sextuple is a key in the
        dictionary returned by :meth:`get_fvars`.

        Otherwise the method returns a list of integer indices that
        internally identify the F-symbols. The ``indices=True`` option is
        meant for internal use.

        EXAMPLES::

            sage: f = FusionRing("A2", 2).get_fmatrix(inject_variables=True)
            creating variables fx1..fx287
            Defining fx0, ..., fx286
            sage: f.largest_fmat_size()
            2
            sage: f.get_fvars_by_size(2)
            {(f2, f2, f2, f4, f1, f1),
             (f2, f2, f2, f4, f1, f5),
             ...
             (f4, f4, f4, f4, f4, f0),
             (f4, f4, f4, f4, f4, f4)}
        '''
    def save_fvars(self, filename) -> None:
        '''
        Save computed F-symbols for later use.

        INPUT:

        - ``filename`` -- string specifying the name of the pickle file
          to be used

        The current directory is used unless an absolute path to a file in
        a different directory is provided.

        .. NOTE::

            This method should only be used *after* successfully running one
            of the solvers, e.g. :meth:`find_cyclotomic_solution` or
            :meth:`find_orthogonal_solution`.

        When used in conjunction with :meth:`load_fvars`, this method may
        be used to restore state of an :class:`FMatrix` object at the end
        of a successful F-matrix solver run.

        EXAMPLES::

            sage: f = FusionRing("A2", 1).get_fmatrix(new=True)
            sage: f.find_orthogonal_solution(verbose=False)
            sage: fvars = f.get_fvars()
            sage: K = f.field()
            sage: filename = f.get_fr_str() + "_solver_results.pickle"
            sage: f.save_fvars(filename)
            sage: del f
            sage: f2 = FusionRing("A2", 1).get_fmatrix(new=True)
            sage: f2.load_fvars(filename)
            sage: fvars == f2.get_fvars()
            True
            sage: K == f2.field()
            True
            sage: os.remove(filename)
        '''
    def load_fvars(self, filename) -> None:
        '''
        Load previously computed F-symbols from a pickle file.

        See :meth:`save_fvars` for more information.

        EXAMPLES::

            sage: f = FusionRing("A2", 1).get_fmatrix(new=True)
            sage: f.find_orthogonal_solution(verbose=False)
            sage: fvars = f.get_fvars()
            sage: K = f.field()
            sage: filename = f.get_fr_str() + "_solver_results.pickle"
            sage: f.save_fvars(filename)
            sage: del f
            sage: f2 = FusionRing("A2", 1).get_fmatrix(new=True)
            sage: f2.load_fvars(filename)
            sage: fvars == f2.get_fvars()
            True
            sage: K == f2.field()
            True
            sage: os.remove(filename)

        .. NOTE::

            :meth:`save_fvars`. This method does not work with intermediate
            checkpoint pickles; it only works with pickles containing *all*
            F-symbols, i.e. those created by :meth:`save_fvars` and by
            specifying an optional ``save_results`` parameter for
            :meth:`find_orthogonal_solution`.
        '''
    def get_fr_str(self):
        '''
        Auto-generate an identifying key for saving results.

        EXAMPLES::

            sage: f = FusionRing("B3", 1).get_fmatrix()
            sage: f.get_fr_str()
            \'B31\'
        '''
    def start_worker_pool(self, processes=None) -> None:
        '''
        Initialize a ``multiprocessing`` worker pool for parallel processing,
        which may be used e.g. to set up defining equations using
        :meth:`get_defining_equations`.

        This method sets ``self``\'s ``pool`` attribute. The worker
        pool may be used time and again. Upon initialization, each process
        in the pool attaches to the necessary shared memory resources.

        When you are done using the worker pool, use
        :meth:`shutdown_worker_pool` to close the pool and properly dispose
        of shared memory resources.

        INPUT:

        - ``processes`` -- integer indicating the number of workers
          in the pool; if left unspecified, the number of workers
          equals the number of processors available

        OUTPUT: boolean; whether a worker pool was successfully initialized

        EXAMPLES::

            sage: f = FusionRing("G2", 1).get_fmatrix(new=True)
            sage: f.start_worker_pool()
            sage: he = f.get_defining_equations(\'hexagons\')
            sage: sorted(he)
            [fx0 - 1,
             fx2*fx3 + (zeta60^14 + zeta60^12 - zeta60^6 - zeta60^4 + 1)*fx4^2 + (zeta60^6)*fx4,
             fx1*fx3 + (zeta60^14 + zeta60^12 - zeta60^6 - zeta60^4 + 1)*fx3*fx4 + (zeta60^14 - zeta60^4)*fx3,
             fx1*fx2 + (zeta60^14 + zeta60^12 - zeta60^6 - zeta60^4 + 1)*fx2*fx4 + (zeta60^14 - zeta60^4)*fx2,
             fx1^2 + (zeta60^14 + zeta60^12 - zeta60^6 - zeta60^4 + 1)*fx2*fx3 + (-zeta60^12)*fx1]
            sage: pe = f.get_defining_equations(\'pentagons\')
            sage: f.shutdown_worker_pool()

        .. WARNING::

            This method is needed to initialize the worker pool using the
            necessary shared memory resources. Simply using the
            ``multiprocessing.Pool`` constructor will not work with our
            class methods.

        .. WARNING::

            Failure to call :meth:`shutdown_worker_pool` may result in a memory
            leak, since shared memory resources outlive the process that created
            them.
        '''
    def shutdown_worker_pool(self) -> None:
        '''
        Shutdown the given worker pool and dispose of shared memory resources
        created when the pool was set up using :meth:`start_worker_pool`.

        .. WARNING::

            Failure to call this method after using :meth:`start_worker_pool`
            to create a process pool may result in a memory
            leak, since shared memory resources outlive the process that
            created them.

        EXAMPLES::

            sage: f = FusionRing("A1", 3).get_fmatrix(new=True)
            sage: f.start_worker_pool()
            sage: he = f.get_defining_equations(\'hexagons\')
            sage: f.shutdown_worker_pool()
        '''
    def get_orthogonality_constraints(self, output: bool = True):
        '''
        Get equations imposed on the F-matrix by orthogonality.

        INPUT:

        - ``output`` -- boolean

        OUTPUT:

        If ``output=True``, orthogonality constraints are returned as
        polynomial objects.

        Otherwise, the constraints are appended to ``self.ideal_basis``.
        They are stored in the internal tuple representation. The
        ``output=False`` option is meant mostly for internal use by the
        F-matrix solver.

        EXAMPLES::

            sage: f = FusionRing("B4", 1).get_fmatrix()
            sage: f.get_orthogonality_constraints()
            [fx0^2 - 1,
             fx1^2 - 1,
             fx2^2 - 1,
             fx3^2 - 1,
             fx4^2 - 1,
             fx5^2 - 1,
             fx6^2 - 1,
             fx7^2 - 1,
             fx8^2 - 1,
             fx9^2 - 1,
             fx10^2 + fx12^2 - 1,
             fx10*fx11 + fx12*fx13,
             fx10*fx11 + fx12*fx13,
             fx11^2 + fx13^2 - 1]
        '''
    def get_defining_equations(self, option, output: bool = True):
        '''
        Get the equations defining the ideal generated by the hexagon or
        pentagon relations.

        INPUT:

        - ``option`` -- string determining equations to be set up:

          * ``\'hexagons\'`` -- get equations imposed on the F-matrix by
            the hexagon relations in the definition of a braided category

          * ``\'pentagons\'`` -- get equations imposed on the F-matrix by
            the pentagon relations in the definition of a monoidal category

        - ``output`` -- boolean (default: ``True``); whether
          results should be returned, where the equations will be polynomials.
          Otherwise, the constraints are appended to ``self.ideal_basis``.
          Constraints are stored in the internal tuple representation. The
          ``output=False`` option is meant only for internal use by the
          F-matrix solver. When computing the hexagon equations with the
          ``output=False`` option, the initial state of the F-symbols is used.

        .. NOTE::

            To set up the defining equations using parallel processing,
            use :meth:`start_worker_pool` to initialize multiple processes
            *before* calling this method.

        EXAMPLES::

            sage: f = FusionRing("B2", 1).get_fmatrix()
            sage: sorted(f.get_defining_equations(\'hexagons\'))
            [fx7 + 1,
             fx6 - 1,
             fx2 + 1,
             fx0 - 1,
             fx11*fx12 + (-zeta32^8)*fx13^2 + (zeta32^12)*fx13,
             fx10*fx12 + (-zeta32^8)*fx12*fx13 + (zeta32^4)*fx12,
             fx10*fx11 + (-zeta32^8)*fx11*fx13 + (zeta32^4)*fx11,
             fx10^2 + (-zeta32^8)*fx11*fx12 + (-zeta32^12)*fx10,
             fx4*fx9 + fx7,
             fx3*fx8 - fx6,
             fx1*fx5 + fx2]
            sage: pe = f.get_defining_equations(\'pentagons\')
            sage: len(pe)
            33
        '''
    def equations_graph(self, eqns=None):
        '''
        Construct a graph corresponding to the given equations.

        Every node corresponds to a variable and nodes are connected when
        the corresponding variables appear together in an equation.

        INPUT:

        - ``eqns`` -- list of polynomials

        Each polynomial is either an object in the ring returned by
        :meth:`get_poly_ring` or it is a tuple of pairs representing
        a polynomial using the internal representation.

        If no list of equations is passed, the graph is built from the
        polynomials in ``self.ideal_basis``. In this case the method assumes
        the internal representation of a polynomial as a tuple of pairs is
        used.

        This method is crucial to :meth:`find_orthogonal_solution`. The
        hexagon equations, obtained using :meth:`get_defining_equations`,
        define a disconnected graph that breaks up into many small components.
        The :meth:`find_orthogonal_solution` solver exploits this when
        undertaking a Groebner basis computation.

        OUTPUT:

        A ``Graph`` object. If a list of polynomial objects was given,
        the set of nodes in the output graph is the subset polynomial
        ring generators appearing in the equations.

        If the internal representation was used, the set of nodes is
        the subset of indices corresponding to polynomial ring generators.
        This option is meant for internal use by the F-matrix solver.

        EXAMPLES::

            sage: f = FusionRing("A3", 1).get_fmatrix()
            sage: f.get_poly_ring().ngens()
            27
            sage: he = f.get_defining_equations(\'hexagons\')
            sage: graph = f.equations_graph(he)
            sage: graph.connected_components_sizes()
            [6, 3, 3, 3, 3, 3, 3, 1, 1, 1]
        '''
    def attempt_number_field_computation(self) -> bool:
        '''
        Based on the ``CartanType`` of ``self`` and data
        known on March 17, 2021, determine whether to attempt
        to find a :func:`NumberField` containing all the F-symbols.

        This method is used by :meth:`find_orthogonal_solution`
        to determine a field containing all F-symbols.
        See :meth:`field` and :meth:`get_non_cyclotomic_roots`.

        For certain :class:`fusion rings <FusionRing>`, the number field
        computation does not terminate in reasonable time.
        In these cases, we report F-symbols as elements
        of the :class:`QQbar<AlgebraicField>`.

        EXAMPLES::

            sage: f = FusionRing("F4", 2).get_fmatrix()
            sage: f.attempt_number_field_computation()
            False
            sage: f = FusionRing("G2", 1).get_fmatrix()
            sage: f.attempt_number_field_computation()
            True

        .. NOTE::

            In certain cases, F-symbols are found in the associated
            :class:`FusionRing`\'s cyclotomic field and a
            :func:`NumberField` computation is not needed. In these
            cases this method returns ``True`` but the
            :meth:`find_orthogonal_solution` solver does *not*
            undertake a :func:`NumberField` computation.
        '''
    def find_orthogonal_solution(self, checkpoint: bool = False, save_results: str = '', warm_start: str = '', use_mp: bool = True, verbose: bool = True) -> None:
        '''
        Solve the hexagon and pentagon relations, along with
        orthogonality constraints, to evaluate an orthogonal F-matrix.

        INPUT:

        - ``checkpoint`` -- boolean (default: ``False``); whether
          the computation should be checkpointed. Depending on the associated
          ``CartanType``, the computation may take hours to complete. For
          large examples, checkpoints are recommended. This method supports
          "warm" starting, so the calculation may be resumed from a checkpoint,
          using the ``warm_start`` option.

          Checkpoints store necessary state in the pickle file
          ``"fmatrix_solver_checkpoint_" + key + ".pickle"``, where ``key``
          is the result of :meth:`get_fr_str`.

          Checkpoint pickles are automatically deleted when the solver exits
          a successful run.

        - ``save_results`` -- (optional) a string indicating the name of a
          pickle file in which to store calculated F-symbols for later use.

          If ``save_results`` is not provided (default), F-matrix results
          are not stored to file.

          The F-symbols may be saved to file after running the solver using
          :meth:`save_fvars`.

        - ``warm_start`` -- (optional) a string indicating the name of a pickle
          file containing checkpointed solver state. This file must have been
          produced by a previous call to the solver using the ``checkpoint``
          option.

          If no file name is provided, the calculation begins from scratch.

        - ``use_mp`` -- boolean (default: ``True``); whether to use
          multiprocessing to speed up calculation. The default value
          ``True`` is highly recommended, since parallel processing yields
          results much more quickly.

        - ``verbose`` -- boolean (default: ``True``); whether the
          solver should print out intermediate progress reports

        OUTPUT:

        This method returns ``None``. If the solver runs successfully, the
        results may be accessed through various methods, such as
        :meth:`get_fvars`, :meth:`fmatrix`, :meth:`fmat`, etc.

        EXAMPLES::

            sage: f = FusionRing("B5", 1).get_fmatrix(fusion_label=\'b\', inject_variables=True)
            creating variables fx1..fx14
            Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx13
            sage: f.find_orthogonal_solution()
            Computing F-symbols for The Fusion Ring of Type B5 and level 1 with Integer Ring coefficients with 14 variables...
            Set up 25 hex and orthogonality constraints...
            Partitioned 25 equations into 5 components of size:
            [4, 3, 3, 3, 1]
            Elimination epoch completed... 0 eqns remain in ideal basis
            Hex elim step solved for 10 / 14 variables
            Set up 7 reduced pentagons...
            Elimination epoch completed... 0 eqns remain in ideal basis
            Pent elim step solved for 12 / 14 variables
            Partitioned 0 equations into 0 components of size:
            []
            Partitioned 2 equations into 2 components of size:
            [1, 1]
            sage: f.fmatrix(b2, b2, b2, b2)
            [ 1/2*zeta80^30 - 1/2*zeta80^10 -1/2*zeta80^30 + 1/2*zeta80^10]
            [ 1/2*zeta80^30 - 1/2*zeta80^10  1/2*zeta80^30 - 1/2*zeta80^10]
            sage: f.fmat(b2, b2, b2, b2, b0, b1)
            -1/2*zeta80^30 + 1/2*zeta80^10

        Every F-matrix `F^{a, b, c}_d` is orthogonal and in many cases real.
        We may use :meth:`fmats_are_orthogonal` and :meth:`fvars_are_real`
        to obtain correctness certificates.

        EXAMPLES::

            sage: f.fmats_are_orthogonal()
            True

        In any case, the F-symbols are obtained as elements of the associated
        :class:`FusionRing`\'s
        :class:`Cyclotomic field<sage.rings.number_field.number_field.CyclotomicFieldFactory>`,
        a computed :func:`NumberField`, or :class:`QQbar<AlgebraicField>`.
        Currently, the field containing the F-symbols is determined based
        on the ``CartanType`` associated to ``self``.

        .. SEEALSO::

            :meth:`attempt_number_field_computation`
        '''
    def find_cyclotomic_solution(self, equations=None, algorithm: str = '', verbose: bool = True, output: bool = False):
        '''
        Solve the hexagon and pentagon relations to evaluate the F-matrix.

        This method (omitting the orthogonality constraints) produces
        output in the cyclotomic field, but it is very limited in the size
        of examples it can handle: for example, `G_2` at level 2 is
        too large for this method. You may use :meth:`find_orthogonal_solution`
        to solve much larger examples.

        INPUT:

        - ``equations`` -- (optional) a set of equations to be
          solved; defaults to the hexagon and pentagon equations
        - ``algorithm`` -- (optional) algorithm to compute Groebner Basis
        - ``output`` -- boolean (default: ``False``); output a dictionary of
          F-matrix values; this may be useful to see but may be omitted
          since this information will be available afterwards via the
          :meth:`fmatrix` and :meth:`fmat` methods.

        EXAMPLES::

            sage: fr = FusionRing("A2", 1, fusion_labels=\'a\', inject_variables=True)
            sage: f = fr.get_fmatrix(inject_variables=True)
            creating variables fx1..fx8
            Defining fx0, fx1, fx2, fx3, fx4, fx5, fx6, fx7
            sage: f.find_cyclotomic_solution(output=True)
            Setting up hexagons and pentagons...
            Finding a Groebner basis...
            Solving...
            Fixing the gauge...
            adding equation... fx4 - 1
            Done!
            {(a2, a2, a2, a0, a1, a1): 1,
             (a2, a2, a1, a2, a1, a0): 1,
             (a2, a1, a2, a2, a0, a0): 1,
             (a2, a1, a1, a1, a0, a2): 1,
             (a1, a2, a2, a2, a0, a1): 1,
             (a1, a2, a1, a1, a0, a0): 1,
             (a1, a1, a2, a1, a2, a0): 1,
             (a1, a1, a1, a0, a2, a2): 1}

        After you successfully run :meth:`find_cyclotomic_solution` you may
        check the correctness of the F-matrix by running
        :meth:`get_defining_equations` with ``option=\'hexagons\'`` and
        ``option=\'pentagons\'``. These should return empty lists
        of equations.

        EXAMPLES::

            sage: f.get_defining_equations("hexagons")
            []
            sage: f.get_defining_equations("pentagons")
            []
        '''
    def fmats_are_orthogonal(self):
        '''
        Verify that all F-matrices are orthogonal.

        This method should always return ``True`` when called after running
        :meth:`find_orthogonal_solution`.

        EXAMPLES::

            sage: f = FusionRing("D4", 1).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False)
            sage: f.fmats_are_orthogonal()
            True
        '''
    def fvars_are_real(self):
        '''
        Test whether all F-symbols are real.

        EXAMPLES::

            sage: f = FusionRing("A1", 3).get_fmatrix()
            sage: f.find_orthogonal_solution(verbose=False) # long time
            sage: f.fvars_are_real()                        # not tested (cypari issue in doctesting framework)
            True
        '''
    def certify_pentagons(self, use_mp: bool = True, verbose: bool = False):
        '''
        Obtain a certificate of satisfaction for the pentagon equations,
        up to floating-point error.

        This method converts the computed F-symbols (available through
        :meth:`get_fvars`) to native Python floats and then checks whether
        the pentagon equations are satisfied using floating point arithmetic.

        When ``self.FR().basis()`` has many elements, verifying satisfaction
        of the pentagon relations exactly using :meth:`get_defining_equations`
        with ``option="pentagons"`` may take a long time. This method is
        faster, but it cannot provide mathematical guarantees.

        EXAMPLES::

            sage: f = FusionRing("C3", 1).get_fmatrix()
            sage: f.find_orthogonal_solution()        # long time
            Computing F-symbols for The Fusion Ring of Type C3 and level 1 with Integer Ring coefficients with 71 variables...
            Set up 134 hex and orthogonality constraints...
            Partitioned 134 equations into 17 components of size:
            [12, 12, 6, 6, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1]
            Elimination epoch completed... 10 eqns remain in ideal basis
            Elimination epoch completed... 0 eqns remain in ideal basis
            Hex elim step solved for 51 / 71 variables
            Set up 121 reduced pentagons...
            Elimination epoch completed... 18 eqns remain in ideal basis
            Elimination epoch completed... 5 eqns remain in ideal basis
            Pent elim step solved for 64 / 71 variables
            Partitioned 5 equations into 1 components of size:
            [4]
            Elimination epoch completed... 0 eqns remain in ideal basis
            Partitioned 6 equations into 6 components of size:
            [1, 1, 1, 1, 1, 1]
            Computing appropriate NumberField...
            sage: f.certify_pentagons()  is None      # not tested (cypari issue in doctesting framework), long time (~1.5s)
            True
        '''
