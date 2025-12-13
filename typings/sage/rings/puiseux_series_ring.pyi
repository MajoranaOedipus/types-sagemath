from sage.categories.fields import Fields as Fields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.laurent_series_ring_element import LaurentSeries as LaurentSeries
from sage.rings.power_series_ring_element import PowerSeries as PowerSeries
from sage.rings.puiseux_series_ring_element import PuiseuxSeries as PuiseuxSeries
from sage.structure.element import parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PuiseuxSeriesRing(UniqueRepresentation, Parent):
    """
    Rings of Puiseux series.

    EXAMPLES::

        sage: P = PuiseuxSeriesRing(QQ, 'y')
        sage: y = P.gen()
        sage: f = y**(4/3) + y**(-5/6); f
        y^(-5/6) + y^(4/3)
        sage: f.add_bigoh(2)
        y^(-5/6) + y^(4/3) + O(y^2)
        sage: f.add_bigoh(1)
        y^(-5/6) + O(y)
    """
    @staticmethod
    def __classcall__(cls, *args, **kwds):
        """
        TESTS::

            sage: L = PuiseuxSeriesRing(QQ, 'q')
            sage: L is PuiseuxSeriesRing(QQ, name='q')
            True
            sage: Lp.<q> = PuiseuxSeriesRing(QQ)
            sage: L is Lp
            True
            sage: loads(dumps(L)) is L
            True

            sage: L.variable_names()
            ('q',)
            sage: L.variable_name()
            'q'
        """
    def __init__(self, laurent_series) -> None:
        """
        Generic class for Puiseux series rings.

        EXAMPLES::

            sage: P = PuiseuxSeriesRing(QQ, 'y')
            sage: TestSuite(P).run()

            sage: P = PuiseuxSeriesRing(ZZ, 'x')
            sage: TestSuite(P).run()

            sage: P = PuiseuxSeriesRing(ZZ['a,b'], 'x')
            sage: TestSuite(P).run()
        """
    def base_extend(self, R):
        """
        Extend the coefficients.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(ZZ, 'y')
            sage: A.base_extend(QQ)
            Puiseux Series Ring in y over Rational Field
        """
    def change_ring(self, R):
        """
        Return a Puiseux series ring over another ring.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(ZZ, 'y')
            sage: A.change_ring(QQ)
            Puiseux Series Ring in y over Rational Field
        """
    def is_sparse(self) -> bool:
        """
        Return whether ``self`` is sparse.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(ZZ, 'y')
            sage: A.is_sparse()
            False
        """
    def is_dense(self) -> bool:
        """
        Return whether ``self`` is dense.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(ZZ, 'y')
            sage: A.is_dense()
            True
        """
    def is_field(self, proof: bool = True) -> bool:
        """
        Return whether ``self`` is a field.

        A Puiseux series ring is a field if and only
        its base ring is a field.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(ZZ, 'y')
            sage: A.is_field()
            False
            sage: A in Fields()
            False
            sage: B = A.change_ring(QQ); B.is_field()
            True
            sage: B in Fields()
            True
        """
    def fraction_field(self):
        """
        Return the fraction field of this ring of Laurent series.

        If the base ring is a field, then Puiseux series are already a field.
        If the base ring is a domain, then the Puiseux series over its fraction
        field is returned. Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: R = PuiseuxSeriesRing(ZZ, 't', 30).fraction_field()
            sage: R
            Puiseux Series Ring in t over Rational Field
            sage: R.default_prec()
            30

            sage: PuiseuxSeriesRing(Zmod(4), 't').fraction_field()
            Traceback (most recent call last):
            ...
            ValueError: must be an integral domain
        """
    def residue_field(self):
        """
        Return the residue field of this Puiseux series field
        if it is a complete discrete valuation field (i.e. if
        the base ring is a field, in which case it is also the
        residue field).

        EXAMPLES::

            sage: R.<x> = PuiseuxSeriesRing(GF(17))
            sage: R.residue_field()
            Finite Field of size 17

            sage: R.<x> = PuiseuxSeriesRing(ZZ)
            sage: R.residue_field()
            Traceback (most recent call last):
            ...
            TypeError: the base ring is not a field
        """
    def uniformizer(self):
        """
        Return a uniformizer of this Puiseux series field if it is
        a discrete valuation field (i.e. if the base ring is actually
        a field). Otherwise, an error is raised.

        EXAMPLES::

            sage: R.<t> = PuiseuxSeriesRing(QQ)
            sage: R.uniformizer()
            t

            sage: R.<t> = PuiseuxSeriesRing(ZZ)
            sage: R.uniformizer()
            Traceback (most recent call last):
            ...
            TypeError: the base ring is not a field
        """
    Element = PuiseuxSeries
    @cached_method
    def gen(self, n: int = 0):
        """
        Return the generator of ``self``.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(AA, 'z')                                        # needs sage.rings.number_field
            sage: A.gen()                                                               # needs sage.rings.number_field
            z
        """
    def gens(self) -> tuple:
        """
        Return the tuple of generators.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(QQ, 'z')
            sage: A.gens()
            (z,)
        """
    def ngens(self) -> int:
        """
        Return the number of generators of ``self``, namely 1.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(AA, 'z')                                        # needs sage.rings.number_field
            sage: A.ngens()                                                             # needs sage.rings.number_field
            1
        """
    def laurent_series_ring(self):
        """
        Return the underlying Laurent series ring.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(AA, 'z')                                        # needs sage.rings.number_field
            sage: A.laurent_series_ring()                                               # needs sage.rings.number_field
            Laurent Series Ring in z over Algebraic Real Field
        """
    def default_prec(self):
        """
        Return the default precision of ``self``.

        EXAMPLES::

            sage: A = PuiseuxSeriesRing(AA, 'z')                                        # needs sage.rings.number_field
            sage: A.default_prec()                                                      # needs sage.rings.number_field
            20
        """
