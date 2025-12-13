from .smoothchar import SmoothCharacterGroupQp as SmoothCharacterGroupQp, SmoothCharacterGroupRamifiedQuadratic as SmoothCharacterGroupRamifiedQuadratic, SmoothCharacterGroupUnramifiedQuadratic as SmoothCharacterGroupUnramifiedQuadratic
from .type_space import TypeSpace as TypeSpace
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.modular.modform.element import Newform as Newform
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence
from typing import Self

def LocalComponent(f, p, twist_factor=None):
    '''
    Calculate the local component at the prime `p` of the automorphic
    representation attached to the newform `f`.

    INPUT:

    - ``f`` -- (:class:`~sage.modular.modform.element.Newform`) a newform of weight `k \\ge 2`
    - ``p`` -- integer; prime
    - ``twist_factor`` -- integer congruent to `k` modulo 2 (default: `k - 2`)

    .. NOTE::

        The argument ``twist_factor`` determines the choice of normalisation: if it is
        set to `j \\in \\ZZ`, then the central character of `\\pi_{f, \\ell}` maps `\\ell`
        to `\\ell^j \\varepsilon(\\ell)` for almost all `\\ell`, where `\\varepsilon` is the
        Nebentypus character of `f`.

        In the analytic theory it is conventional to take `j = 0` (the "Langlands
        normalisation"), so the representation `\\pi_f` is unitary; however, this is
        inconvenient for `k` odd, since in this case one needs to choose a square root of `p`
        and thus the map `f \\to \\pi_{f}` is not Galois-equivariant. Hence we use, by default, the
        "Hecke normalisation" given by `j = k - 2`. This is also the most natural normalisation
        from the perspective of modular symbols.

        We also adopt a slightly unusual definition of the principal series: we
        define `\\pi(\\chi_1, \\chi_2)` to be the induction from the Borel subgroup of
        the character of the maximal torus `\\begin{pmatrix} x & \\\\ & y
        \\end{pmatrix} \\mapsto \\chi_1(a) \\chi_2(b) |a|`, so its central character is
        `z \\mapsto \\chi_1(z) \\chi_2(z) |z|`. Thus `\\chi_1 \\chi_2` is the
        restriction to `\\QQ_p^\\times` of the unique character of the id\\\'ele class
        group mapping `\\ell` to `\\ell^{k-1} \\varepsilon(\\ell)` for almost all `\\ell`.
        This has the property that the *set* `\\{\\chi_1, \\chi_2\\}` also depends
        Galois-equivariantly on `f`.

    EXAMPLES::

        sage: Pi = LocalComponent(Newform(\'49a\'), 7); Pi
        Smooth representation of GL_2(Q_7) with conductor 7^2
        sage: Pi.central_character()
        Character of Q_7*, of level 0, mapping 7 |--> 1
        sage: Pi.species()
        \'Supercuspidal\'
        sage: Pi.characters()
        [Character of unramified extension Q_7(s)* (s^2 + 6*s + 3 = 0), of level 1, mapping s |--> -d, 7 |--> 1,
         Character of unramified extension Q_7(s)* (s^2 + 6*s + 3 = 0), of level 1, mapping s |--> d, 7 |--> 1]
    '''

