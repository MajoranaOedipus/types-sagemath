from sage.algebras.splitting_algebra import SplittingAlgebra as SplittingAlgebra, solve_with_extension as solve_with_extension
from sage.categories.action import Action as Action
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import cyclotomic_polynomial as cyclotomic_polynomial
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.localization import Localization as Localization
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing_mpair as LaurentPolynomialRing_mpair
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import get_coercion_model as get_coercion_model

def normalize_names_markov(names, markov_trace_version):
    """
    Return a tuple of strings of variable names of length 3 resp. 4 (if
    ``markov_trace_version`` is ``True``) according to the given input names.

    INPUT:

    - ``names`` -- passed to :func:`~sage.structure.category_object.normalize_names`
    - ``markov_trace_version`` -- boolean; if set to ``True`` four names are
      expected the last of which corresponds to the writhe factor of the
      Markov trace

    EXAMPLES::

        sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
        sage: chbr.normalize_names_markov('a, b, c', False)
        ('a', 'b', 'c')
        sage: chbr.normalize_names_markov(('u', 'v', 'w', 's'), False)
        ('u', 'v', 'w')
    """
def register_ring_hom(ring_hom) -> None:
    """
    Register the given ring homomorphism as conversion map.

    EXAMPLES::

        sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
        sage: BR = chbr.CubicHeckeRingOfDefinition()
        sage: BR.create_specialization([E(5), E(7), E(3)])  # indirect doctest
        Universal Cyclotomic Field
        sage: _.convert_map_from(BR)
        Ring morphism:
          From: Multivariate Polynomial Ring in u, v, w
                  over Integer Ring localized at (w,)
          To:   Universal Cyclotomic Field
          Defn: u |--> E(5)
                v |--> E(7)
                w |--> E(3)
    """

class GaloisGroupAction(Action):
    """
    Action on a multivariate polynomial ring by permuting the generators.

    EXAMPLES::

        sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
        sage: from operator import mul
        sage: R.<x, y, z> = ZZ[]
        sage: G = SymmetricGroup(3)
        sage: p = 5*x*y + 3*z**2
        sage: R._unset_coercions_used()
        sage: R.register_action(chbr.GaloisGroupAction(G, R, op=mul))
        sage: s = G([2,3,1])
        sage: s*p
        3*x^2 + 5*y*z
    """

