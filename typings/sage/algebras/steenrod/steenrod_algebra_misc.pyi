def get_basis_name(basis, p, generic=None):
    """
    Return canonical basis named by string basis at the prime p.

    INPUT:

    - ``basis`` -- string

    - ``p`` -- positive prime number

    - ``generic`` -- boolean (default: 'None')

    OUTPUT: ``basis_name`` -- string

    Specify the names of the implemented bases.  The input is
    converted to lower-case, then processed to return the canonical
    name for the basis.

    For the Milnor and Serre-Cartan bases, use the list of synonyms
    defined by the variables :data:`_steenrod_milnor_basis_names` and
    :data:`_steenrod_serre_cartan_basis_names`.  Their canonical names
    are 'milnor' and 'serre-cartan', respectively.

    For the other bases, use pattern-matching rather than a list of
    synonyms:

    - Search for 'wood' and 'y' or 'wood' and 'z' to get the Wood
      bases.  Canonical names 'woody', 'woodz'.

    - Search for 'arnon' and 'c' for the Arnon C basis.  Canonical
      name: 'arnonc'.

    - Search for 'arnon' (and no 'c') for the Arnon A basis.  Also see
      if 'long' is present, for the long form of the basis.  Canonical
      names: 'arnona', 'arnona_long'.

    - Search for 'wall' for the Wall basis. Also see if 'long' is
      present.  Canonical names: 'wall', 'wall_long'.

    - Search for 'pst' for P^s_t bases, then search for the order
      type: 'rlex', 'llex', 'deg', 'revz'.  Canonical names:
      'pst_rlex', 'pst_llex', 'pst_deg', 'pst_revz'.

    - For commutator types, search for 'comm', an order type, and also
      check to see if 'long' is present.  Canonical names:
      'comm_rlex', 'comm_llex', 'comm_deg', 'comm_revz',
      'comm_rlex_long', 'comm_llex_long', 'comm_deg_long',
      'comm_revz_long'.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import get_basis_name
        sage: get_basis_name('adem', 2)
        'serre-cartan'
        sage: get_basis_name('milnor', 2)
        'milnor'
        sage: get_basis_name('MiLNoR', 5)
        'milnor'
        sage: get_basis_name('pst-llex', 2)
        'pst_llex'
        sage: get_basis_name('wood_abcdedfg_y', 2)
        'woody'
        sage: get_basis_name('wood', 2)
        Traceback (most recent call last):
        ...
        ValueError: wood is not a recognized basis at the prime 2
        sage: get_basis_name('arnon--hello--long', 2)
        'arnona_long'
        sage: get_basis_name('arnona_long', p=5)
        Traceback (most recent call last):
        ...
        ValueError: arnona_long is not a recognized basis at the prime 5
        sage: get_basis_name('NOT_A_BASIS', 2)
        Traceback (most recent call last):
        ...
        ValueError: not_a_basis is not a recognized basis at the prime 2
        sage: get_basis_name('woody', 2, generic=True)
        Traceback (most recent call last):
        ...
        ValueError: woody is not a recognized basis for the generic Steenrod algebra at the prime 2
    """
