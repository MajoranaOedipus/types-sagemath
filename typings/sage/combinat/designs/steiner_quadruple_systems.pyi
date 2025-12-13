from sage.combinat.designs.incidence_structures import IncidenceStructure as IncidenceStructure
from sage.misc.cachefunc import cached_function as cached_function

def two_n(B):
    '''
    Return a Steiner Quadruple System on `2n` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import two_n
        sage: for n in range(4, 30):
        ....:     if (n%6) in [2,4]:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not two_n(sqs).is_t_design(3,2*n,4,1):
        ....:             print("Something is wrong !")
    '''
def three_n_minus_two(B):
    '''
    Return a Steiner Quadruple System on `3n-2` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import three_n_minus_two
        sage: for n in range(4, 30):
        ....:     if (n%6) in [2,4]:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not three_n_minus_two(sqs).is_t_design(3,3*n-2,4,1):
        ....:             print("Something is wrong !")
    '''
def three_n_minus_eight(B):
    '''
    Return a Steiner Quadruple System on `3n-8` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import three_n_minus_eight
        sage: for n in range(4, 30):
        ....:     if (n%12) == 2:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not three_n_minus_eight(sqs).is_t_design(3,3*n-8,4,1):
        ....:             print("Something is wrong !")
    '''
def three_n_minus_four(B):
    '''
    Return a Steiner Quadruple System on `3n-4` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points where `n\\equiv
      10\\pmod{12}`

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import three_n_minus_four
        sage: for n in range(4, 30):
        ....:     if n%12 == 10:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not three_n_minus_four(sqs).is_t_design(3,3*n-4,4,1):
        ....:             print("Something is wrong !")
    '''
def four_n_minus_six(B):
    '''
    Return a Steiner Quadruple System on `4n-6` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import four_n_minus_six
        sage: for n in range(4, 20):
        ....:     if (n%6) in [2,4]:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not four_n_minus_six(sqs).is_t_design(3,4*n-6,4,1):
        ....:             print("Something is wrong !")
    '''
def twelve_n_minus_ten(B):
    '''
    Return a Steiner Quadruple System on `12n-6` points.

    INPUT:

    - ``B`` -- a Steiner Quadruple System on `n` points

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import twelve_n_minus_ten
        sage: for n in range(4, 15):
        ....:     if (n%6) in [2,4]:
        ....:         sqs = designs.steiner_quadruple_system(n)
        ....:         if not twelve_n_minus_ten(sqs).is_t_design(3,12*n-10,4,1):
        ....:             print("Something is wrong !")
    '''
def relabel_system(B):
    """
    Relabel the set so that `\\{n-4, n-3, n-2, n-1\\}` is in `B`.

    INPUT:

    - ``B`` -- list of 4-uples on `0,...,n-1`

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import relabel_system
        sage: SQS8 = designs.steiner_quadruple_system(8)
        sage: relabel_system(SQS8)
        Incidence structure with 8 points and 14 blocks
    """
def P(alpha, m):
    """
    Return the collection of pairs `P_{\\alpha}(m)`.

    For more information on this system, see [Han1960]_.

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import P
        sage: P(3,4)
        [(0, 5), (2, 7), (4, 1), (6, 3)]
    """
def barP(eps, m):
    """
    Return the collection of pairs `\\overline P_{\\alpha}(m)`.

    For more information on this system, see [Han1960]_.

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import barP
        sage: barP(3,4)
        [(0, 4), (3, 5), (1, 2)]
    """
@cached_function
def barP_system(m):
    """
    Return the 1-factorization of `K_{2m}` `\\overline P(m)`.

    For more information on this system, see [Han1960]_.

    EXAMPLES::

        sage: from sage.combinat.designs.steiner_quadruple_systems import barP_system
        sage: barP_system(3)
        [[(4, 3), (2, 5)],
        [(0, 5), (4, 1)],
        [(0, 2), (1, 3)],
        [(1, 5), (4, 2), (0, 3)],
        [(0, 4), (3, 5), (1, 2)],
        [(0, 1), (2, 3), (4, 5)]]
    """
@cached_function
def steiner_quadruple_system(n, check: bool = False):
    """
    Return a Steiner Quadruple System on `n` points.

    INPUT:

    - ``n`` -- integer such that `n\\equiv 2,4\\pmod 6`

    - ``check`` -- boolean (default: ``False``); whether to check that the
      system is a Steiner Quadruple System before returning it

    EXAMPLES::

        sage: sqs4 = designs.steiner_quadruple_system(4)
        sage: sqs4
        Incidence structure with 4 points and 1 blocks
        sage: sqs4.is_t_design(3,4,4,1)
        True

        sage: sqs8 = designs.steiner_quadruple_system(8)
        sage: sqs8
        Incidence structure with 8 points and 14 blocks
        sage: sqs8.is_t_design(3,8,4,1)
        True

    TESTS::

        sage: for n in range(4, 100):                                      # long time
        ....:     if (n%6) in [2,4]:
        ....:         sqs = designs.steiner_quadruple_system(n, check=True)
    """
