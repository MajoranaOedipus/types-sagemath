from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.free_module_element import FreeModuleElement_generic_dense as FreeModuleElement_generic_dense

class OreModuleElement(FreeModuleElement_generic_dense):
    """
    A generic element of a Ore module.
    """
    def is_mutable(self) -> bool:
        """
        Always return ``False`` since elements in Ore modules
        are all immutable.

        EXAMPLES::

            sage: K.<t> = Frac(QQ['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M = S.quotient_module(X^2 + t)

            sage: v, w = M.basis()
            sage: v
            (1, 0)
            sage: v.is_mutable()
            False
            sage: v[1] = 1
            Traceback (most recent call last):
            ...
            ValueError: vectors in Ore modules are immutable
        """
    def __setitem__(self, i, v) -> None:
        """
        Always raise an error since elements in Ore modules are
        all immutable.

        TESTS::

            sage: K.<t> = Frac(QQ['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module(X^2 + t)
            sage: w[1] = 0
            Traceback (most recent call last):
            ...
            ValueError: vectors in Ore modules are immutable
        """
    def __hash__(self):
        """
        Return a hash of this element.

        TESTS::

            sage: K.<t> = Frac(QQ['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module(X^2 + t)
            sage: hash(v)  # random
            -5164621852614943976
            sage: hash(w)  # random
            -1950498447580522560
        """
    def vector(self):
        """
        Return the coordinates vector of this element.

        EXAMPLES::

            sage: K.<t> = Frac(QQ['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module(X^2 + t)
            sage: v.vector()
            (1, 0)

        We underline that this vector is not an element of the
        Ore module; it lives in `K^2`. Compare::

            sage: v.parent()
            Ore module <v, w> over Fraction Field of Univariate Polynomial Ring in t over Rational Field twisted by d/dt
            sage: v.vector().parent()
            Vector space of dimension 2 over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def image(self):
        """
        Return the image of this element by the pseudomorphism
        defining the action of the Ore variable on this Ore module.

        EXAMPLES::

            sage: K.<t> = Frac(QQ['t'])
            sage: S.<X> = OrePolynomialRing(K, K.derivation())
            sage: M.<v,w> = S.quotient_module(X^2 + t)
            sage: v.image()
            w
            sage: w.image()
            -t*v

        TESTS:

        We check that this corresponds to the action of `X`::

            sage: x = M.random_element()
            sage: x.image() == X*x
            True
        """
