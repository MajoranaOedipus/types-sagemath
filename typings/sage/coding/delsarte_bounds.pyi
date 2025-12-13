def krawtchouk(n, q, l, x, check: bool = True):
    """
    Compute `K^{n,q}_l(x)`, the Krawtchouk (a.k.a. Kravchuk) polynomial.

    See :wikipedia:`Kravchuk_polynomials`.

    It is defined by the generating function

    .. MATH::

        (1+(q-1)z)^{n-x}(1-z)^x=\\sum_{l} K^{n,q}_l(x)z^l

    and is equal to

    .. MATH::

        K^{n,q}_l(x)=\\sum_{j=0}^l (-1)^j (q-1)^{(l-j)} \\binom{x}{j} \\binom{n-x}{l-j}.

    INPUT:

    - ``n``, ``q``, ``x`` -- arbitrary numbers

    - ``l`` -- nonnegative integer

    - ``check`` -- check the input for correctness. ``True`` by
      default. Otherwise, pass it as it is. Use ``check=False`` at
      your own risk.

    .. SEEALSO::

        :class:`Symbolic Krawtchouk polynomials
        <sage.functions.orthogonal_polys.Func_krawtchouk>` `\\tilde{K}_l(x; n, p)`
        which are related by

        .. MATH::

            (-q)^l K^{n,q^{-1}}_l(x) = \\tilde{K}_l(x; n, 1-q).

    EXAMPLES::

        sage: codes.bounds.krawtchouk(24,2,5,4)
        2224
        sage: codes.bounds.krawtchouk(12300,4,5,6)
        567785569973042442072

    TESTS:

    Check that the bug reported on :issue:`19561` is fixed::

        sage: codes.bounds.krawtchouk(3,2,3,3)
        -1
        sage: codes.bounds.krawtchouk(int(3),int(2),int(3),int(3))
        -1
        sage: codes.bounds.krawtchouk(int(3),int(2),int(3),int(3),check=False)
        -1.0
        sage: codes.bounds.krawtchouk(24,2,5,4)
        2224

    Other unusual inputs::

        sage: codes.bounds.krawtchouk(sqrt(5),1-I*sqrt(3),3,55.3).n()                   # needs sage.symbolic
        211295.892797... + 1186.42763...*I
        sage: codes.bounds.krawtchouk(-5/2,7*I,3,-1/10)                                 # needs sage.symbolic
        480053/250*I - 357231/400
        sage: codes.bounds.krawtchouk(1,1,-1,1)
        Traceback (most recent call last):
        ...
        ValueError: l must be a nonnegative integer
        sage: codes.bounds.krawtchouk(1,1,3/2,1)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
    """
def eberlein(n, w, k, u, check: bool = True):
    """
    Compute `E^{w,n}_k(x)`, the Eberlein polynomial.

    See :wikipedia:`Eberlein_polynomials`.

    It is defined as:

    .. MATH::

        E^{w,n}_k(u)=\\sum_{j=0}^k (-1)^j \\binom{u}{j} \\binom{w-u}{k-j}
        \\binom{n-w-u}{k-j},

    INPUT:

    - ``w``, ``k``, ``x`` -- arbitrary numbers

    - ``n`` -- nonnegative integer

    - ``check`` -- check the input for correctness. ``True`` by
      default. Otherwise, pass it as it is. Use ``check=False`` at
      your own risk.

    EXAMPLES::

        sage: codes.bounds.eberlein(24,10,2,6)
        -9

    TESTS:

    check normal inputs (various formats for arguments) ::

        sage: codes.bounds.eberlein(24,10,2,6)
        -9
        sage: codes.bounds.eberlein(int(24),int(10),int(2),int(6))
        -9
        sage: codes.bounds.eberlein(int(24),int(10),int(2),int(6),check=False)
        -9

    unusual inputs ::

        sage: codes.bounds.eberlein(-1,1,1,1)
        Traceback (most recent call last):
        ...
        ValueError: l must be a nonnegative integer
        sage: codes.bounds.eberlein(1,1,3/2,1)
        Traceback (most recent call last):
        ...
        TypeError: either m or x-m must be an integer
    """