def is_valid_profile(profile, truncation_type, p: int = 2, generic=None):
    """
    Return ``True`` if ``profile``, together with ``truncation_type``, is a valid
    profile at the prime `p`.

    INPUT:

    - ``profile`` -- when `p=2`, a tuple or list of numbers; when `p`
      is odd, a pair of such lists

    - ``truncation_type`` -- either 0 or `\\infty`

    - ``p`` -- prime number (default: 2)

    - ``generic`` -- boolean (default: ``None``)

    OUTPUT: ``True`` if the profile function is valid, ``False`` otherwise

    See the documentation for :mod:`sage.algebras.steenrod.steenrod_algebra`
    for descriptions of profile functions and how they correspond to
    sub-Hopf algebras of the Steenrod algebra.  Briefly: at the prime
    2, a profile function `e` is valid if it satisfies the condition

    - `e(r) \\geq \\min( e(r-i) - i, e(i))` for all `0 < i < r`.

    At odd primes, a pair of profile functions `e` and `k` are valid
    if they satisfy

    - `e(r) \\geq \\min( e(r-i) - i, e(i))` for all `0 < i < r`.

    - if `k(i+j) = 1`, then either `e(i) \\leq j` or `k(j) = 1` for all
      `i \\geq 1`, `j \\geq 0`.

    In this function, profile functions are lists or tuples, and
    ``truncation_type`` is appended as the last element of the list
    `e` before testing.

    EXAMPLES:

    `p=2`::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import is_valid_profile
        sage: is_valid_profile([3,2,1], 0)
        True
        sage: is_valid_profile([3,2,1], Infinity)
        True
        sage: is_valid_profile([1,2,3], 0)
        False
        sage: is_valid_profile([6,2,0], Infinity)
        False
        sage: is_valid_profile([0,3], 0)
        False
        sage: is_valid_profile([0,0,4], 0)
        False
        sage: is_valid_profile([0,0,0,4,0], 0)
        True

    Odd primes::

        sage: is_valid_profile(([0,0,0], [2,1,1,1,2,2]), 0, p=3)
        True
        sage: is_valid_profile(([1], [2,2]), 0, p=3)
        True
        sage: is_valid_profile(([1], [2]), 0, p=7)
        False
        sage: is_valid_profile(([1,2,1], []), 0, p=7)
        True
        sage: is_valid_profile(([0,0,0], [2,1,1,1,2,2]), 0, p=2, generic=True)
        True
    """
