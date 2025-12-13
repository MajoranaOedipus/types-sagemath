from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.elliptic_curves.ell_field import EllipticCurve_field as EllipticCurve_field
from sage.schemes.elliptic_curves.ell_number_field import EllipticCurve_number_field as EllipticCurve_number_field
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class IsogenyClass_EC(SageObject):
    """
    Isogeny class of an elliptic curve.

    .. NOTE::

        The current implementation chooses a curve from each isomorphism
        class in the isogeny class. Over `\\QQ` this is a unique reduced
        minimal model in each isomorphism class.  Over number fields the
        model chosen may change in future.
    """
    E: Incomplete
    def __init__(self, E, label=None, empty: bool = False) -> None:
        '''
        Over `\\QQ` we use curves since minimal models exist and there
        is a canonical choice of one.

        INPUT:

        - ``label`` -- string or ``None``, a Cremona or LMFDB label, used
          in printing; ignored if base field is not `\\QQ`

        EXAMPLES::

            sage: cls = EllipticCurve(\'1011b1\').isogeny_class()
            sage: print("\\n".join(repr(E) for E in cls.curves))
            Elliptic Curve defined by y^2 + x*y = x^3 - 8*x - 9 over Rational Field
            Elliptic Curve defined by y^2 + x*y = x^3 - 23*x + 30 over Rational Field
        '''
    def __len__(self) -> int:
        """
        The number of curves in the class.

        EXAMPLES::

            sage: E = EllipticCurve('15a')
            sage: len(E.isogeny_class()) # indirect doctest
            8
        """
    def __iter__(self):
        """
        Iterator over curves in the class.

        EXAMPLES::

            sage: E = EllipticCurve('15a')
            sage: all(C.conductor() == 15 for C in E.isogeny_class()) # indirect doctest
            True
        """
    def __getitem__(self, i):
        """
        Return the `i`-th curve in the class.

        EXAMPLES::

            sage: E = EllipticCurve('990j1')
            sage: iso = E.isogeny_class(order='lmfdb') # orders lexicographically on a-invariants
            sage: iso[2] == E # indirect doctest
            True
        """
    def index(self, C):
        """
        Return the index of a curve in this class.

        INPUT:

        - ``C`` -- an elliptic curve in this isogeny class

        OUTPUT:

        - ``i`` -- integer so that the ``i`` th curve in the class
          is isomorphic to ``C``

        EXAMPLES::

            sage: E = EllipticCurve('990j1')
            sage: iso = E.isogeny_class(order='lmfdb') # orders lexicographically on a-invariants
            sage: iso.index(E.short_weierstrass_model())
            2
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        If they are different, compares the sorted underlying lists of
        curves.

        Note that two isogeny classes with different orderings will
        compare as the same.  If you want to include the ordering,
        just compare the list of curves.

        EXAMPLES::

            sage: E = EllipticCurve('990j1')
            sage: EE = EllipticCurve('990j4')
            sage: E.isogeny_class() == EE.isogeny_class() # indirect doctest
            True
        """
    def __hash__(self):
        """
        Hash is based on the a-invariants of the sorted list of
        minimal models.

        EXAMPLES::

            sage: E = EllipticCurve('990j1')
            sage: C = E.isogeny_class()
            sage: hash(C) == hash(tuple(sorted([curve.a_invariants() for curve in C.curves]))) # indirect doctest
            True
        """
    def __contains__(self, x) -> bool:
        """
        INPUT:

        - ``x`` -- a Python object

        OUTPUT: boolean; ``True`` iff ``x`` is an elliptic curve in this
        isogeny class

        .. NOTE::

            If the input is isomorphic but not identical to a curve in
            the class, then ``False`` will be returned.

        EXAMPLES::

            sage: cls = EllipticCurve('15a3').isogeny_class()
            sage: E = EllipticCurve('15a7'); E in cls
            True
            sage: E.short_weierstrass_model() in cls
            True
        """
    @cached_method
    def matrix(self, fill: bool = True):
        """
        Return the matrix whose entries give the minimal degrees of
        isogenies between curves in this class.

        INPUT:

        - ``fill`` -- boolean (default: ``True``); if ``False`` then the
          matrix will contain only zeros and prime entries. If ``True`` it
          will fill in the other degrees.

        EXAMPLES::

            sage: isocls = EllipticCurve('15a3').isogeny_class()
            sage: isocls.matrix()
            [ 1  2  2  2  4  4  8  8]
            [ 2  1  4  4  8  8 16 16]
            [ 2  4  1  4  8  8 16 16]
            [ 2  4  4  1  2  2  4  4]
            [ 4  8  8  2  1  4  8  8]
            [ 4  8  8  2  4  1  2  2]
            [ 8 16 16  4  8  2  1  4]
            [ 8 16 16  4  8  2  4  1]
            sage: isocls.matrix(fill=False)
            [0 2 2 2 0 0 0 0]
            [2 0 0 0 0 0 0 0]
            [2 0 0 0 0 0 0 0]
            [2 0 0 0 2 2 0 0]
            [0 0 0 2 0 0 0 0]
            [0 0 0 2 0 0 2 2]
            [0 0 0 0 0 2 0 0]
            [0 0 0 0 0 2 0 0]
        """
    @cached_method
    def qf_matrix(self):
        """
        Return the array whose entries are quadratic forms
        representing the degrees of isogenies between curves in this
        class (CM case only).

        OUTPUT:

        a `2x2` array (list of lists) of list, each of the form [2] or
        [2,1,3] representing the coefficients of an integral quadratic
        form in 1 or 2 variables whose values are the possible isogeny
        degrees between the i'th and j'th curve in the class.

        EXAMPLES::

            sage: pol = PolynomialRing(QQ,'x')([1,0,3,0,1])
            sage: K.<c> = NumberField(pol)
            sage: j = 1480640 + 565760*c^2
            sage: E = EllipticCurve(j=j)
            sage: C = E.isogeny_class()
            sage: C.qf_matrix()
            [[[1], [2, 2, 3]], [[2, 2, 3], [1]]]
        """
    @cached_method
    def isogenies(self, fill: bool = False):
        """
        Return a list of lists of isogenies and 0s, corresponding to
        the entries of :meth:`matrix`

        INPUT:

        - ``fill`` -- boolean (default: ``False``); whether to only return
          prime degree isogenies.  Currently only implemented for
          ``fill=False``.

        OUTPUT:

        - a list of lists, where the ``j`` th entry of the ``i`` th list
          is either zero or a prime degree isogeny from the ``i`` th curve
          in this class to the ``j`` th curve.

        .. WARNING::

            The domains and codomains of the isogenies will have the same
            Weierstrass equation as the curves in this class, but they
            may not be identical python objects in the current
            implementation.

        EXAMPLES::

            sage: isocls = EllipticCurve('15a3').isogeny_class()
            sage: f = isocls.isogenies()[0][1]; f
            Isogeny of degree 2
              from Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 5*x + 2 over Rational Field
                to Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 80*x + 242 over Rational Field
            sage: f.domain() == isocls.curves[0] and f.codomain() == isocls.curves[1]
            True
        """
    @cached_method
    def graph(self):
        """
        Return a graph whose vertices correspond to curves in this
        class, and whose edges correspond to prime degree isogenies.

        .. NOTE::

            There are only finitely many possible isogeny graphs for
            curves over `\\QQ` [Maz1978b].  This function tries to lay out
            the graph nicely by special casing each isogeny graph.
            This could also be done over other number fields, such as
            quadratic fields.

        .. NOTE::

            The vertices are labeled 1 to n rather than 0 to n-1 to
            match LMFDB and Cremona labels for curves over `\\QQ`.

        EXAMPLES::

            sage: isocls = EllipticCurve('15a3').isogeny_class()
            sage: G = isocls.graph()
            sage: sorted(G._pos.items())
            [(1, [-0.8660254, 0.5]), (2, [-0.8660254, 1.5]), (3, [-1.7320508, 0]),
             (4, [0, 0]), (5, [0, -1]), (6, [0.8660254, 0.5]),
             (7, [0.8660254, 1.5]), (8, [1.7320508, 0])]
        """
    @cached_method
    def reorder(self, order):
        '''
        Return a new isogeny class with the curves reordered.

        INPUT:

        - ``order`` -- ``None``, a string or an iterable over all curves in
          this class.  See
          :meth:`sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.isogeny_class`
          for more details.

        OUTPUT:

        Another :class:`IsogenyClass_EC` with the curves reordered (and
        matrices and maps changed as appropriate).

        EXAMPLES::

            sage: isocls = EllipticCurve(\'15a1\').isogeny_class()
            sage: print("\\n".join(repr(C) for C in isocls.curves))
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 10*x - 10 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 5*x + 2 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + 35*x - 28 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 135*x - 660 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 80*x + 242 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 110*x - 880 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 2160*x - 39540 over Rational Field
            sage: isocls2 = isocls.reorder(\'lmfdb\')
            sage: print("\\n".join(repr(C) for C in isocls2.curves))
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 2160*x - 39540 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 135*x - 660 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 110*x - 880 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 80*x + 242 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 10*x - 10 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 5*x + 2 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + 35*x - 28 over Rational Field
        '''

