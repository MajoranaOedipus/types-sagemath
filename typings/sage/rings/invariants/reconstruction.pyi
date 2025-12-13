def binary_quadratic_coefficients_from_invariants(discriminant, invariant_choice: str = 'default'):
    """
    Reconstruct a binary quadratic from the value of its discriminant.

    INPUT:

    - ``discriminant`` -- the value of the discriminant of the
      binary quadratic

    - ``invariant_choice`` -- the type of invariants provided. The accepted
      options are ``'discriminant'`` and ``'default'``, which are the same. No
      other options are implemented.

    OUTPUT:

    A set of coefficients of a binary quadratic, whose discriminant
    is equal to the given ``discriminant`` up to a scaling.

    EXAMPLES::

        sage: from sage.rings.invariants.reconstruction import binary_quadratic_coefficients_from_invariants
        sage: quadratic = invariant_theory.binary_form_from_invariants(2, [24])  # indirect doctest
        sage: quadratic
        Binary quadratic with coefficients (1, -6, 0)
        sage: quadratic.discriminant()
        24
        sage: binary_quadratic_coefficients_from_invariants(0)
        (1, 0, 0)
    """
def binary_cubic_coefficients_from_invariants(discriminant, invariant_choice: str = 'default'):
    """
    Reconstruct a binary cubic from the value of its discriminant.

    INPUT:

    - ``discriminant`` -- the value of the discriminant of the
      binary cubic

    - ``invariant_choice`` -- the type of invariants provided. The accepted
      options are ``'discriminant'`` and ``'default'``, which are the same. No
      other options are implemented.

    OUTPUT:

    A set of coefficients of a binary cubic, whose discriminant
    is equal to the given ``discriminant`` up to a scaling.

    EXAMPLES::

        sage: from sage.rings.invariants.reconstruction import binary_cubic_coefficients_from_invariants
        sage: coeffs = binary_cubic_coefficients_from_invariants(1)
        sage: coeffs
        (0, 1, -1, 0)
        sage: R.<x> = QQ[]
        sage: R(coeffs).discriminant()                                                  # needs sage.libs.pari
        1

    The two non-equivalent cubics `x^3` and `x^2*z` with discriminant 0 can't
    be distinguished based on their discriminant, hence an error is raised::

        sage: binary_cubic_coefficients_from_invariants(0)
        Traceback (most recent call last):
        ...
        ValueError: no unique reconstruction possible for binary cubics with a double root
    """
