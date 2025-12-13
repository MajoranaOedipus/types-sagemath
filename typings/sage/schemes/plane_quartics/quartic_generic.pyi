import sage.schemes.curves.projective_curve as projective_curve

def is_QuarticCurve(C):
    """
    Check whether ``C`` is a Quartic Curve.

    EXAMPLES::

        sage: from sage.schemes.plane_quartics.quartic_generic import is_QuarticCurve
        sage: x,y,z = PolynomialRing(QQ, ['x','y','z']).gens()
        sage: Q = QuarticCurve(x**4 + y**4 + z**4)
        sage: is_QuarticCurve(Q)
        doctest:warning...
        DeprecationWarning: The function is_QuarticCurve is deprecated; use 'isinstance(..., QuarticCurve_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
    """

class QuarticCurve_generic(projective_curve.ProjectivePlaneCurve):
    def genus(self):
        """
        Return the genus of ``self``.

        EXAMPLES::

            sage: x,y,z = PolynomialRing(QQ, ['x','y','z']).gens()
            sage: Q = QuarticCurve(x**4 + y**4 + z**4)
            sage: Q.genus()
            3
        """
