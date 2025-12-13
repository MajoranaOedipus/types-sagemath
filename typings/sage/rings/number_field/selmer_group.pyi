from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.rational_field import QQ as QQ

def coords_in_U_mod_p(u, U, p):
    """
    Return coordinates of a unit ``u`` with respect to a basis of the
    `p`-cotorsion `U/U^p` of the unit group ``U``.

    INPUT:

    - ``u`` -- (algebraic unit) a unit in a number field ``K``

    - ``U`` -- (unit group) the unit group of ``K``

    - ``p`` -- prime number

    OUTPUT:

    The coordinates of the unit `u` in the `p`-cotorsion group `U/U^p`.

    ALGORITHM:

    Take the coordinate vector of `u` with respect to the generators
    of the unit group, drop the coordinate of the roots of unity
    factor if it is prime to `p`, and reduce the vector mod `p`.

    EXAMPLES::

        sage: from sage.rings.number_field.selmer_group import coords_in_U_mod_p
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^4 - 5*x^2 + 1)
        sage: U = K.unit_group()
        sage: U
        Unit group with structure C2 x Z x Z x Z of Number Field in a with defining polynomial x^4 - 5*x^2 + 1
        sage: u0, u1, u2, u3 = U.gens_values()
        sage: u = u1*u2^2*u3^3
        sage: coords_in_U_mod_p(u,U,2)
        [0, 1, 0, 1]
        sage: coords_in_U_mod_p(u,U,3)
        [1, 2, 0]
        sage: u*=u0
        sage: coords_in_U_mod_p(u,U,2)
        [1, 1, 0, 1]
        sage: coords_in_U_mod_p(u,U,3)
        [1, 2, 0]
    """
def basis_for_p_cokernel(S, C, p):
    """
    Return a basis for the group of ideals supported on ``S`` (mod
    `p`-th-powers) whose class in the class group ``C`` is a `p`-th power,
    together with a function which takes the ``S``-exponents of such an
    ideal and returns its coordinates on this basis.

    INPUT:

    - ``S`` -- list of prime ideals in a number field ``K``

    - ``C`` -- (class group) the ideal class group of ``K``

    - ``p`` -- prime number

    OUTPUT:

    (tuple) (``b``, ``f``) where

    - ``b`` is a list of ideals which is a basis for the group of
      ideals supported on ``S`` (modulo `p`-th powers) whose ideal
      class is a `p`-th power;

    - ``f`` is a function which takes such an ideal and returns its
      coordinates with respect to this basis.

    EXAMPLES::

        sage: from sage.rings.number_field.selmer_group import basis_for_p_cokernel
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - x + 58)
        sage: S = K.ideal(30).support(); S
        [Fractional ideal (2, a),
        Fractional ideal (2, a + 1),
        Fractional ideal (3, a + 1),
        Fractional ideal (5, a + 1),
        Fractional ideal (5, a + 3)]
        sage: C = K.class_group()
        sage: C.gens_orders()
        (6, 2)
        sage: [C(P).exponents() for P in S]
        [(5, 0), (1, 0), (3, 1), (1, 1), (5, 1)]
        sage: b, f = basis_for_p_cokernel(S, C, 2); b
        [Fractional ideal (2), Fractional ideal (15, a + 13), Fractional ideal (5)]
        sage: b, f = basis_for_p_cokernel(S, C, 3); b
        [Fractional ideal (50, a + 18),
        Fractional ideal (10, a + 3),
        Fractional ideal (3, a + 1),
        Fractional ideal (5)]
        sage: b, f = basis_for_p_cokernel(S, C, 5); b
        [Fractional ideal (2, a),
        Fractional ideal (2, a + 1),
        Fractional ideal (3, a + 1),
        Fractional ideal (5, a + 1),
        Fractional ideal (5, a + 3)]
    """
