r"""
Algebraic numbers

This module implements the algebraic numbers (the complex
numbers which are the zero of a polynomial in `\ZZ[x]`; in other
words, the algebraic closure of `\QQ`, with an embedding into `\CC`).
All computations are exact. We also include an implementation of the
algebraic reals (the intersection of the algebraic numbers with
`\RR`). The field of algebraic numbers `\QQbar` is available with
abbreviation ``QQbar``; the field of algebraic reals has abbreviation
``AA``.

As with many other implementations of the algebraic numbers, we try
hard to avoid computing a number field and working in the number
field; instead, we use floating-point interval arithmetic whenever
possible (basically whenever we need to prove non-equalities), and
resort to symbolic computation only as needed (basically to prove
equalities).

Algebraic numbers exist in one of the following forms:

- a rational number

- the sum, difference, product, or quotient of algebraic numbers

- the negation, inverse, absolute value, norm, real part,
  imaginary part, or complex conjugate of an algebraic number

- a particular root of a polynomial, given as a polynomial with
  algebraic coefficients together with an isolating interval (given as
  a ``RealIntervalFieldElement``) which encloses exactly one root, and
  the multiplicity of the root

- a polynomial in one generator, where the generator is an algebraic
  number given as the root of an irreducible polynomial with integral
  coefficients and the polynomial is given as a
  ``NumberFieldElement``.

An algebraic number can be coerced into ``ComplexIntervalField`` (or
``RealIntervalField``, for algebraic reals); every algebraic number has a
cached interval of the highest precision yet calculated.

In most cases, computations that need to compare two algebraic numbers
compute them with 128-bit precision intervals; if this does not suffice to
prove that the numbers are different, then we fall back on exact
computation.

Note that division involves an implicit comparison of the divisor against
zero, and may thus trigger exact computation.

Also, using an algebraic number in the leading coefficient of
a polynomial also involves an implicit comparison against zero, which
again may trigger exact computation.

Note that we work fairly hard to avoid computing new number fields;
to help, we keep a lattice of already-computed number fields and
their inclusions.

EXAMPLES::

    sage: sqrt(AA(2)) > 0
    True
    sage: (sqrt(5 + 2*sqrt(QQbar(6))) - sqrt(QQbar(3)))^2 == 2
    True
    sage: AA((sqrt(5 + 2*sqrt(6)) - sqrt(3))^2) == 2                                    # needs sage.symbolic
    True

For a monic cubic polynomial `x^3 + bx^2 + cx + d` with roots `s1`,
`s2`, `s3`, the discriminant is defined as
`(s1-s2)^2(s1-s3)^2(s2-s3)^2` and can be computed as `b^2c^2 - 4b^3d -
4c^3 + 18bcd - 27d^2`. We can test that these definitions do give the
same result::

    sage: def disc1(b, c, d):
    ....:     return b^2*c^2 - 4*b^3*d - 4*c^3 + 18*b*c*d - 27*d^2
    sage: def disc2(s1, s2, s3):
    ....:     return ((s1-s2)*(s1-s3)*(s2-s3))^2
    sage: x = polygen(AA)
    sage: p = x*(x-2)*(x-4)
    sage: cp = AA.common_polynomial(p)
    sage: d, c, b, _ = p.list()
    sage: s1 = AA.polynomial_root(cp, RIF(-1, 1))
    sage: s2 = AA.polynomial_root(cp, RIF(1, 3))
    sage: s3 = AA.polynomial_root(cp, RIF(3, 5))
    sage: disc1(b, c, d) == disc2(s1, s2, s3)
    True
    sage: p = p + 1
    sage: cp = AA.common_polynomial(p)
    sage: d, c, b, _ = p.list()
    sage: s1 = AA.polynomial_root(cp, RIF(-1, 1))
    sage: s2 = AA.polynomial_root(cp, RIF(1, 3))
    sage: s3 = AA.polynomial_root(cp, RIF(3, 5))
    sage: disc1(b, c, d) == disc2(s1, s2, s3)
    True
    sage: p = (x-sqrt(AA(2)))*(x-AA(2).nth_root(3))*(x-sqrt(AA(3)))
    sage: cp = AA.common_polynomial(p)
    sage: d, c, b, _ = p.list()
    sage: s1 = AA.polynomial_root(cp, RIF(1.4, 1.5))
    sage: s2 = AA.polynomial_root(cp, RIF(1.7, 1.8))
    sage: s3 = AA.polynomial_root(cp, RIF(1.2, 1.3))
    sage: disc1(b, c, d) == disc2(s1, s2, s3)
    True

We can convert from symbolic expressions::

    sage: # needs sage.symbolic
    sage: QQbar(sqrt(-5))
    2.236067977499790?*I
    sage: AA(sqrt(2) + sqrt(3))
    3.146264369941973?
    sage: QQbar(I)
    I
    sage: QQbar(I * golden_ratio)
    1.618033988749895?*I
    sage: AA(golden_ratio)^2 - AA(golden_ratio)
    1
    sage: QQbar((-8)^(1/3))
    1.000000000000000? + 1.732050807568878?*I
    sage: AA((-8)^(1/3))
    -2
    sage: QQbar((-4)^(1/4))
    1 + 1*I
    sage: AA((-4)^(1/4))
    Traceback (most recent call last):
    ...
    ValueError: Cannot coerce algebraic number with nonzero imaginary part to algebraic real

The coercion, however, goes in the other direction, since not all
symbolic expressions are algebraic numbers::

    sage: QQbar(sqrt(2)) + sqrt(3)                                                      # needs sage.symbolic
    sqrt(3) + 1.414213562373095?
    sage: QQbar(sqrt(2) + QQbar(sqrt(3)))                                               # needs sage.symbolic
    3.146264369941973?

Note the different behavior in taking roots: for ``AA`` we prefer real
roots if they exist, but for ``QQbar`` we take the principal root::

    sage: AA(-1)^(1/3)
    -1
    sage: QQbar(-1)^(1/3)
    0.500000000000000? + 0.866025403784439?*I

However, implicit coercion from `\QQ[I]` is only allowed when it is equipped
with a complex embedding::

    sage: i.parent()
    Number Field in I with defining polynomial x^2 + 1 with I = 1*I
    sage: QQbar(1) + i
    I + 1

    sage: K.<im> = QuadraticField(-1, embedding=None)
    sage: QQbar(1) + im
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for +: 'Algebraic Field' and
    'Number Field in im with defining polynomial x^2 + 1'

However, we can explicitly coerce from the abstract number field `\QQ[I]`.
(Technically, this is not quite kosher, since we do not know whether the field
generator is supposed to map to `+I` or `-I`. We assume that for any quadratic
field with polynomial `x^2+1`, the generator maps to `+I`.)::

    sage: pythag = QQbar(3/5 + 4*im/5); pythag
    4/5*I + 3/5
    sage: pythag.abs() == 1
    True

We can implicitly coerce from algebraic reals to algebraic numbers::

    sage: a = QQbar(1); a, a.parent()
    (1, Algebraic Field)
    sage: b = AA(1); b, b.parent()
    (1, Algebraic Real Field)
    sage: c = a + b; c, c.parent()
    (2, Algebraic Field)

Some computation with radicals::

    sage: phi = (1 + sqrt(AA(5))) / 2
    sage: phi^2 == phi + 1
    True
    sage: tau = (1 - sqrt(AA(5))) / 2
    sage: tau^2 == tau + 1
    True
    sage: phi + tau == 1
    True
    sage: tau < 0
    True

    sage: rt23 = sqrt(AA(2/3))
    sage: rt35 = sqrt(AA(3/5))
    sage: rt25 = sqrt(AA(2/5))
    sage: rt23 * rt35 == rt25
    True

The Sage rings ``AA`` and ``QQbar`` can decide equalities between radical
expressions (over the reals and complex numbers respectively)::

    sage: a = AA((2/(3*sqrt(3)) + 10/27)^(1/3)                                          # needs sage.symbolic
    ....:        - 2/(9*(2/(3*sqrt(3)) + 10/27)^(1/3)) + 1/3)
    sage: a                                                                             # needs sage.symbolic
    1.000000000000000?
    sage: a == 1                                                                        # needs sage.symbolic
    True

Algebraic numbers which are known to be rational print as rationals;
otherwise they print as intervals (with 53-bit precision)::

    sage: AA(2)/3
    2/3
    sage: QQbar(5/7)
    5/7
    sage: QQbar(1/3 - 1/4*I)
    -1/4*I + 1/3
    sage: two = QQbar(4).nth_root(4)^2; two
    2.000000000000000?
    sage: two == 2; two
    True
    2
    sage: phi
    1.618033988749895?

We can find the real and imaginary parts of an algebraic number (exactly)::

    sage: r = QQbar.polynomial_root(x^5 - x - 1, CIF(RIF(0.1, 0.2), RIF(1.0, 1.1))); r
    0.1812324444698754? + 1.083954101317711?*I
    sage: r.real()
    0.1812324444698754?
    sage: r.imag()
    1.083954101317711?
    sage: r.minpoly()
    x^5 - x - 1
    sage: r.real().minpoly()
    x^10 + 3/16*x^6 + 11/32*x^5 - 1/64*x^2 + 1/128*x - 1/1024
    sage: r.imag().minpoly()  # long time (10s on sage.math, 2013)
    x^20 - 5/8*x^16 - 95/256*x^12 - 625/1024*x^10 - 5/512*x^8 - 1875/8192*x^6 + 25/4096*x^4 - 625/32768*x^2 + 2869/1048576

We can find the absolute value and norm of an algebraic number exactly.
(Note that we define the norm as the product of a number and its
complex conjugate; this is the algebraic definition of norm, if we
view ``QQbar`` as ``AA[I]``.)::

    sage: R.<x> = QQ[]
    sage: r = (x^3 + 8).roots(QQbar, multiplicities=False)[2]; r
    1.000000000000000? + 1.732050807568878?*I
    sage: r.abs() == 2
    True
    sage: r.norm() == 4
    True
    sage: (r+QQbar(I)).norm().minpoly()
    x^2 - 10*x + 13
    sage: r = AA.polynomial_root(x^2 - x - 1, RIF(-1, 0)); r
    -0.618033988749895?
    sage: r.abs().minpoly()
    x^2 + x - 1

We can compute the multiplicative order of an algebraic number::

    sage: QQbar(-1/2 + I*sqrt(3)/2).multiplicative_order()                              # needs sage.symbolic
    3
    sage: QQbar(-sqrt(3)/2 + I/2).multiplicative_order()                                # needs sage.symbolic
    12
    sage: (QQbar.zeta(23)**5).multiplicative_order()
    23

The paper "ARPREC: An Arbitrary Precision Computation Package" by
Bailey, Yozo, Li and Thompson discusses this result. Evidently it is
difficult to find, but we can easily verify it. ::

    sage: alpha = QQbar.polynomial_root(x^10 + x^9 - x^7 - x^6
    ....:                                - x^5 - x^4 - x^3 + x + 1, RIF(1, 1.2))
    sage: lhs = alpha^630 - 1
    sage: rhs_num = (alpha^315 - 1) * (alpha^210 - 1) * (alpha^126 - 1)^2 * (alpha^90 - 1) * (alpha^3 - 1)^3 * (alpha^2 - 1)^5 * (alpha - 1)^3
    sage: rhs_den = (alpha^35 - 1) * (alpha^15 - 1)^2 * (alpha^14 - 1)^2 * (alpha^5 - 1)^6 * alpha^68
    sage: rhs = rhs_num / rhs_den
    sage: lhs
    2.642040335819351?e44
    sage: rhs
    2.642040335819351?e44
    sage: lhs - rhs
    0.?e29
    sage: lhs == rhs
    True
    sage: lhs - rhs
    0
    sage: lhs._exact_value()
    -10648699402510886229334132989629606002223831*a^9 + 23174560249100286133718183712802529035435800*a^8 - 27259790692625442252605558473646959458901265*a^7 + 21416469499004652376912957054411004410158065*a^6 - 14543082864016871805545108986578337637140321*a^5 + 6458050008796664339372667222902512216589785*a^4 + 3052219053800078449122081871454923124998263*a^3 - 14238966128623353681821644902045640915516176*a^2 + 16749022728952328254673732618939204392161001*a - 9052854758155114957837247156588012516273410 where a^10 - a^9 + a^7 - a^6 + a^5 - a^4 + a^3 - a + 1 = 0 and a in -1.176280818259918?

Given an algebraic number, we can produce a string that will reproduce
that algebraic number if you type the string into Sage. We can see
that until exact computation is triggered, an algebraic number keeps
track of the computation steps used to produce that number::

    sage: rt2 = AA(sqrt(2))
    sage: rt3 = AA(sqrt(3))
    sage: n = (rt2 + rt3)^5; n
    308.3018001722975?
    sage: sage_input(n)
    R.<x> = AA[]
    v1 = AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951))) + AA.polynomial_root(AA.common_polynomial(x^2 - 3), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))
    v2 = v1*v1
    v2*v2*v1

But once exact computation is triggered, the computation tree is discarded,
and we get a way to produce the number directly::

    sage: n == 109*rt2 + 89*rt3
    True
    sage: sage_input(n)
    R.<y> = QQ[]
    v = AA.polynomial_root(AA.common_polynomial(y^4 - 4*y^2 + 1), RIF(-RR(1.9318516525781366), -RR(1.9318516525781364)))
    -109*v^3 + 89*v^2 + 327*v - 178

We can also see that some computations (basically, those which are
easy to perform exactly) are performed directly, instead of storing
the computation tree::

    sage: z3_3 = QQbar.zeta(3) * 3
    sage: z4_4 = QQbar.zeta(4) * 4
    sage: z5_5 = QQbar.zeta(5) * 5
    sage: sage_input(z3_3 * z4_4 * z5_5)
    R.<y> = QQ[]
    3*QQbar.polynomial_root(AA.common_polynomial(y^2 + y + 1), CIF(RIF(-RR(0.50000000000000011), -RR(0.49999999999999994)), RIF(RR(0.8660254037844386), RR(0.86602540378443871))))*QQbar(4*I)*(5*QQbar.polynomial_root(AA.common_polynomial(y^4 + y^3 + y^2 + y + 1), CIF(RIF(RR(0.3090169943749474), RR(0.30901699437494745)), RIF(RR(0.95105651629515353), RR(0.95105651629515364)))))

Note that the ``verify=True`` argument to ``sage_input`` will always trigger
exact computation, so running ``sage_input`` twice in a row on the same number
will actually give different answers. In the following, running ``sage_input``
on ``n`` will also trigger exact computation on ``rt2``, as you can see by the
fact that the third output is different than the first::

    sage: # needs sage.symbolic
    sage: rt2 = AA(sqrt(2))
    sage: n = rt2^2
    sage: sage_input(n, verify=True)
    # Verified
    R.<x> = AA[]
    v = AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
    v*v
    sage: sage_input(n, verify=True)
    # Verified
    AA(2)
    sage: n = rt2^2
    sage: sage_input(n, verify=True)
    # Verified
    AA(2)

Just for fun, let's try ``sage_input`` on a very complicated expression. The
output of this example changed with the rewriting of polynomial multiplication
algorithms in :issue:`10255`::

    sage: rt2 = sqrt(AA(2))
    sage: rt3 = sqrt(QQbar(3))
    sage: x = polygen(QQbar)
    sage: nrt3 = AA.polynomial_root((x-rt2)*(x+rt3), RIF(-2, -1))
    sage: one = AA.polynomial_root((x-rt2)*(x-rt3)*(x-nrt3)*(x-1-rt3-nrt3), RIF(0.9, 1.1))
    sage: one
    1.000000000000000?
    sage: sage_input(one, verify=True)
    # Verified
    R1.<x> = QQbar[]
    R2.<y> = QQ[]
    v = AA.polynomial_root(AA.common_polynomial(y^4 - 4*y^2 + 1), RIF(-RR(1.9318516525781366), -RR(1.9318516525781364)))
    AA.polynomial_root(AA.common_polynomial(x^4 + QQbar(v^3 - 3*v - 1)*x^3 + QQbar(-v^3 + 3*v - 3)*x^2 + QQbar(-3*v^3 + 9*v + 3)*x + QQbar(3*v^3 - 9*v)), RIF(RR(0.99999999999999989), RR(1.0000000000000002)))
    sage: one
    1

We can pickle and unpickle algebraic fields (and they are globally unique)::

    sage: loads(dumps(AlgebraicField())) is AlgebraicField()
    True
    sage: loads(dumps(AlgebraicRealField())) is AlgebraicRealField()
    True

We can pickle and unpickle algebraic numbers::

    sage: loads(dumps(QQbar(10))) == QQbar(10)
    True
    sage: loads(dumps(QQbar(5/2))) == QQbar(5/2)
    True
    sage: loads(dumps(QQbar.zeta(5))) == QQbar.zeta(5)
    True

    sage: # needs sage.symbolic
    sage: t = QQbar(sqrt(2)); type(t._descr)
    <class 'sage.rings.qqbar.ANRoot'>
    sage: loads(dumps(t)) == QQbar(sqrt(2))
    True
    sage: t.exactify(); type(t._descr)
    <class 'sage.rings.qqbar.ANExtensionElement'>
    sage: loads(dumps(t)) == QQbar(sqrt(2))
    True
    sage: t = ~QQbar(sqrt(2)); type(t._descr)
    <class 'sage.rings.qqbar.ANUnaryExpr'>
    sage: loads(dumps(t)) == 1/QQbar(sqrt(2))
    True
    sage: t = QQbar(sqrt(2)) + QQbar(sqrt(3)); type(t._descr)
    <class 'sage.rings.qqbar.ANBinaryExpr'>
    sage: loads(dumps(t)) == QQbar(sqrt(2)) + QQbar(sqrt(3))
    True

We can convert elements of ``QQbar`` and ``AA`` into the following
types: ``float``, ``complex``, ``RDF``, ``CDF``, ``RR``, ``CC``,
``RIF``, ``CIF``, ``ZZ``, and ``QQ``, with a few exceptions. (For the
arbitrary-precision types, ``RR``, ``CC``, ``RIF``, and ``CIF``, it
can convert into a field of arbitrary precision.)

Converting from ``QQbar`` to a real type (``float``, ``RDF``, ``RR``,
``RIF``, ``ZZ``, or ``QQ``) succeeds only if the ``QQbar`` is actually
real (has an imaginary component of exactly zero). Converting from
either ``AA`` or ``QQbar`` to ``ZZ`` or ``QQ`` succeeds only if the
number actually is an integer or rational. If conversion fails, a
:exc:`ValueError` will be raised.

Here are examples of all of these conversions::

    sage: # needs sage.symbolic
    sage: all_vals = [AA(42), AA(22/7), AA(golden_ratio),
    ....:             QQbar(-13), QQbar(89/55), QQbar(-sqrt(7)), QQbar.zeta(5)]
    sage: def convert_test_all(ty):
    ....:     def convert_test(v):
    ....:         try:
    ....:             return ty(v)
    ....:         except (TypeError, ValueError):
    ....:             return None
    ....:     return [convert_test(_) for _ in all_vals]
    sage: convert_test_all(float)
    [42.0, 3.1428571428571432, 1.618033988749895, -13.0, 1.6181818181818182, -2.6457513110645907, None]
    sage: convert_test_all(complex)
    [(42+0j), (3.1428571428571432+0j), (1.618033988749895+0j), (-13+0j), (1.6181818181818182+0j), (-2.6457513110645907+0j), (0.30901699437494745+0.9510565162951536j)]
    sage: convert_test_all(RDF)
    [42.0, 3.1428571428571432, 1.618033988749895, -13.0, 1.6181818181818182, -2.6457513110645907, None]
    sage: convert_test_all(CDF)
    [42.0, 3.1428571428571432, 1.618033988749895, -13.0, 1.6181818181818182, -2.6457513110645907, 0.30901699437494745 + 0.9510565162951536*I]
    sage: convert_test_all(RR)
    [42.0000000000000, 3.14285714285714, 1.61803398874989, -13.0000000000000, 1.61818181818182, -2.64575131106459, None]
    sage: convert_test_all(CC)
    [42.0000000000000, 3.14285714285714, 1.61803398874989, -13.0000000000000, 1.61818181818182, -2.64575131106459, 0.309016994374947 + 0.951056516295154*I]
    sage: convert_test_all(RIF)
    [42, 3.142857142857143?, 1.618033988749895?, -13, 1.618181818181819?, -2.645751311064591?, None]
    sage: convert_test_all(CIF)
    [42, 3.142857142857143?, 1.618033988749895?, -13, 1.618181818181819?, -2.645751311064591?, 0.3090169943749474? + 0.9510565162951536?*I]
    sage: convert_test_all(ZZ)
    [42, None, None, -13, None, None, None]
    sage: convert_test_all(QQ)
    [42, 22/7, None, -13, 89/55, None, None]

Compute the exact coordinates of a 34-gon (the formulas used are from
Weisstein, Eric W. "Trigonometry Angles--Pi/17." and can be found at
http://mathworld.wolfram.com/TrigonometryAnglesPi17.html)::

    sage: rt17 = AA(17).sqrt()
    sage: rt2 = AA(2).sqrt()
    sage: eps = (17 + rt17).sqrt()
    sage: epss = (17 - rt17).sqrt()
    sage: delta = rt17 - 1
    sage: alpha = (34 + 6*rt17 + rt2*delta*epss - 8*rt2*eps).sqrt()
    sage: beta = 2*(17 + 3*rt17 - 2*rt2*eps - rt2*epss).sqrt()
    sage: x = rt2*(15 + rt17 + rt2*(alpha + epss)).sqrt()/8
    sage: y = rt2*(epss**2 - rt2*(alpha + epss)).sqrt()/8

    sage: cx, cy = 1, 0
    sage: for i in range(34):
    ....:    cx, cy = x*cx-y*cy, x*cy+y*cx
    sage: cx
    1.000000000000000?
    sage: cy
    0.?e-15

    sage: ax = polygen(AA)
    sage: x2 = AA.polynomial_root(256*ax**8 - 128*ax**7 - 448*ax**6 + 192*ax**5
    ....:                          + 240*ax**4 - 80*ax**3 - 40*ax**2 + 8*ax + 1,
    ....:                         RIF(0.9829, 0.983))
    sage: y2 = (1 - x2**2).sqrt()
    sage: x - x2
    0.?e-18
    sage: y - y2
    0.?e-17

Ideally, in the above example we should be able to test ``x == x2`` and ``y ==
y2`` but this is currently infinitely long.

TESTS:

Verify that :issue:`10981` is fixed::

    sage: x = AA['x'].gen()
    sage: P = 1/(1+x^4)
    sage: P.partial_fraction_decomposition()
    (0, [(-0.3535533905932738?*x + 1/2)/(x^2 - 1.414213562373095?*x + 1),
         (0.3535533905932738?*x + 1/2)/(x^2 + 1.414213562373095?*x + 1)])

Check that :issue:`22202` is fixed::

    sage: R1.<x> = AA[]; R2.<s> = QQbar[]
    sage: v = QQbar.polynomial_root(x^2 - x + 1, CIF(0.5, RIF(-0.87, -0.85)))
    sage: a = QQbar.polynomial_root((-4*v + 2)*s + (v - 1/2), CIF(RIF(0.24, 0.26), RIF(0)))
    sage: QQ(a)
    1/4

This example from :issue:`17896` should run in reasonable time, see also
:issue:`15600`::

    sage: x,y = polygens(QQ,"x,y")
    sage: p1 = x^5 + 6*x^4 - 42*x^3 - 142*x^2 + 467*x + 422
    sage: p2 = p1(x=(x-1)^2)
    sage: p3 = p2(x=x*y).resultant(p2,x).univariate_polynomial()
    sage: p4, = [f[0] for f in p3.factor() if f[0].degree() == 80]
    sage: ival = CIF((0.77, 0.78), (-0.08, -0.07))
    sage: z, = [r for r in p4.roots(QQbar, False) if r in ival]
    sage: z.exactify()

Check that :issue:`17895` is fixed. We check that ``polynomial_root``
runs under 5 seconds (used to take ~40sec)::

    sage: x,y = polygens(QQ,"x,y")
    sage: p1 = x^5 + 6*x^4 - 42*x^3 - 142*x^2 + 467*x + 422
    sage: p2 = p1(x=(x-1)^2)
    sage: p3 = p2(x=x*y).resultant(p2,x).univariate_polynomial()
    sage: p4, = [f[0] for f in p3.factor() if f[0].degree() == 80]
    sage: ival = CIF((0.77, 0.78), (-0.08, -0.07))
    sage: alarm(5.0)
    sage: z2 = QQbar.polynomial_root(p4, ival)
    sage: cancel_alarm()

Check that :issue:`28530` is fixed::

    sage: x = polygen(QQ)
    sage: K.<a> = NumberField(x^2 - x - 6256320, embedding=-2500.763730596996)
    sage: y = polygen(K)
    sage: lc = (253699680440307500000000000000000000000000*y^13 +
    ....: (-82964409970750000000000000000000000*a - 253907049983029389625000000000000000000000)*y^12 -
    ....: 1269011504560040442911087500000000000000000*y^11 +
    ....: (414989843657644100408750000000000000*a + 1270048771674262724340059170625000000000000)*y^10 +
    ....: 2539049473271641600616704837811000000000000*y^9 +
    ....: (-830315359762894607374452813100000000*a - 2541124846513368955687837282617343450000000)*y^8 -
    ....: 2540076196857756969319550626460768394380000*y^7 +
    ....: (830651117050319162421733536395645998*a + 2542152409324824242066023749434989311552001)*y^6 +
    ....: 1270551589939213408433336739488536788760000*y^5 +
    ....: (-415493479588780904355108633491291996*a - 1271590115891445566303772333517948273104002)*y^4 -
    ....: 254213042233365096819403450838768394380000*y^3 +
    ....: (83132288614462248899077910195645998*a + 254420831388756945210526696075302411552001)*y^2)
    sage: lc = lc.change_ring(QQbar)
    sage: lc.roots(CIF)
    [(-1.000505492239?, 2),
     (-1.000000000000?, 2),
     (-0.999999999662605?, 1),
     (0, 2),
     (1.000000000000?, 2),
     (1.000505492239?, 2),
     (0.999999587? + 0.?e-11*I, 1),
     (0.999999999? + 0.?e-11*I, 1)]

Check that issue:`37927` is fixed::

    sage: y = polygen(QQ, 'y')
    sage: v1 = QQbar.polynomial_root(y**2 + 1, CIF(0, -1))
    sage: v2 = -QQbar(2).sqrt()
    sage: M = matrix(QQbar, [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    ....:              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ....:              [-4, 2*v1, 1, 64, -32*v1, -16, 8*v1, 4, -2*v1, -1],
    ....:              [4*v1, 1, 0, -192*v1, -80, 32*v1, 12, -4*v1, -1, 0],
    ....:               [2, 0, 0, -480, 160*v1, 48, -12*v1, -2, 0, 0],
    ....:               [-4, 2*I, 1, 64, -32*I, -16, 8*I, 4, -2*I, -1],
    ....:               [4*I, 1, 0, -192*I, -80, 32*I, 12, -4*I, -1, 0],
    ....:               [2, 0, 0, -480, 160*I, 48, -12*I, -2, 0, 0],
    ....:               [0, 0, 0, 8, 4*v2, 4, 2*v2, 2, v2, 1],
    ....:               [0, 0, 0, 24*v2, 20, 8*v2, 6, 2*v2, 1, 0],
    ....:               [0, 0, 0, 8, 4*v2, 4, 2*v2, 2, -v2, 1],
    ....:               [0, 0, 0, 24*v2, 20, 8*v2, 6, 2*v2, 1, 0],
    ....:               [0, 0, 0, -4096, -1024*I, 256, 64*I, -16, -4*I, 1],
    ....:               [0, 0, 0, -4096, 1024*I, 256, -64*I, -16, 4*I, 1]])
    sage: M.right_kernel_matrix()
    [   1.000000000000000? + 0.?e-16*I                                 0                                 0 -0.00925925925925926? + 0.?e-19*I               0.?e-35 + 0.?e-18*I -0.11111111111111111? + 0.?e-18*I               0.?e-34 + 0.?e-17*I   0.5555555555555555? + 0.?e-16*I                                 0  -0.5925925925925926? + 0.?e-17*I]

AUTHOR:

- Carl Witty (2007-01-27): initial version
- Carl Witty (2007-10-29): massive rewrite to support complex as well as real numbers
"""
import sage
import sage.rings.abc
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import factor as factor
from sage.categories.action import Action as Action
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import Singleton as Singleton
from sage.misc.lazy_string import lazy_string as lazy_string
from sage.misc.misc import increase_recursion_limit as increase_recursion_limit
from sage.rings import infinity as infinity
from sage.rings.cc import CC as CC
from sage.rings.cif import CIF as CIF
from sage.rings.complex_interval import ComplexIntervalFieldElement as ComplexIntervalFieldElement
from sage.rings.complex_interval_field import ComplexIntervalField as ComplexIntervalField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field import CyclotomicField as CyclotomicField, GaussianField as GaussianField, NumberField as NumberField
from sage.rings.number_field.number_field_element_quadratic import NumberFieldElement_gaussian as NumberFieldElement_gaussian
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_arb import RealBallField as RealBallField
from sage.rings.real_mpfi import RIF as RIF, RealIntervalField as RealIntervalField, RealIntervalFieldElement as RealIntervalFieldElement, RealIntervalField_class as RealIntervalField_class
from sage.rings.real_mpfr import RR as RR
from sage.structure.coerce import parent_is_numerical as parent_is_numerical, parent_is_real_numerical as parent_is_real_numerical
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.richcmp import op_EQ as op_EQ, op_GT as op_GT, op_NE as op_NE, rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal
from sage.structure.sage_object import SageObject as SageObject

