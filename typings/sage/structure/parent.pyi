r"""
Base class for parent objects

CLASS HIERARCHY::

    SageObject
        CategoryObject
            Parent

A simple example of registering coercions::

    sage: class A_class(Parent):
    ....:   def __init__(self, name):
    ....:       Parent.__init__(self)
    ....:       self._populate_coercion_lists_()
    ....:       self.rename(name)
    ....:
    ....:   def category(self):
    ....:       return Sets()
    ....:
    ....:   def _element_constructor_(self, i):
    ....:       assert(isinstance(i, (int, Integer)))
    ....:       return ElementWrapper(self, i)
    sage: A = A_class("A")
    sage: B = A_class("B")
    sage: C = A_class("C")

    sage: def f(a):
    ....:   return B(a.value+1)
    sage: class MyMorphism(Morphism):
    ....:   def __init__(self, domain, codomain):
    ....:       Morphism.__init__(self, Hom(domain, codomain))
    ....:
    ....:   def _call_(self, x):
    ....:       return self.codomain()(x.value)
    sage: f = MyMorphism(A,B)
    sage: f
        Generic morphism:
          From: A
          To:   B
    sage: B.register_coercion(f)
    sage: C.register_coercion(MyMorphism(B,C))
    sage: A(A(1)) == A(1)
    True
    sage: B(A(1)) == B(1)
    True
    sage: C(A(1)) == C(1)
    True

    sage: A(B(1))
    Traceback (most recent call last):
    ...
    AssertionError

When implementing an element of a ring, one would typically provide the
element class with ``_rmul_`` and/or ``_lmul_`` methods for the action of a
base ring, and with ``_mul_`` for the ring multiplication. However, prior to
:issue:`14249`, it would have been necessary to additionally define a method
``_an_element_()`` for the parent. But now, the following example works::

    sage: from sage.structure.element import RingElement
    sage: class MyElement(RingElement):
    ....:      def __init__(self, parent, x, y):
    ....:          RingElement.__init__(self, parent)
    ....:      def _mul_(self, other):
    ....:          return self
    ....:      def _rmul_(self, other):
    ....:          return self
    ....:      def _lmul_(self, other):
    ....:          return self
    sage: class MyParent(Parent):
    ....:      Element = MyElement

Now, we define ::

    sage: P = MyParent(base=ZZ, category=Rings())
    sage: a = P(1,2)
    sage: a*a is a
    True
    sage: a*2 is a
    True
    sage: 2*a is a
    True

TESTS:

This came up in some subtle bug once::

    sage: gp(2) + gap(3)                                                                # needs sage.libs.gap sage.libs.pari
    5
"""

from typing import Any, Self, TypeGuard, overload
from collections.abc import Sequence as PySequence, Callable
import operator
from sage.categories.homset import Homset
from sage.structure.element import Element
from sage.categories.map import Map
from sage.categories.action import Action

type _BinOp = Callable[[Any, Any], Any]

from sage.categories.category import Category as Category
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.category_object import CategoryObject as CategoryObject
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from sage.structure.dynamic_class import dynamic_class as dynamic_class
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

Sets_parent_class: type[Sets.parent_class] = Sets().parent_class

def is_Parent(x) -> TypeGuard[Parent]:
    """
    Return ``True`` if x is a parent object, i.e., derives from
    sage.structure.parent.Parent and ``False`` otherwise.

    EXAMPLES::

        sage: from sage.structure.parent import is_Parent
        sage: is_Parent(2/3)
        doctest:warning...
        DeprecationWarning: the function is_Parent is deprecated;
        use 'isinstance(..., Parent)' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        False
        sage: is_Parent(ZZ)
        True
        sage: is_Parent(Primes())
        True
    """