class IsogenyClass_EC_NumberField(IsogenyClass_EC):
    """
    Isogeny classes for elliptic curves over number fields.
    """
    def __init__(self, E, reducible_primes=None, algorithm: str = 'Billerey', minimal_models: bool = True) -> None:
        """
        INPUT:

        - ``E`` -- an elliptic curve over a number field

        - ``reducible_primes`` -- list of integers, or ``None`` (default); if
          not ``None`` then this should be a list of primes; in computing the
          isogeny class, only composites isogenies of these degrees will be used.

        - ``algorithm`` -- string (default: ``'Billerey'``); the algorithm
          to use to compute the reducible primes.  Ignored for CM
          curves or if ``reducible_primes`` is provided.  Values are
          ``'Billerey'`` (default), ``'Larson'``, and ``'heuristic'``.

        - ``minimal_models`` -- boolean (default: ``True``); if ``True``,
          all curves in the class will be minimal or semi-minimal
          models.  Over fields of larger degree it can be expensive to
          compute these so set to ``False``.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve(K, [0,0,0,0,1])
            sage: C = E.isogeny_class(); C
            Isogeny class of Elliptic Curve defined by y^2 = x^3 + 1
            over Number Field in i with defining polynomial x^2 + 1 with i = 1*I

        The curves in the class (sorted)::

            sage: [E1.ainvs() for E1 in C]
            [(0, 0, 0, 0, -27),
             (0, 0, 0, 0, 1),
             (i + 1, i, 0, 3, -i),
             (i + 1, i, 0, 33, 91*i)]

        The matrix of degrees of cyclic isogenies between curves::

            sage: C.matrix()
            [1 3 6 2]
            [3 1 2 6]
            [6 2 1 3]
            [2 6 3 1]

        The array of isogenies themselves is not filled out but only
        contains those used to construct the class, the other entries
        containing the integer 0.  This will be changed when the
        class :class:`EllipticCurveIsogeny` allowed composition.  In
        this case we used `2`-isogenies to go from 0 to 2 and from 1
        to 3, and `3`-isogenies to go from 0 to 1 and from 2 to 3::

            sage: isogs = C.isogenies()
            sage: [((i,j), isogs[i][j].degree())
            ....:  for i in range(4) for j in range(4) if isogs[i][j] != 0]
            [((0, 1), 3),
             ((0, 3), 2),
             ((1, 0), 3),
             ((1, 2), 2),
             ((2, 1), 2),
             ((2, 3), 3),
             ((3, 0), 2),
             ((3, 2), 3)]
            sage: [((i,j), isogs[i][j].x_rational_map())
            ....:  for i in range(4) for j in range(4) if isogs[i][j] != 0]
            [((0, 1), (1/9*x^3 - 12)/x^2),
             ((0, 3), (1/2*i*x^2 - 2*i*x + 15*i)/(x - 3)),
             ((1, 0), (x^3 + 4)/x^2),
             ((1, 2), (1/2*i*x^2 + i)/(x + 1)),
             ((2, 1), (-1/2*i*x^2 - 1/2*i)/(x - 1/2*i)),
             ((2, 3), (x^3 - 2*i*x^2 - 7*x + 4*i)/(x^2 - 2*i*x - 1)),
             ((3, 0), (-1/2*i*x^2 + 2*x - 5/2*i)/(x + 7/2*i)),
             ((3, 2), (1/9*x^3 + 2/3*i*x^2 - 13/3*x - 116/9*i)/(x^2 + 10*i*x - 25))]

            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve([1+i, -i, i, 1, 0])
            sage: C = E.isogeny_class(); C
            Isogeny class of Elliptic Curve defined
             by y^2 + (i+1)*x*y + i*y = x^3 + (-i)*x^2 + x
             over Number Field in i with defining polynomial x^2 + 1 with i = 1*I
            sage: len(C)
            6
            sage: C.matrix()
            [ 1  3  9 18  6  2]
            [ 3  1  3  6  2  6]
            [ 9  3  1  2  6 18]
            [18  6  2  1  3  9]
            [ 6  2  6  3  1  3]
            [ 2  6 18  9  3  1]
            sage: [E1.ainvs() for E1 in C]
            [(i + 1, i - 1, i, -i - 1, -i + 1),
            (i + 1, i - 1, i, 14*i + 4, 7*i + 14),
            (i + 1, i - 1, i, 59*i + 99, 372*i - 410),
            (i + 1, -i, i, -240*i - 399, 2869*i + 2627),
            (i + 1, -i, i, -5*i - 4, 2*i + 5),
            (i + 1, -i, i, 1, 0)]

        An example with CM by `\\sqrt{-5}`::

            sage: pol = PolynomialRing(QQ,'x')([1,0,3,0,1])
            sage: K.<c> = NumberField(pol)
            sage: j = 1480640 + 565760*c^2
            sage: E = EllipticCurve(j=j)
            sage: E.has_cm()
            True
            sage: E.has_rational_cm()
            True
            sage: E.cm_discriminant()
            -20
            sage: C = E.isogeny_class()
            sage: len(C)
            2
            sage: C.matrix()
            [1 2]
            [2 1]
            sage: [E.ainvs() for E in C]
            [(0, 0, 0, 83490*c^2 - 147015, -64739840*c^2 - 84465260),
             (0, 0, 0, -161535*c^2 + 70785, -62264180*c^3 + 6229080*c)]
            sage: C.isogenies()[0][1]
            Isogeny of degree 2
              from Elliptic Curve defined by
                   y^2 = x^3 + (83490*c^2-147015)*x + (-64739840*c^2-84465260)
                   over Number Field in c with defining polynomial x^4 + 3*x^2 + 1
                to Elliptic Curve defined by
                   y^2 = x^3 + (-161535*c^2+70785)*x + (-62264180*c^3+6229080*c)
                   over Number Field in c with defining polynomial x^4 + 3*x^2 + 1

        TESTS::

            sage: TestSuite(C).run()
        """
    def copy(self):
        """
        Return a copy (mostly used in reordering).

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve(K, [0,0,0,0,1])
            sage: C = E.isogeny_class()
            sage: C2 = C.copy()
            sage: C is C2
            False
            sage: C == C2
            True
        """

