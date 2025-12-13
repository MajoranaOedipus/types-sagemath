import sage.structure.parent_base
from typing import Any, ClassVar, overload

class ParentWithGens(sage.structure.parent_base.ParentWithBase):
    """ParentWithGens(base, names=None, normalize=True, category=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base, names=..., normalize=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 84)

                EXAMPLES::

                    sage: from sage.structure.parent_gens import ParentWithGens
                    sage: class MyParent(ParentWithGens):
                    ....:     def ngens(self): return 3
                    sage: P = MyParent(base=QQ, names='a,b,c', normalize=True, category=Groups())
                    sage: P.category()
                    Category of groups
                    sage: P._names
                    ('a', 'b', 'c')
        """
    def gen(self, i=...) -> Any:
        """ParentWithGens.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 108)"""
    def gens(self) -> Any:
        """ParentWithGens.gens(self)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 112)

        Return a tuple whose entries are the generators for this
        object, in order."""
    @overload
    def hom(self, im_gens, codomain=..., base_map=..., category=..., check=...) -> Any:
        """ParentWithGens.hom(self, im_gens, codomain=None, base_map=None, category=None, check=True)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 200)

        Return the unique homomorphism from ``self`` to codomain that
        sends ``self.gens()`` to the entries of ``im_gens``
        and induces the map ``base_map`` on the base ring.

        This raises a :exc:`TypeError` if there is no such homomorphism.

        INPUT:

        - ``im_gens`` -- the images in the codomain of the generators of
          this object under the homomorphism

        - ``codomain`` -- the codomain of the homomorphism

        - ``base_map`` -- a map from the base ring of the domain into something
          that coerces into the codomain

        - ``category`` -- the category of the resulting morphism

        - ``check`` -- whether to verify that the images of generators extend
          to define a map (using only canonical coercions)

        OUTPUT: a homomorphism ``self --> codomain``

        .. NOTE::

           As a shortcut, one can also give an object X instead of
           ``im_gens``, in which case return the (if it exists)
           natural map to X.

        EXAMPLES: Polynomial Ring
        We first illustrate construction of a few homomorphisms
        involving a polynomial ring.

        ::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R.hom([5], QQ)
            sage: f(x^2 - 19)
            6

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = R.hom([5], GF(7))
            Traceback (most recent call last):
            ...
            ValueError: relations do not all (canonically) map to 0
            under map determined by images of generators

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = PolynomialRing(GF(7))
            sage: f = R.hom([3], GF(49, 'a'))
            sage: f
            Ring morphism:
              From: Univariate Polynomial Ring in x over Finite Field of size 7
              To:   Finite Field in a of size 7^2
              Defn: x |--> 3
            sage: f(x + 6)
            2
            sage: f(x^2 + 1)
            3

        EXAMPLES: Natural morphism

        ::

            sage: f = ZZ.hom(GF(5))
            sage: f(7)
            2
            sage: f
            Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5

        There might not be a natural morphism, in which case a
        :exc:`TypeError` exception is raised.

        ::

            sage: QQ.hom(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: natural coercion morphism from Rational Field to Integer Ring not defined

        You can specify a map on the base ring::

            sage: # needs sage.rings.finite_rings
            sage: k = GF(2)
            sage: R.<a> = k[]
            sage: l.<a> = k.extension(a^3 + a^2 + 1)
            sage: R.<b> = l[]
            sage: m.<b> = l.extension(b^2 + b + a)
            sage: n.<z> = GF(2^6)
            sage: m.hom([z^4 + z^3 + 1], base_map=l.hom([z^5 + z^4 + z^2]))
            Ring morphism:
              From: Univariate Quotient Polynomial Ring in b over
                    Finite Field in a of size 2^3 with modulus b^2 + b + a
              To:   Finite Field in z of size 2^6
              Defn: b |--> z^4 + z^3 + 1
                    with map of base ring"""
    @overload
    def hom(self, ZZ) -> Any:
        """ParentWithGens.hom(self, im_gens, codomain=None, base_map=None, category=None, check=True)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 200)

        Return the unique homomorphism from ``self`` to codomain that
        sends ``self.gens()`` to the entries of ``im_gens``
        and induces the map ``base_map`` on the base ring.

        This raises a :exc:`TypeError` if there is no such homomorphism.

        INPUT:

        - ``im_gens`` -- the images in the codomain of the generators of
          this object under the homomorphism

        - ``codomain`` -- the codomain of the homomorphism

        - ``base_map`` -- a map from the base ring of the domain into something
          that coerces into the codomain

        - ``category`` -- the category of the resulting morphism

        - ``check`` -- whether to verify that the images of generators extend
          to define a map (using only canonical coercions)

        OUTPUT: a homomorphism ``self --> codomain``

        .. NOTE::

           As a shortcut, one can also give an object X instead of
           ``im_gens``, in which case return the (if it exists)
           natural map to X.

        EXAMPLES: Polynomial Ring
        We first illustrate construction of a few homomorphisms
        involving a polynomial ring.

        ::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = R.hom([5], QQ)
            sage: f(x^2 - 19)
            6

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = R.hom([5], GF(7))
            Traceback (most recent call last):
            ...
            ValueError: relations do not all (canonically) map to 0
            under map determined by images of generators

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = PolynomialRing(GF(7))
            sage: f = R.hom([3], GF(49, 'a'))
            sage: f
            Ring morphism:
              From: Univariate Polynomial Ring in x over Finite Field of size 7
              To:   Finite Field in a of size 7^2
              Defn: x |--> 3
            sage: f(x + 6)
            2
            sage: f(x^2 + 1)
            3

        EXAMPLES: Natural morphism

        ::

            sage: f = ZZ.hom(GF(5))
            sage: f(7)
            2
            sage: f
            Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5

        There might not be a natural morphism, in which case a
        :exc:`TypeError` exception is raised.

        ::

            sage: QQ.hom(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: natural coercion morphism from Rational Field to Integer Ring not defined

        You can specify a map on the base ring::

            sage: # needs sage.rings.finite_rings
            sage: k = GF(2)
            sage: R.<a> = k[]
            sage: l.<a> = k.extension(a^3 + a^2 + 1)
            sage: R.<b> = l[]
            sage: m.<b> = l.extension(b^2 + b + a)
            sage: n.<z> = GF(2^6)
            sage: m.hom([z^4 + z^3 + 1], base_map=l.hom([z^5 + z^4 + z^2]))
            Ring morphism:
              From: Univariate Quotient Polynomial Ring in b over
                    Finite Field in a of size 2^3 with modulus b^2 + b + a
              To:   Finite Field in z of size 2^6
              Defn: b |--> z^4 + z^3 + 1
                    with map of base ring"""
    def ngens(self) -> Any:
        """ParentWithGens.ngens(self)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 103)"""