class Parent(CategoryObject):
    def __init__(self, base=..., category=..., names=..., normalize=..., facade=...):
        """
                Base class for all parents.

                Parents are the Sage/mathematical analogues of container
                objects in computer science.

                INPUT:

                - ``base`` -- an algebraic structure considered to be the "base" of
                  this parent (e.g. the base field for a vector space)

                - ``category`` -- a category or list/tuple of categories. The category
                  in which this parent lies (or list or tuple thereof). Since
                  categories support more general super-categories, this should be the
                  most specific category possible. If category is a list or tuple, a
                  ``JoinCategory`` is created out of them. If category is not
                  specified, the category will be guessed (see
                  :class:`~sage.structure.category_object.CategoryObject`), but will
                  not be used to inherit parent\'s or element\'s code from this category.

                - ``names`` -- names of generators

                - ``normalize`` -- whether to standardize the names (remove
                  punctuation, etc.)

                - ``facade`` -- a parent, or tuple thereof, or ``True``

                If ``facade`` is specified, then ``Sets().Facade()`` is added
                to the categories of the parent. Furthermore, if ``facade`` is
                not ``True``, the internal attribute ``_facade_for`` is set
                accordingly for use by
                :meth:`Sets.Facade.ParentMethods.facade_for`.

                Internal invariants:

                - ``self._element_init_pass_parent == guess_pass_parent(self,
                  self._element_constructor)`` Ensures that :meth:`__call__`
                  passes down the parent properly to
                  :meth:`_element_constructor`.  See :issue:`5979`.

                .. TODO::

                    Eventually, category should be
                    :class:`~sage.categories.sets_cat.Sets` by default.

                TESTS:

                We check that the facade option is compatible with specifying
                categories as a tuple::

                    sage: class MyClass(Parent): pass
                    sage: P = MyClass(facade = ZZ, category = (Monoids(), CommutativeAdditiveMonoids()))
                    sage: P.category()
                    Join of Category of monoids and Category of commutative additive monoids and Category of facade sets

                .. automethod:: __call__
                .. automethod:: _populate_coercion_lists_
                .. automethod:: __mul__
                .. automethod:: __contains__
                .. automethod:: _coerce_map_from_
                .. automethod:: _convert_map_from_
                .. automethod:: _get_action_
                .. automethod:: _an_element_
                .. automethod:: _repr_option
                .. automethod:: _init_category_
                .. automethod:: _is_coercion_cached
                .. automethod:: _is_conversion_cached
        """
    def Hom(self, codomain: Parent, category: Category | None = None) -> Homset: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Return the homspace ``Hom(self, codomain, category)``.

        INPUT:

        - ``codomain`` -- a parent
        - ``category`` -- a category or ``None`` (default: ``None``)
          If ``None``, the meet of the category of ``self`` and
          ``codomain`` is used.

        OUTPUT:

        The homspace of all homomorphisms from ``self`` to
        ``codomain`` in the category ``category``.

        .. SEEALSO:: :func:`~sage.categories.homset.Hom`

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.Hom(QQ)
            Set of Homomorphisms from Multivariate Polynomial Ring in x, y over Rational Field to Rational Field

        Homspaces are defined for very general Sage objects, even elements of familiar rings::

            sage: n = 5; Hom(n,7)
            Set of Morphisms from 5 to 7 in Category of elements of Integer Ring
            sage: z=(2/3); Hom(z,8/1)
            Set of Morphisms from 2/3 to 8 in Category of elements of Rational Field

        This example illustrates the optional third argument::

            sage: QQ.Hom(ZZ, Sets())
            Set of Morphisms from Rational Field to Integer Ring in Category of sets

        A parent may specify how to construct certain homsets by
        implementing a method :meth:`_Hom_`(codomain, category).
        See :func:`~sage.categories.homset.Hom` for details."""
    def an_element(self) -> Element[Self]:
        """
        Return a (preferably typical) element of this parent.

        This is used both for illustration and testing purposes. If
        the set ``self`` is empty, :meth:`an_element` raises the
        exception :exc:`EmptySetError`.

        This calls :meth:`_an_element_` (which see), and caches the
        result. Parent are thus encouraged to override :meth:`_an_element_`.

        EXAMPLES::

            sage: CDF.an_element()                                                      # needs sage.rings.complex_double
            1.0*I
            sage: ZZ[['t']].an_element()
            t

        In case the set is empty, an :exc:`EmptySetError` is raised::

            sage: Set([]).an_element()
            Traceback (most recent call last):
            ...
            EmptySetError"""
    def category(self) -> type[Category]:
        """
        EXAMPLES::

            sage: P = Parent()
            sage: P.category()
            Category of sets
            sage: class MyParent(Parent):
            ....:     def __init__(self): pass
            sage: MyParent().category()
            Category of sets"""
    def coerce(self: Self, x) -> Element[Self]:
        """
        Return x as an element of ``self``, if and only if there is a
        canonical coercion from the parent of x to ``self``.

        EXAMPLES::

            sage: QQ.coerce(ZZ(2))
            2
            sage: ZZ.coerce(QQ(2))
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Rational Field to Integer Ring

        We make an exception for zero::

            sage: V = GF(7)^7                                                           # needs sage.modules
            sage: V.coerce(0)                                                           # needs sage.modules
            (0, 0, 0, 0, 0, 0, 0)"""
    def coerce_embedding(self) -> Map:
        """
        Return the embedding of ``self`` into some other parent, if such a
        parent exists.

        This does not mean that there are no coercion maps from ``self`` into
        other fields, this is simply a specific morphism specified out of
        ``self`` and usually denotes a special relationship (e.g. sub-objects,
        choice of completion, etc.)

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + 1, embedding=1)
            sage: K.coerce_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^3 + x^2 + 1
                    with a = -1.465571231876768?
              To:   Real Lazy Field
              Defn: a -> -1.465571231876768?
            sage: K.<a> = NumberField(x^3 + x^2 + 1, embedding=CC.gen())
            sage: K.coerce_embedding()
            Generic morphism:
              From: Number Field in a with defining polynomial x^3 + x^2 + 1
                    with a = 0.2327856159383841? + 0.7925519925154479?*I
              To:   Complex Lazy Field
              Defn: a -> 0.2327856159383841? + 0.7925519925154479?*I"""
    def coerce_map_from(self, S: Parent | type) -> Map | None:
        """
        Return a :class:`Map` object to coerce from ``S`` to ``self`` if one
        exists, or ``None`` if no such coercion exists.

        EXAMPLES:

        By :issue:`12313`, a special kind of weak key dictionary is used to
        store coercion and conversion maps, namely
        :class:`~sage.structure.coerce_dict.MonoDict`. In that way, a memory
        leak was fixed that would occur in the following test::

            sage: import gc
            sage: _ = gc.collect()
            sage: K = GF(1<<55,'t')                                                     # needs sage.rings.finite_rings
            sage: for i in range(50):                                                   # needs sage.rings.finite_rings sage.schemes
            ....:   a = K.random_element()
            ....:   E = EllipticCurve(j=a)
            ....:   b = K.has_coerce_map_from(E)
            sage: _ = gc.collect()
            sage: len([x for x in gc.get_objects() if isinstance(x, type(E))])          # needs sage.rings.finite_rings sage.schemes
            1

        TESTS:

        The following was fixed in :issue:`12969`::

            sage: # needs sage.combinat sage.modules
            sage: R = QQ['q,t'].fraction_field()
            sage: Sym = SymmetricFunctions(R)
            sage: H = Sym.macdonald().H()
            sage: P = Sym.macdonald().P()
            sage: m = Sym.monomial()
            sage: Ht = Sym.macdonald().Ht()
            sage: phi = m.coerce_map_from(P)"""
    def convert_map_from(self, S: Parent | type) -> Map | None:
        """
        This function returns a :class:`Map` from `S` to ``self``,
        which may or may not succeed on all inputs.
        If a coercion map from S to ``self`` exists,
        then the it will be returned. If a coercion from ``self`` to `S` exists,
        then it will attempt to return a section of that map.

        Under the new coercion model, this is the fastest way to convert
        elements of `S` to elements of ``self`` (short of manually constructing
        the elements) and is used by :meth:`__call__`.

        EXAMPLES::

            sage: m = ZZ.convert_map_from(QQ)
            sage: m
            Generic map:
              From: Rational Field
              To:   Integer Ring
            sage: m(-35/7)
            -5
            sage: parent(m(-35/7))
            Integer Ring"""
    def element_class(self) -> type:
        """
        The (default) class for the elements of this parent.

        FIXME\'s and design issues:

        - If self.Element is "trivial enough", should we optimize it away with:
          self.element_class = dynamic_class("%s.element_class"%self.__class__.__name__, (category.element_class,), self.Element)
        - This should lookup for Element classes in all super classes"""
    def get_action( # TODO: not yet done
        self, S: type | Parent, 
        op: _BinOp = operator.mul, 
        self_on_left: bool = True, 
        self_el =None, 
        S_el =None
    ) -> Action:
        """
        Return an action of ``self`` on ``S`` or ``S`` on ``self``.

        To provide additional actions, override :meth:`_get_action_`.

        .. WARNING::

            This is not the method that you typically want to call.
            Instead, call ``coercion_model.get_action(...)`` which
            caches results (this ``Parent.get_action`` method does not).

        TESTS::

            sage: M = QQ['y']^3                                                         # needs sage.modules
            sage: M.get_action(ZZ['x']['y'])                                            # needs sage.modules
            Right scalar multiplication
             by Univariate Polynomial Ring in y
                over Univariate Polynomial Ring in x over Integer Ring
             on Ambient free module of rank 3 over the principal ideal domain
                Univariate Polynomial Ring in y over Rational Field
            sage: print(M.get_action(ZZ['x']))                                          # needs sage.modules
            None"""
    @overload
    def has_coerce_map_from(self, S) -> bool:
        """
        Return ``True`` if there is a natural map from ``S`` to ``self``.
        Otherwise, return ``False``.

        EXAMPLES::

            sage: RDF.has_coerce_map_from(QQ)
            True
            sage: RDF.has_coerce_map_from(QQ['x'])
            False
            sage: RDF['x'].has_coerce_map_from(QQ['x'])
            True
            sage: RDF['x,y'].has_coerce_map_from(QQ['x'])
            True"""
    @overload
    def has_coerce_map_from(self, QQ) -> Any:
        """
        Return ``True`` if there is a natural map from ``S`` to ``self``.
        Otherwise, return ``False``.

        EXAMPLES::

            sage: RDF.has_coerce_map_from(QQ)
            True
            sage: RDF.has_coerce_map_from(QQ['x'])
            False
            sage: RDF['x'].has_coerce_map_from(QQ['x'])
            True
            sage: RDF['x,y'].has_coerce_map_from(QQ['x'])
            True"""
    @overload
    def hom(    # TODO: not sure how this works yet
        self, 
        im_gens: PySequence,
        codomain: None = None,
        check = None, 
        base_map = None, 
        category: Category | None = None, 
        **kwds
    ) -> Element[Homset]: ...
    @overload
    def hom[C: Parent](
        self, 
        im_gens: PySequence[Element[C]], 
        codomain: C, 
        check: bool | None = None, 
        base_map = None, 
        category: Category | None = None, 
        **kwds
    ) -> Element[Homset]:
        """
        Return the unique homomorphism from ``self`` to ``codomain`` that
        sends ``self.gens()`` to the entries of ``im_gens``.

        This raises a :exc:`TypeError` if there is no such homomorphism.

        INPUT:

        - ``im_gens`` -- the images in the codomain of the generators
          of this object under the homomorphism

        - ``codomain`` -- the codomain of the homomorphism

        - ``base_map`` -- a map from the base ring to the codomain; if not
          given, coercion is used

        - ``check`` -- whether to verify that the images of generators
          extend to define a map (using only canonical coercions)

        OUTPUT: a homomorphism ``self --> codomain``

        .. NOTE::

            As a shortcut, one can also give an object X instead of
            ``im_gens``, in which case return the (if it exists)
            natural map to X.

        EXAMPLES:

        Polynomial Ring: We first illustrate construction of a few
        homomorphisms involving a polynomial ring::

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
            sage: f = R.hom([3], GF(49,'a'))
            sage: f
            Ring morphism:
              From: Univariate Polynomial Ring in x over Finite Field of size 7
              To:   Finite Field in a of size 7^2
              Defn: x |--> 3
            sage: f(x + 6)
            2
            sage: f(x^2 + 1)
            3

        Natural morphism::

            sage: f = ZZ.hom(GF(5))
            sage: f(7)
            2
            sage: f
            Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5

        There might not be a natural morphism, in which case a
        :exc:`TypeError` is raised::

            sage: QQ.hom(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: natural coercion morphism from Rational Field to Integer Ring not defined"""
    def is_exact(self) -> bool:
        """
        Test whether elements of this parent are represented exactly.

        .. NOTE::

            This defaults to true, so even if it does return ``True``
            you have no guarantee (unless the parent has properly
            overloaded this).

        OUTPUT:

        Return ``True`` if elements of this parent are represented exactly, i.e.,
        there is no precision loss when doing arithmetic.

        EXAMPLES::

            sage: QQ.is_exact()
            True
            sage: ZZ.is_exact()
            True
            sage: Qp(7).is_exact()                                                      # needs sage.rings.padics
            False
            sage: Zp(7, type='capped-abs').is_exact()                                   # needs sage.rings.padics
            False"""
    def register_action(self, action: Action) -> None:
        """
        Update the coercion model to use ``action`` to act on ``self``.

        ``action`` should be of type ``sage.categories.action.Action``.

        EXAMPLES::

            sage: import sage.categories.action
            sage: import operator

            sage: class SymmetricGroupAction(sage.categories.action.Action):
            ....:     "Act on a multivariate polynomial ring by permuting the generators."
            ....:     def __init__(self, G, M, is_left=True):
            ....:         sage.categories.action.Action.__init__(self, G, M, is_left, operator.mul)
            ....:
            ....:     def _act_(self, g, a):
            ....:         D = {}
            ....:         for k, v in a.monomial_coefficients().items():
            ....:             nk = [0]*len(k)
            ....:             for i in range(len(k)):
            ....:                 nk[g(i+1)-1] = k[i]
            ....:             D[tuple(nk)] = v
            ....:         return a.parent()(D)

            sage: # needs sage.groups
            sage: R.<x, y, z> = QQ[\'x, y, z\']
            sage: G = SymmetricGroup(3)
            sage: act = SymmetricGroupAction(G, R)
            sage: t = x + 2*y + 3*z

            sage: # needs sage.groups
            sage: act(G((1, 2)), t)
            2*x + y + 3*z
            sage: act(G((2, 3)), t)
            x + 3*y + 2*z
            sage: act(G((1, 2, 3)), t)
            3*x + y + 2*z

        This should fail, since we have not registered the left
        action::

            sage: G((1,2)) * t                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            TypeError: ...

        Now let\'s make it work::

            sage: # needs sage.groups
            sage: R._unset_coercions_used()
            sage: R.register_action(act)
            sage: G((1, 2)) * t
            2*x + y + 3*z"""
    def register_coercion(self, mor: Map | type | Parent) -> None:
        """
        Update the coercion model to use `mor : P \\to \\text{self}` to coerce
        from a parent ``P`` into ``self``.

        For safety, an error is raised if another coercion has already
        been registered or discovered between ``P`` and ``self``.

        EXAMPLES::

            sage: K.<a> = ZZ['a']
            sage: L.<b> = ZZ['b']
            sage: L_into_K = L.hom([-a]) # non-trivial automorphism
            sage: K.register_coercion(L_into_K)

            sage: K(0) + b
            -a
            sage: a + b
            0
            sage: K(b) # check that convert calls coerce first; normally this is just a
            -a

            sage: L(0) + a in K # this goes through the coercion mechanism of K
            True
            sage: L(a) in L # this still goes through the convert mechanism of L
            True

            sage: K.register_coercion(L_into_K)
            Traceback (most recent call last):
            ...
            AssertionError: coercion from Univariate Polynomial Ring in b over Integer Ring to Univariate Polynomial Ring in a over Integer Ring already registered or discovered

        TESTS:

        We check that :issue:`29517` has been fixed::

            sage: A.<x> = ZZ[]
            sage: B.<y> = ZZ[]
            sage: B.has_coerce_map_from(A)
            False
            sage: B.register_coercion(A.hom([y]))
            sage: x + y
            2*y"""
    def register_conversion(self, mor: type | Parent | Map) -> None:
        """
        Update the coercion model to use `\\text{mor} : P \\to \\text{self}` to convert
        from ``P`` into ``self``.

        EXAMPLES::

            sage: K.<a> = ZZ['a']
            sage: M.<c> = ZZ['c']
            sage: M_into_K = M.hom([a]) # trivial automorphism
            sage: K._unset_coercions_used()
            sage: K.register_conversion(M_into_K)

            sage: K(c)
            a
            sage: K(0) + c
            Traceback (most recent call last):
            ...
            TypeError: ..."""
    def register_embedding(self, embedding: Map | Parent) -> None:
        """
        Add embedding to coercion model.

        This method updates the coercion model to use
        `\\text{embedding} : \\text{self} \\to P` to embed ``self`` into
        the parent ``P``.

        There can only be one embedding registered; it can only be registered
        once; and it must be registered before using this parent in the
        coercion model.

        EXAMPLES::

            sage: S3 = AlternatingGroup(3)                                              # needs sage.groups
            sage: G = SL(3, QQ)                                                         # needs sage.groups
            sage: p = S3[2]; p.matrix()                                                 # needs sage.groups
            [0 0 1]
            [1 0 0]
            [0 1 0]

        In general one cannot mix matrices and permutations::

            sage: # needs sage.groups
            sage: G(p)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert (1,3,2) to a rational
            sage: phi = S3.hom(lambda p: G(p.matrix()), codomain=G)
            sage: phi(p)
            [0 0 1]
            [1 0 0]
            [0 1 0]
            sage: S3._unset_coercions_used()
            sage: S3.register_embedding(phi)

        By :issue:`14711`, coerce maps should be copied when using outside of
        the coercion system::

            sage: phi = copy(S3.coerce_embedding()); phi                                # needs sage.groups
            Generic morphism:
              From: Alternating group of order 3!/2 as a permutation group
              To:   Special Linear Group of degree 3 over Rational Field
            sage: phi(p)                                                                # needs sage.groups
            [0 0 1]
            [1 0 0]
            [0 1 0]

        This does not work since matrix groups are still old-style
        parents (see :issue:`14014`)::

            sage: G(p)                          # not implemented                       # needs sage.groups

        Though one can have a permutation act on the rows of a matrix::

            sage: G(1) * p                                                              # needs sage.groups
            [0 0 1]
            [1 0 0]
            [0 1 0]

        Some more advanced examples::

            sage: # needs sage.rings.number_field
            sage: x = QQ[\'x\'].0
            sage: t = abs(ZZ.random_element(10^6))
            sage: K = NumberField(x^2 + 2*3*7*11, "a"+str(t))
            sage: a = K.gen()
            sage: K_into_MS = K.hom([a.matrix()])
            sage: K._unset_coercions_used()
            sage: K.register_embedding(K_into_MS)

            sage: # needs sage.rings.number_field
            sage: L = NumberField(x^2 + 2*3*7*11*19*31,
            ....:                 "b" + str(abs(ZZ.random_element(10^6))))
            sage: b = L.gen()
            sage: L_into_MS = L.hom([b.matrix()])
            sage: L._unset_coercions_used()
            sage: L.register_embedding(L_into_MS)

            sage: K.coerce_embedding()(a)                                               # needs sage.rings.number_field
            [   0    1]
            [-462    0]
            sage: L.coerce_embedding()(b)                                               # needs sage.rings.number_field
            [      0       1]
            [-272118       0]

            sage: a.matrix() * b.matrix()                                               # needs sage.rings.number_field
            [-272118       0]
            [      0    -462]
            sage: a.matrix() * b.matrix()                                               # needs sage.rings.number_field
            [-272118       0]
            [      0    -462]"""
    
    def __getstate__(self) -> dict[str, Any]:
            """
            Used for pickling.

            TESTS::

                sage: loads(dumps(RR['x'])) == RR['x']
                True
            """
    def __setstate__(self, d: dict[str, Any]) -> None:
        """
        Used for pickling.

        TESTS::

            sage: loads(dumps(CDF['x'])) == CDF['x']                                    # needs sage.rings.complex_double
            True
        """

    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self: Self, x: Any = 0, *args, **kwds) -> Element[Self]: # eg for RR, Self is RealField_class, returns RealNumber
        """
        This is the generic call method for all parents.

        When called, it will find a map based on the Parent (or type) of x.
        If a coercion exists, it will always be chosen. This map will
        then be called (with the arguments and keywords if any).

        By default this will dispatch as quickly as possible to
        :meth:`_element_constructor_` though faster pathways are
        possible if so desired.

        TESTS:

        We check that the invariant

        ::

            self._element_init_pass_parent == guess_pass_parent(self, self._element_constructor)

        is preserved (see :issue:`5979`)::

            sage: class MyParent(Parent):
            ....:     def _element_constructor_(self, x):
            ....:         print("{} {}".format(self, x))
            ....:         return sage.structure.element.Element(parent = self)
            ....:     def _repr_(self):
            ....:         return "my_parent"
            sage: my_parent = MyParent()
            sage: x = my_parent("bla")
            my_parent bla
            sage: x.parent()         # indirect doctest
            my_parent

            sage: x = my_parent()    # shouldn\'t this one raise an error?
            my_parent 0
            sage: x = my_parent(3)   # todo: not implemented  why does this one fail???
            my_parent 3"""
    def __contains__(self, x) -> bool:
        """
        ``True`` if there is an element of ``self`` that is equal to ``x``
        under ``==``, or if ``x`` is already an element of ``self``.  Also,
        ``True`` in other cases involving the Symbolic Ring, which is handled
        specially.

        For many structures we test this by using :meth:`__call__` and
        then testing equality between ``x`` and the result.

        The Symbolic Ring is treated differently because it is
        ultra-permissive about letting other rings coerce in, but
        ultra-strict about doing comparisons.

        EXAMPLES::

            sage: 2 in Integers(7)
            True
            sage: 2 in ZZ
            True
            sage: Integers(7)(3) in ZZ
            True
            sage: 3/1 in ZZ
            True
            sage: 5 in QQ
            True
            sage: I in RR                                                               # needs sage.rings.real_mpfr sage.symbolic
            False
            sage: RIF(1, 2) in RIF                                                      # needs sage.rings.real_interval_field
            True

            sage: # needs sage.symbolic
            sage: SR(2) in ZZ
            True
            sage: pi in RIF  # there is no element of RIF equal to pi
            False
            sage: sqrt(2) in CC
            True
            sage: pi in RR
            True
            sage: pi in CC
            True
            sage: pi in RDF
            True
            sage: pi in CDF
            True

        Note that we have

        ::

            sage: 3/2 in RIF                                                            # needs sage.rings.real_interval_field
            True

        because ``3/2`` has an exact representation in ``RIF`` (i.e. can be
        represented as an interval that contains exactly one value)::

            sage: RIF(3/2).is_exact()                                                   # needs sage.rings.real_interval_field
            True

        On the other hand, we have

        ::

            sage: 2/3 in RIF                                                            # needs sage.rings.real_interval_field
            False

        because ``2/3`` has no exact representation in ``RIF``. Since
        ``RIF(2/3)`` is a nontrivial interval, it cannot be equal to anything
        (not even itself)::

            sage: RIF(2/3).is_exact()                                                   # needs sage.rings.real_interval_field
            False
            sage: RIF(2/3).endpoints()                                                  # needs sage.rings.real_interval_field
            (0.666666666666666, 0.666666666666667)
            sage: RIF(2/3) == RIF(2/3)                                                  # needs sage.rings.real_interval_field
            False

        TESTS:

        Check that :issue:`13824` is fixed::

            sage: 4/3 in GF(3)
            False
            sage: 15/50 in GF(25, 'a')                                                  # needs sage.rings.finite_rings
            False
            sage: 7/4 in Integers(4)
            False
            sage: 15/36 in Integers(6)
            False

        Check that :issue:`32078` is fixed::

            sage: P = Frac(ZZ['x,y'])
            sage: P(1) in ZZ
            True
            sage: P(1/2) in ZZ
            False

        Check that :issue:`24209` is fixed::

            sage: I in QQbar                                                            # needs sage.rings.number_field
            True
            sage: sqrt(-1) in QQbar                                                     # needs sage.rings.number_field sage.symbolic
            True"""
    def __getitem__(self, n) -> Any:
        """
        Return the `n`-th item or slice `n` of ``self``,
        by getting ``self`` as a list.

        EXAMPLES::

            sage: VectorSpace(GF(7), 3)[:10]                                            # needs sage.modules
            [(0, 0, 0),
             (1, 0, 0),
             (2, 0, 0),
             (3, 0, 0),
             (4, 0, 0),
             (5, 0, 0),
             (6, 0, 0),
             (0, 1, 0),
             (1, 1, 0),
             (2, 1, 0)]

        TESTS:

        We test the workaround described in :issue:`12956` to let categories
        override this default implementation::

            sage: class As(Category):
            ....:     def super_categories(self): return [Sets()]
            ....:     class ParentMethods:
            ....:         def __getitem__(self, n):
            ....:             return 'coucou'
            sage: class A(Parent):
            ....:     def __init__(self):
            ....:         Parent.__init__(self, category=As())
            sage: a = A()
            sage: a[1]
            'coucou'"""
    def __make_element_class__(
        self, 
        cls: type, 
        name: str | None = None, 
        module: str | None = None, 
        inherit: bool | None = None
    ) -> type:
        """
        A utility to construct classes for the elements of this
        parent, with appropriate inheritance from the element class of
        the category.

        It used to be the case that this did not work for extension
        types, which used to never support a ``__dict__`` for instances.
        So for backwards compatibility, we only use dynamic classes by
        default if the class has a nonzero ``__dictoffset__``. But it
        works regardless: just pass ``inherit=True`` to
        ``__make_element_class__``. See also :issue:`24715`.

        When we do not use a dynamic element class, the ``__getattr__``
        implementation from :class:`Element` provides fake
        inheritance from categories."""
    def __mul__(self, x) -> Any:
        """
        This is a multiplication method that more or less directly
        calls another attribute ``_mul_`` (single underscore). This
        is because ``__mul__`` cannot be implemented via inheritance
        from the parent methods of the category, but ``_mul_`` can
        be inherited. This is, e.g., used when creating twosided
        ideals of matrix algebras. See :issue:`7797`.

        EXAMPLES::

            sage: MS = MatrixSpace(QQ, 2, 2)                                            # needs sage.modules

        This matrix space is in fact an algebra, and in particular
        it is a ring, from the point of view of categories::

            sage: MS.category()                                                         # needs sage.modules
            Category of infinite finite dimensional algebras with basis
             over (number fields and quotient fields and metric spaces)
            sage: MS in Rings()                                                         # needs sage.modules
            True

        However, its class does not inherit from the base class
        ``Ring``::

            sage: isinstance(MS, Ring)                                                  # needs sage.modules
            False

        Its ``_mul_`` method is inherited from the category, and
        can be used to create a left or right ideal::

            sage: # needs sage.modules
            sage: MS._mul_.__module__
            'sage.categories.rings'
            sage: MS * MS.1      # indirect doctest
            Left Ideal
            (
              [0 1]
              [0 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: MS * [MS.1, 2]
            Left Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [2 0]
              [0 2]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: MS.1 * MS
            Right Ideal
            (
              [0 1]
              [0 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: [MS.1, 2] * MS
            Right Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [2 0]
              [0 2]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field"""
    @overload
    def __pow__(self, x, mod) -> Any:
        """
        Power function.

        The default implementation of ``__pow__`` on parent redirects to the
        super class (in case of multiple inheritance) or to the category. This
        redirection is necessary when the parent is a Cython class (aka
        extension class) because in that case the parent class does not inherit
        from the ``ParentMethods`` of the category.

        Concrete implementations of parents can freely overwrite this default
        method.

        TESTS::

            sage: # needs sage.modules
            sage: ZZ^3
            Ambient free module of rank 3 over the principal ideal domain
             Integer Ring
            sage: QQ^3
            Vector space of dimension 3 over Rational Field
            sage: QQ['x']^3
            Ambient free module of rank 3 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field
            sage: IntegerModRing(6)^3
            Ambient free module of rank 3 over Ring of integers modulo 6

            sage: 3^ZZ
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for ^: 'Integer Ring' and '<class 'sage.rings.integer_ring.IntegerRing_class'>'
            sage: Partitions(3)^3                                                       # needs sage.combinat sage.modules
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'Partitions_n_with_category' and 'int'

        Check multiple inheritance::

            sage: class A:
            ....:    def __pow__(self, n):
            ....:        return 'Apow'
            sage: class MyParent(A, Parent):
            ....:    pass
            sage: MyParent()^2
            'Apow'"""
    @overload
    def __pow__(self, n) -> Any:
        """
        Power function.

        The default implementation of ``__pow__`` on parent redirects to the
        super class (in case of multiple inheritance) or to the category. This
        redirection is necessary when the parent is a Cython class (aka
        extension class) because in that case the parent class does not inherit
        from the ``ParentMethods`` of the category.

        Concrete implementations of parents can freely overwrite this default
        method.

        TESTS::

            sage: # needs sage.modules
            sage: ZZ^3
            Ambient free module of rank 3 over the principal ideal domain
             Integer Ring
            sage: QQ^3
            Vector space of dimension 3 over Rational Field
            sage: QQ['x']^3
            Ambient free module of rank 3 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field
            sage: IntegerModRing(6)^3
            Ambient free module of rank 3 over Ring of integers modulo 6

            sage: 3^ZZ
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for ^: 'Integer Ring' and '<class 'sage.rings.integer_ring.IntegerRing_class'>'
            sage: Partitions(3)^3                                                       # needs sage.combinat sage.modules
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for ** or pow(): 'Partitions_n_with_category' and 'int'

        Check multiple inheritance::

            sage: class A:
            ....:    def __pow__(self, n):
            ....:        return 'Apow'
            sage: class MyParent(A, Parent):
            ....:    pass
            sage: MyParent()^2
            'Apow'"""
    def __rmul__(self, other): ...
    def __rpow__(self, other): ...

class Set_generic(Parent):
    """
        Abstract base class for sets.

        TESTS::

            sage: Set(QQ).category()
            Category of infinite sets
    """
    
    def object(self) -> Self:
        """
        Return the underlying object of ``self``.

        EXAMPLES::

            sage: Set(QQ).object()
            Rational Field"""
    def __bool__(self) -> bool: ...

class EltPair[Tag]:
    x: Any
    y: Any
    tag: Tag
    def short_repr(self) -> tuple[Tag, str, str]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int:
        """
        EXAMPLES::

            sage: from sage.structure.parent import EltPair
            sage: a = EltPair(ZZ, QQ, "coerce")
            sage: b = EltPair(ZZ, QQ, "coerce")
            sage: hash(a) == hash(b)
            True

        TESTS:

        Verify that :issue:`16341` has been resolved::

            sage: K.<a> = Qq(9)                                                         # needs sage.rings.padics
            sage: E = EllipticCurve_from_j(0).base_extend(K)                            # needs sage.rings.padics
            sage: E.get_action(ZZ)                                                      # needs sage.rings.padics
            Right action by Integer Ring
             on Elliptic Curve defined by y^2 + (1+O(3^20))*y = x^3
              over 3-adic Unramified Extension Field in a
               defined by x^2 + 2*x + 2"""
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
