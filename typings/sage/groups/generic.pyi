from _typeshed import Incomplete
from sage.arith.misc import integer_ceil as integer_ceil, integer_floor as integer_floor, xlcm as xlcm
from sage.arith.srange import xsrange as xsrange
from sage.misc.misc_c import prod as prod

multiplication_names: Incomplete
addition_names: Incomplete

def multiple(a, n, operation: str = '*', identity=None, inverse=None, op=None):
    """
    Return either `na` or `a^n`, where `n` is any integer and `a` is
    a Python object on which a group operation such as addition or
    multiplication is defined.  Uses the standard binary algorithm.

    INPUT: See the documentation for ``discrete_logarithm()``.

    EXAMPLES::

        sage: multiple(2, 5)
        32
        sage: multiple(RealField()('2.5'), 4)                                           # needs sage.rings.real_mpfr
        39.0625000000000
        sage: multiple(2, -3)
        1/8
        sage: multiple(2, 100, '+') == 100*2
        True
        sage: multiple(2, 100) == 2**100
        True
        sage: multiple(2, -100,) == 2**-100
        True
        sage: R.<x> = ZZ[]
        sage: multiple(x, 100)
        x^100
        sage: multiple(x, 100, '+')
        100*x
        sage: multiple(x, -10)
        1/x^10

    Idempotence is detected, making the following fast::

        sage: multiple(1, 10^1000)
        1

        sage: # needs sage.schemes
        sage: E = EllipticCurve('389a1')
        sage: P = E(-1,1)
        sage: multiple(P, 10, '+')
        (645656132358737542773209599489/22817025904944891235367494656 :
         525532176124281192881231818644174845702936831/3446581505217248068297884384990762467229696 : 1)
        sage: multiple(P, -10, '+')
        (645656132358737542773209599489/22817025904944891235367494656 :
         -528978757629498440949529703029165608170166527/3446581505217248068297884384990762467229696 : 1)
    """

class multiples:
    '''
    Return an iterator which runs through ``P0+i*P`` for ``i`` in ``range(n)``.

    ``P`` and ``P0`` must be Sage objects in some group; if the operation is
    multiplication then the returned values are instead ``P0*P**i``.

    EXAMPLES::

        sage: list(multiples(1, 10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: list(multiples(1, 10, 100))
        [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

        sage: E = EllipticCurve(\'389a1\')                                                # needs sage.schemes
        sage: P = E(-1,1)                                                               # needs sage.schemes
        sage: for Q in multiples(P, 5): print((Q, Q.height()/P.height()))               # needs sage.schemes
        ((0 : 1 : 0), 0.000000000000000)
        ((-1 : 1 : 1), 1.00000000000000)
        ((10/9 : -35/27 : 1), 4.00000000000000)
        ((26/361 : -5720/6859 : 1), 9.00000000000000)
        ((47503/16641 : 9862190/2146689 : 1), 16.0000000000000)

        sage: R.<x> = ZZ[]
        sage: list(multiples(x, 5))
        [0, x, 2*x, 3*x, 4*x]
        sage: list(multiples(x, 5, operation=\'*\'))
        [1, x, x^2, x^3, x^4]
        sage: list(multiples(x, 5, indexed=True))
        [(0, 0), (1, x), (2, 2*x), (3, 3*x), (4, 4*x)]
        sage: list(multiples(x, 5, indexed=True, operation=\'*\'))
        [(0, 1), (1, x), (2, x^2), (3, x^3), (4, x^4)]
        sage: for i,y in multiples(x, 5, indexed=True): print("%s  times %s = %s"%(i,x,y))
        0  times x = 0
        1  times x = x
        2  times x = 2*x
        3  times x = 3*x
        4  times x = 4*x

        sage: for i,n in multiples(3, 5, indexed=True, operation=\'*\'):
        ....:     print("3 to the power %s = %s" % (i,n))
        3 to the power 0 = 1
        3 to the power 1 = 3
        3 to the power 2 = 9
        3 to the power 3 = 27
        3 to the power 4 = 81
    '''
    op: Incomplete
    P: Incomplete
    Q: Incomplete
    i: int
    bound: Incomplete
    indexed: Incomplete
    def __init__(self, P, n, P0=None, indexed: bool = False, operation: str = '+', op=None) -> None:
        """
        Create a multiples iterator.

        INPUT:

        - ``P`` -- step value; any Sage object on which a binary operation is defined
        - ``n`` -- number of multiples; nonnegative integer
        - ``P0`` -- offset (default: 0); Sage object which can be 'added' to P
        - ``indexed`` -- boolean (default: ``False``)

          If ``indexed==False``, then the iterator delivers ``P0+i*P``
          (if ``operation=='+'``) or ``P0*P**i`` (if
          ``operation=='*'``), for ``i`` in ``range(n)``.

          If ``indexed==True`` then the iterator delivers tuples
          ``(i, P0+i*P)`` or ``(i, P0*P**i)``.

        - ``operation`` -- string: ``'+'`` (the default) or ``'*'`` or other.

          If other, a function ``op()`` must be supplied (a function
          of 2 arguments) defining the group binary operation; also
          ``P0`` must be supplied.
        """
    def __next__(self):
        """
        Return the next item in this multiples iterator.
        """
    next = __next__
    def __iter__(self):
        """
        Standard member function making this class an iterator.
        """