def pSelmerGroup(K, S, p, proof=None, debug: bool = False):
    """
    Return the `p`-Selmer group `K(S,p)` of the number field `K`
    with respect to the prime ideals in ``S``.

    INPUT:

    - ``K`` -- a number field or `\\QQ`

    - ``S`` -- list of prime ideals in `K`, or prime
      numbers when `K` is `\\QQ`

    - ``p`` -- a prime number

    - ``proof`` -- if ``True``, compute the class group provably
      correctly. Default is ``True``. Call :meth:`proof.number_field` to
      change this default globally.

    - ``debug`` -- boolean (default: ``False``); debug flag

    OUTPUT:

    (tuple) ``KSp``, ``KSp_gens``, ``from_KSp``, ``to_KSp`` where

    - ``KSp`` is an abstract vector space over `GF(p)` isomorphic to `K(S,p)`;

    - ``KSp_gens`` is a list of elements of `K^*` generating `K(S,p)`;

    - ``from_KSp`` is a function from ``KSp`` to `K^*` implementing
      the isomorphism from the abstract `K(S,p)` to `K(S,p)` as a
      subgroup of `K^*/(K^*)^p`;

    - ``to_KSP`` is a partial function from `K^*` to ``KSp``, defined
      on elements `a` whose image in `K^*/(K^*)^p` lies in `K(S,p)`,
      mapping them via the inverse isomorphism to the abstract vector
      space ``KSp``.

    ALGORITHM:

    The list of generators of `K(S,p)` is the concatenation of three
    sublists, called ``alphalist``, ``betalist`` and ``ulist`` in the
    code.  Only ``alphalist`` depends on the primes in `S`.

    - ``ulist`` is a basis for `U/U^p` where `U` is the unit group.
      This is the list of fundamental units, including the generator
      of the group of roots of unity if its order is divisible by `p`.
      These have valuation `0` at all primes.

    - ``betalist`` is a list of the generators of the `p`-th powers of
      ideals which generate the `p`-torsion in the class group (so is
      empty if the class number is prime to `p`).  These have
      valuation divisible by `p` at all primes.

    - ``alphalist`` is a list of generators for each ideal `A` in a
      basis of those ideals supported on `S` (modulo `p`-th powers of
      ideals) which are `p`-th powers in the class group.  We find `B`
      such that `A/B^p` is principal and take a generator of it, for
      each `A` in a generating set.  As a special case, if all the
      ideals in `S` are principal then ``alphalist`` is a list of
      their generators.

    The map from the abstract space to `K^*` is easy: we just take the
    product of the generators to powers given by the coefficient
    vector.  No attempt is made to reduce the resulting product modulo
    `p`-th powers.

    The reverse map is more complicated.  Given `a\\in K^*`:

    - write the principal ideal `(a)` in the form `AB^p` with `A`
      supported by `S` and `p`-th power free.  If this fails, then `a`
      does not represent an element of `K(S,p)` and an error is
      raised.

    - set `I_S` to be the group of ideals spanned by `S` mod `p`-th
      powers, and `I_{S,p}` the subgroup of `I_S` which maps to `0` in
      `C/C^p`.

    - Convert `A` to an element of `I_{S,p}`, hence find the
      coordinates of `a` with respect to the generators in
      ``alphalist``.

    - after dividing out by `A`, now `(a)=B^p` (with a different `a`
      and `B`).  Write the ideal class `[B]`, whose `p`-th power is
      trivial, in terms of the generators of `C[p]`; then `B=(b)B_1`,
      where the coefficients of `B_1` with respect to generators of
      `C[p]` give the coordinates of the result with respect to the
      generators in ``betalist``.

    - after dividing out by `B`, and by `b^p`, we now have `(a)=(1)`,
      so `a` is a unit, which can be expressed in terms of the unit
      generators.

    EXAMPLES:

    Over `\\QQ` the unit contribution is trivial unless `p=2` and
    the class group is trivial::

        sage: from sage.rings.number_field.selmer_group import pSelmerGroup
        sage: QS2, gens, fromQS2, toQS2 = pSelmerGroup(QQ, [2,3], 2)
        sage: QS2
        Vector space of dimension 3 over Finite Field of size 2
        sage: gens
        [2, 3, -1]
        sage: a = fromQS2([1,1,1]); a.factor()
        -1 * 2 * 3
        sage: toQS2(-6)
        (1, 1, 1)

        sage: QS3, gens, fromQS3, toQS3 = pSelmerGroup(QQ, [2,13], 3)
        sage: QS3
        Vector space of dimension 2 over Finite Field of size 3
        sage: gens
        [2, 13]
        sage: a = fromQS3([5,4]); a.factor()
        2^5 * 13^4
        sage: toQS3(a)
        (2, 1)
        sage: toQS3(a) == QS3([5,4])
        True

    A real quadratic field with class number 2, where the fundamental
    unit is a generator, and the class group provides another
    generator when `p=2`::

        sage: K.<a> = QuadraticField(-5)
        sage: K.class_number()
        2
        sage: P2 = K.ideal(2, -a+1)
        sage: P3 = K.ideal(3, a+1)
        sage: P5 = K.ideal(a)
        sage: KS2, gens, fromKS2, toKS2 = pSelmerGroup(K, [P2, P3, P5], 2)
        sage: KS2
        Vector space of dimension 4 over Finite Field of size 2
        sage: gens
        [a + 1, a, 2, -1]

    Each generator must have even valuation at primes not in `S`::

        sage: [K.ideal(g).factor() for g in gens]
        [(Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1)),
         Fractional ideal (-a),
         (Fractional ideal (2, a + 1))^2,
         1]

        sage: toKS2(10)
        (0, 0, 1, 1)
        sage: fromKS2([0,0,1,1])
        -2
        sage: K(10/(-2)).is_square()
        True

        sage: KS3, gens, fromKS3, toKS3 = pSelmerGroup(K, [P2, P3, P5], 3)
        sage: KS3
        Vector space of dimension 3 over Finite Field of size 3
        sage: gens
        [1/2, 1/4*a + 1/4, a]

    The ``to`` and ``from`` maps are inverses of each other::

        sage: K.<a> = QuadraticField(-5)
        sage: S = K.ideal(30).support()
        sage: KS2, gens, fromKS2, toKS2 = pSelmerGroup(K, S, 2)
        sage: KS2
        Vector space of dimension 5 over Finite Field of size 2
        sage: assert all(toKS2(fromKS2(v))==v for v in KS2)
        sage: KS3, gens, fromKS3, toKS3 = pSelmerGroup(K, S, 3)
        sage: KS3
        Vector space of dimension 4 over Finite Field of size 3
        sage: assert all(toKS3(fromKS3(v))==v for v in KS3)
    """
