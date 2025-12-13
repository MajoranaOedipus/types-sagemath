from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic

def gen_lattice(type: str = 'modular', n: int = 4, m: int = 8, q: int = 11, seed=None, quotient=None, dual: bool = False, ntl: bool = False, lattice: bool = False):
    """
    This function generates different types of integral lattice bases
    of row vectors relevant in cryptography.

    Randomness can be set either with ``seed``, or by using
    :func:`sage.misc.randstate.set_random_seed`.

    INPUT:

    - ``type`` -- one of the following strings

      - ``'modular'`` -- default; a class of lattices for which
        asymptotic worst-case to average-case connections hold. For
        more refer to [Aj1996]_
      - ``'random'`` -- special case of modular (n=1); a dense class
        of lattice used for testing basis reduction algorithms
        proposed by Goldstein and Mayer [GM2002]_
      - ``'ideal'`` -- special case of modular; allows for a more
        compact representation proposed by [LM2006]_
      - ``'cyclotomic'`` -- special case of ideal; allows for
        efficient processing proposed by [LM2006]_

    - ``n`` -- determinant size, primal: `det(L) = q^n`, dual: `det(L) = q^{m-n}`.
      For ideal lattices this is also the degree of the quotient polynomial.

    - ``m`` -- lattice dimension, `L \\subseteq Z^m`

    - ``q`` -- coefficient size, `q-Z^m \\subseteq L`

    - ``seed`` -- randomness seed

    - ``quotient`` -- for the type ``'ideal'``, this determines the quotient
      polynomial. Ignored for all other types

    - ``dual`` -- set this flag if you want a basis for `q-dual(L)`, for example
      for Regev's LWE bases [Reg2005]_

    - ``ntl`` -- set this flag if you want the lattice basis in NTL readable
      format

    - ``lattice`` -- set this flag if you want a
      :class:`FreeModule_submodule_with_basis_integer` object instead
      of an integer matrix representing the basis

    OUTPUT: ``B`` a unique size-reduced triangular (primal: lower_left,
    dual: lower_right) basis of row vectors for the lattice in question

    EXAMPLES:

    Modular basis::

        sage: sage.crypto.gen_lattice(m=10, seed=42)
        [11  0  0  0  0  0  0  0  0  0]
        [ 0 11  0  0  0  0  0  0  0  0]
        [ 0  0 11  0  0  0  0  0  0  0]
        [ 0  0  0 11  0  0  0  0  0  0]
        [ 2  4  3  5  1  0  0  0  0  0]
        [ 1 -5 -4  2  0  1  0  0  0  0]
        [-4  3 -1  1  0  0  1  0  0  0]
        [-2 -3 -4 -1  0  0  0  1  0  0]
        [-5 -5  3  3  0  0  0  0  1  0]
        [-4 -3  2 -5  0  0  0  0  0  1]

    Random basis::

        sage: sage.crypto.gen_lattice(type='random', n=1, m=10, q=11^4, seed=42)
        [14641     0     0     0     0     0     0     0     0     0]
        [  431     1     0     0     0     0     0     0     0     0]
        [-4792     0     1     0     0     0     0     0     0     0]
        [ 1015     0     0     1     0     0     0     0     0     0]
        [-3086     0     0     0     1     0     0     0     0     0]
        [-5378     0     0     0     0     1     0     0     0     0]
        [ 4769     0     0     0     0     0     1     0     0     0]
        [-1159     0     0     0     0     0     0     1     0     0]
        [ 3082     0     0     0     0     0     0     0     1     0]
        [-4580     0     0     0     0     0     0     0     0     1]

    Ideal bases with quotient `x^n-1`, `m=2*n` are NTRU bases::

        sage: sage.crypto.gen_lattice(type='ideal', seed=42, quotient=x^4 - 1)          # needs sage.symbolic
        [11  0  0  0  0  0  0  0]
        [ 0 11  0  0  0  0  0  0]
        [ 0  0 11  0  0  0  0  0]
        [ 0  0  0 11  0  0  0  0]
        [-3 -3 -2  4  1  0  0  0]
        [ 4 -3 -3 -2  0  1  0  0]
        [-2  4 -3 -3  0  0  1  0]
        [-3 -2  4 -3  0  0  0  1]

    Ideal bases also work with polynomials::

        sage: R.<t> = PolynomialRing(ZZ)
        sage: sage.crypto.gen_lattice(type='ideal', seed=1234, quotient=t^4 - 1)        # needs sage.libs.pari
        [11  0  0  0  0  0  0  0]
        [ 0 11  0  0  0  0  0  0]
        [ 0  0 11  0  0  0  0  0]
        [ 0  0  0 11  0  0  0  0]
        [-3  4  1  4  1  0  0  0]
        [ 4 -3  4  1  0  1  0  0]
        [ 1  4 -3  4  0  0  1  0]
        [ 4  1  4 -3  0  0  0  1]

    Cyclotomic bases with n=2^k are SWIFFT bases::

        sage: sage.crypto.gen_lattice(type='cyclotomic', seed=42)                       # needs sage.libs.pari
        [11  0  0  0  0  0  0  0]
        [ 0 11  0  0  0  0  0  0]
        [ 0  0 11  0  0  0  0  0]
        [ 0  0  0 11  0  0  0  0]
        [-3 -3 -2  4  1  0  0  0]
        [-4 -3 -3 -2  0  1  0  0]
        [ 2 -4 -3 -3  0  0  1  0]
        [ 3  2 -4 -3  0  0  0  1]

    Dual modular bases are related to Regev's famous public-key
    encryption [Reg2005]_::

        sage: sage.crypto.gen_lattice(type='modular', m=10, seed=42, dual=True)
        [ 0  0  0  0  0  0  0  0  0 11]
        [ 0  0  0  0  0  0  0  0 11  0]
        [ 0  0  0  0  0  0  0 11  0  0]
        [ 0  0  0  0  0  0 11  0  0  0]
        [ 0  0  0  0  0 11  0  0  0  0]
        [ 0  0  0  0 11  0  0  0  0  0]
        [ 0  0  0  1 -5 -2 -1  1 -3  5]
        [ 0  0  1  0 -3  4  1  4 -3 -2]
        [ 0  1  0  0 -4  5 -3  3  5  3]
        [ 1  0  0  0 -2 -1  4  2  5  4]

    Relation of primal and dual bases::

        sage: B_primal = sage.crypto.gen_lattice(m=10, q=11, seed=42)
        sage: B_dual = sage.crypto.gen_lattice(m=10, q=11, seed=42, dual=True)
        sage: B_dual_alt = transpose(11*B_primal.inverse()).change_ring(ZZ)
        sage: B_dual_alt.hermite_form() == B_dual.hermite_form()
        True

    TESTS:

    Test some bad quotient polynomials::

        sage: sage.crypto.gen_lattice(type='ideal', seed=1234, quotient=cos(x))         # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: self must be a numeric expression
        sage: sage.crypto.gen_lattice(type='ideal', seed=1234, quotient=x^23-1)         # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: ideal basis requires n = quotient.degree()
        sage: R.<u,v> = ZZ[]
        sage: sage.crypto.gen_lattice(type='ideal', seed=1234, quotient=u+v)
        Traceback (most recent call last):
        ...
        TypeError: quotient should be a univariate polynomial

    We are testing output format choices::

        sage: sage.crypto.gen_lattice(m=10, q=11, seed=42)
        [11  0  0  0  0  0  0  0  0  0]
        [ 0 11  0  0  0  0  0  0  0  0]
        [ 0  0 11  0  0  0  0  0  0  0]
        [ 0  0  0 11  0  0  0  0  0  0]
        [ 2  4  3  5  1  0  0  0  0  0]
        [ 1 -5 -4  2  0  1  0  0  0  0]
        [-4  3 -1  1  0  0  1  0  0  0]
        [-2 -3 -4 -1  0  0  0  1  0  0]
        [-5 -5  3  3  0  0  0  0  1  0]
        [-4 -3  2 -5  0  0  0  0  0  1]

        sage: sage.crypto.gen_lattice(m=10, q=11, seed=42, ntl=True)
        [
        [11 0 0 0 0 0 0 0 0 0]
        [0 11 0 0 0 0 0 0 0 0]
        [0 0 11 0 0 0 0 0 0 0]
        [0 0 0 11 0 0 0 0 0 0]
        [2 4 3 5 1 0 0 0 0 0]
        [1 -5 -4 2 0 1 0 0 0 0]
        [-4 3 -1 1 0 0 1 0 0 0]
        [-2 -3 -4 -1 0 0 0 1 0 0]
        [-5 -5 3 3 0 0 0 0 1 0]
        [-4 -3 2 -5 0 0 0 0 0 1]
        ]

        sage: sage.crypto.gen_lattice(m=10, q=11, seed=42, lattice=True)                # needs fpylll
        Free module of degree 10 and rank 10 over Integer Ring
        User basis matrix:
        [ 0  0  1  1  0 -1 -1 -1  1  0]
        [-1  1  0  1  0  1  1  0  1  1]
        [-1  0  0  0 -1  1  1 -2  0  0]
        [-1 -1  0  1  1  0  0  1  1 -1]
        [ 1  0 -1  0  0  0 -2 -2  0  0]
        [ 2 -1  0  0  1  0  1  0  0 -1]
        [-1  1 -1  0  1 -1  1  0 -1 -2]
        [ 0  0 -1  3  0  0  0 -1 -1 -1]
        [ 0 -1  0 -1  2  0 -1  0  0  2]
        [ 0  1  1  0  1  1 -2  1 -1 -2]
    """
