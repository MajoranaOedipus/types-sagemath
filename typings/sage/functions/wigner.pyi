from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.integer import Integer as Integer

def wigner_3j(j_1, j_2, j_3, m_1, m_2, m_3, prec=None):
    """
    Return the Wigner 3-`j` symbol `\\begin{pmatrix} j_1 & j_2 & j_3 \\\\ m_1 & m_2 & m_3 \\end{pmatrix}`.

    INPUT:

    - ``j_1``, ``j_2``, ``j_3``, ``m_1``, ``m_2``, ``m_3`` -- integer or half integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES::

        sage: wigner_3j(2, 6, 4, 0, 0, 0)                                               # needs sage.symbolic
        sqrt(5/143)
        sage: wigner_3j(2, 6, 4, 0, 0, 1)
        0
        sage: wigner_3j(0.5, 0.5, 1, 0.5, -0.5, 0)                                      # needs sage.symbolic
        sqrt(1/6)
        sage: wigner_3j(40, 100, 60, -10, 60, -50)                                      # needs sage.symbolic
        95608/18702538494885*sqrt(21082735836735314343364163310/220491455010479533763)
        sage: wigner_3j(2500, 2500, 5000, 2488, 2400, -4888, prec=64)                   # needs sage.rings.real_mpfr
        7.60424456883448589e-12

    It is an error to have arguments that are not integer or half
    integer values::

        sage: wigner_3j(2.1, 6, 4, 0, 0, 0)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer
        sage: wigner_3j(2, 6, 4, 1, 0, -1.1)
        Traceback (most recent call last):
        ...
        ValueError: m values must be integer or half integer

    The Wigner 3-`j` symbol obeys the following symmetry rules:

    - invariant under any permutation of the columns (with the
      exception of a sign change where `J=j_1+j_2+j_3`):

      .. MATH::

         \\begin{pmatrix} j_1 & j_2 & j_3 \\\\ m_1 & m_2 & m_3 \\end{pmatrix}
          =\\begin{pmatrix} j_3 & j_1 & j_2 \\\\ m_3 & m_1 & m_2 \\end{pmatrix}
          =\\begin{pmatrix} j_2 & j_3 & j_1 \\\\ m_2 & m_3 & m_1 \\end{pmatrix} \\hspace{10em} \\\\\n          =(-1)^J \\begin{pmatrix} j_3 & j_2 & j_1 \\\\ m_3 & m_2 & m_1 \\end{pmatrix}
          =(-1)^J \\begin{pmatrix} j_1 & j_3 & j_2 \\\\ m_1 & m_3 & m_2 \\end{pmatrix}
          =(-1)^J \\begin{pmatrix} j_2 & j_1 & j_3 \\\\ m_2 & m_1 & m_3 \\end{pmatrix}

    - invariant under space inflection, i.e.

      .. MATH::

         \\begin{pmatrix} j_1 & j_2 & j_3 \\\\ m_1 & m_2 & m_3 \\end{pmatrix}
         =(-1)^J \\begin{pmatrix} j_1 & j_2 & j_3 \\\\ -m_1 & -m_2 & -m_3 \\end{pmatrix}

    - symmetric with respect to the 72 additional symmetries based on
      the work by [Reg1958]_

    - zero for `j_1`, `j_2`, `j_3` not fulfilling triangle relation

    - zero for `m_1 + m_2 + m_3 \\neq 0`

    - zero for violating any one of the conditions
      `j_1 \\ge |m_1|`,  `j_2 \\ge |m_2|`,  `j_3 \\ge |m_3|`

    ALGORITHM:

    This function uses the algorithm of [Ed1974]_ to calculate the
    value of the 3-`j` symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [RH2003]_.

    AUTHORS:

    - Jens Rasch (2009-03-24): initial version
    """
