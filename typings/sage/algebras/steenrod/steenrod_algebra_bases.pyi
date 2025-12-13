from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_function as cached_function

@cached_function
def convert_to_milnor_matrix(n, basis, p: int = 2, generic: str = 'auto'):
    """
    Change-of-basis matrix, 'basis' to Milnor, in dimension
    `n`, at the prime `p`.

    INPUT:

    - ``n`` -- nonnegative integer, the dimension
    - ``basis`` -- string, the basis from which to convert
    - ``p`` -- positive prime number (default: 2)

    OUTPUT:

    ``matrix`` -- change-of-basis matrix, a square matrix over `\\GF{p}`

    EXAMPLES::

        sage: # needs sage.modules
        sage: from sage.algebras.steenrod.steenrod_algebra_bases import convert_to_milnor_matrix
        sage: convert_to_milnor_matrix(5, 'adem')  # indirect doctest
        [0 1]
        [1 1]
        sage: convert_to_milnor_matrix(45, 'milnor')
        111 x 111 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)
        sage: convert_to_milnor_matrix(12, 'wall')
        [1 0 0 1 0 0 0]
        [1 1 0 0 0 1 0]
        [0 1 0 1 0 0 0]
        [0 0 0 1 0 0 0]
        [1 1 0 0 1 0 0]
        [0 0 1 1 1 0 1]
        [0 0 0 0 1 0 1]

    The function takes an optional argument, the prime `p` over
    which to work::

        sage: # needs sage.modules
        sage: convert_to_milnor_matrix(17, 'adem', 3)
        [0 0 1 1]
        [0 0 0 1]
        [1 1 1 1]
        [0 1 0 1]
        sage: convert_to_milnor_matrix(48, 'adem', 5)
        [0 1]
        [1 1]
        sage: convert_to_milnor_matrix(36, 'adem', 3)
        [0 0 1]
        [0 1 0]
        [1 2 0]
    """
def convert_from_milnor_matrix(n, basis, p: int = 2, generic: str = 'auto'):
    """
    Change-of-basis matrix, Milnor to ``basis``, in dimension `n`.

    INPUT:

    - ``n`` -- nonnegative integer, the dimension

    - ``basis`` -- string, the basis to which to convert

    - ``p`` -- positive prime number (default: 2)

    OUTPUT:

    ``matrix`` -- change-of-basis matrix, a square matrix over `\\GF{p}`

    .. NOTE::

        This is called internally.  It is not intended for casual
        users, so no error checking is made on the integer `n`, the
        basis name, or the prime.

    EXAMPLES::

        sage: # needs sage.modules
        sage: from sage.algebras.steenrod.steenrod_algebra_bases import convert_from_milnor_matrix, convert_to_milnor_matrix
        sage: convert_from_milnor_matrix(12, 'wall')
        [1 0 0 1 0 0 0]
        [0 0 1 1 0 0 0]
        [0 0 0 1 0 1 1]
        [0 0 0 1 0 0 0]
        [1 0 1 0 1 0 0]
        [1 1 1 0 0 0 0]
        [1 0 1 0 1 0 1]
        sage: convert_from_milnor_matrix(38, 'serre_cartan')
        72 x 72 dense matrix over Finite Field of size 2 (use the '.str()' method to see the entries)
        sage: x = convert_to_milnor_matrix(20, 'wood_y')
        sage: y = convert_from_milnor_matrix(20, 'wood_y')
        sage: x*y
        [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        [0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0]
        [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0]
        [0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
        [0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]
        [0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0]
        [0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
        [0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0]
        [0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
        [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
        [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]

    The function takes an optional argument, the prime `p` over
    which to work::

        sage: convert_from_milnor_matrix(17, 'adem', 3)                                 # needs sage.modules
        [2 1 1 2]
        [0 2 0 1]
        [1 2 0 0]
        [0 1 0 0]
    """