from sage.rings.polynomial.polynomial_ring import PolynomialRing_field # with_category
from sage.rings.polynomial.polynomial_rational_flint import Polynomial_rational_flint
from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
from sage.rings.polynomial.polynomial_integer_dense_flint import Polynomial_integer_dense_flint
from sage.rings.real_mpfr import RealNumber as RealNumber
from sage.rings.rational import Rational
from sage.rings.number_field.number_field import NumberField_quadratic # with_category

class AlgebraicField_common(sage.rings.abc.AlgebraicField_common):
    """
    Common base class for the classes :class:`~AlgebraicRealField` and
    :class:`~AlgebraicField`.

    TESTS::

        sage: AA.is_finite()
        False
        sage: QQbar.is_finite()
        False
    """
    class options(GlobalOptions):
        NAME: str
        display_format: Incomplete
    def default_interval_prec(self):
        """
        Return the default interval precision used for root isolation.

        EXAMPLES::

            sage: AA.default_interval_prec()
            64
        """
    def characteristic(self):
        """
        Return the characteristic of this field.

        Since this class is only used
        for fields of characteristic 0, this always returns 0.

        EXAMPLES::

            sage: AA.characteristic()
            0
        """
    def order(self):
        """
        Return the cardinality of ``self``.

        Since this class is only used for
        fields of characteristic 0, always returns Infinity.

        EXAMPLES::

            sage: QQbar.order()
            +Infinity
        """
    def common_polynomial(self, poly):
        '''
        Given a polynomial with algebraic coefficients, return a
        wrapper that caches high-precision calculations and
        factorizations. This wrapper can be passed to :meth:`polynomial_root`
        in place of the polynomial.

        Using :meth:`common_polynomial` makes no semantic difference, but will
        improve efficiency if you are dealing with multiple roots
        of a single polynomial.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = AA.common_polynomial(x^2 - x - 1)
            sage: phi = AA.polynomial_root(p, RIF(1, 2))
            sage: tau = AA.polynomial_root(p, RIF(-1, 0))
            sage: phi + tau == 1
            True
            sage: phi * tau == -1
            True

            sage: # needs sage.symbolic
            sage: x = polygen(SR)
            sage: p = (x - sqrt(-5)) * (x - sqrt(3)); p
            x^2 + (-sqrt(3) - sqrt(-5))*x + sqrt(3)*sqrt(-5)
            sage: p = QQbar.common_polynomial(p)
            sage: a = QQbar.polynomial_root(p, CIF(RIF(-0.1, 0.1), RIF(2, 3))); a
            0.?e-18 + 2.236067977499790?*I
            sage: b = QQbar.polynomial_root(p, RIF(1, 2)); b
            1.732050807568878?

        These "common polynomials" can be shared between real and
        complex roots::

             sage: p = AA.common_polynomial(x^3 - x - 1)
             sage: r1 = AA.polynomial_root(p, RIF(1.3, 1.4)); r1
             1.324717957244746?
             sage: r2 = QQbar.polynomial_root(p, CIF(RIF(-0.7, -0.6), RIF(0.5, 0.6))); r2
             -0.6623589786223730? + 0.5622795120623013?*I
        '''

class AlgebraicRealField(Singleton, AlgebraicField_common, sage.rings.abc.AlgebraicRealField):
    """
    The field of algebraic reals.

    TESTS::

        sage: AA == loads(dumps(AA))
        True
    """
    def __new__(cls):
        '''
        This method is there to ensure that pickles created before this class
        was made a :class:`~sage.misc.fast_methods.Singleton` still load.

        TESTS::

            sage: s = loads(b\'x\\x9cmQ\\xcbR\\x141\\x14\\xad\\x11A\\x083\\xe2\\x03T|\'
            ....: b\'\\x82l`\\xd3\\xff\\xe0\\x86\\x8de/\\xba*\\xcb\\xa9[\\xe9\\xf4\'
            ....: b\'\\xa5;e:=\\\'I+,\\xa6J\\x17B\\xf9\\xd7f\\x08\\xe2s\\x95\\xa4\\xee9\\xf7<\'
            ....: b\'\\xf2\\xe5\\x8e\\x0e\\xaa\\xe5"D?\\xea8z.\\x9a\\x0b\\xa7z\\xa3I[\\x15\'
            ....: b\'\\x82\\xf8\\xf3\\x85\\xc9\\xb1<xg[\\xae\\xbd2\\xbabeO\\r\\xdb\\x86>\\x9b\'
            ....: b\'\\xd8\\x91V\\x91\\xdb\\xc1_\\xe0f\\xa57\\xae\\r\\x05P+/\\xfe\\xe5\\x08\'
            ....: b\'\\xaci\\xa2z46\\x1aG$Z\\x8e*F/p\\xf7oC\\xa33\\x18\\x99</<\\x07v\\tf\'
            ....: b\'\\x06\\\'F\\xe7\\xb9\\x195\\x0b\\xacg\\xc2\\x8d\\xbc\\xe1P\\x9c\\xad\\x04\'
            ....: b\'\\x828\\xcd\\x076N\\x96W\\xb8WaSN\\x17\\xca\\xa7\\r9\\r\\xb6.+\\x88Kl\'
            ....: b\'\\x97e\\xb7\\x16+LO\\xbeb\\xb6\\xc4\\xfdc)\\x88\\xfb\\x9a\\x9b&\\x05\'
            ....: b\'\\xc0N)wI\\x0f\\xee\\x13\\xfbH=\\xc7nh(U\\xc2xP\\xca\\r\\xd2\\x8d\'
            ....: b\'\\x8a\\n\\x0fK\\xb9\\xf5+\\xfe\\xa3n3MV\\x98\\x80\\xc7rr\\xfe\\r\\xbbr\'
            ....: b\'\\x9bZv\\xecU\\x1c|\\xc0\\xde\\x12O\\xe4:\\xd5*0\\x9ev3\\xb9C\\x0b\'
            ....: b\'\\xa3?Z\\xa6\\xa4\\x11R6<{?I\\xa2l\\xb9\\xbf6;\\xb8\\\\\\xc6\\xe0\\xb1\'
            ....: b\'\\x9f\\xb3\\xf6&\\xe8\\xe2,\\xb3R\\x13\\xf9\\xf2\\xe1\\xda\\x9c\\xc0s\'
            ....: b\'\\xb9\\xf7?.\\xe1E7\\xeb\\xa6W\\x15^&\\x80q&\\x1aeo\\x93Y\\x13"^\\xcd\'
            ....: b\'\\xf1Z\\xee\\xdf\\x92W\\x18Z\\xa4\\xa6(\\xd7\\x867\\xdf\\x93\\xad\\x9fL\'
            ....: b\'\\xa5W\\xff\\x90\\x89\\x07s\\x1c\\xfe6\\xd2\\x03{\\xcdy\\xf4v\\x8e\\xa3\'
            ....: b\'\\xb1.~\\x000\\xc2\\xe0\\xa1\')
            sage: s is AA
            True
        '''
    def __init__(self) -> None:
        """
        Standard initialization function.

        EXAMPLES:

        This function calls functions in superclasses which set the category, so we check that. ::

            sage: QQbar.category() # indirect doctest
            Category of infinite fields

        Coercions::

            sage: AA.has_coerce_map_from(ZZ)
            True
            sage: AA.has_coerce_map_from(int)
            True
        """
    def completion(self, p, prec, extras={}):
        """
        Return the completion of ``self`` at the place `p`.

        Only implemented for `p = \\infty` at present.

        INPUT:

        - ``p`` -- either a prime (not implemented at present) or ``Infinity``
        - ``prec`` -- precision of approximate field to return
        - ``extras`` -- (optional) a dict of extra keyword arguments
          for the ``RealField`` constructor

        EXAMPLES::

            sage: AA.completion(infinity, 500)
            Real Field with 500 bits of precision
            sage: AA.completion(infinity, prec=53, extras={'type':'RDF'})
            Real Double Field
            sage: AA.completion(infinity, 53) is RR
            True
            sage: AA.completion(7, 10)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def algebraic_closure(self):
        """
        Return the algebraic closure of this field, which is the field
        `\\overline{\\QQ}` of algebraic numbers.

        EXAMPLES::

            sage: AA.algebraic_closure()
            Algebraic Field
        """
    def gens(self) -> tuple:
        """
        Return a set of generators for this field.

        As this field is not
        finitely generated, we opt for just returning 1.

        EXAMPLES::

            sage: AA.gens()
            (1,)
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th element of the tuple returned by :meth:`gens`.

        EXAMPLES::

            sage: AA.gen(0)
            1
            sage: AA.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: n must be 0
        """
    def ngens(self):
        """
        Return the size of the tuple returned by :meth:`gens`.

        EXAMPLES::

            sage: AA.ngens()
            1
        """
    def zeta(self, n: int = 2):
        """
        Return an `n`-th root of unity in this field. This will raise a
        :exc:`ValueError` if `n \\ne \\{1, 2\\}` since no such root exists.

        INPUT:

        - ``n`` -- integer (default: 2)

        EXAMPLES::

            sage: AA.zeta(1)
            1
            sage: AA.zeta(2)
            -1
            sage: AA.zeta()
            -1
            sage: AA.zeta(3)
            Traceback (most recent call last):
            ...
            ValueError: no n-th root of unity in algebraic reals

        Some silly inputs::

            sage: AA.zeta(Mod(-5, 7))
            -1
            sage: AA.zeta(0)
            Traceback (most recent call last):
            ...
            ValueError: no n-th root of unity in algebraic reals
        """
    def polynomial_root(self, poly, interval, multiplicity: int = 1):
        """
        Given a polynomial with algebraic coefficients and an interval
        enclosing exactly one root of the polynomial, constructs
        an algebraic real representation of that root.

        The polynomial need not be irreducible, or even squarefree; but
        if the given root is a multiple root, its multiplicity must be
        specified. (IMPORTANT NOTE: Currently, multiplicity-`k` roots
        are handled by taking the `(k-1)`-st derivative of the polynomial.
        This means that the interval must enclose exactly one root
        of this derivative.)

        The conditions on the arguments (that the interval encloses exactly
        one root, and that multiple roots match the given multiplicity)
        are not checked; if they are not satisfied, an error may be
        thrown (possibly later, when the algebraic number is used),
        or wrong answers may result.

        Note that if you are constructing multiple roots of a single
        polynomial, it is better to use ``AA.common_polynomial`` (or
        ``QQbar.common_polynomial``; the two are equivalent) to get a
        shared polynomial.

        EXAMPLES::

            sage: x = polygen(AA)
            sage: phi = AA.polynomial_root(x^2 - x - 1, RIF(1, 2)); phi
            1.618033988749895?
            sage: p = (x-1)^7 * (x-2)
            sage: r = AA.polynomial_root(p, RIF(9/10, 11/10), multiplicity=7)
            sage: r; r == 1
            1.000000000000000?
            True
            sage: p = (x-phi)*(x-sqrt(AA(2)))
            sage: r = AA.polynomial_root(p, RIF(1, 3/2))
            sage: r; r == sqrt(AA(2))
            1.414213562373095?
            True

        We allow complex polynomials, as long as the particular root
        in question is real. ::

            sage: K.<im> = QQ[I]
            sage: x = polygen(K)
            sage: p = (im + 1) * (x^3 - 2); p
            (I + 1)*x^3 - 2*I - 2
            sage: r = AA.polynomial_root(p, RIF(1, 2)); r^3
            2.000000000000000?
        """
    def random_element(self, poly_degree: int = 2, *args, **kwds):
        """
        Return a random algebraic real number.

        INPUT:

        - ``poly_degree`` -- (default: 2) degree of the random
          polynomial over the integers of which the returned algebraic
          real number is a (real part of a) root. This is not
          necessarily the degree of the minimal polynomial of the
          number. Increase this parameter to achieve a greater
          diversity of algebraic numbers, at a cost of greater
          computation time. You can also vary the distribution of the
          coefficients but that will not vary the degree of the
          extension containing the element.

        - ``args``, ``kwds`` -- arguments and keywords passed to the random
          number generator for elements of ``ZZ``, the integers. See
          :meth:`~sage.rings.integer_ring.IntegerRing_class.random_element` for
          details, or see example below.

        OUTPUT:

        An element of ``AA``, the field of algebraic real numbers (see
        :mod:`sage.rings.qqbar`).

        ALGORITHM:

        We pass all arguments to :meth:`AlgebraicField.random_element`, and
        then take the real part of the result.

        EXAMPLES::

            sage: a = AA.random_element()
            sage: a in AA
            True

        ::

            sage: b = AA.random_element(poly_degree=5)
            sage: b in AA
            True

        Parameters for the distribution of the integer coefficients of
        the polynomials can be passed on to the random element method
        for integers. For example, we can rule out zero as a
        coefficient (and therefore as a root) by requesting
        coefficients between ``1`` and ``10``::

            sage: z = [AA.random_element(x=1, y=10) for _ in range(5)]
            sage: AA(0) in z
            False

        TESTS::

            sage: AA.random_element('junk')
            Traceback (most recent call last):
            ...
            TypeError: polynomial degree must be an integer, not junk
            sage: AA.random_element(poly_degree=0)
            Traceback (most recent call last):
            ...
            ValueError: polynomial degree must be greater than zero, not 0

        Random vectors already have a 'degree' keyword, so
        we cannot use that for the polynomial's degree::

            sage: v = random_vector(AA, degree=2, poly_degree=3)
            sage: v in AA^2
            True
        """

def is_AlgebraicRealField(F):
    '''
    Check whether ``F`` is an :class:`~AlgebraicRealField` instance. For internal use.

    This function is deprecated. Use :func:`isinstance` with
    :class:`~sage.rings.abc.AlgebraicRealField` instead.

    EXAMPLES::

        sage: from sage.rings.qqbar import is_AlgebraicRealField
        sage: [is_AlgebraicRealField(x) for x in [AA, QQbar, None, 0, "spam"]]
        doctest:warning...
        DeprecationWarning: is_AlgebraicRealField is deprecated;
        use isinstance(..., sage.rings.abc.AlgebraicRealField instead
        See https://github.com/sagemath/sage/issues/32660 for details.
        [True, False, False, False, False]
    '''

AA: AlgebraicRealField

class AlgebraicField(Singleton, AlgebraicField_common, sage.rings.abc.AlgebraicField):
    """
    The field of all algebraic complex numbers.
    """
    def __new__(cls):
        '''
        This method is there to ensure that pickles created before this class
        was made a :class:`~sage.misc.fast_methods.Singleton` still load.

        TESTS::

            sage: s = loads(b\'x\\x9c}RMo\\x131\\x10U(-\\xad\\x9b\\x92\\x16ZJh\\x80~\'
            ....: b\'\\x00MZX~\\x03\\x97J\\x08\\xb1\\x87H>F\\x96\\xd7;\\xdd\\xb1\\xd8x3\\xb6\'
            ....: b\'\\x17\\xe8!\\x12\\x1c\\xda\\xaa\\xff\\x9aI\\xb7\\x04\\x8a*N\\xb65\\xef\'
            ....: b\'\\xcd\\xbc\\xf7\\xc6?\\xee\\x99\\xa0\\x0bHB\\xf4\\xb5\\x89\\xb5\'
            ....: b\'\\x87$?szl\\x8d2\\xa5\\x0eA\\xdc~Q\\xab/{\\x1f\\xca\\x022\\xaf\\xad9\'
            ....: b\'\\xb1P\\xe6\\xea\\x9b\\x8d\\xa8\\x8c\\x8ePT\\xfe\\x8cn\\xday\\xeb\\x8a\'
            ....: b\'\\x90\\x10e\\xda\\x8b\\xdbxA\\x0bF\\xa9\\xac\\xb6e\\xb4N)Q@\\xd41zA\'
            ....: b\'\\xf7\\xff\\x15R;K5(\\x0f\\x13\\x0f\\x01\\x1c\\xc3l\\xe5D\\xed<\\xe4\'
            ....: b\'\\xb5\\x01A\\x8b\\r\\xe1f\\xb4\\x85\\x90\\x9c\\xce\\x06\\x04q\\xd2\\x1c\'
            ....: b\'\\xb44\\x98^\\xd2\\x83!-\\xcb\\xf6D{\\xee\\xd0\\xb8\\xa0\\x95\\x8b!\\x89\'
            ....: b\'\\x0bZMS\\\\\\x88Cj\\x0f~\\xd2\\xda\\x94\\x1e\\xf6\\xa5P0\\xce \\xcfY<uR\'
            ....: b\'\\xb9\\xa9L\\xe5\\xbe\\x82\\x8fj\\x0c\\x11\\xab\\\\q\\x14@\\xeb\\xa9\\\\R&\'
            ....: b\'\\xd7Q\\xd3F*W\\xfeX\\x7f\\x84\\xcb\\\\\\x99a\\x02=\\x96\\xad\\x8f\\xe7\'
            ....: b\'\\xb4)WU\\x01\\x0e\\xbc\\x8e\\x95\\x0f\\xb45\\xa5\\\'rQe:\\x00m#G\\xb9;\'
            ....: b\'\\x8ff\\x08\\xba\\xbc+\\xce\\xa7\\xff\\x89s\\xce\\x11\\xd4E\\xf6\\xf3\'
            ....: b\'\\x8c\\xfdt\\xd9\\xcf\\x0e\\xfb\\xe9M\\xe9y\\x1f;)\\xae\\xa7\\xb8\'
            ....: b\'\\x91"KC\\x96\\xf4\\xfd\\x9c^ \\xabx\\x89\\xdb\\xd8\\x93\\x1d5\\xb1\'
            ....: b\'\\xe6K\\t\\x8a-\\x06\\x8e\\x96v?\\xb5\\xd83\\x940\\xbe\\xce\\xaar\'
            ....: b\'\\xcd.*O{\\x8d\\x8c\\xb1\\r&9mX\\xbc\\x88\\xe6\\xf2\\xf9:\\x1bA\\xfbr\'
            ....: b\'\\xeb.\\xae\\xa2\\x03\\xec\\xe1\\xce\\xe5\\x90^1\\xc0:\\x1b\\xad.\\xe7\'
            ....: b\'\\xc1\\x966Dz=\\xa27\\xb2;\\\'\\xcf0j\\xc2\\x8bR\\xcd\\xd6\\xe8\\xf0\'
            ....: b\'\\x8ae\\xfdfj3\\xfb\\x06\\r\\xb1?\\xa2\\xc1_%S\\x817\\xd0\\x94\'
            ....: b\'\\x8eFt\\\\g\\xc8\\x96p\\x0f\\xf7\\xf1\\x00\\xd7\\xb0\\xcd\\x1a\\xde"\'
            ....: b\'\\x0f{\\x87\\x87W\\xc8\\xdc\\x04\\x19\\xf5\\xbe\\xce\\x92_p\\\'\\x13\\xc5\')
            sage: s is QQbar
            True
        '''
    def __init__(self) -> None:
        """
        Standard init function.

        We test by setting the category::

            sage: QQbar.category() # indirect doctest
            Category of infinite fields
            sage: QQbar.base_ring()
            Algebraic Real Field

        TESTS::

            sage: QQbar._repr_option('element_is_atomic')
            False

            sage: QQbar.has_coerce_map_from(ZZ)
            True
            sage: QQbar.has_coerce_map_from(int)
            True
        """
    def completion(self, p, prec, extras={}):
        """
        Return the completion of ``self`` at the place `p`.

        Only implemented for `p = \\infty` at present.

        INPUT:

        - ``p`` -- either a prime (not implemented at present) or ``Infinity``
        - ``prec`` -- precision of approximate field to return
        - ``extras`` -- (optional) a dict of extra keyword arguments
          for the ``RealField`` constructor

        EXAMPLES::

            sage: QQbar.completion(infinity, 500)
            Complex Field with 500 bits of precision
            sage: QQbar.completion(infinity, prec=53, extras={'type':'RDF'})
            Complex Double Field
            sage: QQbar.completion(infinity, 53) is CC
            True
            sage: QQbar.completion(3, 20)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def algebraic_closure(self):
        """
        Return the algebraic closure of this field.

        As this field is already algebraically closed, just returns ``self``.

        EXAMPLES::

            sage: QQbar.algebraic_closure()
            Algebraic Field
        """
    def construction(self):
        """
        Return a functor that constructs ``self`` (used by the coercion machinery).

        EXAMPLES::

            sage: QQbar.construction()
            (AlgebraicClosureFunctor, Rational Field)
        """
    def gens(self) -> tuple:
        """
        Return a set of generators for this field.

        As this field is not
        finitely generated over its prime field, we opt for just returning I.

        EXAMPLES::

            sage: QQbar.gens()
            (I,)
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th element of the tuple returned by :meth:`gens`.

        EXAMPLES::

            sage: QQbar.gen(0)
            I
            sage: QQbar.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: n must be 0
        """
    def ngens(self):
        """
        Return the size of the tuple returned by :meth:`gens`.

        EXAMPLES::

            sage: QQbar.ngens()
            1
        """
    @cached_method
    def zeta(self, n: int = 4):
        """
        Return a primitive `n`-th root of unity, specifically `\\exp(2*\\pi*i/n)`.

        INPUT:

        - ``n`` -- integer (default: 4)

        EXAMPLES::

            sage: QQbar.zeta(1)
            1
            sage: QQbar.zeta(2)
            -1
            sage: QQbar.zeta(3)
            -0.500000000000000? + 0.866025403784439?*I
            sage: QQbar.zeta(4)
            I
            sage: QQbar.zeta()
            I
            sage: QQbar.zeta(5)
            0.3090169943749474? + 0.9510565162951536?*I
            sage: QQbar.zeta(3000)
            0.999997806755380? + 0.002094393571219374?*I
        """
    def polynomial_root(self, poly, interval, multiplicity: int = 1):
        """
        Given a polynomial with algebraic coefficients and an interval
        enclosing exactly one root of the polynomial, constructs
        an algebraic real representation of that root.

        The polynomial need not be irreducible, or even squarefree; but
        if the given root is a multiple root, its multiplicity must be
        specified. (IMPORTANT NOTE: Currently, multiplicity-`k` roots
        are handled by taking the `(k-1)`-st derivative of the polynomial.
        This means that the interval must enclose exactly one root
        of this derivative.)

        The conditions on the arguments (that the interval encloses exactly
        one root, and that multiple roots match the given multiplicity)
        are not checked; if they are not satisfied, an error may be
        thrown (possibly later, when the algebraic number is used),
        or wrong answers may result.

        Note that if you are constructing multiple roots of a single
        polynomial, it is better to use ``QQbar.common_polynomial``
        to get a shared polynomial.

        EXAMPLES::

            sage: x = polygen(QQbar)
            sage: phi = QQbar.polynomial_root(x^2 - x - 1, RIF(0, 2)); phi
            1.618033988749895?
            sage: p = (x-1)^7 * (x-2)
            sage: r = QQbar.polynomial_root(p, RIF(9/10, 11/10), multiplicity=7)
            sage: r; r == 1
            1
            True
            sage: p = (x-phi)*(x-sqrt(QQbar(2)))
            sage: r = QQbar.polynomial_root(p, RIF(1, 3/2))
            sage: r; r == sqrt(QQbar(2))
            1.414213562373095?
            True
        """
    def random_element(self, poly_degree: int = 2, *args, **kwds):
        """
        Return a random algebraic number.

        INPUT:

        - ``poly_degree`` -- (default: 2) degree of the random polynomial over
          the integers of which the returned algebraic number is a root. This
          is not necessarily the degree of the minimal polynomial of the
          number. Increase this parameter to achieve a greater diversity of
          algebraic numbers, at a cost of greater computation time. You can
          also vary the distribution of the coefficients but that will not vary
          the degree of the extension containing the element.

        - ``args``, ``kwds`` -- arguments and keywords passed to the random
          number generator for elements of ``ZZ``, the integers. See
          :meth:`~sage.rings.integer_ring.IntegerRing_class.random_element` for
          details, or see example below.

        OUTPUT:

        An element of ``QQbar``, the field of algebraic numbers (see
        :mod:`sage.rings.qqbar`).

        ALGORITHM:

        A polynomial with degree between 1 and ``poly_degree``,
        with random integer coefficients is created. A root of this
        polynomial is chosen at random. The default degree is
        2 and the integer coefficients come from a distribution
        heavily weighted towards `0, \\pm 1, \\pm 2`.

        EXAMPLES::

            sage: a = QQbar.random_element()
            sage: a                         # random
            0.2626138748742799? + 0.8769062830975992?*I
            sage: a in QQbar
            True

            sage: b = QQbar.random_element(poly_degree=20)
            sage: b                         # random
            -0.8642649077479498? - 0.5995098147478391?*I
            sage: b in QQbar
            True

        Parameters for the distribution of the integer coefficients
        of the polynomials can be passed on to the random element method
        for integers. For example, current default behavior of this method
        returns zero about 15% of the time; if we do not include zero as a
        possible coefficient, there will never be a zero constant term, and
        thus never a zero root. ::

            sage: z = [QQbar.random_element(x=1, y=10) for _ in range(20)]
            sage: QQbar(0) in z
            False

        If you just want real algebraic numbers you can filter them out.
        Using an odd degree for the polynomials will ensure some degree of
        success. ::

            sage: r = []
            sage: while len(r) < 3:
            ....:   x = QQbar.random_element(poly_degree=3)
            ....:   if x in AA:
            ....:     r.append(x)
            sage: (len(r) == 3) and all(z in AA for z in r)
            True

        TESTS::

            sage: QQbar.random_element('junk')
            Traceback (most recent call last):
            ...
            TypeError: polynomial degree must be an integer, not junk
            sage: QQbar.random_element(poly_degree=0)
            Traceback (most recent call last):
            ...
            ValueError: polynomial degree must be greater than zero, not 0

        Random vectors already have a 'degree' keyword, so
        we cannot use that for the polynomial's degree. ::

            sage: v = random_vector(QQbar, degree=2, poly_degree=3)
            sage: v                                 # random
            (0.4694381338921299?, -0.500000000000000? + 0.866025403784439?*I)
        """

