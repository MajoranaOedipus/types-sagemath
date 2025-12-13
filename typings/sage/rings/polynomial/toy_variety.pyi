def is_triangular(B) -> bool:
    """
    Check whether the basis ``B`` of an ideal is triangular.

    That is: check whether the largest variable in ``B[i]`` with
    respect to the ordering of the base ring ``R`` is ``R.gens()[i]``.

    The algorithm is based on the definition of a triangular basis,
    given by Lazard in 1992 in [Laz1992]_.

    INPUT:

    - ``B`` -- list/tuple of polynomials or a multivariate polynomial ideal

    OUTPUT: ``True`` if the basis is triangular; ``False`` otherwise

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_variety import is_triangular
        sage: R.<x,y,z> = PolynomialRing(QQ)
        sage: p1 = x^2*y + z^2
        sage: p2 = y*z + z^3
        sage: p3 = y+z
        sage: is_triangular(R.ideal(p1,p2,p3))
        False
        sage: p3 = z^2 - 3
        sage: is_triangular(R.ideal(p1,p2,p3))
        True
    """
def coefficient_matrix(polys):
    """
    Generate the matrix ``M`` whose entries are the coefficients of ``polys``.

    The entries of row ``i`` of ``M`` consist of the coefficients of
    ``polys[i]``.

    INPUT:

    - ``polys`` -- list/tuple of polynomials

    OUTPUT: a matrix ``M`` of the coefficients of ``polys``

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_variety import coefficient_matrix
        sage: R.<x,y> = PolynomialRing(QQ)
        sage: coefficient_matrix([x^2 + 1, y^2 + 1, x*y + 1])                           # needs sage.modules
        [1 0 0 1]
        [0 0 1 1]
        [0 1 0 1]

    .. NOTE::

        This function may be merged with
        :meth:`sage.rings.polynomial.multi_polynomial_sequence.PolynomialSequence_generic.coefficient_matrix()` in the future.
    """
def is_linearly_dependent(polys) -> bool:
    """
    Decide whether the polynomials of ``polys`` are linearly dependent.

    Here ``polys`` is a collection of polynomials.

    The algorithm creates a matrix of coefficients of the monomials of
    ``polys``. It computes the echelon form of the matrix, then checks whether
    any of the rows is the zero vector.

    Essentially this relies on the fact that the monomials are linearly
    independent, and therefore is building a linear map from the vector space of
    the monomials to the canonical basis of ``R^n``, where ``n`` is the number of
    distinct monomials in ``polys``. There is a zero vector iff there is a
    linear dependence among ``polys``.

    The case where ``polys=[]`` is considered to be not linearly dependent.

    INPUT:

    - ``polys`` -- list/tuple of polynomials

    OUTPUT:

    ``True`` if the elements of ``polys`` are linearly dependent;
    ``False`` otherwise.

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_variety import is_linearly_dependent
        sage: R.<x,y> = PolynomialRing(QQ)
        sage: B = [x^2 + 1, y^2 + 1, x*y + 1]
        sage: p = 3*B[0] - 2*B[1] + B[2]
        sage: is_linearly_dependent(B + [p])                                            # needs sage.modules
        True
        sage: p = x*B[0]
        sage: is_linearly_dependent(B + [p])                                            # needs sage.modules
        False
        sage: is_linearly_dependent([])
        False
        sage: R.<x> = PolynomialRing(QQ)
        sage: B = [x^147 + x^99,
        ....:      2*x^123 + x^75,
        ....:      x^147 + 2*x^123 + 2*x^75,
        ....:      2*x^147 + x^99 + x^75]
        sage: is_linearly_dependent(B)
        True
    """