@cached_function
def steenrod_algebra_basis(n, basis: str = 'milnor', p: int = 2, **kwds):
    """
    Basis for the Steenrod algebra in degree `n`.

    INPUT:

    - ``n`` -- nonnegative integer
    - ``basis`` -- string, which basis to use (default: ``'milnor'``)
    - ``p`` -- positive prime number (default: 2)
    - ``profile`` -- profile function (default: ``None``); this
      is just passed on to the functions :func:`milnor_basis` and
      :func:`pst_basis`
    - ``truncation_type`` -- truncation type, either 0 or ``Infinity``
      (default: ``Infinity`` if no profile function is specified,
      0 otherwise).  This is just passed on to the function
      :func:`milnor_basis`.
    - ``generic`` -- boolean (default: ``None``)

    OUTPUT:

    Tuple of objects representing basis elements for the Steenrod algebra
    in dimension n.

    The choices for the string ``basis`` are as follows; see the
    documentation for :mod:`sage.algebras.steenrod.steenrod_algebra`
    for details on each basis:

    - ``'milnor'`` -- Milnor basis
    - ``'serre-cartan'`` or ``'adem'`` or ``'admissible'`` -- Serre-Cartan basis
    - ``'pst'``, ``'pst_rlex'``, ``'pst_llex'``, ``'pst_deg'``, ``'pst_revz'`` --
      various `P^s_t`-bases
    - ``'comm'``, ``'comm_rlex'``, ``'comm_llex'``, ``'comm_deg'``, ``'comm_revz'``, or
      any of these with ``'_long'`` appended -- various commutator bases

    The rest of these bases are only defined when `p=2`.

    - ``'wood_y'`` -- Wood's Y basis
    - ``'wood_z'`` -- Wood's Z basis
    - ``'wall'`` or ``'wall_long'`` -- Wall's basis
    - ``'arnon_a'`` or ``'arnon_a_long'`` -- Arnon's A basis
    - ``'arnon_c'`` -- Arnon's C basis

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import steenrod_algebra_basis
        sage: steenrod_algebra_basis(7, 'milnor') # indirect doctest
        ((0, 0, 1), (1, 2), (4, 1), (7,))
        sage: steenrod_algebra_basis(5)   # milnor basis is the default
        ((2, 1), (5,))

    Bases in negative dimensions are empty::

        sage: steenrod_algebra_basis(-2, 'wall')
        ()

    The third (optional) argument to 'steenrod_algebra_basis' is the
    prime p::

        sage: steenrod_algebra_basis(9, 'milnor', p=3)
        (((1,), (1,)), ((0,), (2,)))
        sage: steenrod_algebra_basis(9, 'milnor', 3)
        (((1,), (1,)), ((0,), (2,)))
        sage: steenrod_algebra_basis(17, 'milnor', 3)
        (((2,), ()), ((1,), (3,)), ((0,), (0, 1)), ((0,), (4,)))

    Other bases::

        sage: steenrod_algebra_basis(7, 'admissible')
        ((7,), (6, 1), (4, 2, 1), (5, 2))
        sage: steenrod_algebra_basis(13, 'admissible', p=3)
        ((1, 3, 0), (0, 3, 1))
        sage: steenrod_algebra_basis(5, 'wall')
        (((2, 2), (0, 0)), ((1, 1), (1, 0)))
        sage: steenrod_algebra_basis(5, 'wall_long')
        (((2, 2), (0, 0)), ((1, 1), (1, 0)))
        sage: steenrod_algebra_basis(5, 'pst-rlex')
        (((0, 1), (2, 1)), ((1, 1), (0, 2)))
    """
def restricted_partitions(n, l, no_repeats: bool = False) -> Generator[Incomplete]:
    """
    Iterator over 'restricted' partitions of `n`: partitions with parts taken
    from list `l`.

    INPUT:

    - ``n`` -- nonnegative integer
    - ``l`` -- list of positive integers
    - ``no_repeats`` -- boolean (default: ``False``); if ``True``,
      only return partitions with no repeated parts

    OUTPUT: iterator of lists

    One could also use ``Partitions(n, parts_in=l)``, but this
    function may be faster.  Also, while ``Partitions(n, parts_in=l,
    max_slope=-1)`` should in theory return the partitions of `n` with
    parts in ``l`` with no repetitions, the ``max_slope=-1`` argument
    is ignored, so it does not work.  (At the moment, the
    ``no_repeats=True`` case is the only one used in the code.)

    .. TODO::

        This should be re-implemented in a non-recursive way.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import restricted_partitions
        sage: list(restricted_partitions(10, [7,5,1]))
        [[7, 1, 1, 1], [5, 5], [5, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        sage: list(restricted_partitions(10, [6,5,4,3,2,1], no_repeats=True))
        [[6, 4], [6, 3, 1], [5, 4, 1], [5, 3, 2], [4, 3, 2, 1]]
        sage: list(restricted_partitions(10, [6,4,2]))
        [[6, 4], [6, 2, 2], [4, 4, 2], [4, 2, 2, 2], [2, 2, 2, 2, 2]]
        sage: list(restricted_partitions(10, [6,4,2], no_repeats=True))
        [[6, 4]]

    ``l`` may have repeated elements. If ``no_repeats`` is ``False``, this
    has no effect. If ``no_repeats`` is ``True``, and if the repeated
    elements appear consecutively in ``l``, then each element may be
    used only as many times as it appears in ``l``::

        sage: list(restricted_partitions(10, [6,4,2,2], no_repeats=True))
        [[6, 4], [6, 2, 2]]
        sage: list(restricted_partitions(10, [6,4,2,2,2], no_repeats=True))
        [[6, 4], [6, 2, 2], [4, 2, 2, 2]]

    (If the repeated elements don't appear consecutively, the results
    are likely meaningless, containing several partitions more than
    once, for example.)

    In the following examples, ``no_repeats`` is ``False``::

        sage: list(restricted_partitions(10, [6,4,2]))
        [[6, 4], [6, 2, 2], [4, 4, 2], [4, 2, 2, 2], [2, 2, 2, 2, 2]]
        sage: list(restricted_partitions(10, [6,4,2,2,2]))
        [[6, 4], [6, 2, 2], [4, 4, 2], [4, 2, 2, 2], [2, 2, 2, 2, 2]]
        sage: list(restricted_partitions(10, [6,4,4,4,2,2,2,2,2,2]))
        [[6, 4], [6, 2, 2], [4, 4, 2], [4, 2, 2, 2], [2, 2, 2, 2, 2]]
    """
