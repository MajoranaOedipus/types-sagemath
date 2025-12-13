from .constructor import EllipticCurve as EllipticCurve
from _typeshed import Incomplete

class EllipticCurves:
    def rank(self, rank, tors: int = 0, n: int = 10, labels: bool = False):
        """
        Return a list of at most `n` curves with given
        rank and torsion order.

        INPUT:

        - ``rank`` -- integer; the desired rank

        - ``tors`` -- integer (default: 0); the desired torsion order (ignored if 0)

        - ``n`` -- integer (default: 10); the maximum number of curves returned

        - ``labels`` -- boolean (default: ``False``); if ``True``, return Cremona
          labels instead of curves

        OUTPUT: list at most `n` of elliptic curves of required rank

        EXAMPLES::

            sage: elliptic_curves.rank(n=5, rank=3, tors=2, labels=True)
            ['59450i1', '59450i2', '61376c1', '61376c2', '65481c1']

        ::

            sage: elliptic_curves.rank(n=5, rank=0, tors=5, labels=True)
            ['11a1', '11a3', '38b1', '50b1', '50b2']

        ::

            sage: elliptic_curves.rank(n=5, rank=1, tors=7, labels=True)
            ['574i1', '4730k1', '6378c1']

        ::

            sage: e = elliptic_curves.rank(6)[0]; e.ainvs(), e.conductor()
            ((1, 1, 0, -2582, 48720), 5187563742)
            sage: e = elliptic_curves.rank(7)[0]; e.ainvs(), e.conductor()
            ((0, 0, 0, -10012, 346900), 382623908456)
            sage: e = elliptic_curves.rank(8)[0]; e.ainvs(), e.conductor()
            ((1, -1, 0, -106384, 13075804), 249649566346838)

        For large conductors, the labels are not known::

            sage: L = elliptic_curves.rank(6, n=3); L
            [Elliptic Curve defined by y^2 + x*y = x^3 + x^2 - 2582*x + 48720 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 - 7077*x + 235516 over Rational Field,
             Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 2326*x + 43456 over Rational Field]
            sage: L[0].cremona_label()
            Traceback (most recent call last):
            ...
            LookupError: Cremona database does not contain entry for Elliptic Curve
            defined by y^2 + x*y = x^3 + x^2 - 2582*x + 48720 over Rational Field
            sage: elliptic_curves.rank(6, n=3, labels=True)
            []
        """

elliptic_curves: Incomplete
