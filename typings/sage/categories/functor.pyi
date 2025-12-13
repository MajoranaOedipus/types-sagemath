import _cython_3_2_1
import sage.categories.category as category
import sage.structure.sage_object
from typing import Any, overload

ForgetfulFunctor: _cython_3_2_1.cython_function_or_method
IdentityFunctor: _cython_3_2_1.cython_function_or_method
is_Functor: _cython_3_2_1.cython_function_or_method

class ForgetfulFunctor_generic(Functor):
    """File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 451)

        The forgetful functor, i.e., embedding of a subcategory.

        NOTE:

        Forgetful functors should be created using :func:`ForgetfulFunctor`,
        since the init method of this class does not check whether the
        domain is a subcategory of the codomain.

        EXAMPLES::

            sage: F = ForgetfulFunctor(FiniteFields(), Fields())  # indirect doctest
            sage: F
            The forgetful functor
             from Category of finite enumerated fields
               to Category of fields
            sage: F(GF(3))
            Finite Field of size 3
    """
    def __eq__(self, other) -> Any:
        """ForgetfulFunctor_generic.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 493)

        NOTE:

        It is tested whether the second argument belongs to the class
        of forgetful functors and has the same domain and codomain as
        ``self``. If the second argument is a functor of a different class
        but happens to be a forgetful functor, both arguments will
        still be considered as being *different*.

        TESTS::

            sage: F1 = ForgetfulFunctor(FiniteFields(), Fields())

        This is to test against a bug occurring in a previous version
        (see :issue:`8800`)::

            sage: F1 == QQ #indirect doctest
            False

        We now compare with the fraction field functor, that has a
        different domain::

            sage: F2 = QQ.construction()[0]
            sage: F1 == F2 #indirect doctest
            False"""
    def __ne__(self, other) -> Any:
        """ForgetfulFunctor_generic.__ne__(self, other)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 526)

        Return whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F1 = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F1 != F1
            False
            sage: F1 != QQ
            True"""
    def __reduce__(self) -> Any:
        """ForgetfulFunctor_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 471)

        EXAMPLES::

            sage: F = ForgetfulFunctor(Groups(), Sets())
            sage: loads(F.dumps()) == F
            True"""