def xi_degrees(n, p: int = 2, reverse: bool = True):
    """
    Decreasing list of degrees of the `\\xi_i`'s, starting in degree `n`.

    INPUT:

    - ``n`` -- integer
    - ``p`` -- prime number (default: 2)
    - ``reverse`` -- boolean (default: ``True``)

    OUTPUT: list of integers

    When `p=2`: decreasing list of the degrees of the `\\xi_i`'s with
    degree at most `n`.

    At odd primes: decreasing list of these degrees, each divided by
    `2(p-1)`.

    If ``reverse`` is ``False``, then return an increasing list rather
    than a decreasing one.

    EXAMPLES::

        sage: sage.algebras.steenrod.steenrod_algebra_bases.xi_degrees(17)
        [15, 7, 3, 1]
        sage: sage.algebras.steenrod.steenrod_algebra_bases.xi_degrees(17, reverse=False)
        [1, 3, 7, 15]
        sage: sage.algebras.steenrod.steenrod_algebra_bases.xi_degrees(17, p=3)
        [13, 4, 1]
        sage: sage.algebras.steenrod.steenrod_algebra_bases.xi_degrees(400, p=17)
        [307, 18, 1]
    """
def milnor_basis(n, p: int = 2, **kwds):
    """
    Milnor basis in dimension `n` with profile function ``profile``.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``p`` -- positive prime number (default: 2)

    - ``profile`` -- profile function (default: ``None``).
      Together with ``truncation_type``, specify the profile function
      to be used; ``None`` means the profile function for the entire
      Steenrod algebra.  See
      :mod:`sage.algebras.steenrod.steenrod_algebra` and
      :func:`SteenrodAlgebra <sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra>`
      for information on profile functions.

    - ``truncation_type`` -- truncation type, either 0 or ``Infinity``
      (default: ``Infinity`` if no profile function is specified,
      0 otherwise)

    OUTPUT: tuple of mod `p` Milnor basis elements in dimension `n`

    At the prime 2, the Milnor basis consists of symbols of the form
    `\\text{Sq}(m_1, m_2, ..., m_t)`, where each
    `m_i` is a nonnegative integer and if `t>1`, then
    `m_t \\neq 0`. At odd primes, it consists of symbols of the
    form `Q_{e_1} Q_{e_2} ... P(m_1, m_2, ..., m_t)`,
    where `0 \\leq e_1 < e_2 < ...`, each `m_i` is a
    nonnegative integer, and if `t>1`, then
    `m_t \\neq 0`.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import milnor_basis
        sage: milnor_basis(7)
        ((0, 0, 1), (1, 2), (4, 1), (7,))
        sage: milnor_basis(7, 2)
        ((0, 0, 1), (1, 2), (4, 1), (7,))
        sage: milnor_basis(4, 2)
        ((1, 1), (4,))
        sage: milnor_basis(4, 2, profile=[2,1])
        ((1, 1),)
        sage: milnor_basis(4, 2, profile=(), truncation_type=0)
        ()
        sage: milnor_basis(4, 2, profile=(), truncation_type=Infinity)
        ((1, 1), (4,))
        sage: milnor_basis(9, 3)
        (((1,), (1,)), ((0,), (2,)))
        sage: milnor_basis(17, 3)
        (((2,), ()), ((1,), (3,)), ((0,), (0, 1)), ((0,), (4,)))
        sage: milnor_basis(48, p=5)
        (((), (0, 1)), ((), (6,)))
        sage: len(milnor_basis(100,3))
        13
        sage: len(milnor_basis(200,7))
        0
        sage: len(milnor_basis(240,7))
        3
        sage: len(milnor_basis(240,7, profile=((),()), truncation_type=Infinity))
        3
        sage: len(milnor_basis(240,7, profile=((),()), truncation_type=0))
        0
    """