class LocalComponentBase(SageObject):
    """
    Base class for local components of newforms. Not to be directly instantiated; use the :func:`~LocalComponent` constructor function.
    """
    def __init__(self, newform, prime, twist_factor) -> None:
        """
        Standard initialisation function.

        EXAMPLES::

            sage: LocalComponent(Newform('49a'), 7) # indirect doctest
            Smooth representation of GL_2(Q_7) with conductor 7^2
        """
    @abstract_method
    def species(self) -> None:
        """
        The species of this local component, which is either 'Principal
        Series', 'Special' or 'Supercuspidal'.

        EXAMPLES::

            sage: from sage.modular.local_comp.local_comp import LocalComponentBase
            sage: LocalComponentBase(Newform('50a'), 3, 0).species()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method species at ...>
        """
    @abstract_method
    def check_tempered(self) -> None:
        """
        Check that this representation is quasi-tempered, i.e. `\\pi \\otimes
        |\\det|^{j/2}` is tempered. It is well known that local components of
        modular forms are *always* tempered, so this serves as a useful check
        on our computations.

        EXAMPLES::

            sage: from sage.modular.local_comp.local_comp import LocalComponentBase
            sage: LocalComponentBase(Newform('50a'), 3, 0).check_tempered()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method check_tempered at ...>
        """
    def newform(self):
        """
        The newform of which this is a local component.

        EXAMPLES::

            sage: LocalComponent(Newform('50a'), 5).newform()
            q - q^2 + q^3 + q^4 + O(q^6)
        """
    def prime(self):
        """
        The prime at which this is a local component.

        EXAMPLES::

            sage: LocalComponent(Newform('50a'), 5).prime()
            5
        """
    def conductor(self):
        """
        The smallest `r` such that this representation has a nonzero vector fixed by the subgroup
        `\\begin{pmatrix} * & * \\\\ 0 & 1\\end{pmatrix} \\pmod{p^r}`. This is equal to the power of `p` dividing the level of the corresponding newform.

        EXAMPLES::

            sage: LocalComponent(Newform('50a'), 5).conductor()
            2
        """
    def coefficient_field(self):
        """
        The field `K` over which this representation is defined. This is the field generated by the Hecke eigenvalues of the corresponding newform (over whatever base ring the newform is created).

        EXAMPLES::

            sage: LocalComponent(Newforms(50)[0], 3).coefficient_field()
            Rational Field
            sage: LocalComponent(Newforms(Gamma1(10), 3, base_ring=QQbar)[0], 5).coefficient_field()
            Algebraic Field
            sage: LocalComponent(Newforms(DirichletGroup(5).0, 7,names='c')[0], 5).coefficient_field()
            Number Field in c0 with defining polynomial x^2 + (5*zeta4 + 5)*x - 88*zeta4 over its base field
        """
    def twist_factor(self):
        """
        The unique `j` such that `\\begin{pmatrix} p & 0 \\\\ 0 & p\\end{pmatrix}`
        acts as multiplication by `p^j` times a root of unity.

        There are various conventions for this; see the documentation of the
        :func:`~LocalComponent` constructor function for more information.

        The twist factor should have the same parity as the weight of the form,
        since otherwise the map sending `f` to its local component won't be
        Galois equivariant.

        EXAMPLES::

            sage: LocalComponent(Newforms(50)[0], 3).twist_factor()
            0
            sage: LocalComponent(Newforms(50)[0], 3, twist_factor=173).twist_factor()
            173
        """
    def central_character(self):
        """
        Return the central character of this representation. This is the
        restriction to `\\QQ_p^\\times` of the unique smooth character `\\omega`
        of `\\mathbf{A}^\\times / \\QQ^\\times` such that `\\omega(\\varpi_\\ell) =
        \\ell^j \\varepsilon(\\ell)` for all primes `\\ell \\nmid Np`, where
        `\\varpi_\\ell` is a uniformiser at `\\ell`, `\\varepsilon` is the
        Nebentypus character of the newform `f`, and `j` is the twist factor
        (see the documentation for :func:`~LocalComponent`).

        EXAMPLES::

            sage: LocalComponent(Newform('27a'), 3).central_character()
            Character of Q_3*, of level 0, mapping 3 |--> 1

            sage: LocalComponent(Newforms(Gamma1(5), 5, names='c')[0], 5).central_character()
            Character of Q_5*, of level 1, mapping 2 |--> c0 + 1, 5 |--> 125

            sage: LocalComponent(Newforms(DirichletGroup(24)([1, -1,-1]), 3, names='a')[0], 2).central_character()
            Character of Q_2*, of level 3, mapping 7 |--> 1, 5 |--> -1, 2 |--> -2
        """
    def __eq__(self, other):
        '''
        Comparison function.

        EXAMPLES::

            sage: Pi = LocalComponent(Newform("50a"), 5)
            sage: Pi == LocalComponent(Newform("50a"), 3)
            False
            sage: Pi == LocalComponent(Newform("50b"), 5)
            False
            sage: Pi == QQ
            False
            sage: Pi == None
            False
            sage: Pi == loads(dumps(Pi))
            True
        '''
    def __ne__(self, other):
        '''
        Return ``True`` if ``self != other``.

        EXAMPLES::

            sage: Pi = LocalComponent(Newform("50a"), 5)
            sage: Pi != LocalComponent(Newform("50a"), 3)
            True
            sage: Pi != LocalComponent(Newform("50b"), 5)
            True
            sage: Pi != QQ
            True
            sage: Pi != None
            True
            sage: Pi != loads(dumps(Pi))
            False
        '''