class CubicHeckeExtensionRing(LaurentPolynomialRing_mpair):
    """
    The generic splitting algebra for the irreducible representations of
    the cubic Hecke algebra.

    This ring must contain three invertible indeterminates (representing
    the roots of the cubic equation) together with a third root of unity
    (needed for the 18-dimensional irreducibles of the cubic Hecke algebra
    on 4 strands).

    Therefore this ring is constructed as a multivariate Laurent polynomial
    ring in three indeterminates over a polynomial quotient ring over the
    integers with respect to the minimal polynomial of a third root of unity.

    The polynomial quotient ring is constructed as instance of
    :class:`SplittingAlgebra`.

    INPUT:

    - ``names`` -- (default: ``'u,v,w'``) string containing the names of the
      indeterminates separated by ``,`` or a triple of strings each of which
      are the names of one of the three indeterminates
    - ``order`` -- string (default: ``'degrevlex'``); the term order; see also
      :class:`~sage.rings.polynomial.laurent_polynomial_ring.LaurentPolynomialRing_mpair`
    - ``ring_of_definition`` -- (optional) a :class:`CubicHeckeRingOfDefinition`
      to specify the generic cubic Hecke base ring over which ``self`` may be
      realized as splitting ring via the ``as_splitting_algebra`` method
    - ``third_unity_root_name`` -- string (default: ``'e3'``); for setting the
      name of the third root if unity of ``self``
    - ``markov_trace_version`` -- boolean (default: ``False``); if this is
      set to ``True`` then ``self`` contains one invertible indeterminate in
      addition which is meant to represent the writhe factor of a Markov trace
      on the cubic Hecke algebra and which default name is ``s``

    EXAMPLES::

        sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
        sage: chbr.CubicHeckeExtensionRing('a, b, c')
        Multivariate Laurent Polynomial Ring in a, b, c
          over Splitting Algebra of x^2 + x + 1
            with roots [e3, -e3 - 1]
          over Integer Ring
        sage: _.an_element()
        b^2*c^-1 + e3*a
    """
    def __init__(self, names, order: str = 'degrevlex', ring_of_definition=None, third_unity_root_name: str = 'e3', markov_trace_version: bool = False) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: TestSuite(ER).run()
        """
    def construction(self) -> None:
        """
        Return ``None`` since this construction is not functorial.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: ER._test_category()   # indirect doctest
        """
    def __reduce__(self):
        """
        Used in pickling.

        TESTS::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: loads(dumps(ER)) == ER
            True
        """
    def hom(self, im_gens, codomain=None, check: bool = True, base_map=None):
        """
        Return a homomorphism of ``self``.

        INPUT:

        - ``im_gens`` -- tuple for the image of the generators of ``self``
        - ``codomain`` -- (optional) the codomain of the homomorphism

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: UCF = UniversalCyclotomicField()
            sage: map = ER.hom((UCF.gen(3),) + (UCF(3),UCF(4),UCF(5)))
            sage: ER.an_element()
            b^2*c^-1 + e3*a
            sage: map(_)
            -1/5*E(3) - 16/5*E(3)^2
        """
    def cyclotomic_generator(self):
        """
        Return the third root of unity as generator of the base ring
        of ``self``.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER  = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: ER.cyclotomic_generator()
            e3
            sage: _**3 == 1
            True
        """
    def conjugation(self):
        """
        Return an involution that performs *complex conjugation* with respect
        to base ring considered as order in the complex field.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('x, y, z')
            sage: conj = ER.conjugation()
            sage: conj(ER.an_element())
            y^2*z^-1 + (-e3 - 1)*x
            sage: MER = chbr.CubicHeckeExtensionRing('x, y, z, s', markov_trace_version=True)
            sage: conj = MER.conjugation()
            sage: conj(MER.an_element())
            y^2*z^-1 + (-e3 - 1)*x*s^-1
        """
    def cubic_equation_galois_group(self):
        """
        Return the Galois group of the cubic equation, which is the permutation
        group on the three generators together with its action on ``self``.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: G = ER.cubic_equation_galois_group()
            sage: t = ER.an_element()
            sage: [(g ,g*t) for g in G]
            [((), b^2*c^-1 + e3*a),
            ((1,3,2), a^2*b^-1 + e3*c),
            ((1,2,3), e3*b + a^-1*c^2),
            ((2,3), e3*a + b^-1*c^2),
            ((1,3), a^-1*b^2 + e3*c),
            ((1,2), a^2*c^-1 + e3*b)]
        """
    def mirror_involution(self):
        """
        Return the involution of ``self`` corresponding to the involution of
        the cubic Hecke algebra (with the same name).

        This means that it maps the generators of ``self`` to their inverses.

        .. NOTE::

           The mirror involution of the braid group does not factor through the
           cubic Hecke algebra over its base ring, but it does if it is
           considered as `\\ZZ`-algebra. The base ring elements are transformed
           by this automorphism.

        OUTPUT: the involution as automorphism of ``self``

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('p, q, r')
            sage: ER.mirror_involution()
            Ring endomorphism of Multivariate Laurent Polynomial Ring in p, q, r
                                 over Splitting Algebra of x^2 + x + 1
                                   with roots [e3, -e3 - 1]
                                 over Integer Ring
              Defn: p |--> p^-1
                    q |--> q^-1
                    r |--> r^-1
                    with map of base ring
            sage: _(ER.an_element())
            e3*p^-1 + q^-2*r

            sage: MER = chbr.CubicHeckeExtensionRing('p, q, r, s', markov_trace_version=True)
            sage: MER.mirror_involution()
            Ring endomorphism of Multivariate Laurent Polynomial Ring in p, q, r, s
              over Splitting Algebra of x^2 + x + 1
                with roots [e3, -e3 - 1] over Integer Ring
            Defn: p |--> p^-1
            q |--> q^-1
            r |--> r^-1
            s |--> s^-1
            with map of base ring
            sage: _(MER.an_element())
            e3*p^-1*s + q^-2*r
        """
    def create_specialization(self, im_cubic_equation_roots, im_writhe_parameter=None, var: str = 'T', third_unity_root_name: str = 'E3'):
        """
        Return an appropriate ring containing the elements from the list
        ``im_cubic_equation_roots`` defining a conversion map from ``self`` mapping
        the cubic equation roots of ``self`` to ``im_cubic_equation_roots``.

        INPUT:

        - ``im_cubic_equation_roots`` -- list or tuple of three ring elements
          such that there exists a ring homomorphism from the corresponding
          elements of ``self`` to them

        OUTPUT:

        A common parent containing the elements of ``im_cubic_equation_roots``
        together with their inverses.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: t = ER.an_element(); t
            b^2*c^-1 + e3*a
            sage: Sp1 = ER.create_specialization([E(5), E(7), E(3)]); Sp1
            Universal Cyclotomic Field
            sage: Sp1(t)
            -E(105)^11 - E(105)^16 - E(105)^26 - E(105)^37 - E(105)^41
            - E(105)^58 - E(105)^71 - E(105)^79 - E(105)^86 - E(105)^101
            sage: MER = chbr.CubicHeckeExtensionRing('a, b, c, s', markov_trace_version=True)
            sage: MER.create_specialization([E(5), E(7), E(3)], im_writhe_parameter=E(4))
            Universal Cyclotomic Field
            sage: a, b, c, s = MER.gens()
            sage: Sp1(MER(t)/s)
            E(420) + E(420)^29 + E(420)^89 + E(420)^149 + E(420)^169 + E(420)^209
            + E(420)^253 + E(420)^269 + E(420)^337 + E(420)^389

            sage: Z3 = CyclotomicField(3); E3=Z3.gen()
            sage: Sp2 = ER.create_specialization([E3, E3**2, Z3(1)])
            sage: Sp2(t)
            -1
            sage: MER.create_specialization([E3, E3**2, 1], im_writhe_parameter=2)
            Cyclotomic Field of order 3 and degree 2
            sage: Sp2(MER(t)*s)
            -2

            sage: Sp3 = ER.create_specialization([5, 7, 11])
            sage: Sp3(t)
            5*E3 + 49/11
        """
    def as_splitting_algebra(self):
        """
        Return ``self`` as a :class:`SplittingAlgebra`; that is as an
        extension ring of the corresponding cubic Hecke algebra base ring
        (``self._ring_of_definition``, as a :class:`CubicHeckeRingOfDefinition`)
        splitting its cubic equation into linear factors, such that the roots
        are images of the generators of ``self``.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: GBR = chbr.CubicHeckeRingOfDefinition()
            sage: GER = GBR.extension_ring()
            sage: ER = GER.as_splitting_algebra(); ER
            Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
              over Splitting Algebra of h^3 - u*h^2 + v*h - w
                with roots [a, b, -b - a + u]
              over Multivariate Polynomial Ring in u, v, w
              over Integer Ring localized at (w,)
            sage: ER(GER.an_element())
            a*E3 + ((u/(-w))*a^2 + ((u^2 - v)/w)*a)*b + a - u
            sage: ER(GBR.an_element())
            (u^2 + v*w)/w

            sage: MBR = chbr.CubicHeckeRingOfDefinition(markov_trace_version=True)
            sage: MER = MBR.extension_ring()
            sage: ES = MER.as_splitting_algebra(); ES
            Splitting Algebra of T^2 + T + 1 with roots [E3, -E3 - 1]
              over Splitting Algebra of h^3 - u*h^2 + v*h - w
                with roots [a, b, -b - a + u]
              over Multivariate Polynomial Ring in u, v, w, s
              over Integer Ring localized at (s, w, v, u)
            sage: ES(MER.an_element())
            (((-1)/(-s))*a)*E3 + ((u/(-w))*a^2 + ((u^2 - v)/w)*a)*b + a - u
            sage: ES(MBR.an_element())
            (u^2*s + v*w)/(w*s)
        """
    def field_embedding(self, characteristic: int = 0):
        """
        Return a field embedding of ``self``.

        INPUT:

        - ``characteristic`` -- integer (default: `0`); the characteristic
          of the field

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: ER = BR.extension_ring()
            sage: ER.field_embedding()
            Ring morphism:
            From: Multivariate Laurent Polynomial Ring in a, b, c
                    over Splitting Algebra of x^2 + x + 1
                      with roots [e3, -e3 - 1]
                    over Integer Ring
            To:   Fraction Field of Multivariate Polynomial Ring in a, b, c
                    over Cyclotomic Field of order 3 and degree 2
            Defn: a |--> a
                  b |--> b
                  c |--> c
            with map of base ring

            sage: ER.field_embedding(characteristic=5)
            Ring morphism:
            From: Multivariate Laurent Polynomial Ring in a, b, c
                    over Splitting Algebra of x^2 + x + 1
                      with roots [e3, -e3 - 1]
                    over Integer Ring
            To:   Fraction Field of Multivariate Polynomial Ring in a, b, c
                    over Finite Field in a of size 5^2
            Defn: a |--> a
                  b |--> b
                  c |--> c
            with map of base ring

            sage: MER = ER.markov_trace_version()
            sage: MER.field_embedding()
            Ring morphism:
            From: Multivariate Laurent Polynomial Ring in a, b, c, s
                    over Splitting Algebra of x^2 + x + 1
                      with roots [e3, -e3 - 1]
                    over Integer Ring
            To:   Fraction Field of Multivariate Polynomial Ring in a, b, c, s
                    over Cyclotomic Field of order 3 and degree 2
            Defn: a |--> a
                  b |--> b
                  c |--> c
                  s |--> s
            with map of base ring
        """
    def markov_trace_version(self):
        """
        Return the Markov trace version of ``self``.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: ER = chbr.CubicHeckeExtensionRing('a, b, c')
            sage: ER.markov_trace_version()
            Multivariate Laurent Polynomial Ring in a, b, c, s
              over Splitting Algebra of x^2 + x + 1
                with roots [e3, -e3 - 1] over Integer Ring
        """

class CubicHeckeRingOfDefinition(Localization):
    """
    The *ring of definition* of the cubic Hecke algebra.

    It contains one invertible indeterminate (representing the product of the
    roots of the cubic equation) and two non invertible indeterminates.

    .. NOTE::

        We follow a suggestion by Ivan Marin in the name *ring of definition*.
        We avoid alternative names like *generic* or *universal* base ring
        as these have some issues. The first option could be misleading
        in view of the term *generic point* used in algebraic geometry, which
        would mean the function field in ``u, v, w``, here.

        The second option is problematic since the base ring itself is not a
        universal object. Rather, the universal object is the cubic Hecke algebra
        considered as a `\\ZZ`-algebra including ``u, v, w`` as pairwise commuting
        indeterminates. From this point of view the base ring appears to be a
        subalgebra of this universal object generated by ``u, v, w``.

    INPUT:

    - ``names`` -- (default: ``'u,v,w'``) string containing the names of the
      indeterminates separated by ``,`` or a triple of strings each of which
      are the names of one of the three indeterminates
    - ``order`` -- string (default: ``'degrevlex'``); the term order; see also
      :class:`~sage.rings.polynomial.laurent_polynomial_ring.LaurentPolynomialRing_mpair`
    - ``ring_of_definition`` -- (optional) a :class:`CubicHeckeRingOfDefinition`
      to specify the generic cubic Hecke base ring over which ``self`` may be
      realized as splitting ring via the ``as_splitting_algebra`` method
    - ``markov_trace_version`` -- boolean (default: ``False``); if this is
      set to ``True`` then ``self`` contains one invertible indeterminate in
      addition which is meant to represent the writhe factor of a Markov trace
      on the cubic Hecke algebra and which default name is ``s``

    EXAMPLES::

        sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
        sage: BR = chbr.CubicHeckeRingOfDefinition()
        sage: u, v, w = BR.gens()
        sage: ele = 3*u*v-5*w**(-2)
        sage: ER = BR.extension_ring()
        sage: ER(ele)
        3*a^2*b + 3*a*b^2 + 3*a^2*c + 9*a*b*c + 3*b^2*c
        + 3*a*c^2 + 3*b*c^2 + (-5)*a^-2*b^-2*c^-2
        sage: phi1 = BR.hom( [4,3,1/1] )
        sage: phi1(ele)
        31

        sage: LL.<t> = LaurentPolynomialRing(ZZ)
        sage: phi2=BR.hom( [LL(4),LL(3),t] )
        sage: phi2(ele)
        -5*t^-2 + 36

        sage: BR.create_specialization( [E(5), E(7), E(3)] )
        Universal Cyclotomic Field
        sage: _(ele)
        -3*E(105) - 5*E(105)^2 - 5*E(105)^8 - 5*E(105)^11 - 5*E(105)^17
        - 5*E(105)^23 - 5*E(105)^26 - 5*E(105)^29 - 5*E(105)^32 - 5*E(105)^38
        - 5*E(105)^41 - 5*E(105)^44 - 5*E(105)^47 - 5*E(105)^53 - 5*E(105)^59
        - 5*E(105)^62 - 5*E(105)^68 - 8*E(105)^71 - 5*E(105)^74 - 5*E(105)^83
        - 5*E(105)^86 - 5*E(105)^89 - 5*E(105)^92 - 5*E(105)^101 - 5*E(105)^104
    """
    def __init__(self, names=('u', 'v', 'w', 's'), order: str = 'degrevlex', markov_trace_version: bool = False) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: TestSuite(BR).run()
        """
    def cubic_equation(self, var: str = 'h', as_coefficients: bool = False):
        """
        Return the cubic equation over which the cubic Hecke algebra is defined.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: BR.cubic_equation()
            h^3 - u*h^2 + v*h - w
            sage: BR.cubic_equation(var='t')
            t^3 - u*t^2 + v*t - w
            sage: BR.cubic_equation(as_coefficients=True)
            [-w, v, -u, 1]
        """
    def mirror_involution(self):
        """
        Return the involution of ``self`` corresponding to the involution of the
        cubic Hecke algebra (with the same name).

        This means that it maps the last generator of ``self`` to its inverse
        and both others to their product with the image of the former.

        From the cubic equation for a braid generator `\\beta_i`:

        .. MATH::

            \\beta_i^3 - u \\beta_i^2 + v\\beta_i -w = 0.

        One deduces the following cubic equation for `\\beta_i^{-1}`:

        .. MATH::

            \\beta_i^{-3} -\\frac{v}{w} \\beta_i^{-2} + \\frac{u}{w}\\beta_i^{-1}
            - \\frac{1}{w} = 0.

        .. NOTE::

           The mirror involution of the braid group does not factor through
           the cubic Hecke algebra over its base ring, but it does if it is
           considered as `\\ZZ`-algebra. The base ring elements are transformed
           by this automorphism.

        OUTPUT: the involution as automorphism of ``self``

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: BR.mirror_involution()
            Ring endomorphism of Multivariate Polynomial Ring in u, v, w
                                 over Integer Ring localized at (w,)
              Defn: u |--> v/w
                    v |--> u/w
                    w |--> 1/w
            sage: _(BR.an_element())
            (v^2 + u)/w

            sage: MBR = chbr.CubicHeckeRingOfDefinition(markov_trace_version=True)
            sage: MBR.mirror_involution()
            Ring endomorphism of Multivariate Polynomial Ring in u, v, w, s
                                 over Integer Ring localized at (s, w, v, u)
            Defn: u |--> v/w
            v |--> u/w
            w |--> 1/w
            s |--> 1/s
            sage: _(MBR.an_element())
            (v^2 + u*s)/w
        """
    def create_specialization(self, im_cubic_equation_parameters, im_writhe_parameter=None):
        """
        Return an appropriate Ring containing the elements from the list
        ``im_cubic_equation_parameters`` having a conversion map from ``self``
        mapping the cubic equation parameters of ``self`` to
        ``im_cubic_equation_parameters``.

        INPUT:

        - ``im_cubic_equation_parameters`` -- list or tuple of three ring
          elements such that there exists a ring homomorphism from the
          corresponding elements of ``self`` to them

        OUTPUT:

        A common parent containing the elements of ``im_cubic_equation_parameters``
        together with an inverse of the third element.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: t = BR.an_element(); t
            (u^2 + v*w)/w
            sage: Sp1 = BR.create_specialization([E(5), E(7), E(3)]); Sp1
            Universal Cyclotomic Field
            sage: Sp1(t)
            E(105) + E(105)^8 + E(105)^29 - E(105)^37 + E(105)^43 - E(105)^52
            + E(105)^64 - E(105)^67 + E(105)^71 - E(105)^82 + E(105)^92
            - E(105)^97

            sage: MBR = chbr.CubicHeckeRingOfDefinition(markov_trace_version=True)
            sage: MBR.create_specialization([E(5), E(7), E(3)], im_writhe_parameter=E(4))
            Universal Cyclotomic Field
            sage: u, v, w, s = MBR.gens()
            sage: Sp1(MBR(t)/s)
            E(420)^13 - E(420)^53 + E(420)^73 - E(420)^109 - E(420)^137
            - E(420)^221 + E(420)^253 - E(420)^277 + E(420)^313 - E(420)^361
            + E(420)^373 - E(420)^389

            sage: Z3 = CyclotomicField(3); E3=Z3.gen()
            sage: Sp2 = BR.create_specialization([E3, E3**2, 1]); Sp2
            Cyclotomic Field of order 3 and degree 2
            sage: Sp2(t)
            -2*zeta3 - 2
            sage: MBR.create_specialization([E3, E3**2, 1], im_writhe_parameter=2)
            Cyclotomic Field of order 3 and degree 2
            sage: Sp2(MBR(t)/s)
            -zeta3 - 1

            sage: Sp3 = BR.create_specialization([5, 7, 11]); Sp3
            Integer Ring localized at (11,)
            sage: Sp3(t)
            102/11
        """
    @cached_method
    def extension_ring(self, names=('a', 'b', 'c', 's')):
        """
        Return the generic extension ring attached to ``self``.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: BR = chbr.CubicHeckeRingOfDefinition()
            sage: BR.extension_ring()
            Multivariate Laurent Polynomial Ring in a, b, c
              over Splitting Algebra of x^2 + x + 1
                with roots [e3, -e3 - 1]
              over Integer Ring
        """
    def markov_trace_version(self):
        """
        Return the extension of the ring of definition needed to treat the
        formal Markov traces.

        This appends an additional variable ``s`` to measure the writhe
        of knots and makes ``u`` and ``v`` invertible.

        EXAMPLES::

            sage: from sage.algebras.hecke_algebras import cubic_hecke_base_ring as chbr
            sage: GBR = chbr.CubicHeckeRingOfDefinition()
            sage: GBR.markov_trace_version()
            Multivariate Polynomial Ring in u, v, w, s
              over Integer Ring localized at (s, w, v, u)
        """
    def specialize_homfly(self):
        """
        Return a map to the two variable Laurent polynomial ring that is
        the parent of the HOMFLY-PT polynomial.

        EXAMPLES::

            sage: from sage.knots.knotinfo import KnotInfo
            sage: CHA2 = algebras.CubicHecke(2)
            sage: K5_1 = KnotInfo.K5_1.link()
            sage: br = CHA2(K5_1.braid())
            sage: mt = br.formal_markov_trace()
            sage: MT = mt.base_ring()
            sage: f = MT.specialize_homfly(); f
            Composite map:
              From: Multivariate Polynomial Ring in u, v, w, s over Integer Ring
                    localized at (s, w, v, u)
              To:   Multivariate Laurent Polynomial Ring in L, M over Integer Ring
              Defn:   Ring morphism:
                      From: Multivariate Polynomial Ring in u, v, w, s
                            over Integer Ring localized at (s, w, v, u)
                      To:   Multivariate Polynomial Ring in L, M
                            over Integer Ring localized at (M - 1, M, L)
                      Defn: u |--> -M + 1
                            v |--> -M + 1
                            w |--> 1
                            s |--> L
                    then
                      Conversion map:
                      From: Multivariate Polynomial Ring in L, M
                            over Integer Ring localized at (M - 1, M, L)
                      To:   Multivariate Laurent Polynomial Ring in L, M
                            over Integer Ring
            sage: sup = mt.support()
            sage: h1 = sum(f(mt.coefficient(b)) * b.regular_homfly_polynomial() for b in sup)
            sage: L, M = f.codomain().gens()
            sage: h2 = K5_1.homfly_polynomial()
            sage: h1*L**(-5) == h2  # since the writhe of K5_1 is 5
            True
        """
    def specialize_kauffman(self):
        """
        Return a map to the two variable Laurent polynomial ring that is
        the parent of the Kauffman polynomial.

        EXAMPLES::

            sage: from sage.knots.knotinfo import KnotInfo
            sage: CHA2 = algebras.CubicHecke(2)
            sage: K5_1 = KnotInfo.K5_1.link()
            sage: br = CHA2(K5_1.braid())
            sage: mt = br.formal_markov_trace()
            sage: MT = mt.base_ring()
            sage: f = MT.specialize_kauffman(); f
            Composite map:
              From: Multivariate Polynomial Ring in u, v, w, s over Integer Ring
                    localized at (s, w, v, u)
              To:   Multivariate Laurent Polynomial Ring in a, z over Integer Ring
              Defn:   Ring morphism:
                      From: Multivariate Polynomial Ring in u, v, w, s
                            over Integer Ring localized at (s, w, v, u)
                      To:   Multivariate Polynomial Ring in a, z
                            over Integer Ring localized at (z, a, a + z, a*z + 1)
                      Defn: u |--> (a*z + 1)/a
                            v |--> (a + z)/a
                            w |--> 1/a
                            s |--> a
                    then
                      Conversion map:
                      From: Multivariate Polynomial Ring in a, z over Integer Ring
                            localized at (z, a, a + z, a*z + 1)
                      To:   Multivariate Laurent Polynomial Ring in a, z
                            over Integer Ring
            sage: sup = mt.support()
            sage: k1 = sum(f(mt.coefficient(b)) * b.regular_kauffman_polynomial() for b in sup)
            sage: a, z = f.codomain().gens()
            sage: k2 = KnotInfo.K5_1.kauffman_polynomial()
            sage: k1*a**(-5) == k2  # since the writhe of K5_1 is 5
            True
        """
    def specialize_links_gould(self):
        """
        Return a map to the two variable Laurent polynomial ring that is
        the parent of the Links-Gould polynomial.

        EXAMPLES::

            sage: from sage.knots.knotinfo import KnotInfo
            sage: CHA2 = algebras.CubicHecke(2)
            sage: K5_1 = KnotInfo.K5_1.link()
            sage: br = CHA2(K5_1.braid())
            sage: mt = br.formal_markov_trace()
            sage: MT = mt.base_ring()
            sage: f = MT.specialize_links_gould(); f
            Composite map:
              From: Multivariate Polynomial Ring in u, v, w, s over Integer Ring
                    localized at (s, w, v, u)
              To:   Multivariate Laurent Polynomial Ring in t0, t1 over Integer Ring
              Defn:   Ring morphism:
                      From: Multivariate Polynomial Ring in u, v, w, s
                            over Integer Ring localized at (s, w, v, u)
                      To:   Multivariate Polynomial Ring in t0, t1 over Integer Ring
                            localized at (t1, t0, t0 + t1 - 1, t0*t1 - t0 - t1)
                      Defn: u |--> t0 + t1 - 1
                            v |--> t0*t1 - t0 - t1
                            w |--> -t0*t1
                            s |--> 1
                    then
                      Conversion map:
                      From: Multivariate Polynomial Ring in t0, t1 over Integer Ring
                            localized at (t1, t0, t0 + t1 - 1, t0*t1 - t0 - t1)
                      To:   Multivariate Laurent Polynomial Ring in t0, t1 over Integer Ring
            sage: sup = mt.support()
            sage: sum(f(mt.coefficient(b)) * b.links_gould_polynomial() for b in sup)
            -t0^4*t1 - t0^3*t1^2 - t0^2*t1^3 - t0*t1^4 + t0^4 + 2*t0^3*t1 + 2*t0^2*t1^2
            + 2*t0*t1^3 + t1^4 - t0^3 - 2*t0^2*t1 - 2*t0*t1^2 - t1^3 + t0^2 + 2*t0*t1
            + t1^2 - t0 - t1 + 1
        """
