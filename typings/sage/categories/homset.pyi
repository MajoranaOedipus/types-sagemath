from sage.categories import morphism as morphism
from sage.categories.category import Category as Category, JoinCategory as JoinCategory
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.coerce_dict import TripleDict as TripleDict
from sage.structure.dynamic_class import dynamic_class as dynamic_class
from sage.structure.parent import Parent as Parent, Set_generic as Set_generic
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def Hom(X, Y, category=None, check: bool = True):
    '''
    Create the space of homomorphisms from X to Y in the category ``category``.

    INPUT:

    - ``X`` -- an object of a category

    - ``Y`` -- an object of a category

    - ``category`` -- a category in which the morphisms must be
      (default: the meet of the categories of ``X`` and ``Y``);
      both ``X`` and ``Y`` must belong to that category

    - ``check`` -- boolean (default: ``True``); whether to check the
      input, and in particular that ``X`` and ``Y`` belong to
      ``category``.

    OUTPUT: a homset in category

    EXAMPLES::

        sage: V = VectorSpace(QQ, 3)                                                    # needs sage.modules
        sage: Hom(V, V)                                                                 # needs sage.modules
        Set of Morphisms (Linear Transformations) from
        Vector space of dimension 3 over Rational Field to
        Vector space of dimension 3 over Rational Field
        sage: G = AlternatingGroup(3)                                                   # needs sage.groups
        sage: Hom(G, G)                                                                 # needs sage.groups
        Set of Morphisms
         from Alternating group of order 3!/2 as a permutation group
           to Alternating group of order 3!/2 as a permutation group
           in Category of finite enumerated permutation groups
        sage: Hom(ZZ, QQ, Sets())
        Set of Morphisms from Integer Ring to Rational Field in Category of sets

        sage: Hom(FreeModule(ZZ, 1), FreeModule(QQ, 1))                                 # needs sage.modules
        Set of Morphisms
         from Ambient free module of rank 1 over the principal ideal domain Integer Ring
           to Vector space of dimension 1 over Rational Field
           in Category of commutative additive groups
        sage: Hom(FreeModule(QQ, 1), FreeModule(ZZ, 1))                                 # needs sage.modules
        Set of Morphisms
         from Vector space of dimension 1 over Rational Field
           to Ambient free module of rank 1 over the principal ideal domain Integer Ring
           in Category of commutative additive groups

    Here, we test against a memory leak that has been fixed at :issue:`11521` by
    using a weak cache::

        sage: # needs sage.libs.pari
        sage: for p in prime_range(10^3):
        ....:  K = GF(p)
        ....:  a = K(0)
        sage: import gc
        sage: gc.collect()       # random
        624
        sage: from sage.rings.finite_rings.finite_field_prime_modn import FiniteField_prime_modn as FF
        sage: L = [x for x in gc.get_objects() if isinstance(x, FF)]
        sage: len(L), L[0]
        (1, Finite Field of size 997)

    To illustrate the choice of the category, we consider the
    following parents as running examples::

        sage: X = ZZ; X
        Integer Ring
        sage: Y = SymmetricGroup(3); Y                                                  # needs sage.groups
        Symmetric group of order 3! as a permutation group

    By default, the smallest category containing both ``X`` and ``Y``,
    is used::

        sage: Hom(X, Y)                                                                 # needs sage.groups
        Set of Morphisms from Integer Ring
         to Symmetric group of order 3! as a permutation group
         in Category of enumerated monoids

    Otherwise, if ``category`` is specified, then ``category`` is used,
    after checking that ``X`` and ``Y`` are indeed in ``category``::

        sage: Hom(X, Y, Magmas())                                                       # needs sage.groups
        Set of Morphisms
         from Integer Ring
         to Symmetric group of order 3! as a permutation group
         in Category of magmas

        sage: Hom(X, Y, Groups())                                                       # needs sage.groups
        Traceback (most recent call last):
        ...
        ValueError: Integer Ring is not in Category of groups

    A parent (or a parent class of a category) may specify how to
    construct certain homsets by implementing a method ``_Hom_(self,
    codomain, category)``. This method should either construct the
    requested homset or raise a :exc:`TypeError`. This hook is currently
    mostly used to create homsets in some specific subclass of
    :class:`Homset` (e.g. :class:`sage.rings.homset.RingHomset`)::

        sage: Hom(QQ,QQ).__class__
        <class \'sage.rings.homset.RingHomset_generic_with_category\'>

    Do not call this hook directly to create homsets, as it does not
    handle unique representation::

        sage: Hom(QQ,QQ) == QQ._Hom_(QQ, category=QQ.category())
        True
        sage: Hom(QQ,QQ) is QQ._Hom_(QQ, category=QQ.category())
        False

    TESTS:

    Homset are unique parents::

        sage: k = GF(5)
        sage: H1 = Hom(k, k)
        sage: H2 = Hom(k, k)
        sage: H1 is H2
        True

    Moreover, if no category is provided, then the result is identical
    with the result for the meet of the categories of the domain and
    the codomain::

        sage: Hom(QQ, ZZ) is Hom(QQ,ZZ, Category.meet([QQ.category(), ZZ.category()]))
        True

    Some doc tests in :mod:`sage.rings` (need to) break the unique
    parent assumption. But if domain or codomain are not unique
    parents, then the homset will not fit. That is to say, the hom set
    found in the cache will have a (co)domain that is equal to, but
    not identical with, the given (co)domain.

    By :issue:`9138`, we abandon the uniqueness of homsets, if the
    domain or codomain break uniqueness::

        sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
        sage: P.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order=\'degrevlex\')
        sage: Q.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order=\'degrevlex\')
        sage: P == Q
        True
        sage: P is Q
        False

    Hence, ``P`` and ``Q`` are not unique parents. By consequence, the
    following homsets aren\'t either::

        sage: H1 = Hom(QQ,P)
        sage: H2 = Hom(QQ,Q)
        sage: H1 == H2
        True
        sage: H1 is H2
        False

    It is always the most recently constructed homset that remains in
    the cache::

        sage: H2 is Hom(QQ,Q)
        True

    Variation on the theme::

        sage: # needs sage.modules
        sage: U1 = FreeModule(ZZ, 2)
        sage: U2 = FreeModule(ZZ, 2, inner_product_matrix=matrix([[1,0], [0,-1]]))
        sage: U1 == U2, U1 is U2
        (False, False)
        sage: V = ZZ^3
        sage: H1 = Hom(U1, V); H2 = Hom(U2, V)
        sage: H1 == H2, H1 is H2
        (False, False)
        sage: H1 = Hom(V, U1); H2 = Hom(V, U2)
        sage: H1 == H2, H1 is H2
        (False, False)

    Since :issue:`11900`, the meet of the categories of the given arguments is
    used to determine the default category of the homset. This can also be a
    join category, as in the following example::

        sage: PA = Parent(category=Algebras(QQ))
        sage: PJ = Parent(category=Rings() & Modules(QQ))
        sage: Hom(PA, PJ)
        Set of Homomorphisms
         from <sage.structure.parent.Parent object at ...>
           to <sage.structure.parent.Parent object at ...>
        sage: Hom(PA, PJ).category()
        Category of homsets of
         unital magmas and right modules over Rational Field
          and left modules over Rational Field
        sage: Hom(PA, PJ, Rngs())
        Set of Morphisms
         from <sage.structure.parent.Parent object at ...>
           to <sage.structure.parent.Parent object at ...> in Category of rngs

    .. TODO::

        - Design decision: how much of the homset comes from the
          category of ``X`` and ``Y``, and how much from the specific
          ``X`` and ``Y``.  In particular, do we need several parent
          classes depending on ``X`` and ``Y``, or does the difference
          only lie in the elements (i.e.  the morphism), and of course
          how the parent calls their constructors.
        - Specify the protocol for the ``_Hom_`` hook in case of ambiguity
          (e.g. if both a parent and some category thereof provide one).

    TESTS:

    Facade parents over plain Python types are supported::

        sage: from sage.sets.pythonclass import Set_PythonType
        sage: R = Set_PythonType(int)
        sage: S = Set_PythonType(float)
        sage: Hom(R, S)
        Set of Morphisms from Set of Python objects of class \'int\'
         to Set of Python objects of class \'float\' in Category of infinite sets

    Checks that the domain and codomain are in the specified
    category. Case of a non parent::

        sage: # needs sage.graphs
        sage: S = SimplicialComplex([[1,2], [1,4]]); S.rename(\'S\')
        sage: Hom(S, S, SimplicialComplexes())
        Set of Morphisms from S to S in Category of finite simplicial complexes
        sage: Hom(Set(), S, Sets())
        Set of Morphisms from {} to S in Category of sets
        sage: Hom(S, Set(), Sets())
        Set of Morphisms from S to {} in Category of sets
        sage: H = Hom(S, S, ChainComplexes(QQ))
        Traceback (most recent call last):
        ...
        ValueError: S is not in Category of chain complexes over Rational Field

    Those checks are done with the natural idiom ``X in category``,
    and not ``X.category().is_subcategory(category)`` as it used to be
    before :issue:`16275` (see :issue:`15801` for a real use case)::

        sage: # needs sage.graphs
        sage: class PermissiveCategory(Category):
        ....:     def super_categories(self): return [Objects()]
        ....:     def __contains__(self, X): return True
        sage: C = PermissiveCategory(); C.rename(\'Permissive category\')
        sage: S.category().is_subcategory(C)
        False
        sage: S in C
        True
        sage: Hom(S, S, C)
        Set of Morphisms from S to S in Permissive category

    With ``check=False``, uninitialized parents, as can appear upon
    unpickling, are supported. Case of a parent::

        sage: cls = type(Set())
        sage: S = unpickle_newobj(cls, ())  # A non parent
        sage: H = Hom(S, S, SimplicialComplexes(), check=False)
        sage: H = Hom(S, S, Sets(),                check=False)
        sage: H = Hom(S, S, ChainComplexes(QQ),    check=False)

    Case of a non parent::

        sage: # needs sage.graphs
        sage: cls = type(SimplicialComplex([[1,2], [1,4]]))
        sage: S = unpickle_newobj(cls, ())
        sage: H = Hom(S, S, Sets(),                check=False)
        sage: H = Hom(S, S, Groups(),              check=False)
        sage: H = Hom(S, S, SimplicialComplexes(), check=False)

    Typical example where unpickling involves calling Hom on an
    uninitialized parent::

        sage: P.<x,y> = QQ[\'x,y\']
        sage: Q = P.quotient([x^2 - 1, y^2 - 1])
        sage: q = Q.an_element()                                                        # needs sage.libs.singular
        sage: explain_pickle(dumps(Q))                                                  # needs sage.libs.singular
        pg_...
        ... = pg_dynamic_class(\'QuotientRing_generic_with_category\', (pg_QuotientRing_generic, pg_getattr(..., \'parent_class\')), None, None, pg_QuotientRing_generic)
        si... = unpickle_newobj(..., ())
        ...
        si... = pg_unpickle_MPolynomialRing_libsingular(..., (\'x\', \'y\'), ...)
        si... = ... pg_Hom(si..., si..., ...) ...
        sage: Q == loads(dumps(Q))
        True

    Check that the ``_Hom_`` method of the ``category`` input is used::

        sage: from sage.categories.category_types import Category_over_base_ring
        sage: class ModulesWithHom(Category_over_base_ring):
        ....:     def super_categories(self):
        ....:         return [Modules(self.base_ring())]
        ....:     class ParentMethods:
        ....:         def _Hom_(self, Y, category=None):
        ....:             print("Modules")
        ....:             raise TypeError
        sage: class AlgebrasWithHom(Category_over_base_ring):
        ....:     def super_categories(self):
        ....:         return [Algebras(self.base_ring()), ModulesWithHom(self.base_ring())]
        ....:     class ParentMethods:
        ....:         def _Hom_(self, Y, category=None):
        ....:             R = self.base_ring()
        ....:             if category is not None and category.is_subcategory(Algebras(R)):
        ....:                 print("Algebras")
        ....:             raise TypeError
        sage: from sage.structure.element import Element
        sage: class Foo(Parent):
        ....:     def _coerce_map_from_base_ring(self):
        ....:         return self._generic_coerce_map(self.base_ring())
        ....:     class Element(Element):
        ....:         pass
        sage: X = Foo(base=QQ, category=AlgebrasWithHom(QQ))
        sage: H = Hom(X, X, ModulesWithHom(QQ))
        Modules
    '''
