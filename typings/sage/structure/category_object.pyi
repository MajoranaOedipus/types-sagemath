import _cython_3_2_1
import sage.structure.sage_object
from sage.categories.category import Category as Category
from sage.cpython.getattr import dir_with_other_class as dir_with_other_class
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.dynamic_class import DynamicMetaclass as DynamicMetaclass
from typing import Any, ClassVar, overload

__pyx_capi__: dict
certify_names: _cython_3_2_1.cython_function_or_method
check_default_category: _cython_3_2_1.cython_function_or_method
normalize_names: _cython_3_2_1.cython_function_or_method

class CategoryObject(sage.structure.sage_object.SageObject):
    """CategoryObject(category=None, base=None)

    File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 77)

    An object in some category."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, category=..., base=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 81)

                Initialize an object in a category.

                INPUT:

                - ``category`` -- the category this object belongs to; if this object
                  belongs to multiple categories, those can be passed as a tuple
                - ``base`` -- if this object has another object that should be
                  considered a base in its primary category, you can include that base
                  here

                EXAMPLES::

                    sage: from sage.structure.category_object import CategoryObject
                    sage: A = CategoryObject()
                    sage: A.category()
                    Category of objects
                    sage: A.base()

                    sage: A = CategoryObject(category = Rings(), base = QQ)
                    sage: A.category()
                    Category of rings
                    sage: A.base()
                    Rational Field

                    sage: A = CategoryObject(category = (Semigroups(), CommutativeAdditiveSemigroups()))
                    sage: A.category()
                    Join of Category of semigroups and Category of commutative additive semigroups

                FIXME: the base and generators attributes have nothing to do with categories, do they?
        """
    @overload
    def Hom(self, codomain, cat=...) -> Any:
        """CategoryObject.Hom(self, codomain, cat=None)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 632)

        Return the homspace ``Hom(self, codomain, cat)`` of all
        homomorphisms from ``self`` to ``codomain`` in the category ``cat``.

        The default category is determined by ``self.category()`` and
        ``codomain.category()``.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.Hom(QQ)
            Set of Homomorphisms
             from Multivariate Polynomial Ring in x, y over Rational Field
               to Rational Field

        Homspaces are defined for very general Sage objects, even elements of familiar rings.

        ::

            sage: n = 5; Hom(n,7)
            Set of Morphisms from 5 to 7 in Category of elements of Integer Ring
            sage: z = 2/3; Hom(z, 8/1)
            Set of Morphisms from 2/3 to 8 in Category of elements of Rational Field

        This example illustrates the optional third argument::

            sage: QQ.Hom(ZZ, Sets())
            Set of Morphisms from Rational Field to Integer Ring in Category of sets"""
    @overload
    def Hom(self, codomain, cat) -> Any:
        """CategoryObject.Hom(self, codomain, cat=None)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 632)

        Return the homspace ``Hom(self, codomain, cat)`` of all
        homomorphisms from ``self`` to ``codomain`` in the category ``cat``.

        The default category is determined by ``self.category()`` and
        ``codomain.category()``.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.Hom(QQ)
            Set of Homomorphisms
             from Multivariate Polynomial Ring in x, y over Rational Field
               to Rational Field

        Homspaces are defined for very general Sage objects, even elements of familiar rings.

        ::

            sage: n = 5; Hom(n,7)
            Set of Morphisms from 5 to 7 in Category of elements of Integer Ring
            sage: z = 2/3; Hom(z, 8/1)
            Set of Morphisms from 2/3 to 8 in Category of elements of Rational Field

        This example illustrates the optional third argument::

            sage: QQ.Hom(ZZ, Sets())
            Set of Morphisms from Rational Field to Integer Ring in Category of sets"""
    @overload
    def Hom(self, QQ) -> Any:
        """CategoryObject.Hom(self, codomain, cat=None)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 632)

        Return the homspace ``Hom(self, codomain, cat)`` of all
        homomorphisms from ``self`` to ``codomain`` in the category ``cat``.

        The default category is determined by ``self.category()`` and
        ``codomain.category()``.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.Hom(QQ)
            Set of Homomorphisms
             from Multivariate Polynomial Ring in x, y over Rational Field
               to Rational Field

        Homspaces are defined for very general Sage objects, even elements of familiar rings.

        ::

            sage: n = 5; Hom(n,7)
            Set of Morphisms from 5 to 7 in Category of elements of Integer Ring
            sage: z = 2/3; Hom(z, 8/1)
            Set of Morphisms from 2/3 to 8 in Category of elements of Rational Field

        This example illustrates the optional third argument::

            sage: QQ.Hom(ZZ, Sets())
            Set of Morphisms from Rational Field to Integer Ring in Category of sets"""
    @overload
    def Hom(self, z) -> Any:
        """CategoryObject.Hom(self, codomain, cat=None)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 632)

        Return the homspace ``Hom(self, codomain, cat)`` of all
        homomorphisms from ``self`` to ``codomain`` in the category ``cat``.

        The default category is determined by ``self.category()`` and
        ``codomain.category()``.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.Hom(QQ)
            Set of Homomorphisms
             from Multivariate Polynomial Ring in x, y over Rational Field
               to Rational Field

        Homspaces are defined for very general Sage objects, even elements of familiar rings.

        ::

            sage: n = 5; Hom(n,7)
            Set of Morphisms from 5 to 7 in Category of elements of Integer Ring
            sage: z = 2/3; Hom(z, 8/1)
            Set of Morphisms from 2/3 to 8 in Category of elements of Rational Field

        This example illustrates the optional third argument::

            sage: QQ.Hom(ZZ, Sets())
            Set of Morphisms from Rational Field to Integer Ring in Category of sets"""
    def base(self) -> Any:
        """CategoryObject.base(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 626)"""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def base_ring(self) -> Any:
        """CategoryObject.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 568)

        Return the base ring of ``self``.

        INPUT:

        - ``self`` -- an object over a base ring; typically a module

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: Module(ZZ).base_ring()
            Integer Ring

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F.base_ring()                                                         # needs sage.modules
            Integer Ring
            sage: F.__class__.base_ring                                                 # needs sage.modules
            <cyfunction CategoryObject.base_ring at ...>

        Note that the coordinates of the elements of a module can lie
        in a bigger ring, the ``coordinate_ring``::

            sage: # needs sage.modules
            sage: M = (ZZ^2) * (1/2)
            sage: v = M([1/2, 0])
            sage: v.base_ring()
            Integer Ring
            sage: parent(v[0])
            Rational Field
            sage: v.coordinate_ring()
            Rational Field

        More examples::

            sage: F = FreeAlgebra(QQ, 'x')                                              # needs sage.combinat sage.modules
            sage: F.base_ring()                                                         # needs sage.combinat sage.modules
            Rational Field
            sage: F.__class__.base_ring                                                 # needs sage.combinat sage.modules
            <cyfunction CategoryObject.base_ring at ...>

            sage: # needs sage.modules
            sage: E = CombinatorialFreeModule(ZZ, [1,2,3])
            sage: F = CombinatorialFreeModule(ZZ, [2,3,4])
            sage: H = Hom(E, F)
            sage: H.base_ring()
            Integer Ring
            sage: H.__class__.base_ring
            <cyfunction CategoryObject.base_ring at ...>

        .. TODO::

            Move this method elsewhere (typically in the Modules
            category) so as not to pollute the namespace of all
            category objects."""
    @overload
    def categories(self) -> Any:
        """CategoryObject.categories(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 209)

        Return the categories of ``self``.

        EXAMPLES::

            sage: ZZ.categories()
            [Join of Category of Dedekind domains
                 and Category of euclidean domains
                 and Category of noetherian rings
                 and Category of infinite enumerated sets
                 and Category of metric spaces,
             Category of Dedekind domains,
             Category of euclidean domains,
             Category of principal ideal domains,
             Category of unique factorization domains,
             Category of gcd domains,
             Category of integral domains,
             Category of domains, ...
             Category of commutative rings, ...
             Category of monoids, ...,
             Category of commutative additive groups, ...,
             Category of sets, ...,
             Category of objects]"""
    @overload
    def categories(self) -> Any:
        """CategoryObject.categories(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 209)

        Return the categories of ``self``.

        EXAMPLES::

            sage: ZZ.categories()
            [Join of Category of Dedekind domains
                 and Category of euclidean domains
                 and Category of noetherian rings
                 and Category of infinite enumerated sets
                 and Category of metric spaces,
             Category of Dedekind domains,
             Category of euclidean domains,
             Category of principal ideal domains,
             Category of unique factorization domains,
             Category of gcd domains,
             Category of integral domains,
             Category of domains, ...
             Category of commutative rings, ...
             Category of monoids, ...,
             Category of commutative additive groups, ...,
             Category of sets, ...,
             Category of objects]"""
    def category(self) -> Any:
        """CategoryObject.category(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 202)"""
    @overload
    def gens_dict(self, copy=...) -> Any:
        """CategoryObject.gens_dict(self, *, copy=True)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 271)

        Return a dictionary whose entries are ``{name:variable,...}``,
        where ``name`` stands for the variable names of this
        object (as strings) and ``variable`` stands for the
        corresponding defining generators (as elements of this object).

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()                                 # needs sage.rings.polynomial.pbori
            sage: B.gens_dict()                                                         # needs sage.rings.polynomial.pbori
            {'a': a, 'b': b, 'c': c, 'd': d}

        TESTS::

            sage: B.<a,b,c,d> = PolynomialRing(QQ)
            sage: B.gens_dict(copy=False) is B.gens_dict(copy=False)
            True
            sage: B.gens_dict(copy=False) is B.gens_dict()
            False"""
    @overload
    def gens_dict(self) -> Any:
        """CategoryObject.gens_dict(self, *, copy=True)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 271)

        Return a dictionary whose entries are ``{name:variable,...}``,
        where ``name`` stands for the variable names of this
        object (as strings) and ``variable`` stands for the
        corresponding defining generators (as elements of this object).

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()                                 # needs sage.rings.polynomial.pbori
            sage: B.gens_dict()                                                         # needs sage.rings.polynomial.pbori
            {'a': a, 'b': b, 'c': c, 'd': d}

        TESTS::

            sage: B.<a,b,c,d> = PolynomialRing(QQ)
            sage: B.gens_dict(copy=False) is B.gens_dict(copy=False)
            True
            sage: B.gens_dict(copy=False) is B.gens_dict()
            False"""
    @overload
    def gens_dict_recursive(self) -> Any:
        """CategoryObject.gens_dict_recursive(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 297)

        Return the dictionary of generators of ``self`` and its base rings.

        OUTPUT:

        - a dictionary with string names of generators as keys and
          generators of ``self`` and its base rings as values.

        EXAMPLES::

            sage: R = QQ['x,y']['z,w']
            sage: sorted(R.gens_dict_recursive().items())
            [('w', w), ('x', x), ('y', y), ('z', z)]"""
    @overload
    def gens_dict_recursive(self) -> Any:
        """CategoryObject.gens_dict_recursive(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 297)

        Return the dictionary of generators of ``self`` and its base rings.

        OUTPUT:

        - a dictionary with string names of generators as keys and
          generators of ``self`` and its base rings as values.

        EXAMPLES::

            sage: R = QQ['x,y']['z,w']
            sage: sorted(R.gens_dict_recursive().items())
            [('w', w), ('x', x), ('y', y), ('z', z)]"""
    @overload
    def inject_variables(self, scope=..., verbose=...) -> Any:
        """CategoryObject.inject_variables(self, scope=None, verbose=True)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 538)

        Inject the generators of ``self`` with their names into the
        namespace of the Python code from which this function is
        called.

        Thus, e.g., if the generators of ``self`` are labeled
        'a', 'b', and 'c', then after calling this method the
        variables a, b, and c in the current scope will be set
        equal to the generators of ``self``.

        NOTE: If Foo is a constructor for a Sage object with generators, and
        Foo is defined in Cython, then it would typically call
        ``inject_variables()`` on the object it creates.  E.g.,
        ``PolynomialRing(QQ, 'y')`` does this so that the variable y is the
        generator of the polynomial ring."""
    @overload
    def inject_variables(self) -> Any:
        """CategoryObject.inject_variables(self, scope=None, verbose=True)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 538)

        Inject the generators of ``self`` with their names into the
        namespace of the Python code from which this function is
        called.

        Thus, e.g., if the generators of ``self`` are labeled
        'a', 'b', and 'c', then after calling this method the
        variables a, b, and c in the current scope will be set
        equal to the generators of ``self``.

        NOTE: If Foo is a constructor for a Sage object with generators, and
        Foo is defined in Cython, then it would typically call
        ``inject_variables()`` on the object it creates.  E.g.,
        ``PolynomialRing(QQ, 'y')`` does this so that the variable y is the
        generator of the polynomial ring."""
    def latex_name(self) -> Any:
        """CategoryObject.latex_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 700)"""
    @overload
    def latex_variable_names(self) -> Any:
        """CategoryObject.latex_variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 669)

        Return the list of variable names suitable for latex output.

        All ``_SOMETHING`` substrings are replaced by ``_{SOMETHING}``
        recursively so that subscripts of subscripts work.

        EXAMPLES::

            sage: R, x = PolynomialRing(QQ, 'x', 12).objgens()
            sage: x
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)
            sage: R.latex_variable_names ()
            ['x_{0}', 'x_{1}', 'x_{2}', 'x_{3}', 'x_{4}', 'x_{5}', 'x_{6}',
             'x_{7}', 'x_{8}', 'x_{9}', 'x_{10}', 'x_{11}']
            sage: f = x[0]^3 + 15/3 * x[1]^10
            sage: print(latex(f))
            5 x_{1}^{10} + x_{0}^{3}"""
    @overload
    def latex_variable_names(self) -> Any:
        """CategoryObject.latex_variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 669)

        Return the list of variable names suitable for latex output.

        All ``_SOMETHING`` substrings are replaced by ``_{SOMETHING}``
        recursively so that subscripts of subscripts work.

        EXAMPLES::

            sage: R, x = PolynomialRing(QQ, 'x', 12).objgens()
            sage: x
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)
            sage: R.latex_variable_names ()
            ['x_{0}', 'x_{1}', 'x_{2}', 'x_{3}', 'x_{4}', 'x_{5}', 'x_{6}',
             'x_{7}', 'x_{8}', 'x_{9}', 'x_{10}', 'x_{11}']
            sage: f = x[0]^3 + 15/3 * x[1]^10
            sage: print(latex(f))
            5 x_{1}^{10} + x_{0}^{3}"""
    @overload
    def objgen(self) -> Any:
        """CategoryObject.objgen(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 332)

        Return the tuple ``(self, self.gen())``.

        EXAMPLES::

            sage: R, x = PolynomialRing(QQ,'x').objgen()
            sage: R
            Univariate Polynomial Ring in x over Rational Field
            sage: x
            x"""
    @overload
    def objgen(self) -> Any:
        """CategoryObject.objgen(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 332)

        Return the tuple ``(self, self.gen())``.

        EXAMPLES::

            sage: R, x = PolynomialRing(QQ,'x').objgen()
            sage: R
            Univariate Polynomial Ring in x over Rational Field
            sage: x
            x"""
    @overload
    def objgens(self) -> Any:
        """CategoryObject.objgens(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 319)

        Return the tuple ``(self, self.gens())``.

        EXAMPLES::

            sage: R = PolynomialRing(QQ, 3, 'x'); R
            Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
            sage: R.objgens()
            (Multivariate Polynomial Ring in x0, x1, x2 over Rational Field, (x0, x1, x2))"""
    @overload
    def objgens(self) -> Any:
        """CategoryObject.objgens(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 319)

        Return the tuple ``(self, self.gens())``.

        EXAMPLES::

            sage: R = PolynomialRing(QQ, 3, 'x'); R
            Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
            sage: R.objgens()
            (Multivariate Polynomial Ring in x0, x1, x2 over Rational Field, (x0, x1, x2))"""
    @overload
    def variable_name(self) -> Any:
        """CategoryObject.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 488)

        Return the first variable name.

        OUTPUT: string

        EXAMPLES::

            sage: R.<z,y,a42> = ZZ[]
            sage: R.variable_name()
            'z'
            sage: R.<x> = InfinitePolynomialRing(ZZ)
            sage: R.variable_name()
            'x'"""
    @overload
    def variable_name(self) -> Any:
        """CategoryObject.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 488)

        Return the first variable name.

        OUTPUT: string

        EXAMPLES::

            sage: R.<z,y,a42> = ZZ[]
            sage: R.variable_name()
            'z'
            sage: R.<x> = InfinitePolynomialRing(ZZ)
            sage: R.variable_name()
            'x'"""
    @overload
    def variable_name(self) -> Any:
        """CategoryObject.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 488)

        Return the first variable name.

        OUTPUT: string

        EXAMPLES::

            sage: R.<z,y,a42> = ZZ[]
            sage: R.variable_name()
            'z'
            sage: R.<x> = InfinitePolynomialRing(ZZ)
            sage: R.variable_name()
            'x'"""
    @overload
    def variable_names(self) -> Any:
        """CategoryObject.variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 463)

        Return the list of variable names corresponding to the generators.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: R.<z,y,a42> = QQ[]
            sage: R.variable_names()
            ('z', 'y', 'a42')
            sage: S = R.quotient_ring(z+y)
            sage: S.variable_names()
            ('zbar', 'ybar', 'a42bar')

        ::

            sage: T.<x> = InfinitePolynomialRing(ZZ)
            sage: T.variable_names()
            ('x',)"""
    @overload
    def variable_names(self) -> Any:
        """CategoryObject.variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 463)

        Return the list of variable names corresponding to the generators.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: R.<z,y,a42> = QQ[]
            sage: R.variable_names()
            ('z', 'y', 'a42')
            sage: S = R.quotient_ring(z+y)
            sage: S.variable_names()
            ('zbar', 'ybar', 'a42bar')

        ::

            sage: T.<x> = InfinitePolynomialRing(ZZ)
            sage: T.variable_names()
            ('x',)"""
    @overload
    def variable_names(self) -> Any:
        """CategoryObject.variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 463)

        Return the list of variable names corresponding to the generators.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: R.<z,y,a42> = QQ[]
            sage: R.variable_names()
            ('z', 'y', 'a42')
            sage: S = R.quotient_ring(z+y)
            sage: S.variable_names()
            ('zbar', 'ybar', 'a42bar')

        ::

            sage: T.<x> = InfinitePolynomialRing(ZZ)
            sage: T.variable_names()
            ('x',)"""
    @overload
    def variable_names(self) -> Any:
        """CategoryObject.variable_names(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 463)

        Return the list of variable names corresponding to the generators.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: R.<z,y,a42> = QQ[]
            sage: R.variable_names()
            ('z', 'y', 'a42')
            sage: S = R.quotient_ring(z+y)
            sage: S.variable_names()
            ('zbar', 'ybar', 'a42bar')

        ::

            sage: T.<x> = InfinitePolynomialRing(ZZ)
            sage: T.variable_names()
            ('x',)"""
    def __dir__(self) -> Any:
        '''CategoryObject.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 870)

        Let cat be the category of ``self``. This method emulates
        ``self`` being an instance of both ``CategoryObject`` and
        ``cat.parent_class``, in that order, for attribute directory.

        EXAMPLES::

            sage: for s in dir(ZZ):
            ....:     if s[:6] == "_test_": print(s)
            _test_additive_associativity
            _test_an_element
            _test_associativity
            _test_cardinality
            _test_category
            _test_characteristic
            _test_construction
            _test_distributivity
            _test_divides
            _test_elements
            _test_elements_eq_reflexive
            _test_elements_eq_symmetric
            _test_elements_eq_transitive
            _test_elements_neq
            _test_enumerated_set_contains
            _test_enumerated_set_iter_cardinality
            _test_enumerated_set_iter_list
            _test_eq
            _test_euclidean_degree
            _test_fraction_field
            _test_gcd_vs_xgcd
            _test_metric_function
            _test_new
            _test_not_implemented_methods
            _test_one
            _test_pickling
            _test_prod
            _test_quo_rem
            _test_some_elements
            _test_zero
            _test_zero_divisors
            sage: F = GF(9,\'a\')                                                         # needs sage.rings.finite_rings
            sage: dir(F)                                                                # needs sage.rings.finite_rings
            [..., \'__class__\', ..., \'_test_pickling\', ..., \'extension\', ...]'''
    def __hash__(self) -> Any:
        '''CategoryObject.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/category_object.pyx (starting at line 761)

        A default hash based on the string representation of ``self``.

        It is cached to remain consistent throughout a session, even
        if the representation changes.

        EXAMPLES::

            sage: bla = PolynomialRing(ZZ,"x")
            sage: h1 = hash(bla)
            sage: h1  # random
            -5279516879544852222
            sage: bla.rename(\'toto\')
            sage: h2 = hash(bla)
            sage: h2  # random
            -5279516879544852222
            sage: h1 == h2
            True'''