def clebsch_gordan(j_1, j_2, j_3, m_1, m_2, m_3, prec=None):
    """
    Return the Clebsch-Gordan coefficient
    `\\langle j_1 m_1 \\; j_2 m_2 | j_3 m_3 \\rangle`.

    The reference for this function is [Ed1974]_.

    INPUT:

    - ``j_1``, ``j_2``, ``j_3``, ``m_1``, ``m_2``, ``m_3`` -- integer or half integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES::

        sage: simplify(clebsch_gordan(3/2,1/2,2, 3/2,1/2,2))                            # needs sage.symbolic
        1
        sage: clebsch_gordan(1.5,0.5,1, 1.5,-0.5,1)                                     # needs sage.symbolic
        1/2*sqrt(3)
        sage: clebsch_gordan(3/2,1/2,1, -1/2,1/2,0)                                     # needs sage.symbolic
        -sqrt(3)*sqrt(1/6)

    .. NOTE::

        The Clebsch-Gordan coefficient will be evaluated via its relation
        to Wigner 3-`j` symbols:

        .. MATH::

            \\langle j_1 m_1 \\; j_2 m_2 | j_3 m_3 \\rangle
            =(-1)^{j_1-j_2+m_3} \\sqrt{2j_3+1}
            \\begin{pmatrix} j_1 & j_2 & j_3 \\\\ m_1 & m_2 & -m_3 \\end{pmatrix}

        See also the documentation on Wigner 3-`j` symbols which exhibit much
        higher symmetry relations than the Clebsch-Gordan coefficient.

    AUTHORS:

    - Jens Rasch (2009-03-24): initial version
    """
def racah(aa, bb, cc, dd, ee, ff, prec=None):
    """
    Return the Racah symbol `W(aa,bb,cc,dd;ee,ff)`.

    INPUT:

    - ``aa``, ..., ``ff`` -- integer or half integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES::

        sage: racah(3,3,3,3,3,3)                                                        # needs sage.symbolic
        -1/14

    .. NOTE::

        The Racah symbol is related to the Wigner 6-`j` symbol:

        .. MATH::

           \\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\end{Bmatrix}
           =(-1)^{j_1+j_2+j_4+j_5} W(j_1,j_2,j_5,j_4;j_3,j_6)

        Please see the 6-`j` symbol for its much richer symmetries and for
        additional properties.

    ALGORITHM:

    This function uses the algorithm of [Ed1974]_ to calculate the
    value of the 6-`j` symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [RH2003]_.

    AUTHORS:

    - Jens Rasch (2009-03-24): initial version
    """
def wigner_6j(j_1, j_2, j_3, j_4, j_5, j_6, prec=None):
    """
    Return the Wigner 6-`j` symbol `\\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\end{Bmatrix}`.

    INPUT:

    - ``j_1``, ..., ``j_6`` -- integer or half integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: wigner_6j(3,3,3,3,3,3)
        -1/14
        sage: wigner_6j(5,5,5,5,5,5)
        1/52
        sage: wigner_6j(6,6,6,6,6,6)
        309/10868
        sage: wigner_6j(8,8,8,8,8,8)
        -12219/965770
        sage: wigner_6j(30,30,30,30,30,30)
        36082186869033479581/87954851694828981714124
        sage: wigner_6j(0.5,0.5,1,0.5,0.5,1)
        1/6
        sage: wigner_6j(200,200,200,200,200,200, prec=1000)*1.0
        0.000155903212413242

    It is an error to have arguments that are not integer or half
    integer values or do not fulfill the triangle relation::

        sage: wigner_6j(2.5,2.5,2.5,2.5,2.5,2.5)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation
        sage: wigner_6j(0.5,0.5,1.1,0.5,0.5,1.1)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation

    The Wigner 6-`j` symbol is related to the Racah symbol but exhibits
    more symmetries as detailed below.

    .. MATH::

       \\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\end{Bmatrix}
        =(-1)^{j_1+j_2+j_4+j_5} W(j_1,j_2,j_5,j_4;j_3,j_6)

    The Wigner 6-`j` symbol obeys the following symmetry rules:

    - Wigner 6-`j` symbols are left invariant under any permutation of
      the columns:

      .. MATH::

         \\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\end{Bmatrix}
          =\\begin{Bmatrix} j_3 & j_1 & j_2 \\\\ j_6 & j_4 & j_5 \\end{Bmatrix}
          =\\begin{Bmatrix} j_2 & j_3 & j_1 \\\\ j_5 & j_6 & j_4 \\end{Bmatrix} \\hspace{7em} \\\\\n          =\\begin{Bmatrix} j_3 & j_2 & j_1 \\\\ j_6 & j_5 & j_4 \\end{Bmatrix}
          =\\begin{Bmatrix} j_1 & j_3 & j_2 \\\\ j_4 & j_6 & j_5 \\end{Bmatrix}
          =\\begin{Bmatrix} j_2 & j_1 & j_3 \\\\ j_5 & j_4 & j_6 \\end{Bmatrix} \\hspace{3em}

    - They are invariant under the exchange of the upper and lower
      arguments in each of any two columns, i.e.

      .. MATH::

         \\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\end{Bmatrix}
          =\\begin{Bmatrix} j_1 & j_5 & j_6 \\\\ j_4 & j_2 & j_3 \\end{Bmatrix}
          =\\begin{Bmatrix} j_4 & j_2 & j_6 \\\\ j_1 & j_5 & j_3 \\end{Bmatrix}
          =\\begin{Bmatrix} j_4 & j_5 & j_3 \\\\ j_1 & j_2 & j_6 \\end{Bmatrix}

    - additional 6 symmetries [Reg1959]_ giving rise to 144 symmetries
      in total

    - only nonzero if any triple of `j`'s fulfill a triangle relation

    ALGORITHM:

    This function uses the algorithm of [Ed1974]_ to calculate the
    value of the 6-`j` symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [RH2003]_.
    """
