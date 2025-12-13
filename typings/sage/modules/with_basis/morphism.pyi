from _typeshed import Incomplete
from sage.categories.commutative_additive_semigroups import CommutativeAdditiveSemigroups as CommutativeAdditiveSemigroups
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.categories.modules import Modules as Modules
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.morphism import Morphism as Morphism, SetMorphism as SetMorphism
from sage.categories.sets_cat import Sets as Sets
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps as SetsWithPartialMaps
from sage.misc.c3_controlled import identity as identity
from sage.misc.call import attrcall as attrcall
from sage.structure.element import Matrix as Matrix
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE
from sage.structure.sage_object import SageObject as SageObject

class ModuleMorphism(Morphism):
    """
    The top abstract base class for module with basis morphisms.

    INPUT:

    - ``domain`` -- a parent in ``ModulesWithBasis(...)``
    - ``codomain`` -- a parent in ``Modules(...)``
    - ``category`` -- a category or ``None`` (default: ``None``)
    - ``affine`` -- whether we define an affine module morphism
      (default: ``False``)

    Construct a module morphism from ``domain`` to ``codomain`` in the
    category ``category``. By default, the category is the first of
    ``Modules(R).WithBasis().FiniteDimensional()``,
    ``Modules(R).WithBasis()``, ``Modules(R)``,
    ``CommutativeAdditiveMonoids()`` that contains both the domain and
    the codomain. If initializing an affine morphism, then `Sets()` is
    used instead.

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismFromFunction` and
          :class:`TriangularModuleMorphism`.

    The role of this class is minimal: it provides an :meth:`__init__`
    method which:

    - handles the choice of the default category
    - handles the proper inheritance from categories by updating the
      class of ``self`` upon construction.
    """
    __class__: Incomplete
    def __init__(self, domain, codomain=None, category=None, affine: bool = False) -> None:
        """
        Initialization of module morphisms.

        TESTS::

            sage: X = CombinatorialFreeModule(ZZ, [-2, -1, 1, 2])
            sage: Y = CombinatorialFreeModule(ZZ, [1, 2])
            sage: from sage.modules.with_basis.morphism import ModuleMorphismByLinearity
            sage: phi = ModuleMorphismByLinearity(X, on_basis=Y.monomial * abs)
            sage: TestSuite(phi).run()
        """

class ModuleMorphismFromFunction(ModuleMorphism, SetMorphism):
    """
    A class for module morphisms implemented by a plain function.

    INPUT:

    - ``domain``, ``codomain``, ``category`` -- as for :class:`ModuleMorphism`

    - ``function`` -- any function or callable from domain to codomain

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismFromFunction` and
          :class:`TriangularModuleMorphism`.
    """
    def __init__(self, domain, function, codomain=None, category=None) -> None:
        """
        TESTS::

            sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); X.rename('X'); x = X.basis()
            sage: from sage.modules.with_basis.morphism import ModuleMorphismFromFunction
            sage: def f(x): return 3*x
            sage: import __main__; __main__.f = f  # Fake f being defined in a python module
            sage: phi = ModuleMorphismFromFunction(X, f, codomain=X)
            sage: phi(x[1])
            3*B[1]
            sage: TestSuite(phi).run()
        """

