from sage.rings.integer_ring import ZZ as ZZ

def profile_elt(elt, char: int = 2):
    """
    Return the smallest sub-Hopf algebra containing ``elt``.

    INPUT:

    - ``elt`` -- element of the Steenrod algebra (or a sub-Hopf algebra
      of it) or list(s) representing it
    - ``char`` -- (default: 2) the characteristic

    ``elt`` could also be a list (when ``char=2``) or a pair of lists
    (otherwise), in which case it is treated as corresponding to an
    element of the Steenrod algebra: ``(a, b, c) <-> Sq(a, b, c)`` or
    ``((a, b, c), (x, y, z)) <-> Q_a Q_b Q_c P(x, y, z)``.

    OUTPUT: the profile function corresponding to the smallest
    sub-Hopf algebra containing the element passed

    EXAMPLES::

        sage: from sage.modules.fp_graded.steenrod.profile import profile_elt
        sage: A2 = SteenrodAlgebra(2)
        sage: profile_elt(A2.Sq(2))
        (2, 1)
        sage: profile_elt(A2.Sq(4,8))
        (3, 4, 3, 2, 1)

        sage: B = SteenrodAlgebra(3)
        sage: b = B.an_element(); b
        2 Q_1 Q_3 P(2,1)
        sage: profile_elt(b, char=3)
        ((1, 1), (1, 2, 1, 2))
        sage: profile_elt(B.P(2,1), char=3)
        ((1, 1), ())
        sage: profile_elt(B.Q(2), char=3)
        ((0,), (1, 1, 2))
    """
def enveloping_profile_elements(alist, char: int = 2):
    """
    Return the profile function for the smallest sub-Hopf algebra
    containing the list of elements passed.

    INPUT:

    - ``alist`` -- list of Steenrod algebra elements
    - ``char`` -- (default: 2) the characteristic

    As with :func:`profile_elt`, the entries of ``alist`` could also
    be iterables or pairs of iterables.

    OUTPUT: the profile function for the minimum sub-algebra
    containing all the elements of ``alist``

    EXAMPLES::

        sage: from sage.modules.fp_graded.steenrod.profile import enveloping_profile_elements
        sage: enveloping_profile_elements([Sq(2),Sq(4)])
        (3, 2, 1)
        sage: enveloping_profile_elements([Sq(4)])
        (3, 2, 1)
        sage: enveloping_profile_elements([Sq(2,1,2),Sq(7)])
        (3, 2, 2, 1)

        sage: B = SteenrodAlgebra(3)
        sage: enveloping_profile_elements([B.P(2,1), B.P(0,0,3)], char=3)
        ((1, 1, 2, 1), ())
        sage: enveloping_profile_elements([B.P(3,1)], char=3)
        ((2, 1), ())
        sage: enveloping_profile_elements([B.P(2,1), B.P(0,0,3), B.Q(2)], char=3)
        ((1, 1, 2, 1), (1, 1, 2))
    """
def find_min_profile(prof, char: int = 2):
    """
    Return the smallest valid profile function containing a tuple of
    nonnegative integers.

    INPUT:

    - ``prof`` -- list or tuple of nonnegative integers
    - ``char`` -- (default: 2) the characteristic

    OUTPUT: a valid profile containing ``prof``

    A profile function `e` must satisfy `e(r) \\geq \\min( e(r-i) - i,
    e(i))` for all `0 < i < r`, and at odd primes, if `k(i+j) = 1`,
    then either `e(i) \\leq j` or `k(j) = 1` for all `i \\geq 1`, `j
    \\geq 0`. We use these inequalities to generate the smallest
    profile function `e` satisfying `e(r) \\geq prof(r)` for each `r`
    when `char=2`, and similarly at odd primes.

    EXAMPLES::

        sage: from sage.modules.fp_graded.steenrod.profile import find_min_profile
        sage: find_min_profile([1,2])
        (1, 2, 1)
        sage: find_min_profile([2,1])
        (2, 1)
        sage: find_min_profile([1,2,3])
        (1, 2, 3, 1, 1)
        sage: find_min_profile([4])
        (4, 3, 2, 1)

        sage: find_min_profile([[4], []], char=3)
        ((4, 3, 2, 1), ())
        sage: find_min_profile([[1], [2]], char=3)
        ((1,), (2, 2))
        sage: find_min_profile([[], [2,1,1,2]], char=3)
        ((0,), (2, 1, 1, 2))
    """