def is_AlgebraicField(F):
    '''
    Check whether ``F`` is an :class:`~AlgebraicField` instance.

    This function is deprecated. Use :func:`isinstance` with
    :class:`~sage.rings.abc.AlgebraicField` instead.

    EXAMPLES::

        sage: from sage.rings.qqbar import is_AlgebraicField
        sage: [is_AlgebraicField(x) for x in [AA, QQbar, None, 0, "spam"]]
        doctest:warning...
        DeprecationWarning: is_AlgebraicField is deprecated;
        use isinstance(..., sage.rings.abc.AlgebraicField instead
        See https://github.com/sagemath/sage/issues/32660 for details.
        [False, True, False, False, False]
    '''

QQbar: AlgebraicField

def prec_seq() -> Generator[Incomplete]:
    """
    Return a generator object which iterates over an infinite increasing
    sequence of precisions to be tried in various numerical computations.

    Currently just returns powers of 2 starting at 64.

    EXAMPLES::

        sage: g = sage.rings.qqbar.prec_seq()
        sage: [next(g), next(g), next(g)]
        [64, 128, 256]
    """
def short_prec_seq():
    """
    Return a sequence of precisions to try in cases when an infinite-precision
    computation is possible: returns a couple of small powers of 2 and then
    ``None``.

    EXAMPLES::

        sage: from sage.rings.qqbar import short_prec_seq
        sage: short_prec_seq()
        (64, 128, None)
    """
def tail_prec_seq() -> Generator[Incomplete]:
    """
    A generator over precisions larger than those in :func:`~short_prec_seq`.

    EXAMPLES::

        sage: from sage.rings.qqbar import tail_prec_seq
        sage: g = tail_prec_seq()
        sage: [next(g), next(g), next(g)]
        [256, 512, 1024]
    """
def rational_exact_root(r, d):
    """
    Check whether the rational `r` is an exact `d`-th power.

    If so, this returns the `d`-th root of `r`; otherwise, this returns ``None``.

    EXAMPLES::

        sage: from sage.rings.qqbar import rational_exact_root
        sage: rational_exact_root(16/81, 4)
        2/3
        sage: rational_exact_root(8/81, 3) is None
        True
    """
def clear_denominators(poly):
    '''
    Take a monic polynomial and rescale the variable to get a monic
    polynomial with "integral" coefficients.

    This works on any univariate
    polynomial whose base ring has a ``denominator()`` method that returns
    integers; for example, the base ring might be `\\QQ` or a number
    field.

    Returns the scale factor and the new polynomial.

    (Inspired by :pari:`primitive_pol_to_monic` .)

    We assume that coefficient denominators are "small"; the algorithm
    factors the denominators, to give the smallest possible scale factor.

    EXAMPLES::

        sage: from sage.rings.qqbar import clear_denominators

        sage: _.<x> = QQ[\'x\']
        sage: clear_denominators(x + 3/2)
        (2, x + 3)
        sage: clear_denominators(x^2 + x/2 + 1/4)
        (2, x^2 + x + 1)

    TESTS::

        sage: R.<y> = QQ[]
        sage: coefficients_as_integer_ratios = [
        ....:     (-2774600080567517563395913264491323241652779066919616441429094563840,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (-24216324060414384566983400245979288839929814383090701293489050615808,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (325579773864372490083706670433410006284520887405882567940047555526656,
        ....:      180143564412823751787837643000565238870031999674661705128541236331583133845246252269971),
        ....:     (-86736048492777879473586471630941922517134071457946320753641122078523392,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (-2338058278498910195688689352766977573607428722429118859280880481590329344,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (105830270645785996318880019945503938356315302592627229453391693256551317504,
        ....:      1381100660498315430373421929671000164670245330839073072652149478542137359480221267403111),
        ....:     (1110926147990548796149597141538460730252912439930561079348611699181798425600,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (-89705438380888704653335165590083767769953879654958783855317882966200828559360,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (1151092895747371986483047191334923516591005329489629755485810229546333821625856,
        ....:      1381100660498315430373421929671000164670245330839073072652149478542137359480221267403111),
        ....:     (24725641793859400310483886670136079788266826658111372723121573233077840328938576,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (-31051495080139473677925068000403254349133134904365702868216464107777210775457136,
        ....:      153455628944257270041491325519000018296693925648785896961349942060237484386691251933679),
        ....:     (9431591461895130351865642769482226964622378075329823505708119342634182162193000560,
        ....:      4143301981494946291120265789013000494010735992517219217956448435626412078440663802209333),
        ....:     (1721694880863483428337378731387732043714427651970488363462560317808769716807148992,
        ....:      153455628944257270041491325519000018296693925648785896961349942060237484386691251933679),
        ....:     (255327752077837584624694974814916395144764296822788813014081161094149724325120096,
        ....:      27080405107810106477910233915117650287651869232138687699061754481218379597651397400061),
        ....:     (238105337335596176836773151768694069523377650990453522899627157538495252117232992338,
        ....:      27080405107810106477910233915117650287651869232138687699061754481218379597651397400061),
        ....:     (1255826892296350234297164500548658984205287902407560187136301197703464130999349114638,
        ....:      14336685057075938723599535602121108975815695475838128781856222960645024492874269211797),
        ....:     (1, 1)]
        sage: p = R(coefficients_as_integer_ratios)
        sage: a = QQbar.polynomial_root(
        ....:     AA.common_polynomial(p),
        ....:     CIF(RIF(-RR(0.036151142425748496), -RR(0.036151142425748489)),
        ....:     RIF(-RR(0.011298617187916445), -RR(0.011298617187916443))))
        sage: a.exactify()
        sage: a
        -0.03615114242574849? - 0.011298617187916444?*I
    '''
def do_polred(poly, threshold: int = 32):
    """
    Find a polynomial of reasonably small discriminant that generates
    the same number field as ``poly``, using the PARI ``polredbest``
    function.

    INPUT:

    - ``poly`` -- a monic irreducible polynomial with integer coefficients
    - ``threshold`` -- integer used to decide whether to run ``polredbest``

    OUTPUT:

    A triple (``elt_fwd``, ``elt_back``, ``new_poly``), where:

    - ``new_poly`` is the new polynomial defining the same number field,
    - ``elt_fwd`` is a polynomial expression for a root of the new
      polynomial in terms of a root of the original polynomial,
    - ``elt_back`` is a polynomial expression for a root of the original
      polynomial in terms of a root of the new polynomial.

    EXAMPLES::

        sage: from sage.rings.qqbar import do_polred
        sage: R.<x> = QQ['x']
        sage: oldpol = x^2 - 5
        sage: fwd, back, newpol = do_polred(oldpol)
        sage: newpol
        x^2 - x - 1
        sage: Kold.<a> = NumberField(oldpol)
        sage: Knew.<b> = NumberField(newpol)
        sage: newpol(fwd(a))
        0
        sage: oldpol(back(b))
        0
        sage: do_polred(x^2 - x - 11)
        (1/3*x + 1/3, 3*x - 1, x^2 - x - 1)
        sage: do_polred(x^3 + 123456)
        (-1/4*x, -4*x, x^3 - 1929)

    This shows that :issue:`13054` has been fixed::

        sage: do_polred(x^4 - 4294967296*x^2 + 54265257667816538374400)
        (1/4*x, 4*x, x^4 - 268435456*x^2 + 211973662764908353025)
    """
def isolating_interval(intv_fn, pol):
    """
    ``intv_fn`` is a function that takes a precision and returns an
    interval of that precision containing some particular root of pol.
    (It must return better approximations as the precision increases.)
    pol is an irreducible polynomial with rational coefficients.

    Returns an interval containing at most one root of pol.

    EXAMPLES::

        sage: from sage.rings.qqbar import isolating_interval

        sage: _.<x> = QQ['x']
        sage: isolating_interval(lambda prec: sqrt(RealIntervalField(prec)(2)), x^2 - 2)
        1.4142135623730950488?

    And an example that requires more precision::

        sage: delta = 10^(-70)
        sage: p = (x - 1) * (x - 1 - delta) * (x - 1 + delta)
        sage: isolating_interval(lambda prec: RealIntervalField(prec)(1 + delta), p)
        1.000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000?

    The function also works with complex intervals and complex roots::

        sage: p = x^2 - x + 13/36
        sage: isolating_interval(lambda prec: ComplexIntervalField(prec)(1/2, 1/3), p)
        0.500000000000000000000? + 0.3333333333333333334?*I
    """
def find_zero_result(fn, l):
    """
    ``l`` is a list of some sort. ``fn`` is a function which maps an element of
    ``l`` and a precision into an interval (either real or complex) of that
    precision, such that for sufficient precision, exactly one element of ``l``
    results in an interval containing 0. Returns that one element of ``l``.

    EXAMPLES::

        sage: from sage.rings.qqbar import find_zero_result
        sage: _.<x> = QQ['x']
        sage: delta = 10^(-70)
        sage: p1 = x - 1
        sage: p2 = x - 1 - delta
        sage: p3 = x - 1 + delta
        sage: p2 == find_zero_result(lambda p, prec: p(RealIntervalField(prec)(1 + delta)), [p1, p2, p3])
        True
    """
def conjugate_expand(v):
    """
    If the interval ``v`` (which may be real or complex) includes some
    purely real numbers, return ``v'`` containing ``v`` such that
    ``v' == v'.conjugate()``. Otherwise return ``v`` unchanged. (Note that if
    ``v' == v'.conjugate()``, and ``v'`` includes one non-real root of a real
    polynomial, then ``v'`` also includes the conjugate of that root.
    Also note that the diameter of the return value is at most twice
    the diameter of the input.)

    EXAMPLES::

        sage: from sage.rings.qqbar import conjugate_expand
        sage: conjugate_expand(CIF(RIF(0, 1), RIF(1, 2))).str(style='brackets')
        '[0.0000000000000000 .. 1.0000000000000000] + [1.0000000000000000 .. 2.0000000000000000]*I'
        sage: conjugate_expand(CIF(RIF(0, 1), RIF(0, 1))).str(style='brackets')
        '[0.0000000000000000 .. 1.0000000000000000] + [-1.0000000000000000 .. 1.0000000000000000]*I'
        sage: conjugate_expand(CIF(RIF(0, 1), RIF(-2, 1))).str(style='brackets')
        '[0.0000000000000000 .. 1.0000000000000000] + [-2.0000000000000000 .. 2.0000000000000000]*I'
        sage: conjugate_expand(RIF(1, 2)).str(style='brackets')
        '[1.0000000000000000 .. 2.0000000000000000]'
    """
def conjugate_shrink(v):
    """
    If the interval ``v`` includes some purely real numbers, return
    a real interval containing only those real numbers. Otherwise
    return ``v`` unchanged.

    If ``v`` includes exactly one root of a real polynomial, and ``v`` was
    returned by ``conjugate_expand()``, then ``conjugate_shrink(v)`` still
    includes that root, and is a ``RealIntervalFieldElement`` iff the root
    in question is real.

    EXAMPLES::

        sage: from sage.rings.qqbar import conjugate_shrink
        sage: conjugate_shrink(RIF(3, 4)).str(style='brackets')
        '[3.0000000000000000 .. 4.0000000000000000]'
        sage: conjugate_shrink(CIF(RIF(1, 2), RIF(1, 2))).str(style='brackets')
        '[1.0000000000000000 .. 2.0000000000000000] + [1.0000000000000000 .. 2.0000000000000000]*I'
        sage: conjugate_shrink(CIF(RIF(1, 2), RIF(0, 1))).str(style='brackets')
        '[1.0000000000000000 .. 2.0000000000000000]'
        sage: conjugate_shrink(CIF(RIF(1, 2), RIF(-1, 2))).str(style='brackets')
        '[1.0000000000000000 .. 2.0000000000000000]'
    """