def normalize_profile(profile, precision=None, truncation_type: str = 'auto', p: int = 2, generic=None):
    '''
    Given a profile function and related data, return it in a standard form,
    suitable for hashing and caching as data defining a sub-Hopf
    algebra of the Steenrod algebra.

    INPUT:

    - ``profile`` -- a profile function in form specified below
    - ``precision`` -- integer or ``None`` (default: ``None``)
    - ``truncation_type`` -- 0 or `\\infty` or \'auto\' (default: \'auto\')
    - ``p`` -- prime (default: 2)
    - ``generic`` -- boolean (default: ``None``)

    OUTPUT:

    a triple ``profile, precision, truncation_type``, in
    standard form as described below.

    The "standard form" is as follows: ``profile`` should be a tuple
    of integers (or `\\infty`) with no trailing zeroes when `p=2`, or a
    pair of such when `p` is odd or `generic` is ``True``.  ``precision``
    should be a positive integer.  ``truncation_type`` should be 0 or `\\infty`.
    Furthermore, this must be a valid profile, as determined by the
    function :func:`is_valid_profile`.  See also the documentation for
    the module :mod:`sage.algebras.steenrod.steenrod_algebra` for information
    about profile functions.

    For the inputs: when `p=2`, ``profile`` should be a valid profile
    function, and it may be entered in any of the following forms:

    - a list or tuple, e.g., ``[3,2,1,1]``
    - a function from positive integers to nonnegative integers (and
      `\\infty`), e.g., ``lambda n: n+2``.  This corresponds to the
      list ``[3, 4, 5, ...]``.
    - ``None`` or ``Infinity`` -- use this for the profile function for
      the whole Steenrod algebra.  This corresponds to the list
      ``[Infinity, Infinity, Infinity, ...]``

    To make this hashable, it gets turned into a tuple.  In the first
    case it is clear how to do this; also in this case, ``precision``
    is set to be one more than the length of this tuple.  In the
    second case, construct a tuple of length one less than
    ``precision`` (default: 100).  In the last case, the empty
    tuple is returned and ``precision`` is set to 1.

    Once a sub-Hopf algebra of the Steenrod algebra has been defined
    using such a profile function, if the code requires any remaining
    terms (say, terms after the 100th), then they are given by
    ``truncation_type`` if that is 0 or `\\infty`.  If
    ``truncation_type`` is \'auto\', then in the case of a tuple, it
    gets set to 0, while for the other cases it gets set to `\\infty`.

    See the examples below.

    When `p` is odd, ``profile`` is a pair of "functions", so it may
    have the following forms:

    - a pair of lists or tuples, the second of which takes values in
      the set `\\{1,2\\}`, e.g., ``([3,2,1,1], [1,1,2,2,1])``.

    - a pair of functions, one (called `e`) from positive integers to
      nonnegative integers (and `\\infty`), one (called `k`) from
      nonnegative integers to the set `\\{1,2\\}`, e.g.,
      ``(lambda n: n+2, lambda n: 1)``.  This corresponds to the
      pair ``([3, 4, 5, ...], [1, 1, 1, ...])``.

    - ``None`` or ``Infinity`` -- use this for the profile function for
      the whole Steenrod algebra.  This corresponds to the pair
      ``([Infinity, Infinity, Infinity, ...], [2, 2, 2, ...])``.

    You can also mix and match the first two, passing a pair with
    first entry a list and second entry a function, for instance.  The
    values of ``precision`` and ``truncation_type`` are determined by
    the first entry.

    EXAMPLES:

    `p=2`::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import normalize_profile
        sage: normalize_profile([1,2,1,0,0])
        ((1, 2, 1), 0)

    The full mod 2 Steenrod algebra::

        sage: normalize_profile(Infinity)
        ((), +Infinity)
        sage: normalize_profile(None)
        ((), +Infinity)
        sage: normalize_profile(lambda n: Infinity)
        ((), +Infinity)

    The ``precision`` argument has no effect when the first argument
    is a list or tuple::

        sage: normalize_profile([1,2,1,0,0], precision=12)
        ((1, 2, 1), 0)

    If the first argument is a function, then construct a list of
    length one less than ``precision``, by plugging in the numbers 1,
    2, ..., ``precision`` - 1::

        sage: normalize_profile(lambda n: 4-n, precision=4)
        ((3, 2, 1), +Infinity)
        sage: normalize_profile(lambda n: 4-n, precision=4, truncation_type=0)
        ((3, 2, 1), 0)

    Negative numbers in profile functions are turned into zeroes::

        sage: normalize_profile(lambda n: 4-n, precision=6)
        ((3, 2, 1, 0, 0), +Infinity)

    If it doesn\'t give a valid profile, an error is raised::

        sage: normalize_profile(lambda n: 3, precision=4, truncation_type=0)
        Traceback (most recent call last):
        ...
        ValueError: invalid profile
        sage: normalize_profile(lambda n: 3, precision=4, truncation_type = Infinity)
        ((3, 3, 3), +Infinity)

    When `p` is odd, the behavior is similar::

        sage: normalize_profile(([2,1], [2,2,2]), p=13)
        (((2, 1), (2, 2, 2)), 0)

    The full mod `p` Steenrod algebra::

        sage: normalize_profile(None, p=7)
        (((), ()), +Infinity)
        sage: normalize_profile(Infinity, p=11)
        (((), ()), +Infinity)
        sage: normalize_profile((lambda n: Infinity, lambda n: 2), p=17)
        (((), ()), +Infinity)

    Note that as at the prime 2, the ``precision`` argument has no
    effect on a list or tuple in either entry of ``profile``.  If
    ``truncation_type`` is \'auto\', then it gets converted to either
    ``0`` or ``+Infinity`` depending on the *first* entry of
    ``profile``::

        sage: normalize_profile(([2,1], [2,2,2]), precision=84, p=13)
        (((2, 1), (2, 2, 2)), 0)
        sage: normalize_profile((lambda n: 0, lambda n: 2), precision=4, p=11)
        (((0, 0, 0), ()), +Infinity)
        sage: normalize_profile((lambda n: 0, (1,1,1,1,1,1,1)), precision=4, p=11)
        (((0, 0, 0), (1, 1, 1, 1, 1, 1, 1)), +Infinity)
        sage: normalize_profile(((4,3,2,1), lambda n: 2), precision=6, p=11)
        (((4, 3, 2, 1), (2, 2, 2, 2, 2)), 0)
        sage: normalize_profile(((4,3,2,1), lambda n: 1), precision=3, p=11, truncation_type=Infinity)
        (((4, 3, 2, 1), (1, 1)), +Infinity)

    As at the prime 2, negative numbers in the first component are
    converted to zeroes.  Numbers in the second component must be
    either 1 and 2, or else an error is raised::

        sage: normalize_profile((lambda n: -n, lambda n: 1), precision=4, p=11)
        (((0, 0, 0), (1, 1, 1)), +Infinity)
        sage: normalize_profile([[0,0,0], [1,2,3,2,1]], p=11)
        Traceback (most recent call last):
        ...
        ValueError: invalid profile
    '''
