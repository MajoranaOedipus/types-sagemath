class ModularPolynomialDatabase:
    def __getitem__(self, level):
        """
        Return the modular polynomial of given level, or an error if
        there is no such polynomial in the database.

        EXAMPLES::

            sage: # optional - database_kohel
            sage: DBMP = ClassicalModularPolynomialDatabase()
            sage: f = DBMP[29]
            sage: f.degree()
            58
            sage: f.coefficient([28,28])
            400152899204646997840260839128
            sage: DBMP[50]
            Traceback (most recent call last):
            ...
            FileNotFoundError: file not found in the Kohel database
        """

class ModularCorrespondenceDatabase(ModularPolynomialDatabase): ...

class ClassicalModularPolynomialDatabase(ModularPolynomialDatabase):
    """
    The database of classical modular polynomials, i.e. the polynomials
    Phi_N(X,Y) relating the j-functions j(q) and j(q^N).
    """
    model: str

class DedekindEtaModularPolynomialDatabase(ModularPolynomialDatabase):
    """
    The database of modular polynomials Phi_N(X,Y) relating a quotient
    of Dedekind eta functions, well-defined on X_0(N), relating x(q) and
    the j-function j(q).
    """
    model: str

class DedekindEtaModularCorrespondenceDatabase(ModularCorrespondenceDatabase):
    """
    The database of modular correspondences in `X_0(p) \\times X_0(p)`, where
    the model of the curves `X_0(p) = \\Bold{P}^1` are specified by quotients of
    Dedekind's eta function.
    """
    model: str

class AtkinModularPolynomialDatabase(ModularPolynomialDatabase):
    """
    The database of modular polynomials Phi(x,j) for `X_0(p)`, where
    x is a function on invariant under the Atkin-Lehner invariant,
    with pole of minimal order at infinity.
    """
    model: str

class AtkinModularCorrespondenceDatabase(ModularCorrespondenceDatabase):
    model: str
