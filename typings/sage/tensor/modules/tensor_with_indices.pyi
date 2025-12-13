from sage.structure.sage_object import SageObject as SageObject

class TensorWithIndices(SageObject):
    '''
    Index notation for tensors.

    This is a technical class to allow one to write some tensor operations
    (contractions and symmetrizations) in index notation.

    INPUT:

    - ``tensor`` -- a tensor (or a tensor field)
    - ``indices`` -- string containing the indices, as single letters; the
      contravariant indices must be stated first and separated from the
      covariant indices by the character ``_``

    EXAMPLES:

    Index representation of tensors on a rank-3 free module::

        sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
        sage: e = M.basis(\'e\')
        sage: a = M.tensor((2,0), name=\'a\')
        sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
        sage: b = M.tensor((0,2), name=\'b\')
        sage: b[:] = [[-1,2,-3], [-4,5,6], [7,-8,9]]
        sage: t = a*b ; t.set_name(\'t\') ; t
        Type-(2,2) tensor t on the 3-dimensional vector space M over the
         Rational Field
        sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
        sage: T = TensorWithIndices(t, \'^ij_kl\') ; T
        t^ij_kl

    The :class:`TensorWithIndices` object is returned by the square
    bracket operator acting on the tensor and fed with the string specifying
    the indices::

        sage: a[\'^ij\']
        a^ij
        sage: type(a[\'^ij\'])
        <class \'sage.tensor.modules.tensor_with_indices.TensorWithIndices\'>
        sage: b[\'_ef\']
        b_ef
        sage: t[\'^ij_kl\']
        t^ij_kl

    The symbol \'^\' may be omitted, since the distinction between covariant
    and contravariant indices is performed by the index position relative to
    the symbol \'_\'::

        sage: t[\'ij_kl\']
        t^ij_kl

    Also, LaTeX notation may be used::

        sage: t[\'^{ij}_{kl}\']
        t^ij_kl

    If some operation is asked in the index notation, the resulting tensor
    is returned, not a :class:`TensorWithIndices` object; for instance, for
    a symmetrization::

        sage: s = t[\'^(ij)_kl\'] ; s  # the symmetrization on i,j is indicated by parentheses
        Type-(2,2) tensor on the 3-dimensional vector space M over the
         Rational Field
        sage: s.symmetries()
        symmetry: (0, 1);  no antisymmetry
        sage: s == t.symmetrize(0,1)
        True

    The letters denoting the indices can be chosen freely; since they carry no
    information, they can even be replaced by dots::

        sage: t[\'^(..)_..\'] == t.symmetrize(0,1)
        True

    Similarly, for an antisymmetrization::

        sage: s = t[\'^ij_[kl]\'] ; s # the symmetrization on k,l is indicated by square brackets
        Type-(2,2) tensor on the 3-dimensional vector space M over the Rational
         Field
        sage: s.symmetries()
        no symmetry;  antisymmetry: (2, 3)
        sage: s == t.antisymmetrize(2,3)
        True

    One can also perform multiple symmetrization-antisymmetrizations::

        sage: aa = a*a
        sage: aa[\'(..)(..)\'] == aa.symmetrize(0,1).symmetrize(2,3)
        True
        sage: aa == aa[\'(..)(..)\'] + aa[\'[..][..]\'] + aa[\'(..)[..]\'] + aa[\'[..](..)\']
        True

    Another example of an operation indicated by indices is a contraction::

        sage: s = t[\'^ki_kj\'] ; s  # contraction on the repeated index k
        Type-(1,1) tensor on the 3-dimensional vector space M over the Rational
         Field
        sage: s == t.trace(0,2)
        True

    Indices not involved in the contraction may be replaced by dots::

        sage: s == t[\'^k._k.\']
        True

    The contraction of two tensors is indicated by repeated indices and
    the ``*`` operator::

        sage: s = a[\'^ik\'] * b[\'_kj\'] ; s
        Type-(1,1) tensor on the 3-dimensional vector space M over the Rational
         Field
        sage: s == a.contract(1, b, 0)
        True
        sage: s = t[\'^.k_..\'] * b[\'_.k\'] ; s
        Type-(1,3) tensor on the 3-dimensional vector space M over the Rational
         Field
        sage: s == t.contract(1, b, 1)
        True
        sage: t[\'^{ik}_{jl}\']*b[\'_{mk}\'] == s # LaTeX notation
        True

    Contraction on two indices::

        sage: s = a[\'^kl\'] * b[\'_kl\'] ; s
        105
        sage: s == (a*b)[\'^kl_kl\']
        True
        sage: s == (a*b)[\'_kl^kl\']
        True
        sage: s == a.contract(0,1, b, 0,1)
        True

    The square bracket operator acts in a similar way on :class:`TensorWithIndices`::

        sage: b = +a["ij"] ; b._tensor.set_name("b") # create a copy of a["ij"]
        sage: b
        b^ij
        sage: b[:]
        [1 2 3]
        [4 5 6]
        [7 8 9]
        sage: b[0,0] == 1
        True
        sage: b["ji"]
        b^ji
        sage: b["(ij)"][:]
        [1 3 5]
        [3 5 7]
        [5 7 9]
        sage: b["(ij)"] == b["(ij)"]["ij"]
        True

    However, it keeps track of indices::

        sage: b["ij"] = a["ji"]
        sage: b[:] == a[:]
        False
        sage: b[:] == a[:].transpose()
        True


    Arithmetics::

        sage: 2*a[\'^ij\']
        X^ij
        sage: (2*a[\'^ij\'])._tensor == 2*a
        True
        sage: 2*t[\'ij_kl\']
        X^ij_kl
        sage: +a[\'^ij\']
        +a^ij
        sage: +t[\'ij_kl\']
        +t^ij_kl
        sage: -a[\'^ij\']
        -a^ij
        sage: -t[\'ij_kl\']
        -t^ij_kl
        sage: a["^(..)"]["ij"] == 1/2*(a["^ij"] + a["^ji"])
        True

    The output indices are the ones of the left term of the addition::

        sage: a["^(..)"]["ji"] == 1/2*(a["^ij"] + a["^ji"])
        False
        sage: (a*a)["^..(ij)"]["abij"] == 1/2*((a*a)["^abij"] + (a*a)["^abji"])
        True
        sage: c = 1/2*((a*a)["^abij"] + (a*a)["^ijab"])
        sage: from itertools import product
        sage: all(c[i,j,k,l] == c[k,l,i,j] for i,j,k,l in product(range(3),repeat=4))
        True

    Non-digit unicode identifier characters are allowed::

        sage: a[\'^μξ\']
        a^μξ

    Conventions are checked and non acceptable indices raise
    :exc:`ValueError`, for instance::

        sage: a[\'([..])\']  # nested symmetries
        Traceback (most recent call last):
        ...
        ValueError: index conventions not satisfied
        sage: a[\'(..\']  # unbalanced parenthis
        Traceback (most recent call last):
        ...
        ValueError: index conventions not satisfied
        sage: a[\'ii\']  # repeated indices of the same type
        Traceback (most recent call last):
        ...
        ValueError: index conventions not satisfied: repeated indices of same type
        sage: (a*a)[\'^(ij)^(kl)\']  # multiple indices group of the same type
        Traceback (most recent call last):
        ...
        ValueError: index conventions not satisfied
        sage: a["^\\u2663\\u2665"]  # non-word-constituent
        Traceback (most recent call last):
        ...
        ValueError: index conventions not satisfied
    '''
    def __init__(self, tensor, indices) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: t = M.tensor((2,1), name='t')
            sage: ti = TensorWithIndices(t, 'ab_c')

        We need to skip the pickling test because we can't check equality
        unless the tensor was defined w.r.t. a basis::

            sage: TestSuite(ti).run(skip='_test_pickling')

        ::

            sage: e = M.basis('e')
            sage: t[:] = [[[1,2,3], [-4,5,6], [7,8,-9]],
            ....:         [[10,-11,12], [13,14,-15], [16,17,18]],
            ....:         [[19,-20,-21], [-22,23,24], [25,26,-27]]]
            sage: ti = TensorWithIndices(t, 'ab_c')
            sage: TestSuite(ti).run()
        """
    def update(self):
        """
        Return the tensor contains in ``self`` if it differs from that used
        for creating ``self``, otherwise return ``self``.

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: a = M.tensor((1,1),  name='a')
            sage: a[:] = [[1,-2,3], [-4,5,-6], [7,-8,9]]
            sage: a_ind = TensorWithIndices(a, 'i_j') ; a_ind
            a^i_j
            sage: a_ind.update()
            a^i_j
            sage: a_ind.update() is a_ind
            True
            sage: a_ind = TensorWithIndices(a, 'k_k') ; a_ind
            scalar
            sage: a_ind.update()
            15
        """
    def __eq__(self, other):
        """
        Check equality.

        TESTS::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: t = M.tensor((2,1), name='t')
            sage: ti = TensorWithIndices(t, 'ab_c')
            sage: ti == TensorWithIndices(t, '^{ab}_c')
            True
            sage: ti == TensorWithIndices(t, 'ac_b')
            False
            sage: tp = M.tensor((2,1))
            sage: ti == TensorWithIndices(tp, 'ab_c')
            Traceback (most recent call last):
            ...
            ValueError: no common basis for the comparison
        """
    def __ne__(self, other):
        """
        Check not equals.

        TESTS::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: t = M.tensor((2,1), name='t')
            sage: ti = TensorWithIndices(t, 'ab_c')
            sage: ti != TensorWithIndices(t, '^{ab}_c')
            False
            sage: ti != TensorWithIndices(t, 'ac_b')
            True
        """
    def __mul__(self, other):
        """
        Tensor product or contraction on specified indices.

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: a = M.tensor((2,0), name='a')
            sage: a[:] = [[1,-2,3], [-4,5,-6], [7,-8,9]]
            sage: b = M.linear_form(name='b')
            sage: b[:] = [4,2,1]
            sage: ai = TensorWithIndices(a, '^ij')
            sage: bi = TensorWithIndices(b, '_k')
            sage: s = ai.__mul__(bi) ; s  # no repeated indices ==> tensor product
            Type-(2,1) tensor a⊗b on the 3-dimensional vector space M over the
             Rational Field
            sage: s == a*b
            True
            sage: s[:]
            [[[4, 2, 1], [-8, -4, -2], [12, 6, 3]],
             [[-16, -8, -4], [20, 10, 5], [-24, -12, -6]],
             [[28, 14, 7], [-32, -16, -8], [36, 18, 9]]]
            sage: ai = TensorWithIndices(a, '^kj')
            sage: s = ai.__mul__(bi) ; s  # repeated index k ==> contraction
            Element of the 3-dimensional vector space M over the Rational Field
            sage: s == a.contract(0, b)
            True
            sage: s[:]
            [3, -6, 9]
        """
    def __rmul__(self, other):
        """
        Multiplication on the left by ``other``.

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: a = M.tensor((2,1), name='a')
            sage: a[0,2,1], a[1,2,0] = 7, -4
            sage: ai = TensorWithIndices(a, 'ij_k')
            sage: s = ai.__rmul__(3) ; s
            X^ij_k
            sage: s._tensor == 3*a
            True
        """
    def __add__(self, other):
        '''
        Addition between tensors with indices.

        The underlying tensor of the output is the sum of the underlying tensor
        of ``self`` with the underlying tensor of ``other`` whose entries have
        be permuted to respect Einstein summation usual conventions. The
        indices names of the output are those of ``self``.


        TESTS::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b = M.tensor((0,2), name=\'b\')
            sage: b[:] = [[-1,2,-3], [-4,5,6], [7,-8,9]]
            sage: T = a*a*b*b
            sage: 1/4*(T["ijkl_abcd"] + T["jikl_abcd"] + T["ijkl_abdc"]\\\n            ....: + T["jikl_abdc"]) == T["(..).._..(..)"]["ijkl_abcd"]
            True
        '''
    def __sub__(self, other):
        '''
        Subtraction between tensors with indices.

        The underlying tensor of the output is the underlying tensor of
        ``self`` minus the underlying tensor of ``other`` whose entries have
        be permuted to respect Einstein summation usual conventions. The
        indices names of the output are those of ``self``.

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b = M.tensor((0,2), name=\'b\')
            sage: b[:] = [[-1,2,-3], [-4,5,6], [7,-8,9]]
            sage: a["^[..]"]["ij"] == 1/2*(a["^ij"]-a["^ji"])
            True
            sage: (a*a)["^..[ij]"]["abij"] == 1/2*((a*a)["^abij"]-(a*a)["^abji"])
            True
            sage: Riem = a*a
            sage: Riem = Riem["[ij][kl]"]
            sage: Riem = 1/2*(Riem["ijkl"]+Riem["klij"])
            sage: O = M.tensor((4,0), name=\'O\')
            sage: O[0,0,0,0] = 0
            sage: (Riem["ijkl"]+Riem["iklj"]+Riem["iljk"]) == O["ijkl"]
            True

        TESTS::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b = M.tensor((0,2), name=\'b\')
            sage: b[:] = [[-1,2,-3], [-4,5,6], [7,-8,9]]
            sage: T = a*a*b*b
            sage: 1/4*(T["ijkl_abcd"]-T["jikl_abcd"] - T["ijkl_abdc"]\\\n            ....: + T["jikl_abdc"] ) == T["[..].._..[..]"]["ijkl_abcd"]
            True
        '''
    def __getitem__(self, args):
        '''
        Return a component of the underlying tensor w.r.t. some basis.

        NB: if ``args`` is a string, this method acts as a shortcut for
        tensor contractions and symmetrizations, the string containing
        abstract indices.

        INPUT:

        - ``args`` -- list of indices defining the component; if ``[:]`` is
          provided, all the components are returned. The basis can be passed
          as the first item of ``args``; if not, the free module\'s default
          basis is assumed.
          if ``args`` is a string, this method acts as a shortcut for
          tensor contractions and symmetrizations, the string containing
          abstract indices.

        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b = a["ij"]
            sage: b
            a^ij
            sage: b[:]
            [1 2 3]
            [4 5 6]
            [7 8 9]
            sage: b[0,0] == 1
            True
            sage: b["ji"]
            a^ji
            sage: b["(ij)"][:]
            [1 3 5]
            [3 5 7]
            [5 7 9]
        '''
    def __setitem__(self, args, value) -> None:
        '''
         Set a component w.r.t. some basis.

        INPUT:

        - ``args`` -- list of indices defining the component; if ``[:]`` is
          provided, all the components are set. The basis can be passed
          as the first item of ``args``; if not, the free module\'s default
          basis is assumed  if ``args`` is a string and value is a tensor
          with indices, this method permutes the coefficients of ``value``
          before assigning the underlying tensor of ``value`` to ``self``.

        - ``value`` -- the value to be set or a list of values if
          ``args = [:]`` or a tensor with indices

        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')["ij"]
            sage: b = M.tensor((2,0), name=\'b\')["ij"]
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b["ij"] = a["ji"]
            sage: b[:] == a[:].transpose()
            True
        '''
    def permute_indices(self, permutation):
        '''
        Return a tensor with indices with permuted indices.

        INPUT:

        - ``permutation`` -- permutation that has to be applied to the indices
          the input should be a ``list`` containing the second line of the permutation
          in Cauchy notation.

        OUTPUT:

        - an instance of ``TensorWithIndices`` whose indices names and place
          are those of ``self`` but whose components have been permuted with
          ``permutation``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: b = M.tensor((2,0), name=\'b\')
            sage: b[:] = [[-1,2,-3], [-4,5,6], [7,-8,9]]
            sage: identity = [0,1]
            sage: transposition = [1,0]
            sage: a["ij"].permute_indices(identity) == a["ij"]
            True
            sage: a["ij"].permute_indices(transposition)[:] == a[:].transpose()
            True
            sage: cycle = [1,2,3,0] # the cyclic permutation sending 0 to 1
            sage: (a*b)[0,1,2,0] == (a*b)["ijkl"].permute_indices(cycle)[1,2,0,0]
            True

        TESTS::

            sage: M = FiniteRankFreeModule(QQ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.tensor((2,0), name=\'a\')
            sage: a[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: identity = [0,1]
            sage: transposition = [1,0]
            sage: a["ij"].permute_indices(identity) == a["ij"]
            True
            sage: a["ij"].permute_indices(transposition)[:] == a[:].transpose()
            True
            sage: (a*a)["ijkl"].permute_indices([1,2,3,0])[0,1,2,1] == (a*a)[1,2,1,0]
            True
        '''
    def __pos__(self):
        """
        Unary plus operator.

        OUTPUT: an exact copy of ``self``

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: a = M.tensor((2,1), name='a')
            sage: a[0,2,1], a[1,2,0] = 7, -4
            sage: ai = TensorWithIndices(a, 'ij_k')
            sage: s = ai.__pos__() ; s
            +a^ij_k
            sage: s._tensor == a
            True
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: negative of ``self``

        EXAMPLES::

            sage: from sage.tensor.modules.tensor_with_indices import TensorWithIndices
            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: a = M.tensor((2,1), name='a')
            sage: a[0,2,1], a[1,2,0] = 7, -4
            sage: ai = TensorWithIndices(a, 'ij_k')
            sage: s = ai.__neg__() ; s
            -a^ij_k
            sage: s._tensor == -a
            True
        """