class ModuleMorphismByLinearity(ModuleMorphism):
    """
    A class for module morphisms obtained by extending a function by linearity.

    INPUT:

    - ``domain``, ``codomain``, ``category`` -- as for :class:`ModuleMorphism`
    - ``on_basis`` -- a function which accepts indices of the basis of
      ``domain`` as ``position``-th argument
    - ``codomain`` -- a parent in ``Modules(...)``
        (default: ``on_basis.codomain()``)
    - ``position`` -- nonnegative integer (default: 0)
    - ``zero`` -- the zero of the codomain (defaults: ``codomain.zero()``)

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismFromFunction` and
          :class:`TriangularModuleMorphism`.

    .. NOTE::

        ``on_basis`` may alternatively be provided in derived classes
        by passing ``None`` as argument, and implementing or setting
        the attribute ``_on_basis``
    """
    def __init__(self, domain, on_basis=None, codomain=None, category=None, position: int = 0, zero=None) -> None:
        """
        TESTS::

            sage: X = CombinatorialFreeModule(ZZ, [-2, -1, 1, 2])
            sage: Y = CombinatorialFreeModule(ZZ, [1, 2])
            sage: from sage.modules.with_basis.morphism import ModuleMorphismByLinearity
            sage: phi = ModuleMorphismByLinearity(X, on_basis=Y.monomial * abs)

            sage: TestSuite(phi).run()
        """
    def on_basis(self):
        """
        Return the action of this morphism on basis elements, as per
        :meth:`ModulesWithBasis.Homsets.ElementMethods.on_basis`.

        OUTPUT:

        - a function from the indices of the basis of the domain to the
          codomain

        EXAMPLES::

            sage: X = CombinatorialFreeModule(ZZ, [-2, -1, 1, 2])
            sage: Y = CombinatorialFreeModule(ZZ, [1, 2])
            sage: phi_on_basis = Y.monomial * abs
            sage: phi = sage.modules.with_basis.morphism.ModuleMorphismByLinearity(X, on_basis = phi_on_basis, codomain=Y)
            sage: x = X.basis()
            sage: phi.on_basis()(-2)
            B[2]
            sage: phi.on_basis() == phi_on_basis
            True
        """
    def __call__(self, *args):
        """
        Apply this morphism to ``*args``.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(ZZ, [-2, -1, 1, 2])
            sage: Y = CombinatorialFreeModule(ZZ, [1, 2])
            sage: def phi_on_basis(i): return Y.monomial(abs(i))
            sage: phi = sage.modules.with_basis.morphism.ModuleMorphismByLinearity(X, on_basis = Y.monomial * abs, codomain=Y)
            sage: x = X.basis()
            sage: phi(x[1]), phi(x[-2]), phi(x[1] + 3 * x[-2])
            (B[1], B[2], B[1] + 3*B[2])

        .. TODO::

            Add more tests for multi-parameter module morphisms.
        """

