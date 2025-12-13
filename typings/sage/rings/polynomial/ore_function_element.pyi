from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.structure.element import AlgebraElement as AlgebraElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp

class OreFunction(AlgebraElement):
    """
    An element in a Ore function field.
    """
    def __init__(self, parent, numerator, denominator=None, simplify: bool = True) -> None:
        """
        Initialize this element.

        TESTS::

            sage: R.<t> = GF(5)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: K = A.fraction_field()
            sage: f = K.random_element()

            sage: # TestSuite(f).run()
        """
    def __hash__(self):
        """
        Return a hash of this element.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: f = K.random_element()
            sage: hash(f)  # random
            1700763101013238501
        """
    def left_denominator(self):
        """
        Return `s` if this element reads `s^{-1} t`.

        WARNING:

        When the twisting morphism is bijective, there is a unique
        irreducible fraction of the form `s^{-1} t` representing this
        element. Here irreducible means that `s` and `t` have no
        nontrivial common left divisor.
        Under this additional assumption, this method always returns
        this distinguished denominator `s`.

        On the contrary, when the twisting morphism is not bijective,
        this method returns the denominator of *some* fraction
        representing the input element.
        However, the software guarantees that the method :meth:`right_numerator`
        outputs the numerator of the *same* fraction.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: s = x + a
            sage: t = x^2 + a*x + a^2
            sage: f = s^(-1) * t
            sage: f.left_denominator()
            x + a

        In the example below, a simplification occurs::

            sage: # needs sage.rings.finite_rings
            sage: u = S.random_element(degree=2)
            sage: g = (u*s)^(-1) * (u*t)
            sage: g.left_denominator()
            x + a

        When the twisting morphism is not invertible, simplifications
        do not occur in general::

            sage: R.<z> = GF(11)[]
            sage: sigma = R.hom([z^2])
            sage: S.<x> = R['x', sigma]
            sage: s = (x + z)^2
            sage: t = (x + z) * (x^2 + z^2)
            sage: f = s^(-1) * t                                                        # needs sage.rings.function_field
            sage: f.left_denominator()                                                  # needs sage.rings.function_field
            x^2 + (z^2 + z)*x + z^2

        However, the following always holds true::

            sage: f == f.left_denominator()^(-1) * f.right_numerator()                  # needs sage.rings.function_field
            True

        .. SEEALSO::

            :meth:`right_numerator`, :meth:`left_numerator`, :meth:`right_denominator`
        """
    def right_numerator(self):
        """
        Return `t` if this element reads `s^{-1} t`.

        WARNING:

        When the twisting morphism is bijective, there is a unique
        irreducible fraction of the form `s^{-1} t` representing this
        element. Here irreducible means that `s` and `t` have no
        nontrivial common left divisor.
        Under this additional assumption, this method always returns
        this distinguished numerator `t`.

        On the contrary, when the twisting morphism is not bijective,
        this method returns the numerator of *some* fraction
        representing the input element.
        However, the software guarantees that the method :meth:`left_denominator`
        outputs the numerator of the *same* fraction.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: s = x + a
            sage: t = x^2 + a*x + a^2
            sage: f = s^(-1) * t
            sage: f.right_numerator()
            x^2 + a*x + a^2

        In the example below, a simplification occurs::

            sage: # needs sage.rings.finite_rings
            sage: u = S.random_element(degree=2)
            sage: g = (u*s)^(-1) * (u*t)
            sage: g.right_numerator()
            x^2 + a*x + a^2

        .. SEEALSO::

            :meth:`left_denominator`, :meth:`left_numerator`, :meth:`right_denominator`
        """
    def right_denominator(self):
        """
        Return `s` if this element reads `t s^{-1}`.

        WARNING:

        When the twisting morphism is bijective, there is a unique
        irreducible fraction of the form `t s^{-1}` representing this
        element. Here irreducible means that `s` and `t` have no
        nontrivial common right divisor.
        Under this additional assumption, this method always returns
        this distinguished denominator `s`.

        On the contrary, when the twisting morphism is not bijective,
        the existence of the writing `t s^{-1}` is not guaranteed in
        general. In this case, this method raises an error.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: s = x + a
            sage: t = x^2 + a*x + a^2
            sage: f = t/s
            sage: f.right_denominator()
            x + a

        In the example below, a simplification occurs::

            sage: # needs sage.rings.finite_rings
            sage: u = S.random_element(degree=2)
            sage: g = (t*u) / (s*u)
            sage: g.right_denominator()
            x + a

        .. SEEALSO::

            :meth:`left_numerator`, :meth:`left_denominator`, :meth:`right_numerator`

        TESTS::

            sage: R.<z> = GF(11)[]
            sage: sigma = R.hom([z^2])
            sage: S.<x> = R['x', sigma]
            sage: f = (x + z) / (x - z)                                                 # needs sage.rings.function_field
            sage: f.right_denominator()                                                 # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in z over Finite Field of size 11
              Defn: z |--> z^2
        """
    def left_numerator(self):
        """
        Return `t` if this element reads `t s^{-1}`.

        WARNING:

        When the twisting morphism is bijective, there is a unique
        irreducible fraction of the form `t s^{-1}` representing this
        element. Here irreducible means that `s` and `t` have no
        nontrivial common right divisor.
        Under this additional assumption, this method always returns
        this distinguished numerator `t`.

        On the contrary, when the twisting morphism is not bijective,
        the existence of the writing `t s^{-1}` is not guaranteed in
        general. In this case, this method raises an error.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: s = x + a
            sage: t = x^2 + a*x + a^2
            sage: f = t/s
            sage: f.left_numerator()
            x^2 + a*x + a^2

        In the example below, a simplification occurs::

            sage: # needs sage.rings.finite_rings
            sage: u = S.random_element(degree=2)
            sage: g = (t*u) / (s*u)
            sage: g.left_numerator()
            x^2 + a*x + a^2
        """
    def is_zero(self):
        """
        Return ``True`` if this element is equal to zero.

        EXAMPLES::

            sage: R.<t> = GF(3)[]
            sage: der = R.derivation()
            sage: A.<d> = R['x', der]
            sage: f = t/d
            sage: f.is_zero()
            False
            sage: (f-f).is_zero()
            True
        """
    def __invert__(self):
        """
        Return the inverse of this element.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^2)
            sage: Frob = k.frobenius_endomorphism()
            sage: der = k.derivation(a, twist=Frob)
            sage: S.<x> = k['x', der]
            sage: K = S.fraction_field()
            sage: f = K.random_element()
            sage: g = ~f
            sage: f * g
            1
            sage: ~K(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot divide by zero
        """
    def hilbert_shift(self, s, var=None):
        """
        Return this Ore function with variable shifted by `s`,
        i.e. if this Ore function is `f(x)`, return `f(x+s)`.

        INPUT:

        - ``s`` -- an element in the base ring

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<t> = GF(7)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: K = A.fraction_field()

            sage: f = 1 / (d-t)
            sage: f.hilbert_shift(t)
            d^(-1)

        One can specify another variable name::

            sage: f.hilbert_shift(t, var='x')
            x^(-1)

        When the twisting morphism is not trivial, the output lies
        in a different Ore polynomial ring::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: f = (x-a)^(-2)
            sage: g = f.hilbert_shift(a); g
            x^(-2)
            sage: g.parent()
            Ore Function Field in x over Finite Field in a of size 5^3
             twisted by a |--> a^5 and a*([a |--> a^5] - id)
            sage: g.parent() is S
            False

        This behavior ensures that the Hilbert shift by a fixed element
        defines a homomorphism of fields::

            sage: # needs sage.rings.finite_rings
            sage: U = K.random_element(degree=5)
            sage: V = K.random_element(degree=5)
            sage: s = k.random_element()
            sage: (U+V).hilbert_shift(s) == U.hilbert_shift(s) + V.hilbert_shift(s)
            True
            sage: (U*V).hilbert_shift(s) == U.hilbert_shift(s) * V.hilbert_shift(s)
            True
        """