def hom(X, Y, f):
    """
    Return ``Hom(X,Y)(f)``, where ``f`` is data that defines an element of
    ``Hom(X,Y)``.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: phi = hom(R, QQ, [2])
        sage: phi(x^2 + 3)
        7
    """
def End(X, category=None):
    """
    Create the set of endomorphisms of ``X`` in the category category.

    INPUT:

    - ``X`` -- anything

    - ``category`` -- (optional) category in which to coerce ``X``

    OUTPUT: a set of endomorphisms in category

    EXAMPLES::

        sage: V = VectorSpace(QQ, 3)                                                    # needs sage.modules
        sage: End(V)                                                                    # needs sage.modules
        Set of Morphisms (Linear Transformations)
         from Vector space of dimension 3 over Rational Field
         to Vector space of dimension 3 over Rational Field

    ::

        sage: # needs sage.groups
        sage: G = AlternatingGroup(3)
        sage: S = End(G); S
        Set of Morphisms
         from Alternating group of order 3!/2 as a permutation group
         to Alternating group of order 3!/2 as a permutation group
         in Category of finite enumerated permutation groups
        sage: S.domain()
        Alternating group of order 3!/2 as a permutation group

    To avoid creating superfluous categories, a homset in a category
    ``Cs()`` is in the homset category of the lowest full super category
    ``Bs()`` of ``Cs()`` that implements ``Bs.Homsets`` (or the join
    thereof if there are several). For example, finite groups form a
    full subcategory of unital magmas: any unital magma morphism
    between two finite groups is a finite group morphism. Since finite
    groups currently implement nothing more than unital magmas about
    their homsets, we have::

        sage: # needs sage.groups
        sage: G = GL(3, 3)
        sage: G.category()
        Category of finite groups
        sage: H = Hom(G, G)
        sage: H.homset_category()
        Category of finite groups
        sage: H.category()
        Category of endsets of unital magmas

    Similarly, a ring morphism just needs to preserve addition,
    multiplication, zero, and one. Accordingly, and since the category
    of rings implements nothing specific about its homsets, a ring
    homset is currently constructed in the category of homsets of
    unital magmas and unital additive magmas::

        sage: H = Hom(ZZ,ZZ,Rings())
        sage: H.category()
        Category of endsets of unital magmas and additive unital additive magmas
    """