class TriangularModuleMorphism(ModuleMorphism):
    '''
    An abstract class for triangular module morphisms.

    Let `X` and `Y` be modules over the same base ring, with
    distinguished bases `F` indexed by `I` and `G` indexed by `J`,
    respectively.

    A module morphism `\\phi` from `X` to `Y` is *triangular* if its
    representing matrix in the distinguished bases of `X` and `Y` is
    upper triangular (echelon form).

    More precisely, `\\phi` is *upper triangular* w.r.t. a total order
    `<` on `J` if, for any `j\\in J`, there exists at most one index
    `i\\in I` such that the leading support of `\\phi(F_i)` is `j` (see
    :meth:`leading_support()`). We denote by `r(j)` this index,
    setting `r(j)` to ``None`` if it does not exist.

    *Lower triangular* morphisms are defined similarly, taking the
    trailing support instead (see :meth:`trailing_support()`).

    A triangular morphism is *unitriangular* if all its pivots
    (i.e. coefficient of `j` in each `\\phi(F[r(j)])`) are `1`.

    INPUT:

    - ``domain`` -- a module with basis `X`
    - ``codomain`` -- a module with basis `Y` (default: `X`)
    - ``category`` -- a category, as for :class:`ModuleMorphism`

    - ``triangular`` -- ``\'upper\'`` or ``\'lower\'`` (default: ``\'upper\'``)
    - ``unitriangular`` -- boolean (default: ``False``)
      As a shorthand, one may use ``unitriangular=\'lower\'``
      for ``triangular=\'lower\', unitriangular=True``.

    - ``key`` -- a comparison key on `J`
      (default: the usual comparison of elements of `J`)

    - ``inverse_on_support`` -- a function `J \\to I\\cup \\{None\\}`
      implementing `r` (default: the identity function).
      If set to "compute", the values of `r(j)` are precomputed by
      running through the index set `I` of the basis of the
      domain. This of course requires the domain to be finite
      dimensional.

    - ``invertible`` -- boolean or ``None`` (default: ``None``); can
      be set to specify that `\\phi` is known to be (or not to be)
      invertible. If the domain and codomain share the same indexing
      set, this is by default automatically set to ``True`` if
      ``inverse_on_support`` is the identity, or in the finite
      dimensional case.

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismFromFunction` and
          :class:`TriangularModuleMorphism`.

    OUTPUT: a morphism from `X` to `Y`

    .. WARNING::

        This class is meant to be used as a complement for a concrete
        morphism class.  In particular, the :meth:`__init__` method
        focuses on setting up the data structure describing the
        triangularity of the morphism. It purposely does *not* call
        :meth:`ModuleMorphism.__init__` which should be called
        (directly or indirectly) beforehand.

    EXAMPLES:

    We construct and invert an upper unitriangular module morphism between
    two free `\\QQ`-modules::

        sage: I = range(1,200)
        sage: X = CombinatorialFreeModule(QQ, I); X.rename(\'X\'); x = X.basis()
        sage: Y = CombinatorialFreeModule(QQ, I); Y.rename(\'Y\'); y = Y.basis()
        sage: ut = Y.sum_of_monomials * divisors   # This * is map composition.
        sage: phi = X.module_morphism(ut, unitriangular=\'upper\', codomain=Y)
        sage: phi(x[2])
        B[1] + B[2]
        sage: phi(x[6])
        B[1] + B[2] + B[3] + B[6]
        sage: phi(x[30])
        B[1] + B[2] + B[3] + B[5] + B[6] + B[10] + B[15] + B[30]
        sage: phi.preimage(y[2])
        -B[1] + B[2]
        sage: phi.preimage(y[6])
        B[1] - B[2] - B[3] + B[6]
        sage: phi.preimage(y[30])
        -B[1] + B[2] + B[3] + B[5] - B[6] - B[10] - B[15] + B[30]
        sage: (phi^-1)(y[30])
        -B[1] + B[2] + B[3] + B[5] - B[6] - B[10] - B[15] + B[30]

    A lower triangular (but not unitriangular) morphism::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\'); x = X.basis()
        sage: def lt(i): return sum(j*x[j] for j in range(i, 4))
        sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X)
        sage: phi(x[2])
        2*B[2] + 3*B[3]
        sage: phi.preimage(x[2])
        1/2*B[2] - 1/2*B[3]
        sage: phi(phi.preimage(x[2]))
        B[2]

    Using the ``key`` keyword, we can use triangularity even if
    the map becomes triangular only after a permutation of the basis::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\'); x = X.basis()
        sage: def ut(i): return (x[1] + x[2] if i == 1 else x[2] + (x[3] if i == 3 else 0))
        sage: perm = [0, 2, 1, 3]
        sage: phi = X.module_morphism(ut, triangular=\'upper\', codomain=X,
        ....:                         key=lambda a: perm[a])
        sage: [phi(x[i]) for i in range(1, 4)]
        [B[1] + B[2], B[2], B[2] + B[3]]
        sage: [phi.preimage(x[i]) for i in range(1, 4)]
        [B[1] - B[2], B[2], -B[2] + B[3]]

    The same works in the lower-triangular case::

        sage: def lt(i): return (x[1] + x[2] + x[3] if i == 2 else x[i])
        sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X,
        ....:                         key=lambda a: perm[a])
        sage: [phi(x[i]) for i in range(1, 4)]
        [B[1], B[1] + B[2] + B[3], B[3]]
        sage: [phi.preimage(x[i]) for i in range(1, 4)]
        [B[1], -B[1] + B[2] - B[3], B[3]]

    An injective but not surjective morphism cannot be inverted,
    but the ``inverse_on_support`` keyword allows Sage to find a
    partial inverse::

        sage: X = CombinatorialFreeModule(QQ, [1,2,3]); x = X.basis()
        sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4,5]); y = Y.basis()
        sage: ult = lambda i: sum(  y[j] for j in range(i+1,6)  )
        sage: phi = X.module_morphism(ult, unitriangular=\'lower\', codomain=Y,
        ....:        inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
        sage: phi(x[2])
        B[3] + B[4] + B[5]
        sage: phi.preimage(y[3])
        B[2] - B[3]

    The ``inverse_on_support`` keyword can also be used if the
    bases of the domain and the codomain are identical but one of
    them has to be permuted in order to render the morphism
    triangular. For example::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\'); x = X.basis()
        sage: def ut(i):
        ....:     return (x[3] if i == 1 else x[1] if i == 2
        ....:             else x[1] + x[2])
        sage: def perm(i):
        ....:     return (2 if i == 1 else 3 if i == 2 else 1)
        sage: phi = X.module_morphism(ut, triangular=\'upper\', codomain=X,
        ....:                         inverse_on_support=perm)
        sage: [phi(x[i]) for i in range(1, 4)]
        [B[3], B[1], B[1] + B[2]]
        sage: [phi.preimage(x[i]) for i in range(1, 4)]
        [B[2], -B[2] + B[3], B[1]]

    The same works if the permutation induces lower triangularity::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\'); x = X.basis()
        sage: def lt(i):
        ....:     return (x[3] if i == 1 else x[2] if i == 2
        ....:             else x[1] + x[2])
        sage: def perm(i):
        ....:     return 4 - i
        sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X,
        ....:                         inverse_on_support=perm)
        sage: [phi(x[i]) for i in range(1, 4)]
        [B[3], B[2], B[1] + B[2]]
        sage: [phi.preimage(x[i]) for i in range(1, 4)]
        [-B[2] + B[3], B[2], B[1]]

    In the finite dimensional case, one can ask Sage to recover
    ``inverse_on_support`` by a precomputation::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); x = X.basis()
        sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3, 4]); y = Y.basis()
        sage: ut = lambda i: sum(  y[j] for j in range(1,i+2) )
        sage: phi = X.module_morphism(ut, triangular=\'upper\', codomain=Y,
        ....:                         inverse_on_support=\'compute\')
        sage: tx = "{} {} {}"
        sage: for j in Y.basis().keys():
        ....:     i = phi._inverse_on_support(j)
        ....:     print(tx.format(j, i, phi(x[i]) if i is not None else None))
        1 None None
        2 1 B[1] + B[2]
        3 2 B[1] + B[2] + B[3]
        4 3 B[1] + B[2] + B[3] + B[4]

    The ``inverse_on_basis`` and ``key`` keywords can be combined::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\')
        sage: x = X.basis()
        sage: def ut(i):
        ....:     return (2*x[2] + 3*x[3] if i == 1
        ....:             else x[1] + x[2] + x[3] if i == 2
        ....:             else 4*x[2])
        sage: def perm(i):
        ....:     return (2 if i == 1 else 3 if i == 2 else 1)
        sage: perverse_key = lambda a: (a - 2) % 3
        sage: phi = X.module_morphism(ut, triangular=\'upper\', codomain=X,
        ....:                         inverse_on_support=perm, key=perverse_key)
        sage: [phi(x[i]) for i in range(1, 4)]
        [2*B[2] + 3*B[3], B[1] + B[2] + B[3], 4*B[2]]
        sage: [phi.preimage(x[i]) for i in range(1, 4)]
        [-1/3*B[1] + B[2] - 1/12*B[3], 1/4*B[3], 1/3*B[1] - 1/6*B[3]]
    '''
    def __init__(self, triangular: str = 'upper', unitriangular: bool = False, key=None, inverse=None, inverse_on_support=..., invertible=None) -> None:
        '''
        TESTS::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename(\'X\'); x = X.basis()
            sage: def lt(i): return sum(j*x[j] for j in range(i, 4))
            sage: import __main__; __main__.lt = lt  # Fake lt being defined in a python module
            sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X)
            sage: phi.__class__
            <class \'sage.modules.with_basis.morphism.TriangularModuleMorphismByLinearity_with_category\'>
            sage: phi._invertible
            True
            sage: TestSuite(phi).run()

        With the option ``compute``::

            sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X,
            ....:                         inverse_on_support=\'compute\')
            sage: TestSuite(phi).run(skip=["_test_pickling"])

        Pickling works in Python3 (:issue:`17957`)::

            sage: phi = X.module_morphism(lt, triangular=\'lower\', codomain=X,
            ....:                         inverse_on_support=\'compute\')
            sage: loads(dumps(phi))
            Generic endomorphism of X
            sage: phi._inverse_on_support
            <built-in method get of dict object at ...>
            sage: ldp = loads(dumps(phi._inverse_on_support))
            sage: [ldp(i) == phi._inverse_on_support(i) for i in range(1, 4)]
            [True, True, True]
        '''
    def __invert__(self):
        """
        Return the triangular morphism which is the inverse of ``self``.

        Raises an error if ``self`` is not invertible.

        TESTS::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3]); y = Y.basis()
            sage: uut = lambda i: sum(  y[j] for j in range(1,i+1)) # uni-upper
            sage: ult = lambda i: sum(  y[j] for j in range(i,4)  ) # uni-lower
            sage: ut =  lambda i: sum(j*y[j] for j in range(1,i+1)) # upper
            sage: lt =  lambda i: sum(j*y[j] for j in range(i,4  )) # lower
            sage: f_uut = X.module_morphism(uut, codomain=Y,
            ....:                           unitriangular='upper')
            sage: f_ult = X.module_morphism(ult, codomain=Y,
            ....:                           unitriangular='lower')
            sage: f_ut  = X.module_morphism(ut, codomain=Y, triangular='upper')
            sage: f_lt  = X.module_morphism(lt, codomain=Y, triangular='lower')
            sage: (~f_uut)(y[2])
            -B[1] + B[2]
            sage: (~f_ult)(y[2])
            B[2] - B[3]
            sage: (~f_ut)(y[2])
            -1/2*B[1] + 1/2*B[2]
            sage: (~f_lt)(y[2])
            1/2*B[2] - 1/2*B[3]
        """
    def section(self):
        """
        Return the section (partial inverse) of ``self``.

        This returns a partial triangular morphism which is a section of
        ``self``. The section morphism raises a :exc:`ValueError` if
        asked to apply on an element which is not in the image of ``self``.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(QQ, [1,2,3]); x = X.basis()
            sage: X.rename('X')
            sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4,5]); y = Y.basis()
            sage: ult = lambda i: sum(  y[j] for j in range(i+1,6)  ) # uni-lower
            sage: phi = X.module_morphism(ult, triangular='lower', codomain=Y,
            ....:      inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: ~phi
            Traceback (most recent call last):
            ...
            ValueError: Morphism not known to be invertible;
            see the invertible option of module_morphism
            sage: phiinv = phi.section()
            sage: list(map(phiinv*phi, X.basis().list())) == X.basis().list()
            True
            sage: phiinv(Y.basis()[1])
            Traceback (most recent call last):
            ...
            ValueError: B[1] is not in the image
        """
    def preimage(self, f):
        """
        Return the preimage of `f` under ``self``.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3]); y = Y.basis()
            sage: ult = lambda i: sum(  y[j] for j in range(i,4)  ) # uni-lower
            sage: phi = X.module_morphism(ult, triangular='lower', codomain=Y)
            sage: phi.preimage(y[1] + y[2])
            B[1] - B[3]

        The morphism need not be surjective. In the following example,
        the codomain is of larger dimension than the domain::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3, 4]); y = Y.basis()
            sage: lt = lambda i: sum(  y[j] for j in range(i,5)  )
            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y)
            sage: phi.preimage(y[1] + y[2])
            B[1] - B[3]

        Here are examples using ``inverse_on_support`` to handle a
        morphism that shifts the leading indices by `1`::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3, 4, 5]); y = Y.basis()
            sage: lt = lambda i: sum(  y[j] for j in range(i+1,6)  ) # lower
            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y,
            ....:         inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: phi(x[1])
            B[2] + B[3] + B[4] + B[5]
            sage: phi(x[3])
            B[4] + B[5]
            sage: phi.preimage(y[2] + y[3])
            B[1] - B[3]
            sage: phi(phi.preimage(y[2] + y[3])) == y[2] + y[3]
            True
            sage: el = x[1] + 3*x[2] + 2*x[3]
            sage: phi.preimage(phi(el)) == el
            True

            sage: phi.preimage(y[1])
            Traceback (most recent call last):
            ...
            ValueError: B[1] is not in the image
            sage: phi.preimage(y[4])
            Traceback (most recent call last):
            ...
            ValueError: B[4] is not in the image

        Over a base ring like `\\ZZ`, the morphism need not be
        surjective even when the dimensions match::

            sage: X = CombinatorialFreeModule(ZZ, [1, 2, 3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(ZZ, [1, 2, 3]); y = Y.basis()
            sage: lt = lambda i: sum( 2* y[j] for j in range(i,4)  ) # lower
            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y)
            sage: phi.preimage(2*y[1] + 2*y[2])
            B[1] - B[3]

        The error message in case of failure could be more specific though::

            sage: phi.preimage(y[1] + y[2])
            Traceback (most recent call last):
              ...
            TypeError: no conversion of this rational to integer
        """
    def coreduced(self, y):
        """
        Return `y` reduced w.r.t. the image of ``self``.

        INPUT:

        - ``self`` -- a triangular morphism over a field, or a
          unitriangular morphism over a ring
        - ``y`` -- an element of the codomain of ``self``

        Suppose that ``self`` is a morphism from `X` to `Y`. Then, for
        any `y \\in Y`, the call ``self.coreduced(y)`` returns a
        normal form for `y` in the quotient `Y / I` where `I` is the
        image of ``self``.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(QQ, [1,2,3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4,5]); y = Y.basis()
            sage: ult = lambda i: sum(  y[j] for j in range(i+1,6)  )
            sage: phi = X.module_morphism(ult, unitriangular='lower', codomain=Y,
            ....:        inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: [phi(v) for v in X.basis()]
            [B[2] + B[3] + B[4] + B[5],
                    B[3] + B[4] + B[5],
                           B[4] + B[5]]
            sage: [phi.coreduced(y[1]-2*y[4])]
            [B[1] + 2*B[5]]
            sage: [phi.coreduced(v) for v in y]
            [B[1], 0, 0, -B[5], B[5]]

        Now with a non unitriangular morphism::

            sage: lt = lambda i: sum( j*y[j] for j in range(i+1,6)  )
            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: [phi(v) for v in X.basis()]
            [2*B[2] + 3*B[3] + 4*B[4] + 5*B[5],
                      3*B[3] + 4*B[4] + 5*B[5],
                               4*B[4] + 5*B[5]]
            sage: [phi.coreduced(y[1]-2*y[4])]
            [B[1] + 5/2*B[5]]
            sage: [phi.coreduced(v) for v in y]
            [B[1], 0, 0, -5/4*B[5], B[5]]

        For general rings, this method is only implemented for
        unitriangular morphisms::

            sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(ZZ, [1,2,3,4,5]); y = Y.basis()
            sage: phi = X.module_morphism(ult, unitriangular='lower', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: [phi.coreduced(y[1]-2*y[4])]
            [B[1] + 2*B[5]]
            sage: [phi.coreduced(v) for v in y]
            [B[1], 0, 0, -B[5], B[5]]

            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: [phi.coreduced(v) for v in y]
            Traceback (most recent call last):
            ...
            NotImplementedError: coreduce for a triangular but not unitriangular morphism over a ring

        .. NOTE:: Before :issue:`8678` this method used to be called co_reduced.
        """
    def cokernel_basis_indices(self):
        """
        Return the indices of the natural monomial basis of the cokernel of ``self``.

        INPUT:

        - ``self`` -- a triangular morphism over a field or a
          unitriangular morphism over a ring, with a finite
          dimensional codomain.

        OUTPUT:

        A list `E` of indices of the basis `(B_e)_e` of the codomain
        of ``self`` so that `(B_e)_{e\\in E}` forms a basis of a
        supplementary of the image set of ``self``.

        Thinking of this triangular morphism as a row echelon matrix,
        this returns the complementary of the characteristic
        columns. Namely `E` is the set of indices which do not appear
        as leading support of some element of the image set of
        ``self``.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(ZZ, [1,2,3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(ZZ, [1,2,3,4,5]); y = Y.basis()
            sage: uut = lambda i: sum(  y[j] for j in range(i+1,6)  ) # uni-upper
            sage: phi = X.module_morphism(uut, unitriangular='upper', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: phi.cokernel_basis_indices()
            [1, 5]

            sage: phi = X.module_morphism(uut, triangular='upper', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: phi.cokernel_basis_indices()
            Traceback (most recent call last):
            ...
            NotImplementedError: cokernel_basis_indices for a triangular but not unitriangular morphism over a ring

            sage: Y = CombinatorialFreeModule(ZZ, NN); y = Y.basis()
            sage: phi = X.module_morphism(uut, unitriangular='upper', codomain=Y,
            ....:       inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: phi.cokernel_basis_indices()
            Traceback (most recent call last):
            ...
            NotImplementedError: cokernel_basis_indices implemented only for morphisms with a finite dimensional codomain
        """
    def cokernel_projection(self, category=None):
        """
        Return a projection on the co-kernel of ``self``.

        INPUT:

        - ``category`` -- the category of the result

        EXAMPLES::

            sage: X = CombinatorialFreeModule(QQ, [1,2,3]); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1,2,3,4,5]); y = Y.basis()
            sage: lt = lambda i: sum(  y[j] for j in range(i+1,6)  ) # lower
            sage: phi = X.module_morphism(lt, triangular='lower', codomain=Y,
            ....:      inverse_on_support=lambda i: i-1 if i in [2,3,4] else None)
            sage: phipro = phi.cokernel_projection()
            sage: phipro(y[1] + y[2])
            B[1]
            sage: all(phipro(phi(x)).is_zero() for x in X.basis())
            True
            sage: phipro(y[1])
            B[1]
            sage: phipro(y[4])
            -B[5]
            sage: phipro(y[5])
            B[5]
        """