def bsgs(a, b, bounds, operation: str = '*', identity=None, inverse=None, op=None):
    """
    Totally generic discrete baby-step giant-step function.

    Solves `na=b` (or `a^n=b`) with `lb\\le n\\le ub` where ``bounds==(lb,ub)``,
    raising an error if no such `n` exists.

    `a` and `b` must be elements of some group with given identity,
    inverse of ``x`` given by ``inverse(x)``, and group operation on
    ``x``, ``y`` by ``op(x,y)``.

    If operation is '*' or '+' then the other
    arguments are provided automatically; otherwise they must be
    provided by the caller.

    .. SEEALSO::

        - :func:`discrete_log` for a potentially faster algorithm by combining
          Pohlig-Hellman with baby-step adjacent-step;
        - :func:`order_from_bounds` to find the exact order instead of just some
          multiple of the order.

    INPUT:

    - ``a`` -- group element
    - ``b`` -- group element
    - ``bounds`` -- a 2-tuple of integers ``(lower,upper)`` with ``0<=lower<=upper``
    - ``operation`` -- string: ``'*'``, ``'+'``, other
    - ``identity`` -- the identity element of the group
    - ``inverse`` -- function of 1 argument ``x``, returning inverse of ``x``
    - ``op`` -- function of 2 arguments ``x``, ``y`` returning ``x*y`` in the group

    OUTPUT:

    An integer `n` such that `a^n = b` (or `na = b`).  If no
    such `n` exists, this function raises a :exc:`ValueError` exception.

    .. NOTE::

        This is a generalization of discrete logarithm.  One
        situation where this version is useful is to find the order of
        an element in a group where we only have bounds on the group
        order (see the elliptic curve example below).

    ALGORITHM: Baby step giant step.  Time and space are soft
    `O(\\sqrt{n})` where `n` is the difference between upper and lower
    bounds.

    EXAMPLES::

        sage: from sage.groups.generic import bsgs
        sage: b = Mod(2,37);  a = b^20
        sage: bsgs(b, a, (0, 36))
        20

        sage: p = next_prime(10^20)                                                     # needs sage.libs.pari
        sage: a = Mod(2,p); b = a^(10^25)                                               # needs sage.libs.pari
        sage: bsgs(a, b, (10^25 - 10^6, 10^25 + 10^6)) == 10^25                         # needs sage.libs.pari
        True

        sage: # needs sage.rings.finite_rings
        sage: K = GF(3^6,'b')
        sage: a = K.gen()
        sage: b = a^210
        sage: bsgs(a, b, (0, K.order() - 1))
        210

        sage: K.<z> = CyclotomicField(230)                                              # needs sage.rings.number_field
        sage: w = z^500                                                                 # needs sage.rings.number_field
        sage: bsgs(z, w, (0, 229))                                                      # needs sage.rings.number_field
        40

    An additive example in an elliptic curve group::

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: F.<a> = GF(37^5)
        sage: E = EllipticCurve(F, [1,1])
        sage: P = E.lift_x(a); P
        (a : 28*a^4 + 15*a^3 + 14*a^2 + 7 : 1)

    This will return a multiple of the order of P::

        sage: bsgs(P, P.parent().zero(), Hasse_bounds(F.order()), operation='+')            # needs sage.rings.finite_rings sage.schemes
        69327408

    AUTHOR:

    - John Cremona (2008-03-15)
    """