def number_field_elements_from_algebraics(numbers, minimal: bool = False, same_field: bool = False, embedded: bool = False, name: str = 'a', prec: int = 53):
    """
    Given a sequence of elements of either ``AA`` or ``QQbar``
    (or a mixture), computes a number field containing all of these
    elements, these elements as members of that number field, and a
    homomorphism from the number field back to ``AA`` or
    ``QQbar``.

    INPUT:

    - ``numbers`` -- a number or list of numbers

    - ``minimal`` -- boolean (default: ``False``); whether to minimize the
      degree of the extension

    - ``same_field`` -- boolean (default: ``False``); see below

    - ``embedded`` -- boolean (default: ``False``); whether to make the
      NumberField embedded, note that this has no effect when the
      resulting field is ``QQ`` because there is only one ``QQ`` instance

    - ``name`` -- string (default: ``'a'``); name of the primitive element

    - ``prec`` -- integer (default: 53); the number of bit of precision
      to guarantee finding real roots

    OUTPUT:

    A tuple with the NumberField, the numbers inside the NumberField,
    and a homomorphism from the number field back to ``AA`` or ``QQbar``.

    This may not return the smallest such number field, unless
    ``minimal=True`` is specified.

    If ``same_field=True`` is specified, and all of the elements are
    from the same field (either ``AA`` or ``QQbar``), the generated
    homomorphism will map back to that field.  Otherwise, if all specified
    elements are real, the homomorphism might map back to ``AA``
    (and will, if ``minimal=True`` is specified), even if the
    elements were in ``QQbar``.

    Also, a single number can be passed, rather than a sequence; and
    any values which are not elements of ``AA`` or ``QQbar``
    will automatically be coerced to ``QQbar``

    This function may be useful for efficiency reasons: doing exact
    computations in the corresponding number field will be faster
    than doing exact computations directly in ``AA`` or ``QQbar``.

    EXAMPLES:

    We can use this to compute the splitting field of a polynomial.
    (Unfortunately this takes an unreasonably long time for non-toy
    examples.)::

        sage: x = polygen(QQ)
        sage: p = x^3 + x^2 + x + 17
        sage: rts = p.roots(ring=QQbar, multiplicities=False)
        sage: splitting = number_field_elements_from_algebraics(rts, name='b')[0]; splitting
        Number Field in b with defining polynomial y^6 - 40*y^4 - 22*y^3 + 873*y^2 + 1386*y + 594
        sage: p.roots(ring=splitting)
        [(361/29286*b^5 - 19/3254*b^4 - 14359/29286*b^3 + 401/29286*b^2 + 18183/1627*b + 15930/1627, 1),
         (49/117144*b^5 - 179/39048*b^4 - 3247/117144*b^3 + 22553/117144*b^2 + 1744/4881*b - 17195/6508, 1),
         (-1493/117144*b^5 + 407/39048*b^4 + 60683/117144*b^3 - 24157/117144*b^2 - 56293/4881*b - 53033/6508, 1)]

        sage: # needs sage.symbolic
        sage: rt2 = AA(sqrt(2)); rt2
        1.414213562373095?
        sage: rt3 = AA(sqrt(3)); rt3
        1.732050807568878?
        sage: rt3a = QQbar(sqrt(3)); rt3a
        1.732050807568878?
        sage: qqI = QQbar.zeta(4); qqI
        I
        sage: z3 = QQbar.zeta(3); z3
        -0.500000000000000? + 0.866025403784439?*I
        sage: rt2b = rt3 + rt2 - rt3; rt2b
        1.414213562373095?
        sage: rt2c = z3 + rt2 - z3; rt2c
        1.414213562373095? + 0.?e-19*I
        sage: number_field_elements_from_algebraics(rt2)
        (Number Field in a with defining polynomial y^2 - 2, a,
         Ring morphism:
           From: Number Field in a with defining polynomial y^2 - 2
           To:   Algebraic Real Field
           Defn: a |--> 1.414213562373095?)
        sage: number_field_elements_from_algebraics((rt2,rt3))
        (Number Field in a with defining polynomial y^4 - 4*y^2 + 1, [-a^3 + 3*a, a^2 - 2],
         Ring morphism:
            From: Number Field in a with defining polynomial y^4 - 4*y^2 + 1
            To:   Algebraic Real Field
            Defn: a |--> -1.931851652578137?)

    ``rt3a`` is a real number in ``QQbar``.  Ordinarily, we'd get a homomorphism
    to ``AA`` (because all elements are real), but if we specify ``same_field=True``,
    we'll get a homomorphism back to ``QQbar``::

        sage: number_field_elements_from_algebraics(rt3a)                               # needs sage.symbolic
        (Number Field in a with defining polynomial y^2 - 3, a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 3
            To:   Algebraic Real Field
            Defn: a |--> 1.732050807568878?)

        sage: number_field_elements_from_algebraics(rt3a, same_field=True)              # needs sage.symbolic
        (Number Field in a with defining polynomial y^2 - 3, a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 3
            To:   Algebraic Field
            Defn: a |--> 1.732050807568878?)

    We've created ``rt2b`` in such a way that \\sage does not initially know
    that it's in a degree-2 extension of `\\QQ`::

        sage: number_field_elements_from_algebraics(rt2b)                               # needs sage.symbolic
        (Number Field in a with defining polynomial y^4 - 4*y^2 + 1, -a^3 + 3*a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^4 - 4*y^2 + 1
            To:   Algebraic Real Field
            Defn: a |--> -1.931851652578137?)

    We can specify ``minimal=True`` if we want the smallest number field::

        sage: number_field_elements_from_algebraics(rt2b, minimal=True)                 # needs sage.symbolic
        (Number Field in a with defining polynomial y^2 - 2, a, Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 2
            To:   Algebraic Real Field
            Defn: a |--> 1.414213562373095?)

    Things work fine with rational numbers, too::

        sage: number_field_elements_from_algebraics((QQbar(1/2), AA(17)))
        (Rational Field, [1/2, 17],
         Ring morphism:
            From: Rational Field
            To:   Algebraic Real Field
            Defn: 1 |--> 1)

    Or we can just pass in symbolic expressions, as long as they can be
    coerced into ``QQbar``::

        sage: number_field_elements_from_algebraics((sqrt(7), sqrt(9), sqrt(11)))       # needs sage.symbolic
        (Number Field in a with defining polynomial y^4 - 9*y^2 + 1,
         [-a^3 + 8*a, 3, -a^3 + 10*a],
         Ring morphism:
            From: Number Field in a with defining polynomial y^4 - 9*y^2 + 1
            To:   Algebraic Real Field
            Defn: a |--> 0.3354367396454047?)

    Here we see an example of doing some computations with number field
    elements, and then mapping them back into ``QQbar``::

        sage: # needs sage.symbolic
        sage: algebraics = (rt2, rt3, qqI, z3)
        sage: fld,nums,hom = number_field_elements_from_algebraics(algebraics)
        sage: fld,nums,hom  # random
        (Number Field in a with defining polynomial y^8 - y^4 + 1,
         [-a^5 + a^3 + a, a^6 - 2*a^2, a^6, -a^4],
         Ring morphism:
            From: Number Field in a with defining polynomial y^8 - y^4 + 1
            To:   Algebraic Field
            Defn: a |--> -0.2588190451025208? - 0.9659258262890683?*I)
        sage: (nfrt2, nfrt3, nfI, nfz3) = nums
        sage: hom(nfrt2)
        1.414213562373095? + 0.?e-18*I
        sage: nfrt2^2
        2
        sage: nfrt3^2
        3
        sage: nfz3 + nfz3^2
        -1
        sage: nfI^2
        -1
        sage: sum = nfrt2 + nfrt3 + nfI + nfz3; sum  # random
        a^5 + a^4 - a^3 + 2*a^2 - a - 1
        sage: hom(sum)
        2.646264369941973? + 1.866025403784439?*I
        sage: hom(sum) == rt2 + rt3 + qqI + z3
        True
        sage: [hom(n) for n in nums] == [rt2, rt3, qqI, z3]
        True

    It is also possible to have an embedded Number Field::

        sage: x = polygen(ZZ)
        sage: my_num = AA.polynomial_root(x^3 - 2, RIF(0,3))
        sage: res = number_field_elements_from_algebraics(my_num, embedded=True)
        sage: res[0].gen_embedding()
        1.259921049894873?
        sage: res[2]
        Ring morphism:
          From: Number Field in a with defining polynomial y^3 - 2 with a = 1.259921049894873?
          To:   Algebraic Real Field
          Defn: a |--> 1.259921049894873?

    ::

        sage: # needs sage.symbolic
        sage: elems = [2^(1/3), 3^(1/5)]
        sage: nf, nums, hom = number_field_elements_from_algebraics(elems,
        ....:                                                       embedded=True)
        sage: nf
        Number Field in a with defining polynomial y^15 - 9*y^10 + 21*y^5 - 3
         with a = 0.6866813218928813?
        sage: nums
        [a^10 - 5*a^5 + 2, -a^8 + 4*a^3]
        sage: hom
        Ring morphism:
          From: Number Field in a with defining polynomial y^15 - 9*y^10 + 21*y^5 - 3
                with a = 0.6866813218928813?
          To:   Algebraic Real Field
          Defn: a |--> 0.6866813218928813?

    Complex embeddings are possible as well::

        sage: # needs sage.symbolic
        sage: elems = [sqrt(5), 2^(1/3)+sqrt(3)*I, 3/4]
        sage: nf, nums, hom = number_field_elements_from_algebraics(elems,
        ....:                                                       embedded=True)
        sage: nf  # random (polynomial and root not unique)
        Number Field in a with defining polynomial y^24 - 6*y^23 ...- 9*y^2 + 1
          with a = 0.2598679? + 0.0572892?*I
        sage: nf.is_isomorphic(NumberField(
        ....:                      x^24 - 9*x^22 + 135*x^20 - 720*x^18 + 1821*x^16
        ....:                       - 3015*x^14 + 3974*x^12 - 3015*x^10 + 1821*x^8
        ....:                       - 720*x^6 + 135*x^4 - 9*x^2 + 1, 'a'))
        True
        sage: list(map(QQbar, nums)) == elems == list(map(hom, nums))
        True

    TESTS::

        sage: number_field_elements_from_algebraics(rt3)                                # needs sage.symbolic
        (Number Field in a with defining polynomial y^2 - 3, a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 3
            To:   Algebraic Real Field
            Defn: a |--> 1.732050807568878?)
        sage: number_field_elements_from_algebraics((rt2,qqI))                          # needs sage.symbolic
        (Number Field in a with defining polynomial y^4 + 1,
         [a^3 - a, a^2],
         Ring morphism:
           From: Number Field in a with defining polynomial y^4 + 1
           To:   Algebraic Field
           Defn: a |--> -0.7071067811865475? - 0.7071067811865475?*I)

    Note that for the first example, where \\sage does not realize that
    the number is real, we get a homomorphism to ``QQbar``::

        sage: number_field_elements_from_algebraics(rt2c)   # random                    # needs sage.symbolic
        (Number Field in a with defining polynomial y^4 + 2*y^2 + 4, 1/2*a^3,
         Ring morphism:
            From: Number Field in a with defining polynomial y^4 + 2*y^2 + 4
            To:   Algebraic Field
            Defn: a |--> -0.7071067811865475? - 1.224744871391589?*I)

    But with ``minimal=True``, we get a homomorphism to ``AA``::

        sage: number_field_elements_from_algebraics(rt2c, minimal=True)                 # needs sage.symbolic
        (Number Field in a with defining polynomial y^2 - 2, a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 2
            To:   Algebraic Real Field
            Defn: a |--> 1.414213562373095?)

    If we specify both ``minimal=True`` and ``same_field=True``, we get a second
    degree extension (minimal) that maps back to ``QQbar``::

        sage: number_field_elements_from_algebraics(rt2c, minimal=True,                 # needs sage.symbolic
        ....:                                       same_field=True)
        (Number Field in a with defining polynomial y^2 - 2, a,
         Ring morphism:
            From: Number Field in a with defining polynomial y^2 - 2
            To:   Algebraic Field
            Defn: a |--> 1.414213562373095?)

    Tests trivial cases::

        sage: number_field_elements_from_algebraics([], embedded=True)
        (Rational Field, [],
         Ring morphism:
           From: Rational Field
           To:   Algebraic Real Field
           Defn: 1 |--> 1)
        sage: number_field_elements_from_algebraics([1], embedded=True)
        (Rational Field, [1],
         Ring morphism:
           From: Rational Field
           To:   Algebraic Real Field
           Defn: 1 |--> 1)

    Test ``embedded`` for quadratic and cyclotomic fields::

        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(2/3))], embedded=False, minimal=True); v
        (Number Field in zeta6 with defining polynomial x^2 - x + 1,
         [zeta6 - 1],
         Ring morphism:
           From: Number Field in zeta6 with defining polynomial x^2 - x + 1
           To:   Algebraic Field
           Defn: zeta6 |--> 0.500000000000000? + 0.866025403784439?*I)
        sage: v[0].coerce_embedding()
        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(2/3))], embedded=True, minimal=True); v
        (Cyclotomic Field of order 6 and degree 2,
         [zeta6 - 1],
         Ring morphism:
           From: Cyclotomic Field of order 6 and degree 2
           To:   Algebraic Field
           Defn: zeta6 |--> 0.500000000000000? + 0.866025403784439?*I)
        sage: v[0].coerce_embedding()
        Generic morphism:
          From: Cyclotomic Field of order 6 and degree 2
          To:   Complex Lazy Field
          Defn: zeta6 -> 0.500000000000000? + 0.866025403784439?*I
        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(1/2))], embedded=False, minimal=True); v
        (Number Field in I with defining polynomial x^2 + 1,
         [I],
         Ring morphism:
           From: Number Field in I with defining polynomial x^2 + 1
           To:   Algebraic Field
           Defn: I |--> 1*I)
        sage: v[0].coerce_embedding()
        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(1/2))], embedded=True, minimal=True); v
        (Number Field in I with defining polynomial x^2 + 1 with I = 1*I,
         [I],
         Ring morphism:
           From: Number Field in I with defining polynomial x^2 + 1 with I = 1*I
           To:   Algebraic Field
           Defn: I |--> 1*I)
        sage: v[0].coerce_embedding()
        Generic morphism:
          From: Number Field in I with defining polynomial x^2 + 1 with I = 1*I
          To:   Complex Lazy Field
          Defn: I -> 1*I
        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(1/5))], embedded=False, minimal=True); v
        (Number Field in zeta10 with defining polynomial x^4 - x^3 + x^2 - x + 1,
         [zeta10],
         Ring morphism:
           From: Number Field in zeta10 with defining polynomial x^4 - x^3 + x^2 - x + 1
           To:   Algebraic Field
           Defn: zeta10 |--> 0.8090169943749474? + 0.5877852522924731?*I)
        sage: v[0].coerce_embedding()
        sage: v = number_field_elements_from_algebraics([QQbar((-1)^(1/5))], embedded=True, minimal=True); v
        (Cyclotomic Field of order 10 and degree 4,
         [zeta10],
         Ring morphism:
           From: Cyclotomic Field of order 10 and degree 4
           To:   Algebraic Field
           Defn: zeta10 |--> 0.8090169943749474? + 0.5877852522924731?*I)
        sage: v[0].coerce_embedding()
        Generic morphism:
          From: Cyclotomic Field of order 10 and degree 4
          To:   Complex Lazy Field
          Defn: zeta10 -> 0.809016994374948? + 0.587785252292473?*I

    Tests more complicated combinations::

        sage: # needs sage.libs.gap sage.symbolic
        sage: UCF = UniversalCyclotomicField()
        sage: E = UCF.gen(5)
        sage: L.<b> = NumberField(x^2 - 189*x + 16, embedding=200)
        sage: x = polygen(ZZ)
        sage: my_nums = [-52*E - 136*E^2 - 136*E^3 - 52*E^4,
        ....:            L.gen()._algebraic_(AA),
        ....:            sqrt(2), AA.polynomial_root(x^3 - 3, RIF(0,3)), 11/9, 1]
        sage: res = number_field_elements_from_algebraics(my_nums, embedded=True)
        sage: res[0]
        Number Field in a with defining polynomial y^24 - 107010*y^22 - 24*y^21 + ...
        + 250678447193040618624307096815048024318853254384 with a = 93.32530798172420?

    Test that the semantic of ``AA`` constructor does not affect this function (:issue:`36735`)::

        sage: AA((-1)^(2/3))
        1
        sage: number_field_elements_from_algebraics([(-1)^(2/3)])
        (Number Field in zeta6 with defining polynomial x^2 - x + 1,
         [zeta6 - 1],
         Ring morphism:
           From: Number Field in zeta6 with defining polynomial x^2 - x + 1
           To:   Algebraic Field
           Defn: zeta6 |--> 0.500000000000000? + 0.866025403784439?*I)
    """

QQx: PolynomialRing_field = QQ['x']
QQx_x: Polynomial_rational_flint = QQx.gen()
QQy: PolynomialRing_field = QQ['y']
QQy_y: Polynomial_rational_flint = QQy.gen()
QQxy: MPolynomialRing_libsingular = QQ['x', 'y']
QQxy_x: MPolynomialRing_libsingular = QQxy.gen(0)
QQxy_y: MPolynomialRing_libsingular = QQxy.gen(1)

def cmp_elements_with_same_minpoly(a, b, p):
    """
    Compare the algebraic elements ``a`` and ``b`` knowing that they have the
    same minimal polynomial ``p``.

    This is a helper function for comparison of algebraic elements (i.e. the
    methods :meth:`AlgebraicNumber._richcmp_` and
    :meth:`AlgebraicReal._richcmp_`).

    INPUT:

    - ``a``, ``b`` -- elements of the algebraic or the real algebraic field
      with same minimal polynomial

    - ``p`` -- the minimal polynomial

    OUTPUT:

    `-1`, `0`, `1`, ``None`` depending on whether `a < b`, `a = b` or `a > b` or
    the function did not succeed with the given precision of `a` and `b`.

    EXAMPLES::

        sage: from sage.rings.qqbar import cmp_elements_with_same_minpoly
        sage: x = polygen(ZZ)
        sage: p = x^2 - 2
        sage: a = AA.polynomial_root(p, RIF(1,2))
        sage: b = AA.polynomial_root(p, RIF(-2,-1))
        sage: cmp_elements_with_same_minpoly(a, b, p)
        1
        sage: cmp_elements_with_same_minpoly(-a, b, p)
        0
    """

class AlgebraicGeneratorRelation(SageObject):
    """
    A simple class for maintaining relations in the lattice of algebraic
    extensions.
    """
    child1: Incomplete
    child1_poly: Incomplete
    child2: Incomplete
    child2_poly: Incomplete
    parent: Incomplete
    def __init__(self, child1, child1_poly, child2, child2_poly, parent) -> None:
        """
        EXAMPLES::

            sage: from sage.rings.qqbar import AlgebraicGeneratorRelation
            sage: AlgebraicGeneratorRelation(None, None, None, None, None)
            <sage.rings.qqbar.AlgebraicGeneratorRelation object at ...>
        """

algebraic_generator_counter: int

class AlgebraicGenerator(SageObject):
    """
    An ``AlgebraicGenerator`` represents both an algebraic number `\\alpha` and
    the number field `\\QQ[\\alpha]`. There is a single ``AlgebraicGenerator``
    representing `\\QQ` (with `\\alpha=0`).

    The ``AlgebraicGenerator`` class is private, and should not be used
    directly.
    """
    def __init__(self, field, root) -> None:
        """
        Construct an ``AlgebraicGenerator`` object.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, qq_generator
            sage: y = polygen(QQ, 'y')
            sage: x = polygen(QQbar)
            sage: nf = NumberField(y^2 - y - 1, name='a', check=False)
            sage: root = ANRoot(x^2 - x - 1, RIF(1, 2))
            sage: gen = AlgebraicGenerator(nf, root)
            sage: gen
            Number Field in a with defining polynomial y^2 - y - 1 with a in 1.618033988749895?
            sage: gen.field()
            Number Field in a with defining polynomial y^2 - y - 1
            sage: gen.is_trivial()
            False
            sage: gen.union(qq_generator) is gen
            True
            sage: qq_generator.union(gen) is gen
            True
            sage: nf = NumberField(y^2 + 1, name='a', check=False)
            sage: root = ANRoot(x^2 + 1, CIF(0, 1))
            sage: x = AlgebraicGenerator(nf, root); x
            Number Field in a with defining polynomial y^2 + 1 with a in 1*I
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = QQbar(sqrt(2)) + QQbar(sqrt(3))
            sage: t.exactify()
            sage: type(t._descr._generator)
            <class 'sage.rings.qqbar.AlgebraicGenerator'>
            sage: loads(dumps(t)) == t
            True
        """
    def __hash__(self):
        """
        Return a hash value for ``self``. This will depend on the order that
        commands get executed at load time, so we do not test the value that is
        returned, just that it does not raise an error.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, qq_generator
            sage: _.<y> = QQ['y']
            sage: x = polygen(QQbar)
            sage: nf = NumberField(y^2 - y - 1, name='a', check=False)
            sage: root = ANRoot(x^2 - x - 1, RIF(1, 2))
            sage: gen = AlgebraicGenerator(nf, root)
            sage: hash(gen) # random
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` with another ``AlgebraicGenerator`` object.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, qq_generator
            sage: _.<y> = QQ['y']
            sage: x = polygen(QQbar)
            sage: nf = NumberField(y^2 - y - 1, name='a', check=False)
            sage: root = ANRoot(x^2 - x - 1, RIF(1, 2))
            sage: gen = AlgebraicGenerator(nf, root)
            sage: gen > qq_generator
            True
        """
    def is_complex(self):
        """
        Return ``True`` if this is a generator for a non-real number field.

        EXAMPLES::

            sage: z7 = QQbar.zeta(7)
            sage: g = z7._descr._generator
            sage: g.is_complex()
            True

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator
            sage: y = polygen(QQ, 'y')
            sage: x = polygen(QQbar)
            sage: nf = NumberField(y^2 - y - 1, name='a', check=False)
            sage: root = ANRoot(x^2 - x - 1, RIF(1, 2))
            sage: gen = AlgebraicGenerator(nf, root)
            sage: gen.is_complex()
            False
        """
    def root_as_algebraic(self):
        """
        Return the root attached to ``self`` as an algebraic number.

        EXAMPLES::

            sage: t = sage.rings.qqbar.qq_generator.root_as_algebraic(); t
            1
            sage: t.parent()
            Algebraic Real Field
        """
    def is_trivial(self):
        """
        Return ``True`` iff this is the trivial generator (alpha == 1), which
        does not actually extend the rationals.

        EXAMPLES::

            sage: from sage.rings.qqbar import qq_generator
            sage: qq_generator.is_trivial()
            True
        """
    def field(self):
        """
        Return the number field attached to ``self``.

        EXAMPLES::

            sage: from sage.rings.qqbar import qq_generator
            sage: qq_generator.field()
            Rational Field
        """
    def pari_field(self):
        """
        Return the PARI field attached to this generator.

        EXAMPLES::


            sage: from sage.rings.qqbar import qq_generator
            sage: qq_generator.pari_field()
            Traceback (most recent call last):
            ...
            ValueError: No PARI field attached to trivial generator

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, qq_generator
            sage: y = polygen(QQ)
            sage: x = polygen(QQbar)
            sage: nf = NumberField(y^2 - y - 1, name='a', check=False)
            sage: root = ANRoot(x^2 - x - 1, RIF(1, 2))
            sage: gen = AlgebraicGenerator(nf, root)
            sage: gen.pari_field()
            [[y^2 - y - 1, [2, 0], ...]
        """
    def conjugate(self):
        """
        If this generator is for the algebraic number `\\alpha`, return a
        generator for the complex conjugate of `\\alpha`.

        EXAMPLES::

            sage: from sage.rings.qqbar import AlgebraicGenerator
            sage: x = polygen(QQ); f = x^4 + x + 17
            sage: nf = NumberField(f,name='a')
            sage: b = f.roots(QQbar)[0][0]
            sage: root = b._descr
            sage: gen = AlgebraicGenerator(nf, root)
            sage: gen.conjugate()
            Number Field in a with defining polynomial x^4 + x + 17 with a in -1.436449997483091? + 1.374535713065812?*I
        """
    def union(self, other, name: str = 'a'):
        """
        Given generators ``self``, `\\alpha`, and ``other``, `\\beta`,
        ``self.union(other)`` gives a generator for the number field
        `\\QQ[\\alpha][\\beta]`.

        INPUT:

        - ``other`` -- an algebraic number
        - ``name`` -- string (default: ``'a'``); a name for the primitive element

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, qq_generator
            sage: _.<y> = QQ['y']
            sage: x = polygen(QQbar)
            sage: nf2 = NumberField(y^2 - 2, name='a', check=False)
            sage: root2 = ANRoot(x^2 - 2, RIF(1, 2))
            sage: gen2 = AlgebraicGenerator(nf2, root2)
            sage: gen2
            Number Field in a with defining polynomial y^2 - 2 with a in 1.414213562373095?
            sage: nf3 = NumberField(y^2 - 3, name='a', check=False)
            sage: root3 = ANRoot(x^2 - 3, RIF(1, 2))
            sage: gen3 = AlgebraicGenerator(nf3, root3)
            sage: gen3
            Number Field in a with defining polynomial y^2 - 3 with a in 1.732050807568878?
            sage: gen2.union(qq_generator) is gen2
            True
            sage: qq_generator.union(gen3) is gen3
            True
            sage: gen2.union(gen3, name='b')
            Number Field in b with defining polynomial y^4 - 4*y^2 + 1 with b in -1.931851652578137?
        """
    def super_poly(self, super, checked=None):
        """
        Given a generator ``gen`` and another generator ``super``, where ``super``
        is the result of a tree of ``union()`` operations where one of the
        leaves is ``gen``, ``gen.super_poly(super)`` returns a polynomial
        expressing the value of ``gen`` in terms of the value of ``super``
        (except that if ``gen`` is ``qq_generator``, ``super_poly()`` always
        returns None.)

        EXAMPLES::

            sage: from sage.rings.qqbar import AlgebraicGenerator, ANRoot, qq_generator
            sage: _.<y> = QQ['y']
            sage: x = polygen(QQbar)
            sage: nf2 = NumberField(y^2 - 2, name='a', check=False)
            sage: root2 = ANRoot(x^2 - 2, RIF(1, 2))
            sage: gen2 = AlgebraicGenerator(nf2, root2)
            sage: gen2
            Number Field in a with defining polynomial y^2 - 2 with a in 1.414213562373095?
            sage: nf3 = NumberField(y^2 - 3, name='a', check=False)
            sage: root3 = ANRoot(x^2 - 3, RIF(1, 2))
            sage: gen3 = AlgebraicGenerator(nf3, root3)
            sage: gen3
            Number Field in a with defining polynomial y^2 - 3 with a in 1.732050807568878?
            sage: gen2_3 = gen2.union(gen3)
            sage: gen2_3
            Number Field in a with defining polynomial y^4 - 4*y^2 + 1 with a in -1.931851652578137?
            sage: qq_generator.super_poly(gen2) is None
            True
            sage: gen2.super_poly(gen2_3)
            -a^3 + 3*a
            sage: gen3.super_poly(gen2_3)
            a^2 - 2
        """
    def __call__(self, elt):
        """
        Take an algebraic number which is represented as either a
        rational or a number field element, and which is in a subfield
        of the field generated by this generator. Lifts the number
        into the field of this generator, and returns either a
        ``Rational`` or a ``NumberFieldElement`` depending on whether
        this is the trivial generator.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot, AlgebraicGenerator, ANExtensionElement, ANRational
            sage: _.<y> = QQ['y']
            sage: x = polygen(QQbar)
            sage: nf2 = NumberField(y^2 - 2, name='a', check=False)
            sage: root2 = ANRoot(x^2 - 2, RIF(1, 2))
            sage: gen2 = AlgebraicGenerator(nf2, root2)
            sage: gen2
            Number Field in a with defining polynomial y^2 - 2 with a in 1.414213562373095?
            sage: sqrt2 = ANExtensionElement(gen2, nf2.gen())
            sage: nf3 = NumberField(y^2 - 3, name='a', check=False)
            sage: root3 = ANRoot(x^2 - 3, RIF(1, 2))
            sage: gen3 = AlgebraicGenerator(nf3, root3)
            sage: gen3
            Number Field in a with defining polynomial y^2 - 3 with a in 1.732050807568878?
            sage: sqrt3 = ANExtensionElement(gen3, nf3.gen())
            sage: gen2_3 = gen2.union(gen3)
            sage: gen2_3
            Number Field in a with defining polynomial y^4 - 4*y^2 + 1 with a in -1.931851652578137?
            sage: gen2_3(sqrt2)
            -a^3 + 3*a
            sage: gen2_3(ANRational(1/7))
            1/7
            sage: gen2_3(sqrt3)
            a^2 - 2
        """

