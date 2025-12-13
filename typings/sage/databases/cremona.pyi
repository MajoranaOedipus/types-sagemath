from .sql_db import SQLDatabase as SQLDatabase, verify_column as verify_column
from _typeshed import Incomplete
from collections.abc import Generator
from sage.features.databases import DatabaseCremona as DatabaseCremona
from sage.misc.prandom import randint as randint
from sage.misc.timing import walltime as walltime

def build(name, data_tgz, largest_conductor: int = 0, mini: bool = False, decompress: bool = True) -> None:
    """
    Build the CremonaDatabase with given name from scratch
    using the data_tgz tarball.

    .. NOTE::

           For data up to level 350000, this function takes about
           3m40s.  The resulting database occupies 426MB disk space.

    To create the large Cremona database from Cremona's data_tgz
    tarball, obtainable from
    http://homepages.warwick.ac.uk/staff/J.E.Cremona/ftp/data/, run
    the following command::

        sage: d = sage.databases.cremona.build('cremona','ecdata.tgz')   # not tested
    """
def is_optimal_id(id):
    """
    Return ``True`` if the Cremona id refers to an optimal curve, and
    ``False`` otherwise.

    The curve is optimal if the id, which is of the
    form [letter code][number] has number 1.

    .. NOTE::

       990h3 is the optimal curve in that class, so doesn't obey
       this rule.

    INPUT:

    - ``id`` -- string of form letter code followed by an
      integer, e.g., a3, bb5, etc.

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.databases.cremona import is_optimal_id
        sage: is_optimal_id('b1')
        True
        sage: is_optimal_id('bb1')
        True
        sage: is_optimal_id('c1')
        True
        sage: is_optimal_id('c2')
        False
    """
def cremona_letter_code(n) -> str:
    """
    Return the Cremona letter code corresponding to an integer.

    For example, 0 - a 25 - z 26 - ba 51 - bz 52 - ca 53 - cb etc.

    .. NOTE::

       This is just the base 26 representation of n, where a=0, b=1,
       ..., z=25. This extends the old Cremona notation (counting from
       0) for the first 26 classes, and is different for classes above
       26.

    INPUT:

    - ``n`` -- nonnegative integer

    OUTPUT: string

    EXAMPLES::

        sage: from sage.databases.cremona import cremona_letter_code
        sage: cremona_letter_code(0)
        'a'
        sage: cremona_letter_code(26)
        'ba'
        sage: cremona_letter_code(27)
        'bb'
        sage: cremona_letter_code(521)
        'ub'
        sage: cremona_letter_code(53)
        'cb'
        sage: cremona_letter_code(2005)
        'czd'

    TESTS::

        sage: cremona_letter_code(QQ)
        Traceback (most recent call last):
        ...
        ValueError: Cremona letter codes are only defined for nonnegative integers
        sage: cremona_letter_code(x)                                                    # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: Cremona letter codes are only defined for nonnegative integers
        sage: cremona_letter_code(-1)
        Traceback (most recent call last):
        ...
        ValueError: Cremona letter codes are only defined for nonnegative integers
        sage: cremona_letter_code(3.14159)
        Traceback (most recent call last):
        ...
        ValueError: Cremona letter codes are only defined for nonnegative integers
    """
def old_cremona_letter_code(n) -> str:
    """
    Return the *old* Cremona letter code corresponding to an integer.

    For example::

        1  --> A
        26 --> Z
        27 --> AA
        52 --> ZZ
        53 --> AAA
        etc.

    INPUT:

    - ``n`` -- integer

    OUTPUT: string

    EXAMPLES::

        sage: from sage.databases.cremona import old_cremona_letter_code
        sage: old_cremona_letter_code(1)
        'A'
        sage: old_cremona_letter_code(26)
        'Z'
        sage: old_cremona_letter_code(27)
        'AA'
        sage: old_cremona_letter_code(521)
        'AAAAAAAAAAAAAAAAAAAAA'
        sage: old_cremona_letter_code(53)
        'AAA'
        sage: old_cremona_letter_code(2005)
        'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'
    """