def milnor_mono_to_string(mono, latex: bool = False, generic: bool = False):
    """
    String representation of element of the Milnor basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- if `generic=False`, tuple of nonnegative integers (a,b,c,...);
      if `generic=True`, pair of tuples of nonnegative integers ((e0, e1, e2,
      ...), (r1, r2, ...))

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    - ``generic`` -- whether to format generically, or for the prime 2 (default)

    OUTPUT: ``rep`` -- string

    This returns a string like ``Sq(a,b,c,...)`` when `generic=False`, or a string
    like ``Q_e0 Q_e1 Q_e2 ... P(r1, r2, ...)`` when `generic=True`.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import milnor_mono_to_string
        sage: milnor_mono_to_string((1,2,3,4))
        'Sq(1,2,3,4)'
        sage: milnor_mono_to_string((1,2,3,4),latex=True)
        '\\\\text{Sq}(1,2,3,4)'
        sage: milnor_mono_to_string(((1,0), (2,3,1)), generic=True)
        'Q_{1} Q_{0} P(2,3,1)'
        sage: milnor_mono_to_string(((1,0), (2,3,1)), latex=True, generic=True)
        'Q_{1} Q_{0} \\\\mathcal{P}(2,3,1)'

    The empty tuple represents the unit element::

        sage: milnor_mono_to_string(())
        '1'
        sage: milnor_mono_to_string((), generic=True)
        '1'
    """
def serre_cartan_mono_to_string(mono, latex: bool = False, generic: bool = False):
    """
    String representation of element of the Serre-Cartan basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of positive integers (a,b,c,...)  when `generic=False`,
      or tuple (e0, n1, e1, n2, ...) when `generic=True`, where each ei is 0 or
      1, and each ni is positive

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    - ``generic`` -- whether to format generically, or for the prime 2 (default)

    OUTPUT: ``rep`` -- string

    This returns a string like ``Sq^{a} Sq^{b} Sq^{c} ...`` when
    `generic=False`, or a string like
    ``\\beta^{e0} P^{n1} \\beta^{e1} P^{n2} ...`` when `generic=True`.
    is odd.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import serre_cartan_mono_to_string
        sage: serre_cartan_mono_to_string((1,2,3,4))
        'Sq^{1} Sq^{2} Sq^{3} Sq^{4}'
        sage: serre_cartan_mono_to_string((1,2,3,4),latex=True)
        '\\\\text{Sq}^{1} \\\\text{Sq}^{2} \\\\text{Sq}^{3} \\\\text{Sq}^{4}'
        sage: serre_cartan_mono_to_string((0,5,1,1,0), generic=True)
        'P^{5} beta P^{1}'
        sage: serre_cartan_mono_to_string((0,5,1,1,0), generic=True, latex=True)
        '\\\\mathcal{P}^{5} \\\\beta \\\\mathcal{P}^{1}'

    The empty tuple represents the unit element 1::

        sage: serre_cartan_mono_to_string(())
        '1'
        sage: serre_cartan_mono_to_string((), generic=True)
        '1'
    """
def wood_mono_to_string(mono, latex: bool = False):
    """
    String representation of element of Wood's Y and Z bases.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of nonnegative integers (s,t)

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    OUTPUT:

    ``string`` -- concatenation of strings of the form
    ``Sq^{2^s (2^{t+1}-1)}`` for each pair (s,t)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import wood_mono_to_string
        sage: wood_mono_to_string(((1,2),(3,0)))
        'Sq^{14} Sq^{8}'
        sage: wood_mono_to_string(((1,2),(3,0)),latex=True)
        '\\\\text{Sq}^{14} \\\\text{Sq}^{8}'

    The empty tuple represents the unit element::

        sage: wood_mono_to_string(())
        '1'
    """