class ANDescr(SageObject):
    """
    An ``AlgebraicNumber`` or ``AlgebraicReal`` is a wrapper around an
    ``ANDescr`` object. ``ANDescr`` is an abstract base class, which should
    never be directly instantiated; its concrete subclasses are ``ANRational``,
    ``ANBinaryExpr``, ``ANUnaryExpr``, ``ANRoot``, and ``ANExtensionElement``.
    ``ANDescr`` and all of its subclasses are for internal use, and should not
    be used directly.
    """
    def is_simple(self):
        """
        Check whether this descriptor represents a value with the same
        algebraic degree as the number field associated with the descriptor.

        This returns ``True`` if ``self`` is an ``ANRational``, or a minimal
        ``ANExtensionElement``.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRational
            sage: ANRational(1/2).is_simple()
            True

            sage: # needs sage.symbolic
            sage: rt2 = AA(sqrt(2))
            sage: rt3 = AA(sqrt(3))
            sage: rt2b = rt3 + rt2 - rt3
            sage: rt2.exactify()
            sage: rt2._descr.is_simple()
            True
            sage: rt2b.exactify()
            sage: rt2b._descr.is_simple()
            False
            sage: rt2b.simplify()
            sage: rt2b._descr.is_simple()
            True
        """
    def neg(self, n):
        """
        Negation of ``self``.

        EXAMPLES::

            sage: a = QQbar(sqrt(2))                                                    # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.neg(a)                                                              # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def invert(self, n):
        """
        1/self.

        EXAMPLES::

            sage: a = QQbar(sqrt(2))                                                    # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.invert(a)                                                           # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def abs(self, n):
        """
        Absolute value of ``self``.

        EXAMPLES::

            sage: a = QQbar(sqrt(2))                                                    # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.abs(a)                                                              # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def real(self, n):
        """
        Real part of ``self``.

        EXAMPLES::

            sage: a = QQbar(sqrt(-7))                                                   # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.real(a)                                                             # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def imag(self, n):
        """
        Imaginary part of ``self``.

        EXAMPLES::

            sage: a = QQbar(sqrt(-7))                                                   # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.imag(a)                                                             # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def conjugate(self, n):
        """
        Complex conjugate of ``self``.

        EXAMPLES::

            sage: a = QQbar(sqrt(-7))                                                   # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.conjugate(a)                                                        # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def norm(self, n):
        """
        Field norm of ``self`` from `\\overline{\\QQ}` to its real subfield
        `\\mathbf{A}`, i.e. the square of the usual complex absolute value.

        EXAMPLES::

            sage: a = QQbar(sqrt(-7))                                                   # needs sage.symbolic
            sage: b = a._descr                                                          # needs sage.symbolic
            sage: b.norm(a)                                                             # needs sage.symbolic
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """

class AlgebraicNumber_base(sage.structure.element.FieldElement):
    '''
    This is the common base class for algebraic numbers (complex
    numbers which are the zero of a polynomial in `\\ZZ[x]`) and algebraic
    reals (algebraic numbers which happen to be real).

    ``AlgebraicNumber`` objects can be created using ``QQbar`` (==
    ``AlgebraicNumberField()``), and ``AlgebraicReal`` objects can be created
    using ``AA`` (== ``AlgebraicRealField()``). They can be created either by
    coercing a rational or a symbolic expression, or by using the
    ``QQbar.polynomial_root()`` or ``AA.polynomial_root()`` method to
    construct a particular root of a polynomial with algebraic
    coefficients. Also, ``AlgebraicNumber`` and ``AlgebraicReal`` are closed
    under addition, subtraction, multiplication, division (except by
    0), and rational powers (including roots), except that for a
    negative ``AlgebraicReal``, taking a power with an even denominator returns
    an ``AlgebraicNumber`` instead of an ``AlgebraicReal``.

    ``AlgebraicNumber``   and   ``AlgebraicReal``   objects   can   be
    approximated  to  any desired  precision. They  can be  compared
    exactly; if the two numbers are very close, or are equal, this may
    require exact computation, which can be extremely slow.

    As long as exact computation is not triggered, computation with
    algebraic numbers should not be too much slower than computation with
    intervals. As mentioned above, exact computation is triggered
    when comparing two algebraic numbers which are very close together.
    This can be an explicit comparison in user code, but the following
    list of actions (not necessarily complete) can also trigger exact
    computation:

    - Dividing by an algebraic number which is very close to 0.

    - Using an algebraic number which is very close to 0 as the leading
      coefficient in a polynomial.

    - Taking a root of an algebraic number which is very close to 0.

    The exact definition of "very close" is subject to change; currently,
    we compute our best approximation of the two numbers using 128-bit
    arithmetic, and see if that\'s sufficient to decide the comparison.
    Note that comparing two algebraic numbers which are actually equal will
    always trigger exact computation, unless they are actually the same object.

    EXAMPLES::

        sage: sqrt(QQbar(2))
        1.414213562373095?
        sage: sqrt(QQbar(2))^2 == 2
        True
        sage: x = polygen(QQbar)
        sage: phi = QQbar.polynomial_root(x^2 - x - 1, RIF(1, 2))
        sage: phi
        1.618033988749895?
        sage: phi^2 == phi+1
        True
        sage: AA(sqrt(65537))                                                           # needs sage.symbolic
        256.0019531175495?
    '''
    def __init__(self, parent, x) -> None:
        """
        Initialize an algebraic number. The argument must be either
        a rational number, a Gaussian rational, or a subclass of ``ANDescr``.

        EXAMPLES::

            sage: AlgebraicReal(22/7)
            22/7
        """
    def __invert__(self):
        """
        TESTS::

            sage: ~AA(sqrt(~2))                                                         # needs sage.symbolic
            1.414213562373095?

            sage: z = QQbar(I).real()
            sage: a = ~z
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero in algebraic field
        """
    def __abs__(self):
        """
        TESTS::

            sage: abs(AA(sqrt(2) - sqrt(3)))                                            # needs sage.symbolic
            0.3178372451957823?
            sage: abs(QQbar(3+4*I))
            5
            sage: v = QQbar.zeta(3) + 1
            sage: v.exactify()
            sage: v.abs().minpoly()
            x - 1
        """
    def __hash__(self):
        """
        Compute a hash code for this number (equal algebraic numbers will
        have the same hash code, different algebraic numbers are likely
        to have different hash codes).

        This may trigger exact computation, but that is very unlikely.

        TESTS:

        The hash code is stable, even when the representation changes::

            sage: two = QQbar(4).nth_root(4)^2
            sage: two
            2.000000000000000?
            sage: h1 = hash(two)
            sage: two == 2
            True
            sage: two
            2
            sage: h2 = hash(two)
            sage: h1 == h2
            True

            sage: h1 = hash(QQbar.zeta(6))
            sage: h2 = hash(QQbar(1/2 + I*sqrt(3)/2))                                   # needs sage.symbolic
            sage: h1 == h2                                                              # needs sage.symbolic
            True

        Unfortunately, the hash code for algebraic numbers which are close
        enough to each other are the same. (This is inevitable, if
        equal algebraic reals give the same hash code and hashing does
        not always trigger exact computation.)::

            sage: h1 = hash(QQbar(0))
            sage: h2 = hash(QQbar(1/2^100))
            sage: hash(h1) == hash(h2)
            True
        """
    def __bool__(self) -> bool:
        """
        Check whether ``self`` is nonzero.

        This is fast if interval arithmetic proves it and in many other cases.
        Though, it might be slow in very particular cases where the number is
        actually zero or very close to zero.

        EXAMPLES::

            sage: bool(QQbar.zeta(2) + 1)
            False
            sage: bool(QQbar.zeta(7) / (2^500))
            True

            sage: bool(QQbar(I).imag())
            True
            sage: bool(QQbar(I).real())
            False

        The following is very fast, even though the number is really small::

            sage: a1 = QQbar(2).sqrt() - 16616132878186749607/11749380235262596085
            sage: a2 = QQbar(2).sqrt() - 16616132878186749607/11749380235262596085
            sage: bool(a1 + a2)
            True
            sage: bool(a1 - a2)
            False

            sage: a = QQbar(2).sqrt() - 16616132878186749607/11749380235262596085
            sage: b = QQbar(2).sqrt() - 6882627592338442563/4866752642924153522
            sage: c = QQbar(3).sqrt() - 142437039878091970439/82236063316189858921

            sage: # needs sage.symbolic
            sage: d = (59/2)**(1000/7)
            sage: e = (a + b + c) * (a + b - c) * (a - b) * (a - b - c) / d
            sage: bool(e)
            True
            sage: bool(e.abs() < 2**-500)
            True

        An identity between roots of unity::

            sage: z3 = QQbar.zeta(3)
            sage: z4 = QQbar.zeta(4)
            sage: z5 = QQbar.zeta(5)
            sage: p1 = (z3 + z4 + z5)**2
            sage: p2 = (z3 - z4 - z5)**2
            sage: p3 = (z3 - z4 + z5)**2
            sage: p4 = (z3 + z4 - z5)**2
            sage: bool(p1 - p2 + p3 - p4 - 8 * QQbar.zeta(15)**8)
            False

        Test some non-trivial zeros::

            sage: x = polygen(ZZ)
            sage: a = (AA(2).sqrt() + AA(3).sqrt() + AA(5).sqrt())^2
            sage: b = 10 + 2*max((x^4 - 62*x^2 - 240*x - 239).roots(AA, False))
            sage: bool(a - b)
            False

            sage: d = sum(AA(k)**(1/k) for k in [2..100])
            sage: bool(d * (a - b))
            False
            sage: bool((a - b) * d)
            False
            sage: bool(d * (a - b) * d)
            False
            sage: bool((a - b) / d)
            False

            sage: d = sum(QQbar(-k)**(1/k) for k in [2..100])
            sage: bool(d * (a - b))
            False
            sage: bool((a - b) * d)
            False
            sage: bool(d * (a - b) * d)
            False
            sage: bool((a - b) / d)
            False
        """
    def is_square(self):
        """
        Return whether or not this number is square.

        OUTPUT:

        (boolean)
        ``True`` in all cases for elements of ``QQbar``;
        ``True`` for nonnegative elements of ``AA``;
        otherwise ``False``

        EXAMPLES::

            sage: AA(2).is_square()
            True
            sage: AA(-2).is_square()
            False
            sage: QQbar(-2).is_square()
            True
            sage: QQbar(I).is_square()
            True
        """
    def is_integer(self):
        """
        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: QQbar(2).is_integer()
            True
            sage: QQbar(1/2).is_integer()
            False
        """
    def sqrt(self, all: bool = False, extend: bool = True):
        """
        Return the square root(s) of this number.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); ignored if ``self`` is in QQbar, or
          positive in AA. If ``self`` is negative in AA, do the following: if True,
          return a square root of ``self`` in QQbar, otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list of all square
          roots. If ``False``, return just one square root, or raise an :exc:`ValueError`
          if ``self`` is a negative element of AA and extend=False.

        OUTPUT:

        Either the principal square root of self, or a list of its
        square roots (with the principal one first).

        EXAMPLES::

            sage: AA(2).sqrt()
            1.414213562373095?

            sage: QQbar(I).sqrt()
            0.7071067811865475? + 0.7071067811865475?*I
            sage: QQbar(I).sqrt(all=True)
            [0.7071067811865475? + 0.7071067811865475?*I, -0.7071067811865475? - 0.7071067811865475?*I]

            sage: a = QQbar(0)
            sage: a.sqrt()
            0
            sage: a.sqrt(all=True)
            [0]

            sage: a = AA(0)
            sage: a.sqrt()
            0
            sage: a.sqrt(all=True)
            [0]

        This second example just shows that the program does not care where 0
        is defined, it gives the same answer regardless. After all, how many
        ways can you square-root zero?

        ::

            sage: AA(-2).sqrt()
            1.414213562373095?*I

            sage: AA(-2).sqrt(all=True)
            [1.414213562373095?*I, -1.414213562373095?*I]

            sage: AA(-2).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -2 is not a square in AA, being negative. Use extend = True for a square root in QQbar.
        """
    def nth_root(self, n, all: bool = False):
        """
        Return the ``n``-th root of this number.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list of
          all `n`-th roots as complex algebraic numbers

        .. WARNING::

            Note that for odd `n`, all ``False`` and negative real numbers,
            ``AlgebraicReal`` and ``AlgebraicNumber`` values give different
            answers: ``AlgebraicReal`` values prefer real results, and
            ``AlgebraicNumber`` values return the principal root.

        EXAMPLES::

            sage: AA(-8).nth_root(3)
            -2
            sage: QQbar(-8).nth_root(3)
            1.000000000000000? + 1.732050807568878?*I
            sage: QQbar.zeta(12).nth_root(15)
            0.9993908270190957? + 0.03489949670250097?*I

        You can get all ``n``-th roots of algebraic numbers::

            sage: AA(-8).nth_root(3, all=True)
            [1.000000000000000? + 1.732050807568878?*I,
            -2.000000000000000? + 0.?e-18*I,
            1.000000000000000? - 1.732050807568878?*I]

            sage: QQbar(1+I).nth_root(4, all=True)
            [1.069553932363986? + 0.2127475047267431?*I,
             -0.2127475047267431? + 1.069553932363986?*I,
             -1.069553932363986? - 0.2127475047267431?*I,
             0.2127475047267431? - 1.069553932363986?*I]

        TESTS::

            sage: AA(-8).nth_root(3, all=True)[1]
            -2.000000000000000? + 0.?e-18*I
            sage: _.parent()
            Algebraic Field

            sage: AA(-2).nth_root(5, all=True) == QQbar(-2).nth_root(5, all=True)   # long time
            True
        """
    def as_number_field_element(self, minimal: bool = False, embedded: bool = False, prec: int = 53):
        """
        Return a number field containing this value, a representation of
        this value as an element of that number field, and a homomorphism
        from the number field back to ``AA`` or ``QQbar``.

        INPUT:

        - ``minimal`` -- boolean (default: ``False``); whether to minimize the
          degree of the extension

        - ``embedded`` -- boolean (default: ``False``); whether to make the
          NumberField embedded

        - ``prec`` -- integer (default: 53); the number of bit of precision
          to guarantee finding real roots

        This may not return the smallest such number field, unless
        ``minimal=True`` is specified.

        To compute a single number field containing multiple algebraic
        numbers, use the function
        ``number_field_elements_from_algebraics`` instead.

        EXAMPLES::

            sage: QQbar(sqrt(8)).as_number_field_element()                              # needs sage.symbolic
            (Number Field in a with defining polynomial y^2 - 2, 2*a,
             Ring morphism:
                From: Number Field in a with defining polynomial y^2 - 2
                To:   Algebraic Real Field
                Defn: a |--> 1.414213562373095?)

            sage: x = polygen(ZZ)
            sage: p = x^3 + x^2 + x + 17
            sage: (rt,) = p.roots(ring=AA, multiplicities=False); rt
            -2.804642726932742?

            sage: (nf, elt, hom) = rt.as_number_field_element()
            sage: nf, elt, hom
            (Number Field in a with defining polynomial y^3 - 2*y^2 - 31*y - 50,
             a^2 - 5*a - 19,
             Ring morphism:
               From: Number Field in a with defining polynomial y^3 - 2*y^2 - 31*y - 50
               To:   Algebraic Real Field
               Defn: a |--> 7.237653139801104?)
            sage: elt == rt
            False
            sage: AA(elt)
            Traceback (most recent call last):
            ...
            ValueError: need a real or complex embedding to convert a non rational
            element of a number field into an algebraic number
            sage: hom(elt) == rt
            True

        Creating an element of an embedded number field::

            sage: (nf, elt, hom) = rt.as_number_field_element(embedded=True)
            sage: nf.coerce_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial y^3 - 2*y^2 - 31*y - 50
                    with a = 7.237653139801104?
              To:   Algebraic Real Field
              Defn: a -> 7.237653139801104?
            sage: elt
            a^2 - 5*a - 19
            sage: elt.parent() == nf
            True
            sage: hom(elt).parent()
            Algebraic Real Field
            sage: hom(elt) == rt
            True
            sage: elt == rt
            True
            sage: AA(elt)
            -2.804642726932742?
            sage: RR(elt)
            -2.80464272693274

        A complex algebraic number as an element of an embedded number field::

            sage: # needs sage.symbolic
            sage: num = QQbar(sqrt(2) + 3^(1/3)*I)
            sage: nf, elt, hom = num.as_number_field_element(embedded=True)
            sage: hom(elt).parent() is QQbar
            True
            sage: nf.coerce_embedding() is not None
            True
            sage: QQbar(elt) == num == hom(elt)
            True

        We see an example where we do not get the minimal number field unless
        we specify ``minimal=True``::

            sage: # needs sage.symbolic
            sage: rt2 = AA(sqrt(2))
            sage: rt3 = AA(sqrt(3))
            sage: rt3b = rt2 + rt3 - rt2
            sage: rt3b.as_number_field_element()
            (Number Field in a with defining polynomial y^4 - 4*y^2 + 1, a^2 - 2,
             Ring morphism:
                From: Number Field in a with defining polynomial y^4 - 4*y^2 + 1
                To:   Algebraic Real Field
                Defn: a |--> -1.931851652578137?)
            sage: rt3b.as_number_field_element(minimal=True)
            (Number Field in a with defining polynomial y^2 - 3, a,
             Ring morphism:
               From: Number Field in a with defining polynomial y^2 - 3
               To:   Algebraic Real Field
               Defn: a |--> 1.732050807568878?)
        """
    def is_integral(self):
        """
        Check if this number is an algebraic integer.

        EXAMPLES::

            sage: QQbar(sqrt(-23)).is_integral()
            True
            sage: AA(sqrt(23/2)).is_integral()
            False

        TESTS:

        Method should return the same value as :meth:`NumberFieldElement.is_integral`::

             sage: for a in [QQbar(2^(1/3)), AA(2^(1/3)), QQbar(sqrt(1/2)), AA(1/2), AA(2), QQbar(1/2)]:
             ....:    assert a.as_number_field_element()[1].is_integral() == a.is_integral()
        """
    def exactify(self) -> None:
        """
        Compute an exact representation for this number.

        EXAMPLES::

            sage: two = QQbar(4).nth_root(4)^2
            sage: two
            2.000000000000000?
            sage: two.exactify()
            sage: two
            2
        """
    def simplify(self) -> None:
        """
        Compute an exact representation for this number, in the
        smallest possible number field.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: rt2 = AA(sqrt(2))
            sage: rt3 = AA(sqrt(3))
            sage: rt2b = rt3 + rt2 - rt3
            sage: rt2b.exactify()
            sage: rt2b._exact_value()
            a^3 - 3*a where a^4 - 4*a^2 + 1 = 0 and a in -0.5176380902050415?
            sage: rt2b.simplify()
            sage: rt2b._exact_value()
            a where a^2 - 2 = 0 and a in 1.414213562373095?
        """
    def minpoly(self):
        """
        Compute the minimal polynomial of this algebraic number.
        The minimal polynomial is the monic polynomial of least degree
        having this number as a root; it is unique.

        EXAMPLES::

            sage: QQbar(4).sqrt().minpoly()
            x - 2
            sage: ((QQbar(2).nth_root(4))^2).minpoly()
            x^2 - 2
            sage: v = sqrt(QQbar(2)) + sqrt(QQbar(3)); v
            3.146264369941973?
            sage: p = v.minpoly(); p
            x^4 - 10*x^2 + 1
            sage: p(RR(v.real()))
            1.31006316905768e-14
        """
    def degree(self):
        """
        Return the degree of this algebraic number (the degree of its
        minimal polynomial, or equivalently, the degree of the smallest
        algebraic extension of the rationals containing this number).

        EXAMPLES::

            sage: QQbar(5/3).degree()
            1
            sage: sqrt(QQbar(2)).degree()
            2
            sage: QQbar(17).nth_root(5).degree()
            5
            sage: sqrt(3+sqrt(QQbar(8))).degree()
            2
        """
    def interval_fast(self, field):
        """
        Given a :class:`RealIntervalField` or
        :class:`ComplexIntervalField`, compute the value of this number
        using interval arithmetic of at least the precision of the field,
        and return the value in that field. (More precision may be used
        in the computation.)  The returned interval may be arbitrarily
        imprecise, if this number is the result of a sufficiently long
        computation chain.

        EXAMPLES::

            sage: x = AA(2).sqrt()
            sage: x.interval_fast(RIF)
            1.414213562373095?
            sage: x.interval_fast(RealIntervalField(200))
            1.414213562373095048801688724209698078569671875376948073176680?
            sage: x = QQbar(I).sqrt()
            sage: x.interval_fast(CIF)
            0.7071067811865475? + 0.7071067811865475?*I
            sage: x.interval_fast(RIF)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert complex interval 0.7071067811865475244? + 0.7071067811865475244?*I to real interval
        """
    def interval_diameter(self, diam):
        """
        Compute an interval representation of ``self`` with ``diameter()`` at
        most ``diam``. The precision of the returned value is unpredictable.

        EXAMPLES::

            sage: AA(2).sqrt().interval_diameter(1e-10)
            1.4142135623730950488?
            sage: AA(2).sqrt().interval_diameter(1e-30)
            1.41421356237309504880168872420969807857?
            sage: QQbar(2).sqrt().interval_diameter(1e-10)
            1.4142135623730950488?
            sage: QQbar(2).sqrt().interval_diameter(1e-30)
            1.41421356237309504880168872420969807857?
        """
    def interval(self, field):
        """
        Given an interval (or ball) field (real or complex, as appropriate) of
        precision `p`, compute an interval representation of ``self`` with
        ``diameter()`` at most `2^{-p}`; then round that representation into
        the given field. Here ``diameter()`` is relative diameter for
        intervals not containing 0, and absolute diameter for
        intervals that do contain 0; thus, if the returned interval
        does not contain 0, it has at least `p-1` good bits.

        EXAMPLES::

            sage: RIF64 = RealIntervalField(64)
            sage: x = AA(2).sqrt()
            sage: y = x*x
            sage: y = 1000 * y - 999 * y
            sage: y.interval_fast(RIF64)
            2.000000000000000?
            sage: y.interval(RIF64)
            2.000000000000000000?
            sage: CIF64 = ComplexIntervalField(64)
            sage: x = QQbar.zeta(11)
            sage: x.interval_fast(CIF64)
            0.8412535328311811689? + 0.5406408174555975821?*I
            sage: x.interval(CIF64)
            0.8412535328311811689? + 0.5406408174555975822?*I
            sage: x.interval(CBF) # abs tol 1e-16
            [0.8412535328311812 +/- 3.12e-17] + [0.5406408174555976 +/- 1.79e-17]*I

        The following implicitly use this method::

            sage: RIF(AA(5).sqrt())
            2.236067977499790?
            sage: AA(-5).sqrt().interval(RIF)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.236067977499790?*I to real interval

        TESTS:

        Check that :issue:`20209` is fixed::

            sage: RIF(QQbar(2).sqrt())
            1.414213562373095?
            sage: RIF(QQbar.gen() + QQbar(2).sqrt() - QQbar.gen())
            1.414213562373095?
            sage: RIF((QQbar.gen() + QQbar(2).sqrt() - QQbar.gen()).sqrt())
            1.189207115002722?

            sage: RealIntervalField(129)(QQbar(3).sqrt())
            1.73205080756887729352744634150587236695?
            sage: RIF(QQbar.gen())
            Traceback (most recent call last):
            ...
            TypeError: unable to convert I to real interval
        """
    def radical_expression(self):
        """
        Attempt to obtain a symbolic expression using radicals. If no
        exact symbolic expression can be found, the algebraic number
        will be returned without modification.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: AA(1/sqrt(5)).radical_expression()
            sqrt(1/5)
            sage: AA(sqrt(5 + sqrt(5))).radical_expression()
            sqrt(sqrt(5) + 5)
            sage: QQbar.zeta(5).radical_expression()
            1/4*sqrt(5) + 1/2*sqrt(-1/2*sqrt(5) - 5/2) - 1/4
            sage: x = polygen(QQ, 'x')
            sage: a = (x^7 - x - 1).roots(AA, False)[0]
            sage: a.radical_expression()
            1.112775684278706?
            sage: a.radical_expression().parent() == SR
            False
            sage: a = sorted((x^7-x-1).roots(QQbar, False), key=imag)[0]
            sage: a.radical_expression()
            -0.3636235193291805? - 0.9525611952610331?*I
            sage: QQbar.zeta(5).imag().radical_expression()
            1/2*sqrt(1/2*sqrt(5) + 5/2)
            sage: AA(5/3).radical_expression()
            5/3
            sage: AA(5/3).radical_expression().parent() == SR
            True
            sage: QQbar(0).radical_expression()
            0

        TESTS:

        In this example we find the correct answer despite the fact that
        multiple roots overlap with the current value. As a consequence,
        the precision of the evaluation will have to be increased.

        ::

            sage: # needs sage.symbolic
            sage: a = AA(sqrt(2) + 10^25)
            sage: p = a.minpoly()
            sage: v = a._value
            sage: f = ComplexIntervalField(v.prec())
            sage: var('x')
            x
            sage: [f(b.rhs()).overlaps(f(v)) for b in SR(p).solve(x)]
            [True, True]
            sage: a.radical_expression()
            sqrt(2) + 10000000000000000000000000
        """

