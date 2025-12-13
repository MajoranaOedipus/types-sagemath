from _typeshed import Incomplete
from sage.categories.pushout import InfinitePolynomialFunctor as InfinitePolynomialFunctor
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.ring import CommutativeRing as CommutativeRing
from sage.structure.all import SageObject as SageObject, parent as parent
from sage.structure.factory import UniqueFactory as UniqueFactory

class InfinitePolynomialRingFactory(UniqueFactory):
    '''
    A factory for creating infinite polynomial ring elements.  It
    makes sure that they are unique as well as handling pickling.
    For more details, see
    :class:`~sage.structure.factory.UniqueFactory` and
    :mod:`~sage.rings.polynomial.infinite_polynomial_ring`.

    EXAMPLES::

        sage: A.<a> = InfinitePolynomialRing(QQ)
        sage: B.<b> = InfinitePolynomialRing(A)
        sage: B.construction()
        [InfPoly{[a,b], "lex", "dense"}, Rational Field]
        sage: R.<a,b> = InfinitePolynomialRing(QQ)
        sage: R is B
        True
        sage: X.<x> = InfinitePolynomialRing(QQ)
        sage: X2.<x> = InfinitePolynomialRing(QQ, implementation=\'sparse\')
        sage: X is X2
        False

        sage: X is loads(dumps(X))
        True
    '''
    def create_key(self, R, names=('x',), order: str = 'lex', implementation: str = 'dense'):
        '''
        Create a key which uniquely defines the infinite polynomial ring.

        TESTS::

            sage: InfinitePolynomialRing.create_key(QQ, (\'y1\',))
            (InfPoly{[y1], "lex", "dense"}(FractionField(...)), Integer Ring)
            sage: _[0].all
            [FractionField, InfPoly{[y1], "lex", "dense"}]
            sage: InfinitePolynomialRing.create_key(QQ, names=[\'beta\'], order=\'deglex\',
            ....:                                   implementation=\'sparse\')
            (InfPoly{[beta], "deglex", "sparse"}(FractionField(...)), Integer Ring)
            sage: _[0].all
            [FractionField, InfPoly{[beta], "deglex", "sparse"}]
            sage: InfinitePolynomialRing.create_key(QQ, names=[\'x\',\'y\'],
            ....:                                   implementation=\'dense\')
            (InfPoly{[x,y], "lex", "dense"}(FractionField(...)), Integer Ring)
            sage: _[0].all
            [FractionField, InfPoly{[x,y], "lex", "dense"}]

        If no generator name is provided, a generator named \'x\',
        lexicographic order and the dense implementation are assumed::

            sage: InfinitePolynomialRing.create_key(QQ)
            (InfPoly{[x], "lex", "dense"}(FractionField(...)), Integer Ring)
            sage: _[0].all
            [FractionField, InfPoly{[x], "lex", "dense"}]

        If it is attempted to use no generator, a :exc:`ValueError` is raised::

            sage: InfinitePolynomialRing.create_key(ZZ, names=[])
            Traceback (most recent call last):
            ...
            ValueError: Infinite Polynomial Rings must have at least one generator
        '''
    def create_object(self, version, key):
        """
        Return the infinite polynomial ring corresponding to the key ``key``.

        TESTS::

            sage: InfinitePolynomialRing.create_object('1.0', InfinitePolynomialRing.create_key(ZZ, ('x3',)))
            Infinite polynomial ring in x3 over Integer Ring
        """

InfinitePolynomialRing: Incomplete

