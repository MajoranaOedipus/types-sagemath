from .padic_extension_generic import pAdicExtensionGeneric as pAdicExtensionGeneric
from sage.rings.infinity import infinity as infinity

class EisensteinExtensionGeneric(pAdicExtensionGeneric):
    def __init__(self, poly, prec, print_mode, names, element_class) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2+7)  # indirect doctest                              # needs sage.libs.ntl sage.rings.padics
        """
    def absolute_e(self):
        """
        Return the absolute ramification index of this ring or field.

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: K.absolute_e()                                                        # needs sage.libs.ntl
            1

            sage: x = polygen(ZZ, 'x')
            sage: L.<pi> = Qp(3).extension(x^2 - 3)                                     # needs sage.libs.ntl
            sage: L.absolute_e()                                                        # needs sage.libs.ntl
            2
        """
    def inertia_subring(self):
        """
        Return the inertia subring.

        Since an Eisenstein extension is totally ramified, this is
        just the ground field.

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.inertia_subring()                                                   # needs sage.libs.ntl
            7-adic Ring with capped relative precision 10
        """
    def residue_class_field(self):
        """
        Return the residue class field.

        INPUT:

        - ``self`` -- a `p`-adic ring

        OUTPUT: the residue field

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.residue_class_field()                                               # needs sage.libs.ntl
            Finite Field of size 7
        """
    def residue_ring(self, n):
        """
        Return the quotient of the ring of integers by the `n`-th power of its maximal ideal.

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: W.<w> = Zp(5).extension(x^2 - 5)                                      # needs sage.libs.ntl
            sage: W.residue_ring(1)                                                     # needs sage.libs.ntl
            Ring of integers modulo 5

        The following requires implementing more general Artinian rings::

            sage: W.residue_ring(2)                                                     # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def gen(self, n: int = 0):
        """
        Return a generator for ``self`` as an extension of its ground ring.

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.gen()                                                               # needs sage.libs.ntl
            t + O(t^21)
        """
    def uniformizer_pow(self, n):
        """
        Return the `n`-th power of the uniformizer of ``self`` (as an
        element of ``self``).

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.uniformizer_pow(5)                                                  # needs sage.libs.ntl
            t^5 + O(t^25)
        """
    def uniformizer(self):
        """
        Return the uniformizer of ``self``, i.e., a generator for the unique
        maximal ideal.

        EXAMPLES::

            sage: A = Zp(7,10)
            sage: S.<x> = A[]                                                           # needs sage.libs.ntl
            sage: B.<t> = A.ext(x^2 + 7)                                                # needs sage.libs.ntl
            sage: B.uniformizer()                                                       # needs sage.libs.ntl
            t + O(t^21)
        """