old_cremona_label_regex: Incomplete
cremona_label_regex: Incomplete
lmfdb_label_regex: Incomplete

def parse_cremona_label(label, numerical_class_code: bool = False):
    """
    Given a Cremona label that defines an elliptic
    curve, e.g., 11a1 or 37b3, parse the label and return the
    conductor, isogeny class label, and number.

    For this function, the curve number may be omitted, in which case
    it defaults to 1.  If the curve number and isogeny class are both
    omitted (label is just a string representing a conductor), then
    the isogeny class defaults to 'a' and the number to 1.  Valid
    labels consist of one or more digits, followed by zero or more
    letters (either all in upper case for an old Cremona label, or all
    in lower case), followed by zero or more digits.

    INPUT:

    - ``label`` -- string; a valid Cremona elliptic curve label

    - ``numerical_class_code`` -- boolean (default: ``False``); if ``True``,
      convert the isogeny class label from a letter code in base 26
      to an integer.  This is useful for sorting.

    OUTPUT:

    -  integer; the conductor
    -  string or integer; the isogeny class label
    -  integer; the number

    EXAMPLES::

        sage: from sage.databases.cremona import parse_cremona_label
        sage: parse_cremona_label('37a2')
        (37, 'a', 2)
        sage: parse_cremona_label('37b1')
        (37, 'b', 1)
        sage: parse_cremona_label('10bb2')
        (10, 'bb', 2)
        sage: parse_cremona_label('11a')
        (11, 'a', 1)
        sage: parse_cremona_label('11')
        (11, 'a', 1)

    Valid old Cremona labels are allowed::

        sage: parse_cremona_label('17CCCC')
        (17, 'dc', 1)
        sage: parse_cremona_label('5AB2')
        Traceback (most recent call last):
        ...
        ValueError: 5AB2 is not a valid Cremona label

    When ``numerical_class_code`` is ``True``, the output is a triple of integers::

        sage: from sage.databases.cremona import parse_cremona_label
        sage: parse_cremona_label('100800hj2')
        (100800, 'hj', 2)
        sage: parse_cremona_label('100800hj2', numerical_class_code=True)
        (100800, 191, 2)

    TESTS::

        sage: from sage.databases.cremona import parse_cremona_label
        sage: parse_cremona_label('x11')
        Traceback (most recent call last):
        ...
        ValueError: x11 is not a valid Cremona label
    """
def parse_lmfdb_label(label, numerical_class_code: bool = False):
    """
    Given an LMFDB label that defines an elliptic curve, e.g., 11.a1
    or 37.b3, parse the label and return the conductor, isogeny class
    label, and number.

    The LMFDB label (named after the `L`-functions and modular forms
    database), is determined by the following two orders:

    - Isogeny classes with the same conductor are ordered
      lexicographically by the coefficients in the `q`-expansion of the
      associated modular form.

    - Curves within the same isogeny class are ordered
      lexicographically by the a-invariants of the minimal model.

    The format is <conductor>.<iso><curve>, where the isogeny class is
    encoded using the same base-26 encoding into letters used in
    Cremona's labels.  For example, 990.h3 is the same as Cremona's 990j1

    For this function, the curve number may be omitted, in which case
    it defaults to 1.  If the curve number and isogeny class are both
    omitted (label is just a string representing a conductor), then
    the isogeny class defaults to 'a' and the number to 1.

    INPUT:

    - ``label`` -- str

    - ``numerical_class_code`` -- boolean (default: ``False``); if ``True``,
      convert the isogeny class label from a letter code in base 26
      to an integer.  This is useful for sorting.

    OUTPUT:

    - ``int`` -- the conductor
    - ``str`` or ``int`` -- the isogeny class label
    - ``int`` -- the number

    EXAMPLES::

        sage: from sage.databases.cremona import parse_lmfdb_label
        sage: parse_lmfdb_label('37.a2')
        (37, 'a', 2)
        sage: parse_lmfdb_label('37.b')
        (37, 'b', 1)
        sage: parse_lmfdb_label('10.bb2')
        (10, 'bb', 2)

    When ``numerical_class_code`` is ``True``, the output is a triple of integers::

        sage: from sage.databases.cremona import parse_lmfdb_label
        sage: parse_lmfdb_label('100800.bg4')
        (100800, 'bg', 4)
        sage: parse_lmfdb_label('100800.bg4', numerical_class_code=True)
        (100800, 32, 4)
    """