class IsogenyClass_EC_Rational(IsogenyClass_EC_NumberField):
    """
    Isogeny classes for elliptic curves over `\\QQ`.
    """
    def __init__(self, E, algorithm: str = 'sage', label=None, empty: bool = False) -> None:
        """
        INPUT:

        - ``E`` -- an elliptic curve over `\\QQ`

        - ``algorithm`` -- string (default: ``'sage'``); one of the
          following:

          - ``'sage'`` -- use sage's implementation to compute the curves,
            matrix and isogenies

          - ``'database'`` -- use the Cremona database (only works if the
            curve is in the database)

        - ``label`` -- string; the label of this isogeny class
          (e.g. '15a' or '37.b'), used in printing

        - ``empty`` -- don't compute the curves right now (used when reordering)

        EXAMPLES::

            sage: isocls = EllipticCurve('389a1').isogeny_class(); isocls
            Elliptic curve isogeny class 389a
            sage: E = EllipticCurve([0, 0, 0, 0, 1001]) # conductor 108216108
            sage: E.isogeny_class(order='database')
            Traceback (most recent call last):
            ...
            LookupError: Cremona database does not contain entry for
            Elliptic Curve defined by y^2 = x^3 + 1001 over Rational Field
            sage: TestSuite(isocls).run()
        """
    def copy(self):
        """
        Return a copy (mostly used in reordering).

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: C = E.isogeny_class()
            sage: C2 = C.copy()
            sage: C is C2
            False
            sage: C == C2
            True
        """