class AlgebraicNumber(AlgebraicNumber_base):
    """
    The class for algebraic numbers (complex numbers which are the roots
    of a polynomial with integer coefficients). Much of its functionality
    is inherited from :class:`AlgebraicNumber_base`.

    .. automethod:: _richcmp_
    """
    def __init__(self, x) -> None:
        """
        Initialize this AlgebraicNumber object.

        EXAMPLES::

            sage: t = QQbar.zeta(5)
            sage: type(t)
            <class 'sage.rings.qqbar.AlgebraicNumber'>
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: t = QQbar.zeta(5)
            sage: loads(dumps(t)) == t
            True
        """
    def __float__(self) -> float:
        """
        Compute a good float approximation to ``self``. Works only if the
        imaginary component of ``self`` is exactly zero; otherwise it
        raises a :exc:`ValueError`.

        EXAMPLES::

            sage: QQbar(sqrt(2)).__float__()                                            # needs sage.symbolic
            1.414213562373095
            sage: float(QQbar(-22/7))
            -3.1428571428571432
            sage: float(QQbar.zeta(3))
            Traceback (most recent call last):
            ...
            ValueError: Cannot coerce algebraic number with nonzero imaginary part to algebraic real
        """
    def __complex__(self) -> complex:
        """
        Compute a good complex approximation to ``self``.

        EXAMPLES::

            sage: QQbar(sqrt(2)).__complex__()                                          # needs sage.symbolic
            (1.414213562373095+0j)
            sage: complex(QQbar.zeta(3))
            (-0.5+0.8660254037844386j)
        """
    def real(self):
        """
        Return the real part of ``self``.

        EXAMPLES::

            sage: QQbar.zeta(5).real()
            0.3090169943749474?
        """
    def imag(self):
        """
        Return the imaginary part of ``self``.

        EXAMPLES::

            sage: QQbar.zeta(7).imag()
            0.7818314824680299?
        """
    def conjugate(self):
        """
        Return the complex conjugate of ``self``.

        EXAMPLES::

            sage: QQbar(3 + 4*I).conjugate()
            3 - 4*I
            sage: QQbar.zeta(7).conjugate()
            0.6234898018587335? - 0.7818314824680299?*I
            sage: QQbar.zeta(7) + QQbar.zeta(7).conjugate()
            1.246979603717467? + 0.?e-18*I
        """
    def norm(self):
        """
        Return ``self * self.conjugate()``.

        This is the algebraic definition of norm, if we view ``QQbar``
        as ``AA[I]``.

        EXAMPLES::

            sage: QQbar(3 + 4*I).norm()
            25
            sage: type(QQbar(I).norm())
            <class 'sage.rings.qqbar.AlgebraicReal'>
            sage: QQbar.zeta(1007).norm()
            1.000000000000000?
        """
    def interval_exact(self, field):
        """
        Given a :class:`ComplexIntervalField`, compute the best possible
        approximation of this number in that field. Note that if
        either the real or imaginary parts of this number are
        sufficiently close to some floating-point number (and, in
        particular, if either is exactly representable in floating-point),
        then this will trigger exact computation, which may be very slow.

        EXAMPLES::

            sage: a = QQbar(I).sqrt(); a
            0.7071067811865475? + 0.7071067811865475?*I
            sage: a.interval_exact(CIF)
            0.7071067811865475? + 0.7071067811865475?*I
            sage: b = QQbar((1+I)*sqrt(2)/2)                                            # needs sage.symbolic
            sage: (a - b).interval(CIF)                                                 # needs sage.symbolic
            0.?e-19 + 0.?e-18*I
            sage: (a - b).interval_exact(CIF)                                           # needs sage.symbolic
            0
        """
    def complex_number(self, field):
        """
        Given the complex field ``field``, compute an accurate approximation of
        this element in that field.

        The approximation will be off by at most two ulp's in each component,
        except for components which are very close to zero, which will have an
        absolute error at most `2^{-prec+1}` where ``prec`` is the precision of
        the field.

        EXAMPLES::

            sage: a = QQbar.zeta(5)
            sage: a.complex_number(CC)
            0.309016994374947 + 0.951056516295154*I

            sage: b = QQbar(2).sqrt() + QQbar(3).sqrt() * QQbar.gen()
            sage: b.complex_number(ComplexField(128))
            1.4142135623730950488016887242096980786 + 1.7320508075688772935274463415058723669*I
        """
    def complex_exact(self, field):
        """
        Given a :class:`ComplexField`, return the best possible approximation of
        this number in that field. Note that if either component is
        sufficiently close to the halfway point between two floating-point
        numbers in the corresponding :class:`RealField`, then this will trigger
        exact computation, which may be very slow.

        EXAMPLES::

            sage: a = QQbar.zeta(9) + QQbar(I) + QQbar.zeta(9).conjugate(); a
            1.532088886237957? + 1.000000000000000?*I
            sage: a.complex_exact(CIF)
            1.532088886237957? + 1*I
        """
    def multiplicative_order(self):
        """
        Compute the multiplicative order of this algebraic number.

        That is, find the smallest positive integer `n` such
        that `x^n = 1`. If there is no such `n`, returns ``+Infinity``.

        We first check that ``abs(x)`` is very close to 1. If so, we compute
        `x` exactly and examine its argument.

        EXAMPLES::

            sage: QQbar(-sqrt(3)/2 - I/2).multiplicative_order()                        # needs sage.symbolic
            12
            sage: QQbar(1).multiplicative_order()
            1
            sage: QQbar(-I).multiplicative_order()
            4
            sage: QQbar(707/1000 + 707/1000*I).multiplicative_order()
            +Infinity
            sage: QQbar(3/5 + 4/5*I).multiplicative_order()
            +Infinity
        """
    def rational_argument(self):
        """
        Return the argument of ``self``, divided by `2\\pi`, as long as this
        result is rational. Otherwise returns ``None``. Always triggers
        exact computation.

        EXAMPLES::

            sage: QQbar((1+I)*(sqrt(2)+sqrt(5))).rational_argument()                    # needs sage.symbolic
            1/8
            sage: QQbar(-1 + I*sqrt(3)).rational_argument()                             # needs sage.symbolic
            1/3
            sage: QQbar(-1 - I*sqrt(3)).rational_argument()                             # needs sage.symbolic
            -1/3
            sage: QQbar(3+4*I).rational_argument() is None
            True
            sage: (QQbar(2)**(1/5) * QQbar.zeta(7)**2).rational_argument()  # long time
            2/7
            sage: (QQbar.zeta(73)**5).rational_argument()
            5/73
            sage: (QQbar.zeta(3)^65536).rational_argument()
            1/3
        """

class AlgebraicReal(AlgebraicNumber_base):
    """
    A real algebraic number.

    .. automethod:: _richcmp_
    """
    def __init__(self, x) -> None:
        """
        Create an algebraic real from x, possibly taking the real part of x.

        TESTS:

        Both of the following examples, from :issue:`11728`, trigger
        taking the real part below. This is necessary because
        sometimes a very small (e.g., 1e-17) complex part appears in a
        complex interval used to create an AlgebraicReal.::

            sage: a = QQbar((-1)^(1/4)); b = AA(a^3-a)                                  # needs sage.symbolic
            sage: t = b.as_number_field_element()                                       # needs sage.symbolic
            sage: b*1                                                                   # needs sage.symbolic
            -1.414213562373095?
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: t = AA(sqrt(2))                                                       # needs sage.symbolic
            sage: loads(dumps(t)) == t                                                  # needs sage.symbolic
            True
        """
    def floor(self):
        """
        Return the largest integer not greater than ``self``.

        EXAMPLES::

            sage: AA(sqrt(2)).floor()                                                   # needs sage.symbolic
            1
            sage: AA(-sqrt(2)).floor()                                                  # needs sage.symbolic
            -2
            sage: AA(42).floor()
            42

        TESTS:

        Check that :issue:`15501` is fixed::

            sage: a = QQbar((-1)^(1/4)).real()                                          # needs sage.symbolic
            sage: (floor(a-a) + a).parent()                                             # needs sage.symbolic
            Algebraic Real Field
        """
    def ceil(self):
        """
        Return the smallest integer not smaller than ``self``.

        EXAMPLES::

            sage: AA(sqrt(2)).ceil()                                                    # needs sage.symbolic
            2
            sage: AA(-sqrt(2)).ceil()                                                   # needs sage.symbolic
            -1
            sage: AA(42).ceil()
            42
        """
    def round(self):
        """
        Round ``self`` to the nearest integer.

        EXAMPLES::

            sage: AA(sqrt(2)).round()                                                   # needs sage.symbolic
            1
            sage: AA(1/2).round()
            1
            sage: AA(-1/2).round()
            -1
        """
    def trunc(self):
        """
        Round ``self`` to the nearest integer toward zero.

        EXAMPLES::

            sage: AA(sqrt(2)).trunc()                                                   # needs sage.symbolic
            1
            sage: AA(-sqrt(2)).trunc()                                                  # needs sage.symbolic
            -1
            sage: AA(1).trunc()
            1
            sage: AA(-1).trunc()
            -1
        """
    def real(self):
        """
        Return the real part of this algebraic real.

        It always returns ``self``.

        EXAMPLES::

            sage: a = AA(sqrt(2) + sqrt(3))                                             # needs sage.symbolic
            sage: a.real()                                                              # needs sage.symbolic
            3.146264369941973?
            sage: a.real() is a                                                         # needs sage.symbolic
            True
        """
    def imag(self):
        """
        Return the imaginary part of this algebraic real.

        It always returns 0.

        EXAMPLES::

            sage: a = AA(sqrt(2) + sqrt(3))                                             # needs sage.symbolic
            sage: a.imag()                                                              # needs sage.symbolic
            0
            sage: parent(a.imag())                                                      # needs sage.symbolic
            Algebraic Real Field
        """
    def conjugate(self):
        """
        Return the complex conjugate of ``self``, i.e. returns itself.

        EXAMPLES::

            sage: a = AA(sqrt(2) + sqrt(3))                                             # needs sage.symbolic
            sage: a.conjugate()                                                         # needs sage.symbolic
            3.146264369941973?
            sage: a.conjugate() is a                                                    # needs sage.symbolic
            True
        """
    def multiplicative_order(self):
        """
        Compute the multiplicative order of this real algebraic number.

        That is, find the smallest positive integer `n` such
        that `x^n = 1`. If there is no such `n`, returns ``+Infinity``.

        We first check that ``abs(x)`` is very close to 1. If so, we compute
        `x` exactly and compare it to `1` and `-1`.

        EXAMPLES::

            sage: AA(1).multiplicative_order()
            1
            sage: AA(-1).multiplicative_order()
            2
            sage: AA(5).sqrt().multiplicative_order()
            +Infinity
        """
    def sign(self):
        """
        Compute the sign of this algebraic number (return `-1` if negative,
        `0` if zero, or `1` if positive).

        This computes an interval enclosing this number using 128-bit interval
        arithmetic; if this interval includes 0, then fall back to
        exact computation (which can be very slow).

        EXAMPLES::

            sage: AA(-5).nth_root(7).sign()
            -1
            sage: (AA(2).sqrt() - AA(2).sqrt()).sign()
            0

            sage: a = AA(2).sqrt() + AA(3).sqrt() - 58114382797550084497/18470915334626475921
            sage: a.sign()
            1
            sage: b = AA(2).sqrt() + AA(3).sqrt() - 2602510228533039296408/827174681630786895911
            sage: b.sign()
            -1

            sage: c = AA(5)**(1/3) - 1437624125539676934786/840727688792155114277
            sage: c.sign()
            1

            sage: (((a+b)*(a+c)*(b+c))**9 / (a*b*c)).sign()
            1
            sage: (a-b).sign()
            1
            sage: (b-a).sign()
            -1
            sage: (a*b).sign()
            -1
            sage: ((a*b).abs() + a).sign()
            1
            sage: (a*b - b*a).sign()
            0

            sage: a = AA(sqrt(1/2))                                                     # needs sage.symbolic
            sage: b = AA(-sqrt(1/2))                                                    # needs sage.symbolic
            sage: (a + b).sign()                                                        # needs sage.symbolic
            0

        TESTS:

        We avoid calling :meth:`exactify()` for trivial differences. The
        following example will take a long time (more than 5 seconds)
        when calling ``y.exactify()``::

            sage: # needs sage.symbolic
            sage: x1 = AA(2^(1/50))
            sage: x2 = AA(2^(1/50))
            sage: y = x1 - x2
            sage: y.sign()
            0

        Simplify to rationals for binary operations when computing the sign::

            sage: a = AA(2^(1/60))                                                      # needs sage.symbolic
            sage: b = a - (a + 1)                                                       # needs sage.symbolic
            sage: (b + 1).sign()                                                        # needs sage.symbolic
            0
        """
    def interval_exact(self, field):
        """
        Given a :class:`RealIntervalField`, compute the best possible
        approximation of this number in that field. Note that if this
        number is sufficiently close to some floating-point number
        (and, in particular, if this number is exactly representable in
        floating-point), then this will trigger exact computation, which
        may be very slow.

        EXAMPLES::

            sage: x = AA(2).sqrt()
            sage: y = x*x
            sage: x.interval(RIF)
            1.414213562373095?
            sage: x.interval_exact(RIF)
            1.414213562373095?
            sage: y.interval(RIF)
            2.000000000000000?
            sage: y.interval_exact(RIF)
            2
            sage: z = 1 + AA(2).sqrt() / 2^200
            sage: z.interval(RIF)
            1.000000000000001?
            sage: z.interval_exact(RIF)
            1.000000000000001?

        TESTS:

        Check that :issue:`26898` is fixed.  This calculation triggers the 40 bits
        of extra precision below, and the point is not that the length of the list
        is seven, but that the code runs in a reasonable time::

            sage: R.<x> = QQbar[]
            sage: roots = (x^7 + 27/4).roots()
            sage: from sage.rings.qqbar import QQbar_hash_offset
            sage: len([(r[0] + QQbar_hash_offset).interval_exact(CIF) for r in roots])
            7
        """
    def real_number(self, field):
        """
        Given a :class:`RealField`, compute a good approximation to ``self`` in
        that field. The approximation will be off by at most two
        ulp's, except for numbers which are very close to 0, which
        will have an absolute error at most
        ``2**(-(field.prec()-1))``. Also, the rounding mode of the
        field is respected.

        EXAMPLES::

            sage: x = AA(2).sqrt()^2
            sage: x.real_number(RR)
            2.00000000000000
            sage: x.real_number(RealField(53, rnd='RNDD'))
            1.99999999999999
            sage: x.real_number(RealField(53, rnd='RNDU'))
            2.00000000000001
            sage: x.real_number(RealField(53, rnd='RNDZ'))
            1.99999999999999
            sage: (-x).real_number(RR)
            -2.00000000000000
            sage: (-x).real_number(RealField(53, rnd='RNDD'))
            -2.00000000000001
            sage: (-x).real_number(RealField(53, rnd='RNDU'))
            -1.99999999999999
            sage: (-x).real_number(RealField(53, rnd='RNDZ'))
            -1.99999999999999
            sage: (x-2).real_number(RR)
            5.42101086242752e-20
            sage: (x-2).real_number(RealField(53, rnd='RNDD'))
            -1.08420217248551e-19
            sage: (x-2).real_number(RealField(53, rnd='RNDU'))
            2.16840434497101e-19
            sage: (x-2).real_number(RealField(53, rnd='RNDZ'))
            0.000000000000000
            sage: y = AA(2).sqrt()
            sage: y.real_number(RR)
            1.41421356237309
            sage: y.real_number(RealField(53, rnd='RNDD'))
            1.41421356237309
            sage: y.real_number(RealField(53, rnd='RNDU'))
            1.41421356237310
            sage: y.real_number(RealField(53, rnd='RNDZ'))
            1.41421356237309
        """
    def __float__(self) -> float:
        """
        Compute a good float approximation to ``self``.

        EXAMPLES::

            sage: AA(golden_ratio).__float__()                                          # needs sage.symbolic
            1.618033988749895
            sage: float(AA(sqrt(11)))                                                   # needs sage.symbolic
            3.3166247903554
        """
    def real_exact(self, field):
        """
        Given a :class:`RealField`, compute the best possible approximation of
        this number in that field. Note that if this number is
        sufficiently close to the halfway point between two
        floating-point numbers in the field (for the default
        round-to-nearest mode) or if the number is sufficiently close
        to a floating-point number in the field (for directed rounding
        modes), then this will trigger exact computation, which may be
        very slow.

        The rounding mode of the field is respected.

        EXAMPLES::

            sage: x = AA(2).sqrt()^2
            sage: x.real_exact(RR)
            2.00000000000000
            sage: x.real_exact(RealField(53, rnd='RNDD'))
            2.00000000000000
            sage: x.real_exact(RealField(53, rnd='RNDU'))
            2.00000000000000
            sage: x.real_exact(RealField(53, rnd='RNDZ'))
            2.00000000000000
            sage: (-x).real_exact(RR)
            -2.00000000000000
            sage: (-x).real_exact(RealField(53, rnd='RNDD'))
            -2.00000000000000
            sage: (-x).real_exact(RealField(53, rnd='RNDU'))
            -2.00000000000000
            sage: (-x).real_exact(RealField(53, rnd='RNDZ'))
            -2.00000000000000
            sage: y = (x-2).real_exact(RR).abs()
            sage: y == 0.0 or y == -0.0 # the sign of 0.0 is not significant in MPFI
            True
            sage: y = (x-2).real_exact(RealField(53, rnd='RNDD'))
            sage: y == 0.0 or y == -0.0 # same as above
            True
            sage: y = (x-2).real_exact(RealField(53, rnd='RNDU'))
            sage: y == 0.0 or y == -0.0 # idem
            True
            sage: y = (x-2).real_exact(RealField(53, rnd='RNDZ'))
            sage: y == 0.0 or y == -0.0 # ibidem
            True
            sage: y = AA(2).sqrt()
            sage: y.real_exact(RR)
            1.41421356237310
            sage: y.real_exact(RealField(53, rnd='RNDD'))
            1.41421356237309
            sage: y.real_exact(RealField(53, rnd='RNDU'))
            1.41421356237310
            sage: y.real_exact(RealField(53, rnd='RNDZ'))
            1.41421356237309
        """