class localvars:
    """localvars(obj, names, latex_names=None, normalize=True)

    File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 318)

    Context manager for safely temporarily changing the variables
    names of an object with generators.

    Objects with named generators are globally unique in Sage.
    Sometimes, though, it is very useful to be able to temporarily
    display the generators differently.   The new Python ``with``
    statement and the localvars context manager make this easy and
    safe (and fun!)

    Suppose X is any object with generators.  Write

    ::

        with localvars(X, names[, latex_names] [,normalize=False]):
             some code
             ...

    and the indented code will be run as if the names in X are changed
    to the new names.  If you give normalize=True, then the names are
    assumed to be a tuple of the correct number of strings.

    EXAMPLES::

        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: with localvars(R, 'z,w'):
        ....:     print(x^3 + y^3 - x*y)
        z^3 + w^3 - z*w

    .. NOTE::

       I wrote this because it was needed to print elements of the
       quotient of a ring R by an ideal I using the print function for
       elements of R.  See the code in
       ``quotient_ring_element.pyx``.

    AUTHOR:

    - William Stein (2006-10-31)"""
    def __init__(self, obj, names, latex_names=..., normalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 364)"""
    def __enter__(self) -> Any:
        """localvars.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 373)"""
    def __exit__(self, type, value, traceback) -> Any:
        """localvars.__exit__(self, type, value, traceback)

        File: /build/sagemath/src/sage/src/sage/structure/parent_gens.pyx (starting at line 376)"""