def isogeny_degrees_cm(E, verbose: bool = False):
    """
    Return a list of primes `\\ell` sufficient to generate the
    isogeny class of `E`, where `E` has CM.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field

    OUTPUT:

    A finite list of primes `\\ell` such that every curve isogenous to
    this curve can be obtained by a finite sequence of isogenies of
    degree one of the primes in the list.  This list is not
    necessarily minimal.

    ALGORITHM:

    For curves with CM by the order `O` of discriminant `d`, the
    Galois representation is always non-surjective and the curve will
    admit `\\ell`-isogenies for infinitely many primes `\\ell`, but
    there are only finitely many codomains `E'`.  The primes can be
    divided according to the discriminant `d'` of the CM order `O'`
    associated to `E`: either `O=O'`, or one contains the other with
    index `\\ell`, since `\\ell O\\subset O'` and vice versa.

    Case (1): `O=O'`.  The degrees of all isogenies between `E` and
    `E'` are precisely the integers represented by one of the classes
    of binary quadratic forms `Q` of discriminant `d`.  Hence to
    obtain all possible isomorphism classes of codomain `E'`, we need
    only use one prime `\\ell` represented by each such class `Q`.  It
    would in fact suffice to use primes represented by forms which
    generate the class group.  Here we simply omit the principal class
    and one from each pair of inverse classes, and include a prime
    represented by each of the remaining forms.

    Case (2): `[O':O]=\\ell`: so `d=\\ell^2d;`.  We include all prime
    divisors of `d`.

    Case (3): `[O:O']=\\ell`: we may assume that `\\ell` does not divide
    `d` as we have already included these, so `\\ell` either splits or
    is inert in `O`; the class numbers satisfy `h(O')=(\\ell\\pm1)h(O)`
    accordingly.  We include all primes `\\ell` such that `\\ell\\pm1`
    divides the degree `[K:\\QQ]`.

    For curves with only potential CM we proceed as in the CM case,
    using `2[K:\\QQ]` instead of `[K:\\QQ]`.

    EXAMPLES:

    For curves with CM by a quadratic order of class number greater
    than `1`, we use the structure of the class group to only give one
    prime in each ideal class::

        sage: pol = PolynomialRing(QQ,'x')([1,-3,5,-5,5,-3,1])
        sage: L.<a> = NumberField(pol)
        sage: j = hilbert_class_polynomial(-23).roots(L, multiplicities=False)[0]
        sage: E = EllipticCurve(j=j)
        sage: from sage.schemes.elliptic_curves.isogeny_class import isogeny_degrees_cm
        sage: isogeny_degrees_cm(E, verbose=True)
        CM case, discriminant = -23
        initial primes: {2}
        upward primes: {}
        downward ramified primes: {}
        downward split primes: {2, 3}
        downward inert primes: {5}
        primes generating the class group: [2]
        Set of primes before filtering: {2, 3, 5}
        List of primes after filtering: [2, 3]
        [2, 3]

    TESTS:

    Check that :issue:`36780` is fixed::

        sage: L5.<r5> = NumberField(x^2-5)
        sage: E = EllipticCurve(L5,[0,-4325477943600 *r5-4195572876000])
        sage: from sage.schemes.elliptic_curves.isogeny_class import isogeny_degrees_cm
        sage: isogeny_degrees_cm(E)
        [3, 5]
    """