def discrete_log_rho(a, base, ord=None, operation: str = '*', identity=None, inverse=None, op=None, hash_function=...):
    '''
    Pollard Rho algorithm for computing discrete logarithm in cyclic
    group of prime order.
    If the group order is very small it falls back to the baby step giant step
    algorithm.

    INPUT:

    - ``a`` -- a group element
    - ``base`` -- a group element
    - ``ord`` -- the order of ``base`` or ``None``, in this case we try
      to compute it
    - ``operation`` -- string (default: ``\'*\'``); denoting whether we
      are in an additive group or a multiplicative one
    - ``identity`` -- the group\'s identity
    - ``inverse`` -- function of 1 argument ``x``, returning inverse of ``x``
    - ``op`` -- function of 2 arguments ``x``, ``y``, returning ``x*y`` in the group
    - ``hash_function`` -- having an efficient hash function is critical
      for this algorithm (see examples)

    OUTPUT: integer `n` such that `a = base^n` (or `a = n*base`)

    ALGORITHM: Pollard rho for discrete logarithm, adapted from the
    article of Edlyn Teske, \'A space efficient algorithm for group
    structure computation\'.

    EXAMPLES::

        sage: F.<a> = GF(2^13)                                                          # needs sage.rings.finite_rings
        sage: g = F.gen()                                                               # needs sage.rings.finite_rings
        sage: discrete_log_rho(g^1234, g)                                               # needs sage.rings.finite_rings
        1234

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: F.<a> = GF(37^5)
        sage: E = EllipticCurve(F, [1,1])
        sage: G = (3*31*2^4)*E.lift_x(a)
        sage: discrete_log_rho(12345*G, G, ord=46591, operation=\'+\')
        12345

    It also works with matrices::

        sage: A = matrix(GF(50021), [[10577, 23999, 28893],                             # needs sage.modules sage.rings.finite_rings
        ....:                        [14601, 41019, 30188],
        ....:                        [3081, 736, 27092]])
        sage: discrete_log_rho(A^1234567, A)                                            # needs sage.modules sage.rings.finite_rings
        1234567

    Beware, the order must be prime::

        sage: I = IntegerModRing(171980)
        sage: discrete_log_rho(I(2), I(3))                                              # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: for Pollard rho algorithm the order of the group must be prime

    If it fails to find a suitable logarithm, it raises a :exc:`ValueError`::

        sage: I = IntegerModRing(171980)
        sage: discrete_log_rho(I(31002), I(15501))                                      # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: Pollard rho algorithm failed to find a logarithm

    The main limitation on the hash function is that we don\'t want to have
    ``hash(x*y) == hash(x) + hash(y)``::

        sage: # needs sage.libs.pari
        sage: I = IntegerModRing(next_prime(2^23))
        sage: def test():
        ....:     try:
        ....:          discrete_log_rho(I(123456), I(1), operation=\'+\')
        ....:     except Exception:
        ....:          print("FAILURE")
        sage: test()  # random failure
        FAILURE

    If this happens, we can provide a better hash function::

        sage: discrete_log_rho(I(123456), I(1), operation=\'+\',                          # needs sage.libs.pari
        ....:                  hash_function=lambda x: hash(x*x))
        123456

    AUTHOR:

    - Yann Laigle-Chapuy (2009-09-05)
    '''