class PrimitiveLocalComponent(LocalComponentBase):
    """
    Base class for primitive (twist-minimal) local components.
    """
    def is_primitive(self) -> bool:
        '''
        Return ``True`` if this local component is primitive (has minimal level
        among its character twists).

        EXAMPLES::

            sage: Newform("50a").local_component(5).is_primitive()
            True
        '''
    def minimal_twist(self) -> Self:
        '''
        Return a twist of this local component which has the minimal possible
        conductor.

        EXAMPLES::

            sage: Pi = Newform("50a").local_component(5)
            sage: Pi.minimal_twist() == Pi
            True
        '''

class PrincipalSeries(PrimitiveLocalComponent):
    """
    A principal series representation. This is an abstract base class, not to
    be instantiated directly; see the subclasses
    :class:`~UnramifiedPrincipalSeries` and :class:`~PrimitivePrincipalSeries`.
    """
    def species(self):
        """
        The species of this local component, which is either 'Principal
        Series', 'Special' or 'Supercuspidal'.

        EXAMPLES::

            sage: LocalComponent(Newform('50a'), 3).species()
            'Principal Series'
        """
    def check_tempered(self) -> None:
        """
        Check that this representation is tempered (after twisting by
        `|\\det|^{j/2}`), i.e. that `|\\chi_1(p)| = |\\chi_2(p)| = p^{(j + 1)/2}`.
        This follows from the Ramanujan--Petersson conjecture, as proved by
        Deligne.

        EXAMPLES::

            sage: LocalComponent(Newform('49a'), 3).check_tempered()
        """
    @abstract_method
    def characters(self) -> None:
        """
        Return the two characters `(\\chi_1, \\chi_2)` such this representation
        `\\pi_{f, p}` is equal to the principal series `\\pi(\\chi_1, \\chi_2)`.

        EXAMPLES::

            sage: from sage.modular.local_comp.local_comp import PrincipalSeries
            sage: PrincipalSeries(Newform('50a'), 3, 0).characters()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method characters at ...>
        """

class UnramifiedPrincipalSeries(PrincipalSeries):
    """
    An unramified principal series representation of `{\\rm GL}_2(\\QQ_p)`
    (corresponding to a form whose level is not divisible by `p`).

    EXAMPLES::

        sage: Pi = LocalComponent(Newform('50a'), 3)
        sage: Pi.conductor()
        0
        sage: type(Pi)
        <class 'sage.modular.local_comp.local_comp.UnramifiedPrincipalSeries'>
        sage: TestSuite(Pi).run()
    """
    def satake_polynomial(self):
        """
        Return the Satake polynomial of this representation, i.e.~the polynomial whose roots are `\\chi_1(p), \\chi_2(p)`
        where this representation is `\\pi(\\chi_1, \\chi_2)`. Concretely, this is the polynomial

        .. MATH::

            X^2 - p^{(j - k + 2)/2} a_p(f) X + p^{j + 1} \\varepsilon(p)`.

        An error will be raised if `j \\ne k \\bmod 2`.

        EXAMPLES::

            sage: LocalComponent(Newform('11a'), 17).satake_polynomial()
            X^2 + 2*X + 17
            sage: LocalComponent(Newform('11a'), 17, twist_factor = -2).satake_polynomial()
            X^2 + 2/17*X + 1/17
        """
    def characters(self):
        """
        Return the two characters `(\\chi_1, \\chi_2)` such this representation
        `\\pi_{f, p}` is equal to the principal series `\\pi(\\chi_1, \\chi_2)`.
        These are the unramified characters mapping `p` to the roots of the Satake polynomial,
        so in most cases (but not always) they will be defined over an
        extension of the coefficient field of ``self``.

        EXAMPLES::

            sage: LocalComponent(Newform('11a'), 17).characters()
            [Character of Q_17*, of level 0, mapping 17 |--> d,
             Character of Q_17*, of level 0, mapping 17 |--> -d - 2]
            sage: LocalComponent(Newforms(Gamma1(5), 6, names='a')[1], 3).characters()
            [Character of Q_3*, of level 0, mapping 3 |--> -3/2*a1 + 12,
             Character of Q_3*, of level 0, mapping 3 |--> -3/2*a1 - 12]
        """