class ConstantOreFunctionSection(Map):
    """
    Representation of the canonical homomorphism from the constants of a Ore
    function field to the base field.

    This class is needed by the coercion system.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: from sage.rings.polynomial.ore_polynomial_element import ConstantOrePolynomialSection
        sage: k.<a> = GF(5^3)
        sage: Frob = k.frobenius_endomorphism()
        sage: S.<x> = k['x', Frob]
        sage: K = S.fraction_field()
        sage: iota = K.coerce_map_from(k)
        sage: sigma = iota.section(); sigma
        Generic map:
          From: Ore Function Field in x over Finite Field in a of size 5^3
                twisted by a |--> a^5
          To:   Finite Field in a of size 5^3
    """

class OreFunctionBaseringInjection(Morphism):
    """
    Representation of the canonical homomorphism from a field `k` into a Ore
    function field over `k`.

    This class is needed by the coercion system.
    """
    def __init__(self, domain, codomain) -> None:
        """
        Initialize this morphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: K = S.fraction_field()                                                # needs sage.rings.function_field
            sage: K.coerce_map_from(K.base_ring())  # indirect doctest                  # needs sage.rings.function_field
            Ore Function base injection morphism:
              From: Fraction Field of Univariate Polynomial Ring in t over Rational Field
              To:   Ore Function Field in x over Fraction Field of Univariate Polynomial Ring in t over Rational Field twisted by t |--> t + 1
        """
    def an_element(self):
        """
        Return an element of the codomain of the ring homomorphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: K = S.fraction_field()
            sage: m = K.coerce_map_from(k)
            sage: m.an_element()
            x
        """
    def section(self):
        """
        Return the canonical homomorphism from the constants of a Ore
        function filed to its base field.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: K = S.fraction_field()
            sage: m = K.coerce_map_from(k)
            sage: m.section()
            Generic map:
              From: Ore Function Field in x over Finite Field in t of size 5^3
                    twisted by t |--> t^5
              To:   Finite Field in t of size 5^3
        """