def discrete_log(a, base, ord=None, bounds=None, operation: str = '*', identity=None, inverse=None, op=None, algorithm: str = 'bsgs', *, verify: bool = True):
    '''
    Totally generic discrete log function.

    INPUT:

    - ``a`` -- group element
    - ``base`` -- group element (the base)
    - ``ord`` -- integer (multiple of order of base, ``None``, or
      :mod:`oo <sage.rings.infinity>``); if this is
      :mod:`oo <sage.rings.infinity>`, then it explicitly does
      not use this, for example when factorizing the order is difficult
    - ``bounds`` -- a priori bounds on the log
    - ``operation`` -- string: ``\'*\'``, ``\'+\'``, other
    - ``identity`` -- the group\'s identity
    - ``inverse`` -- function of 1 argument ``x``, returning inverse of ``x``
    - ``op`` -- function of 2 arguments ``x``, ``y``, returning ``x*y`` in the group
    - ``algorithm`` -- string denoting what algorithm to use for prime-order
      logarithms: ``\'bsgs\'``, ``\'rho\'``, ``\'lambda\'``
    - ``verify`` -- boolean (default: ``True``); whether to verify that output is
      correct before returning it.

    ``a`` and ``base`` must be elements of some group with identity
    given by ``identity``, inverse of ``x`` by ``inverse(x)``, and group
    operation on ``x``, ``y`` by ``op(x,y)``.

    If operation is ``\'*\'`` or ``\'+\'``, then the other
    arguments are provided automatically; otherwise they must be
    provided by the caller.

    OUTPUT:

    This returns an integer `n` such that `b^n = a` (or `nb = a`),
    assuming that ``ord`` is a multiple of the order of the base `b`.
    If ``ord`` is not specified, an attempt is made to compute it.

    If no such `n` exists, this function raises a :exc:`ValueError` exception.

    .. WARNING::

       If ``x`` has a ``log`` method, it is likely to be vastly faster
       than using this function.  E.g., if ``x`` is an integer modulo
       `n`, use its ``log`` method instead!

    ALGORITHM: Pohlig-Hellman, Baby step giant step, Pollard\'s lambda/kangaroo, and Pollard\'s rho.

    EXAMPLES::

        sage: b = Mod(2,37);  a = b^20
        sage: discrete_log(a, b)
        20
        sage: b = Mod(3,2017);  a = b^20
        sage: discrete_log(a, b, bounds=(10, 100))
        20

        sage: # needs sage.rings.finite_rings
        sage: K = GF(3^6, \'b\')
        sage: b = K.gen()
        sage: a = b^210
        sage: discrete_log(a, b, K.order() - 1)
        210

        sage: b = Mod(1,37);  x = Mod(2,37)
        sage: discrete_log(x, b)
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of 2 found to base 1
        sage: b = Mod(1,997);  x = Mod(2,997)
        sage: discrete_log(x, b)
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of 2 found to base 1

    See :issue:`2356`::

        sage: F.<w> = GF(121)                                                           # needs sage.rings.finite_rings
        sage: v = w^120                                                                 # needs sage.rings.finite_rings
        sage: v.log(w)                                                                  # needs sage.rings.finite_rings
        0

        sage: K.<z> = CyclotomicField(230)                                              # needs sage.rings.number_field
        sage: w = z^50                                                                  # needs sage.rings.number_field
        sage: discrete_log(w, z)                                                        # needs sage.rings.number_field
        50

    An example where the order is infinite: note that we must give
    an upper bound here::

        sage: # needs sage.rings.number_field
        sage: K.<a> = QuadraticField(23)
        sage: eps = 5*a - 24        # a fundamental unit
        sage: eps.multiplicative_order()
        +Infinity
        sage: eta = eps^100
        sage: discrete_log(eta, eps, bounds=(0,1000))
        100

    In this case we cannot detect negative powers::

        sage: eta = eps^(-3)                                                            # needs sage.rings.number_field
        sage: discrete_log(eta,eps,bounds=(0,100))                                      # needs sage.rings.number_field
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of -11515*a - 55224 found to base 5*a - 24 with bounds (0, 100)

    But we can invert the base (and negate the result) instead::

        sage: -discrete_log(eta^-1, eps, bounds=(0,100))                                # needs sage.rings.number_field
        -3

    An additive example: elliptic curve DLOG::

        sage: # needs sage.libs.gap sage.rings.finite_rings sage.schemes
        sage: F = GF(37^2,\'a\')
        sage: E = EllipticCurve(F, [1,1])
        sage: F.<a> = GF(37^2,\'a\')
        sage: E = EllipticCurve(F, [1,1])
        sage: P = E(25*a + 16, 15*a + 7)
        sage: P.order()
        672
        sage: Q = 39*P; Q
        (36*a + 32 : 5*a + 12 : 1)
        sage: discrete_log(Q, P, P.order(), operation=\'+\')
        39

    An example of big smooth group::

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(2^63)
        sage: g = F.gen()
        sage: u = g**123456789
        sage: discrete_log(u,g)
        123456789

    The above examples also work when the ``\'rho\'`` and ``\'lambda\'`` algorithms are used::

        sage: b = Mod(2,37);  a = b^20
        sage: discrete_log(a, b, algorithm=\'rho\')
        20
        sage: b = Mod(3,2017);  a = b^20
        sage: discrete_log(a, b, algorithm=\'lambda\', bounds=(10, 100))
        20

        sage: # needs sage.rings.finite_rings
        sage: K = GF(3^6,\'b\')
        sage: b = K.gen()
        sage: a = b^210
        sage: discrete_log(a, b, K.order()-1, algorithm=\'rho\')
        210

        sage: b = Mod(1,37);  x = Mod(2,37)
        sage: discrete_log(x, b, algorithm=\'lambda\')
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of 2 found to base 1
        sage: b = Mod(1,997);  x = Mod(2,997)
        sage: discrete_log(x, b, algorithm=\'rho\')
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of 2 found to base 1

        sage: # needs sage.libs.gap sage.rings.finite_rings sage.schemes
        sage: F = GF(37^2,\'a\')
        sage: E = EllipticCurve(F, [1,1])
        sage: F.<a> = GF(37^2,\'a\')
        sage: E = EllipticCurve(F, [1,1])
        sage: P = E(25*a + 16, 15*a + 7)
        sage: P.order()
        672
        sage: Q = 39*P; Q
        (36*a + 32 : 5*a + 12 : 1)
        sage: discrete_log(Q, P, P.order(), operation=\'+\', algorithm=\'lambda\')
        39

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(2^63)
        sage: g = F.gen()
        sage: u = g**123456789
        sage: discrete_log(u, g, algorithm=\'rho\')
        123456789

    Pass ``ord=oo`` to avoid attempts to factorize the group order::

        sage: p, q = next_prime(2^128), next_prime(2^129)
        sage: a = mod(2, p*q*124+1)
        sage: discrete_log(a^100, a, bounds=(1, 500))  # not tested (takes very long, but pari.addprimes(p) makes it faster)
        sage: discrete_log(a^100, a, ord=oo, bounds=(1, 500))
        100

    TESTS:

    Random testing::

        sage: G = Zmod(randrange(1, 1000))
        sage: base = G.random_element()
        sage: order = choice([base.additive_order(), G.order()])
        sage: assert order.divides(G.cardinality())
        sage: sol = randrange(base.additive_order())
        sage: elem = sol * base
        sage: args = (elem, base, order)
        sage: kwargs = {\'operation\': \'+\'}
        sage: kwargs[\'algorithm\'] = choice([\'bsgs\', \'rho\', \'lambda\'])
        sage: if randrange(2):
        ....:     lo = randrange(-order, sol + 1)
        ....:     hi = randrange(sol + 1, 2*order)
        ....:     assert lo <= sol <= hi
        ....:     kwargs[\'bounds\'] = (lo, hi)
        sage: try:
        ....:     res = discrete_log(*args, **kwargs)
        ....: except ValueError:
        ....:     # lambda can fail randomly
        ....:     assert kwargs[\'algorithm\'] == \'lambda\'
        ....: else:
        ....:     assert res == sol

    Verify that :issue:`38316` is fixed::

        sage: F = GF(5)
        sage: base = F(3)
        sage: a = F(1)
        sage: discrete_log(a, base, bounds=(1,2), operation="*")
        Traceback (most recent call last):
        ...
        ValueError: no discrete log of 1 found to base 3 with bounds (1, 2)

    AUTHORS:

    - William Stein and David Joyner (2005-01-05)
    - John Cremona (2008-02-29) rewrite using ``dict()`` and make generic
    - Julien Grijalva (2022-08-09) rewrite to make more generic, more algorithm options, and more effective use of bounds
    '''
