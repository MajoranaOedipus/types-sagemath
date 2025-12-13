from .misc import precprint as precprint
from .padic_generic import pAdicGeneric as pAdicGeneric
from _typeshed import Incomplete
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.padic_capped_absolute_element import pAdicCoercion_ZZ_CA as pAdicCoercion_ZZ_CA, pAdicConvert_QQ_CA as pAdicConvert_QQ_CA
from sage.rings.padics.padic_capped_relative_element import pAdicCoercion_QQ_CR as pAdicCoercion_QQ_CR, pAdicCoercion_ZZ_CR as pAdicCoercion_ZZ_CR, pAdicConvert_QQ_CR as pAdicConvert_QQ_CR
from sage.rings.padics.padic_fixed_mod_element import pAdicCoercion_ZZ_FM as pAdicCoercion_ZZ_FM, pAdicConvert_QQ_FM as pAdicConvert_QQ_FM
from sage.rings.padics.padic_floating_point_element import pAdicCoercion_QQ_FP as pAdicCoercion_QQ_FP, pAdicCoercion_ZZ_FP as pAdicCoercion_ZZ_FP, pAdicConvert_QQ_FP as pAdicConvert_QQ_FP
from sage.rings.padics.pow_computer import PowComputer as PowComputer
from sage.rings.rational_field import QQ as QQ

class pAdicBaseGeneric(pAdicGeneric):
    prime_pow: Incomplete
    Element: Incomplete
    def __init__(self, p, prec, print_mode, names, element_class, category=None) -> None:
        """
        Initialization.

        TESTS::

            sage: R = Zp(5)  # indirect doctest
        """
    def exact_field(self):
        """
        Return the rational field.

        For compatibility with extensions of `p`-adics.

        EXAMPLES::

            sage: Zp(5).exact_field()
            Rational Field
        """
    def exact_ring(self):
        """
        Return the integer ring.

        EXAMPLES::

            sage: Zp(5).exact_ring()
            Integer Ring
        """
    def is_isomorphic(self, ring):
        """
        Return whether ``self`` and ``ring`` are isomorphic, i.e. whether
        ``ring`` is an implementation of `\\ZZ_p` for the same prime as ``self``.

        INPUT:

        - ``self`` -- a `p`-adic ring

        - ``ring`` -- a ring

        OUTPUT: ``boolean`` -- whether ``ring`` is an implementation of \\ZZ_p`
        for the same prime as ``self``

        EXAMPLES::

            sage: R = Zp(5, 15, print_mode='digits'); S = Zp(5, 44, print_max_terms=4); R.is_isomorphic(S)
            True
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of this extension.  For base
        rings/fields, we consider the generator to be the prime.

        EXAMPLES::

            sage: R = Zp(5); R.gen()
            5 + O(5^21)
        """
    def modulus(self, exact: bool = False):
        """
        Return the polynomial defining this extension.

        For compatibility with extension fields; we define the modulus to be `x-1`.

        INPUT:

        - ``exact`` -- boolean (default: ``False``); whether to return a
          polynomial with integer entries

        EXAMPLES::

            sage: Zp(5).modulus(exact=True)
            x
        """
    def absolute_discriminant(self):
        """
        Return the absolute discriminant of this `p`-adic ring.

        EXAMPLES::

            sage: Zp(5).absolute_discriminant()
            1
        """
    def discriminant(self, K=None):
        """
        Return the discriminant of this `p`-adic ring over ``K``.

        INPUT:

        - ``self`` -- a `p`-adic ring

        - ``K`` -- a sub-ring of ``self`` or ``None`` (default: ``None``)

        OUTPUT:

        integer; the discriminant of this ring over ``K`` (or the absolute
        discriminant if ``K`` is ``None``)

        EXAMPLES::

            sage: Zp(5).discriminant()
            1
        """
    def is_abelian(self):
        """
        Return whether the Galois group is abelian, i.e. ``True``.
        #should this be automorphism group?

        EXAMPLES::

            sage: R = Zp(3, 10,'fixed-mod'); R.is_abelian()
            True
        """
    def is_normal(self):
        """
        Return whether or not this is a normal extension, i.e. ``True``.

        EXAMPLES::

            sage: R = Zp(3, 10,'fixed-mod'); R.is_normal()
            True
        """
    def uniformizer(self):
        """
        Return a uniformizer for this ring.

        EXAMPLES::

            sage: R = Zp(3,5,'fixed-mod', 'series')
            sage: R.uniformizer()
            3
        """
    def uniformizer_pow(self, n):
        """
        Return the `n`-th power of the uniformizer of ``self`` (as
        an element of ``self``).

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.uniformizer_pow(5)
            5^5 + O(5^25)
            sage: R.uniformizer_pow(infinity)
            0
        """
    def has_pth_root(self):
        """
        Return whether or not `\\ZZ_p` has a primitive `p`-th
        root of unity.

        EXAMPLES::

            sage: Zp(2).has_pth_root()
            True
            sage: Zp(17).has_pth_root()
            False
        """
    def has_root_of_unity(self, n):
        """
        Return whether or not `\\ZZ_p` has a primitive `n`-th
        root of unity.

        INPUT:

        - ``self`` -- a `p`-adic ring

        - ``n`` -- integer

        OUTPUT:

        boolean; whether ``self`` has primitive `n`-th root of unity

        EXAMPLES::

            sage: R=Zp(37)
            sage: R.has_root_of_unity(12)
            True
            sage: R.has_root_of_unity(11)
            False
        """
    def zeta(self, n=None):
        """
        Return a generator of the group of roots of unity.

        INPUT:

        - ``self`` -- a `p`-adic ring

        - ``n`` -- integer or ``None`` (default: ``None``)

        OUTPUT:

        ``element``; a generator of the `n`-th roots of unity, or a generator
        of the full group of roots of unity if ``n`` is ``None``

        EXAMPLES::

            sage: R = Zp(37,5)
            sage: R.zeta(12)
            8 + 24*37 + 37^2 + 29*37^3 + 23*37^4 + O(37^5)
        """
    def zeta_order(self):
        """
        Return the order of the group of roots of unity.

        EXAMPLES::

            sage: R = Zp(37); R.zeta_order()
            36
            sage: Zp(2).zeta_order()
            2
        """
    def plot(self, max_points: int = 2500, **args):
        """
        Create a visualization of this `p`-adic ring as a fractal
        similar to a generalization of the Sierpi\\'nski
        triangle.

        The resulting image attempts to capture the
        algebraic and topological characteristics of `\\ZZ_p`.

        INPUT:

        - ``max_points`` -- the maximum number or points to plot,
          which controls the depth of recursion (default: 2500)

        - ``**args`` -- color, size, etc. that are passed to the
          underlying point graphics objects

        REFERENCES:

        - Cuoco, A. ''Visualizing the `p`-adic Integers'', The
          American Mathematical Monthly, Vol. 98, No. 4 (Apr., 1991),
          pp. 355-364

        EXAMPLES::

            sage: Zp(3).plot()                                                          # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: Zp(5).plot(max_points=625)                                            # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: Zp(23).plot(rgbcolor=(1,0,0))                                         # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