def end(X, f):
    """
    Return ``End(X)(f)``, where ``f`` is data that defines an element of
    ``End(X)``.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: phi = end(R, [x + 1])
        sage: phi
        Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
          Defn: x |--> x + 1
        sage: phi(x^2 + 5)
        x^2 + 2*x + 6
    """

class Homset(Set_generic):
    """
    The class for collections of morphisms in a category.

    EXAMPLES::

        sage: H = Hom(QQ^2, QQ^3)                                                       # needs sage.modules
        sage: loads(H.dumps()) is H                                                     # needs sage.modules
        True

    Homsets of unique parents are unique as well::

        sage: H = End(AffineSpace(2, names='x,y'))
        sage: loads(dumps(AffineSpace(2, names='x,y'))) is AffineSpace(2, names='x,y')
        True
        sage: loads(dumps(H)) is H
        True

    Conversely, homsets of non-unique parents are non-unique::

        sage: P11 = ProductProjectiveSpaces(QQ, [1, 1])
        sage: H = End(P11)
        sage: loads(dumps(P11)) is ProductProjectiveSpaces(QQ, [1, 1])
        False
        sage: loads(dumps(P11)) == ProductProjectiveSpaces(QQ, [1, 1])
        True
        sage: loads(dumps(H)) is H
        False
        sage: loads(dumps(H)) == H
        True
    """
    def __init__(self, X, Y, category=None, base=None, check: bool = True) -> None:
        """
        TESTS::

            sage: X = ZZ['x']; X.rename('X')
            sage: Y = ZZ['y']; Y.rename('Y')
            sage: f = X.hom([0], Y)
            sage: class MyHomset(Homset):
            ....:     def _an_element_(self):
            ....:         return sage.categories.morphism.SetMorphism(self, f)
            sage: import __main__; __main__.MyHomset = MyHomset  # fakes MyHomset being defined in a Python module
            sage: H = MyHomset(X, Y, category=Monoids(), base = ZZ)
            sage: H
            Set of Morphisms from X to Y in Category of monoids
            sage: TestSuite(H).run()

            sage: H = MyHomset(X, Y, category=1, base = ZZ)
            Traceback (most recent call last):
            ...
            TypeError: category (=1) must be a category

            sage: H = MyHomset(X, Y, category=1, base = ZZ, check = False)
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.rings.integer.Integer' object has no attribute 'Homsets'...
            sage: P.<t> = ZZ[]
            sage: f = P.hom([1/2*t])
            sage: f.parent().domain()
            Univariate Polynomial Ring in t over Integer Ring
            sage: f.domain() is f.parent().domain()
            True

        Test that ``base_ring`` is initialized properly::

            sage: R = QQ['x']
            sage: Hom(R, R).base_ring()
            Rational Field
            sage: Hom(R, R, category=Sets()).base_ring()
            sage: Hom(R, R, category=Modules(QQ)).base_ring()
            Rational Field
            sage: Hom(QQ^3, QQ^3, category=Modules(QQ)).base_ring()                     # needs sage.modules
            Rational Field

        For whatever it's worth, the ``base`` arguments takes precedence::

            sage: MyHomset(ZZ^3, ZZ^3, base=QQ).base_ring()                             # needs sage.modules
            Rational Field
        """
    def __reduce__(self):
        """
        Implement pickling by construction for Homsets.

        Homsets are unpickled using the function
        :func:`~sage.categories.homset.Hom` which is cached:
        ``Hom(domain, codomain, category, check=False)``.

        .. NOTE::

            It can happen, that ``Hom(X,X)`` is called during
            unpickling with an uninitialized instance ``X`` of a Python
            class. In some of these cases, testing that ``X in
            category`` can trigger ``X.category()``. This in turn can
            raise a error, or return a too large category (``Sets()``,
            for example) and (worse!) assign this larger category to
            the ``X._category`` cdef attribute, so that it would
            subsequently seem that ``X``'s category was initialised.

            Beside speed considerations, this is the main rationale
            for disabling checks upon unpickling.

            .. SEEALSO:: :issue:`14793`, :issue:`16275`

        EXAMPLES::

            sage: H = Hom(QQ^2, QQ^3)                                                   # needs sage.modules
            sage: H.__reduce__()                                                        # needs sage.modules
            (<function Hom at ...>,
             (Vector space of dimension 2 over Rational Field,
              Vector space of dimension 3 over Rational Field,
              Category of finite dimensional vector spaces with basis over
                 (number fields and quotient fields and metric spaces),
              False))

        TESTS::

            sage: loads(H.dumps()) is H                                                 # needs sage.modules
            True

        Homsets of non-unique parents are non-unique as well::

            sage: # needs sage.groups
            sage: G = PermutationGroup([[(1, 2, 3), (4, 5)], [(3, 4)]])
            sage: G is loads(dumps(G))
            False
            sage: H = Hom(G, G)
            sage: H is loads(dumps(H))
            False
            sage: H == loads(dumps(H))
            True
        """
    def __hash__(self):
        """
        The hash is obtained from domain, codomain and base.

        TESTS::

            sage: hash(Hom(ZZ, QQ)) == hash((ZZ, QQ, ZZ))
            True
            sage: hash(Hom(QQ, ZZ)) == hash((QQ, ZZ, QQ))
            True

            sage: E = EllipticCurve('37a')                                              # needs sage.schemes
            sage: H = E(0).parent(); H                                                  # needs sage.schemes
            Abelian group of points on Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: hash(H) == hash((H.domain(), H.codomain(), H.base()))                 # needs sage.schemes
            True
        """
    def __bool__(self) -> bool:
        """
        TESTS::

            sage: bool(Hom(ZZ, QQ))
            True
        """
    def homset_category(self):
        """
        Return the category that this is a Hom in, i.e., this is typically
        the category of the domain or codomain object.

        EXAMPLES::

            sage: H = Hom(AlternatingGroup(4), AlternatingGroup(7))                     # needs sage.groups
            sage: H.homset_category()                                                   # needs sage.groups
            Category of finite enumerated permutation groups
        """
    @lazy_attribute
    def element_class_set_morphism(self):
        """
        A base class for elements of this homset which are
        also ``SetMorphism``, i.e. implemented by mean of a
        Python function.

        This is currently plain ``SetMorphism``, without inheritance
        from categories.

        .. TODO::

            Refactor during the upcoming homset cleanup.

        EXAMPLES::

            sage: H = Hom(ZZ, ZZ)
            sage: H.element_class_set_morphism
            <class 'sage.categories.morphism.SetMorphism'>
        """
    def __eq__(self, other):
        """
        For two homsets, it is tested whether the domain, the codomain and
        the category coincide.

        EXAMPLES::

            sage: H1 = Hom(ZZ,QQ, CommutativeAdditiveGroups())
            sage: H2 = Hom(ZZ,QQ)
            sage: H1 == H2
            False
            sage: H1 == loads(dumps(H1))
            True
        """
    def __ne__(self, other):
        """
        Check for not-equality of ``self`` and ``other``.

        EXAMPLES::

            sage: H1 = Hom(ZZ,QQ, CommutativeAdditiveGroups())
            sage: H2 = Hom(ZZ,QQ)
            sage: H3 = Hom(ZZ['t'],QQ, CommutativeAdditiveGroups())
            sage: H4 = Hom(ZZ,QQ['t'], CommutativeAdditiveGroups())
            sage: H1 != H2
            True
            sage: H1 != loads(dumps(H1))
            False
            sage: H1 != H3 != H4 != H1
            True
        """
    def __contains__(self, x) -> bool:
        """
        Test whether the parent of the argument is ``self``.

        TESTS::

            sage: P.<t> = ZZ[]
            sage: f = P.hom([1/2*t])
            sage: f in Hom(ZZ['t'],QQ['t'])  # indirect doctest
            True
            sage: f in Hom(ZZ['t'],QQ['t'], CommutativeAdditiveGroups())  # indirect doctest
            False
        """
    def natural_map(self):
        '''
        Return the "natural map" of this homset.

        .. NOTE::

            By default, a formal coercion morphism is returned.

        EXAMPLES::

            sage: H = Hom(ZZ[\'t\'],QQ[\'t\'], CommutativeAdditiveGroups())
            sage: H.natural_map()
            Coercion morphism:
              From: Univariate Polynomial Ring in t over Integer Ring
              To:   Univariate Polynomial Ring in t over Rational Field
            sage: H = Hom(QQ[\'t\'], GF(3)[\'t\'])
            sage: H.natural_map()
            Traceback (most recent call last):
            ...
            TypeError: natural coercion morphism
            from Univariate Polynomial Ring in t over Rational Field
            to Univariate Polynomial Ring in t over Finite Field of size 3 not defined
        '''
    def identity(self):
        """
        The identity map of this homset.

        .. NOTE::

            Of course, this only exists for sets of endomorphisms.

        EXAMPLES::

            sage: H = Hom(QQ,QQ)
            sage: H.identity()
            Identity endomorphism of Rational Field
            sage: H = Hom(ZZ,QQ)
            sage: H.identity()
            Traceback (most recent call last):
            ...
            TypeError: identity map only defined for endomorphisms; try natural_map() instead
            sage: H.natural_map()
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
        """
    def one(self):
        """
        The identity map of this homset.

        .. NOTE::

            Of course, this only exists for sets of endomorphisms.

        EXAMPLES::

            sage: K = GaussianIntegers()                                                # needs sage.rings.number_field
            sage: End(K).one()                                                          # needs sage.rings.number_field
            Identity endomorphism of Gaussian Integers generated by I
             in Number Field in I with defining polynomial x^2 + 1 with I = 1*I
        """
    def domain(self):
        """
        Return the domain of this homset.

        EXAMPLES::

            sage: P.<t> = ZZ[]
            sage: f = P.hom([1/2*t])
            sage: f.parent().domain()
            Univariate Polynomial Ring in t over Integer Ring
            sage: f.domain() is f.parent().domain()
            True
        """
    def codomain(self):
        """
        Return the codomain of this homset.

        EXAMPLES::

            sage: P.<t> = ZZ[]
            sage: f = P.hom([1/2*t])
            sage: f.parent().codomain()
            Univariate Polynomial Ring in t over Rational Field
            sage: f.codomain() is f.parent().codomain()
            True
        """
    def reversed(self):
        """
        Return the corresponding homset, but with the domain and codomain
        reversed.

        EXAMPLES::

            sage: # needs sage.modules
            sage: H = Hom(ZZ^2, ZZ^3); H
            Set of Morphisms from Ambient free module of rank 2 over
             the principal ideal domain Integer Ring to Ambient free module
             of rank 3 over the principal ideal domain Integer Ring in
             Category of finite dimensional modules with basis over (Dedekind
             domains and euclidean domains and noetherian rings
             and infinite enumerated sets and metric spaces)
            sage: type(H)
            <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
            sage: H.reversed()
            Set of Morphisms from Ambient free module of rank 3 over
             the principal ideal domain Integer Ring to Ambient free module
             of rank 2 over the principal ideal domain Integer Ring in
             Category of finite dimensional modules with basis over (Dedekind
             domains and euclidean domains and noetherian rings
             and infinite enumerated sets and metric spaces)
            sage: type(H.reversed())
            <class 'sage.modules.free_module_homspace.FreeModuleHomspace_with_category'>
        """

