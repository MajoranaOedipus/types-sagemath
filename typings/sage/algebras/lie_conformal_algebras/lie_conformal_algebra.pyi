from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.sets.family import Family as Family
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LieConformalAlgebra(UniqueRepresentation, Parent):
    """
    Lie Conformal Algebras base class and factory.

    INPUT:

    - ``R`` -- a commutative ring (default: ``None``); the base
      ring of this Lie conformal algebra. Behaviour is undefined
      if it is not a field of characteristic zero.

    - ``arg0`` -- dictionary (default: ``None``);
      a dictionary containing the `\\lambda` brackets of the
      generators of this Lie conformal algebra. The keys of this
      dictionary are pairs of either names or indices of the
      generators and the values are themselves dictionaries. For a
      pair of generators ``'a'`` and ``'b'``, the value of
      ``arg0[('a','b')]`` is a dictionary whose keys are positive
      integer numbers and the corresponding value for the
      key ``j`` is a dictionary itself representing the `j`-th product
      `a_{(j)}b`. Thus, for a positive integer number `j`, the
      value of ``arg0[('a','b')][j]`` is a dictionary whose entries
      are pairs ``('c',n)`` where ``'c'`` is the name of a generator
      and ``n`` is a positive number. The value for this key is the
      coefficient of `\\frac{T^{n}}{n!} c` in `a_{(j)}b`. For
      example the ``arg0`` for the *Virasoro* Lie conformal algebra
      is::

            {('L','L'):{0:{('L',1):1}, 1:{('L',0):2}, 3:{('C',0):1/2}}}


      Do not include central elements as keys in this dictionary. Also,
      if the key ``('a','b')`` is present, there is no need to include
      ``('b','a')`` as it is defined by skew-symmetry. Any missing
      pair (besides the ones defined by skew-symmetry) is assumed
      to have vanishing `\\lambda`-bracket.

    - ``names`` -- tuple of strings (default: ``None``); the list of
      names for generators of this Lie conformal algebra. Do not
      include central elements in this list.

    - ``central_elements`` -- tuple of strings (default: ``None``);
      a list of names for central elements of this Lie conformal algebra

    - ``index_set`` -- enumerated set (default: ``None``); an
      indexing set for the generators of this Lie conformal algebra.
      Do not include central elements in this list.

    - ``weights`` -- tuple of nonnegative rational numbers
      (default: ``None``); a list of degrees for this Lie
      conformal algebra.
      The returned Lie conformal algebra is H-Graded. This tuple
      needs to have the same cardinality as ``index_set`` or
      ``names``. Central elements are assumed to have weight `0`.

    - ``parity`` -- tuple of `0` or `1` (default: tuple of `0`);
      if this is a super Lie conformal algebra, this tuple
      specifies the parity of each of the non-central generators of
      this Lie conformal algebra. Central elements are assumed to
      be even. Notice that if this tuple is present, the category
      of this Lie conformal algebra is set to be a subcategory of
      ``LieConformalAlgebras(R).Super()``, even if all generators
      are even.

    - ``category`` -- the category that this Lie conformal algebra
      belongs to

    In addition we accept the following keywords:

    - ``graded`` -- boolean (default: ``False``);
      if ``True``, the returned algebra is H-Graded.
      If ``weights`` is not specified, all non-central generators
      are assigned degree `1`. This keyword is ignored if
      ``weights`` is specified

    - ``super`` -- boolean (default: ``False``);
      if ``True``, the returned algebra is a super
      Lie conformal algebra even if all generators are even.
      If ``parity`` is not specified, all generators are
      assigned even parity. This keyword is ignored if
      ``parity`` is specified.

    .. Note::

        Any remaining keyword is currently passed to
        :class:`CombinatorialFreeModule<sage.combinat.free_module.CombinatorialFreeModule>`.

    EXAMPLES:

    We construct the `\\beta-\\gamma` system or *Weyl* Lie conformal
    algebra::

        sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
        sage: V = LieConformalAlgebra(QQbar, betagamma_dict, names=('a','b'), weights=(1,0), central_elements=('K',))
        sage: V.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Algebraic Field
        sage: V.inject_variables()
        Defining a, b, K
        sage: a.bracket(b)
        {0: -K}

    We construct the current algebra for `\\mathfrak{sl}_2`::

        sage: sl2dict = {('e','f'):{0:{('h',0):1}, 1:{('K',0):1}}, ('e','h'):{0:{('e',0):-2}}, ('f','h'):{0:{('f',0):2}}, ('h', 'h'):{1:{('K', 0):2}}}
        sage: V = LieConformalAlgebra(QQ, sl2dict, names=('e', 'h', 'f'), central_elements=('K',), graded=True)
        sage: V.inject_variables()
        Defining e, h, f, K
        sage: e.bracket(f)
        {0: h, 1: K}
        sage: h.bracket(e)
        {0: 2*e}
        sage: e.bracket(f.T())
        {0: Th, 1: h, 2: 2*K}
        sage: V.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Rational Field
        sage: e.degree()
        1

    .. TODO::

        This class checks that the provided dictionary is consistent
        with skew-symmetry. It does not check that it is consistent
        with the Jacobi identity.

    .. SEEALSO::

        :mod:`sage.algebras.lie_conformal_algebras.graded_lie_conformal_algebra`
    """
    @staticmethod
    def __classcall_private__(cls, R=None, arg0=None, index_set=None, central_elements=None, category=None, prefix=None, names=None, latex_names=None, parity=None, weights=None, **kwds):
        """
        Lie conformal algebra factory.

        EXAMPLES::

            sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
            sage: V = LieConformalAlgebra(QQ, betagamma_dict, names=('a','b'), weights=(1,0), central_elements=('K',))
            sage: type(V)
            <class 'sage.algebras.lie_conformal_algebras.graded_lie_conformal_algebra.GradedLieConformalAlgebra_with_category'>
        """