class InfiniteGenDict:
    """
    A dictionary-like class that is suitable for usage in ``sage_eval``.

    The generators of an Infinite Polynomial Ring are not
    variables. Variables of an Infinite Polynomial Ring are returned
    by indexing a generator. The purpose of this class is to return a
    variable of an Infinite Polynomial Ring, given its string
    representation.

    EXAMPLES::

        sage: R.<a,b> = InfinitePolynomialRing(ZZ)
        sage: D = R.gens_dict() # indirect doctest
        sage: D._D
        [InfiniteGenDict defined by ['a', 'b'], {'1': 1}]
        sage: D._D[0]['a_15']
        a_15
        sage: type(_)
        <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
        sage: sage_eval('3*a_3*b_5-1/2*a_7', D._D[0])
        -1/2*a_7 + 3*a_3*b_5
    """
    def __init__(self, Gens) -> None:
        """
        INPUT:

        - ``Gens`` -- list of generators of an infinite polynomial ring

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D._D
            [InfiniteGenDict defined by ['a', 'b'], {'1': 1}]
            sage: D._D == loads(dumps(D._D)) # indirect doctest
            True
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D._D
            [InfiniteGenDict defined by ['a', 'b'], {'1': 1}]
            sage: D._D == loads(dumps(D._D)) # indirect doctest
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D._D
            [InfiniteGenDict defined by ['a', 'b'], {'1': 1}]
            sage: D._D != loads(dumps(D._D)) # indirect doctest
            False
        """
    def __getitem__(self, k):
        """
        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D._D
            [InfiniteGenDict defined by ['a', 'b'], {'1': 1}]
            sage: D._D[0]['a_15']
            a_15
            sage: type(_)
            <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
        """

class GenDictWithBasering:
    """
    A dictionary-like class that is suitable for usage in ``sage_eval``.

    This pseudo-dictionary accepts strings as index, and then walks down
    a chain of base rings of (infinite) polynomial rings until it finds
    one ring that has the given string as variable name, which is then
    returned.

    EXAMPLES::

        sage: R.<a,b> = InfinitePolynomialRing(ZZ)
        sage: D = R.gens_dict() # indirect doctest
        sage: D
        GenDict of Infinite polynomial ring in a, b over Integer Ring
        sage: D['a_15']
        a_15
        sage: type(_)
        <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
        sage: sage_eval('3*a_3*b_5-1/2*a_7', D)
        -1/2*a_7 + 3*a_3*b_5
    """
    def __init__(self, parent, start) -> None:
        """
        INPUT:

        - ``parent`` -- a ring
        - ``start`` -- some dictionary, usually the dictionary of variables of ``parent``

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D
            GenDict of Infinite polynomial ring in a, b over Integer Ring
            sage: D['a_15']
            a_15
            sage: type(_)
            <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
            sage: sage_eval('3*a_3*b_5-1/2*a_7', D)
            -1/2*a_7 + 3*a_3*b_5

        TESTS::

            sage: from sage.rings.polynomial.infinite_polynomial_ring import GenDictWithBasering
            sage: R = ZZ['x']['y']['a','b']['c']
            sage: D = GenDictWithBasering(R,R.gens_dict())
            sage: R.gens_dict()['a']
            Traceback (most recent call last):
            ...
            KeyError: 'a'
            sage: D['a']
            a
        """
    def __next__(self):
        """
        Return a dictionary that can be used to interpret strings in the base ring of ``self``.

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(QQ['t'])
            sage: D = R.gens_dict()
            sage: D
            GenDict of Infinite polynomial ring in a, b over Univariate Polynomial Ring in t over Rational Field
            sage: next(D)
            GenDict of Univariate Polynomial Ring in t over Rational Field
            sage: sage_eval('t^2', next(D))
            t^2
        """
    next = __next__
    def __getitem__(self, k):
        """
        TESTS::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: D = R.gens_dict() # indirect doctest
            sage: D
            GenDict of Infinite polynomial ring in a, b over Integer Ring
            sage: D['a_15']
            a_15
            sage: type(_)
            <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
        """