class AlgebraicNumberPowQQAction(Action):
    """
    Implement powering of an algebraic number (an element of ``QQbar``
    or ``AA``) by a rational.

    This is always a right action.

    INPUT:

    - ``G`` -- must be ``QQ``

    - ``S`` -- the parent on which to act, either ``AA`` or ``QQbar``

    .. NOTE::

        To compute ``x ^ (a/b)``, we take the `b`-th root of `x`; then
        we take that to the `a`-th power. If `x` is a negative algebraic
        real and `b` is odd, take the real `b`-th root; otherwise take
        the principal `b`-th root.

    EXAMPLES:

    In ``QQbar``::

        sage: QQbar(2)^(1/2)
        1.414213562373095?
        sage: QQbar(8)^(2/3)
        4
        sage: QQbar(8)^(2/3) == 4
        True
        sage: x = polygen(QQbar)
        sage: phi = QQbar.polynomial_root(x^2 - x - 1, RIF(1, 2))
        sage: tau = QQbar.polynomial_root(x^2 - x - 1, RIF(-1, 0))
        sage: rt5 = QQbar(5)^(1/2)
        sage: phi^10 / rt5
        55.00363612324742?
        sage: tau^10 / rt5
        0.003636123247413266?
        sage: (phi^10 - tau^10) / rt5
        55.00000000000000?
        sage: (phi^10 - tau^10) / rt5 == fibonacci(10)
        True
        sage: (phi^50 - tau^50) / rt5 == fibonacci(50)
        True
        sage: QQbar(-8)^(1/3)
        1.000000000000000? + 1.732050807568878?*I
        sage: (QQbar(-8)^(1/3))^3
        -8
        sage: QQbar(32)^(1/5)
        2
        sage: a = QQbar.zeta(7)^(1/3); a
        0.9555728057861407? + 0.2947551744109043?*I
        sage: a == QQbar.zeta(21)
        True
        sage: QQbar.zeta(7)^6
        0.6234898018587335? - 0.7818314824680299?*I
        sage: (QQbar.zeta(7)^6)^(1/3) * QQbar.zeta(21)
        1.000000000000000? + 0.?e-17*I

    In ``AA``::

        sage: AA(2)^(1/2)
        1.414213562373095?
        sage: AA(8)^(2/3)
        4
        sage: AA(8)^(2/3) == 4
        True
        sage: x = polygen(AA)
        sage: phi = AA.polynomial_root(x^2 - x - 1, RIF(0, 2))
        sage: tau = AA.polynomial_root(x^2 - x - 1, RIF(-2, 0))
        sage: rt5 = AA(5)^(1/2)
        sage: phi^10 / rt5
        55.00363612324742?
        sage: tau^10 / rt5
        0.003636123247413266?
        sage: (phi^10 - tau^10) / rt5
        55.00000000000000?
        sage: (phi^10 - tau^10) / rt5 == fibonacci(10)
        True
        sage: (phi^50 - tau^50) / rt5 == fibonacci(50)
        True

    TESTS::

        sage: AA(-8)^(1/3)
        -2
        sage: AA(-8)^(2/3)
        4
        sage: AA(32)^(3/5)
        8
        sage: AA(-16)^(1/2)
        4*I
        sage: AA(-16)^(1/4)
        1.414213562373095? + 1.414213562373095?*I
        sage: AA(-16)^(1/4)/QQbar.zeta(8)
        2

    We check that :issue:`7859` is fixed::

        sage: (AA(2)^(1/2)-AA(2)^(1/2))^(1/2)
        0
    """
    def __init__(self, G, S) -> None:
        """
        EXAMPLES::

            sage: from sage.rings.qqbar import AlgebraicNumberPowQQAction
            sage: act = AlgebraicNumberPowQQAction(QQ, AA); act
            Right Rational Powering by Rational Field on Algebraic Real Field
            sage: act(AA(-2), 1/3)
            -1.259921049894873?

        ::

            sage: act = AlgebraicNumberPowQQAction(QQ, QQbar); act
            Right Rational Powering by Rational Field on Algebraic Field
            sage: act(QQbar(-2), 1/3)
            0.6299605249474365? + 1.091123635971722?*I
        """

class ANRational(ANDescr):
    """
    The subclass of :class:`ANDescr` that represents an arbitrary
    rational. This class is private, and should not be used directly.
    """
    def __init__(self, x) -> None:
        """
        TESTS::

            sage: polygen(QQbar) / int(3)
            1/3*x
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: t = AA(5/2); type(t._descr)
            <class 'sage.rings.qqbar.ANRational'>
            sage: loads(dumps(t)) == t
            True
        """
    def handle_sage_input(self, sib, coerce, is_qqbar):
        """
        Produce an expression which will reproduce this value when evaluated,
        and an indication of whether this value is worth sharing (always
        False, for rationals).

        EXAMPLES::

            sage: sage_input(QQbar(22/7), verify=True)
            # Verified
            QQbar(22/7)
            sage: sage_input(-AA(3)/5, verify=True)
            # Verified
            AA(-3/5)
            sage: sage_input(vector(AA, (0, 1/2, 1/3)), verify=True)
            # Verified
            vector(AA, [0, 1/2, 1/3])
            sage: from sage.rings.qqbar import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: rat = ANRational(9/10)
            sage: rat.handle_sage_input(sib, False, True)
            ({call: {atomic:QQbar}({binop:/ {atomic:9} {atomic:10}})}, False)
        """
    def generator(self):
        """
        Return an :class:`AlgebraicGenerator` object associated to this
        element. Returns the trivial generator, since ``self`` is rational.

        EXAMPLES::

            sage: QQbar(0)._descr.generator()
            Trivial generator
        """
    def is_complex(self):
        """
        Return ``False``, since rational numbers are real.

        EXAMPLES::

            sage: QQbar(1/7)._descr.is_complex()
            False
        """
    def exactify(self):
        """
        Calculate ``self`` exactly. Since ``self`` is a rational number, return ``self``.

        EXAMPLES::

            sage: a = QQbar(1/3)._descr
            sage: a.exactify() is a
            True
        """
    def is_simple(self):
        """
        Check whether this descriptor represents a value with the same
        algebraic degree as the number field associated with the descriptor.

        This is always true for rational numbers.

        EXAMPLES::

            sage: AA(1/2)._descr.is_simple()
            True
        """
    def minpoly(self):
        """
        Return the min poly of ``self`` over `\\QQ`.

        EXAMPLES::

            sage: QQbar(7)._descr.minpoly()
            x - 7
        """
    def neg(self, n):
        """
        Negation of ``self``.

        EXAMPLES::

            sage: a = QQbar(3)
            sage: b = a._descr
            sage: type(b)
            <class 'sage.rings.qqbar.ANRational'>
            sage: b.neg(a)
            -3
        """
    def invert(self, n):
        """
        1/``self``.

        EXAMPLES::

            sage: a = QQbar(3)
            sage: b = a._descr
            sage: b.invert(a)
            1/3
        """
    def abs(self, n):
        """
        Absolute value of ``self``.

        EXAMPLES::

            sage: a = QQbar(3)
            sage: b = a._descr
            sage: b.abs(a)
            3
        """
    def rational_argument(self, n):
        """
        Return the argument of ``self`` divided by `2 \\pi`, or ``None`` if this
        element is 0.

        EXAMPLES::

            sage: QQbar(3)._descr.rational_argument(None)
            0
            sage: QQbar(-3)._descr.rational_argument(None)
            1/2
            sage: QQbar(0)._descr.rational_argument(None) is None
            True
        """
    def angle(self):
        """
        Return a rational number `q \\in (-1/2, 1/2]` such that ``self`` is a rational multiple of
        `e^{2\\pi i q}`. Always returns 0, since this element is rational.

        EXAMPLES::

            sage: QQbar(3)._descr.angle()
            0
            sage: QQbar(-3)._descr.angle()
            0
            sage: QQbar(0)._descr.angle()
            0
        """
    def scale(self):
        """
        Return a rational number `r` such that ``self`` is equal to `r e^{2 \\pi
        i q}` for some `q \\in (-1/2, 1/2]`.  In other words, just return ``self``
        as a rational number.

        EXAMPLES::

            sage: QQbar(-3)._descr.scale()
            -3
        """

def is_AlgebraicReal(x):
    '''
    Test if ``x`` is an instance of :class:`~AlgebraicReal`. For internal use.

    EXAMPLES::

        sage: from sage.rings.qqbar import is_AlgebraicReal
        sage: is_AlgebraicReal(AA(sqrt(2)))                                             # needs sage.symbolic
        doctest:warning...
        DeprecationWarning: The function is_AlgebraicReal is deprecated;
        use \'isinstance(..., AlgebraicReal)\' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: is_AlgebraicReal(QQbar(sqrt(2)))                                          # needs sage.symbolic
        False
        sage: is_AlgebraicReal("spam")
        False
    '''
def is_AlgebraicNumber(x):
    '''
    Test if ``x`` is an instance of :class:`~AlgebraicNumber`. For internal use.

    EXAMPLES::

        sage: from sage.rings.qqbar import is_AlgebraicNumber
        sage: is_AlgebraicNumber(AA(sqrt(2)))                                           # needs sage.symbolic
        doctest:warning...
        DeprecationWarning: The function is_AlgebraicNumber is deprecated;
        use \'isinstance(..., AlgebraicNumber)\' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        False
        sage: is_AlgebraicNumber(QQbar(sqrt(2)))                                        # needs sage.symbolic
        True
        sage: is_AlgebraicNumber("spam")
        False
    '''

QQbarPoly: PolynomialRing_field
AAPoly: PolynomialRing_field

class AlgebraicPolynomialTracker(SageObject):
    """
    Keeps track of a polynomial used for algebraic numbers.

    If multiple algebraic numbers are created as roots of a single
    polynomial, this allows the polynomial and information about
    the polynomial to be shared. This reduces work if the polynomial
    must be recomputed at higher precision, or if it must be factored.

    This class is private, and should only be constructed by
    ``AA.common_polynomial()`` or ``QQbar.common_polynomial()``, and should
    only be used as an argument to ``AA.polynomial_root()`` or
    ``QQbar.polynomial_root()``. (It does not matter whether you create
    the common polynomial with ``AA.common_polynomial()`` or
    ``QQbar.common_polynomial()``.)

    EXAMPLES::

        sage: x = polygen(QQbar)
        sage: P = QQbar.common_polynomial(x^2 - x - 1)
        sage: P
        x^2 - x - 1
        sage: QQbar.polynomial_root(P, RIF(1, 2))
        1.618033988749895?
    """
    def __init__(self, poly) -> None:
        """
        Initialize this AlgebraicPolynomialTracker object.

        EXAMPLES::

            sage: x = polygen(QQbar)
            sage: P = QQbar.common_polynomial(x^2 - x - 1)
            sage: type(P) # indirect doctest
            <class 'sage.rings.qqbar.AlgebraicPolynomialTracker'>
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]
            sage: type(v._descr._poly)
            <class 'sage.rings.qqbar.AlgebraicPolynomialTracker'>
            sage: loads(dumps(v)) == v
            True
        """
    def poly(self):
        """
        Return the underlying polynomial of ``self``.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: f = x^3 - 7
            sage: g = AA.common_polynomial(f)
            sage: g.poly()
            y^3 - 7
        """
    def is_complex(self):
        """
        Return ``True`` if the coefficients of this polynomial are non-real.

        EXAMPLES::

            sage: x = polygen(QQ); f = x^3 - 7
            sage: g = AA.common_polynomial(f)
            sage: g.is_complex()
            False
            sage: QQbar.common_polynomial(x^3 - QQbar(I)).is_complex()
            True
        """
    def complex_roots(self, prec, multiplicity):
        """
        Find the roots of ``self`` in the complex field to precision ``prec``.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: cp = AA.common_polynomial(x^4 - 2)

        Note that the precision is not guaranteed to find the tightest
        possible interval since :meth:`complex_roots` depends on the
        underlying BLAS implementation. ::

            sage: cp.complex_roots(30, 1)
            [-1.18920711500272...?,
             1.189207115002721?,
             -1.189207115002721?*I,
             1.189207115002721?*I]
        """
    def exactify(self) -> None:
        '''
        Compute a common field that holds all of the algebraic coefficients
        of this polynomial, then factor the polynomial over that field.
        Store the factors for later use (ignoring multiplicity).

        EXAMPLES::

            sage: x = polygen(AA)
            sage: p = sqrt(AA(2)) * x^2 - sqrt(AA(3))
            sage: cp = AA.common_polynomial(p)
            sage: cp._exact
            False
            sage: cp.exactify()
            sage: cp._exact
            True

        TESTS:

        Check that interrupting ``exactify()`` does not lead to incoherent state::

            sage: x = polygen(AA)
            sage: p = AA(2)^(1/100) * x + AA(3)^(1/100)
            sage: cp = AA.common_polynomial(p)
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: from warnings import catch_warnings, filterwarnings
            sage: with ensure_interruptible_after(0.5), catch_warnings():
            ....:     filterwarnings("ignore", r"cypari2 leaked \\d+ bytes on the PARI stack")
            ....:     cp.generator()
            sage: with ensure_interruptible_after(0.5), catch_warnings():
            ....:     filterwarnings("ignore", r"cypari2 leaked \\d+ bytes on the PARI stack")
            ....:     cp.generator()
        '''
    def factors(self):
        """
        EXAMPLES::

            sage: x = polygen(QQ)
            sage: f = QQbar.common_polynomial(x^4 + 4)
            sage: f.factors()
            [y^2 - 2*y + 2, y^2 + 2*y + 2]
        """
    def generator(self):
        """
        Return an :class:`AlgebraicGenerator` for a number field containing all
        the coefficients of ``self``.

        EXAMPLES::

            sage: x = polygen(AA)
            sage: p = sqrt(AA(2)) * x^2 - sqrt(AA(3))
            sage: cp = AA.common_polynomial(p)
            sage: cp.generator()
            Number Field in a with defining polynomial y^4 - 4*y^2 + 1
             with a in -0.5176380902050415?
        """

class ANRoot(ANDescr):
    """
    The subclass of :class:`ANDescr` that represents a particular
    root of a polynomial with algebraic coefficients.
    This class is private, and should not be used directly.
    """
    def __init__(self, poly, interval, multiplicity: int = 1) -> None:
        """
        Initialize this ``ANRoot`` object.

        EXAMPLES::

            sage: x = polygen(QQ); f = (x^3 + x + 1).roots(AA,multiplicities=False)[0]._descr
            sage: type(f) # indirect doctest
            <class 'sage.rings.qqbar.ANRoot'>
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]
            sage: type(v._descr)
            <class 'sage.rings.qqbar.ANRoot'>
            sage: loads(dumps(v)) == v
            True
        """
    def handle_sage_input(self, sib, coerce, is_qqbar):
        """
        Produce an expression which will reproduce this value when evaluated,
        and an indication of whether this value is worth sharing (always ``True``
        for :class:`ANRoot`).

        EXAMPLES::

            sage: sage_input((AA(3)^(1/2))^(1/3), verify=True)
            # Verified
            R.<x> = AA[]
            AA.polynomial_root(AA.common_polynomial(x^3 - AA.polynomial_root(AA.common_polynomial(x^2 - 3), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))), RIF(RR(1.2009369551760025), RR(1.2009369551760027)))

        These two examples are too big to verify quickly. (Verification
        would create a field of degree 28.)::

            sage: sage_input((sqrt(AA(3))^(5/7))^(9/4))
            R.<x> = AA[]
            v1 = AA.polynomial_root(AA.common_polynomial(x^2 - 3), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))
            v2 = v1*v1
            v3 = AA.polynomial_root(AA.common_polynomial(x^7 - v2*v2*v1), RIF(RR(1.4804728524798112), RR(1.4804728524798114)))
            v4 = v3*v3
            v5 = v4*v4
            AA.polynomial_root(AA.common_polynomial(x^4 - v5*v5*v3), RIF(RR(2.4176921938267877), RR(2.4176921938267881)))
            sage: sage_input((sqrt(QQbar(-7))^(5/7))^(9/4))
            R.<x> = QQbar[]
            v1 = QQbar.polynomial_root(AA.common_polynomial(x^2 + 7), CIF(RIF(RR(0)), RIF(RR(2.6457513110645903), RR(2.6457513110645907))))
            v2 = v1*v1
            v3 = QQbar.polynomial_root(AA.common_polynomial(x^7 - v2*v2*v1), CIF(RIF(RR(0.8693488875796217), RR(0.86934888757962181)), RIF(RR(1.8052215661454434), RR(1.8052215661454436))))
            v4 = v3*v3
            v5 = v4*v4
            QQbar.polynomial_root(AA.common_polynomial(x^4 - v5*v5*v3), CIF(RIF(-RR(3.8954086044650791), -RR(3.8954086044650786)), RIF(RR(2.7639398015408925), RR(2.7639398015408929))))
            sage: x = polygen(QQ)
            sage: sage_input(AA.polynomial_root(x^2-x-1, RIF(1, 2)), verify=True)
            # Verified
            R.<y> = QQ[]
            AA.polynomial_root(AA.common_polynomial(y^2 - y - 1), RIF(RR(1.6180339887498947), RR(1.6180339887498949)))
            sage: sage_input(QQbar.polynomial_root(x^3-5, CIF(RIF(-3, 0), RIF(0, 3))), verify=True)
            # Verified
            R.<y> = QQ[]
            QQbar.polynomial_root(AA.common_polynomial(y^3 - 5), CIF(RIF(-RR(0.85498797333834853), -RR(0.85498797333834842)), RIF(RR(1.4808826096823642), RR(1.4808826096823644))))
            sage: from sage.rings.qqbar import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: rt = ANRoot(x^3 - 2, RIF(0, 4))
            sage: rt.handle_sage_input(sib, False, True)
            ({call: {getattr: {atomic:QQbar}.polynomial_root}({call: {getattr: {atomic:AA}.common_polynomial}({binop:- {binop:** {gen:y {constr_parent: {subscr: {atomic:QQ}[{atomic:'y'}]} with gens: ('y',)}} {atomic:3}} {atomic:2}})}, {call: {atomic:RIF}({call: {atomic:RR}({atomic:1.259921049894873})}, {call: {atomic:RR}({atomic:1.2599210498948732})})})},
             True)
        """
    def is_complex(self):
        """
        Whether this is a root in `\\overline{\\QQ}` (rather than `\\mathbf{A}`).
        Note that this may return ``True`` even if the root is actually real, as
        the second example shows; it does *not* trigger exact computation to
        see if the root is real.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]._descr.is_complex()
            False
            sage: (x^2 - x - 1).roots(ring=QQbar, multiplicities=False)[1]._descr.is_complex()
            True
        """
    def conjugate(self, n):
        """
        Complex conjugate of this :class:`ANRoot` object.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = (x^2 + 23).roots(ring=QQbar, multiplicities=False)[0]
            sage: b = a._descr
            sage: type(b)
            <class 'sage.rings.qqbar.ANRoot'>
            sage: c = b.conjugate(a); c
            <sage.rings.qqbar.ANUnaryExpr object at ...>
            sage: c.exactify()
            -2*a + 1 where a^2 - a + 6 = 0 and a in 0.50000000000000000? - 2.397915761656360?*I
        """
    def refine_interval(self, interval, prec):
        """
        Take an interval which is assumed to enclose exactly one root
        of the polynomial (or, with multiplicity=`k`, exactly one root
        of the `k-1`-st derivative); and a precision, in bits.

        Tries to find a narrow interval enclosing the root using
        interval arithmetic of the given precision. (No particular
        number of resulting bits of precision is guaranteed.)

        Uses a combination of Newton's method (adapted for interval
        arithmetic) and bisection. The algorithm will converge very
        quickly if started with a sufficiently narrow interval.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot
            sage: x = polygen(AA)
            sage: rt2 = ANRoot(x^2 - 2, RIF(0, 2))
            sage: rt2.refine_interval(RIF(0, 2), 75)
            1.4142135623730950488017?
        """
    def exactify(self):
        """
        Return either an :class:`ANRational` or an
        :class:`ANExtensionElement` with the same value as this number.

        EXAMPLES::

            sage: from sage.rings.qqbar import ANRoot
            sage: x = polygen(QQbar)
            sage: two = ANRoot((x-2)*(x-sqrt(QQbar(2))), RIF(1.9, 2.1))
            sage: two.exactify()
            2
            sage: strange = ANRoot(x^2 + sqrt(QQbar(3))*x - sqrt(QQbar(2)), RIF(-0, 1))
            sage: strange.exactify()
            a where a^8 - 6*a^6 + 5*a^4 - 12*a^2 + 4 = 0 and a in 0.6051012265139511?

        TESTS:

        Verify that :issue:`12727` is fixed::

            sage: m = sqrt(sin(pi/5)); a = QQbar(m); b = AA(m)                          # needs sage.symbolic
            sage: a.minpoly()                                                           # needs sage.symbolic
            x^8 - 5/4*x^4 + 5/16
            sage: b.minpoly()                                                           # needs sage.symbolic
            x^8 - 5/4*x^4 + 5/16
        """

