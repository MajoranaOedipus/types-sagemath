from sage.rings.integer import Integer as Integer

class Nonexact:
    """
    A non-exact object with default precision.

    INPUT:

    - ``prec`` -- nonnegative integer representing the default precision of
      ``self`` (default: 20)
    """
    def __init__(self, prec: int = 20) -> None: ...
    def default_prec(self):
        """
        Return the default precision for ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: R = QQ[[x]]
            sage: R.default_prec()
            20

        ::

            sage: R.<x> = PowerSeriesRing(QQ, default_prec=10)
            sage: R.default_prec()
            10
        """