def serre_cartan_basis(n, p: int = 2, bound: int = 1, **kwds):
    """
    Serre-Cartan basis in dimension `n`.

    INPUT:

    - ``n`` -- nonnegative integer
    - ``bound`` -- positive integer (optional)
    - ``prime`` -- positive prime number (default: 2)

    OUTPUT: tuple of mod `p` Serre-Cartan basis elements in dimension `n`

    The Serre-Cartan basis consists of 'admissible monomials in the
    Steenrod squares'. Thus at the prime 2, it consists of monomials
    `\\text{Sq}^{m_1} \\text{Sq}^{m_2} ... \\text{Sq}^{m_t}` with `m_i
    \\geq 2m_{i+1}` for each `i`. At odd primes, it consists of
    monomials `\\beta^{e_0} P^{s_1} \\beta^{e_1} P^{s_2} ...  P^{s_k}
    \\beta^{e_k}` with each `e_i` either 0 or 1, `s_i \\geq p s_{i+1} +
    e_i` for all `i`, and `s_k \\geq 1`.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import serre_cartan_basis
        sage: serre_cartan_basis(7)
        ((7,), (6, 1), (4, 2, 1), (5, 2))
        sage: serre_cartan_basis(13,3)
        ((1, 3, 0), (0, 3, 1))
        sage: serre_cartan_basis(50,5)
        ((1, 5, 0, 1, 1), (1, 6, 1))

    If optional argument ``bound`` is present, include only those monomials
    whose last term is at least ``bound`` (when `p=2`), or those for which
    `s_k - e_k \\geq bound` (when `p` is odd). ::

        sage: serre_cartan_basis(7, bound=2)
        ((7,), (5, 2))
        sage: serre_cartan_basis(13, 3, bound=3)
        ((1, 3, 0),)
    """
def atomic_basis(n, basis, **kwds):
    """
    Basis for dimension `n` made of elements in 'atomic' degrees:
    degrees of the form `2^i (2^j - 1)`.

    This works at the prime 2 only.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``basis`` -- string, the name of the basis

    - ``profile`` -- profile function (default: ``None``).
      Together with ``truncation_type``, specify the profile function
      to be used; ``None`` means the profile function for the entire
      Steenrod algebra.  See
      :mod:`sage.algebras.steenrod.steenrod_algebra` and
      :func:`SteenrodAlgebra` for information on profile functions.

    - ``truncation_type`` -- truncation type, either 0 or ``Infinity``
      (default: ``Infinity`` if no profile function is specified,
      0 otherwise).

    OUTPUT: tuple of basis elements in dimension `n`

    The atomic bases include Wood's Y and Z bases, Wall's basis,
    Arnon's A basis, the `P^s_t`-bases, and the commutator
    bases. (All of these bases are constructed similarly, hence their
    constructions have been consolidated into a single function. Also,
    see the documentation for :func:`steenrod_algebra_basis` for
    descriptions of them.)  For `P^s_t`-bases, you may also specify a
    profile function and truncation type; profile functions are ignored
    for the other bases.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import atomic_basis
        sage: atomic_basis(6,'woody')
        (((1, 0), (0, 1), (0, 0)), ((2, 0), (1, 0)), ((1, 1),))
        sage: atomic_basis(8,'woodz')
        (((2, 0), (0, 1), (0, 0)), ((0, 2), (0, 0)), ((1, 1), (1, 0)), ((3, 0),))
        sage: atomic_basis(6,'woodz') == atomic_basis(6, 'woody')
        True
        sage: atomic_basis(9,'woodz') == atomic_basis(9, 'woody')
        False

    Wall's basis::

        sage: atomic_basis(8,'wall')
        (((2, 2), (1, 0), (0, 0)), ((2, 0), (0, 0)), ((2, 1), (1, 1)), ((3, 3),))

    Arnon's A basis::

        sage: atomic_basis(7,'arnona')
        (((0, 0), (1, 1), (2, 2)), ((0, 0), (2, 1)), ((1, 0), (2, 2)), ((2, 0),))

    `P^s_t`-bases::

        sage: atomic_basis(7,'pst_rlex')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((2, 1), (0, 2)), ((0, 3),))
        sage: atomic_basis(7,'pst_llex')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))
        sage: atomic_basis(7,'pst_deg')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))
        sage: atomic_basis(7,'pst_revz')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))

    Commutator bases::

        sage: atomic_basis(7,'comm_rlex')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((2, 1), (0, 2)), ((0, 3),))
        sage: atomic_basis(7,'comm_llex')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))
        sage: atomic_basis(7,'comm_deg')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))
        sage: atomic_basis(7,'comm_revz')
        (((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 2)), ((0, 2), (2, 1)), ((0, 3),))
    """