class TriangularModuleMorphismByLinearity(ModuleMorphismByLinearity, TriangularModuleMorphism):
    """
    A concrete class for triangular module morphisms obtained by extending a function by linearity.

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismByLinearity` and
          :class:`TriangularModuleMorphism`.
    """
    def __init__(self, domain, on_basis, codomain=None, category=None, **keywords) -> None:
        '''
        TESTS::

            sage: X = CombinatorialFreeModule(QQ, ZZ)
            sage: from sage.modules.with_basis.morphism import TriangularModuleMorphismByLinearity
            sage: def on_basis(i): return X.sum_of_monomials(range(i-2, i+1))
            sage: import __main__; __main__.on_basis = on_basis  # Fake on_basis being defined in a python module
            sage: phi = TriangularModuleMorphismByLinearity(
            ....:           X, on_basis=on_basis, codomain=X)
            sage: TestSuite(phi).run(skip=["_test_nonzero_equal"])
        '''

class TriangularModuleMorphismFromFunction(ModuleMorphismFromFunction, TriangularModuleMorphism):
    """
    A concrete class for triangular module morphisms implemented by a function.

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism` for
          usage information and examples;
        - :mod:`sage.modules.with_basis.morphism` for a technical
          overview of the classes for module morphisms;
        - :class:`ModuleMorphismFromFunction` and
          :class:`TriangularModuleMorphism`.
    """
    def __init__(self, domain, function, codomain=None, category=None, **keywords) -> None:
        """
        TESTS::

            sage: X = CombinatorialFreeModule(QQ, [0,1,2,3,4])
            sage: from sage.modules.with_basis.morphism import TriangularModuleMorphismFromFunction
            sage: def f(x): return x + X.term(0, sum(x.coefficients()))
            sage: import __main__; __main__.f = f  # Fake f being defined in a python module
            sage: phi = TriangularModuleMorphismFromFunction(
            ....:           X, function=f, codomain=X)
            sage: TestSuite(phi).run()
        """