def discrete_log_generic(a, base, ord=None, bounds=None, operation: str = '*', identity=None, inverse=None, op=None, algorithm: str = 'bsgs'):
    """
    Alias for ``discrete_log``.
    """
def discrete_log_lambda(a, base, bounds, operation: str = '*', identity=None, inverse=None, op=None, hash_function=...):
    """
    Pollard Lambda algorithm for computing discrete logarithms. It uses
    only a logarithmic amount of memory. It's useful if you have
    bounds on the logarithm. If you are computing logarithms in a
    whole finite group, you should use Pollard Rho algorithm.

    INPUT:

    - ``a`` -- a group element
    - ``base`` -- a group element
    - ``bounds`` -- a couple (lb,ub) representing the range where we look for a logarithm
    - ``operation`` -- string: '+', '*' or 'other'
    - ``identity`` -- the identity element of the group
    - ``inverse`` -- function of 1 argument ``x`` returning inverse of ``x``
    - ``op`` -- function of 2 arguments ``x``, ``y`` returning ``x*y`` in the group
    - ``hash_function`` -- having an efficient hash function is critical for this algorithm

    OUTPUT: integer `n` such that `a=base^n` (or `a=n*base`)

    ALGORITHM: Pollard Lambda, if bounds are (lb,ub) it has time complexity
        O(sqrt(ub-lb)) and space complexity O(log(ub-lb))

    EXAMPLES::

        sage: F.<a> = GF(2^63)                                                          # needs sage.rings.finite_rings
        sage: discrete_log_lambda(a^1234567, a, (1200000,1250000))                      # needs sage.rings.finite_rings
        1234567

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: F.<a> = GF(37^5)
        sage: E = EllipticCurve(F, [1,1])
        sage: P = E.lift_x(a); P
        (a : 28*a^4 + 15*a^3 + 14*a^2 + 7 : 1)

    This will return a multiple of the order of P::

        sage: discrete_log_lambda(P.parent().zero(), P, Hasse_bounds(F.order()),            # needs sage.rings.finite_rings sage.schemes
        ....:                     operation='+')
        69327408

        sage: K.<a> = GF(89**5)                                                         # needs sage.rings.finite_rings
        sage: hs = lambda x: hash(x) + 15
        sage: discrete_log_lambda(a**(89**3 - 3),       # long time (10s on sage.math, 2011), needs sage.rings.finite_rings
        ....:                     a, (89**2, 89**4), operation='*', hash_function=hs)
        704966

    AUTHOR:

        -- Yann Laigle-Chapuy (2009-01-25)
    """