def split_code(key):
    """
    Split class + curve id string into its two parts.

    EXAMPLES::

        sage: import sage.databases.cremona as cremona
        sage: cremona.split_code('ba2')
        ('ba', '2')
        sage: cremona.split_code('42')
        Traceback (most recent call last):
        ...
        ValueError: invalid curve ID: '42'
    """
def class_to_int(k):
    """
    Convert class id string into an integer.

    Note that this is the inverse of :func:`cremona_letter_code`.

    EXAMPLES::

        sage: import sage.databases.cremona as cremona
        sage: cremona.class_to_int('ba')
        26
        sage: cremona.class_to_int('cremona')
        821863562
        sage: cremona.cremona_letter_code(821863562)
        'cremona'
    """
def sort_key(key1):
    """
    Comparison key for curve id strings.

    .. NOTE::

       Not the same as standard lexicographic order!

    EXAMPLES::

        sage: from sage.databases.cremona import sort_key
        sage: l = ['ba1', 'z1']
        sage: sorted(l, key=sort_key)
        ['z1', 'ba1']
    """
def cremona_to_lmfdb(cremona_label, CDB=None):
    """
    Convert a Cremona label into an LMFDB label.

    See :func:`parse_lmfdb_label` for an explanation of LMFDB labels.

    INPUT:

    - ``cremona_label`` -- string, the Cremona label of a curve; this can be
      the label of a curve (e.g. '990j1') or of an isogeny class (e.g. '990j')
    - ``CDB`` -- the Cremona database in which to look up the isogeny
      classes of the same conductor

    OUTPUT: ``lmfdb_label``; string, the corresponding LMFDB label

    EXAMPLES::

        sage: from sage.databases.cremona import cremona_to_lmfdb, lmfdb_to_cremona
        sage: cremona_to_lmfdb('990j1')
        '990.h3'
        sage: lmfdb_to_cremona('990.h3')
        '990j1'

    TESTS::

        sage: for label in ['5077a1','66a3','102b','420c2']:
        ....:     assert(lmfdb_to_cremona(cremona_to_lmfdb(label)) == label)
        sage: for label in ['438.c2','306.b','462.f3']:
        ....:     assert(cremona_to_lmfdb(lmfdb_to_cremona(label)) == label)
    """
def lmfdb_to_cremona(lmfdb_label, CDB=None):
    """
    Convert an LMFDB label into a Cremona label.

    See :func:`parse_lmfdb_label` for an explanation of LMFDB labels.

    INPUT:

    - ``lmfdb_label`` -- string, the LMFDB label of a curve; this can be the
      label of a curve (e.g. '990.j1') or of an isogeny class (e.g. '990.j')
    - ``CDB`` -- the Cremona database in which to look up the isogeny
      classes of the same conductor

    OUTPUT: ``cremona_label``; a string, the corresponding Cremona label

    EXAMPLES::

        sage: from sage.databases.cremona import cremona_to_lmfdb, lmfdb_to_cremona
        sage: lmfdb_to_cremona('990.h3')
        '990j1'
        sage: cremona_to_lmfdb('990j1')
        '990.h3'
    """