def wigner_9j(j_1, j_2, j_3, j_4, j_5, j_6, j_7, j_8, j_9, prec=None):
    """
    Return the Wigner 9-`j` symbol
    `\\begin{Bmatrix} j_1 & j_2 & j_3 \\\\ j_4 & j_5 & j_6 \\\\ j_7 & j_8 & j_9 \\end{Bmatrix}`.

    INPUT:

    - ``j_1``, ..., ``j_9`` -- integer or half integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES:

    A couple of examples and test cases, note that for speed reasons a
    precision is given::

        sage: # needs sage.symbolic
        sage: wigner_9j(1,1,1, 1,1,1, 1,1,0, prec=64) # ==1/18
        0.0555555555555555555
        sage: wigner_9j(1,1,1, 1,1,1, 1,1,1)
        0
        sage: wigner_9j(1,1,1, 1,1,1, 1,1,2, prec=64) # ==1/18
        0.0555555555555555556
        sage: wigner_9j(1,2,1, 2,2,2, 1,2,1, prec=64) # ==-1/150
        -0.00666666666666666667
        sage: wigner_9j(3,3,2, 2,2,2, 3,3,2, prec=64) # ==157/14700
        0.0106802721088435374
        sage: wigner_9j(3,3,2, 3,3,2, 3,3,2, prec=64) # ==3221*sqrt(70)/(246960*sqrt(105)) - 365/(3528*sqrt(70)*sqrt(105))
        0.00944247746651111739
        sage: wigner_9j(3,3,1, 3.5,3.5,2, 3.5,3.5,1, prec=64) # ==3221*sqrt(70)/(246960*sqrt(105)) - 365/(3528*sqrt(70)*sqrt(105))
        0.0110216678544351364
        sage: wigner_9j(100,80,50, 50,100,70, 60,50,100, prec=1000)*1.0
        1.05597798065761e-7
        sage: wigner_9j(30,30,10, 30.5,30.5,20, 30.5,30.5,10, prec=1000)*1.0 # ==(80944680186359968990/95103769817469)*sqrt(1/682288158959699477295)
        0.0000325841699408828
        sage: wigner_9j(64,62.5,114.5, 61.5,61,112.5, 113.5,110.5,60, prec=1000)*1.0
        -3.41407910055520e-39
        sage: wigner_9j(15,15,15, 15,3,15, 15,18,10, prec=1000)*1.0
        -0.0000778324615309539
        sage: wigner_9j(1.5,1,1.5, 1,1,1, 1.5,1,1.5)
        0

    It is an error to have arguments that are not integer or half
    integer values or do not fulfill the triangle relation::

        sage: wigner_9j(0.5,0.5,0.5, 0.5,0.5,0.5, 0.5,0.5,0.5,prec=64)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation
        sage: wigner_9j(1,1,1, 0.5,1,1.5, 0.5,1,2.5,prec=64)                            # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation

    ALGORITHM:

    This function uses the algorithm of [Ed1974]_ to calculate the
    value of the 3-`j` symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [RH2003]_.
    """