def delsarte_bound_constant_weight_code(n, d, w, return_data: bool = False, solver: str = 'PPL', isinteger: bool = False):
    """
    Find the Delsarte bound on a constant weight code.

    Find the Delsarte bound on a constant weight code of weight ``w``, length
    ``n``, lower bound on minimal distance ``d``.

    INPUT:

    - ``n`` -- the code length

    - ``d`` -- the (lower bound on) minimal distance of the code

    - ``w`` -- the weight of the code

    - ``return_data`` -- if ``True``, return a triple
      ``(W,LP,bound)``, where ``W`` is a weights vector, and ``LP``
      the Delsarte upper bound LP; both of them are Sage LP data.
      ``W`` need not be a weight distribution of a code.

    - ``solver`` -- the LP/ILP solver to be used. Defaults to
      ``PPL``. It is arbitrary precision, thus there will be no
      rounding errors. With other solvers (see
      :class:`MixedIntegerLinearProgram` for the list), you are on
      your own!

    - ``isinteger`` -- if ``True``, uses an integer programming solver
      (ILP), rather that an LP solver. Can be very slow if set to
      ``True``.

    EXAMPLES:

    The bound on the size of codes of length 17, weight 3, and minimal distance 4::

       sage: codes.bounds.delsarte_bound_constant_weight_code(17, 4, 3)
       45
       sage: a, p, val = codes.bounds.delsarte_bound_constant_weight_code(17, 4, 3, return_data=True)
       sage: [j for i,j in p.get_values(a).items()]
       [21, 70/3]

    The stricter bound (using ILP) on codes of length 17, weight 3, and minimal
    distance 4::

       sage: codes.bounds.delsarte_bound_constant_weight_code(17, 4, 3, isinteger=True)
       43
    """
def delsarte_bound_hamming_space(n, d, q, return_data: bool = False, solver: str = 'PPL', isinteger: bool = False):
    """
    Find the Delsarte bound on codes in ``H_q^n`` of minimal distance ``d``.

    Find the Delsarte bound [De1973]_ on the size of codes in
    the Hamming space ``H_q^n`` of minimal distance ``d``.

    INPUT:

    - ``n`` -- the code length

    - ``d`` -- the (lower bound on) minimal distance of the code

    - ``q`` -- the size of the alphabet

    - ``return_data`` -- if ``True``, return a triple
      ``(W,LP,bound)``, where ``W`` is a weights vector, and ``LP``
      the Delsarte upper bound LP; both of them are Sage LP data.
      ``W`` need not be a weight distribution of a code.

    - ``solver`` -- the LP/ILP solver to be used. Defaults to
      ``PPL``. It is arbitrary precision, thus there will be no
      rounding errors. With other solvers (see
      :class:`MixedIntegerLinearProgram` for the list), you are on
      your own!

    - ``isinteger`` -- if ``True``, uses an integer programming solver
      (ILP), rather that an LP solver. Can be very slow if set to
      ``True``.

    EXAMPLES:

    The bound on the size of the `\\GF{2}`-codes of length 11 and minimal distance 6::

       sage: codes.bounds.delsarte_bound_hamming_space(11, 6, 2)
       12
       sage: a, p, val = codes.bounds.delsarte_bound_hamming_space(11, 6, 2, return_data=True)
       sage: [j for i,j in p.get_values(a).items()]
       [1, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0]

    The bound on the size of the `\\GF{2}`-codes of length 24 and minimal distance
    8, i.e. parameters of the extended binary Golay code::

       sage: a,p,x = codes.bounds.delsarte_bound_hamming_space(24,8,2,return_data=True)
       sage: x
       4096
       sage: [j for i,j in p.get_values(a).items()]
       [1, 0, 0, 0, 0, 0, 0, 0, 759, 0, 0, 0, 2576, 0, 0, 0, 759, 0, 0, 0, 0, 0, 0, 0, 1]

    The bound on the size of `\\GF{4}`-codes of length 11 and minimal distance 3::

       sage: codes.bounds.delsarte_bound_hamming_space(11,3,4)
       327680/3

    An improvement of a known upper bound (150) from https://www.win.tue.nl/~aeb/codes/binary-1.html ::

       sage: a,p,x = codes.bounds.delsarte_bound_hamming_space(23,10,2,return_data=True,isinteger=True); x # long time
       148
       sage: [j for i,j in p.get_values(a).items()]                                      # long time
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 95, 0, 2, 0, 36, 0, 14, 0, 0, 0, 0, 0, 0, 0]

    Note that a usual LP, without integer variables, won't do the trick ::

       sage: codes.bounds.delsarte_bound_hamming_space(23,10,2).n(20)
       151.86

    Such an input is invalid::

       sage: codes.bounds.delsarte_bound_hamming_space(11,3,-4)
       Solver exception: PPL : There is no feasible solution
       False
    """
