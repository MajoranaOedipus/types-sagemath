r"""
Helper functions for congruence subgroups

This file contains optimized Cython implementations of a few functions related
to the standard congruence subgroups `\Gamma_0, \Gamma_1, \Gamma_H`.  These
functions are for internal use by routines elsewhere in the Sage library.
"""
import sage as sage
from sage.categories.category import ZZ as ZZ
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_constructor as Gamma0
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_constructor as Gamma1
from sage.modular.modsym.p1list import lift_to_sl2z as lift_to_sl2z
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

Mat2Z: MatrixSpace = MatrixSpace(ZZ, 2) # TODO: with category
def degeneracy_coset_representatives_gamma0(N: int, M: int, t: int) -> list[list[int]]:
    r"""
    Let `N` be a positive integer and `M` a divisor of `N`.  Let `t` be a
    divisor of `N/M`, and let `T` be the `2 \times 2` matrix `(1, 0; 0, t)`.
    This function returns representatives for the orbit set `\Gamma_0(N)
    \backslash T \Gamma_0(M)`, where `\Gamma_0(N)` acts on the left on `T
    \Gamma_0(M)`.

    INPUT:

    - ``N`` -- integer
    - ``M`` -- integer (divisor of `N`)
    - ``t`` -- integer (divisor of `N/M`)

    OUTPUT:

    list -- list of lists ``[a,b,c,d]``, where ``[a,b,c,d]`` should be viewed
    as a 2x2 matrix.

    This function is used for computation of degeneracy maps between
    spaces of modular symbols, hence its name.

    We use that `T^{-1} \cdot (a,b;c,d) \cdot T = (a,bt; c/t,d)`, that the
    group `T^{-1} \Gamma_0(N) T` is contained in `\Gamma_0(M)`, and that
    `\Gamma_0(N) T` is contained in `T \Gamma_0(M)`.

    ALGORITHM:

    1. Compute representatives for `\Gamma_0(N/t,t)` inside of `\Gamma_0(M)`:

      + COSET EQUIVALENCE: Two right cosets represented by `[a,b;c,d]` and
        `[a',b';c',d']` of `\Gamma_0(N/t,t)` in `\SL_2(\ZZ)` are equivalent if
        and only if `(a,b)=(a',b')` as points of `\mathbf{P}^1(\ZZ/t\ZZ)`,
        i.e., `ab' \cong ba' \pmod{t}`, and `(c,d) = (c',d')` as points of
        `\mathbf{P}^1(\ZZ/(N/t)\ZZ)`.

      + ALGORITHM to list all cosets:

        a) Compute the number of cosets.
        b) Compute a random element `x` of `\Gamma_0(M)`.
        c) Check if x is equivalent to anything generated so far; if not, add x
           to the list.
        d) Continue until the list is as long as the bound
           computed in step (a).

    2. There is a bijection between `\Gamma_0(N)\backslash T \Gamma_0(M)` and
       `\Gamma_0(N/t,t) \backslash \Gamma_0(M)` given by `T r \leftrightarrow
       r`. Consequently we obtain coset representatives for
       `\Gamma_0(N)\backslash T \Gamma_0(M)` by left multiplying by `T` each
       coset representative of `\Gamma_0(N/t,t) \backslash \Gamma_0(M)` found
       in step 1.

    EXAMPLES::

        sage: from sage.modular.arithgroup.all import degeneracy_coset_representatives_gamma0
        sage: len(degeneracy_coset_representatives_gamma0(13, 1, 1))
        14
        sage: len(degeneracy_coset_representatives_gamma0(13, 13, 1))
        1
        sage: len(degeneracy_coset_representatives_gamma0(13, 1, 13))
        14
    """
def degeneracy_coset_representatives_gamma1(N: int, M: int, t: int) -> list[list[int]]:
    r"""
    Let `N` be a positive integer and `M` a divisor of `N`.  Let `t` be a
    divisor of `N/M`, and let `T` be the `2 \times 2` matrix `(1,0; 0,t)`.
    This function returns representatives for the orbit set `\Gamma_1(N)
    \backslash T \Gamma_1(M)`, where `\Gamma_1(N)` acts on the left on `T
    \Gamma_1(M)`.

    INPUT:

    - ``N`` -- integer
    - ``M`` -- integer (divisor of `N`)
    - ``t`` -- integer (divisor of `N/M`)

    OUTPUT:

    list -- list of lists ``[a,b,c,d]``, where ``[a,b,c,d]`` should be viewed
    as a 2x2 matrix.

    This function is used for computation of degeneracy maps between
    spaces of modular symbols, hence its name.

    ALGORITHM:

    Everything is the same as for
    :func:`~degeneracy_coset_representatives_gamma0`, except for coset
    equivalence.   Here `\Gamma_1(N/t,t)` consists of matrices that are of the
    form `(1,*; 0,1) \bmod N/t` and `(1,0; *,1) \bmod t`.

    COSET EQUIVALENCE: Two right cosets represented by `[a,b;c,d]` and
    `[a',b';c',d']` of `\Gamma_1(N/t,t)` in `\SL_2(\ZZ)` are equivalent if
    and only if

    .. MATH::

        a \cong a' \pmod{t},
        b \cong b' \pmod{t},
        c \cong c' \pmod{N/t},
        d \cong d' \pmod{N/t}.

    EXAMPLES::

        sage: from sage.modular.arithgroup.all import degeneracy_coset_representatives_gamma1
        sage: len(degeneracy_coset_representatives_gamma1(13, 1, 1))
        168
        sage: len(degeneracy_coset_representatives_gamma1(13, 13, 1))
        1
        sage: len(degeneracy_coset_representatives_gamma1(13, 1, 13))
        168
    """
def generators_helper(coset_reps, level):
    r"""
    Helper function for generators of Gamma0, Gamma1 and GammaH.

    These are computed using coset representatives, via an "inverse
    Todd-Coxeter" algorithm, and generators for `\SL_2(\ZZ)`.

    ALGORITHM: Given coset representatives for a finite index subgroup `G` of
    `\SL_2(\ZZ)` we compute generators for `G` as follows.  Let `R` be a set of
    coset representatives for `G`.  Let `S, T \in \SL_2(\ZZ)` be defined by
    `(0,-1; 1,0)` and `(1,1,0,1)`, respectively.
    Define maps `s, t: R \to G` as follows. If `r \in R`, then there exists a
    unique `r' \in R` such that `GrS = Gr'`. Let `s(r) = rSr'^{-1}`. Likewise,
    there is a unique `r'` such that `GrT = Gr'` and we let `t(r) = rTr'^{-1}`.
    Note that `s(r)` and `t(r)` are in `G` for all `r`.  Then `G` is generated
    by `s(R)\cup t(R)`.

    There are more sophisticated algorithms using group actions on trees (and
    Farey symbols) that give smaller generating sets -- this code is now
    deprecated in favour of the newer implementation based on Farey symbols.

    EXAMPLES::

        sage: Gamma0(7).generators(algorithm='todd-coxeter') # indirect doctest
        [
        [1 1]  [-1  0]  [ 1 -1]  [1 0]  [1 1]  [-3 -1]  [-2 -1]  [-5 -1]
        [0 1], [ 0 -1], [ 0  1], [7 1], [0 1], [ 7  2], [ 7  3], [21  4],
        <BLANKLINE>
        [-4 -1]  [-1  0]  [ 1  0]
        [21  5], [ 7 -1], [-7  1]
        ]
    """
