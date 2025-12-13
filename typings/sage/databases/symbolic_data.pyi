from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

class SymbolicData:
    """
    Database of ideals as distributed by The SymbolicData Project
    (http://symbolicdata.org).

    This class needs the optional ``database_symbolic_data`` package to be
    installed.
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: sd = SymbolicData(); sd # optional - database_symbolic_data
            SymbolicData with 372 ideals
        """
    def get_ideal(self, name, base_ring=..., term_order: str = 'degrevlex'):
        """
        Return the ideal given by 'name' over the base ring given by
        'base_ring' in a polynomial ring with the term order given by
        'term_order'.

        INPUT:

        - ``name`` -- name as on the symbolic data website
        - ``base_ring`` -- base ring for the polynomial ring (default: ``QQ``)
        - ``term_order`` -- term order for the polynomial ring (default: ``degrevlex``)

        OUTPUT: ideal as given by ``name`` in ``PolynomialRing(base_ring,vars,term_order)``

        EXAMPLES::

            sage: sd = SymbolicData() # optional - database_symbolic_data
            sage: sd.get_ideal('Katsura_3',GF(127),'degrevlex') # optional - database_symbolic_data
            Ideal (u0 + 2*u1 + 2*u2 + 2*u3 - 1,
                   u1^2 + 2*u0*u2 + 2*u1*u3 - u2,
                   2*u0*u1 + 2*u1*u2 + 2*u2*u3 - u1,
                   u0^2 + 2*u1^2 + 2*u2^2 + 2*u3^2 - u0) of Multivariate Polynomial Ring in u0, u1, u2, u3 over Finite Field of size 127
        """
    def __getattr__(self, name):
        """
        EXAMPLES::

           sage: sd = SymbolicData() # optional - database_symbolic_data
           sage: sd.Cyclic5 # optional - database_symbolic_data
           Traceback (most recent call last):
           ...
           AttributeError: no ideal matching 'Cyclic5' found in database...

           sage: sd.Cyclic_5 # optional - database_symbolic_data
           Ideal (v + w + x + y + z,
                  v*w + w*x + x*y + v*z + y*z,
                  v*w*x + w*x*y + v*w*z + v*y*z + x*y*z,
                  v*w*x*y + v*w*x*z + v*w*y*z + v*x*y*z + w*x*y*z,
                  v*w*x*y*z - 1) of Multivariate Polynomial Ring in v, w, x, y, z over Rational Field
        """
    def __dir__(self):
        """
        EXAMPLES::

            sage: sd = SymbolicData() # optional - database_symbolic_data
            sage: sorted(sd.__dir__())[:10] # optional - database_symbolic_data
            ['Bjoerk_8',
             'Bronstein-86',
             'Buchberger-87',
             'Butcher',
             'Caprasse',
             'Cassou',
             'Cohn_2',
             'Curves__curve10_20',
             'Curves__curve10_20',
             'Curves__curve10_30']
        """