def delsarte_bound_additive_hamming_space(n, d, q, d_star: int = 1, q_base: int = 0, return_data: bool = False, solver: str = 'PPL', isinteger: bool = False):
    """
    Find a modified Delsarte bound on additive codes in Hamming space `H_q^n` of minimal distance `d`.

    Find the Delsarte LP bound on ``F_{q_base}``-dimension of additive
    codes in Hamming space `H_q^n` of minimal distance ``d`` with
    minimal distance of the dual code at least ``d_star``.  If
    ``q_base`` is set to nonzero, then ``q`` is a power of
    ``q_base``, and the code is, formally, linear over
    ``F_{q_base}``. Otherwise it is assumed that ``q_base==q``.

    INPUT:

    - ``n`` -- the code length

    - ``d`` -- the (lower bound on) minimal distance of the code

    - ``q`` -- the size of the alphabet

    - ``d_star`` -- the (lower bound on) minimal distance of the dual code;
      only makes sense for additive codes

    - ``q_base`` -- if ``0``, the code is assumed to be linear. Otherwise,
      ``q=q_base^m`` and the code is linear over ``F_{q_base}``

    - ``return_data`` -- if ``True``, return a triple ``(W,LP,bound)``,
      where ``W`` is a weights vector, and ``LP`` the Delsarte bound
      LP; both of them are Sage LP data.  ``W`` need not be a weight
      distribution of a code, or, if ``isinteger==False``, even have
      integer entries.

    - ``solver`` -- the LP/ILP solver to be used. Defaults to ``'PPL'``. It is
      arbitrary precision, thus there will be no rounding errors. With
      other solvers (see :class:`MixedIntegerLinearProgram` for the
      list), you are on your own!

    - ``isinteger`` -- if ``True``, uses an integer programming solver (ILP),
      rather that an LP solver (can be very slow if set to ``True``)

    EXAMPLES:

    The bound on dimension of linear `\\GF{2}`-codes of length 11 and minimal distance 6::

        sage: codes.bounds.delsarte_bound_additive_hamming_space(11, 6, 2)
        3
        sage: a,p,val = codes.bounds.delsarte_bound_additive_hamming_space(\\\n        ....:                11, 6, 2, return_data=True)
        sage: [j for i,j in p.get_values(a).items()]
        [1, 0, 0, 0, 0, 0, 5, 2, 0, 0, 0, 0]

    The bound on the dimension of linear `\\GF{4}`-codes of length 11 and minimal distance 3::

        sage: codes.bounds.delsarte_bound_additive_hamming_space(11,3,4)
        8

    The bound on the `\\GF{2}`-dimension of additive `\\GF{4}`-codes of length 11 and minimal
    distance 3::

        sage: codes.bounds.delsarte_bound_additive_hamming_space(11,3,4,q_base=2)
        16

    Such a ``d_star`` is not possible::

        sage: codes.bounds.delsarte_bound_additive_hamming_space(11,3,4,d_star=9)
        Solver exception: PPL : There is no feasible solution
        False

    TESTS::

        sage: a,p,x = codes.bounds.delsarte_bound_additive_hamming_space(\\\n        ....:            19,15,7,return_data=True,isinteger=True)
        sage: [j for i,j in p.get_values(a).items()]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 307, 0, 0, 1, 34]
        sage: codes.bounds.delsarte_bound_additive_hamming_space(19,15,7,solver='glpk')
        3
        sage: codes.bounds.delsarte_bound_additive_hamming_space(\\\n        ....:    19,15,7, isinteger=True, solver='glpk')
        3
    """
def delsarte_bound_Q_matrix(q, d, return_data: bool = False, solver: str = 'PPL', isinteger: bool = False):
    """
    Delsarte bound on a code with Q matrix ``q`` and lower bound on min. dist. ``d``.

    Find the Delsarte bound on a code with Q matrix ``q`` and lower bound on
    minimal distance ``d``.

    INPUT:

    - ``q`` -- the Q matrix

    - ``d`` -- the (lower bound on) minimal distance of the code

    - ``return_data`` -- if ``True``, return a triple
      ``(W,LP,bound)``, where ``W`` is a weights vector, and ``LP``
      the Delsarte upper bound LP; both of them are Sage LP data.
      ``W`` need not be a weight distribution of a code.

    - ``solver`` -- the LP/ILP solver to be used. Defaults to
      ``PPL``. It is arbitrary precision, thus there will be no
      rounding errors. With other solvers (see
      :class:`MixedIntegerLinearProgram` for the list), you are on
      your own!

    - ``isinteger`` -- if ``True``, uses an integer programming solver
      (ILP), rather that an LP solver. Can be very slow if set to
      ``True``.

    EXAMPLES:

    The bound on dimension of linear `\\GF{2}`-codes of length 10 and minimal distance 6::

        sage: q_matrix = Matrix([[codes.bounds.krawtchouk(10,2,i,j) for i in range(11)]
        ....:                    for j in range(11)])
        sage: codes.bounds.delsarte_bound_Q_matrix(q_matrix, 6)
        2

        sage: a,p,val = codes.bounds.delsarte_bound_Q_matrix(q_matrix, 6, return_data=True)
        sage: [j for i,j in p.get_values(a).items()]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    TESTS:

    Cases for using Hamming scheme Q matrix::

        sage: q_matrix = Matrix([[codes.bounds.krawtchouk(10,2,i,j) for i in range(11)] for j in range(11)])
        sage: codes.bounds.delsarte_bound_Q_matrix(q_matrix, 6)
        2

        sage: a,p,val = codes.bounds.delsarte_bound_Q_matrix(q_matrix, 6, return_data=True)
        sage: [j for i,j in p.get_values(a).items()]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    """