class MiniCremonaDatabase(SQLDatabase):
    """
    The Cremona database of elliptic curves.

    EXAMPLES::

        sage: c = CremonaDatabase()
        sage: c.allcurves(11)
        {'a1': [[0, -1, 1, -10, -20], 0, 5],
         'a2': [[0, -1, 1, -7820, -263580], 0, 1],
         'a3': [[0, -1, 1, 0, 0], 0, 5]}
    """
    name: Incomplete
    def __init__(self, name, read_only: bool = True, build: bool = False) -> None:
        """
        Initialize the database.

        TESTS::

            sage: c = CremonaDatabase('cremona mini')
            sage: c.name
            'cremona mini'
            sage: c = CremonaDatabase('cremona')    # optional - database_cremona_ellcurve
            sage: c.name                            # optional - database_cremona_ellcurve
            'cremona'
        """
    def __iter__(self):
        """
        Return an iterator through all EllipticCurve objects in the
        Cremona database.

        TESTS::

            sage: it = CremonaDatabase().__iter__()
            sage: next(it).label()
            '11a1'
            sage: next(it).label()
            '11a2'
            sage: next(it).label()
            '11a3'
            sage: next(it).label()
            '14a1'
            sage: skip = [next(it) for _ in range(100)]
            sage: next(it).label()
            '45a3'
        """
    def __getitem__(self, N):
        """
        If `N` is an integer, return all data about level `N` in the database.
        If `N` is a string it must be a Cremona label, in which case return
        the corresponding elliptic curve, if it is in the database.

        INPUT:

        - ``N`` -- integer or string

        OUTPUT: dictionary (if `N` is an integer) or EllipticCurve (if `N` is
        a string)

        TESTS::

            sage: c = CremonaDatabase()
            sage: c[11]['allcurves']['a2']
            [[0, -1, 1, -7820, -263580], 0, 1]
            sage: c['11a2']
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field
        """
    def allcurves(self, N):
        """
        Return the allcurves table of curves of conductor N.

        INPUT:

        - ``N`` -- integer; the conductor

        OUTPUT: dictionary; id:[ainvs, rank, tor], ...

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.allcurves(11)['a3']
            [[0, -1, 1, 0, 0], 0, 5]
            sage: c.allcurves(12)
            {}
            sage: c.allcurves(12001)['a1']   # optional - database_cremona_ellcurve
            [[1, 0, 0, -101, 382], 1, 1]
        """
    def curves(self, N):
        """
        Return the curves table of all *optimal* curves of conductor N.

        INPUT:

        - ``N`` -- integer; the conductor

        OUTPUT: dictionary; id:[ainvs, rank, tor], ...

        EXAMPLES:

        Optimal curves of conductor 37::

            sage: CremonaDatabase().curves(37)
            {'a1': [[0, 0, 1, -1, 0], 1, 1], 'b1': [[0, 1, 1, -23, -50], 0, 3]}

        Note the 'h3', which is the unique case in the tables where
        the optimal curve doesn't have label ending in 1::

            sage: sorted(CremonaDatabase().curves(990))
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h3', 'i1', 'j1', 'k1', 'l1']

        TESTS::

            sage: c = CremonaDatabase()
            sage: c.curves(12001)['a1']   # optional - database_cremona_ellcurve
            [[1, 0, 0, -101, 382], 1, 1]
        """
    def coefficients_and_data(self, label):
        """
        Return the Weierstrass coefficients and other data for the
        curve with given label.

        EXAMPLES::

            sage: c, d = CremonaDatabase().coefficients_and_data('144b1')
            sage: c
            [0, 0, 0, 6, 7]
            sage: d['conductor']
            144
            sage: d['cremona_label']
            '144b1'
            sage: d['rank']
            0
            sage: d['torsion_order']
            2

        Check that :issue:`17904` is fixed::

            sage: 'gens' in CremonaDatabase().coefficients_and_data('100467a2')[1] # optional - database_cremona_ellcurve
            True
        """
    def data_from_coefficients(self, ainvs):
        """
        Return elliptic curve data for the curve with given
        Weierstrass coefficients.

        EXAMPLES::

            sage: d = CremonaDatabase().data_from_coefficients([1, -1, 1, 31, 128])
            sage: d['conductor']
            1953
            sage: d['cremona_label']
            '1953c1'
            sage: d['rank']
            1
            sage: d['torsion_order']
            2

        Check that :issue:`17904` is fixed::

            sage: ai = EllipticCurve('100467a2').ainvs() # optional - database_cremona_ellcurve
            sage: 'gens' in CremonaDatabase().data_from_coefficients(ai) # optional - database_cremona_ellcurve
            True
        """
    def elliptic_curve_from_ainvs(self, ainvs):
        """
        Return the elliptic curve in the database of with minimal ``ainvs``
        if it exists.

        This raises a :exc:`RuntimeError` exception otherwise.

        INPUT:

        - ``ainvs`` -- list (5-tuple of int's); the minimal
          Weierstrass model for an elliptic curve

        OUTPUT: EllipticCurve

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.elliptic_curve_from_ainvs([0, -1, 1, -10, -20])
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: c.elliptic_curve_from_ainvs([1, 0, 0, -101, 382])  # optional - database_cremona_ellcurve
            Elliptic Curve defined by y^2 + x*y = x^3 - 101*x + 382 over Rational Field

        Old (pre-2006) Cremona labels are also allowed::

            sage: c.elliptic_curve('9450KKKK1')
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 5*x + 7 over Rational Field

        Make sure :issue:`12565` is fixed::

            sage: c.elliptic_curve('10a1')
            Traceback (most recent call last):
            ...
            ValueError: There is no elliptic curve with label 10a1 in the database
        """
    def elliptic_curve(self, label):
        """
        Return an elliptic curve with given label with some data about it
        from the database pre-filled in.

        INPUT:

        - ``label`` -- string (Cremona or LMFDB label)

        OUTPUT: an :class:`sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field`

        .. NOTE::

            For more details on LMFDB labels see :func:`parse_lmfdb_label`.

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.elliptic_curve('11a1')
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: c.elliptic_curve('12001a1')    # optional - database_cremona_ellcurve
            Elliptic Curve defined by y^2 + x*y = x^3 - 101*x + 382 over Rational Field
            sage: c.elliptic_curve('48c1')
            Traceback (most recent call last):
            ...
            ValueError: There is no elliptic curve with label 48c1 in the database

        You can also use LMFDB labels::

            sage: c.elliptic_curve('462.f3')
            Elliptic Curve defined by y^2 + x*y = x^3 - 363*x + 1305 over Rational Field
        """
    def iter(self, conductors) -> Generator[Incomplete]:
        """
        Return an iterator through all curves in the database with given
        conductors.

        INPUT:

        - ``conductors`` -- list or generator of ints

        OUTPUT: generator that iterates over EllipticCurve objects

        EXAMPLES::

            sage: [e.cremona_label() for e in CremonaDatabase().iter([11..15])]
            ['11a1', '11a2', '11a3', '14a1', '14a2', '14a3', '14a4', '14a5',
             '14a6', '15a1', '15a2', '15a3', '15a4', '15a5', '15a6', '15a7', '15a8']
        """
    def isogeny_classes(self, conductor):
        """
        Return the allcurves data (ainvariants, rank and torsion) for the
        elliptic curves in the database of given conductor as a list of
        lists, one for each isogeny class. The curve with number 1 is
        always listed first.

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.isogeny_classes(11)
            [[[[0, -1, 1, -10, -20], 0, 5],
             [[0, -1, 1, -7820, -263580], 0, 1],
             [[0, -1, 1, 0, 0], 0, 5]]]
            sage: c.isogeny_classes(12001)   # optional - database_cremona_ellcurve
            [[[[1, 0, 0, -101, 382], 1, 1]],
             [[[0, 0, 1, -247, 1494], 1, 1]],
             [[[0, 0, 1, -4, -18], 1, 1]],
             [[[0, 1, 1, -10, 18], 1, 1]]]
        """
    def isogeny_class(self, label):
        """
        Return the isogeny class of elliptic curves that are
        isogenous to the curve with given Cremona label.

        INPUT:

        - ``label`` -- string

        OUTPUT: list of EllipticCurve objects

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.isogeny_class('11a1')
            [Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 - x^2 over Rational Field]
            sage: c.isogeny_class('12001a1')   # optional - database_cremona_ellcurve
            [Elliptic Curve defined by y^2 + x*y = x^3 - 101*x + 382 over Rational Field]
        """
    def iter_optimal(self, conductors) -> Generator[Incomplete]:
        """
        Return an iterator through all optimal curves in the database
        with given conductors.

        INPUT:

        - ``conductors`` -- list or generator of ints

        OUTPUT: generator that iterates over EllipticCurve objects

        EXAMPLES:

        We list optimal curves with conductor up to 20::

            sage: [e.cremona_label() for e in CremonaDatabase().iter_optimal([11..20])]
            ['11a1', '14a1', '15a1', '17a1', '19a1', '20a1']

        Note the unfortunate 990h3 special case::

            sage: [e.cremona_label() for e in CremonaDatabase().iter_optimal([990])]
            ['990a1', '990b1', '990c1', '990d1', '990e1', '990f1', '990g1', '990h3', '990i1', '990j1', '990k1', '990l1']
        """
    def list(self, conductors):
        """
        Return a list of all curves with given conductors.

        INPUT:

        - ``conductors`` -- list or generator of ints

        OUTPUT: list of EllipticCurve objects

        EXAMPLES::

            sage: CremonaDatabase().list([37])
            [Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 23*x - 50 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 1873*x - 31833 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 3*x + 1 over Rational Field]
        """
    def list_optimal(self, conductors):
        """
        Return a list of all optimal curves with given conductors.

        INPUT:

        - ``conductors`` -- list or generator of ints list of EllipticCurve
          objects

        OUTPUT: list of EllipticCurve objects

        EXAMPLES::

            sage: CremonaDatabase().list_optimal([37])
            [Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 23*x - 50 over Rational Field]
        """
    __largest_conductor__: Incomplete
    def largest_conductor(self):
        """
        The largest conductor for which the database is complete.

        OUTPUT: integer; largest conductor

        EXAMPLES::

            sage: c = CremonaDatabase('cremona mini')
            sage: c.largest_conductor()
            9999
        """
    def smallest_conductor(self):
        """
        The smallest conductor for which the database is complete: always 1.

        OUTPUT: integer; smallest conductor

        .. NOTE::

            This always returns the integer 1, since that is the
            smallest conductor for which the database is complete,
            although there are no elliptic curves of conductor 1.  The
            smallest conductor of a curve in the database is 11.

        EXAMPLES::

            sage: CremonaDatabase().smallest_conductor()
            1
        """
    def conductor_range(self):
        """
        Return the range of conductors that are covered by the database.

        OUTPUT: tuple of ints (N1,N2+1) where N1 is the smallest and
        N2 the largest conductor for which the database is complete.

        EXAMPLES::

            sage: c = CremonaDatabase('cremona mini')
            sage: c.conductor_range()
            (1, 10000)
        """
    __number_of_curves__: Incomplete
    def number_of_curves(self, N: int = 0, i: int = 0):
        """
        Return the number of curves stored in the database with conductor
        `N`. If `N = 0`, returns the total number of curves in the database.

        If `i` is nonzero, returns the number of curves in the `i`-th isogeny
        class. If `i` is a Cremona letter code, e.g., 'a' or 'bc', it is
        converted to the corresponding number.

        INPUT:

        - ``N`` -- integer
        - ``i`` -- integer or string

        OUTPUT: integer

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.number_of_curves(11)
            3
            sage: c.number_of_curves(37)
            4
            sage: c.number_of_curves(990)
            42
            sage: num = c.number_of_curves()
        """
    __number_of_isogeny_classes__: Incomplete
    def number_of_isogeny_classes(self, N: int = 0):
        """
        Return the number of isogeny classes of curves in the database of
        conductor N. If N is 0, return the total number of isogeny classes
        of curves in the database.

        INPUT:

        - ``N`` -- integer

        OUTPUT: integer

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.number_of_isogeny_classes(11)
            1
            sage: c.number_of_isogeny_classes(37)
            2
            sage: num = c.number_of_isogeny_classes()
        """
    def random(self):
        """
        Return a random curve from the database.

        EXAMPLES::

            sage: CremonaDatabase().random() # random -- depends on database installed
            Elliptic Curve defined by y^2 + x*y  = x^3 - x^2 - 224*x + 3072 over Rational Field
        """

