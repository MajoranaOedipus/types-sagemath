from .padic_extension_generic import pAdicExtensionGeneric as pAdicExtensionGeneric
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings.finite_field_constructor import GF as GF

class UnramifiedExtensionGeneric(pAdicExtensionGeneric):
    """
    An unramified extension of `\\QQ_p` or `\\ZZ_p`.
    """
    def __init__(self, poly, prec, print_mode, names, element_class) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``poly`` -- polynomial defining this extension
        - ``prec`` -- the precision cap
        - ``print_mode`` -- dictionary with print options
        - ``names`` -- a 4-tuple, (``variable_name``, ``residue_name``,
          ``unramified_subextension_variable_name``, ``uniformizer_name``)
        - ``element_class`` -- the class for elements of this unramified extension

        EXAMPLES::

            sage: R.<a> = Zq(27)  # indirect doctest                                    # needs sage.libs.ntl
        """
    def absolute_f(self):
        """
        Return the degree of the residue field of this ring/field
        over its prime subfield.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_f()                                                        # needs sage.libs.ntl
            5

            sage: x = polygen(ZZ, 'x')
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_f()                                                        # needs sage.libs.ntl
            1
        """
    def residue_class_field(self):
        """
        Return the residue class field.

        EXAMPLES::

            sage: R.<a> = Zq(125); R.residue_class_field()                              # needs sage.libs.ntl
            Finite Field in a0 of size 5^3
        """
    def residue_ring(self, n):
        """
        Return the quotient of the ring of integers by the `n`-th power of its maximal ideal.

        EXAMPLES::

            sage: R.<a> = Zq(125)                                                       # needs sage.libs.ntl
            sage: R.residue_ring(1)                                                     # needs sage.libs.ntl
            Finite Field in a0 of size 5^3

        The following requires implementing more general Artinian rings::

            sage: R.residue_ring(2)                                                     # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def discriminant(self, K=None):
        """
        Return the discriminant of ``self`` over the subring `K`.

        INPUT:

        - ``K`` -- a subring/subfield (defaults to the base ring)

        EXAMPLES::

            sage: R.<a> = Zq(125)                                                       # needs sage.libs.ntl
            sage: R.discriminant()                                                      # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def is_galois(self, K=None):
        """
        Return ``True`` if this extension is Galois.

        Every unramified extension is Galois.

        INPUT:

        - ``K`` -- a subring/subfield (defaults to the base ring)

        EXAMPLES::

            sage: R.<a> = Zq(125); R.is_galois()                                        # needs sage.libs.ntl
            True
        """
    def gen(self, n: int = 0):
        """
        Return a generator for this unramified extension.

        This is an element that satisfies the polynomial defining this
        extension.  Such an element will reduce to a generator of the
        corresponding residue field extension.

        EXAMPLES::

            sage: R.<a> = Zq(125); R.gen()                                              # needs sage.libs.ntl
            a + O(5^20)
        """
    def uniformizer_pow(self, n):
        """
        Return the `n`-th power of the uniformizer of ``self`` (as an element of ``self``).

        EXAMPLES::

            sage: R.<a> = ZqCR(125)                                                     # needs sage.libs.ntl
            sage: R.uniformizer_pow(5)                                                  # needs sage.libs.ntl
            5^5 + O(5^25)
        """
    def uniformizer(self):
        """
        Return a uniformizer for this extension.

        Since this extension is unramified, a uniformizer for the
        ground ring will also be a uniformizer for this extension.

        EXAMPLES::

            sage: R.<a> = ZqCR(125)                                                     # needs sage.libs.ntl
            sage: R.uniformizer()                                                       # needs sage.libs.ntl
            5 + O(5^21)
        """
    def has_pth_root(self):
        """
        Return whether or not `\\ZZ_p` has a primitive `p`-th root of unity.

        Since adjoining a `p`-th root of unity yields a
        totally ramified extension, ``self`` will contain one if and only
        if the ground ring does.

        INPUT:

        - ``self`` -- a `p`-adic ring

        OUTPUT: boolean; whether ``self`` has primitive `p`-th root of unity

        EXAMPLES::

            sage: R.<a> = Zq(1024); R.has_pth_root()                                    # needs sage.libs.ntl
            True
            sage: R.<a> = Zq(17^5); R.has_pth_root()                                    # needs sage.libs.ntl
            False
        """
    def has_root_of_unity(self, n):
        """
        Return whether or not `\\ZZ_p` has a primitive `n`-th
        root of unity.

        INPUT:

        - ``self`` -- a `p`-adic ring
        - ``n`` -- integer

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(37^8)
            sage: R.has_root_of_unity(144)
            True
            sage: R.has_root_of_unity(89)
            True
            sage: R.has_root_of_unity(11)
            False
        """