def gaunt(l_1, l_2, l_3, m_1, m_2, m_3, prec=None):
    """
    Return the Gaunt coefficient.

    The Gaunt coefficient is defined as the integral over three
    spherical harmonics:

    .. MATH::

        Y(l_1,l_2,l_3,m_1,m_2,m_3) \\hspace{12em} \\\\\n        =\\int Y_{l_1,m_1}(\\Omega) \\\n         Y_{l_2,m_2}(\\Omega) \\ Y_{l_3,m_3}(\\Omega) \\ d\\Omega \\hspace{5em} \\\\\n        =\\sqrt{\\frac{(2l_1+1)(2l_2+1)(2l_3+1)}{4\\pi}} \\hspace{6.5em} \\\\\n         \\times \\begin{pmatrix} l_1 & l_2 & l_3 \\\\ 0 & 0 & 0 \\end{pmatrix}
         \\begin{pmatrix} l_1 & l_2 & l_3 \\\\ m_1 & m_2 & m_3 \\end{pmatrix}

    INPUT:

    - ``l_1``, ``l_2``, ``l_3``, ``m_1``, ``m_2``, ``m_3`` -- integer

    - ``prec`` -- precision (default: ``None``); providing a precision can
      drastically speed up the calculation

    OUTPUT:

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: gaunt(1,0,1,1,0,-1)
        -1/2/sqrt(pi)
        sage: gaunt(1,0,1,1,0,0)
        0
        sage: gaunt(29,29,34,10,-5,-5)
        1821867940156/215552371055153321*sqrt(22134)/sqrt(pi)
        sage: gaunt(20,20,40,1,-1,0)
        28384503878959800/74029560764440771/sqrt(pi)
        sage: gaunt(12,15,5,2,3,-5)
        91/124062*sqrt(36890)/sqrt(pi)
        sage: gaunt(10,10,12,9,3,-12)
        -98/62031*sqrt(6279)/sqrt(pi)
        sage: gaunt(1000,1000,1200,9,3,-12).n(64)
        0.00689500421922113448

    If the sum of the `l_i` is odd, the answer is zero, even for Python
    ints (see :issue:`14766`)::

        sage: gaunt(1,2,2,1,0,-1)
        0
        sage: gaunt(int(1),int(2),int(2),1,0,-1)
        0

    It is an error to use non-integer values for `l` or `m`::

        sage: gaunt(1.2,0,1.2,0,0,0)                                                    # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        TypeError: Attempt to coerce non-integral RealNumber to Integer
        sage: gaunt(1,0,1,1.1,0,-1.1)                                                   # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        TypeError: Attempt to coerce non-integral RealNumber to Integer

    TESTS:

    Check for :issue:`14735`::

        sage: gaunt(int(1),int(1),int(1),int(0),int(1),int(-1))
        0

    The Gaunt coefficient obeys the following symmetry rules:

    - invariant under any permutation of the columns

      .. MATH::

          Y(l_1,l_2,l_3,m_1,m_2,m_3)
          =Y(l_3,l_1,l_2,m_3,m_1,m_2) \\hspace{3em} \\\\ \\hspace{3em}
          =Y(l_2,l_3,l_1,m_2,m_3,m_1)
          =Y(l_3,l_2,l_1,m_3,m_2,m_1) \\\\ \\hspace{3em}
          =Y(l_1,l_3,l_2,m_1,m_3,m_2)
          =Y(l_2,l_1,l_3,m_2,m_1,m_3)

    - invariant under space inflection, i.e.

      .. MATH::

          Y(l_1,l_2,l_3,m_1,m_2,m_3)
          =Y(l_1,l_2,l_3,-m_1,-m_2,-m_3)

    - symmetric with respect to the 72 Regge symmetries as inherited
      for the 3-`j` symbols [Reg1958]_

    - zero for `l_1`, `l_2`, `l_3` not fulfilling triangle relation

    - zero for violating any one of the conditions: `l_1 \\ge |m_1|`,
      `l_2 \\ge |m_2|`, `l_3 \\ge |m_3|`

    - nonzero only for an even sum of the `l_i`, i.e.
      `J=l_1+l_2+l_3=2n` for `n` in `\\Bold{N}`

    ALGORITHM:

    This function uses the algorithm of [LdB1982]_ to
    calculate the value of the Gaunt coefficient exactly. Note that
    the formula contains alternating sums over large factorials and is
    therefore unsuitable for finite precision arithmetic and only
    useful for a computer algebra system [RH2003]_.

    AUTHORS:

    - Jens Rasch (2009-03-24): initial version for Sage
    """