def linear_representation(p, polys):
    """
    Assuming that ``p`` is a linear combination of ``polys``,
    determine coefficients that describe the linear combination.

    This probably does not work for any inputs except ``p``, a polynomial,
    and ``polys``, a sequence of polynomials.
    If ``p`` is not in fact a linear combination of ``polys``,
    the function raises an exception.

    The algorithm creates a matrix of coefficients of the monomials of
    ``polys`` and ``p``, with the coefficients of ``p`` in the last
    row. It augments this matrix with the appropriate identity matrix, then
    computes the echelon form of the augmented matrix. The last row should
    contain zeroes in the first columns, and the last
    columns contain a linear dependence relation. Solving for
    the desired linear relation is straightforward.

    INPUT:

    - ``p`` -- a polynomial
    - ``polys`` -- list/tuple of polynomials

    OUTPUT:

    If ``n == len(polys)``, returns ``[a[0],a[1],...,a[n-1]]``
    such that ``p == a[0]*poly[0] + ... + a[n-1]*poly[n-1]``.

    EXAMPLES::

        sage: # needs sage.modules sage.rings.finite_rings
        sage: from sage.rings.polynomial.toy_variety import linear_representation
        sage: R.<x,y> = PolynomialRing(GF(32003))
        sage: B = [x^2 + 1, y^2 + 1, x*y + 1]
        sage: p = 3*B[0] - 2*B[1] + B[2]
        sage: linear_representation(p, B)
        [3, 32001, 1]
    """
def triangular_factorization(B, n: int = -1):
    """
    Compute the triangular factorization of the Groebner basis ``B`` of an ideal.

    This will not work properly if ``B`` is not a Groebner basis!

    The algorithm used is that described in a 1992 paper by Daniel Lazard [Laz1992]_.
    It is not necessary for the term ordering to be lexicographic.

    INPUT:

    - ``B`` -- list/tuple of polynomials or a multivariate polynomial ideal
    - ``n`` -- the recursion parameter (default: ``-1``)

    OUTPUT: list ``T`` of triangular sets ``T_0``, ``T_1``, etc.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.misc.verbose import set_verbose
        sage: set_verbose(0)
        sage: from sage.rings.polynomial.toy_variety import triangular_factorization
        sage: R.<x,y,z> = PolynomialRing(GF(32003))
        sage: p1 = x^2*(x-1)^3*y^2*(z-3)^3
        sage: p2 = z^2 - z
        sage: p3 = (x-2)^2*(y-1)^3
        sage: I = R.ideal(p1,p2,p3)
        sage: triangular_factorization(I.groebner_basis())                              # needs sage.libs.singular
        [[x^2 - 4*x + 4, y, z - 1],
         [x^5 - 3*x^4 + 3*x^3 - x^2, y - 1, z - 1],
         [x^2 - 4*x + 4, y, z],
         [x^5 - 3*x^4 + 3*x^3 - x^2, y - 1, z]]
    """
def elim_pol(B, n: int = -1):
    """
    Find the unique monic polynomial of lowest degree and lowest variable
    in the ideal described by ``B``.

    For the purposes of the triangularization algorithm, it is necessary to
    preserve the ring, so ``n`` specifies which variable to check.
    By default, we check the last one, which should also be the smallest.

    The algorithm may not work if you are trying to cheat:
    ``B`` should describe the Groebner basis of a zero-dimensional ideal.
    However, it is not necessary for the Groebner basis to be lexicographic.

    The algorithm is taken from a 1993 paper by Lazard [Laz1992]_.

    INPUT:

    - ``B`` -- list/tuple of polynomials or a multivariate polynomial ideal
    - ``n`` -- the variable to check (see above) (default: ``-1``)

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.misc.verbose import set_verbose
        sage: set_verbose(0)
        sage: from sage.rings.polynomial.toy_variety import elim_pol
        sage: R.<x,y,z> = PolynomialRing(GF(32003))
        sage: p1 = x^2*(x-1)^3*y^2*(z-3)^3
        sage: p2 = z^2 - z
        sage: p3 = (x-2)^2*(y-1)^3
        sage: I = R.ideal(p1,p2,p3)
        sage: elim_pol(I.groebner_basis())                                              # needs sage.libs.singular
        z^2 - z
    """