@cached_function
def arnonC_basis(n, bound: int = 1):
    """
    Arnon's C basis in dimension `n`.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``bound`` -- positive integer (optional)

    OUTPUT: tuple of basis elements in dimension `n`

    The elements of Arnon's C basis are monomials of the form
    `\\text{Sq}^{t_1} ... \\text{Sq}^{t_m}` where for each
    `i`, we have `t_i \\leq 2t_{i+1}` and
    `2^i | t_{m-i}`.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import arnonC_basis
        sage: arnonC_basis(7)
        ((7,), (2, 5), (4, 3), (4, 2, 1))

    If optional argument ``bound`` is present, include only those monomials
    whose first term is at least as large as ``bound``::

        sage: arnonC_basis(7,3)
        ((7,), (4, 3), (4, 2, 1))
    """
def atomic_basis_odd(n, basis, p, **kwds):
    """
    `P^s_t`-bases and commutator basis in dimension `n` at odd primes.

    This function is called ``atomic_basis_odd`` in analogy with
    :func:`atomic_basis`.

    INPUT:

    - ``n`` -- nonnegative integer

    - ``basis`` -- string, the name of the basis

    - ``p`` -- positive prime number

    - ``profile`` -- profile function (default: ``None``).
      Together with ``truncation_type``, specify the profile function
      to be used; ``None`` means the profile function for the entire
      Steenrod algebra.  See
      :mod:`sage.algebras.steenrod.steenrod_algebra` and
      :func:`SteenrodAlgebra` for information on profile functions.

    - ``truncation_type`` -- truncation type, either 0 or ``Infinity``
      (default: ``Infinity`` if no profile function is specified,
      0 otherwise).

    OUTPUT: tuple of basis elements in dimension `n`

    The only possible difference in the implementations for `P^s_t`
    bases and commutator bases is that the former make sense, and
    require filtering, if there is a nontrivial profile function.
    This function is called by :func:`steenrod_algebra_basis`, and it
    will not be called for commutator bases if there is a profile
    function, so we treat the two bases exactly the same.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_bases import atomic_basis_odd
        sage: atomic_basis_odd(8, 'pst_rlex', 3)
        (((), (((0, 1), 2),)),)

        sage: atomic_basis_odd(18, 'pst_rlex', 3)
        (((0, 2), ()), ((0, 1), (((1, 1), 1),)))
        sage: atomic_basis_odd(18, 'pst_rlex', 3, profile=((), (2,2,2)))
        (((0, 2), ()),)
    """
def steenrod_basis_error_check(dim, p, **kwds) -> None:
    """
    This performs crude error checking.

    INPUT:

    - ``dim`` -- nonnegative integer
    - ``p`` -- positive prime number

    OUTPUT: none

    This checks to see if the different bases have the same length, and
    if the change-of-basis matrices are invertible. If something goes
    wrong, an error message is printed.

    This function checks at the prime `p` as the dimension goes up
    from 0 to ``dim``.

    If you set the Sage verbosity level to a positive integer (using
    ``set_verbose(n)``), then some extra messages will be printed.

    EXAMPLES::

        sage: # long time
        sage: from sage.algebras.steenrod.steenrod_algebra_bases import steenrod_basis_error_check
        sage: steenrod_basis_error_check(15, 2)
        sage: steenrod_basis_error_check(15, 2, generic=True)
        sage: steenrod_basis_error_check(40, 3)
        sage: steenrod_basis_error_check(80, 5)
    """