class OreFunction_with_large_center(OreFunction):
    """
    A special class for elements of Ore function fields whose
    center has finite index.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: k.<a> = GF(5^3)
        sage: Frob = k.frobenius_endomorphism()
        sage: S.<x> = k['x', Frob]
        sage: K = S.fraction_field()
        sage: f = K.random_element()
        sage: from sage.rings.polynomial.ore_function_element import OreFunction_with_large_center
        sage: isinstance(f, OreFunction_with_large_center)
        True

        sage: # TestSuite(f).run()
    """
    def reduced_trace(self, var=None):
        """
        Return the reduced trace of this element.

        INPUT:

        - ``var`` -- string or ``None`` (default: ``None``);
          the name of the central variable

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: a = 1 / (x^2 + t)
            sage: tr = a.reduced_trace(); tr
            3/(z^2 + 2)

        The reduced trace lies in the center of `S`, which is the fraction field
        of a univariate polynomial ring in the variable `z = x^3` over `GF(5)`::

            sage: # needs sage.rings.finite_rings
            sage: tr.parent()
            Fraction Field of Univariate Polynomial Ring in z over Finite Field of size 5
            sage: tr.parent() is K.center()
            True

        We can use explicit conversion to view ``tr`` as a Ore function::

            sage: K(tr)                                                                 # needs sage.rings.finite_rings
            (x^6 + 2)^(-1) * 3

        By default, the name of the central variable is usually ``z`` (see
        :meth:`sage.rings.polynomial.skew_polynomial_ring.OreFunctionField_with_large_center.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_trace(var='u')                                              # needs sage.rings.finite_rings
            3/(u^2 + 2)

        TESTS:

        We check that the reduced trace is additive::

            sage: # needs sage.rings.finite_rings
            sage: a = K.random_element(degree=5)
            sage: b = K.random_element(degree=7)
            sage: a.reduced_trace() + b.reduced_trace() == (a+b).reduced_trace()
            True

        ::

            sage: (a*b).reduced_trace() == (b*a).reduced_trace()                        # needs sage.rings.finite_rings
            True
        """
    def reduced_norm(self, var=None):
        """
        Return the reduced norm of this Ore function.

        INPUT:

        - ``var`` -- string or ``None`` (default: ``None``);
          the name of the central variable

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: a = (x + t) / (x^2 + t^2)
            sage: N = a.reduced_norm(); N
            (z + 2)/(z^2 + 4)

        The reduced norm lies in the center of `S`, which is the fraction field
        of a univariate polynomial ring in the variable `z = x^3` over `GF(5)`. ::

            sage: # needs sage.rings.finite_rings
            sage: N.parent()
            Fraction Field of Univariate Polynomial Ring in z over Finite Field of size 5
            sage: N.parent() is K.center()
            True

        We can use explicit conversion to view ``N`` as a skew polynomial::

            sage: K(N)                                                                  # needs sage.rings.finite_rings
            (x^6 + 4)^(-1) * (x^3 + 2)

        By default, the name of the central variable is usually ``z`` (see
        :meth:`sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_norm(var='u')                                               # needs sage.rings.finite_rings
            (u + 2)/(u^2 + 4)

        TESTS:

        We check that the reduced norm is a multiplicative map::

            sage: # needs sage.rings.finite_rings
            sage: a = K.random_element()
            sage: b = K.random_element()
            sage: a.reduced_norm() * b.reduced_norm() == (a*b).reduced_norm()
            True
        """