def wall_mono_to_string(mono, latex: bool = False):
    """
    String representation of element of Wall's basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of nonnegative integers (m,k) with `m
      >= k`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    OUTPUT:

    ``string`` -- concatenation of strings ``Q^{m}_{k}`` for each pair (m,k)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import wall_mono_to_string
        sage: wall_mono_to_string(((1,2),(3,0)))
        'Q^{1}_{2} Q^{3}_{0}'
        sage: wall_mono_to_string(((1,2),(3,0)),latex=True)
        'Q^{1}_{2} Q^{3}_{0}'

    The empty tuple represents the unit element::

        sage: wall_mono_to_string(())
        '1'
    """
def wall_long_mono_to_string(mono, latex: bool = False):
    """
    Alternate string representation of element of Wall's basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of nonnegative integers (m,k) with `m
      >= k`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    OUTPUT:

    ``string`` -- concatenation of strings of the form ``Sq^(2^m)``

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import wall_long_mono_to_string
        sage: wall_long_mono_to_string(((1,2),(3,0)))
        'Sq^{1} Sq^{2} Sq^{4} Sq^{8}'
        sage: wall_long_mono_to_string(((1,2),(3,0)),latex=True)
        '\\\\text{Sq}^{1} \\\\text{Sq}^{2} \\\\text{Sq}^{4} \\\\text{Sq}^{8}'

    The empty tuple represents the unit element::

        sage: wall_long_mono_to_string(())
        '1'
    """
def arnonA_mono_to_string(mono, latex: bool = False, p: int = 2):
    """
    String representation of element of Arnon's A basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of nonnegative integers
       (m,k) with `m >= k`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    OUTPUT: concatenation of strings of the form ``X^{m}_{k}`` for each pair
    (m,k)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import arnonA_mono_to_string
        sage: arnonA_mono_to_string(((1,2),(3,0)))
        'X^{1}_{2} X^{3}_{0}'
        sage: arnonA_mono_to_string(((1,2),(3,0)),latex=True)
        'X^{1}_{2} X^{3}_{0}'

    The empty tuple represents the unit element::

        sage: arnonA_mono_to_string(())
        '1'
    """
def arnonA_long_mono_to_string(mono, latex: bool = False, p: int = 2):
    """
    Alternate string representation of element of Arnon's A basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of nonnegative integers (m,k) with `m
      >= k`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    OUTPUT:

    ``string`` -- concatenation of strings of the form ``Sq(2^m)``

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import arnonA_long_mono_to_string
        sage: arnonA_long_mono_to_string(((1,2),(3,0)))
        'Sq^{8} Sq^{4} Sq^{2} Sq^{1}'
        sage: arnonA_long_mono_to_string(((1,2),(3,0)),latex=True)
        '\\\\text{Sq}^{8} \\\\text{Sq}^{4} \\\\text{Sq}^{2} \\\\text{Sq}^{1}'

    The empty tuple represents the unit element::

        sage: arnonA_long_mono_to_string(())
        '1'
    """
def pst_mono_to_string(mono, latex: bool = False, generic: bool = False):
    """
    String representation of element of a `P^s_t`-basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of integers (s,t) with `s >= 0`, `t >
      0`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    - ``generic`` -- whether to format generically, or for the prime 2 (default)

    OUTPUT:

    ``string`` -- concatenation of strings of the form ``P^{s}_{t}``
    for each pair (s,t)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import pst_mono_to_string
        sage: pst_mono_to_string(((1,2),(0,3)), generic=False)
        'P^{1}_{2} P^{0}_{3}'
        sage: pst_mono_to_string(((1,2),(0,3)),latex=True, generic=False)
        'P^{1}_{2} P^{0}_{3}'
        sage: pst_mono_to_string(((1,4), (((1,2), 1),((0,3), 2))), generic=True)
        'Q_{1} Q_{4} P^{1}_{2} (P^{0}_{3})^2'
        sage: pst_mono_to_string(((1,4), (((1,2), 1),((0,3), 2))), latex=True, generic=True)
        'Q_{1} Q_{4} P^{1}_{2} (P^{0}_{3})^{2}'

    The empty tuple represents the unit element::

        sage: pst_mono_to_string(())
        '1'
    """
