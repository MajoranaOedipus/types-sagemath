from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.homsets import Homsets as Homsets
from sage.categories.modules import Modules as Modules
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing as OrePolynomialRing

class OreModules(Category_over_base_ring):
    """
    Category of Ore modules.
    """
    @staticmethod
    def __classcall_private__(cls, ring, twist):
        """
        Normalize the input and call the init function.

        INPUT:

        - ``ring`` -- a commutative ring, the base ring of
          the Ore modules

        - ``twist`` -- a twisting morphism/derivation or a
          Ore polynomial ring

        TESTS::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat
            Category of Ore modules over Finite Field in a of size 5^3 twisted by a |--> a^5

            sage: S = cat.ore_ring('y')
            sage: cat is OreModules(K, S)
            True
        """
    def __init__(self, ore) -> None:
        """
        Initialize this category.

        TESTS::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)

            sage: TestSuite(cat).run()
        """
    def __reduce__(self):
        """
        Return the arguments which were used to create this instance.

        This method is needed for pickling.

        TESTS::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat2 = loads(dumps(cat))  # indirect doctest
            sage: cat is cat2
            True
        """
    def super_categories(self):
        """
        Return the immediate super categories of this category.

        EXAMPLES::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat.super_categories()
            [Category of vector spaces over Finite Field in a of size 5^3]
        """
    def ore_ring(self, var: str = 'x'):
        """
        Return the underlying Ore polynomial ring.

        INPUT:

        - ``var`` (default; ``x``) -- the variable name

        EXAMPLES::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat.ore_ring()
            Ore Polynomial Ring in x over Finite Field in a of size 5^3 twisted by a |--> a^5

            sage: cat.ore_ring('y')
            Ore Polynomial Ring in y over Finite Field in a of size 5^3 twisted by a |--> a^5
        """
    def twisting_morphism(self):
        """
        Return the underlying twisting morphism.

        EXAMPLES::

            sage: from sage.categories.ore_modules import OreModules
            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat.twisting_morphism()
            Frobenius endomorphism a |--> a^5 on Finite Field in a of size 5^3

        If the twising morphism is the identity, nothing is returned::

            sage: R.<t> = QQ[]
            sage: d = R.derivation()
            sage: cat = OreModules(R, d)
            sage: cat.twisting_morphism()
        """
    def twisting_derivation(self):
        """
        Return the underlying twisting derivation.

        EXAMPLES::

            sage: from sage.categories.ore_modules import OreModules
            sage: R.<t> = QQ[]
            sage: d = R.derivation()
            sage: cat = OreModules(R, d)
            sage: cat.twisting_derivation()
            d/dt

        If the twising derivation is zero, nothing is returned::

            sage: K.<a> = GF(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: cat = OreModules(K, Frob)
            sage: cat.twisting_derivation()
        """