class PrimitivePrincipalSeries(PrincipalSeries):
    """
    A ramified principal series of the form `\\pi(\\chi_1, \\chi_2)`
    where `\\chi_1` is unramified but `\\chi_2` is not.

    EXAMPLES::

        sage: Pi = LocalComponent(Newforms(Gamma1(13), 2, names='a')[0], 13)
        sage: type(Pi)
        <class 'sage.modular.local_comp.local_comp.PrimitivePrincipalSeries'>
        sage: TestSuite(Pi).run()
    """
    def characters(self):
        """
        Return the two characters `(\\chi_1, \\chi_2)` such that the local component `\\pi_{f, p}` is the induction of the character `\\chi_1 \\times \\chi_2` of the Borel subgroup.

        EXAMPLES::

            sage: LocalComponent(Newforms(Gamma1(13), 2, names='a')[0], 13).characters()
            [Character of Q_13*, of level 0, mapping 13 |--> 3*a0 + 2,
             Character of Q_13*, of level 1, mapping 2 |--> a0 + 2, 13 |--> -3*a0 - 7]
        """

class PrimitiveSpecial(PrimitiveLocalComponent):
    """
    A primitive special representation: that is, the Steinberg representation
    twisted by an unramified character. All such representations have conductor
    1.

    EXAMPLES::

        sage: Pi = LocalComponent(Newform('37a'), 37)
        sage: Pi.species()
        'Special'
        sage: Pi.conductor()
        1
        sage: type(Pi)
        <class 'sage.modular.local_comp.local_comp.PrimitiveSpecial'>
        sage: TestSuite(Pi).run()
    """
    def species(self):
        """
        The species of this local component, which is either 'Principal
        Series', 'Special' or 'Supercuspidal'.

        EXAMPLES::

            sage: LocalComponent(Newform('37a'), 37).species()
            'Special'
        """
    def characters(self):
        """
        Return the defining characters of this representation. In this case, it
        will return the unique unramified character `\\chi` of `\\QQ_p^\\times`
        such that this representation is equal to `\\mathrm{St} \\otimes \\chi`,
        where `\\mathrm{St}` is the Steinberg representation (defined as the
        quotient of the parabolic induction of the trivial character by its
        trivial subrepresentation).

        EXAMPLES:

        Our first example is the newform corresponding to an elliptic curve of
        conductor `37`. This is the nontrivial quadratic twist of Steinberg,
        corresponding to the fact that the elliptic curve has non-split
        multiplicative reduction at 37::

            sage: LocalComponent(Newform('37a'), 37).characters()
            [Character of Q_37*, of level 0, mapping 37 |--> -1]

        We try an example in odd weight, where the central character isn't
        trivial::

            sage: Pi = LocalComponent(Newforms(DirichletGroup(21)([-1, 1]), 3, names='j')[0], 7); Pi.characters()
            [Character of Q_7*, of level 0, mapping 7 |--> -1/2*j0^2 - 7/2]
            sage: Pi.characters()[0] ^2 == Pi.central_character()
            True

        An example using a non-standard twist factor::

            sage: Pi = LocalComponent(Newforms(DirichletGroup(21)([-1, 1]), 3, names='j')[0], 7, twist_factor=3); Pi.characters()
            [Character of Q_7*, of level 0, mapping 7 |--> -7/2*j0^2 - 49/2]
            sage: Pi.characters()[0]^2 == Pi.central_character()
            True
        """
    def check_tempered(self) -> None:
        """
        Check that this representation is tempered (after twisting by
        `|\\det|^{j/2}` where `j` is the twist factor). Since local components
        of modular forms are always tempered, this is a useful check on our
        calculations.

        EXAMPLES::

            sage: Pi = LocalComponent(Newforms(DirichletGroup(21)([-1, 1]), 3, names='j')[0], 7)
            sage: Pi.check_tempered()
        """