class Functor(sage.structure.sage_object.SageObject):
    """Functor(domain, codomain)

    File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 63)

    A class for functors between two categories.

    NOTE:

    - In the first place, a functor is given by its domain and codomain,
      which are both categories.
    - When defining a sub-class, the user should not implement a call method.
      Instead, one should implement three methods, which are composed in the
      default call method:

      - ``_coerce_into_domain(self, x)`` -- return an object of ``self``'s
        domain, corresponding to ``x``, or raise a :exc:`TypeError`.
        - Default: Raise :exc:`TypeError` if ``x`` is not in ``self``'s domain.

      - ``_apply_functor(self, x)`` -- apply ``self`` to an object ``x`` of
        ``self``'s domain.
        - Default: Conversion into ``self``'s codomain.

      - ``_apply_functor_to_morphism(self, f)`` -- apply ``self`` to a morphism
        ``f`` in ``self``'s domain.
        - Default: Return ``self(f.domain()).hom(f,self(f.codomain()))``.

    EXAMPLES::

        sage: rings  = Rings()
        sage: abgrps = CommutativeAdditiveGroups()
        sage: F = ForgetfulFunctor(rings, abgrps)
        sage: F.domain()
        Category of rings
        sage: F.codomain()
        Category of commutative additive groups
        sage: from sage.categories.functor import Functor
        sage: isinstance(F, Functor)
        True
        sage: I = IdentityFunctor(abgrps)
        sage: I
        The identity functor on Category of commutative additive groups
        sage: I.domain()
        Category of commutative additive groups
        sage: isinstance(I, Functor)
        True

    Note that by default, an instance of the class Functor is coercion
    from the domain into the codomain. The above subclasses overloaded
    this behaviour. Here we illustrate the default::

        sage: from sage.categories.functor import Functor
        sage: F = Functor(Rings(), Fields())
        sage: F
        Functor from Category of rings to Category of fields
        sage: F(ZZ)
        Rational Field
        sage: F(GF(2))
        Finite Field of size 2

    Functors are not only about the objects of a category, but also about
    their morphisms. We illustrate it, again, with the coercion functor
    from rings to fields.

    ::

        sage: R1.<x> = ZZ[]
        sage: R2.<a,b> = QQ[]
        sage: f = R1.hom([a + b], R2)
        sage: f
        Ring morphism:
          From: Univariate Polynomial Ring in x over Integer Ring
          To:   Multivariate Polynomial Ring in a, b over Rational Field
          Defn: x |--> a + b
        sage: F(f)
        Ring morphism:
          From: Fraction Field of Univariate Polynomial Ring in x over Integer Ring
          To:   Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
          Defn: x |--> a + b
        sage: F(f)(1/x)
        1/(a + b)

    We can also apply a polynomial ring construction functor to our homomorphism. The
    result is a homomorphism that is defined on the base ring::

        sage: F = QQ['t'].construction()[0]
        sage: F
        Poly[t]
        sage: F(f)
        Ring morphism:
          From: Univariate Polynomial Ring in t
                 over Univariate Polynomial Ring in x over Integer Ring
          To:   Univariate Polynomial Ring in t
                 over Multivariate Polynomial Ring in a, b over Rational Field
          Defn: Induced from base ring by
                Ring morphism:
                  From: Univariate Polynomial Ring in x over Integer Ring
                  To:   Multivariate Polynomial Ring in a, b over Rational Field
                  Defn: x |--> a + b
        sage: p = R1['t']('(-x^2 + x)*t^2 + (x^2 - x)*t - 4*x^2 - x + 1')
        sage: F(f)(p)
        (-a^2 - 2*a*b - b^2 + a + b)*t^2 + (a^2 + 2*a*b + b^2 - a - b)*t
        - 4*a^2 - 8*a*b - 4*b^2 - a - b + 1"""
    def __init__(self, domain, codomain) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 164)

                TESTS::

                    sage: from sage.categories.functor import Functor
                    sage: F = Functor(Rings(), Fields())
                    sage: F
                    Functor from Category of rings to Category of fields
                    sage: F(ZZ)
                    Rational Field
                    sage: F(GF(2))
                    Finite Field of size 2
        """
    @overload
    def codomain(self) -> Any:
        """Functor.codomain(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 401)

        The codomain of ``self``.

        EXAMPLES::

            sage: F = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F.codomain()
            Category of fields"""
    @overload
    def codomain(self) -> Any:
        """Functor.codomain(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 401)

        The codomain of ``self``.

        EXAMPLES::

            sage: F = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F.codomain()
            Category of fields"""
    @overload
    def domain(self) -> Any:
        """Functor.domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 389)

        The domain of ``self``.

        EXAMPLES::

            sage: F = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F.domain()
            Category of finite enumerated fields"""
    @overload
    def domain(self) -> Any:
        """Functor.domain(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 389)

        The domain of ``self``.

        EXAMPLES::

            sage: F = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F.domain()
            Category of finite enumerated fields"""
    def __call__(self, x) -> Any:
        """Functor.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 320)

        NOTE:

        Implement _coerce_into_domain, _apply_functor and
        _apply_functor_to_morphism when subclassing Functor.

        TESTS:

        The default::

            sage: from sage.categories.functor import Functor
            sage: F = Functor(Rings(),Fields())
            sage: F
            Functor from Category of rings to Category of fields
            sage: F(ZZ)
            Rational Field
            sage: F(GF(2))
            Finite Field of size 2

        Two subclasses::

            sage: F1 = ForgetfulFunctor(FiniteFields(), Fields())
            sage: F1(GF(5))  # indirect doctest
            Finite Field of size 5
            sage: F1(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: x (=Integer Ring) is not in Category of finite enumerated fields
            sage: F2 = IdentityFunctor(Fields())
            sage: F2(RR) is RR #indirect doctest
            True
            sage: F2(ZZ['x','y'])
            Traceback (most recent call last):
            ...
            TypeError: x (=Multivariate Polynomial Ring in x, y over Integer Ring)
            is not in Category of fields

        The last example shows that it is tested whether the result of
        applying the functor lies in the functor's codomain. Note that
        the matrix functor used to be defined similar to this example,
        which was fixed in :issue:`8807`::

            sage: class IllFunctor(Functor):
            ....:   def __init__(self, m, n):
            ....:       self._m = m
            ....:       self._n = n
            ....:       Functor.__init__(self, Rings(), Rings())
            ....:   def _apply_functor(self, R):
            ....:       return MatrixSpace(R, self._m, self._n)
            sage: F = IllFunctor(2, 2)
            sage: F(QQ)                                                                 # needs sage.modules
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: F = IllFunctor(2, 3)
            sage: F(QQ)                                                                 # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: Functor from Category of rings to Category of rings
            is ill-defined, since it sends x (=Rational Field) to something
            that is not in Category of rings."""
    def __hash__(self) -> Any:
        """Functor.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 184)

        TESTS::

            sage: from sage.categories.functor import Functor
            sage: F = Functor(Rings(), Fields())
            sage: hash(F)  # random
            42"""
    def __reduce__(self) -> Any:
        """Functor.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 195)

        Generic pickling of functors.

        AUTHOR:

        - Simon King (2010-12):  :issue:`10460`

        TESTS::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F = CompositeConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0],QQ.construction()[0],ZZ['y'].construction()[0])
            sage: F == loads(dumps(F))
            True
            sage: F.codomain()
            Category of rings"""

class IdentityFunctor_generic(ForgetfulFunctor_generic):
    """File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 541)

        Generic identity functor on any category.

        NOTE:

        This usually is created using :func:`IdentityFunctor`.

        EXAMPLES::

            sage: F = IdentityFunctor(Fields()) #indirect doctest
            sage: F
            The identity functor on Category of fields
            sage: F(RR) is RR
            True
            sage: F(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: x (=Integer Ring) is not in Category of fields

        TESTS::

            sage: R = IdentityFunctor(Rings())
            sage: P, _ = QQ['t'].construction()
            sage: R == P
            False
            sage: P == R
            False
            sage: R == QQ
            False
    """
    def __init__(self, C) -> Any:
        """IdentityFunctor_generic.__init__(self, C)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 572)

        TESTS::

            sage: from sage.categories.functor import IdentityFunctor_generic
            sage: F = IdentityFunctor_generic(Groups())
            sage: F == IdentityFunctor(Groups())
            True
            sage: F
            The identity functor on Category of groups"""
    def __reduce__(self) -> Any:
        """IdentityFunctor_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/categories/functor.pyx (starting at line 585)

        EXAMPLES::

            sage: F = IdentityFunctor(Groups())
            sage: loads(F.dumps()) == F
            True"""
