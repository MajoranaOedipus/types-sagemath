from sage.functions.log import logb as logb
from sage.functions.other import ceil as ceil, sqrt as sqrt
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.special import companion_matrix as companion_matrix
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule as DrinfeldModule
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

class DrinfeldModule_finite(DrinfeldModule):
    """
    This class implements finite Drinfeld `\\mathbb{F}_q[T]`-modules.

    A *finite Drinfeld module* is a Drinfeld module whose base field is
    finite. In this case, the function field characteristic is a prime
    ideal.

    For general definitions and help on Drinfeld modules, see class
    :class:`sage.rings.function_fields.drinfeld_module.drinfeld_module.DrinfeldModule`.

    .. RUBRIC:: Construction:

    The user does not ever need to directly call
    ``DrinfeldModule_finite`` --- the metaclass ``DrinfeldModule`` is
    responsible for instantiating ``DrinfeldModule`` or
    ``DrinfeldModule_finite`` depending on the input::

        sage: Fq = GF(343)
        sage: A.<T> = Fq[]
        sage: K.<z6> = Fq.extension(2)
        sage: phi = DrinfeldModule(A, [z6, 0, 5])
        sage: phi
        Drinfeld module defined by T |--> 5*t^2 + z6

    ::

        sage: isinstance(phi, DrinfeldModule)
        True
        sage: from sage.rings.function_field.drinfeld_modules.finite_drinfeld_module import DrinfeldModule_finite
        sage: isinstance(phi, DrinfeldModule_finite)
        True

    The user should never use ``DrinfeldModule_finite`` to test if a
    Drinfeld module is finite, but rather the ``is_finite`` method::

        sage: phi.is_finite()
        True

    .. RUBRIC:: Complex multiplication of rank two finite Drinfeld modules

    We can handle some aspects of the theory of complex multiplication
    of finite Drinfeld modules. Apart from the method
    ``frobenius_endomorphism``, we only handle rank two Drinfeld
    modules.

    First of all, it is easy to create the Frobenius endomorphism::

        sage: frobenius_endomorphism = phi.frobenius_endomorphism()
        sage: frobenius_endomorphism
        Endomorphism of Drinfeld module defined by T |--> 5*t^2 + z6
          Defn: t^2

    Its characteristic polynomial can be computed::

        sage: chi = phi.frobenius_charpoly()
        sage: chi
        X^2 + (T + 2*z3^2 + 2*z3 + 1)*X + 2*T^2 + (z3^2 + z3 + 4)*T + 2*z3
        sage: frob_pol = frobenius_endomorphism.ore_polynomial()
        sage: chi(frob_pol, phi(T))
        0

    as well as its trace and norm::

        sage: phi.frobenius_trace()
        6*T + 5*z3^2 + 5*z3 + 6
        sage: phi.frobenius_trace() == -chi[1]
        True
        sage: phi.frobenius_norm()
        2*T^2 + (z3^2 + z3 + 4)*T + 2*z3

    We can decide if a Drinfeld module is ordinary or supersingular::

        sage: phi.is_ordinary()
        True
        sage: phi.is_supersingular()
        False

    .. RUBRIC:: Inverting the Drinfeld module

    The morphism that defines a Drinfeld module is injective (see
    [Gos1998]_, cor. 4.5.2). If the Drinfeld module is finite, one can
    retrieve preimages::

        sage: a = A.random_element()
        sage: phi.invert(phi(a)) == a
        True
    """
    def __init__(self, gen, category) -> None:
        """
        Initialize ``self``.

        Validity of the input is checked in ``__classcall_private__``. The
        ``__init__`` just saves attributes.

        INPUT:

        - ``function_ring`` -- a univariate polynomial ring whose base
          is a finite field

        - ``gen`` -- the generator of the Drinfeld module as a list of
          coefficients or an Ore polynomial

        - ``name`` -- (default: ``'t'``) the name of the Ore polynomial
          ring gen

        TESTS::

            sage: Fq = GF(25)
            sage: A.<T> = Fq[]
            sage: K.<z12> = Fq.extension(6)
            sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
            sage: gen = [p_root, z12^3, z12^5]
            sage: phi = DrinfeldModule(A, gen)
            sage: ore_polring = phi.ore_polring()
            sage: phi._gen == ore_polring(gen)
            True
        """
    def frobenius_endomorphism(self):
        """
        Return the Frobenius endomorphism of the Drinfeld module as a
        morphism object.

        Let `q` be the order of the base field of the function ring. The
        *Frobenius endomorphism* is defined as the endomorphism whose
        defining Ore polynomial is `t^q`.

        EXAMPLES::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: phi.frobenius_endomorphism()
            Endomorphism of Drinfeld module defined by T |--> z6*t^2 + 1
              Defn: t^2

        TESTS::

            sage: from sage.rings.function_field.drinfeld_modules.morphism import DrinfeldModuleMorphism
            sage: isinstance(phi.frobenius_endomorphism(), DrinfeldModuleMorphism)
            True
        """
    def frobenius_charpoly(self, var: str = 'X', algorithm=None):
        '''
        Return the characteristic polynomial of the Frobenius
        endomorphism.

        Let `\\mathbb{F}_q` be the base field of the function ring. The
        *characteristic polynomial* `\\chi` *of the Frobenius endomorphism*
        is defined in [Gek1991]_. An important feature of this
        polynomial is that it is monic, univariate, and has coefficients
        in the function ring. As in our case the function
        ring is a univariate polynomial ring, it is customary to see the
        characteristic polynomial of the Frobenius endomorphism as a
        bivariate polynomial.

        Let `\\chi = X^r + \\sum_{i=0}^{r-1} A_{i}(T)X^{i}` be the
        characteristic polynomial of the Frobenius endomorphism, and
        let `t^n` be the Ore polynomial that defines the Frobenius
        endomorphism of `\\phi`; by definition, `n` is the degree of `K`
        over the base field `\\mathbb{F}_q`. Then we have

        .. MATH::

            \\chi(t^n)(\\phi(T))
            = t^{nr} + \\sum_{i=1}^{r} \\phi_{A_{i}}t^{n(i)}
            = 0,

        with `\\deg(A_i) \\leq \\frac{n(r-i)}{r}`.

        Note that the *Frobenius trace* is defined as `A_{r-1}(T)` and the
        *Frobenius norm* is defined as `A_0(T)`.

        INPUT:

        - ``var`` (default: ``\'X\'``) -- the name of the second variable
        - ``algorithm`` (default: ``None``) -- the algorithm
          used to compute the characteristic polynomial

        .. NOTE:

        Available algorithms are:

            - ``\'CSA\'`` -- it exploits the fact that `K\\{\\tau\\}` is a
              central simple algebra (CSA) over `\\mathbb
              F_q[\\text{Frob}_\\phi]` (see Chapter 4 of [CL2023]_).
            - ``\'crystalline\'`` -- it uses the action of the Frobenius
              on the crystalline cohomology (see [MS2023]_).
            - ``\'gekeler\'`` -- it tries to identify coefficients by
              writing that the characteristic polynomial annihilates the
              Frobenius endomorphism; this algorithm may fail is some
              cases (see [Gek2008]_).
            - ``\'motive\'`` -- it uses the action of the Frobenius on the
              Anderson motive (see Chapter 2 of [CL2023]_).

        The method raises an exception if the user asks for an
        unimplemented algorithm, even if the characteristic polynomial
        has already been computed.

        EXAMPLES::

            sage: Fq = GF(25)
            sage: A.<T> = Fq[]
            sage: K.<z12> = Fq.extension(6)
            sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
            sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
            sage: phi.frobenius_charpoly()
            X^2 + ((4*z2 + 4)*T^3 + (z2 + 3)*T^2 + 3*T + 2*z2 + 3)*X + 3*z2*T^6 + (4*z2 + 3)*T^5 + (4*z2 + 4)*T^4 + 2*T^3 + (3*z2 + 3)*T^2 + (z2 + 2)*T + 4*z2

        ::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: chi = phi.frobenius_charpoly(algorithm=\'crystalline\')
            sage: chi
            X^2 + ((3*z3^2 + z3 + 4)*T + 4*z3^2 + 6*z3 + 3)*X + (5*z3^2 + 2*z3)*T^2 + (4*z3^2 + 3*z3)*T + 5*z3^2 + 2*z3

        ::

            sage: frob_pol = phi.frobenius_endomorphism().ore_polynomial()
            sage: chi(frob_pol, phi(T))
            0
            sage: phi.frobenius_charpoly(algorithm=\'motive\')(phi.frobenius_endomorphism())
            Endomorphism of Drinfeld module defined by T |--> z6*t^2 + 1
              Defn: 0

        ::

            sage: phi.frobenius_charpoly(algorithm="NotImplemented")
            Traceback (most recent call last):
            ...
            NotImplementedError: algorithm "NotImplemented" not implemented

        ALGORITHM:

            If the user specifies an algorithm, then the characteristic
            polynomial is computed according to the user\'s input (see
            the note above), even if it had already been computed.

            If no algorithm is given, then the function either returns a
            cached value, or if no cached value is available, the
            function computes the Frobenius characteristic polynomial
            from scratch. In that case, if the rank `r` is less than the
            extension degree `n`, then the ``crystalline`` algorithm is
            used, while the ``CSA`` algorithm is used otherwise.

        TESTS::

            sage: Fq = GF(9)
            sage: A.<T> = Fq[]
            sage: k.<zk> = Fq.extension(2)
            sage: K.<z> = k.extension(3)

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^8, z^7])
            sage: phi.frobenius_charpoly(algorithm=\'CSA\')
            X^2 + (2*T^3 + (2*z2 + 2)*T^2 + (z2 + 1)*T + 2*z2)*X + z2*T^6 + (2*z2 + 2)*T^3 + 2
            sage: phi.frobenius_charpoly(algorithm=\'crystalline\')
            X^2 + (2*T^3 + (2*z2 + 2)*T^2 + (z2 + 1)*T + 2*z2)*X + z2*T^6 + (2*z2 + 2)*T^3 + 2
            sage: phi.frobenius_charpoly(algorithm=\'gekeler\')
            X^2 + (2*T^3 + (2*z2 + 2)*T^2 + (z2 + 1)*T + 2*z2)*X + z2*T^6 + (2*z2 + 2)*T^3 + 2
            sage: phi.frobenius_charpoly(algorithm=\'motive\')
            X^2 + (2*T^3 + (2*z2 + 2)*T^2 + (z2 + 1)*T + 2*z2)*X + z2*T^6 + (2*z2 + 2)*T^3 + 2
            sage: phi.frobenius_charpoly()(phi.frobenius_endomorphism()).ore_polynomial()
            0

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^2, z^3, z^4])
            sage: phi.frobenius_charpoly(algorithm=\'CSA\')
            X^3 + ((z2 + 1)*T^2 + (z2 + 1)*T + z2 + 2)*X^2 + ((z2 + 2)*T^4 + 2*T^3 + z2*T^2 + T + 2*z2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'crystalline\')
            X^3 + ((z2 + 1)*T^2 + (z2 + 1)*T + z2 + 2)*X^2 + ((z2 + 2)*T^4 + 2*T^3 + z2*T^2 + T + 2*z2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'gekeler\')
            X^3 + ((z2 + 1)*T^2 + (z2 + 1)*T + z2 + 2)*X^2 + ((z2 + 2)*T^4 + 2*T^3 + z2*T^2 + T + 2*z2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'motive\')
            X^3 + ((z2 + 1)*T^2 + (z2 + 1)*T + z2 + 2)*X^2 + ((z2 + 2)*T^4 + 2*T^3 + z2*T^2 + T + 2*z2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly()(phi.frobenius_endomorphism()).ore_polynomial()
            0

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^8, z^7, z^20])
            sage: phi.frobenius_charpoly(algorithm=\'CSA\')
            X^3 + (z2*T^2 + z2*T + z2 + 1)*X^2 + (T^4 + (2*z2 + 1)*T^3 + (z2 + 2)*T^2 + (2*z2 + 1)*T + z2 + 2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'crystalline\')
            X^3 + (z2*T^2 + z2*T + z2 + 1)*X^2 + (T^4 + (2*z2 + 1)*T^3 + (z2 + 2)*T^2 + (2*z2 + 1)*T + z2 + 2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'gekeler\')
            X^3 + (z2*T^2 + z2*T + z2 + 1)*X^2 + (T^4 + (2*z2 + 1)*T^3 + (z2 + 2)*T^2 + (2*z2 + 1)*T + z2 + 2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly(algorithm=\'motive\')
            X^3 + (z2*T^2 + z2*T + z2 + 1)*X^2 + (T^4 + (2*z2 + 1)*T^3 + (z2 + 2)*T^2 + (2*z2 + 1)*T + z2 + 2)*X + T^6 + 2*z2*T^3 + 2*z2 + 1
            sage: phi.frobenius_charpoly()(phi.frobenius_endomorphism()).ore_polynomial()
            0

        Check that ``var`` inputs are taken into account for cached
        characteristic polynomials::

            sage: Fq = GF(2)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [z, 0, 1])
            sage: phi.frobenius_charpoly()
            X^2 + X + T^2 + T + 1
            sage: phi.frobenius_charpoly(var=\'Foo\')
            Foo^2 + Foo + T^2 + T + 1
            sage: phi.frobenius_charpoly(var=\'Bar\')
            Bar^2 + Bar + T^2 + T + 1
        '''
    def frobenius_norm(self):
        """
        Return the Frobenius norm of the Drinfeld module.

        Let `C(X) = \\sum_{i=0}^r a_iX^{i}` denote the characteristic
        polynomial of the Frobenius endomorphism. The Frobenius norm
        is `a_{0}`, and given by the formula

        .. MATH::

            a_0 = (-1)^{nr - n -r}
                  \\mathrm{Norm}_{K/\\mathbb F_q}(\\Delta)^{-1}
                  p^{n / \\mathrm{deg}(p)},

        where `K` is the ground field, which as degree `n` over
        `\\mathbb F_q`, `r` is the rank of the Drinfeld module,
        and `\\Delta` is the leading coefficient of the generator.
        This formula is given in Theorem~4.2.7 of [Pap2023]_.

        Note that the Frobenius norm computed by this method may be
        different than what is computed as the isogeny norm of the
        Frobenius endomorphism (see :meth:`norm` on the Frobenius
        endomorphism), which is an ideal defined of the function ring
        given by its monic generator; the Frobenius norm may not be
        monic.

        EXAMPLES::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: frobenius_norm = phi.frobenius_norm()
            sage: frobenius_norm
            (5*z3^2 + 2*z3)*T^2 + (4*z3^2 + 3*z3)*T + 5*z3^2 + 2*z3

        ::

            sage: n = 2  # Degree of the base field over Fq
            sage: frobenius_norm.degree() == n
            True

        ::

            sage: frobenius_norm == phi.frobenius_charpoly()[0]
            True

        ::

            sage: lc = frobenius_norm.leading_coefficient()
            sage: isogeny_norm = phi.frobenius_endomorphism().norm()
            sage: isogeny_norm.gen() == frobenius_norm / lc
            True
            sage: A.ideal(frobenius_norm) == isogeny_norm
            True

        ALGORITHM:

            The Frobenius norm is computed using the formula, by
            Gekeler, given in [MS2019]_, Section 4, Proposition 3.
        """
    def frobenius_trace(self, algorithm=None):
        """
        Return the Frobenius trace of the Drinfeld module.

        Let `C(X) = \\sum_{i=0}^r a_iX^{i}` denote the characteristic
        polynomial of the Frobenius endomorphism. The Frobenius trace
        is `-a_{r-1}`. This is an element of the regular function ring
        and if `n` is the degree of the base field over `\\mathbb{F}_q`,
        then the Frobenius trace has degree at most `\\frac{n}{r}`.

        INPUT:

        - ``algorithm`` (default: ``None``) -- the algorithm
          used to compute the characteristic polynomial

        .. NOTE:

        Available algorithms are:

            - ``'CSA'`` -- it exploits the fact that `K\\{\\tau\\}` is a
              central simple algebra (CSA) over `\\mathbb
              F_q[\\text{Frob}_\\phi]` (see Chapter 4 of [CL2023]_).
            - ``'crystalline'`` -- it uses the action of the Frobenius
              on the crystalline cohomology (see [MS2023]_).

        The method raises an exception if the user asks for an
        unimplemented algorithm, even if the characteristic has already
        been computed. See :meth:`frobenius_charpoly` for more details.

        EXAMPLES::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: frobenius_trace = phi.frobenius_trace()
            sage: frobenius_trace
            (4*z3^2 + 6*z3 + 3)*T + 3*z3^2 + z3 + 4

        ::

            sage: n = 2  # Degree over Fq of the base codomain
            sage: frobenius_trace.degree() <= n/2
            True

        ::

            sage: frobenius_trace == -phi.frobenius_charpoly()[1]
            True

        One can specify an algorithm::

            sage: psi = DrinfeldModule(A, [z6, 1, z6^3, z6 + 1])
            sage: psi.frobenius_trace(algorithm='crystalline')
            z3^2 + 6*z3 + 2
            sage: psi.frobenius_trace(algorithm='CSA')
            z3^2 + 6*z3 + 2

        ALGORITHM:

            If the user specifies an algorithm, then the trace is
            computed according to the user's input (see the note above),
            even if the Frobenius trace or the Frobenius characteristic
            polynomial had already been computed.

            If no algorithm is given, then the function either returns a
            cached value, or if no cached value is available, the
            function computes the Frobenius trace from scratch. In that
            case, if the rank `r` is less than the extension degree `n`,
            then the ``crystalline`` algorithm is used, while the
            ``CSA`` algorithm is used otherwise.

        TESTS:

        These test values are taken from :meth:`frobenius_charpoly`::

            sage: Fq = GF(9)
            sage: A.<T> = Fq[]
            sage: k.<zk> = Fq.extension(2)
            sage: K.<z> = k.extension(3)

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^8, z^7])
            sage: phi.frobenius_trace(algorithm='CSA')
            T^3 + (z2 + 1)*T^2 + (2*z2 + 2)*T + z2
            sage: phi.frobenius_trace(algorithm='crystalline')
            T^3 + (z2 + 1)*T^2 + (2*z2 + 2)*T + z2
            sage: charpoly = phi.frobenius_charpoly()
            sage: trace = phi.frobenius_trace()
            sage: trace == -charpoly[1]
            True

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^2, z^3, z^4])
            sage: phi.frobenius_trace(algorithm='CSA')
            (2*z2 + 2)*T^2 + (2*z2 + 2)*T + 2*z2 + 1
            sage: phi.frobenius_trace(algorithm='crystalline')
            (2*z2 + 2)*T^2 + (2*z2 + 2)*T + 2*z2 + 1
            sage: charpoly = phi.frobenius_charpoly()
            sage: trace = phi.frobenius_trace()
            sage: trace == -charpoly[2]
            True

        ::

            sage: phi = DrinfeldModule(A, [K(zk), z^8, z^7, z^20])
            sage: phi.frobenius_trace(algorithm='CSA')
            2*z2*T^2 + 2*z2*T + 2*z2 + 2
            sage: phi.frobenius_trace(algorithm='crystalline')
            2*z2*T^2 + 2*z2*T + 2*z2 + 2
            sage: charpoly = phi.frobenius_charpoly()
            sage: trace = phi.frobenius_trace()
            sage: trace == -charpoly[2]
            True
        """
    def invert(self, ore_pol):
        """
        Return the preimage of the input under the Drinfeld module, if it
        exists.

        INPUT:

        - ``ore_pol`` -- the Ore polynomial whose preimage we want to
          compute

        EXAMPLES::

            sage: Fq = GF(25)
            sage: A.<T> = Fq[]
            sage: K.<z12> = Fq.extension(6)
            sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
            sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
            sage: a = A.random_element()
            sage: phi.invert(phi(a)) == a
            True
            sage: phi.invert(phi(T)) == T
            True
            sage: phi.invert(phi(Fq.gen())) == Fq.gen()
            True

        When the input is not in the image of the Drinfeld module, an
        exception is raised::

            sage: t = phi.ore_polring().gen()
            sage: phi.invert(t + 1)
            Traceback (most recent call last):
            ...
            ValueError: input must be in the image of the Drinfeld module

        ::

            sage: phi.invert(t^4 + t^2 + 1)
            Traceback (most recent call last):
            ...
            ValueError: input must be in the image of the Drinfeld module

        ALGORITHM:

            The algorithm relies on the inversion of a linear algebra
            system. See [MS2019]_, 3.2.5 for details.

        TESTS::

            sage: a = A.random_element()
            sage: cat = phi.category()
            sage: phi_r1 = cat.random_object(1)
            sage: phi_r1.invert(phi_r1(a)) == a
            True
            sage: phi_r2 = cat.random_object(2)
            sage: phi_r2.invert(phi_r2(a)) == a
            True
            sage: phi_r3 = cat.random_object(3)
            sage: phi_r3.invert(phi_r3(a)) == a
            True
            sage: phi_r4 = cat.random_object(4)
            sage: phi_r4.invert(phi_r4(a)) == a
            True
            sage: phi_r5 = cat.random_object(5)
            sage: phi_r5.invert(phi_r5(a)) == a
            True

        ::

            sage: B.<X> = Fq[]
            sage: phi_r5.invert(X)
            Traceback (most recent call last):
            ...
            TypeError: input must be an Ore polynomial
        """
    def is_isogenous(self, psi):
        """
        Return ``True`` when ``self`` is isogenous to the other
        Drinfeld module.

        If the Drinfeld modules do not belong to the same category, an
        exception is raised.

        EXAMPLES::

            sage: Fq = GF(2)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(3)
            sage: psi = DrinfeldModule(A, [z, z + 1, z^2 + z + 1])
            sage: phi = DrinfeldModule(A, [z, z^2 + z + 1, z^2 + z])
            sage: phi.is_isogenous(psi)
            True

        ::

            sage: chi = DrinfeldModule(A, [z, z + 1, z^2 + z])
            sage: phi.is_isogenous(chi)
            False

        ::

            sage: mu = DrinfeldModule(A, [z + 1, z^2 + z + 1, z^2 + z])
            sage: phi.is_isogenous(mu)
            Traceback (most recent call last):
            ...
            TypeError: Drinfeld modules are not in the same category

        ::

            sage: mu = 1
            sage: phi.is_isogenous(mu)
            Traceback (most recent call last):
            ...
            TypeError: input must be a Drinfeld module

        ALGORITHM:

        Two Drinfeld A-modules of equal characteristic are isogenous
        if and only if:

        - they have the same rank
        - the characteristic polynomial of the Frobenius endomorphism
          for both Drinfeld modules are equal.
        """
    def is_supersingular(self):
        """
        Return ``True`` if this Drinfeld module is supersingular.

        A Drinfeld module is supersingular if and only if its
        height equals its rank.

        EXAMPLES::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: phi.is_supersingular()
            True
            sage: phi(phi.characteristic())   # Purely inseparable
            z6*t^2

        In rank two, a Drinfeld module is either ordinary or
        supersinguler. In higher ranks, it could be neither of
        the two::

            sage: psi = DrinfeldModule(A, [1, 0, z6, z6])
            sage: psi.is_ordinary()
            False
            sage: psi.is_supersingular()
            False
        """
    def is_ordinary(self):
        """
        Return ``True`` if this Drinfeld module is ordinary.

        A Drinfeld module is ordinary if and only if its
        height is one.

        EXAMPLES::

            sage: Fq = GF(343)
            sage: A.<T> = Fq[]
            sage: K.<z6> = Fq.extension(2)
            sage: phi = DrinfeldModule(A, [1, 0, z6])
            sage: phi.is_ordinary()
            False

        ::

            sage: phi = DrinfeldModule(A, [1, z6, 0, z6])
            sage: phi.is_ordinary()
            True
        """
