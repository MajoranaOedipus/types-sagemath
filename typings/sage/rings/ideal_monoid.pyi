from sage.categories.monoids import Monoids as Monoids
from sage.rings import ideal as ideal
from sage.structure.parent import Parent as Parent

def IdealMonoid(R):
    """
    Return the monoid of ideals in the ring ``R``.

    EXAMPLES::

        sage: R = QQ['x']
        sage: from sage.rings.ideal_monoid import IdealMonoid
        sage: IdealMonoid(R)
        Monoid of ideals of Univariate Polynomial Ring in x over Rational Field
    """

class IdealMonoid_c(Parent):
    '''
    The monoid of ideals in a commutative ring.

    TESTS::

        sage: R = QQ[\'x\']
        sage: from sage.rings.ideal_monoid import IdealMonoid
        sage: M = IdealMonoid(R)
        sage: TestSuite(M).run()
          Failure in _test_category:
        ...
        The following tests failed: _test_elements

    (The "_test_category" test fails but I haven\'t the foggiest idea why.)
    '''
    Element = ideal.Ideal_generic
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R = QuadraticField(-23, 'a')                                          # needs sage.rings.number_field
            sage: from sage.rings.ideal_monoid import IdealMonoid
            sage: M = IdealMonoid(R); M  # indirect doctest                             # needs sage.rings.number_field
            Monoid of ideals of Number Field in a with defining polynomial x^2 + 23
             with a = 4.795831523312720?*I

            sage: id = QQ.ideal(6)
            sage: id.parent().category()
            Category of commutative monoids

            sage: MS = MatrixSpace(QQ, 3, 3)                                            # needs sage.modules
            sage: MS.ideal(MS.one()).parent().category()                                # needs sage.modules
            Category of monoids
        """
    def ring(self):
        """
        Return the ring of which this is the ideal monoid.

        EXAMPLES::

            sage: R = QuadraticField(-23, 'a')                                          # needs sage.rings.number_field
            sage: from sage.rings.ideal_monoid import IdealMonoid
            sage: M = IdealMonoid(R); M.ring() is R                                     # needs sage.rings.number_field
            True
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R = QuadraticField(-23, 'a')
            sage: M = R.ideal_monoid()
            sage: M == QQ
            False
            sage: M == 17
            False
            sage: M == R.ideal_monoid()
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R = QuadraticField(-23, 'a')
            sage: M = R.ideal_monoid()
            sage: M != QQ
            True
            sage: M != 17
            True
            sage: M != R.ideal_monoid()
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R = QuadraticField(-23, 'a')
            sage: M = R.ideal_monoid()
            sage: hash(M) == hash(QQ)
            False
            sage: hash(M) == 17
            False
            sage: hash(M) == hash(R.ideal_monoid())
            True
        """