def linear_relation(P, Q, operation: str = '+', identity=None, inverse=None, op=None):
    """
    Function which solves the equation ``a*P=m*Q`` or ``P^a=Q^m``.

    Additive version: returns `(a,m)` with minimal `m>0` such that
    `aP=mQ`.  Special case: if `\\left<P\\right>` and `\\left<Q\\right>`
    intersect only in `\\{0\\}` then `(a,m)=(0,n)` where `n` is
    ``Q.additive_order()``.

    Multiplicative version: returns `(a,m)` with minimal `m>0` such
    that `P^a=Q^m`.  Special case: if `\\left<P\\right>` and
    `\\left<Q\\right>` intersect only in `\\{1\\}` then `(a,m)=(0,n)`
    where `n` is ``Q.multiplicative_order()``.

    ALGORITHM:

    Uses the generic ``bsgs()`` function, and so works in general
    finite abelian groups.

    EXAMPLES:

    An additive example (in an elliptic curve group)::

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: F.<a> = GF(3^6,'a')
        sage: E = EllipticCurve([a^5 + 2*a^3 + 2*a^2 + 2*a, a^4 + a^3 + 2*a + 1])
        sage: P = E(a^5 + a^4 + a^3 + a^2 + a + 2, 0)
        sage: Q = E(2*a^3 + 2*a^2 + 2*a, a^3 + 2*a^2 + 1)
        sage: linear_relation(P, Q, '+')
        (1, 2)
        sage: P == 2*Q
        True

    A multiplicative example (in a finite field's multiplicative group)::

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(3^6,'a')
        sage: a.multiplicative_order().factor()
        2^3 * 7 * 13
        sage: b = a^7
        sage: c = a^13
        sage: linear_relation(b, c, '*')
        (13, 7)
        sage: b^13 == c^7
        True
    """
def order_from_multiple(P, m, plist=None, factorization=None, check: bool = True, operation: str = '+', identity=None, inverse=None, op=None):
    """
    Generic function to find order of a group element given a multiple
    of its order.

    See :meth:`bsgs` for full explanation of the inputs.

    INPUT:

    - ``P`` -- a Sage object which is a group element
    - ``m`` -- Sage integer which is a multiple of the order of ``P``,
      i.e. we require that ``m*P=0`` (or ``P**m=1``)
    - ``check`` -- a Boolean (default: ``True``), indicating whether we check if ``m``
      really is a multiple of the order
    - ``factorization`` -- the factorization of ``m``, or ``None`` in which
      case this function will need to factor ``m``
    - ``plist`` -- list of the prime factors of ``m``, or ``None``. Kept for compatibility only,
      prefer the use of ``factorization``
    - ``operation`` -- string: ``'+'`` (default), ``'*'`` or ``None``
    - ``identity`` -- the identity element of the group
    - ``inverse`` -- function of 1 argument ``x``, returning inverse of ``x``
    - ``op`` -- function of 2 arguments ``x``, ``y`` returning ``x*y`` in the group

    .. NOTE::

        It is more efficient for the caller to factor ``m`` and cache
        the factors for subsequent calls.

    EXAMPLES::

        sage: from sage.groups.generic import order_from_multiple

        sage: # needs sage.rings.finite_rings
        sage: k.<a> = GF(5^5)
        sage: b = a^4
        sage: order_from_multiple(b, 5^5 - 1, operation='*')
        781

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: E = EllipticCurve(k, [2,4])
        sage: P = E(3*a^4 + 3*a, 2*a + 1)
        sage: M = E.cardinality(); M
        3227
        sage: F = M.factor()
        sage: order_from_multiple(P, M, factorization=F, operation='+')
        3227
        sage: Q = E(0,2)
        sage: order_from_multiple(Q, M, factorization=F, operation='+')
        7

        sage: # needs sage.rings.number_field
        sage: K.<z> = CyclotomicField(230)
        sage: w = z^50
        sage: order_from_multiple(w, 230, operation='*')
        23

        sage: # needs sage.modules sage.rings.finite_rings
        sage: F = GF(2^1279,'a')
        sage: n = F.cardinality() - 1  # Mersenne prime
        sage: order_from_multiple(F.random_element(), n,
        ....:                     factorization=[(n,1)], operation='*') == n
        True

        sage: # needs sage.rings.finite_rings
        sage: K.<a> = GF(3^60)
        sage: order_from_multiple(a, 3^60 - 1, operation='*', check=False)
        42391158275216203514294433200

    TESTS:

    Check that :issue:`38489` is fixed::

        sage: from sage.groups.generic import order_from_multiple
        sage: plist = [43, 257, 547, 881]
        sage: m = prod(plist[:-1])
        sage: elt = Zmod(m)(plist[-1])
        sage: order_from_multiple(elt, m, plist=plist)
        6044897
    """
