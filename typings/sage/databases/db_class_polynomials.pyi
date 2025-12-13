disc_format: str
level_format: str

class ClassPolynomialDatabase:
    def __getitem__(self, disc):
        """
        TESTS::

            sage: # optional - database_kohel
            sage: db = HilbertClassPolynomialDatabase()
            sage: db[32]
            x^2 - 52250000*x + 12167000000
            sage: db[123913912]
            Traceback (most recent call last):
            ...
            ValueError: file not found in the Kohel database
        """

class HilbertClassPolynomialDatabase(ClassPolynomialDatabase):
    """
    The database of Hilbert class polynomials.

    EXAMPLES::

        sage: # optional - database_kohel
        sage: db = HilbertClassPolynomialDatabase()
        sage: db[-4]
        x - 1728
        sage: db[-7]
        x + 3375
        sage: f = db[-23]; f
        x^3 + 3491750*x^2 - 5151296875*x + 12771880859375
        sage: f.discriminant().factor()
        -1 * 5^18 * 7^12 * 11^4 * 17^2 * 19^2 * 23
        sage: db[-23]
        x^3 + 3491750*x^2 - 5151296875*x + 12771880859375
    """
    model: str

class AtkinClassPolynomialDatabase(ClassPolynomialDatabase):
    """
    The database of Atkin class polynomials.
    """
    model: str

class WeberClassPolynomialDatabase(ClassPolynomialDatabase):
    """
    The database of Weber class polynomials.
    """

class DedekindEtaClassPolynomialDatabase(ClassPolynomialDatabase):
    """
    The database of Dedekind eta class polynomials.
    """
    model: str