def comm_mono_to_string(mono, latex: bool = False, generic: bool = False):
    """
    String representation of element of a commutator basis.

    This is used by the _repr_ and _latex_ methods.

    INPUT:

    - ``mono`` -- tuple of pairs of integers (s,t) with `s >= 0`, `t >
      0`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    - ``generic`` -- whether to format generically, or for the prime 2 (default)

    OUTPUT:

    ``string`` -- concatenation of strings of the form ``c_{s,t}``
    for each pair (s,t)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import comm_mono_to_string
        sage: comm_mono_to_string(((1,2),(0,3)), generic=False)
        'c_{1,2} c_{0,3}'
        sage: comm_mono_to_string(((1,2),(0,3)), latex=True)
        'c_{1,2} c_{0,3}'
        sage: comm_mono_to_string(((1, 4), (((1,2), 1),((0,3), 2))), generic=True)
        'Q_{1} Q_{4} c_{1,2} c_{0,3}^2'
        sage: comm_mono_to_string(((1, 4), (((1,2), 1),((0,3), 2))), latex=True, generic=True)
        'Q_{1} Q_{4} c_{1,2} c_{0,3}^{2}'

    The empty tuple represents the unit element::

        sage: comm_mono_to_string(())
        '1'
    """
def comm_long_mono_to_string(mono, p, latex: bool = False, generic: bool = False):
    """
    Alternate string representation of element of a commutator basis.

    Okay in low dimensions, but gets unwieldy as the dimension
    increases.

    INPUT:

    - ``mono`` -- tuple of pairs of integers (s,t) with `s >= 0`, `t >
      0`

    - ``latex`` -- boolean (default: ``False``); if ``True``, output
      LaTeX string

    - ``generic`` -- whether to format generically, or for the prime 2 (default)

    OUTPUT:

    ``string`` -- concatenation of strings of the form ``s_{2^s... 2^(s+t-1)}``
    for each pair (s,t)

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_misc import comm_long_mono_to_string
        sage: comm_long_mono_to_string(((1,2),(0,3)), 2)
        's_{24} s_{124}'
        sage: comm_long_mono_to_string(((1,2),(0,3)), 2, latex=True)
        's_{24} s_{124}'
        sage: comm_long_mono_to_string(((1, 4), (((1,2), 1),((0,3), 2))), 5, generic=True)
        'Q_{1} Q_{4} s_{5,25} s_{1,5,25}^2'
        sage: comm_long_mono_to_string(((1, 4), (((1,2), 1),((0,3), 2))), 3, latex=True, generic=True)
        'Q_{1} Q_{4} s_{3,9} s_{1,3,9}^{2}'

    The empty tuple represents the unit element::

        sage: comm_long_mono_to_string((), p=2)
        '1'
    """
def convert_perm(m):
    """
    Convert tuple m of nonnegative integers to a permutation in
    one-line form.

    INPUT:

    - ``m`` -- tuple of nonnegative integers with no repetitions

    OUTPUT:

    ``list`` -- conversion of ``m`` to a permutation of the set
    1,2,...,len(m)

    If ``m=(3,7,4)``, then one can view ``m`` as representing the
    permutation of the set `(3,4,7)` sending 3 to 3, 4 to 7, and 7 to
    4. This function converts ``m`` to the list ``[1,3,2]``, which
    represents essentially the same permutation, but of the set
    `(1,2,3)`. This list can then be passed to :func:`Permutation
    <sage.combinat.permutation.Permutation>`, and its signature can be
    computed.

    EXAMPLES::

        sage: sage.algebras.steenrod.steenrod_algebra_misc.convert_perm((3,7,4))
        [1, 3, 2]
        sage: sage.algebras.steenrod.steenrod_algebra_misc.convert_perm((5,0,6,3))
        [3, 1, 4, 2]
    """