class InfinitePolynomialRing_sparse(CommutativeRing):
    """
    Sparse implementation of Infinite Polynomial Rings.

    An Infinite Polynomial Ring with generators `x_\\ast, y_\\ast,
    ...` over a field `F` is a free commutative `F`-algebra generated
    by `x_0, x_1, x_2, ..., y_0, y_1, y_2, ..., ...` and is equipped
    with a permutation action on the generators, namely `x_n^P =
    x_{P(n)}, y_{n}^P=y_{P(n)}, ...` for any permutation `P` (note
    that variables of index zero are invariant under such
    permutation).

    It is known that any permutation invariant ideal in an Infinite
    Polynomial Ring is finitely generated modulo the permutation
    action -- see :class:`~sage.rings.polynomial.symmetric_ideal.SymmetricIdeal`
    for more details.

    Usually, an instance of this class is created using
    ``InfinitePolynomialRing`` with the optional parameter
    ``implementation='sparse'``. This takes care of uniqueness of
    parent structures. However, a direct construction is possible, in
    principle::

        sage: X.<x,y> = InfinitePolynomialRing(QQ, implementation='sparse')
        sage: Y.<x,y> = InfinitePolynomialRing(QQ, implementation='sparse')
        sage: X is Y
        True
        sage: from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing_sparse
        sage: Z = InfinitePolynomialRing_sparse(QQ, ['x','y'], 'lex')

    Nevertheless, since infinite polynomial rings are supposed to be unique
    parent structures, they do not evaluate equal. ::

        sage: Z == X
        False

    The last parameter ('lex' in the above example) can also be
    'deglex' or 'degrevlex'; this would result in an Infinite
    Polynomial Ring in degree lexicographic or degree reverse
    lexicographic order.

    See :mod:`~sage.rings.polynomial.infinite_polynomial_ring` for
    more details.
    """
    def __init__(self, R, names, order) -> None:
        """
        INPUT:

        - ``R`` -- base ring
        - ``names`` -- list of generator names
        - ``order`` -- string determining the monomial order of the infinite polynomial ring

        EXAMPLES::

            sage: X.<alpha,beta> = InfinitePolynomialRing(ZZ, implementation='sparse')

        Infinite Polynomial Rings are unique parent structures::

            sage: X is loads(dumps(X))
            True
            sage: p=alpha[10]*beta[2]^3+2*alpha[1]*beta[3]
            sage: p
            alpha_10*beta_2^3 + 2*alpha_1*beta_3

        We define another Infinite Polynomial Ring with same generator
        names but a different order. These rings are different, but
        allow for coercion::

            sage: Y.<alpha,beta> = InfinitePolynomialRing(QQ, order='deglex', implementation='sparse')
            sage: Y is X
            False
            sage: q=beta[2]^3*alpha[10]+beta[3]*alpha[1]*2
            sage: q
            alpha_10*beta_2^3 + 2*alpha_1*beta_3
            sage: p==q
            True
            sage: X.gen(1)[2]*Y.gen(0)[1]
            alpha_1*beta_2
        """
    @cached_method
    def one(self):
        """
        TESTS::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: X.one()
            1
        """
    def construction(self):
        '''
        Return the construction of ``self``.

        OUTPUT:

        A pair ``F,R``, where ``F`` is a construction functor and ``R`` is a ring,
        so that ``F(R) is self``.

        EXAMPLES::

            sage: R.<x,y> = InfinitePolynomialRing(GF(5))
            sage: R.construction()
            [InfPoly{[x,y], "lex", "dense"}, Finite Field of size 5]
        '''
    def tensor_with_ring(self, R):
        """
        Return the tensor product of ``self`` with another ring.

        INPUT:

        - ``R`` -- a ring

        OUTPUT:

        An infinite polynomial ring that, mathematically, can be seen as the
        tensor product of ``self`` with ``R``.

        NOTE:

        It is required that the underlying ring of ``self`` coerces into ``R``.
        Hence, the tensor product is in fact merely an extension of the base
        ring.

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ)
            sage: R.tensor_with_ring(QQ)
            Infinite polynomial ring in a, b over Rational Field
            sage: R
            Infinite polynomial ring in a, b over Integer Ring

        The following tests against a bug that was fixed at :issue:`10468`::

            sage: R.<x,y> = InfinitePolynomialRing(QQ)
            sage: R.tensor_with_ring(QQ) is R
            True
        """
    def is_noetherian(self):
        """
        Return ``False``, since polynomial rings in infinitely many
        variables are never Noetherian rings.

        Since Infinite Polynomial Rings must have at least one
        generator, they have infinitely many variables and are thus
        not Noetherian, as a ring.

        .. NOTE::

            Infinite Polynomial Rings over a field `F` are Noetherian as
            `F(G)` modules, where `G` is the symmetric group of the
            natural numbers. But this is not what the method
            ``is_noetherian()`` is answering.

        TESTS::

            sage: R = InfinitePolynomialRing(GF(2))
            sage: R
            Infinite polynomial ring in x over Finite Field of size 2
            sage: R.is_noetherian()
            False

            sage: R.<x> = InfinitePolynomialRing(QQ)
            sage: R.is_noetherian()
            False
        """
    def is_field(self, *args, **kwds):
        """
        Return ``False`` since Infinite Polynomial Rings are never fields.

        Since Infinite Polynomial Rings must have at least one generator,
        they have infinitely many variables and thus never are fields.

        EXAMPLES::

            sage: R.<x, y> = InfinitePolynomialRing(QQ)
            sage: R.is_field()
            False

        TESTS::

            sage: R = InfinitePolynomialRing(GF(2))
            sage: R
            Infinite polynomial ring in x over Finite Field of size 2
            sage: R.is_field()
            False

        :issue:`9443`::

            sage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')
            sage: W.is_field()
            False
        """
    def varname_key(self, x):
        """
        Key for comparison of variable names.

        INPUT:

        - ``x`` -- string of the form ``a+'_'+str(n)``, where a is the
          name of a generator, and n is an integer

        OUTPUT: a key used to sort the variables

        THEORY:

        The order is defined as follows:

        x<y `\\iff` the string ``x.split('_')[0]`` is later in the list of
        generator names of ``self`` than ``y.split('_')[0]``, or
        (``x.split('_')[0]==y.split('_')[0]`` and
        ``int(x.split('_')[1])<int(y.split('_')[1])``)

        EXAMPLES::

            sage: X.<alpha,beta> = InfinitePolynomialRing(ZZ)
            sage: X.varname_key('alpha_1')
            (0, 1)
            sage: X.varname_key('beta_10')
            (-1, 10)
            sage: X.varname_key('beta_1')
            (-1, 1)
            sage: X.varname_key('alpha_10')
            (0, 10)
            sage: X.varname_key('alpha_1')
            (0, 1)
            sage: X.varname_key('alpha_10')
            (0, 10)
        """
    def ngens(self):
        """
        Return the number of generators for this ring.

        Since there
        are countably infinitely many variables in this polynomial
        ring, by 'generators' we mean the number of infinite families
        of variables. See :mod:`~sage.rings.polynomial.infinite_polynomial_ring`
        for more details.

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(ZZ)
            sage: X.ngens()
            1

            sage: X.<x1,x2> = InfinitePolynomialRing(QQ)
            sage: X.ngens()
            2
        """
    @cached_method
    def gen(self, i=None):
        """
        Return the `i`-th 'generator' (see the description in :meth:`.ngens`)
        of this infinite polynomial ring.

        EXAMPLES::

            sage: X = InfinitePolynomialRing(QQ)
            sage: x = X.gen()
            sage: x[1]
            x_1
            sage: X.gen() is X.gen(0)
            True
            sage: XX = InfinitePolynomialRing(GF(5))
            sage: XX.gen(0) is XX.gen()
            True
        """
    @cached_method
    def gens_dict(self) -> GenDictWithBasering:
        """
        Return a dictionary-like object containing the infinitely many
        ``{var_name:variable}`` pairs.

        EXAMPLES::

            sage: R = InfinitePolynomialRing(ZZ, 'a')
            sage: D = R.gens_dict()
            sage: D
            GenDict of Infinite polynomial ring in a over Integer Ring
            sage: D['a_5']
            a_5
        """
    def characteristic(self):
        """
        Return the characteristic of the base field.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(GF(25,'a'))                          # needs sage.rings.finite_rings
            sage: X                                                                     # needs sage.rings.finite_rings
            Infinite polynomial ring in x, y over Finite Field in a of size 5^2
            sage: X.characteristic()                                                    # needs sage.rings.finite_rings
            5
        """
    def is_integral_domain(self, *args, **kwds):
        """
        An infinite polynomial ring is an integral domain if and only if
        the base ring is.  Arguments are passed to is_integral_domain
        method of base ring.

        EXAMPLES::

            sage: R.<x, y> = InfinitePolynomialRing(QQ)
            sage: R.is_integral_domain()
            True

        TESTS:

        :issue:`9443`::

            sage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')
            sage: W.is_integral_domain()
            True
        """
    def krull_dimension(self, *args, **kwds):
        """
        Return ``Infinity``, since polynomial rings in infinitely many
        variables have infinite Krull dimension.

        EXAMPLES::

            sage: R.<x, y> = InfinitePolynomialRing(QQ)
            sage: R.krull_dimension()
            +Infinity
        """
    def order(self):
        """
        Return ``Infinity``, since polynomial rings have infinitely
        many elements.

        EXAMPLES::

            sage: R.<x> = InfinitePolynomialRing(GF(2))
            sage: R.order()
            +Infinity
        """
    def key_basis(self):
        """
        Return the basis of ``self`` given by key polynomials.

        EXAMPLES::

            sage: R.<x> = InfinitePolynomialRing(GF(2))
            sage: R.key_basis()                                                         # needs sage.combinat sage.modules
            Key polynomial basis over Finite Field of size 2
        """