class LargeCremonaDatabase(MiniCremonaDatabase):
    """
    The Cremona database of elliptic curves.

    EXAMPLES::

        sage: c = CremonaDatabase('cremona')  # optional - database_cremona_ellcurve
        sage: c.allcurves(11)                 # optional - database_cremona_ellcurve
        {'a1': [[0, -1, 1, -10, -20], 0, 5],
        'a2': [[0, -1, 1, -7820, -263580], 0, 1],
        'a3': [[0, -1, 1, 0, 0], 0, 5]}
    """
    def allbsd(self, N):
        """
        Return the allbsd table for conductor N. The entries are::

            [id, tamagawa_product, Omega_E, L, Reg_E, Sha_an(E)]

        where id is the isogeny class (letter) followed by a number, e.g.,
        b3, and L is `L^r(E,1)/r!`, where E has rank r.

        INPUT:

        - ``N`` -- integer; the conductor

        OUTPUT: dictionary containing the allbsd table for each isogeny class
        in conductor N

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.allbsd(12)            # optional - database_cremona_ellcurve
            {}
            sage: c.allbsd(19)['a3']      # optional - database_cremona_ellcurve
            [1, 4.07927920046493, 0.453253244496104, 1.0, 1]
            sage: c.allbsd(12001)['a1']   # optional - database_cremona_ellcurve
            [2, 3.27608135248722, 1.54910143090506, 0.236425971187952, 1.0]
        """
    def allgens(self, N):
        """
        Return the allgens table for conductor N.

        INPUT:

        - ``N`` -- integer; the conductor

        OUTPUT: dictionary; id:[points, ...], ...

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.allgens(12)            # optional - database_cremona_ellcurve
            {}
            sage: c.allgens(1001)['a1']    # optional - database_cremona_ellcurve
            [[61, 181, 1]]
            sage: c.allgens(12001)['a1']   # optional - database_cremona_ellcurve
            [[7, 2, 1]]
        """
    def degphi(self, N):
        """
        Return the degphi table for conductor N.

        INPUT:

        - ``N`` -- integer; the conductor

        OUTPUT: dictionary; id:degphi, ...

        EXAMPLES::

            sage: c = CremonaDatabase()
            sage: c.degphi(11)            # optional - database_cremona_ellcurve
            {'a1': 1}
            sage: c.degphi(12001)['c1']   # optional - database_cremona_ellcurve
            1640
        """