class ANExtensionElement(ANDescr):
    """
    The subclass of :class:`ANDescr` that represents a number field
    element in terms of a specific generator. Consists of a polynomial
    with rational coefficients in terms of the generator, and the
    generator itself, an :class:`AlgebraicGenerator`.
    """
    def __new__(self, generator, value): ...
    def __init__(self, generator, value) -> None: ...
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]
            sage: v.exactify()
            sage: type(v._descr)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: loads(dumps(v)) == v
            True
        """
    def handle_sage_input(self, sib, coerce, is_qqbar):
        """
        Produce an expression which will reproduce this value when evaluated,
        and an indication of whether this value is worth sharing (always ``True``
        for :class:`ANExtensionElement`).

        EXAMPLES::

            sage: I = QQbar(I)
            sage: sage_input(3+4*I, verify=True)
            # Verified
            QQbar(3 + 4*I)
            sage: v = QQbar.zeta(3) + QQbar.zeta(5)
            sage: v - v == 0
            True
            sage: sage_input(vector(QQbar, (4-3*I, QQbar.zeta(7))), verify=True)
            # Verified
            R.<y> = QQ[]
            vector(QQbar, [4 - 3*I, QQbar.polynomial_root(AA.common_polynomial(y^6 + y^5 + y^4 + y^3 + y^2 + y + 1), CIF(RIF(RR(0.62348980185873348), RR(0.62348980185873359)), RIF(RR(0.7818314824680298), RR(0.78183148246802991))))])
            sage: sage_input(v, verify=True)
            # Verified
            R.<y> = QQ[]
            v = QQbar.polynomial_root(AA.common_polynomial(y^8 - y^7 + y^5 - y^4 + y^3 - y + 1), CIF(RIF(RR(0.66913060635885813), RR(0.66913060635885824)), RIF(-RR(0.74314482547739424), -RR(0.74314482547739413))))
            v^6 + v^5
            sage: v = QQbar(sqrt(AA(2)))
            sage: v.exactify()
            sage: sage_input(v, verify=True)
            # Verified
            R.<y> = QQ[]
            QQbar(AA.polynomial_root(AA.common_polynomial(y^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951))))
            sage: from sage.rings.qqbar import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: extel = ANExtensionElement(QQbar_I_generator, QQbar_I_generator.field().gen() + 1)
            sage: extel.handle_sage_input(sib, False, True)
            ({call: {atomic:QQbar}({binop:+ {atomic:1} {atomic:I}})}, True)
        """
    def is_complex(self):
        """
        Return ``True`` if the number field that defines this element is not real.

        This does not imply that the element itself is definitely non-real, as
        in the example below.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: rt2 = QQbar(sqrt(2))
            sage: rtm3 = QQbar(sqrt(-3))
            sage: x = rtm3 + rt2 - rtm3
            sage: x.exactify()
            sage: y = x._descr
            sage: type(y)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: y.is_complex()
            True
            sage: x.imag() == 0
            True
        """
    def is_simple(self):
        """
        Check whether this descriptor represents a value with the same
        algebraic degree as the number field associated with the descriptor.

        For :class:`ANExtensionElement` elements, we check this by
        comparing the degree of the minimal polynomial to the degree
        of the field.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: rt2 = AA(sqrt(2))
            sage: rt3 = AA(sqrt(3))
            sage: rt2b = rt3 + rt2 - rt3
            sage: rt2.exactify()
            sage: rt2._descr
            a where a^2 - 2 = 0 and a in 1.414213562373095?
            sage: rt2._descr.is_simple()
            True

            sage: rt2b.exactify()                                                       # needs sage.symbolic
            sage: rt2b._descr                                                           # needs sage.symbolic
            a^3 - 3*a where a^4 - 4*a^2 + 1 = 0 and a in -0.5176380902050415?
            sage: rt2b._descr.is_simple()                                               # needs sage.symbolic
            False
        """
    def generator(self):
        """
        Return the :class:`~AlgebraicGenerator` object corresponding to ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]._descr.exactify()
            sage: v.generator()
            Number Field in a with defining polynomial y^2 - y - 1 with a in 1.618033988749895?
        """
    def exactify(self):
        """
        Return an exact representation of ``self``.

        Since ``self`` is already exact, just return ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]._descr.exactify()
            sage: type(v)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: v.exactify() is v
            True
        """
    def field_element_value(self):
        """
        Return the underlying number field element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]._descr.exactify()
            sage: v.field_element_value()
            a
        """
    def minpoly(self):
        """
        Compute the minimal polynomial of this algebraic number.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: v = (x^2 - x - 1).roots(ring=AA, multiplicities=False)[1]._descr.exactify()
            sage: type(v)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: v.minpoly()
            x^2 - x - 1
        """
    def simplify(self, n):
        """
        Compute an exact representation for this descriptor, in the
        smallest possible number field.

        INPUT:

        - ``n`` -- the element of ``AA`` or ``QQbar`` corresponding
          to this descriptor

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: rt2 = AA(sqrt(2))
            sage: rt3 = AA(sqrt(3))
            sage: rt2b = rt3 + rt2 - rt3
            sage: rt2b.exactify()
            sage: rt2b._descr
            a^3 - 3*a where a^4 - 4*a^2 + 1 = 0 and a in -0.5176380902050415?
            sage: rt2b._descr.simplify(rt2b)
            a where a^2 - 2 = 0 and a in 1.414213562373095?
        """
    def neg(self, n):
        '''
        Negation of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(-3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class \'sage.rings.qqbar.ANExtensionElement\'>
            sage: c = b.neg(None); c  # random (not uniquely represented)
            -1/3*a^3 + 1/3*a^2 - a - 1 where a^4 - 2*a^3 + a^2 + 6*a + 3 = 0
             and a in 1.724744871391589? + 1.573132184970987?*I
            sage: (c.generator() == b.generator()
            ....:  and c.field_element_value() + b.field_element_value() == 0)
            True

        The parameter is ignored::

            sage: (b.neg("random").generator() == c.generator()                         # needs sage.symbolic
            ....:  and b.neg("random").field_element_value() == c.field_element_value())
            True
        '''
    def invert(self, n):
        '''
        Reciprocal of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(-3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class \'sage.rings.qqbar.ANExtensionElement\'>
            sage: c = b.invert(None); c  # random (not uniquely represented)
            -7/3*a^3 + 19/3*a^2 - 7*a - 9 where a^4 - 2*a^3 + a^2 + 6*a + 3 = 0
             and a in 1.724744871391589? + 1.573132184970987?*I
            sage: (c.generator() == b.generator()
            ....:  and c.field_element_value() * b.field_element_value() == 1)
            True

        The parameter is ignored::

            sage: (b.invert("random").generator() == c.generator()                      # needs sage.symbolic
            ....:  and b.invert("random").field_element_value() == c.field_element_value())
            True
        '''
    def conjugate(self, n):
        '''
        Complex conjugate of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(-3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class \'sage.rings.qqbar.ANExtensionElement\'>
            sage: c = b.conjugate(None); c  # random (not uniquely represented)
            1/3*a^3 - 1/3*a^2 + a + 1 where a^4 - 2*a^3 + a^2 + 6*a + 3 = 0
             and a in 1.724744871391589? - 1.573132184970987?*I

        Internally, complex conjugation is implemented by taking the
        same abstract field element but conjugating the complex embedding of
        the field::

            sage: c.generator() == b.generator().conjugate()                            # needs sage.symbolic
            True
            sage: c.field_element_value() == b.field_element_value()                    # needs sage.symbolic
            True

        The parameter is ignored::

            sage: (b.conjugate("random").generator() == c.generator()                   # needs sage.symbolic
            ....:  and b.conjugate("random").field_element_value() == c.field_element_value())
            True
        '''
    def norm(self, n):
        """
        Norm of ``self`` (square of complex absolute value).

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(-3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: b.norm(a)
            <sage.rings.qqbar.ANUnaryExpr object at ...>
        """
    def abs(self, n):
        """
        Return the absolute value of ``self`` (square root of the norm).

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(-3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: b.abs(a)
            Root 3.146264369941972342? of x^2 - 9.89897948556636?
        """
    def rational_argument(self, n):
        """
        If the argument of ``self`` is `2\\pi` times some rational number in `[1/2,
        -1/2)`, return that rational; otherwise, return ``None``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = QQbar(sqrt(-2)) + QQbar(sqrt(3))
            sage: a.exactify()
            sage: b = a._descr
            sage: type(b)
            <class 'sage.rings.qqbar.ANExtensionElement'>
            sage: b.rational_argument(a) is None
            True

            sage: x = polygen(QQ)
            sage: a = (x^4 + 1).roots(QQbar, multiplicities=False)[0]
            sage: a.exactify()
            sage: b = a._descr
            sage: b.rational_argument(a)
            -3/8
        """

class ANUnaryExpr(ANDescr):
    def __init__(self, arg, op) -> None:
        """
        Initialize this ANUnaryExpr.

        EXAMPLES::

            sage: t = ~QQbar(sqrt(2)); type(t._descr)  # indirect doctest               # needs sage.symbolic
            <class 'sage.rings.qqbar.ANUnaryExpr'>
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: t = ~QQbar(sqrt(2)); type(t._descr)                                   # needs sage.symbolic
            <class 'sage.rings.qqbar.ANUnaryExpr'>
            sage: loads(dumps(t)) == 1/QQbar(sqrt(2))                                   # needs sage.symbolic
            True
        """
    def handle_sage_input(self, sib, coerce, is_qqbar):
        """
        Produce an expression which will reproduce this value when evaluated,
        and an indication of whether this value is worth sharing (always
        ``True`` for :class:`ANUnaryExpr`).

        EXAMPLES::

            sage: sage_input(-sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            -AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(~sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            ~AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(sqrt(QQbar(-3)).conjugate(), verify=True)
            # Verified
            R.<x> = QQbar[]
            QQbar.polynomial_root(AA.common_polynomial(x^2 + 3), CIF(RIF(RR(0)), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))).conjugate()
            sage: sage_input(QQbar.zeta(3).real(), verify=True)
            # Verified
            R.<y> = QQ[]
            QQbar.polynomial_root(AA.common_polynomial(y^2 + y + 1), CIF(RIF(-RR(0.50000000000000011), -RR(0.49999999999999994)), RIF(RR(0.8660254037844386), RR(0.86602540378443871)))).real()
            sage: sage_input(QQbar.zeta(3).imag(), verify=True)
            # Verified
            R.<y> = QQ[]
            QQbar.polynomial_root(AA.common_polynomial(y^2 + y + 1), CIF(RIF(-RR(0.50000000000000011), -RR(0.49999999999999994)), RIF(RR(0.8660254037844386), RR(0.86602540378443871)))).imag()
            sage: sage_input(abs(sqrt(QQbar(-3))), verify=True)
            # Verified
            R.<x> = QQbar[]
            abs(QQbar.polynomial_root(AA.common_polynomial(x^2 + 3), CIF(RIF(RR(0)), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))))
            sage: sage_input(sqrt(QQbar(-3)).norm(), verify=True)
            # Verified
            R.<x> = QQbar[]
            QQbar.polynomial_root(AA.common_polynomial(x^2 + 3), CIF(RIF(RR(0)), RIF(RR(1.7320508075688772), RR(1.7320508075688774)))).norm()
            sage: sage_input(QQbar(QQbar.zeta(3).real()), verify=True)
            # Verified
            R.<y> = QQ[]
            QQbar(QQbar.polynomial_root(AA.common_polynomial(y^2 + y + 1), CIF(RIF(-RR(0.50000000000000011), -RR(0.49999999999999994)), RIF(RR(0.8660254037844386), RR(0.86602540378443871)))).real())
            sage: from sage.rings.qqbar import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: unexp = ANUnaryExpr(sqrt(AA(2)), '~')
            sage: unexp.handle_sage_input(sib, False, False)
            ({unop:~ {call: {getattr: {atomic:AA}.polynomial_root}({call: {getattr: {atomic:AA}.common_polynomial}({binop:- {binop:** {gen:x {constr_parent: {subscr: {atomic:AA}[{atomic:'x'}]} with gens: ('x',)}} {atomic:2}} {atomic:2}})}, {call: {atomic:RIF}({call: {atomic:RR}({atomic:1.4142135623730949})}, {call: {atomic:RR}({atomic:1.4142135623730951})})})}},
             True)
            sage: unexp.handle_sage_input(sib, False, True)
            ({call: {atomic:QQbar}({unop:~ {call: {getattr: {atomic:AA}.polynomial_root}({call: {getattr: {atomic:AA}.common_polynomial}({binop:- {binop:** {gen:x {constr_parent: {subscr: {atomic:AA}[{atomic:'x'}]} with gens: ('x',)}} {atomic:2}} {atomic:2}})}, {call: {atomic:RIF}({call: {atomic:RR}({atomic:1.4142135623730949})}, {call: {atomic:RR}({atomic:1.4142135623730951})})})}})},
             True)
        """
    def is_complex(self):
        """
        Return whether or not this element is complex. Note that this is a data
        type check, and triggers no computations -- if it returns ``False``, the
        element might still be real, it just doesn't know it yet.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = AA(sqrt(2))
            sage: s = (-t)._descr
            sage: s
            <sage.rings.qqbar.ANUnaryExpr object at ...>
            sage: s.is_complex()
            False
            sage: QQbar(-sqrt(2))._descr.is_complex()
            True
        """
    def exactify(self):
        """
        Trigger exact computation of ``self``.

        EXAMPLES::

            sage: v = (-QQbar(sqrt(2)))._descr                                          # needs sage.symbolic
            sage: type(v)                                                               # needs sage.symbolic
            <class 'sage.rings.qqbar.ANUnaryExpr'>
            sage: v.exactify()                                                          # needs sage.symbolic
            -a where a^2 - 2 = 0 and a in 1.414213562373095?
        """

class ANBinaryExpr(ANDescr):
    def __init__(self, left, right, op) -> None:
        """
        Initialize this ANBinaryExpr.

        EXAMPLES::

            sage: t = QQbar(sqrt(2)) + QQbar(sqrt(3)); type(t._descr)  # indirect doctest           # needs sage.symbolic
            <class 'sage.rings.qqbar.ANBinaryExpr'>
        """
    def __reduce__(self):
        """
        Add customized pickling support.

        EXAMPLES::

            sage: t = QQbar(sqrt(2)) + QQbar(sqrt(3)); type(t._descr)                   # needs sage.symbolic
            <class 'sage.rings.qqbar.ANBinaryExpr'>
            sage: loads(dumps(t)) == QQbar(sqrt(2)) + QQbar(sqrt(3))                    # needs sage.symbolic
            True
        """
    def handle_sage_input(self, sib, coerce, is_qqbar):
        """
        Produce an expression which will reproduce this value when evaluated,
        and an indication of whether this value is worth sharing (always
        ``True`` for :class:`ANBinaryExpr`).

        EXAMPLES::

            sage: sage_input(2 + sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            2 + AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(sqrt(AA(2)) + 2, verify=True)
            # Verified
            R.<x> = AA[]
            AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951))) + 2
            sage: sage_input(2 - sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            2 - AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(2 / sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            2/AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(2 + (-1*sqrt(AA(2))), verify=True)
            # Verified
            R.<x> = AA[]
            2 - AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: sage_input(2*sqrt(AA(2)), verify=True)
            # Verified
            R.<x> = AA[]
            2*AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            sage: rt2 = sqrt(AA(2))
            sage: one = rt2/rt2
            sage: n = one+3
            sage: sage_input(n)
            R.<x> = AA[]
            v = AA.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951)))
            v/v + 3
            sage: one == 1
            True
            sage: sage_input(n)
            1 + AA(3)
            sage: rt3 = QQbar(sqrt(3))                                                  # needs sage.symbolic
            sage: one = rt3/rt3                                                         # needs sage.symbolic
            sage: n = sqrt(AA(2)) + one
            sage: one == 1                                                              # needs sage.symbolic
            True
            sage: sage_input(n)
            R.<x> = AA[]
            QQbar.polynomial_root(AA.common_polynomial(x^2 - 2), RIF(RR(1.4142135623730949), RR(1.4142135623730951))) + 1
            sage: from sage.rings.qqbar import *
            sage: from sage.misc.sage_input import SageInputBuilder
            sage: sib = SageInputBuilder()
            sage: binexp = ANBinaryExpr(AA(3), AA(5), operator.mul)
            sage: binexp.handle_sage_input(sib, False, False)
            ({binop:* {atomic:3} {call: {atomic:AA}({atomic:5})}}, True)
            sage: binexp.handle_sage_input(sib, False, True)
            ({call: {atomic:QQbar}({binop:* {atomic:3} {call: {atomic:AA}({atomic:5})}})}, True)
        """
    def is_complex(self):
        """
        Whether this element is complex. Does not trigger exact computation, so
        may return ``True`` even if the element is real.

        EXAMPLES::

            sage: x = (QQbar(sqrt(-2)) / QQbar(sqrt(-5)))._descr                        # needs sage.symbolic
            sage: x.is_complex()                                                        # needs sage.symbolic
            True
        """
    def exactify(self):
        """
        TESTS::

            sage: rt2c = QQbar.zeta(3) + AA(sqrt(2)) - QQbar.zeta(3)                    # needs sage.symbolic
            sage: rt2c.exactify()                                                       # needs sage.symbolic

        We check to make sure that this method still works even. We
        do this by increasing the recursion level at each step and
        decrease it before we return.
        We lower the recursion limit for this test to allow
        a test in reasonable time::

            sage: # needs sage.combinat
            sage: import sys
            sage: old_recursion_limit = sys.getrecursionlimit()
            sage: sys.setrecursionlimit(1000)
            sage: sys.getrecursionlimit()
            1000
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a=s([3,2]).expand(8)(flatten([[QQbar.zeta(3)^d for d in range(3)], [QQbar.zeta(5)^d for d in range(5)]]))
            sage: a.exactify(); a # long time
            0
            sage: sys.getrecursionlimit()
            1000
            sage: sys.setrecursionlimit(old_recursion_limit)
        """

def an_binop_rational(a, b, op):
    """
    Used to add, subtract, multiply or divide algebraic numbers.

    Used when both are actually rational.

    EXAMPLES::

        sage: from sage.rings.qqbar import an_binop_rational
        sage: f = an_binop_rational(QQbar(2), QQbar(3/7), operator.add)
        sage: f
        17/7
        sage: type(f)
        <class 'sage.rings.qqbar.ANRational'>

        sage: f = an_binop_rational(QQbar(2), QQbar(3/7), operator.mul)
        sage: f
        6/7
        sage: type(f)
        <class 'sage.rings.qqbar.ANRational'>
    """
def an_binop_expr(a, b, op):
    """
    Add, subtract, multiply or divide algebraic numbers represented as
    binary expressions.

    INPUT:

    - ``a``, ``b`` -- two elements

    - ``op`` -- an operator

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: a = QQbar(sqrt(2)) + QQbar(sqrt(3))
        sage: b = QQbar(sqrt(3)) + QQbar(sqrt(5))
        sage: type(a._descr); type(b._descr)
        <class 'sage.rings.qqbar.ANBinaryExpr'>
        <class 'sage.rings.qqbar.ANBinaryExpr'>
        sage: from sage.rings.qqbar import an_binop_expr
        sage: x = an_binop_expr(a, b, operator.add); x
        <sage.rings.qqbar.ANBinaryExpr object at ...>
        sage: x.exactify()
        6/7*a^7 - 2/7*a^6 - 71/7*a^5 + 26/7*a^4 + 125/7*a^3 - 72/7*a^2 - 43/7*a + 47/7
        where a^8 - 12*a^6 + 23*a^4 - 12*a^2 + 1 = 0 and a in -0.3199179336182997?

        sage: # needs sage.symbolic
        sage: a = QQbar(sqrt(2)) + QQbar(sqrt(3))
        sage: b = QQbar(sqrt(3)) + QQbar(sqrt(5))
        sage: type(a._descr)
        <class 'sage.rings.qqbar.ANBinaryExpr'>
        sage: x = an_binop_expr(a, b, operator.mul); x
        <sage.rings.qqbar.ANBinaryExpr object at ...>
        sage: x.exactify()
        2*a^7 - a^6 - 24*a^5 + 12*a^4 + 46*a^3 - 22*a^2 - 22*a + 9
        where a^8 - 12*a^6 + 23*a^4 - 12*a^2 + 1 = 0 and a in -0.3199179336182997?
    """
def an_binop_element(a, b, op):
    """
    Add, subtract, multiply or divide two elements represented as elements of
    number fields.

    EXAMPLES::

        sage: sqrt2 = QQbar(2).sqrt()
        sage: sqrt3 = QQbar(3).sqrt()
        sage: sqrt5 = QQbar(5).sqrt()

        sage: a = sqrt2 + sqrt3; a.exactify()
        sage: b = sqrt3 + sqrt5; b.exactify()
        sage: type(a._descr)
        <class 'sage.rings.qqbar.ANExtensionElement'>
        sage: from sage.rings.qqbar import an_binop_element
        sage: an_binop_element(a, b, operator.add)
        <sage.rings.qqbar.ANBinaryExpr object at ...>
        sage: an_binop_element(a, b, operator.sub)
        <sage.rings.qqbar.ANBinaryExpr object at ...>
        sage: an_binop_element(a, b, operator.mul)
        <sage.rings.qqbar.ANBinaryExpr object at ...>
        sage: an_binop_element(a, b, operator.truediv)
        <sage.rings.qqbar.ANBinaryExpr object at ...>

    The code tries to use existing unions of number fields::

        sage: sqrt17 = QQbar(17).sqrt()
        sage: sqrt19 = QQbar(19).sqrt()
        sage: a = sqrt17 + sqrt19
        sage: b = sqrt17 * sqrt19 - sqrt17 + sqrt19 * (sqrt17 + 2)
        sage: b, type(b._descr)
        (40.53909377268655?, <class 'sage.rings.qqbar.ANBinaryExpr'>)
        sage: a.exactify()
        sage: b = sqrt17 * sqrt19 - sqrt17 + sqrt19 * (sqrt17 + 2)
        sage: b, type(b._descr)
        (40.53909377268655?, <class 'sage.rings.qqbar.ANExtensionElement'>)
    """

qq_generator: AlgebraicGenerator
AA_golden_ratio: AlgebraicReal

def get_AA_golden_ratio():
    """
    Return the golden ratio as an element of the algebraic real field. Used by
    :meth:`sage.symbolic.constants.golden_ratio._algebraic_`.

    EXAMPLES::

        sage: AA(golden_ratio)  # indirect doctest                                      # needs sage.symbolic
        1.618033988749895?
    """

RR_1_10: RealNumber = RR(1) / 10
QQ_0: Rational = QQ.zero()
QQ_1: Rational = QQ.one()
QQ_1_2: Rational = QQ((1, 2))
QQ_1_4: Rational = QQ((1, 4))

AA_0: AlgebraicReal = AA.zero()

QQbar_I_nf: NumberField_quadratic = GaussianField()
QQbar_I_generator = AlgebraicGenerator(QQbar_I_nf, ANRoot(AAPoly.gen()**2 + 1, CIF(0, 1)))
QQbar_I = AlgebraicNumber(ANExtensionElement(QQbar_I_generator, QQbar_I_nf.gen()))

AA_hash_offset: AlgebraicReal = AA(~ZZ(123456789))

QQbar_hash_offset: AlgebraicNumber = AlgebraicNumber(ANExtensionElement(QQbar_I_generator, ~ZZ(123456789) + QQbar_I_nf.gen() / ZZ(987654321)))

ZZX_x: Polynomial_integer_dense_flint = ZZ['x'].gen()