def order_from_bounds(P, bounds, d=None, operation: str = '+', identity=None, inverse=None, op=None):
    """
    Generic function to find order of a group element, given only
    upper and lower bounds for a multiple of the order (e.g. bounds on
    the order of the group of which it is an element)

    INPUT:

    - ``P`` -- a Sage object which is a group element

    - ``bounds`` -- a 2-tuple ``(lb,ub)`` such that ``m*P=0`` (or
      ``P**m=1``) for some ``m`` with ``lb<=m<=ub``

    - ``d`` -- (optional) a positive integer; only ``m`` which are
      multiples of this will be considered

    - ``operation`` -- string; ``'+'`` (default) or ``'*'`` or other.
      If other, the following must be supplied:

      - ``identity`` -- the identity element for the group
      - ``inverse`` -- a function of one argument giving the inverse
        of a group element
      - ``op`` -- a function of 2 arguments defining the group binary
        operation

    .. NOTE::

       Typically ``lb`` and ``ub`` will be bounds on the group order,
       and from previous calculation we know that the group order is
       divisible by ``d``.

    EXAMPLES::

        sage: from sage.groups.generic import order_from_bounds

        sage: # needs sage.rings.finite_rings
        sage: k.<a> = GF(5^5)
        sage: b = a^4
        sage: order_from_bounds(b, (5^4, 5^5), operation='*')
        781

        sage: # needs sage.rings.finite_rings sage.schemes
        sage: E = EllipticCurve(k, [2,4])
        sage: P = E(3*a^4 + 3*a, 2*a + 1)
        sage: bounds = Hasse_bounds(5^5)
        sage: Q = E(0,2)
        sage: order_from_bounds(Q, bounds, operation='+')
        7
        sage: order_from_bounds(P, bounds, 7, operation='+')
        3227

        sage: # needs sage.rings.number_field
        sage: K.<z> = CyclotomicField(230)
        sage: w = z^50
        sage: order_from_bounds(w, (200, 250), operation='*')
        23
    """
def has_order(P, n, operation: str = '+') -> bool:
    """
    Generic function to test if a group element `P` has order
    exactly equal to a given positive integer `n`.

    INPUT:

    - ``P`` -- group element with respect to the specified ``operation``
    - ``n`` -- positive integer, or its :class:`~sage.structure.factorization.Factorization`
    - ``operation`` -- string, either ``'+'`` (default) or ``'*'``

    EXAMPLES::

        sage: from sage.groups.generic import has_order
        sage: E.<P> = EllipticCurve(GF(71), [5,5])
        sage: P.order()
        57
        sage: has_order(P, 57)
        True
        sage: has_order(P, factor(57))
        True
        sage: has_order(P, 19)
        False
        sage: has_order(3*P, 19)
        True
        sage: has_order(3*P, 57)
        False

    ::

        sage: R = Zmod(14981)
        sage: g = R(321)
        sage: g.multiplicative_order()
        42
        sage: has_order(g, 42, operation='*')
        True
        sage: has_order(g, factor(42), operation='*')
        True
        sage: has_order(g, 70, operation='*')
        False

    TESTS::

        sage: ns = [randrange(1,10**5) for _ in range(randrange(1,5))]
        sage: A = AdditiveAbelianGroup(ns)
        sage: from sage.groups.generic import has_order
        sage: el = A.random_element()
        sage: o = el.order()
        sage: has_order(el, o)
        True
        sage: has_order(el, o.factor())
        True
        sage: not_o = ZZ(randrange(100*o))
        sage: not_o += (not_o == o)
        sage: has_order(el, not_o)
        False

    Check for :issue:`37102`::

        sage: from sage.groups.generic import has_order
        sage: x = Mod(9, 24)
        sage: has_order(x, 0)
        False
        sage: has_order(x, -8)
        False

    Check for :issue:`38708`::

        sage: has_order(Mod(2,3), int(2), operation='*')
        True

    .. NOTE::

        In some cases, order *testing* can be much faster than
        *computing* the order using :func:`order_from_multiple`.
    """