class ModuleMorphismFromMatrix(ModuleMorphismByLinearity):
    '''
    A class for module morphisms built from a matrix in the
    distinguished bases of the domain and codomain.

    .. SEEALSO::

        - :meth:`ModulesWithBasis.ParentMethods.module_morphism`
        - :meth:`ModulesWithBasis.FiniteDimensional.MorphismMethods.matrix`

    INPUT:

    - ``domain``, ``codomain`` -- two finite dimensional modules over
      the same base ring `R` with basis `F` and `G`, respectively

    - ``matrix`` -- a matrix with base ring `R` and dimensions
      matching that of `F` and `G`, respectively

    - ``side`` -- ``\'left\'`` or ``\'right\'`` (default: ``\'left\'``)

        If ``side`` is "left", this morphism is considered as
        acting on the left; i.e. each column of the matrix
        represents the image of an element of the basis of the
        domain.

    - ``category`` -- a category or ``None`` (default: ``None``)

    EXAMPLES::

        sage: X = CombinatorialFreeModule(ZZ, [1,2]); X.rename(\'X\'); x = X.basis()
        sage: Y = CombinatorialFreeModule(ZZ, [3,4]); Y.rename(\'Y\'); y = Y.basis()
        sage: m = matrix([[1,2],[3,5]])
        sage: phi = X.module_morphism(matrix=m, codomain=Y)
        sage: phi.parent()
        Set of Morphisms from X to Y in Category of finite dimensional modules with basis over Integer Ring
        sage: phi.__class__
        <class \'sage.modules.with_basis.morphism.ModuleMorphismFromMatrix_with_category\'>
        sage: phi(x[1])
        B[3] + 3*B[4]
        sage: phi(x[2])
        2*B[3] + 5*B[4]

        sage: m = matrix([[1,2],[3,5]])
        sage: phi = X.module_morphism(matrix=m, codomain=Y, side=\'right\',
        ....:                         category=Modules(ZZ).WithBasis())
        sage: phi.parent()
        Set of Morphisms from X to Y
        in Category of modules with basis over Integer Ring
        sage: phi(x[1])
        B[3] + 2*B[4]
        sage: phi(x[2])
        3*B[3] + 5*B[4]

    .. TODO::

        Possibly implement rank, addition, multiplication, matrix,
        etc, from the stored matrix.
    '''
    def __init__(self, domain, matrix, codomain=None, category=None, side: str = 'left') -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: from sage.modules.with_basis.morphism import ModuleMorphismFromMatrix
            sage: X = CombinatorialFreeModule(ZZ, [1,2]); X.rename(\'X\'); x = X.basis()
            sage: Y = CombinatorialFreeModule(ZZ, [3,4]); Y.rename(\'Y\'); y = Y.basis()
            sage: m = matrix([[1,2],[3,5]])
            sage: phi = ModuleMorphismFromMatrix(matrix=m, domain=X, codomain=Y, side=\'right\')
            sage: phi.__class__
            <class \'sage.modules.with_basis.morphism.ModuleMorphismFromMatrix_with_category\'>
            sage: phi.matrix(side=\'right\') == m
            True
            sage: TestSuite(phi).run(skip=["_test_pickling"])

        Pickling works (:issue:`17957`) in Python 3::

            sage: phi._on_basis
            <built-in method __getitem__ of dict object at ...>
            sage: loads(dumps(phi)) == phi
            True

        The matrix is stored in the morphism, as if it was for an
        action on the right::

            sage: phi._matrix
            [1 2]
            [3 5]

            sage: phi = ModuleMorphismFromMatrix(matrix=m, side=\'left\',
            ....:                                domain=X, codomain=Y)
            sage: phi._matrix
            [1 3]
            [2 5]
        '''

class DiagonalModuleMorphism(ModuleMorphismByLinearity):
    """
    A class for diagonal module morphisms.

    See :meth:`ModulesWithBasis.ParentMethods.module_morphism`.

    INPUT:

    - ``domain``, ``codomain`` -- two modules with basis `F` and `G`,
      respectively
    - ``diagonal`` -- a function `d`

    Assumptions:

    - ``domain`` and ``codomain`` have the same base ring `R`,
    - their respective bases `F` and `G` have the same index set `I`,
    - `d` is a function `I \\to R`.

    Return the diagonal module morphism from ``domain`` to ``codomain``
    sending `F(i) \\mapsto d(i) G(i)` for all `i \\in I`.

    By default, ``codomain`` is currently assumed to be ``domain``.
    (Todo: make a consistent choice with ``*ModuleMorphism``.)

    .. TODO::

        - Implement an optimized ``_call_()`` function.
        - Generalize to a mapcoeffs.
        - Generalize to a mapterms.

    EXAMPLES::

        sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
        sage: phi = X.module_morphism(diagonal=factorial, codomain=X)
        sage: x = X.basis()
        sage: phi(x[1]), phi(x[2]), phi(x[3])
        (B[1], 2*B[2], 6*B[3])
    """
    def __init__(self, domain, diagonal, codomain=None, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X')
            sage: phi = X.module_morphism(diagonal=factorial, codomain=X)
            sage: phi.__class__
            <class 'sage.modules.with_basis.morphism.DiagonalModuleMorphism_with_category'>
            sage: TestSuite(phi).run()
        """
    def __invert__(self):
        """
        Return the inverse diagonal morphism.

        EXAMPLES::

            sage: X = CombinatorialFreeModule(QQ, [1, 2, 3]); X.rename('X'); x = X.basis()
            sage: Y = CombinatorialFreeModule(QQ, [1, 2, 3]); Y.rename('Y'); y = Y.basis()
            sage: phi = X.module_morphism(diagonal=factorial, codomain=X)
            sage: phi_inv = ~phi
            sage: phi_inv
            Generic endomorphism of Y
            sage: phi_inv(y[3])
            1/6*B[3]

        Caveat: this inverse morphism is only well defined if
        `d(\\lambda)` is always invertible in the base ring. This
        condition is *not* tested for, so using an ill defined inverse
        morphism will trigger arithmetic errors.
        """

def pointwise_inverse_function(f):
    """
    Return the function `x \\mapsto 1 / f(x)`.

    INPUT:

    - ``f`` -- a function

    EXAMPLES::

        sage: from sage.modules.with_basis.morphism import pointwise_inverse_function
        sage: def f(x): return x
        sage: g = pointwise_inverse_function(f)
        sage: g(1), g(2), g(3)
        (1, 1/2, 1/3)

    :func:`pointwise_inverse_function` is an involution::

        sage: f is pointwise_inverse_function(g)
        True

    .. TODO::

        This has nothing to do here!!! Should there be a library for
        pointwise operations on functions somewhere in Sage?
    """

class PointwiseInverseFunction(SageObject):
    """
    A class for pointwise inverse functions.

    The pointwise inverse function of a function `f` is the function
    sending every `x` to `1 / f(x)`.

    EXAMPLES::

        sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
        sage: f = PointwiseInverseFunction(factorial)
        sage: f(0), f(1), f(2), f(3)
        (1, 1, 1/2, 1/6)
    """
    def __init__(self, f) -> None:
        """
        TESTS::

            sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
            sage: f = PointwiseInverseFunction(factorial)
            sage: f(0), f(1), f(2), f(3)
            (1, 1, 1/2, 1/6)
            sage: TestSuite(f).run()
        """
    def __eq__(self, other):
        """
        Return whether this function is equal to ``other``.

        TESTS::

            sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
            sage: f = PointwiseInverseFunction(factorial)
            sage: g = PointwiseInverseFunction(factorial)
            sage: f is g
            False
            sage: f == g
            True
        """
    def __ne__(self, other):
        """
        Return whether this function is not equal to ``other``.

        TESTS::

            sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
            sage: f = PointwiseInverseFunction(factorial)
            sage: g = PointwiseInverseFunction(factorial)
            sage: f != g
            False
        """
    def __call__(self, *args):
        """
        TESTS::

            sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
            sage: g = PointwiseInverseFunction(operator.mul)
            sage: g(5,7)
            1/35
        """
    def pointwise_inverse(self):
        """
        TESTS::

            sage: from sage.modules.with_basis.morphism import PointwiseInverseFunction
            sage: g = PointwiseInverseFunction(operator.mul)
            sage: g.pointwise_inverse() is operator.mul
            True
        """
