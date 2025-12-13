from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

print_name_mapping: Incomplete
singular_name_mapping: Incomplete
inv_singular_name_mapping: Incomplete
macaulay2_name_mapping: Incomplete
inv_macaulay2_name_mapping: Incomplete
magma_name_mapping: Incomplete
inv_magma_name_mapping: Incomplete
lex_description: str
invlex_description: str
degrevlex_description: str
deglex_description: str
neglex_description: str
negdegrevlex_description: str
negdeglex_description: str
degneglex_description: str
wdegrevlex_description: str
wdeglex_description: str
negwdegrevlex_description: str
negwdeglex_description: str
matrix_description: str
block_description: str
description_mapping: Incomplete

class TermOrder(SageObject):
    """
    A term order.

    See ``sage.rings.polynomial.term_order`` for details on supported
    term orders.
    """
    __doc__: Incomplete
    def __init__(self, name: str = 'lex', n: int = 0, force: bool = False) -> None:
        """
        Construct a new term order object.

        INPUT:

        - ``name`` -- name of the term order (default: ``'lex'``)

        - ``n`` -- number of variables (default: `0`) weights for
          weighted degree orders. The weights are converted to
          integers and must be positive.

        - ``force`` -- ignore unknown term orders

        See the ``sage.rings.polynomial.term_order`` module
        for help which names and orders are available.

        EXAMPLES::

            sage: t = TermOrder('lex')
            sage: t
            Lexicographic term order
            sage: loads(dumps(t)) == t
            True

        We can construct block orders directly as::

            sage: TermOrder('degrevlex(3),neglex(2)')
            Block term order with blocks:
            (Degree reverse lexicographic term order of length 3,
             Negative lexicographic term order of length 2)

        or by adding together the blocks::

            sage: t1 = TermOrder('degrevlex',3)
            sage: t2 = TermOrder('neglex',2)
            sage: t1 + t2
            Block term order with blocks:
            (Degree reverse lexicographic term order of length 3,
             Negative lexicographic term order of length 2)
            sage: t3 = TermOrder('wdeglex',(1,2))
            sage: t1 + t3
            Block term order with blocks:
            (Degree reverse lexicographic term order of length 3,
             Weighted degree lexicographic term order with weights (1, 2))
            sage: t4 = TermOrder('degneglex')
            sage: t4
            Degree negative lexicographic term order

        We allow blocks of length 0, these are simply ignored::

            sage: TermOrder('lex(0),degrevlex(5),deglex(0),deglex(2)')
            Block term order with blocks:
            (Degree reverse lexicographic term order of length 5,
             Degree lexicographic term order of length 2)

        .. NOTE::

           The optional `n` parameter is not necessary if only
           non-block orders like `deglex` are
           constructed. However, it is useful if block orders are
           to be constructed from this ``TermOrder`` object later.

        TESTS:

        We demonstrate that nonpositive weights are refused and non-integral weights
        are converted to integers (and potentially rounded)::

            sage: N.<a,b,c> = PolynomialRing(QQ, 3, order=TermOrder('wdeglex',[-1,2,-3]))
            Traceback (most recent call last):
            ...
            ValueError: the degree weights must be positive integers
            sage: N.<a,b,c> = PolynomialRing(QQ, 3, order=TermOrder('wdeglex',[1.1,2,3]))
            sage: a.degree()
            1

        We enforce consistency when calling the copy constructor (cf.
        :issue:`12748`)::

            sage: T = TermOrder('degrevlex', 6) + TermOrder('degrevlex',10)
            sage: R.<x0,y0,z0,x1,y1,z1,a0,a1,a2,a3,a4,a5,a6,a7,a8> = PolynomialRing(QQ, order=T)
            Traceback (most recent call last):
            ...
            ValueError: the length of the given term order (16) differs from the number of variables (15)

        If ``_singular_ringorder_column`` attribute is set, then it is regarded
        as a different term order::

            sage: T = TermOrder('degrevlex')
            sage: R.<x,y,z> = PolynomialRing(QQ, order=T)
            sage: R._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 3
            //        block   1 : ordering dp
            //                  : names    x y z
            //        block   2 : ordering C
            sage: T2 = copy(T)
            sage: T2 == T
            True
            sage: T2._singular_ringorder_column = 0
            sage: T2 == T
            False
            sage: S = R.change_ring(order=T2)
            sage: S == T
            False
            sage: S._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 3
            //        block   1 : ordering C
            //        block   2 : ordering dp
            //                  : names    x y z

        Check that :issue:`29635` is fixed::

            sage: T = PolynomialRing(GF(101^5), 'u,v,w',                                # needs sage.rings.finite_rings
            ....:                    order=TermOrder('degneglex')).term_order()
            sage: T.singular_str()                                                      # needs sage.rings.finite_rings
            '(a(1:3),ls(3))'
            sage: (T + T).singular_str()                                                # needs sage.rings.finite_rings
            '(a(1:3),ls(3),a(1:3),ls(3))'
        """
    def __hash__(self):
        """
        A hash function.

        EXAMPLES::

            sage: _=hash(TermOrder('lex'))
        """
    @property
    def sortkey(self):
        """
        The default ``sortkey`` method for this term order.

        EXAMPLES::

            sage: O = TermOrder()
            sage: O.sortkey.__func__ is O.sortkey_lex.__func__
            True
            sage: O = TermOrder('deglex')
            sage: O.sortkey.__func__ is O.sortkey_deglex.__func__
            True
        """
    @property
    def greater_tuple(self):
        """
        The default ``greater_tuple`` method for this term order.

        EXAMPLES::

            sage: O = TermOrder()
            sage: O.greater_tuple.__func__ is O.greater_tuple_lex.__func__
            True
            sage: O = TermOrder('deglex')
            sage: O.greater_tuple.__func__ is O.greater_tuple_deglex.__func__
            True
        """
    def sortkey_matrix(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the matrix
        term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='m(1,3,1,0)')                # needs sage.rings.number_field
            sage: y > x^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: y > x^3                                                               # needs sage.rings.number_field
            False
        """
    def sortkey_lex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='lex')                       # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: x > 1                                                                 # needs sage.rings.number_field
            True
        """
    def sortkey_invlex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the inversed
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='invlex')                    # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x > 1                                                                 # needs sage.rings.number_field
            True
        """
    def sortkey_deglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the degree
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='deglex')                    # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x > 1                                                                 # needs sage.rings.number_field
            True
        """
    def sortkey_degrevlex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        degree reversed lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='degrevlex')                 # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x > 1                                                                 # needs sage.rings.number_field
            True
        """
    def sortkey_neglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the negative
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='neglex')                    # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x > 1                                                                 # needs sage.rings.number_field
            False
        """
    def sortkey_negdegrevlex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        negative degree reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='negdegrevlex')              # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: x > 1                                                                 # needs sage.rings.number_field
            False
        """
    def sortkey_negdeglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        negative degree lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='negdeglex')                 # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: x > 1                                                                 # needs sage.rings.number_field
            False
        """
    def sortkey_degneglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        degree negative lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='degneglex')               # needs sage.rings.number_field
            sage: x*y > y*z  # indirect doctest                                         # needs sage.rings.number_field
            False
            sage: x*y > x                                                               # needs sage.rings.number_field
            True
        """
    def sortkey_wdegrevlex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        weighted degree reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('wdegrevlex',(3,2))
            sage: P.<x,y> = PolynomialRing(QQbar, 2, order=t)                           # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x^2 > y^3                                                             # needs sage.rings.number_field
            True
        """
    def sortkey_wdeglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        weighted degree lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('wdeglex',(3,2))
            sage: P.<x,y> = PolynomialRing(QQbar, 2, order=t)                           # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: x > y                                                                 # needs sage.rings.number_field
            True
        """
    def sortkey_negwdeglex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        negative weighted degree lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('negwdeglex',(3,2))
            sage: P.<x,y> = PolynomialRing(QQbar, 2, order=t)                           # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: x^2 > y^3                                                             # needs sage.rings.number_field
            True
        """
    def sortkey_negwdegrevlex(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        negative weighted degree reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('negwdegrevlex',(3,2))
            sage: P.<x,y> = PolynomialRing(QQbar, 2, order=t)                           # needs sage.rings.number_field
            sage: x > y^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: x^2 > y^3                                                             # needs sage.rings.number_field
            True
        """
    def sortkey_block(self, f):
        """
        Return the sortkey of an exponent tuple with respect to the
        block order as specified when constructing this element.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: P.<a,b,c,d,e,f> = PolynomialRing(QQbar, 6,                            # needs sage.rings.number_field
            ....:                                  order='degrevlex(3),degrevlex(3)')
            sage: a > c^4  # indirect doctest                                           # needs sage.rings.number_field
            False
            sage: a > e^4                                                               # needs sage.rings.number_field
            True

        TESTS:

        Check that the issue in :issue:`27139` is fixed::

            sage: R.<x,y,z,t> = PolynomialRing(AA, order='lex(2),lex(2)')               # needs sage.rings.number_field
            sage: x > y                                                                 # needs sage.rings.number_field
            True
        """
    def greater_tuple_matrix(self, f, g):
        """
        Return the greater exponent tuple with respect to the matrix
        term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQbar, 2, order='m(1,3,1,0)')                # needs sage.rings.number_field
            sage: y > x^2  # indirect doctest                                           # needs sage.rings.number_field
            True
            sage: y > x^3                                                               # needs sage.rings.number_field
            False
        """
    def greater_tuple_lex(self, f, g):
        """
        Return the greater exponent tuple with respect to the
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='lex')                     # needs sage.rings.number_field
            sage: f = x + y^2; f.lm()  # indirect doctest                               # needs sage.rings.number_field
            x

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_invlex(self, f, g):
        """
        Return the greater exponent tuple with respect to the inversed
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='invlex')                  # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            y
            sage: f = y + x^2; f.lm()                                                   # needs sage.rings.number_field
            y

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_deglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the total degree
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='deglex')                  # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            x
            sage: f = x + y^2*z; f.lm()                                                 # needs sage.rings.number_field
            y^2*z

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_degrevlex(self, f, g):
        """
        Return the greater exponent tuple with respect to the total degree
        reversed lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='degrevlex')               # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            x
            sage: f = x + y^2*z; f.lm()                                                 # needs sage.rings.number_field
            y^2*z

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_negdegrevlex(self, f, g):
        """
        Return the greater exponent tuple with respect to the negative
        degree reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='negdegrevlex')
            sage: f = x + y; f.lm() # indirect doctest
            x
            sage: f = x + x^2; f.lm()
            x
            sage: f = x^2*y*z^2 + x*y^3*z; f.lm()
            x*y^3*z

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_negdeglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the negative
        degree lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='negdeglex')
            sage: f = x + y; f.lm() # indirect doctest
            x
            sage: f = x + x^2; f.lm()
            x
            sage: f = x^2*y*z^2 + x*y^3*z; f.lm()
            x^2*y*z^2

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_degneglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the degree negative
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order='degneglex')               # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            y
            sage: f = x + y^2*z; f.lm()                                                 # needs sage.rings.number_field
            y^2*z

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_neglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the negative
        lexicographical term order.

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<a,b,c,d,e,f> = PolynomialRing(QQbar, 6,                            # needs sage.rings.number_field
            ....:                                  order='degrevlex(3),degrevlex(3)')
            sage: f = a + c^4; f.lm()  # indirect doctest                               # needs sage.rings.number_field
            c^4
            sage: g = a + e^4; g.lm()                                                   # needs sage.rings.number_field
            a
        """
    def greater_tuple_wdeglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the weighted degree
        lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('wdeglex',(1,2,3))
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order=t)                         # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            y
            sage: f = x*y + z; f.lm()                                                   # needs sage.rings.number_field
            x*y

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_wdegrevlex(self, f, g):
        """
        Return the greater exponent tuple with respect to the weighted degree
        reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('wdegrevlex',(1,2,3))
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order=t)                         # needs sage.rings.number_field
            sage: f = x + y; f.lm()  # indirect doctest                                 # needs sage.rings.number_field
            y
            sage: f = x + y^2*z; f.lm()                                                 # needs sage.rings.number_field
            y^2*z

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_negwdeglex(self, f, g):
        """
        Return the greater exponent tuple with respect to the negative
        weighted degree lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: t = TermOrder('negwdeglex',(1,2,3))
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order=t)
            sage: f = x + y; f.lm() # indirect doctest
            x
            sage: f = x + x^2; f.lm()
            x
            sage: f = x^3 + z; f.lm()
            x^3

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_negwdegrevlex(self, f, g):
        """
        Return the greater exponent tuple with respect to the negative
        weighted degree reverse lexicographical term order.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: t = TermOrder('negwdegrevlex',(1,2,3))
            sage: P.<x,y,z> = PolynomialRing(QQbar, 3, order=t)
            sage: f = x + y; f.lm() # indirect doctest
            x
            sage: f = x + x^2; f.lm()
            x
            sage: f = x^3 + z; f.lm()
            x^3

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.
        """
    def greater_tuple_block(self, f, g):
        """
        Return the greater exponent tuple with respect to the block
        order as specified when constructing this element.

        This method is called by the lm/lc/lt methods of
        ``MPolynomial_polydict``.

        INPUT:

        - ``f`` -- exponent tuple

        - ``g`` -- exponent tuple

        EXAMPLES::

            sage: P.<a,b,c,d,e,f> = PolynomialRing(QQbar, 6,                            # needs sage.rings.number_field
            ....:                                  order='degrevlex(3),degrevlex(3)')
            sage: f = a + c^4; f.lm()  # indirect doctest                               # needs sage.rings.number_field
            c^4
            sage: g = a + e^4; g.lm()                                                   # needs sage.rings.number_field
            a
        """
    def tuple_weight(self, f):
        """
        Return the weight of tuple f.

        INPUT:

        - ``f`` -- exponent tuple

        EXAMPLES::

            sage: t = TermOrder('wdeglex',(1,2,3))
            sage: P.<a,b,c> = PolynomialRing(QQbar, order=t)                            # needs sage.rings.number_field
            sage: P.term_order().tuple_weight([3,2,1])                                  # needs sage.rings.number_field
            10
        """
    def name(self):
        """
        EXAMPLES::

            sage: TermOrder('lex').name()
            'lex'
        """
    def singular_str(self):
        '''
        Return a SINGULAR representation of ``self``.

        Used to convert polynomial rings to their SINGULAR representation.

        EXAMPLES::

            sage: P = PolynomialRing(GF(127), 10, names=\'x\',
            ....:                    order=\'lex(3),deglex(5),lex(2)\')
            sage: T = P.term_order()
            sage: T.singular_str()
            \'(lp(3),Dp(5),lp(2))\'
            sage: P._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: ZZ/127...
            // number of vars : 10
            //        block   1 : ordering lp
            //                  : names    x0 x1 x2
            //        block   2 : ordering Dp
            //                  : names    x3 x4 x5 x6 x7
            //        block   3 : ordering lp
            //                  : names    x8 x9
            //        block   4 : ordering C

        The ``degneglex`` ordering is somehow special, it looks like a block
        ordering in SINGULAR::

            sage: T = TermOrder("degneglex", 2)
            sage: P = PolynomialRing(QQ,2, names=\'x\', order=T)
            sage: T = P.term_order()
            sage: T.singular_str()
            \'(a(1:2),ls(2))\'

            sage: T = TermOrder("degneglex", 2) + TermOrder("degneglex", 2)
            sage: P = PolynomialRing(QQ,4, names=\'x\', order=T)
            sage: T = P.term_order()
            sage: T.singular_str()
            \'(a(1:2),ls(2),a(1:2),ls(2))\'
            sage: P._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 4
            //        block   1 : ordering a
            //                  : names    x0 x1
            //                  : weights   1  1
            //        block   2 : ordering ls
            //                  : names    x0 x1
            //        block   3 : ordering a
            //                  : names    x2 x3
            //                  : weights   1  1
            //        block   4 : ordering ls
            //                  : names    x2 x3
            //        block   5 : ordering C

        The position of the ``ordering C`` block can be controlled by setting
        ``_singular_ringorder_column`` attribute to an integer::

            sage: T = TermOrder("degneglex", 2) + TermOrder("degneglex", 2)
            sage: T._singular_ringorder_column = 0
            sage: P = PolynomialRing(QQ, 4, names=\'x\', order=T)
            sage: P._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 4
            //        block   1 : ordering C
            //        block   2 : ordering a
            //                  : names    x0 x1
            //                  : weights   1  1
            //        block   3 : ordering ls
            //                  : names    x0 x1
            //        block   4 : ordering a
            //                  : names    x2 x3
            //                  : weights   1  1
            //        block   5 : ordering ls
            //                  : names    x2 x3

            sage: T._singular_ringorder_column = 1
            sage: P = PolynomialRing(QQ, 4, names=\'y\', order=T)
            sage: P._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 4
            //        block   1 : ordering c
            //        block   2 : ordering a
            //                  : names    y0 y1
            //                  : weights   1  1
            //        block   3 : ordering ls
            //                  : names    y0 y1
            //        block   4 : ordering a
            //                  : names    y2 y3
            //                  : weights   1  1
            //        block   5 : ordering ls
            //                  : names    y2 y3

            sage: T._singular_ringorder_column = 2
            sage: P = PolynomialRing(QQ, 4, names=\'z\', order=T)
            sage: P._singular_()                                                        # needs sage.libs.singular
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 4
            //        block   1 : ordering a
            //                  : names    z0 z1
            //                  : weights   1  1
            //        block   2 : ordering C
            //        block   3 : ordering ls
            //                  : names    z0 z1
            //        block   4 : ordering a
            //                  : names    z2 z3
            //                  : weights   1  1
            //        block   5 : ordering ls
            //                  : names    z2 z3
        '''
    def singular_moreblocks(self):
        '''
        Return a the number of additional blocks SINGULAR needs to allocate
        for handling non-native orderings like ``degneglex``.

        EXAMPLES::

            sage: P = PolynomialRing(GF(127), 10, names=\'x\',
            ....:                    order=\'lex(3),deglex(5),lex(2)\')
            sage: T = P.term_order()
            sage: T.singular_moreblocks()
            0
            sage: P = PolynomialRing(GF(127), 10, names=\'x\',
            ....:                    order=\'lex(3),degneglex(5),lex(2)\')
            sage: T = P.term_order()
            sage: T.singular_moreblocks()
            1
            sage: P = PolynomialRing(GF(127), 10, names=\'x\',
            ....:                    order=\'degneglex(5),degneglex(5)\')
            sage: T = P.term_order()
            sage: T.singular_moreblocks()
            2

        TESTS:

        The \'degneglex\' ordering is somehow special: SINGULAR handles it
        using an extra weight vector block. ::

            sage: T = TermOrder("degneglex", 2)
            sage: P = PolynomialRing(QQ,2, names=\'x\', order=T)
            sage: T = P.term_order()
            sage: T.singular_moreblocks()
            1
            sage: T = TermOrder("degneglex", 2) + TermOrder("degneglex", 2)
            sage: P = PolynomialRing(QQ,4, names=\'x\', order=T)
            sage: T = P.term_order()
            sage: T.singular_moreblocks()
            2
        '''
    def macaulay2_str(self):
        """
        Return a Macaulay2 representation of ``self``.

        Used to convert polynomial rings to their Macaulay2
        representation.

        EXAMPLES::

            sage: P = PolynomialRing(GF(127), 8, names='x', order='degrevlex(3),lex(5)')
            sage: T = P.term_order()
            sage: T.macaulay2_str()
            '{GRevLex => 3,Lex => 5}'
            sage: P._macaulay2_().options()['MonomialOrder']    # optional - macaulay2
            {MonomialSize => 16  }
            {GRevLex => {1, 1, 1}}
            {Lex => 5            }
            {Position => Up      }
        """
    def magma_str(self):
        '''
        Return a MAGMA representation of ``self``.

        Used to convert polynomial rings to their MAGMA representation.

        EXAMPLES::

            sage: P = PolynomialRing(GF(127), 10, names=\'x\', order=\'degrevlex\')
            sage: magma(P)                                      # optional - magma
            Polynomial ring of rank 10 over GF(127)
            Order: Graded Reverse Lexicographical
            Variables: x0, x1, x2, x3, x4, x5, x6, x7, x8, x9

        ::

            sage: T = P.term_order()
            sage: T.magma_str()
            \'"grevlex"\'
        '''
    def blocks(self):
        """
        Return the term order blocks of ``self``.

        NOTE:

        This method has been added in :issue:`11316`. There used
        to be an *attribute* of the same name and the same content.
        So, it is a backward incompatible syntax change.

        EXAMPLES::

            sage: t = TermOrder('deglex',2) + TermOrder('lex',2)
            sage: t.blocks()
            (Degree lexicographic term order, Lexicographic term order)
        """
    def matrix(self):
        '''
        Return the matrix defining matrix term order.

        EXAMPLES::

            sage: t = TermOrder("M(1,2,0,1)")                                           # needs sage.modules
            sage: t.matrix()                                                            # needs sage.modules
            [1 2]
            [0 1]
        '''
    def weights(self):
        """
        Return the weights for weighted term orders.

        EXAMPLES::

            sage: t = TermOrder('wdeglex',(2,3))
            sage: t.weights()
            (2, 3)
        """
    def __eq__(self, other):
        '''
        Return ``True`` if ``self`` and ``other`` are equal.

        EXAMPLES::

            sage: TermOrder(\'lex\') == TermOrder(\'lex\',3)
            True

        ::

            sage: TermOrder(\'degrevlex\') == TermOrder(\'lex\')
            False

        ::

            sage: T1 = TermOrder(\'lex\',2) + TermOrder(\'lex\',3)
            sage: T2 = TermOrder(\'lex\',3) + TermOrder(\'lex\',2)
            sage: T1 == T2
            False

        ::

            sage: T1 = TermOrder(\'lex\',2) + TermOrder(\'neglex\',3)
            sage: T2 = TermOrder(\'lex\',2) + TermOrder(\'neglex\',3)
            sage: T1 == T2
            True

        TESTS:

        We assert that comparisons take into account the block size of
        orderings (cf. :issue:`24981`)::

            sage: R = PolynomialRing(QQ, 6, \'x\', order="lex(1),degrevlex(5)")
            sage: S = R.change_ring(order="lex(2),degrevlex(4)")
            sage: R == S
            False
            sage: S.term_order() == R.term_order()
            False
            sage: S.term_order() == TermOrder(\'lex\', 2) + TermOrder(\'degrevlex\', 4)
            True
        '''
    def __ne__(self, other):
        """
        Return ``True`` if ``self`` and ``other`` are not equal.

        EXAMPLES::

            sage: T1 = TermOrder('lex',2) + TermOrder('lex',3)
            sage: T2 = TermOrder('lex',3) + TermOrder('lex',2)
            sage: T1 != T2
            True
        """
    def __add__(self, other):
        """
        Construct a block order combining ``self`` and ``other``.

        INPUT:

        - ``other`` -- a term order

        OUTPUT: a block order

        EXAMPLES::

            sage: from sage.rings.polynomial.term_order import TermOrder
            sage: TermOrder('deglex',2) + TermOrder('degrevlex(3),neglex(3)')
            Block term order with blocks:
            (Degree lexicographic term order of length 2,
             Degree reverse lexicographic term order of length 3,
             Negative lexicographic term order of length 3)
        """
    def __len__(self) -> int:
        """
        Return the length of this term order, i.e. the number of
        variables it covers. This may be zero for indefinitely many
        variables.

        EXAMPLES::

            sage: T = TermOrder('lex')
            sage: len(T)
            0
            sage: T = TermOrder('lex', 2) + TermOrder('degrevlex', 3)
            sage: len(T)
            5
        """
    def __getitem__(self, i):
        """
        Return the `i`-th block of this term order.

        INPUT:

        - ``i`` -- index

        EXAMPLES::

            sage: T = TermOrder('lex')
            sage: T[0]
            Lexicographic term order

        ::

            sage: T = TermOrder('lex', 2) + TermOrder('degrevlex', 3)
            sage: T[1]
            Degree reverse lexicographic term order

        Note that ``len(self)`` does not count blocks but
        variables.

        ::

            sage: T = TermOrder('lex', 2) + TermOrder('degrevlex', 3)
            sage: T[len(T)-1]
            Traceback (most recent call last):
            \\dots
            IndexError: tuple index out of range
        """
    def __iter__(self):
        """
        Iterate over the blocks of this term order.

        EXAMPLES::

            sage: T = TermOrder('lex')
            sage: list(T) # indirect doctest
            [Lexicographic term order]

        ::

            sage: T = TermOrder('lex', 2) + TermOrder('degrevlex', 3)
            sage: list(T)
            [Lexicographic term order, Degree reverse lexicographic term order]

        Note that ``len(self)`` and
        ``len(list(self))`` are not the same. The former counts
        the number of variables in ``self`` while the latter
        counts the number of blocks.
        """
    def is_global(self):
        """
        Return ``True`` if this term order is definitely
        global. Return false otherwise, which includes
        unknown term orders.

        EXAMPLES::

            sage: T = TermOrder('lex')
            sage: T.is_global()
            True
            sage: T = TermOrder('degrevlex', 3) + TermOrder('degrevlex', 3)
            sage: T.is_global()
            True
            sage: T = TermOrder('degrevlex', 3) + TermOrder('negdegrevlex', 3)
            sage: T.is_global()
            False
            sage: T = TermOrder('degneglex', 3)
            sage: T.is_global()
            True
            sage: T = TermOrder('invlex', 3)
            sage: T.is_global()
            True
        """
    def is_local(self):
        """
        Return ``True`` if this term order is definitely
        local. Return false otherwise, which includes
        unknown term orders.

        EXAMPLES::

            sage: T = TermOrder('lex')
            sage: T.is_local()
            False
            sage: T = TermOrder('negdeglex', 3) + TermOrder('negdegrevlex', 3)
            sage: T.is_local()
            True
            sage: T = TermOrder('degrevlex', 3) + TermOrder('negdegrevlex', 3)
            sage: T.is_local()
            False
        """
    def is_block_order(self):
        """
        Return ``True`` if ``self`` is a block term order.

        EXAMPLES::

            sage: t = TermOrder('deglex',2) + TermOrder('lex',2)
            sage: t.is_block_order()
            True
        """
    def is_weighted_degree_order(self):
        """
        Return ``True`` if ``self`` is a weighted degree term order.

        EXAMPLES::

            sage: t = TermOrder('wdeglex',(2,3))
            sage: t.is_weighted_degree_order()
            True
        """