class HomsetWithBase(Homset):
    def __init__(self, X, Y, category=None, check: bool = True, base=None) -> None:
        """
        TESTS::

            sage: X = ZZ['x']; X.rename('X')
            sage: Y = ZZ['y']; Y.rename('Y')
            sage: f = X.hom([0], Y)
            sage: class MyHomset(HomsetWithBase):
            ....:     def _an_element_(self):
            ....:         return sage.categories.morphism.SetMorphism(self, f)
            sage: import __main__; __main__.MyHomset = MyHomset # fakes MyHomset being defined in a Python module
            sage: H = MyHomset(X, Y, category=Monoids())
            sage: H
            Set of Morphisms from X to Y in Category of monoids
            sage: H.base()
            Integer Ring
            sage: TestSuite(H).run()
        """

def is_Homset(x):
    """
    Return ``True`` if ``x`` is a set of homomorphisms in a category.

    EXAMPLES::

        sage: from sage.categories.homset import is_Homset
        sage: P.<t> = ZZ[]
        sage: f = P.hom([1/2*t])
        sage: is_Homset(f)
        doctest:warning...
        DeprecationWarning: the function is_Homset is deprecated;
        use 'isinstance(..., Homset)' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        False
        sage: is_Homset(f.category())
        False
        sage: is_Homset(f.parent())
        True
    """
def is_Endset(x):
    """
    Return ``True`` if ``x`` is a set of endomorphisms in a category.

    EXAMPLES::

        sage: from sage.categories.homset import is_Endset
        sage: P.<t> = ZZ[]
        sage: f = P.hom([1/2*t])
        sage: is_Endset(f.parent())
        doctest:warning...
        DeprecationWarning: the function is_Endset is deprecated;
        use 'isinstance(..., Homset) and ....is_endomorphism_set()' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        False
        sage: g = P.hom([2*t])
        sage: is_Endset(g.parent())
        True
    """
