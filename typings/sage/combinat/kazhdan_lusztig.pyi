from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial as LaurentPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class KazhdanLusztigPolynomial(UniqueRepresentation, SageObject):
    '''
    A Kazhdan-Lusztig polynomial.

    INPUT:

    - ``W`` -- a Weyl Group
    - ``q`` -- an indeterminate

    OPTIONAL:

    - ``trace`` -- if ``True``, then this displays the trace: the intermediate
      results. This is instructive and fun.

    The parent of ``q`` may be a :class:`PolynomialRing` or a
    :class:`LaurentPolynomialRing`.

    EXAMPLES::

        sage: W = WeylGroup("B3",prefix=\'s\')
        sage: [s1,s2,s3] = W.simple_reflections()
        sage: R.<q> = LaurentPolynomialRing(QQ)
        sage: KL = KazhdanLusztigPolynomial(W,q)
        sage: KL.P(s2,s3*s2*s3*s1*s2)
        1 + q

    A faster implementation (using the optional package Coxeter 3) is given by::

        sage: W = CoxeterGroup([\'B\', 3], implementation=\'coxeter3\') # optional - coxeter3
        sage: W.kazhdan_lusztig_polynomial([2], [3,2,3,1,2])        # optional - coxeter3
        q + 1
    '''
    def __init__(self, W, q, trace: bool = False) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: W = WeylGroup("B3",prefix=\'s\')
            sage: R.<q> = LaurentPolynomialRing(QQ)
            sage: KL = KazhdanLusztigPolynomial(W,q)
            sage: TestSuite(KL).run()
        '''
    @cached_method
    def R(self, x, y):
        '''
        Return the Kazhdan-Lusztig `R` polynomial.

        INPUT:

        - ``x``, ``y`` -- elements of the underlying Coxeter group

        EXAMPLES::

            sage: R.<q>=QQ[]
            sage: W = WeylGroup("A2", prefix=\'s\')
            sage: [s1,s2]=W.simple_reflections()
            sage: KL = KazhdanLusztigPolynomial(W, q)
            sage: [KL.R(x,s2*s1) for x in [1,s1,s2,s1*s2]]
            [q^2 - 2*q + 1, q - 1, q - 1, 0]
        '''
    @cached_method
    def R_tilde(self, x, y):
        '''
        Return the Kazhdan-Lusztig `\\tilde{R}` polynomial.

        Information about the `\\tilde{R}` polynomials can be found in
        [Dy1993]_ and [BB2005]_.

        INPUT:

        - ``x``, ``y`` -- elements of the underlying Coxeter group

        EXAMPLES::

            sage: R.<q> = QQ[]
            sage: W = WeylGroup("A2", prefix=\'s\')
            sage: [s1,s2] = W.simple_reflections()
            sage: KL = KazhdanLusztigPolynomial(W, q)
            sage: [KL.R_tilde(x,s2*s1) for x in [1,s1,s2,s1*s2]]
            [q^2, q, q, 0]
        '''
    @cached_method
    def P(self, x, y):
        '''
        Return the Kazhdan-Lusztig `P` polynomial.

        If the rank is large, this runs slowly at first but speeds up
        as you do repeated calculations due to the caching.

        INPUT:

        - ``x``, ``y`` -- elements of the underlying Coxeter group

        .. SEEALSO::

            :mod:`~sage.libs.coxeter3.coxeter_group.CoxeterGroup.kazhdan_lusztig_polynomial`
            for a faster implementation using Fokko Ducloux\'s Coxeter3 C++ library.

        EXAMPLES::

            sage: R.<q> = QQ[]
            sage: W = WeylGroup("A3", prefix=\'s\')
            sage: [s1,s2,s3] = W.simple_reflections()
            sage: KL = KazhdanLusztigPolynomial(W, q)
            sage: KL.P(s2,s2*s1*s3*s2)
            q + 1
        '''