def termorder_from_singular(S):
    """
    Return the Sage term order of the basering in the given Singular interface.

    INPUT:

    An instance of the Singular interface.

    EXAMPLES::

        sage: from sage.rings.polynomial.term_order import termorder_from_singular
        sage: singular.eval('ring r1 = (9,x),(a,b,c,d,e,f),(M((1,2,3,0)),wp(2,3),lp)')  # needs sage.libs.singular
        ''
        sage: termorder_from_singular(singular)                                         # needs sage.libs.singular
        Block term order with blocks:
        (Matrix term order with matrix
           [1 2]
           [3 0],
         Weighted degree reverse lexicographic term order with weights (2, 3),
         Lexicographic term order of length 2)

    A term order in Singular also involves information on orders for modules.
    This information is reflected in ``_singular_ringorder_column`` attribute of
    the term order. ::

        sage: # needs sage.libs.singular
        sage: singular.ring(0, '(x,y,z,w)', '(C,dp(2),lp(2))')
        polynomial ring, over a field, global ordering
        // coefficients: QQ...
        // number of vars : 4
        //        block   1 : ordering C
        //        block   2 : ordering dp
        //                  : names    x y
        //        block   3 : ordering lp
        //                  : names    z w
        sage: T = termorder_from_singular(singular)
        sage: T
        Block term order with blocks:
        (Degree reverse lexicographic term order of length 2,
         Lexicographic term order of length 2)
        sage: T._singular_ringorder_column
        0

        sage: # needs sage.libs.singular
        sage: singular.ring(0, '(x,y,z,w)', '(c,dp(2),lp(2))')
        polynomial ring, over a field, global ordering
        // coefficients: QQ...
        // number of vars : 4
        //        block   1 : ordering c
        //        block   2 : ordering dp
        //                  : names    x y
        //        block   3 : ordering lp
        //                  : names    z w
        sage: T = termorder_from_singular(singular)
        sage: T
        Block term order with blocks:
        (Degree reverse lexicographic term order of length 2,
         Lexicographic term order of length 2)
        sage: T._singular_ringorder_column
        1

    TESTS:

    Check that ``degneglex`` term orders are converted correctly
    (:issue:`29635`)::

        sage: # needs sage.libs.singular
        sage: _ = singular.ring(0, '(x,y,z,w)', '(a(1:4),ls(4))')
        sage: termorder_from_singular(singular).singular_str()
        '(a(1:4),ls(4))'
        sage: _ = singular.ring(0, '(x,y,z,w)', '(a(1:2),ls(2),a(1:2),ls(2))')
        sage: termorder_from_singular(singular).singular_str()
        '(a(1:2),ls(2),a(1:2),ls(2))'
        sage: _ = singular.ring(0, '(x,y,z,w)', '(a(1:2),ls(2),C,a(1:2),ls(2))')
        sage: termorder_from_singular(singular).singular_str()
        '(a(1:2),ls(2),C,a(1:2),ls(2))'
        sage: PolynomialRing(QQ, 'x,y', order='degneglex')('x^2')._singular_().sage()
        x^2
    """