class PrimitiveSupercuspidal(PrimitiveLocalComponent):
    '''
    A primitive supercuspidal representation.

    Except for some exceptional cases when `p = 2` which we do not implement
    here, such representations are parametrized by smooth characters of tamely
    ramified quadratic extensions of `\\QQ_p`.

    EXAMPLES::

        sage: f = Newform("50a")
        sage: Pi = LocalComponent(f, 5)
        sage: type(Pi)
        <class \'sage.modular.local_comp.local_comp.PrimitiveSupercuspidal\'>
        sage: Pi.species()
        \'Supercuspidal\'
        sage: TestSuite(Pi).run()
    '''
    def species(self):
        """
        The species of this local component, which is either 'Principal
        Series', 'Special' or 'Supercuspidal'.

        EXAMPLES::

            sage: LocalComponent(Newform('49a'), 7).species()
            'Supercuspidal'
        """
    @cached_method
    def type_space(self):
        """
        Return a :class:`~sage.modular.local_comp.type_space.TypeSpace` object
        describing the (homological) type space of this newform, which we know
        is dual to the type space of the local component.

        EXAMPLES::

            sage: LocalComponent(Newform('49a'), 7).type_space()
            6-dimensional type space at prime 7 of form q + q^2 - q^4 + O(q^6)
        """
    def characters(self):
        """
        Return the two conjugate characters of `K^\\times`, where `K` is some
        quadratic extension of `\\QQ_p`, defining this representation. An error
        will be raised in some 2-adic cases, since not all 2-adic supercuspidal
        representations arise in this way.

        EXAMPLES:

        The first example from [LW2012]_::

            sage: f = Newform('50a')
            sage: Pi = LocalComponent(f, 5)
            sage: chars = Pi.characters(); chars
            [Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -d - 1, 5 |--> 1,
             Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> d, 5 |--> 1]
            sage: chars[0].base_ring()
            Number Field in d with defining polynomial x^2 + x + 1

        These characters are interchanged by the Frobenius automorphism of `\\GF{25}`::

            sage: chars[0] == chars[1]**5
            True

        A more complicated example (higher weight and nontrivial central character)::

            sage: f = Newforms(GammaH(25, [6]), 3, names='j')[0]; f
            q + j0*q^2 + 1/3*j0^3*q^3 - 1/3*j0^2*q^4 + O(q^6)
            sage: Pi = LocalComponent(f, 5)
            sage: Pi.characters()
            [Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> 1/3*j0^2*d - 1/3*j0^3, 5 |--> 5,
             Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -1/3*j0^2*d, 5 |--> 5]
            sage: Pi.characters()[0].base_ring()
            Number Field in d with defining polynomial x^2 - j0*x + 1/3*j0^2 over its base field

        .. warning::

            The above output isn't actually the same as in Example 2 of
            [LW2012]_, due to an error in the published paper (correction
            pending) -- the published paper has the inverses of the above
            characters.

        A higher level example::

            sage: f = Newform('81a', names='j'); f
            q + j0*q^2 + q^4 - j0*q^5 + O(q^6)
            sage: LocalComponent(f, 3).characters()  # long time (12s on sage.math, 2012)
            [Character of unramified extension Q_3(s)* (s^2 + 2*s + 2 = 0), of level 2, mapping -2*s |--> -2*d + j0, 4 |--> 1, 3*s + 1 |--> -j0*d + 1, 3 |--> 1,
             Character of unramified extension Q_3(s)* (s^2 + 2*s + 2 = 0), of level 2, mapping -2*s |--> 2*d - j0, 4 |--> 1, 3*s + 1 |--> j0*d - 2, 3 |--> 1]

        Some ramified examples::

            sage: Newform('27a').local_component(3).characters()
            [Character of ramified extension Q_3(s)* (s^2 - 6 = 0), of level 2, mapping 2 |--> 1, s + 1 |--> -d, s |--> -1,
             Character of ramified extension Q_3(s)* (s^2 - 6 = 0), of level 2, mapping 2 |--> 1, s + 1 |--> d - 1, s |--> -1]
            sage: LocalComponent(Newform('54a'), 3, twist_factor=4).characters()
            [Character of ramified extension Q_3(s)* (s^2 - 3 = 0), of level 2, mapping 2 |--> 1, s + 1 |--> -1/9*d, s |--> -9,
             Character of ramified extension Q_3(s)* (s^2 - 3 = 0), of level 2, mapping 2 |--> 1, s + 1 |--> 1/9*d - 1, s |--> -9]

        A 2-adic non-example::

            sage: Newform('24a').local_component(2).characters()
            Traceback (most recent call last):
            ...
            ValueError: Totally ramified 2-adic representations are not classified by characters

        Examples where `K^\\times / \\QQ_p^\\times` is not topologically cyclic
        (which complicates the computations greatly)::

            sage: Newforms(DirichletGroup(64, QQ).1, 2, names='a')[0].local_component(2).characters() # long time, random
            [
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 3,
              mapping s |--> 1, 2*s + 1 |--> 1/2*a0, 4*s + 1 |--> 1, -1 |--> 1, 2 |--> 1,
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 3,
              mapping s |--> 1, 2*s + 1 |--> 1/2*a0, 4*s + 1 |--> -1, -1 |--> 1, 2 |--> 1
            ]
            sage: Newform('243a',names='a').local_component(3).characters() # long time
            [Character of ramified extension Q_3(s)* (s^2 - 6 = 0), of level 4, mapping -2*s - 1 |--> -d - 1, 4 |--> 1, 3*s + 1 |--> -d - 1, s |--> 1,
             Character of ramified extension Q_3(s)* (s^2 - 6 = 0), of level 4, mapping -2*s - 1 |--> d, 4 |--> 1, 3*s + 1 |--> d, s |--> 1]
        """
    def check_tempered(self) -> None:
        '''
        Check that this representation is tempered (after twisting by
        `|\\det|^{j/2}` where `j` is the twist factor). Since local components
        of modular forms are always tempered, this is a useful check on our
        calculations.

        Since the computation of the characters attached to this representation
        is not implemented in the odd-conductor case, a NotImplementedError
        will be raised for such representations.

        EXAMPLES::

            sage: LocalComponent(Newform("50a"), 5).check_tempered()
            sage: LocalComponent(Newform("27a"), 3).check_tempered()
        '''