class InfinitePolynomialGen(SageObject):
    """
    This class provides the object which is responsible for returning
    variables in an infinite polynomial ring (implemented in
    :meth:`.__getitem__`).

    EXAMPLES::

        sage: X.<x1,x2> = InfinitePolynomialRing(RR)
        sage: x1
        x1_*
        sage: x1[5]
        x1_5
        sage: x1 == loads(dumps(x1))
        True
    """
    def __init__(self, parent, name) -> None:
        """
        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: loads(dumps(x))
            x_*
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialGen
            sage: x2 = InfinitePolynomialGen(X, 'x')
            sage: x2 == x
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialGen
            sage: x2 = InfinitePolynomialGen(X, 'x')
            sage: x2 != x
            False
        """
    def __getitem__(self, i):
        """
        Return the variable ``x[i]`` where ``x`` is this
        :class:`sage.rings.polynomial.infinite_polynomial_ring.InfinitePolynomialGen`,
        and i is a nonnegative integer.

        EXAMPLES::

            sage: X.<alpha> = InfinitePolynomialRing(QQ)
            sage: alpha[1]
            alpha_1
        """

class InfinitePolynomialRing_dense(InfinitePolynomialRing_sparse):
    """
    Dense implementation of Infinite Polynomial Rings.

    Compared with :class:`~sage.rings.polynomial.infinite_polynomial_ring.InfinitePolynomialRing_sparse`,
    from which this class inherits, it keeps a polynomial ring that comprises all elements that have
    been created so far.
    """
    def __init__(self, R, names, order) -> None:
        """
        EXAMPLES::

            sage: X.<x2,alpha,y4> = InfinitePolynomialRing(ZZ, implementation='dense')
            sage: X == loads(dumps(X))
            True
        """
    def construction(self):
        '''
        Return the construction of ``self``.

        OUTPUT:

        A pair ``F,R``, where ``F`` is a construction functor and ``R`` is a ring,
        so that ``F(R) is self``.

        EXAMPLES::

            sage: R.<x,y> = InfinitePolynomialRing(GF(5))
            sage: R.construction()
            [InfPoly{[x,y], "lex", "dense"}, Finite Field of size 5]
        '''
    def tensor_with_ring(self, R):
        """
        Return the tensor product of ``self`` with another ring.

        INPUT:

        - ``R`` -- a ring

        OUTPUT:

        An infinite polynomial ring that, mathematically, can be seen as the
        tensor product of ``self`` with ``R``.

        NOTE:

        It is required that the underlying ring of ``self`` coerces into ``R``.
        Hence, the tensor product is in fact merely an extension of the base
        ring.

        EXAMPLES::

            sage: R.<a,b> = InfinitePolynomialRing(ZZ, implementation='sparse')
            sage: R.tensor_with_ring(QQ)
            Infinite polynomial ring in a, b over Rational Field
            sage: R
            Infinite polynomial ring in a, b over Integer Ring

        The following tests against a bug that was fixed at :issue:`10468`::

            sage: R.<x,y> = InfinitePolynomialRing(QQ, implementation='sparse')
            sage: R.tensor_with_ring(QQ) is R
            True
        """
    def polynomial_ring(self):
        """
        Return the underlying *finite* polynomial ring.

        .. NOTE::

           The ring returned can change over time as more variables
           are used.

           Since the rings are cached, we create here a ring with variable
           names that do not occur in other doc tests, so that we avoid
           side effects.

        EXAMPLES::

            sage: X.<xx, yy> = InfinitePolynomialRing(ZZ)
            sage: X.polynomial_ring()
            Multivariate Polynomial Ring in xx_0, yy_0 over Integer Ring
            sage: a = yy[3]
            sage: X.polynomial_ring()
            Multivariate Polynomial Ring in xx_3, xx_2, xx_1, xx_0, yy_3, yy_2, yy_1, yy_0
             over Integer Ring
        """