def CremonaDatabase(name=None, mini=None):
    """
    Initialize the Cremona database with name ``name``.

    If ``name`` is
    ``None`` it instead initializes large Cremona database (named 'cremona'),
    if available or default mini Cremona database (named 'cremona mini').

    If the Cremona database in question is in the format of the mini database,
    you must set ``mini=True``, otherwise it must be set to ``False``.

    TESTS::

        sage: c = CremonaDatabase()
        sage: isinstance(c, sage.databases.cremona.MiniCremonaDatabase)
        True
        sage: isinstance(c, sage.databases.cremona.LargeCremonaDatabase)  # optional - database_cremona_ellcurve
        True

    Verify that :issue:`12341` has been resolved::

        sage: c = CremonaDatabase('should not exist', mini=True)
        Traceback (most recent call last):
        ...
        FeatureNotPresentError: database_should_not_exist_ellcurve is not available.
        '...db' not found in any of [...]
        ...Further installation instructions might be available at https://github.com/JohnCremona/ecdata.
        sage: c = CremonaDatabase('should not exist',mini=False)
        Traceback (most recent call last):
        ...
        FeatureNotPresentError: database_should_not_exist_ellcurve is not available.
        '...db' not found in any of [...]
        ...Further installation instructions might be available at https://github.com/JohnCremona/ecdata.

    Verify that :issue:`39072` has been resolved::

        sage: C = CremonaDatabase(mini=False)  # optional - !database_cremona_ellcurve
        Traceback (most recent call last):
        ...
        ValueError: the full Cremona database is not available; consider using the mini Cremona database by setting mini=True
    """
