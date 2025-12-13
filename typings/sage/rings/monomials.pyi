from sage.structure.sequence import Sequence as Sequence

def monomials(v, n):
    """
    Given two lists ``v`` and ``n``, of exactly the same length,
    return all monomials in the elements of ``v``, where
    variable ``i`` (i.e., ``v[i]``) in the monomial appears to
    degree strictly less than ``n[i]``.

    INPUT:

    - ``v`` -- list of ring elements

    - ``n`` -- list of integers

    EXAMPLES::

        sage: monomials([x], [3])                                                       # needs sage.symbolic
        [1, x, x^2]
        sage: R.<x,y,z> = QQ[]
        sage: monomials([x,y], [5,5])
        [1, y, y^2, y^3, y^4, x, x*y, x*y^2, x*y^3, x*y^4, x^2, x^2*y, x^2*y^2, x^2*y^3, x^2*y^4, x^3, x^3*y, x^3*y^2, x^3*y^3, x^3*y^4, x^4, x^4*y, x^4*y^2, x^4*y^3, x^4*y^4]
        sage: monomials([x,y,z], [2,3,2])
        [1, z, y, y*z, y^2, y^2*z, x, x*z, x*y, x*y*z, x*y^2, x*y^2*z]
    """