def binary_quintic_coefficients_from_invariants(invariants, K=None, invariant_choice: str = 'default', scaling: str = 'none'):
    """
    Reconstruct a binary quintic from the values of its (Clebsch) invariants.

    INPUT:

    - ``invariants`` -- list or tuple of values of the three or four
      invariants. The default option requires the Clebsch invariants `A`, `B`,
      `C` and `R` of the binary quintic.

    - ``K`` -- the field over which the quintic is defined

    - ``invariant_choice`` -- the type of invariants provided. The accepted
      options are ``'clebsch'`` and ``'default'``, which are the same. No
      other options are implemented.

    - ``scaling`` -- how the coefficients should be scaled. The accepted
      values are ``'none'`` for no scaling, ``'normalized'`` to scale in such
      a way that the resulting coefficients are independent of the scaling of
      the input invariants and ``'coprime'`` which scales the input invariants
      by dividing them by their gcd.

    OUTPUT:

    A set of coefficients of a binary quintic, whose invariants are equal to
    the given ``invariants`` up to a scaling.

    EXAMPLES:

    First we check the general case, where the invariant `M` is nonzero::

        sage: R.<x0, x1> = QQ[]
        sage: p = 3*x1^5 + 6*x1^4*x0 + 3*x1^3*x0^2 + 4*x1^2*x0^3 - 5*x1*x0^4 + 4*x0^5
        sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: reconstructed = invariant_theory.binary_form_from_invariants(  # indirect doctest
        ....:     5, invs, variables=quintic.variables())
        sage: reconstructed
        Binary quintic with coefficients (9592267437341790539005557/244140625000000,
        2149296928207625556323004064707/610351562500000000,
        11149651890347700974453304786783/76293945312500000,
        122650775751894638395648891202734239/47683715820312500000,
        323996630945706528474286334593218447/11920928955078125000,
        1504506503644608395841632538558481466127/14901161193847656250000)

    We can see that the invariants of the reconstructed form match the ones of
    the original form by scaling the invariants `B` and `C`::

        sage: scale = invs[0]/reconstructed.A_invariant()
        sage: invs[1] == reconstructed.B_invariant()*scale^2
        True
        sage: invs[2] == reconstructed.C_invariant()*scale^3
        True

    If we compare the form obtained by this reconstruction to the one found by
    letting the covariants `\\alpha` and `\\beta` be the coordinates of the form,
    we find the forms are the same up to a power of the determinant of `\\alpha`
    and `\\beta`::

        sage: alpha = quintic.alpha_covariant()
        sage: beta = quintic.beta_covariant()
        sage: g = matrix([[alpha(x0=1,x1=0), alpha(x0=0,x1=1)],
        ....:             [beta(x0=1,x1=0), beta(x0=0,x1=1)]])^-1
        sage: transformed = tuple([g.determinant()^-5*x
        ....:                      for x in quintic.transformed(g).coeffs()])
        sage: transformed == reconstructed.coeffs()
        True

    This can also be seen by computing the `\\alpha` covariant of the obtained
    form::

        sage: reconstructed.alpha_covariant().coefficient(x1)
        0
        sage: reconstructed.alpha_covariant().coefficient(x0) != 0
        True

    If the invariant `M` vanishes, then the coefficients are computed in a
    different way::

        sage: A, B, C = 3, 1, 2
        sage: M = 2*A*B - 3*C
        sage: M
        0
        sage: from sage.rings.invariants.reconstruction import binary_quintic_coefficients_from_invariants
        sage: reconstructed = binary_quintic_coefficients_from_invariants([A,B,C])
        sage: reconstructed
        (-66741943359375/2097152,
         -125141143798828125/134217728,
         0,
         52793920040130615234375/34359738368,
         19797720015048980712890625/1099511627776,
         -4454487003386020660400390625/17592186044416)
        sage: newform = sum([ reconstructed[i]*x0^i*x1^(5-i) for i in range(6) ])
        sage: newquintic = invariant_theory.binary_quintic(newform, x0, x1)
        sage: scale = 3/newquintic.A_invariant()
        sage: [3, newquintic.B_invariant()*scale^2, newquintic.C_invariant()*scale^3]
        [3, 1, 2]

    Several special cases::

        sage: quintic = invariant_theory.binary_quintic(x0^5 - x1^5, x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: binary_quintic_coefficients_from_invariants(invs)
        (1, 0, 0, 0, 0, 1)
        sage: quintic = invariant_theory.binary_quintic(x0*x1*(x0^3-x1^3), x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: binary_quintic_coefficients_from_invariants(invs)
        (0, 1, 0, 0, 1, 0)
        sage: quintic = invariant_theory.binary_quintic(x0^5 + 10*x0^3*x1^2 - 15*x0*x1^4, x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: binary_quintic_coefficients_from_invariants(invs)
        (1, 0, 10, 0, -15, 0)
        sage: quintic = invariant_theory.binary_quintic(x0^2*(x0^3 + x1^3), x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: binary_quintic_coefficients_from_invariants(invs)
        (1, 0, 0, 1, 0, 0)
        sage: quintic = invariant_theory.binary_quintic(x0*(x0^4 + x1^4), x0, x1)
        sage: invs = quintic.clebsch_invariants(as_tuple=True)
        sage: binary_quintic_coefficients_from_invariants(invs)
        (1, 0, 0, 0, 1, 0)

    For fields of characteristic 2, 3 or 5, there is no reconstruction
    implemented. This is part of :issue:`26786`.::

        sage: binary_quintic_coefficients_from_invariants([3,1,2], K=GF(5))
        Traceback (most recent call last):
        ...
        NotImplementedError: no reconstruction of binary quintics implemented
        for fields of characteristic 2, 3 or 5

    TESTS::

        sage: from sage.rings.invariants.reconstruction import binary_quintic_coefficients_from_invariants
        sage: binary_quintic_coefficients_from_invariants([1,2,3], scaling='unknown')
        Traceback (most recent call last):
        ...
        ValueError: unknown scaling option 'unknown'
    """