class ImprimitiveLocalComponent(LocalComponentBase):
    """
    A smooth representation which is not of minimal level among its character
    twists. Internally, this is stored as a pair consisting of a minimal local
    component and a character to twist by.
    """
    def __init__(self, newform, prime, twist_factor, min_twist, chi) -> None:
        '''
        EXAMPLES::

            sage: Newform("45a").local_component(3) # indirect doctest
            Smooth representation of GL_2(Q_3) with conductor 3^2, twist of representation of conductor 3^1
        '''
    def is_primitive(self) -> bool:
        '''
        Return ``True`` if this local component is primitive (has minimal level
        among its character twists).

        EXAMPLES::

            sage: Newform("45a").local_component(3).is_primitive()
            False
        '''
    def minimal_twist(self):
        '''
        Return a twist of this local component which has the minimal possible
        conductor.

        EXAMPLES::

            sage: Pi = Newform("75b").local_component(5)
            sage: Pi.minimal_twist()
            Smooth representation of GL_2(Q_5) with conductor 5^1
        '''
    def twisting_character(self):
        '''
        Return the character giving the minimal twist of this representation.

        EXAMPLES::

            sage: Pi = Newform("45a").local_component(3)
            sage: Pi.twisting_character()
            Dirichlet character modulo 3 of conductor 3 mapping 2 |--> -1
        '''
    def species(self):
        '''
        The species of this local component, which is either \'Principal
        Series\', \'Special\' or \'Supercuspidal\'.

        EXAMPLES::

            sage: Pi = Newform("45a").local_component(3)
            sage: Pi.species()
            \'Special\'
        '''
    def characters(self):
        """
        Return the pair of characters (either of `\\QQ_p^*` or of some quadratic
        extension) corresponding to this representation.

        EXAMPLES::

            sage: f = [f for f in Newforms(63, 4, names='a') if f[2] == 1][0]
            sage: f.local_component(3).characters()
            [Character of Q_3*, of level 1, mapping 2 |--> -1, 3 |--> d,
             Character of Q_3*, of level 1, mapping 2 |--> -1, 3 |--> -d - 2]
        """
    def check_tempered(self) -> None:
        """
        Check that this representation is quasi-tempered, i.e. `\\pi \\otimes
        |\\det|^{j/2}` is tempered. It is well known that local components of
        modular forms are *always* tempered, so this serves as a useful check
        on our computations.

        EXAMPLES::

            sage: f = [f for f in Newforms(63, 4, names='a') if f[2] == 1][0]
            sage: f.local_component(3).check_tempered()
        """
