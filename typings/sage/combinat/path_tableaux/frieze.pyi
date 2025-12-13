from sage.categories.fields import Fields as Fields
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.path_tableaux.path_tableau import CylindricalDiagram as CylindricalDiagram, PathTableau as PathTableau, PathTableaux as PathTableaux
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent

class FriezePattern(PathTableau, metaclass=InheritComparisonClasscallMetaclass):
    """
    A frieze pattern.

    We encode a frieze pattern as a sequence in a fixed ground field.

    INPUT:

    - ``fp`` -- a sequence of elements of ``field``
    - ``field`` -- (default: ``QQ``) the ground field

    EXAMPLES::

        sage: t = path_tableaux.FriezePattern([1,2,1,2,3,1])
        sage: path_tableaux.CylindricalDiagram(t)
        [0, 1, 2, 1, 2, 3, 1, 0]
        [ , 0, 1, 1, 3, 5, 2, 1, 0]
        [ ,  , 0, 1, 4, 7, 3, 2, 1, 0]
        [ ,  ,  , 0, 1, 2, 1, 1, 1, 1, 0]
        [ ,  ,  ,  , 0, 1, 1, 2, 3, 4, 1, 0]
        [ ,  ,  ,  ,  , 0, 1, 3, 5, 7, 2, 1, 0]
        [ ,  ,  ,  ,  ,  , 0, 1, 2, 3, 1, 1, 1, 0]
        [ ,  ,  ,  ,  ,  ,  , 0, 1, 2, 1, 2, 3, 1, 0]

        sage: TestSuite(t).run()

        sage: t = path_tableaux.FriezePattern([1,2,7,5,3,7,4,1])
        sage: path_tableaux.CylindricalDiagram(t)
        [0, 1, 2, 7, 5, 3, 7, 4, 1, 0]
        [ , 0, 1, 4, 3, 2, 5, 3, 1, 1, 0]
        [ ,  , 0, 1, 1, 1, 3, 2, 1, 2, 1, 0]
        [ ,  ,  , 0, 1, 2, 7, 5, 3, 7, 4, 1, 0]
        [ ,  ,  ,  , 0, 1, 4, 3, 2, 5, 3, 1, 1, 0]
        [ ,  ,  ,  ,  , 0, 1, 1, 1, 3, 2, 1, 2, 1, 0]
        [ ,  ,  ,  ,  ,  , 0, 1, 2, 7, 5, 3, 7, 4, 1, 0]
        [ ,  ,  ,  ,  ,  ,  , 0, 1, 4, 3, 2, 5, 3, 1, 1, 0]
        [ ,  ,  ,  ,  ,  ,  ,  , 0, 1, 1, 1, 3, 2, 1, 2, 1, 0]
        [ ,  ,  ,  ,  ,  ,  ,  ,  , 0, 1, 2, 7, 5, 3, 7, 4, 1, 0]

         sage: TestSuite(t).run()

        sage: t = path_tableaux.FriezePattern([1,3,4,5,1])
        sage: path_tableaux.CylindricalDiagram(t)
        [  0,   1,   3,   4,   5,   1,   0]
        [   ,   0,   1, 5/3, 7/3, 2/3,   1,   0]
        [   ,    ,   0,   1,   2,   1,   3,   1,   0]
        [   ,    ,    ,   0,   1,   1,   4, 5/3,   1,   0]
        [   ,    ,    ,    ,   0,   1,   5, 7/3,   2,   1,   0]
        [   ,    ,    ,    ,    ,   0,   1, 2/3,   1,   1,   1,   0]
        [   ,    ,    ,    ,    ,    ,   0,   1,   3,   4,   5,   1,   0]

        sage: TestSuite(t).run()

    This constructs the examples from [HJ18]_::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<sqrt3> = NumberField(x^2 - 3)
        sage: t = path_tableaux.FriezePattern([1, sqrt3, 2, sqrt3, 1, 1], field=K)
        sage: path_tableaux.CylindricalDiagram(t)
        [        0,         1,     sqrt3,         2,     sqrt3,         1,         1,         0]
        [         ,         0,         1,     sqrt3,         2,     sqrt3, sqrt3 + 1,         1,         0]
        [         ,          ,         0,         1,     sqrt3,         2, sqrt3 + 2,     sqrt3,         1,         0]
        [         ,          ,          ,         0,         1,     sqrt3, sqrt3 + 2,         2,     sqrt3,         1,         0]
        [         ,          ,          ,          ,         0,         1, sqrt3 + 1,     sqrt3,         2,     sqrt3,         1,         0]
        [         ,          ,          ,          ,          ,         0,         1,         1,     sqrt3,         2,     sqrt3,         1,         0]
        [         ,          ,          ,          ,          ,          ,         0,         1, sqrt3 + 1, sqrt3 + 2, sqrt3 + 2, sqrt3 + 1,         1,         0]
        [         ,          ,          ,          ,          ,          ,          ,         0,         1,     sqrt3,         2,     sqrt3,         1,         1,         0]
        sage: TestSuite(t).run()

        sage: # needs sage.rings.number_field
        sage: K.<sqrt2> = NumberField(x^2 - 2)
        sage: t = path_tableaux.FriezePattern([1, sqrt2, 1, sqrt2, 3, 2*sqrt2, 5, 3*sqrt2, 1],
        ....:                                 field=K)
        sage: path_tableaux.CylindricalDiagram(t)
        [      0,       1,   sqrt2,       1,   sqrt2,       3, 2*sqrt2,       5, 3*sqrt2,       1,       0]
        [       ,       0,       1,   sqrt2,       3, 5*sqrt2,       7, 9*sqrt2,      11, 2*sqrt2,       1,       0]
        [       ,        ,       0,       1, 2*sqrt2,       7, 5*sqrt2,      13, 8*sqrt2,       3,   sqrt2,       1,       0]
        [       ,        ,        ,       0,       1, 2*sqrt2,       3, 4*sqrt2,       5,   sqrt2,       1,   sqrt2,       1,       0]
        [       ,        ,        ,        ,       0,       1,   sqrt2,       3, 2*sqrt2,       1,   sqrt2,       3, 2*sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,       0,       1, 2*sqrt2,       3,   sqrt2,       3, 5*sqrt2,       7, 2*sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,        ,       0,       1,   sqrt2,       1, 2*sqrt2,       7, 5*sqrt2,       3,   sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,        ,        ,       0,       1,   sqrt2,       5, 9*sqrt2,      13, 4*sqrt2,       3, 2*sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,        ,        ,        ,       0,       1, 3*sqrt2,      11, 8*sqrt2,       5, 2*sqrt2,       3,   sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,        ,        ,        ,        ,       0,       1, 2*sqrt2,       3,   sqrt2,       1,   sqrt2,       1,   sqrt2,       1,       0]
        [       ,        ,        ,        ,        ,        ,        ,        ,        ,        ,       0,       1,   sqrt2,       1,   sqrt2,       3, 2*sqrt2,       5, 3*sqrt2,       1,       0]
        sage: TestSuite(t).run()
    """
    @staticmethod
    def __classcall_private__(cls, fp, field=...):
        """
        This is the preprocessing for creating friezes.

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,1,2,3,1])
            [1, 2, 1, 2, 3, 1]

        TESTS::

            sage: path_tableaux.FriezePattern(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid input 2

            sage: x = polygen(ZZ, 'x')
            sage: K.<sqrt3> = NumberField(x^2 - 3)                                      # needs sage.rings.number_field
            sage: t = path_tableaux.FriezePattern([1,sqrt3,2,sqrt3,1,1])                # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ValueError: [1, sqrt3, 2, sqrt3, 1, 1] is not a sequence in the field Rational Field

            sage: path_tableaux.FriezePattern([1,2,1,2,3,1], field=Integers())
            Traceback (most recent call last):
            ...
            ValueError: Integer Ring must be a field
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid frieze pattern.

        TESTS::

            sage: path_tableaux.FriezePattern([1,2,1,2,3,1]) # indirect test
            [1, 2, 1, 2, 3, 1]
        """
    def local_rule(self, i):
        """
        Return the `i`-th local rule on ``self``.

        This interprets ``self`` as a list of objects. This method first takes
        the list of objects of length three consisting of the `(i-1)`-st,
        `i`-th and `(i+1)`-term and applies the rule. It then replaces
        the `i`-th object  by the object returned by the rule.

        EXAMPLES::

            sage: t = path_tableaux.FriezePattern([1,2,1,2,3,1])
            sage: t.local_rule(3)
            [1, 2, 5, 2, 3, 1]

            sage: t = path_tableaux.FriezePattern([1,2,1,2,3,1])
            sage: t.local_rule(0)
            Traceback (most recent call last):
            ...
            ValueError: 0 is not a valid integer
        """
    def is_skew(self):
        """
        Return ``True`` if ``self`` is skew and ``False`` if not.

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,1,2,3,1]).is_skew()
            False

            sage: path_tableaux.FriezePattern([2,2,1,2,3,1]).is_skew()
            True
        """
    def width(self):
        """
        Return the width of ``self``.

        If the first and last terms of ``self`` are 1 then this is the
        length of ``self`` plus two and otherwise is undefined.

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,1,2,3,1]).width()
            8

            sage: path_tableaux.FriezePattern([1,2,1,2,3,4]).width() is None
            True
        """
    def is_positive(self):
        """
        Return ``True`` if all elements of ``self`` are positive.

        This implies that all entries of ``CylindricalDiagram(self)``
        are positive.

        .. WARNING::

            There are orders on all fields. These may not be ordered fields
            as they may not be compatible with the field operations. This
            method is intended to be used with ordered fields only.

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,7,5,3,7,4,1]).is_positive()
            True

            sage: path_tableaux.FriezePattern([1,-3,4,5,1]).is_positive()
            False

            sage: x = polygen(ZZ, 'x')
            sage: K.<sqrt3> = NumberField(x^2 - 3)                                      # needs sage.rings.number_field
            sage: path_tableaux.FriezePattern([1,sqrt3,1], K).is_positive()             # needs sage.rings.number_field
            True
        """
    def is_integral(self):
        """
        Return ``True`` if all entries of the frieze pattern are
        positive integers.

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,7,5,3,7,4,1]).is_integral()
            True

            sage: path_tableaux.FriezePattern([1,3,4,5,1]).is_integral()
            False
        """
    def triangulation(self):
        """
        Plot a regular polygon with some diagonals.

        If ``self`` is positive and integral then this will be a triangulation.

        .. PLOT::
            :width: 400 px

            G = path_tableaux.FriezePattern([1,2,7,5,3,7,4,1]).triangulation()
            sphinx_plot(G)

        EXAMPLES::

            sage: path_tableaux.FriezePattern([1,2,7,5,3,7,4,1]).triangulation()        # needs sage.plot sage.symbolic
            Graphics object consisting of 25 graphics primitives

            sage: path_tableaux.FriezePattern([1,2,1/7,5,3]).triangulation()            # needs sage.plot sage.symbolic
            Graphics object consisting of 12 graphics primitives


            sage: x = polygen(ZZ, 'x')
            sage: K.<sqrt2> = NumberField(x^2 - 2)                                      # needs sage.rings.number_field
            sage: path_tableaux.FriezePattern([1,sqrt2,1,sqrt2,3,2*sqrt2,5,3*sqrt2,1],  # needs sage.plot sage.rings.number_field sage.symbolic
            ....:                             field=K).triangulation()
            Graphics object consisting of 24 graphics primitives
        """
    def plot(self, model: str = 'UHP'):
        """
        Plot the frieze as an ideal hyperbolic polygon.

        This is only defined up to isometry of the hyperbolic plane.

        We are identifying the boundary of the hyperbolic plane with the
        real projective line.

        The option ``model`` must be one of

        * ``'UHP'`` -- (default) for the upper half plane model
        * ``'PD'`` -- for the Poincare disk model
        * ``'KM'`` -- for the Klein model

        The hyperboloid model is not an option as this does not implement
        boundary points.

        .. PLOT::
            :width: 400 px

            t = path_tableaux.FriezePattern([1,2,7,5,3,7,4,1])
            sphinx_plot(t.plot())

        EXAMPLES::

            sage: # needs sage.plot sage.symbolic
            sage: t = path_tableaux.FriezePattern([1,2,7,5,3,7,4,1])
            sage: t.plot()
            Graphics object consisting of 18 graphics primitives
            sage: t.plot(model='UHP')
            Graphics object consisting of 18 graphics primitives
            sage: t.plot(model='PD')
            Traceback (most recent call last):
            ...
            TypeError: '>' not supported between instances of 'NotANumber' and 'Pi'
            sage: t.plot(model='KM')
            Graphics object consisting of 18 graphics primitives
        """
    def change_ring(self, R):
        """
        Return ``self`` as a frieze pattern with coefficients in ``R``.

        This assumes that there is a canonical coerce map from the base ring of ``self``
        to ``R``.

        EXAMPLES::

            sage: fp = path_tableaux.FriezePattern([1,2,7,5,3,7,4,1])
            sage: fp.change_ring(RealField())                                           # needs sage.rings.real_mpfr
            [0.000000000000000, 1.00000000000000, ...
             4.00000000000000, 1.00000000000000, 0.000000000000000]
            sage: fp.change_ring(GF(7))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
        """

class FriezePatterns(PathTableaux):
    """
    The set of all frieze patterns.

    EXAMPLES::

        sage: P = path_tableaux.FriezePatterns(QQ)
        sage: fp = P((1, 1, 1))
        sage: fp
        [1]
        sage: path_tableaux.CylindricalDiagram(fp)
        [1, 1, 1]
        [ , 1, 2, 1]
        [ ,  , 1, 1, 1]
    """
    def __init__(self, field) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: P = path_tableaux.FriezePatterns(QQ)
            sage: TestSuite(P).run()
        """
    Element = FriezePattern