def possible_isogeny_degrees(E, algorithm: str = 'Billerey', max_l=None, num_l=None, exact: bool = True, verbose: bool = False):
    """
    Return a list of primes `\\ell` sufficient to generate the
    isogeny class of `E`.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field

    - ``algorithm`` -- string (default: ``'Billerey'``); algorithm to be
      used for non-CM curves: either ``'Billerey'``, ``'Larson'``, or
      ``'heuristic'``.  Only relevant for non-CM curves and base fields
      other than `\\QQ`.

    - ``max_l`` -- integer or ``None``; only relevant for non-CM curves
      and algorithms ``'Billerey'`` and ``'heuristic'``.  Controls the maximum
      prime used in either algorithm.  If ``None``, use the default
      for that algorithm.

    - ``num_l`` -- integer or ``None``; only relevant for non-CM curves
      and algorithm ``'Billerey'``.  Controls the maximum number of primes
      used in the algorithm.  If ``None``, use the default for that
      algorithm.

    - ``exact`` -- boolean (default: ``True``); if ``True``, perform an
      additional check that the primes returned are all reducible.  If
      ``False``, skip this step, in which case some of the primes
      returned may be irreducible.

    OUTPUT:

    A finite list of primes `\\ell` such that every curve isogenous to
    this curve can be obtained by a finite sequence of isogenies of
    degree one of the primes in the list.

    ALGORITHM:

    For curves without CM, the set may be taken to be the finite set
    of primes at which the Galois representation is not surjective,
    since the existence of an `\\ell`-isogeny is equivalent to the
    image of the mod-`\\ell` Galois representation being contained in a
    Borel subgroup.  Two rigorous algorithms have been implemented to
    determine this set, due to Larson and Billeray respectively.  We
    also provide a non-rigorous 'heuristic' algorithm which only tests
    reducible primes up to a bound depending on the degree of the
    base field.

    For curves with CM see the documentation for :meth:`isogeny_degrees_cm()`.

    EXAMPLES:

    For curves without CM we determine the primes at which the mod `p`
    Galois representation is reducible, i.e. contained in a Borel
    subgroup::

        sage: from sage.schemes.elliptic_curves.isogeny_class import possible_isogeny_degrees
        sage: E = EllipticCurve('11a1')
        sage: possible_isogeny_degrees(E)
        [5]
        sage: possible_isogeny_degrees(E, algorithm='Larson')
        [5]
        sage: possible_isogeny_degrees(E, algorithm='Billerey')
        [5]
        sage: possible_isogeny_degrees(E, algorithm='heuristic')
        [5]

    We check that in this case `E` really does have rational
    `5`-isogenies::

        sage: [phi.degree() for phi in E.isogenies_prime_degree()]
        [5, 5]

    Over an extension field::

        sage: E3 = E.change_ring(CyclotomicField(3))
        sage: possible_isogeny_degrees(E3)                                              # long time (5s)
        [5]
        sage: [phi.degree() for phi in E3.isogenies_prime_degree()]
        [5, 5]

    A higher degree example (LMFDB curve 5.5.170701.1-4.1-b1)::

        sage: K.<a> = NumberField(x^5 - x^4 - 6*x^3 + 4*x + 1)
        sage: E = EllipticCurve(K, [a^3 - a^2 - 5*a + 1, a^4 - a^3 - 5*a^2 - a + 1,
        ....:                       -a^4 + 2*a^3 + 5*a^2 - 5*a - 3, a^4 - a^3 - 5*a^2 - a,
        ....:                       -3*a^4 + 4*a^3 + 17*a^2 - 6*a - 12])
        sage: possible_isogeny_degrees(E, algorithm='heuristic')
        [2]
        sage: possible_isogeny_degrees(E, algorithm='Billerey')
        [2]
        sage: possible_isogeny_degrees(E, algorithm='Larson')
        [2]

    LMFDB curve 4.4.8112.1-108.1-a5::

        sage: K.<a> = NumberField(x^4 - 5*x^2 + 3)
        sage: E = EllipticCurve(K, [a^2 - 2, -a^2 + 3, a^2 - 2, -50*a^2 + 35, 95*a^2 - 67])
        sage: possible_isogeny_degrees(E, exact=False, algorithm='Billerey')            # long time (6.5s)
        [2, 5]
        sage: possible_isogeny_degrees(E, exact=False, algorithm='Larson')
        [2, 5]
        sage: possible_isogeny_degrees(E, exact=False, algorithm='heuristic')
        [2, 5]
        sage: possible_isogeny_degrees(E)
        [2, 5]

    This function only returns the primes which are isogeny degrees::

        sage: Set(E.isogeny_class().matrix().list())                                    # long time (7s)
        {1, 2, 4, 5, 20, 10}

    For curves with CM by a quadratic order of class number greater
    than `1`, we use the structure of the class group to only give one
    prime in each ideal class::

        sage: pol = PolynomialRing(QQ,'x')([1,-3,5,-5,5,-3,1])
        sage: L.<a> = NumberField(pol)
        sage: j = hilbert_class_polynomial(-23).roots(L, multiplicities=False)[0]
        sage: E = EllipticCurve(j=j)
        sage: from sage.schemes.elliptic_curves.isogeny_class import possible_isogeny_degrees
        sage: possible_isogeny_degrees(E, verbose=True)
        CM case, discriminant = -23
        initial primes: {2}
        upward primes: {}
        downward ramified primes: {}
        downward split primes: {2, 3}
        downward inert primes: {5}
        primes generating the class group: [2]
        Set of primes before filtering: {2, 3, 5}
        List of primes after filtering: [2, 3]
        [2, 3]
    """