def merge_points(P1, P2, operation: str = '+', identity=None, inverse=None, op=None, check: bool = True):
    """
    Return a group element whose order is the lcm of the given elements.

    INPUT:

    - ``P1`` -- a pair `(g_1,n_1)` where `g_1` is a group element of order `n_1`
    - ``P2`` -- a pair `(g_2,n_2)` where `g_2` is a group element of order `n_2`
    - ``operation`` -- string; ``'+'`` (default) or ``'*'`` or other. If
      other, the following must be supplied:

      - ``identity`` -- the identity element for the group
      - ``inverse`` -- a function of one argument giving the inverse
        of a group element
      - ``op`` -- a function of 2 arguments defining the group
        binary operation

    OUTPUT: a pair `(g_3,n_3)` where `g_3` has order `n_3=\\hbox{lcm}(n_1,n_2)`

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.groups.generic import merge_points
        sage: F.<a> = GF(3^6,'a')
        sage: b = a^7
        sage: c = a^13
        sage: ob = (3^6-1)//7
        sage: oc = (3^6-1)//13
        sage: merge_points((b,ob), (c,oc), operation='*')
        (a^4 + 2*a^3 + 2*a^2, 728)
        sage: d, od = merge_points((b,ob), (c,oc), operation='*')
        sage: od == d.multiplicative_order()
        True
        sage: od == lcm(ob, oc)
        True

        sage: # needs sage.libs.gap sage.rings.finite_rings sage.schemes
        sage: E = EllipticCurve([a^5 + 2*a^3 + 2*a^2 + 2*a, a^4 + a^3 + 2*a + 1])
        sage: P = E(2*a^5 + 2*a^4 + a^3 + 2, a^4 + a^3 + a^2 + 2*a + 2)
        sage: P.order()
        7
        sage: Q = E(2*a^5 + 2*a^4 + 1, a^5 + 2*a^3 + 2*a + 2)
        sage: Q.order()
        4
        sage: R, m = merge_points((P,7), (Q,4), operation='+')
        sage: R.order() == m
        True
        sage: m == lcm(7,4)
        True
    """
def structure_description(G, latex: bool = False):
    """
    Return a string that tries to describe the structure of ``G``.

    This methods wraps GAP's ``StructureDescription`` method.

    For full details, including the form of the returned string and the
    algorithm to build it, see :gap:`GAP's documentation <chap39>`.

    INPUT:

    - ``latex`` -- boolean (default: ``False``); if ``True``, return a
      LaTeX formatted string

    OUTPUT: string

    .. WARNING::

        From GAP's documentation: The string returned by
        ``StructureDescription`` is **not** an isomorphism invariant:
        non-isomorphic groups can have the same string value, and two
        isomorphic groups in different representations can produce different
        strings.

    EXAMPLES::

        sage: # needs sage.groups
        sage: G = CyclicPermutationGroup(6)
        sage: G.structure_description()
        'C6'
        sage: G.structure_description(latex=True)
        'C_{6}'
        sage: G2 = G.direct_product(G, maps=False)
        sage: LatexExpr(G2.structure_description(latex=True))
        C_{6} \\times C_{6}

    This method is mainly intended for small groups or groups with few
    normal subgroups. Even then there are some surprises::

        sage: D3 = DihedralGroup(3)                                                     # needs sage.groups
        sage: D3.structure_description()                                                # needs sage.groups
        'S3'

    We use the Sage notation for the degree of dihedral groups::

        sage: D4 = DihedralGroup(4)                                                     # needs sage.groups
        sage: D4.structure_description()                                                # needs sage.groups
        'D4'

    Works for finitely presented groups (:issue:`17573`)::

        sage: F.<x, y> = FreeGroup()                                                    # needs sage.groups
        sage: G = F / [x^2*y^-1, x^3*y^2, x*y*x^-1*y^-1]                                # needs sage.groups
        sage: G.structure_description()                                                 # needs sage.groups
        'C7'

    And matrix groups (:issue:`17573`)::

        sage: groups.matrix.GL(4,2).structure_description()                             # needs sage.libs.gap sage.modules
        'A8'
    """
