import _cython_3_2_1
import sage as sage
import sage.rings.ring
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.prandom import randrange as randrange
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_FiniteField: _cython_3_2_1.cython_function_or_method
unpickle_FiniteField_ext: _cython_3_2_1.cython_function_or_method
unpickle_FiniteField_prm: _cython_3_2_1.cython_function_or_method

class FiniteField(sage.rings.ring.Field):
    """FiniteField(base, names, normalize, category=None)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 48)

    Abstract base class for finite fields.

    TESTS::

        sage: GF(997).is_finite()
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base, names, normalize, category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 57)

                Initialize ``self``.

                EXAMPLES::

                    sage: K = GF(7); K
                    Finite Field of size 7
                    sage: loads(K.dumps()) == K
                    True
                    sage: GF(7^10, 'a')
                    Finite Field in a of size 7^10
                    sage: K = GF(7^10, 'a'); K
                    Finite Field in a of size 7^10
                    sage: loads(K.dumps()) == K
                    True
        """
    @overload
    def algebraic_closure(self, name=..., **kwds) -> Any:
        """FiniteField.algebraic_closure(self, name='z', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1717)

        Return an algebraic closure of ``self``.

        INPUT:

        - ``name`` -- string (default: ``'z'``); prefix to use for
          variable names of subfields

        - ``implementation`` -- string (optional); specifies how to
          construct the algebraic closure.  The only value supported
          at the moment is ``'pseudo_conway'``.  For more details, see
          :mod:`~sage.rings.algebraic_closure_finite_field`.

        OUTPUT:

        An algebraic closure of ``self``.  Note that mathematically
        speaking, this is only unique up to *non-unique* isomorphism.
        To obtain canonically defined algebraic closures, one needs an
        algorithm that also provides a canonical isomorphism between
        any two algebraic closures constructed using the algorithm.

        This non-uniqueness problem can in principle be solved by
        using *Conway polynomials*; see for example
        :wikipedia:`Conway_polynomial_(finite_fields)`. These have
        the drawback that computing them takes a long time.  Therefore
        Sage implements a variant called *pseudo-Conway polynomials*,
        which are easier to compute but do not determine an algebraic
        closure up to unique isomorphism.

        The output of this method is cached, so that within the same
        Sage session, calling it multiple times will return the same
        algebraic closure (i.e. the same Sage object).  Despite this,
        the non-uniqueness of the current implementation means that
        coercion and pickling cannot work as one might expect.  See
        below for an example.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: F
            Algebraic closure of Finite Field of size 5
            sage: F.gen(3)
            z3

        For finite fields, the algebraic closure is always (isomorphic
        to) the algebraic closure of the prime field::

            sage: GF(5^2).algebraic_closure() == F
            True

        The default name is 'z' but you can change it through the option
        ``name``::

            sage: Ft = GF(5).algebraic_closure('t')
            sage: Ft.gen(3)
            t3

        Because Sage currently only implements algebraic closures
        using a non-unique definition (see above), it is currently
        impossible to implement pickling in such a way that a pickled
        and unpickled element compares equal to the original::

            sage: F = GF(7).algebraic_closure()
            sage: x = F.gen(2)
            sage: loads(dumps(x)) == x
            False

        .. NOTE::

            For non-prime finite fields, this method currently simply
            returns the algebraic closure of the prime field. This may
            or may not change in the future when extension towers are
            supported properly.

        TESTS::

            sage: GF(5).algebraic_closure() is GF(5).algebraic_closure()
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """FiniteField.algebraic_closure(self, name='z', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1717)

        Return an algebraic closure of ``self``.

        INPUT:

        - ``name`` -- string (default: ``'z'``); prefix to use for
          variable names of subfields

        - ``implementation`` -- string (optional); specifies how to
          construct the algebraic closure.  The only value supported
          at the moment is ``'pseudo_conway'``.  For more details, see
          :mod:`~sage.rings.algebraic_closure_finite_field`.

        OUTPUT:

        An algebraic closure of ``self``.  Note that mathematically
        speaking, this is only unique up to *non-unique* isomorphism.
        To obtain canonically defined algebraic closures, one needs an
        algorithm that also provides a canonical isomorphism between
        any two algebraic closures constructed using the algorithm.

        This non-uniqueness problem can in principle be solved by
        using *Conway polynomials*; see for example
        :wikipedia:`Conway_polynomial_(finite_fields)`. These have
        the drawback that computing them takes a long time.  Therefore
        Sage implements a variant called *pseudo-Conway polynomials*,
        which are easier to compute but do not determine an algebraic
        closure up to unique isomorphism.

        The output of this method is cached, so that within the same
        Sage session, calling it multiple times will return the same
        algebraic closure (i.e. the same Sage object).  Despite this,
        the non-uniqueness of the current implementation means that
        coercion and pickling cannot work as one might expect.  See
        below for an example.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: F
            Algebraic closure of Finite Field of size 5
            sage: F.gen(3)
            z3

        For finite fields, the algebraic closure is always (isomorphic
        to) the algebraic closure of the prime field::

            sage: GF(5^2).algebraic_closure() == F
            True

        The default name is 'z' but you can change it through the option
        ``name``::

            sage: Ft = GF(5).algebraic_closure('t')
            sage: Ft.gen(3)
            t3

        Because Sage currently only implements algebraic closures
        using a non-unique definition (see above), it is currently
        impossible to implement pickling in such a way that a pickled
        and unpickled element compares equal to the original::

            sage: F = GF(7).algebraic_closure()
            sage: x = F.gen(2)
            sage: loads(dumps(x)) == x
            False

        .. NOTE::

            For non-prime finite fields, this method currently simply
            returns the algebraic closure of the prime field. This may
            or may not change in the future when extension towers are
            supported properly.

        TESTS::

            sage: GF(5).algebraic_closure() is GF(5).algebraic_closure()
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """FiniteField.algebraic_closure(self, name='z', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1717)

        Return an algebraic closure of ``self``.

        INPUT:

        - ``name`` -- string (default: ``'z'``); prefix to use for
          variable names of subfields

        - ``implementation`` -- string (optional); specifies how to
          construct the algebraic closure.  The only value supported
          at the moment is ``'pseudo_conway'``.  For more details, see
          :mod:`~sage.rings.algebraic_closure_finite_field`.

        OUTPUT:

        An algebraic closure of ``self``.  Note that mathematically
        speaking, this is only unique up to *non-unique* isomorphism.
        To obtain canonically defined algebraic closures, one needs an
        algorithm that also provides a canonical isomorphism between
        any two algebraic closures constructed using the algorithm.

        This non-uniqueness problem can in principle be solved by
        using *Conway polynomials*; see for example
        :wikipedia:`Conway_polynomial_(finite_fields)`. These have
        the drawback that computing them takes a long time.  Therefore
        Sage implements a variant called *pseudo-Conway polynomials*,
        which are easier to compute but do not determine an algebraic
        closure up to unique isomorphism.

        The output of this method is cached, so that within the same
        Sage session, calling it multiple times will return the same
        algebraic closure (i.e. the same Sage object).  Despite this,
        the non-uniqueness of the current implementation means that
        coercion and pickling cannot work as one might expect.  See
        below for an example.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: F
            Algebraic closure of Finite Field of size 5
            sage: F.gen(3)
            z3

        For finite fields, the algebraic closure is always (isomorphic
        to) the algebraic closure of the prime field::

            sage: GF(5^2).algebraic_closure() == F
            True

        The default name is 'z' but you can change it through the option
        ``name``::

            sage: Ft = GF(5).algebraic_closure('t')
            sage: Ft.gen(3)
            t3

        Because Sage currently only implements algebraic closures
        using a non-unique definition (see above), it is currently
        impossible to implement pickling in such a way that a pickled
        and unpickled element compares equal to the original::

            sage: F = GF(7).algebraic_closure()
            sage: x = F.gen(2)
            sage: loads(dumps(x)) == x
            False

        .. NOTE::

            For non-prime finite fields, this method currently simply
            returns the algebraic closure of the prime field. This may
            or may not change in the future when extension towers are
            supported properly.

        TESTS::

            sage: GF(5).algebraic_closure() is GF(5).algebraic_closure()
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """FiniteField.algebraic_closure(self, name='z', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1717)

        Return an algebraic closure of ``self``.

        INPUT:

        - ``name`` -- string (default: ``'z'``); prefix to use for
          variable names of subfields

        - ``implementation`` -- string (optional); specifies how to
          construct the algebraic closure.  The only value supported
          at the moment is ``'pseudo_conway'``.  For more details, see
          :mod:`~sage.rings.algebraic_closure_finite_field`.

        OUTPUT:

        An algebraic closure of ``self``.  Note that mathematically
        speaking, this is only unique up to *non-unique* isomorphism.
        To obtain canonically defined algebraic closures, one needs an
        algorithm that also provides a canonical isomorphism between
        any two algebraic closures constructed using the algorithm.

        This non-uniqueness problem can in principle be solved by
        using *Conway polynomials*; see for example
        :wikipedia:`Conway_polynomial_(finite_fields)`. These have
        the drawback that computing them takes a long time.  Therefore
        Sage implements a variant called *pseudo-Conway polynomials*,
        which are easier to compute but do not determine an algebraic
        closure up to unique isomorphism.

        The output of this method is cached, so that within the same
        Sage session, calling it multiple times will return the same
        algebraic closure (i.e. the same Sage object).  Despite this,
        the non-uniqueness of the current implementation means that
        coercion and pickling cannot work as one might expect.  See
        below for an example.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: F
            Algebraic closure of Finite Field of size 5
            sage: F.gen(3)
            z3

        For finite fields, the algebraic closure is always (isomorphic
        to) the algebraic closure of the prime field::

            sage: GF(5^2).algebraic_closure() == F
            True

        The default name is 'z' but you can change it through the option
        ``name``::

            sage: Ft = GF(5).algebraic_closure('t')
            sage: Ft.gen(3)
            t3

        Because Sage currently only implements algebraic closures
        using a non-unique definition (see above), it is currently
        impossible to implement pickling in such a way that a pickled
        and unpickled element compares equal to the original::

            sage: F = GF(7).algebraic_closure()
            sage: x = F.gen(2)
            sage: loads(dumps(x)) == x
            False

        .. NOTE::

            For non-prime finite fields, this method currently simply
            returns the algebraic closure of the prime field. This may
            or may not change in the future when extension towers are
            supported properly.

        TESTS::

            sage: GF(5).algebraic_closure() is GF(5).algebraic_closure()
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """FiniteField.algebraic_closure(self, name='z', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1717)

        Return an algebraic closure of ``self``.

        INPUT:

        - ``name`` -- string (default: ``'z'``); prefix to use for
          variable names of subfields

        - ``implementation`` -- string (optional); specifies how to
          construct the algebraic closure.  The only value supported
          at the moment is ``'pseudo_conway'``.  For more details, see
          :mod:`~sage.rings.algebraic_closure_finite_field`.

        OUTPUT:

        An algebraic closure of ``self``.  Note that mathematically
        speaking, this is only unique up to *non-unique* isomorphism.
        To obtain canonically defined algebraic closures, one needs an
        algorithm that also provides a canonical isomorphism between
        any two algebraic closures constructed using the algorithm.

        This non-uniqueness problem can in principle be solved by
        using *Conway polynomials*; see for example
        :wikipedia:`Conway_polynomial_(finite_fields)`. These have
        the drawback that computing them takes a long time.  Therefore
        Sage implements a variant called *pseudo-Conway polynomials*,
        which are easier to compute but do not determine an algebraic
        closure up to unique isomorphism.

        The output of this method is cached, so that within the same
        Sage session, calling it multiple times will return the same
        algebraic closure (i.e. the same Sage object).  Despite this,
        the non-uniqueness of the current implementation means that
        coercion and pickling cannot work as one might expect.  See
        below for an example.

        EXAMPLES::

            sage: F = GF(5).algebraic_closure()
            sage: F
            Algebraic closure of Finite Field of size 5
            sage: F.gen(3)
            z3

        For finite fields, the algebraic closure is always (isomorphic
        to) the algebraic closure of the prime field::

            sage: GF(5^2).algebraic_closure() == F
            True

        The default name is 'z' but you can change it through the option
        ``name``::

            sage: Ft = GF(5).algebraic_closure('t')
            sage: Ft.gen(3)
            t3

        Because Sage currently only implements algebraic closures
        using a non-unique definition (see above), it is currently
        impossible to implement pickling in such a way that a pickled
        and unpickled element compares equal to the original::

            sage: F = GF(7).algebraic_closure()
            sage: x = F.gen(2)
            sage: loads(dumps(x)) == x
            False

        .. NOTE::

            For non-prime finite fields, this method currently simply
            returns the algebraic closure of the prime field. This may
            or may not change in the future when extension towers are
            supported properly.

        TESTS::

            sage: GF(5).algebraic_closure() is GF(5).algebraic_closure()
            True"""
    def an_embedding(self, K) -> Any:
        """FiniteField.an_embedding(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1823)

        Return some embedding of this field into another field `K`,
        and raise a :class:`ValueError` if none exists.

        .. SEEALSO::

            :meth:`sage.rings.ring.Field.an_embedding`

        EXAMPLES::

            sage: GF(4,'a').an_embedding(GF(2).algebraic_closure())
            Ring morphism:
              From: Finite Field in a of size 2^2
              To:   Algebraic closure of Finite Field of size 2
              Defn: a |--> ..."""
    @overload
    def cardinality(self) -> Any:
        """FiniteField.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 811)

        Return the cardinality of ``self``.

        Same as :meth:`order`.

        EXAMPLES::

            sage: GF(997).cardinality()
            997"""
    @overload
    def cardinality(self) -> Any:
        """FiniteField.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 811)

        Return the cardinality of ``self``.

        Same as :meth:`order`.

        EXAMPLES::

            sage: GF(997).cardinality()
            997"""
    @overload
    def construction(self) -> Any:
        """FiniteField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1294)

        Return the construction of this finite field, as a ``ConstructionFunctor``
        and the base field.

        EXAMPLES::

            sage: v = GF(3^3).construction(); v
            (AlgebraicExtensionFunctor, Finite Field of size 3)
            sage: v[0].polys[0]
            3
            sage: v = GF(2^1000, 'a').construction(); v[0].polys[0]
            a^1000 + a^5 + a^4 + a^3 + 1

        The implementation is taken into account, by :issue:`15223`::

            sage: k = FiniteField(9, 'a', impl='pari_ffelt')
            sage: F, R = k.construction()
            sage: F(R) is k
            True"""
    @overload
    def construction(self) -> Any:
        """FiniteField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1294)

        Return the construction of this finite field, as a ``ConstructionFunctor``
        and the base field.

        EXAMPLES::

            sage: v = GF(3^3).construction(); v
            (AlgebraicExtensionFunctor, Finite Field of size 3)
            sage: v[0].polys[0]
            3
            sage: v = GF(2^1000, 'a').construction(); v[0].polys[0]
            a^1000 + a^5 + a^4 + a^3 + 1

        The implementation is taken into account, by :issue:`15223`::

            sage: k = FiniteField(9, 'a', impl='pari_ffelt')
            sage: F, R = k.construction()
            sage: F(R) is k
            True"""
    @overload
    def construction(self) -> Any:
        """FiniteField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1294)

        Return the construction of this finite field, as a ``ConstructionFunctor``
        and the base field.

        EXAMPLES::

            sage: v = GF(3^3).construction(); v
            (AlgebraicExtensionFunctor, Finite Field of size 3)
            sage: v[0].polys[0]
            3
            sage: v = GF(2^1000, 'a').construction(); v[0].polys[0]
            a^1000 + a^5 + a^4 + a^3 + 1

        The implementation is taken into account, by :issue:`15223`::

            sage: k = FiniteField(9, 'a', impl='pari_ffelt')
            sage: F, R = k.construction()
            sage: F(R) is k
            True"""
    @overload
    def construction(self) -> Any:
        """FiniteField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1294)

        Return the construction of this finite field, as a ``ConstructionFunctor``
        and the base field.

        EXAMPLES::

            sage: v = GF(3^3).construction(); v
            (AlgebraicExtensionFunctor, Finite Field of size 3)
            sage: v[0].polys[0]
            3
            sage: v = GF(2^1000, 'a').construction(); v[0].polys[0]
            a^1000 + a^5 + a^4 + a^3 + 1

        The implementation is taken into account, by :issue:`15223`::

            sage: k = FiniteField(9, 'a', impl='pari_ffelt')
            sage: F, R = k.construction()
            sage: F(R) is k
            True"""
    def dual_basis(self, basis=..., check=...) -> Any:
        """FiniteField.dual_basis(self, basis=None, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1959)

        Return the dual basis of ``basis``, or the dual basis of the power
        basis if no basis is supplied.

        If `e = \\{e_0, e_1, ..., e_{n-1}\\}` is a basis of
        `\\GF{p^n}` as a vector space over `\\GF{p}`, then the dual basis of `e`,
        `d = \\{d_0, d_1, ..., d_{n-1}\\}`, is the unique basis such that
        `\\mathrm{Tr}(e_i d_j) = \\delta_{i,j}, 0 \\leq i,j \\leq n-1`, where
        `\\mathrm{Tr}` is the trace function.

        INPUT:

        - ``basis`` -- (default: ``None``); a basis of the finite field
          ``self``, `\\GF{p^n}`, as a vector space over the base field
          `\\GF{p}`. Uses the power basis `\\{x^i : 0 \\leq i \\leq n-1\\}` as
          input if no basis is supplied, where `x` is the generator of
          ``self``.

        - ``check`` -- (default: ``True``); verifies that ``basis`` is
          a valid basis of ``self``

        ALGORITHM:

        The algorithm used to calculate the dual basis comes from pages
        110--111 of [McE1987]_.

        Let `e = \\{e_0, e_1, ..., e_{n-1}\\}` be a basis of `\\GF{p^n}` as a
        vector space over `\\GF{p}` and `d = \\{d_0, d_1, ..., d_{n-1}\\}` be the
        dual basis of `e`. Since `e` is a basis, we can rewrite any
        `d_c, 0 \\leq c \\leq n-1`, as
        `d_c = \\beta_0 e_0 + \\beta_1 e_1 + ... + \\beta_{n-1} e_{n-1}`, for some
        `\\beta_0, \\beta_1, ..., \\beta_{n-1} \\in \\GF{p}`. Using properties of
        the trace function, we can rewrite the `n` equations of the form
        `\\mathrm{Tr}(e_i d_c) = \\delta_{i,c}` and express the result as the
        matrix vector product:
        `A [\\beta_0, \\beta_1, ..., \\beta_{n-1}] = i_c`, where the `i,j`-th
        element of `A` is `\\mathrm{Tr(e_i e_j)}` and `i_c` is the `i`-th
        column of the `n \\times n` identity matrix. Since `A` is an invertible
        matrix, `[\\beta_0, \\beta_1, ..., \\beta_{n-1}] = A^{-1} i_c`, from
        which we can easily calculate `d_c`.

        EXAMPLES::

            sage: F.<a> = GF(2^4)
            sage: F.dual_basis(basis=None, check=False)                                 # needs sage.modules
            [a^3 + 1, a^2, a, 1]

        We can test that the dual basis returned satisfies the defining
        property of a dual basis:
        `\\mathrm{Tr}(e_i d_j) = \\delta_{i,j}, 0 \\leq i,j \\leq n-1` ::

            sage: # needs sage.modules
            sage: F.<a> = GF(7^4)
            sage: e = [4*a^3, 2*a^3 + a^2 + 3*a + 5,
            ....:      3*a^3 + 5*a^2 + 4*a + 2, 2*a^3 + 2*a^2 + 2]
            sage: d = F.dual_basis(e, check=True); d
            [3*a^3 + 4*a^2 + 6*a + 2, a^3 + 6*a + 5,
            3*a^3 + 6*a^2 + 2*a + 5, 5*a^2 + 4*a + 3]
            sage: vals = [[(x * y).trace() for x in e] for y in d]
            sage: matrix(vals) == matrix.identity(4)
            True

        We can test that if `d` is the dual basis of `e`, then `e` is the dual
        basis of `d`::

            sage: # needs sage.modules
            sage: F.<a> = GF(7^8)
            sage: e = [a^0, a^1, a^2, a^3, a^4, a^5, a^6, a^7]
            sage: d = F.dual_basis(e, check=False); d
            [6*a^6 + 4*a^5 + 4*a^4 + a^3 + 6*a^2 + 3,
             6*a^7 + 4*a^6 + 4*a^5 + 2*a^4 + a^2,
             4*a^6 + 5*a^5 + 5*a^4 + 4*a^3 + 5*a^2 + a + 6,
             5*a^7 + a^6 + a^4 + 4*a^3 + 4*a^2 + 1,
             2*a^7 + 5*a^6 + a^5 + a^3 + 5*a^2 + 2*a + 4,
             a^7 + 2*a^6 + 5*a^5 + a^4 + 5*a^2 + 4*a + 4,
             a^7 + a^6 + 2*a^5 + 5*a^4 + a^3 + 4*a^2 + 4*a + 6,
             5*a^7 + a^6 + a^5 + 2*a^4 + 5*a^3 + 6*a]
            sage: F.dual_basis(d)
            [1, a, a^2, a^3, a^4, a^5, a^6, a^7]

        We cannot calculate the dual basis if ``basis`` is not a valid basis.
        ::

            sage: F.<a> = GF(2^3)
            sage: F.dual_basis([a], check=True)                                         # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: basis length should be 3, not 1

            sage: F.dual_basis([a^0, a, a^0 + a], check=True)                           # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: value of 'basis' keyword is not a basis

        AUTHOR:

        - Thomas Gagne (2015-06-16)"""
    def embeddings(self, K) -> Any:
        """FiniteField.embeddings(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1859)

        Return a list of all embeddings of this field in another field `K`.

        EXAMPLES::

            sage: GF(2).embeddings(GF(4))
            [Ring morphism:
               From: Finite Field of size 2
               To:   Finite Field in z2 of size 2^2
               Defn: 1 |--> 1]
            sage: GF(4).embeddings(GF(2).algebraic_closure())
            [Ring morphism:
               From: Finite Field in z2 of size 2^2
               To:   Algebraic closure of Finite Field of size 2
               Defn: z2 |--> z2,
             Ring morphism:
               From: Finite Field in z2 of size 2^2
               To:   Algebraic closure of Finite Field of size 2
               Defn: z2 |--> z2 + 1]"""
    @overload
    def extension(self, modulus, name=..., names=..., map=..., embedding=..., latex_name=..., latex_names=..., **kwds) -> Any:
        """FiniteField.extension(self, modulus, name=None, names=None, map=False, embedding=None, *, latex_name=None, latex_names=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1334)

        Return an extension of this finite field.

        INPUT:

        - ``modulus`` -- a polynomial with coefficients in ``self``,
          or an integer

        - ``name`` or ``names`` -- string; the name of the generator
          in the new extension

        - ``latex_name`` or ``latex_names`` -- string; latex name of
          the generator in the new extension

        - ``map`` -- boolean (default: ``False``); if ``False``,
          return just the extension `E`. If ``True``, return a pair
          `(E, f)`, where `f` is an embedding of ``self`` into `E`.

        - ``embedding`` -- currently not used; for compatibility with
          other ``AlgebraicExtensionFunctor`` calls

        - ``**kwds`` -- further keywords, passed to the finite field
          constructor.

        OUTPUT:

        An extension of the given modulus, or pseudo-Conway of the
        given degree if ``modulus`` is an integer.

        EXAMPLES::

            sage: k = GF(2)
            sage: R.<x> = k[]
            sage: k.extension(x^1000 + x^5 + x^4 + x^3 + 1, 'a')
            Finite Field in a of size 2^1000
            sage: k = GF(3^4)
            sage: R.<x> = k[]
            sage: k.extension(3)
            Finite Field in z12 of size 3^12
            sage: K = k.extension(2, 'a')
            sage: k.is_subring(K)
            True

        An example using the ``map`` argument::

            sage: F = GF(5)
            sage: E, f = F.extension(2, 'b', map=True)
            sage: E
            Finite Field in b of size 5^2
            sage: f
            Ring morphism:
              From: Finite Field of size 5
              To:   Finite Field in b of size 5^2
              Defn: 1 |--> 1
            sage: f.parent()
            Set of field embeddings
             from Finite Field of size 5
               to Finite Field in b of size 5^2

        Extensions of non-prime finite fields by polynomials are not yet
        supported: we fall back to generic code::

            sage: k.extension(x^5 + x^2 + x - 1)
            Univariate Quotient Polynomial Ring in x over Finite Field in z4 of size 3^4
             with modulus x^5 + x^2 + x + 2

        TESTS:

        We check that :issue:`18915` is fixed::

            sage: F = GF(2)
            sage: F.extension(int(3), 'a')
            Finite Field in a of size 2^3

            sage: F = GF((2,4), 'a')
            sage: F.extension(int(3), 'aa')
            Finite Field in aa of size 2^12

        Randomized test for :issue:`33937`::

            sage: p = random_prime(100)
            sage: a,b = (randrange(1,10) for _ in 'ab')
            sage: K.<u> = GF((p,a))
            sage: L.<v> = K.extension(b)
            sage: L(u).minpoly() == u.minpoly()
            True"""
    @overload
    def extension(self, b) -> Any:
        """FiniteField.extension(self, modulus, name=None, names=None, map=False, embedding=None, *, latex_name=None, latex_names=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1334)

        Return an extension of this finite field.

        INPUT:

        - ``modulus`` -- a polynomial with coefficients in ``self``,
          or an integer

        - ``name`` or ``names`` -- string; the name of the generator
          in the new extension

        - ``latex_name`` or ``latex_names`` -- string; latex name of
          the generator in the new extension

        - ``map`` -- boolean (default: ``False``); if ``False``,
          return just the extension `E`. If ``True``, return a pair
          `(E, f)`, where `f` is an embedding of ``self`` into `E`.

        - ``embedding`` -- currently not used; for compatibility with
          other ``AlgebraicExtensionFunctor`` calls

        - ``**kwds`` -- further keywords, passed to the finite field
          constructor.

        OUTPUT:

        An extension of the given modulus, or pseudo-Conway of the
        given degree if ``modulus`` is an integer.

        EXAMPLES::

            sage: k = GF(2)
            sage: R.<x> = k[]
            sage: k.extension(x^1000 + x^5 + x^4 + x^3 + 1, 'a')
            Finite Field in a of size 2^1000
            sage: k = GF(3^4)
            sage: R.<x> = k[]
            sage: k.extension(3)
            Finite Field in z12 of size 3^12
            sage: K = k.extension(2, 'a')
            sage: k.is_subring(K)
            True

        An example using the ``map`` argument::

            sage: F = GF(5)
            sage: E, f = F.extension(2, 'b', map=True)
            sage: E
            Finite Field in b of size 5^2
            sage: f
            Ring morphism:
              From: Finite Field of size 5
              To:   Finite Field in b of size 5^2
              Defn: 1 |--> 1
            sage: f.parent()
            Set of field embeddings
             from Finite Field of size 5
               to Finite Field in b of size 5^2

        Extensions of non-prime finite fields by polynomials are not yet
        supported: we fall back to generic code::

            sage: k.extension(x^5 + x^2 + x - 1)
            Univariate Quotient Polynomial Ring in x over Finite Field in z4 of size 3^4
             with modulus x^5 + x^2 + x + 2

        TESTS:

        We check that :issue:`18915` is fixed::

            sage: F = GF(2)
            sage: F.extension(int(3), 'a')
            Finite Field in a of size 2^3

            sage: F = GF((2,4), 'a')
            sage: F.extension(int(3), 'aa')
            Finite Field in aa of size 2^12

        Randomized test for :issue:`33937`::

            sage: p = random_prime(100)
            sage: a,b = (randrange(1,10) for _ in 'ab')
            sage: K.<u> = GF((p,a))
            sage: L.<v> = K.extension(b)
            sage: L(u).minpoly() == u.minpoly()
            True"""
    @overload
    def factored_order(self) -> Any:
        """FiniteField.factored_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 764)

        Return the factored order of this field.  For compatibility with
        :mod:`~sage.rings.finite_rings.integer_mod_ring`.

        EXAMPLES::

            sage: GF(7^2,'a').factored_order()
            7^2"""
    @overload
    def factored_order(self) -> Any:
        """FiniteField.factored_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 764)

        Return the factored order of this field.  For compatibility with
        :mod:`~sage.rings.finite_rings.integer_mod_ring`.

        EXAMPLES::

            sage: GF(7^2,'a').factored_order()
            7^2"""
    @overload
    def factored_unit_order(self) -> Any:
        """FiniteField.factored_unit_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 778)

        Return the factorization of ``self.order()-1``, as a 1-tuple.

        The format is for compatibility with
        :mod:`~sage.rings.finite_rings.integer_mod_ring`.

        EXAMPLES::

            sage: GF(7^2,'a').factored_unit_order()
            (2^4 * 3,)

        TESTS:

        Check that :issue:`31686` is fixed::

            sage: p = 1100585370631
            sage: F = GF(p^24, 'a')
            sage: F.factored_unit_order()
            (2^6 * 3^2 * 5 * 7 * 11 * 13 * 17 * 53 * 97 * 229 * 337 * 421
             * 3929 * 215417 * 249737 * 262519 * 397897 * 59825761 * 692192057
             * 12506651939 * 37553789761 * 46950147799 * 172462808473 * 434045140817
             * 81866093016401 * 617237859576697 * 659156729361017707
             * 268083135725348991493995910983015600019336657
             * 90433843562394341719266736354746485652016132372842876085423636587989263202299569913,)"""
    @overload
    def factored_unit_order(self) -> Any:
        """FiniteField.factored_unit_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 778)

        Return the factorization of ``self.order()-1``, as a 1-tuple.

        The format is for compatibility with
        :mod:`~sage.rings.finite_rings.integer_mod_ring`.

        EXAMPLES::

            sage: GF(7^2,'a').factored_unit_order()
            (2^4 * 3,)

        TESTS:

        Check that :issue:`31686` is fixed::

            sage: p = 1100585370631
            sage: F = GF(p^24, 'a')
            sage: F.factored_unit_order()
            (2^6 * 3^2 * 5 * 7 * 11 * 13 * 17 * 53 * 97 * 229 * 337 * 421
             * 3929 * 215417 * 249737 * 262519 * 397897 * 59825761 * 692192057
             * 12506651939 * 37553789761 * 46950147799 * 172462808473 * 434045140817
             * 81866093016401 * 617237859576697 * 659156729361017707
             * 268083135725348991493995910983015600019336657
             * 90433843562394341719266736354746485652016132372842876085423636587989263202299569913,)"""
    @overload
    def factored_unit_order(self) -> Any:
        """FiniteField.factored_unit_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 778)

        Return the factorization of ``self.order()-1``, as a 1-tuple.

        The format is for compatibility with
        :mod:`~sage.rings.finite_rings.integer_mod_ring`.

        EXAMPLES::

            sage: GF(7^2,'a').factored_unit_order()
            (2^4 * 3,)

        TESTS:

        Check that :issue:`31686` is fixed::

            sage: p = 1100585370631
            sage: F = GF(p^24, 'a')
            sage: F.factored_unit_order()
            (2^6 * 3^2 * 5 * 7 * 11 * 13 * 17 * 53 * 97 * 229 * 337 * 421
             * 3929 * 215417 * 249737 * 262519 * 397897 * 59825761 * 692192057
             * 12506651939 * 37553789761 * 46950147799 * 172462808473 * 434045140817
             * 81866093016401 * 617237859576697 * 659156729361017707
             * 268083135725348991493995910983015600019336657
             * 90433843562394341719266736354746485652016132372842876085423636587989263202299569913,)"""
    def free_module(self, base=..., basis=..., map=...) -> Any:
        """FiniteField.free_module(self, base=None, basis=None, map=True)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1055)

        Return the vector space over the subfield isomorphic to this
        finite field as a vector space, along with the isomorphisms.

        INPUT:

        - ``base`` -- a subfield of or a morphism into this finite field.
          If not given, the prime subfield is assumed. A subfield means
          a finite field with coercion to this finite field.

        - ``basis`` -- a basis of the finite field as a vector space
          over the subfield. If not given, one is chosen automatically.

        - ``map`` -- boolean (default: ``True``); if ``True``, isomorphisms
          from and to the vector space are also returned

        The ``basis`` maps to the standard basis of the vector space
        by the isomorphisms.

        OUTPUT: if ``map`` is ``False``,

        - vector space over the subfield or the domain of the morphism,
          isomorphic to this finite field.

        and if ``map`` is ``True``, then also

        - an isomorphism from the vector space to the finite field.

        - the inverse isomorphism to the vector space from the finite field.

        EXAMPLES::

            sage: GF(27,'a').vector_space(map=False)                                    # needs sage.modules
            Vector space of dimension 3 over Finite Field of size 3

            sage: # needs sage.modules
            sage: F = GF(8)
            sage: E = GF(64)
            sage: V, from_V, to_V = E.vector_space(F, map=True)
            sage: V
            Vector space of dimension 2 over Finite Field in z3 of size 2^3
            sage: to_V(E.gen())
            (0, 1)
            sage: all(from_V(to_V(e)) == e for e in E)
            True
            sage: all(to_V(e1 + e2) == to_V(e1) + to_V(e2) for e1 in E for e2 in E)
            True
            sage: all(to_V(c * e) == c * to_V(e) for e in E for c in F)
            True

            sage: # needs sage.modules
            sage: basis = [E.gen(), E.gen() + 1]
            sage: W, from_W, to_W = E.vector_space(F, basis, map=True)
            sage: all(from_W(to_W(e)) == e for e in E)
            True
            sage: all(to_W(c * e) == c * to_W(e) for e in E for c in F)
            True
            sage: all(to_W(e1 + e2) == to_W(e1) + to_W(e2) for e1 in E for e2 in E)  # long time
            True
            sage: to_W(basis[0]); to_W(basis[1])
            (1, 0)
            (0, 1)

            sage: # needs sage.modules
            sage: x = polygen(ZZ)
            sage: F = GF(9, 't', modulus=x^2 + x - 1)
            sage: E = GF(81)
            sage: h = Hom(F,E).an_element()
            sage: V, from_V, to_V = E.vector_space(h, map=True)
            sage: V
            Vector space of dimension 2 over Finite Field in t of size 3^2
            sage: V.base_ring() is F
            True
            sage: all(from_V(to_V(e)) == e for e in E)
            True
            sage: all(to_V(e1 + e2) == to_V(e1) + to_V(e2) for e1 in E for e2 in E)
            True
            sage: all(to_V(h(c) * e) == c * to_V(e) for e in E for c in F)
            True"""
    @overload
    def frobenius_endomorphism(self, n=...) -> Any:
        """FiniteField.frobenius_endomorphism(self, n=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1893)

        INPUT:

        - ``n`` -- integer (default: 1)

        OUTPUT:

        The `n`-th power of the absolute arithmetic Frobenius
        endomorphism on this finite field.

        EXAMPLES::

            sage: k.<t> = GF(3^5)
            sage: Frob = k.frobenius_endomorphism(); Frob
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5

            sage: a = k.random_element()                                                # needs sage.modules
            sage: Frob(a) == a^3                                                        # needs sage.modules
            True

        We can specify a power::

            sage: k.frobenius_endomorphism(2)
            Frobenius endomorphism t |--> t^(3^2) on Finite Field in t of size 3^5

        The result is simplified if possible::

            sage: k.frobenius_endomorphism(6)
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5
            sage: k.frobenius_endomorphism(5)
            Identity endomorphism of Finite Field in t of size 3^5

        Comparisons work::

            sage: k.frobenius_endomorphism(6) == Frob
            True
            sage: from sage.categories.morphism import IdentityMorphism
            sage: k.frobenius_endomorphism(5) == IdentityMorphism(k)
            True

        AUTHOR:

        - Xavier Caruso (2012-06-29)"""
    @overload
    def frobenius_endomorphism(self) -> Any:
        """FiniteField.frobenius_endomorphism(self, n=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1893)

        INPUT:

        - ``n`` -- integer (default: 1)

        OUTPUT:

        The `n`-th power of the absolute arithmetic Frobenius
        endomorphism on this finite field.

        EXAMPLES::

            sage: k.<t> = GF(3^5)
            sage: Frob = k.frobenius_endomorphism(); Frob
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5

            sage: a = k.random_element()                                                # needs sage.modules
            sage: Frob(a) == a^3                                                        # needs sage.modules
            True

        We can specify a power::

            sage: k.frobenius_endomorphism(2)
            Frobenius endomorphism t |--> t^(3^2) on Finite Field in t of size 3^5

        The result is simplified if possible::

            sage: k.frobenius_endomorphism(6)
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5
            sage: k.frobenius_endomorphism(5)
            Identity endomorphism of Finite Field in t of size 3^5

        Comparisons work::

            sage: k.frobenius_endomorphism(6) == Frob
            True
            sage: from sage.categories.morphism import IdentityMorphism
            sage: k.frobenius_endomorphism(5) == IdentityMorphism(k)
            True

        AUTHOR:

        - Xavier Caruso (2012-06-29)"""
    @overload
    def from_bytes(self, input_bytes, byteorder=...) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self, input_bytes) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self, input_bytes, byteorder=...) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self, input_bytes) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self, input_bytes, byteorder=...) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_bytes(self, a_bytes, byteorder=...) -> Any:
        '''FiniteField.from_bytes(self, input_bytes, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 2078)

        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes`` (can only be ``\'big\'`` or ``\'little\'``)

        EXAMPLES::

            sage: input_bytes = b"some_bytes"
            sage: F = GF(2**127 - 1)
            sage: F.from_bytes(input_bytes)
            545127616933790290830707
            sage: a = F.from_bytes(input_bytes, byteorder=\'little\'); a
            544943659528996309004147
            sage: type(a)
            <class \'sage.rings.finite_rings.integer_mod.IntegerMod_gmp\'>

        ::

            sage: input_bytes = b"some_bytes"
            sage: F_ext = GF(65537**5)
            sage: F_ext.from_bytes(input_bytes)
            29549*z5^4 + 40876*z5^3 + 52171*z5^2 + 13604*z5 + 20843
            sage: F_ext.from_bytes(input_bytes, byteorder=\'little\')
            29539*z5^4 + 42728*z5^3 + 47440*z5^2 + 12423*z5 + 27473

        TESTS::

            sage: fields = [GF(2), GF(3), GF(65537), GF(2^10), GF(163^5)]
            sage: for F in fields:
            ....:     for _ in range(1000):
            ....:         a = F.random_element()
            ....:         order = choice(["little", "big"])
            ....:         a_bytes = a.to_bytes(byteorder=order)
            ....:         assert F.from_bytes(a_bytes, byteorder=order) == a'''
    @overload
    def from_integer(self, n, reverse=...) -> Any:
        """FiniteField.from_integer(self, n, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 396)

        Return the finite field element obtained by reinterpreting the base-`p`
        expansion of `n` as a polynomial and evaluating it at the generator of
        this finite field.

        If ``reverse`` is set to ``True`` (default: ``False``),
        the list of digits is reversed prior to evaluation.

        Inverse of :meth:`sage.rings.finite_rings.element_base.FinitePolyExtElement.to_integer`.

        INPUT:

        - ``n`` -- integer between `0` and the cardinality of this field minus `1`

        EXAMPLES::

            sage: p = 4091
            sage: F = GF(p^4, 'a')
            sage: n = 100*p^3 + 37*p^2 + 12*p + 6
            sage: F.from_integer(n)
            100*a^3 + 37*a^2 + 12*a + 6
            sage: F.from_integer(n) in F
            True
            sage: F.from_integer(n, reverse=True)
            6*a^3 + 12*a^2 + 37*a + 100

        TESTS::

            sage: F = GF(19^5)
            sage: F.from_integer(0)
            0
            sage: _.parent()
            Finite Field in ... of size 19^5
            sage: F.from_integer(-5)
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()
            sage: F.from_integer(F.cardinality())
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()"""
    @overload
    def from_integer(self, n) -> Any:
        """FiniteField.from_integer(self, n, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 396)

        Return the finite field element obtained by reinterpreting the base-`p`
        expansion of `n` as a polynomial and evaluating it at the generator of
        this finite field.

        If ``reverse`` is set to ``True`` (default: ``False``),
        the list of digits is reversed prior to evaluation.

        Inverse of :meth:`sage.rings.finite_rings.element_base.FinitePolyExtElement.to_integer`.

        INPUT:

        - ``n`` -- integer between `0` and the cardinality of this field minus `1`

        EXAMPLES::

            sage: p = 4091
            sage: F = GF(p^4, 'a')
            sage: n = 100*p^3 + 37*p^2 + 12*p + 6
            sage: F.from_integer(n)
            100*a^3 + 37*a^2 + 12*a + 6
            sage: F.from_integer(n) in F
            True
            sage: F.from_integer(n, reverse=True)
            6*a^3 + 12*a^2 + 37*a + 100

        TESTS::

            sage: F = GF(19^5)
            sage: F.from_integer(0)
            0
            sage: _.parent()
            Finite Field in ... of size 19^5
            sage: F.from_integer(-5)
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()
            sage: F.from_integer(F.cardinality())
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()"""
    @overload
    def from_integer(self, n) -> Any:
        """FiniteField.from_integer(self, n, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 396)

        Return the finite field element obtained by reinterpreting the base-`p`
        expansion of `n` as a polynomial and evaluating it at the generator of
        this finite field.

        If ``reverse`` is set to ``True`` (default: ``False``),
        the list of digits is reversed prior to evaluation.

        Inverse of :meth:`sage.rings.finite_rings.element_base.FinitePolyExtElement.to_integer`.

        INPUT:

        - ``n`` -- integer between `0` and the cardinality of this field minus `1`

        EXAMPLES::

            sage: p = 4091
            sage: F = GF(p^4, 'a')
            sage: n = 100*p^3 + 37*p^2 + 12*p + 6
            sage: F.from_integer(n)
            100*a^3 + 37*a^2 + 12*a + 6
            sage: F.from_integer(n) in F
            True
            sage: F.from_integer(n, reverse=True)
            6*a^3 + 12*a^2 + 37*a + 100

        TESTS::

            sage: F = GF(19^5)
            sage: F.from_integer(0)
            0
            sage: _.parent()
            Finite Field in ... of size 19^5
            sage: F.from_integer(-5)
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()
            sage: F.from_integer(F.cardinality())
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()"""
    @overload
    def from_integer(self, n, reverse=...) -> Any:
        """FiniteField.from_integer(self, n, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 396)

        Return the finite field element obtained by reinterpreting the base-`p`
        expansion of `n` as a polynomial and evaluating it at the generator of
        this finite field.

        If ``reverse`` is set to ``True`` (default: ``False``),
        the list of digits is reversed prior to evaluation.

        Inverse of :meth:`sage.rings.finite_rings.element_base.FinitePolyExtElement.to_integer`.

        INPUT:

        - ``n`` -- integer between `0` and the cardinality of this field minus `1`

        EXAMPLES::

            sage: p = 4091
            sage: F = GF(p^4, 'a')
            sage: n = 100*p^3 + 37*p^2 + 12*p + 6
            sage: F.from_integer(n)
            100*a^3 + 37*a^2 + 12*a + 6
            sage: F.from_integer(n) in F
            True
            sage: F.from_integer(n, reverse=True)
            6*a^3 + 12*a^2 + 37*a + 100

        TESTS::

            sage: F = GF(19^5)
            sage: F.from_integer(0)
            0
            sage: _.parent()
            Finite Field in ... of size 19^5
            sage: F.from_integer(-5)
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()
            sage: F.from_integer(F.cardinality())
            Traceback (most recent call last):
            ...
            ValueError: n must be between 0 and self.order()"""
    @overload
    def galois_group(self) -> Any:
        """FiniteField.galois_group(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1941)

        Return the Galois group of this finite field, a cyclic group generated by Frobenius.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = GF(3^6).galois_group(); G
            Galois group C6 of GF(3^6)
            sage: F = G.gen()
            sage: F^2
            Frob^2
            sage: F^6
            1"""
    @overload
    def galois_group(self) -> Any:
        """FiniteField.galois_group(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1941)

        Return the Galois group of this finite field, a cyclic group generated by Frobenius.

        EXAMPLES::

            sage: # needs sage.groups
            sage: G = GF(3^6).galois_group(); G
            Galois group C6 of GF(3^6)
            sage: F = G.gen()
            sage: F^2
            Frob^2
            sage: F^6
            1"""
    @overload
    def gen(self) -> Any:
        """FiniteField.gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 631)

        Return a generator of this field (over its prime field). As this is an
        abstract base class, this just raises a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: K = GF(17)
            sage: sage.rings.finite_rings.finite_field_base.FiniteField.gen(K)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def gen(self, K) -> Any:
        """FiniteField.gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 631)

        Return a generator of this field (over its prime field). As this is an
        abstract base class, this just raises a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: K = GF(17)
            sage: sage.rings.finite_rings.finite_field_base.FiniteField.gen(K)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def is_conway(self) -> Any:
        """FiniteField.is_conway(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1803)

        Return ``True`` if ``self`` is defined by a Conway polynomial.

        EXAMPLES::

            sage: GF(5^3, 'a').is_conway()
            True
            sage: GF(5^3, 'a', modulus='adleman-lenstra').is_conway()
            False
            sage: GF(next_prime(2^16, 2), 'a').is_conway()
            False"""
    @overload
    def is_conway(self) -> Any:
        """FiniteField.is_conway(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1803)

        Return ``True`` if ``self`` is defined by a Conway polynomial.

        EXAMPLES::

            sage: GF(5^3, 'a').is_conway()
            True
            sage: GF(5^3, 'a', modulus='adleman-lenstra').is_conway()
            False
            sage: GF(next_prime(2^16, 2), 'a').is_conway()
            False"""
    @overload
    def is_conway(self) -> Any:
        """FiniteField.is_conway(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1803)

        Return ``True`` if ``self`` is defined by a Conway polynomial.

        EXAMPLES::

            sage: GF(5^3, 'a').is_conway()
            True
            sage: GF(5^3, 'a', modulus='adleman-lenstra').is_conway()
            False
            sage: GF(next_prime(2^16, 2), 'a').is_conway()
            False"""
    @overload
    def is_conway(self) -> Any:
        """FiniteField.is_conway(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1803)

        Return ``True`` if ``self`` is defined by a Conway polynomial.

        EXAMPLES::

            sage: GF(5^3, 'a').is_conway()
            True
            sage: GF(5^3, 'a', modulus='adleman-lenstra').is_conway()
            False
            sage: GF(next_prime(2^16, 2), 'a').is_conway()
            False"""
    @overload
    def is_prime_field(self) -> Any:
        """FiniteField.is_prime_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 826)

        Return ``True`` if ``self`` is a prime field, i.e., has degree 1.

        EXAMPLES::

            sage: GF(3^7, 'a').is_prime_field()
            False
            sage: GF(3, 'a').is_prime_field()
            True"""
    @overload
    def is_prime_field(self) -> Any:
        """FiniteField.is_prime_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 826)

        Return ``True`` if ``self`` is a prime field, i.e., has degree 1.

        EXAMPLES::

            sage: GF(3^7, 'a').is_prime_field()
            False
            sage: GF(3, 'a').is_prime_field()
            True"""
    @overload
    def is_prime_field(self) -> Any:
        """FiniteField.is_prime_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 826)

        Return ``True`` if ``self`` is a prime field, i.e., has degree 1.

        EXAMPLES::

            sage: GF(3^7, 'a').is_prime_field()
            False
            sage: GF(3, 'a').is_prime_field()
            True"""
    def modulus(self) -> Any:
        """FiniteField.modulus(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 839)

        Return the minimal polynomial of the generator of ``self`` over
        the prime finite field.

        The minimal polynomial of an element `a` in a field is the
        unique monic irreducible polynomial of smallest degree with
        coefficients in the base field that has `a` as a root. In
        finite field extensions, `\\GF{p^n}`, the base field is `\\GF{p}`.

        OUTPUT: a monic polynomial over `\\GF{p}` in the variable `x`

        EXAMPLES::

            sage: F.<a> = GF(7^2); F
            Finite Field in a of size 7^2
            sage: F.polynomial_ring()
            Univariate Polynomial Ring in a over Finite Field of size 7
            sage: f = F.modulus(); f
            x^2 + 6*x + 3
            sage: f(a)
            0

        Although `f` is irreducible over the base field, we can double-check
        whether or not `f` factors in `F` as follows. The command
        ``F['x'](f)`` coerces `f` as a polynomial with coefficients in `F`.
        (Instead of a polynomial with coefficients over the base field.)

        ::

            sage: f.factor()
            x^2 + 6*x + 3
            sage: F['x'](f).factor()
            (x + a + 6) * (x + 6*a)

        Here is an example with a degree 3 extension::

            sage: G.<b> = GF(7^3); G
            Finite Field in b of size 7^3
            sage: g = G.modulus(); g
            x^3 + 6*x^2 + 4
            sage: g.degree(); G.degree()
            3
            3

        For prime fields, this returns `x - 1` unless a custom modulus
        was given when constructing this field::

            sage: k = GF(199)
            sage: k.modulus()
            x + 198
            sage: var('x')
            x
            sage: k = GF(199, modulus=x+1)
            sage: k.modulus()
            x + 1

        The given modulus is always made monic::

            sage: k.<a> = GF(7^2, modulus=2*x^2 - 3, impl='pari_ffelt')
            sage: k.modulus()
            x^2 + 2

        TESTS:

        We test the various finite field implementations::

            sage: GF(2, impl='modn').modulus()
            x + 1
            sage: GF(2, impl='givaro').modulus()                                        # needs sage.libs.linbox
            x + 1
            sage: GF(2, impl='ntl').modulus()                                           # needs sage.libs.ntl
            x + 1
            sage: GF(2, impl='modn', modulus=x).modulus()
            x
            sage: GF(2, impl='givaro', modulus=x).modulus()                             # needs sage.libs.linbox
            x
            sage: GF(2, impl='ntl', modulus=x).modulus()                                # needs sage.libs.ntl
            x
            sage: GF(13^2, 'a', impl='givaro', modulus=x^2 + 2).modulus()               # needs sage.libs.linbox
            x^2 + 2
            sage: GF(13^2, 'a', impl='pari_ffelt', modulus=x^2 + 2).modulus()           # needs sage.libs.pari
            x^2 + 2"""
    @overload
    def multiplicative_generator(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def multiplicative_generator(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def multiplicative_generator(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def multiplicative_generator(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def multiplicative_generator(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def ngens(self) -> Any:
        """FiniteField.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 739)

        The number of generators of the finite field.  Always 1.

        EXAMPLES::

            sage: k = FiniteField(3^4, 'b')
            sage: k.ngens()
            1"""
    @overload
    def ngens(self) -> Any:
        """FiniteField.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 739)

        The number of generators of the finite field.  Always 1.

        EXAMPLES::

            sage: k = FiniteField(3^4, 'b')
            sage: k.ngens()
            1"""
    @overload
    def order(self) -> Any:
        """FiniteField.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 751)

        Return the order of this finite field.

        EXAMPLES::

            sage: GF(997).order()
            997"""
    @overload
    def order(self) -> Any:
        """FiniteField.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 751)

        Return the order of this finite field.

        EXAMPLES::

            sage: GF(997).order()
            997"""
    def polynomial(self, name=...) -> Any:
        """FiniteField.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 935)

        Return the minimal polynomial of the generator of ``self`` over
        the prime finite field.

        INPUT:

        - ``name`` -- a variable name to use for the polynomial. By
          default, use the name given when constructing this field.

        OUTPUT: a monic polynomial over `\\GF{p}` in the variable ``name``

        .. SEEALSO::

            Except for the ``name`` argument, this is identical to the
            :meth:`modulus` method.

        EXAMPLES::

            sage: k.<a> = FiniteField(9)
            sage: k.polynomial('x')
            x^2 + 2*x + 2
            sage: k.polynomial()
            a^2 + 2*a + 2

            sage: F = FiniteField(9, 'a', impl='pari_ffelt')
            sage: F.polynomial()
            a^2 + 2*a + 2

            sage: F = FiniteField(7^20, 'a', impl='pari_ffelt')
            sage: f = F.polynomial(); f
            a^20 + a^12 + 6*a^11 + 2*a^10 + 5*a^9 + 2*a^8 + 3*a^7 + a^6 + 3*a^5 + 3*a^3 + a + 3
            sage: f(F.gen())
            0

            sage: # needs sage.libs.ntl
            sage: k.<a> = GF(2^20, impl='ntl')
            sage: k.polynomial()
            a^20 + a^10 + a^9 + a^7 + a^6 + a^5 + a^4 + a + 1
            sage: k.polynomial('FOO')
            FOO^20 + FOO^10 + FOO^9 + FOO^7 + FOO^6 + FOO^5 + FOO^4 + FOO + 1
            sage: a^20
            a^10 + a^9 + a^7 + a^6 + a^5 + a^4 + a + 1"""
    @overload
    def polynomial_ring(self, variable_name=...) -> Any:
        """FiniteField.polynomial_ring(self, variable_name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1032)

        Return the polynomial ring over the prime subfield in the
        same variable as this finite field.

        EXAMPLES::

            sage: k.<alpha> = FiniteField(3^4)
            sage: k.polynomial_ring()
            Univariate Polynomial Ring in alpha over Finite Field of size 3"""
    @overload
    def polynomial_ring(self) -> Any:
        """FiniteField.polynomial_ring(self, variable_name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1032)

        Return the polynomial ring over the prime subfield in the
        same variable as this finite field.

        EXAMPLES::

            sage: k.<alpha> = FiniteField(3^4)
            sage: k.polynomial_ring()
            Univariate Polynomial Ring in alpha over Finite Field of size 3"""
    @overload
    def primitive_element(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def primitive_element(self) -> Any:
        """FiniteField.multiplicative_generator(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 646)

        Return a primitive element of this finite field, i.e. a
        generator of the multiplicative group.

        You can use :meth:`multiplicative_generator()` or
        :meth:`primitive_element()`, these mean the same thing.

        .. WARNING::

           This generator might change from one version of Sage to another.

        EXAMPLES::

            sage: k = GF(997)
            sage: k.multiplicative_generator()
            7
            sage: k.<a> = GF(11^3)
            sage: k.primitive_element()
            a
            sage: k.<b> = GF(19^32)
            sage: k.multiplicative_generator()
            b + 4

        TESTS:

        Check that large characteristics work (:issue:`11946`)::

            sage: p = 10^20 + 39
            sage: x = polygen(GF(p))
            sage: K.<a> = GF(p^2, modulus=x^2+1)
            sage: K.multiplicative_generator()
            a + 12"""
    @overload
    def random_element(self, *args, **kwds) -> Any:
        """FiniteField.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 998)

        A random element of the finite field.  Passes arguments to
        ``random_element()`` function of underlying vector space.

        EXAMPLES::

            sage: k = GF(19^4, 'a')
            sage: k.random_element().parent() is k                                      # needs sage.modules
            True

        Passes extra positional or keyword arguments through::

            sage: k.random_element(prob=0)                                              # needs sage.modules
            0"""
    @overload
    def random_element(self) -> Any:
        """FiniteField.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 998)

        A random element of the finite field.  Passes arguments to
        ``random_element()`` function of underlying vector space.

        EXAMPLES::

            sage: k = GF(19^4, 'a')
            sage: k.random_element().parent() is k                                      # needs sage.modules
            True

        Passes extra positional or keyword arguments through::

            sage: k.random_element(prob=0)                                              # needs sage.modules
            0"""
    @overload
    def random_element(self) -> Any:
        """FiniteField.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 998)

        A random element of the finite field.  Passes arguments to
        ``random_element()`` function of underlying vector space.

        EXAMPLES::

            sage: k = GF(19^4, 'a')
            sage: k.random_element().parent() is k                                      # needs sage.modules
            True

        Passes extra positional or keyword arguments through::

            sage: k.random_element(prob=0)                                              # needs sage.modules
            0"""
    @overload
    def random_element(self, prob=...) -> Any:
        """FiniteField.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 998)

        A random element of the finite field.  Passes arguments to
        ``random_element()`` function of underlying vector space.

        EXAMPLES::

            sage: k = GF(19^4, 'a')
            sage: k.random_element().parent() is k                                      # needs sage.modules
            True

        Passes extra positional or keyword arguments through::

            sage: k.random_element(prob=0)                                              # needs sage.modules
            0"""
    @overload
    def some_elements(self) -> Any:
        """FiniteField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1019)

        Return a collection of elements of this finite field for use in unit
        testing.

        EXAMPLES::

            sage: k = GF(2^8,'a')
            sage: k.some_elements()  # random output                                    # needs sage.modules
            [a^4 + a^3 + 1, a^6 + a^4 + a^3, a^5 + a^4 + a, a^2 + a]"""
    @overload
    def some_elements(self) -> Any:
        """FiniteField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1019)

        Return a collection of elements of this finite field for use in unit
        testing.

        EXAMPLES::

            sage: k = GF(2^8,'a')
            sage: k.some_elements()  # random output                                    # needs sage.modules
            [a^4 + a^3 + 1, a^6 + a^4 + a^3, a^5 + a^4 + a, a^2 + a]"""
    def subfield(self, degree, name=..., map=...) -> Any:
        """FiniteField.subfield(self, degree, name=None, map=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1521)

        Return the subfield of the field of ``degree``.

        The inclusion maps between these subfields will always commute, but they are only added as coercion maps
        if the following condition holds for the generator `g` of the field, where `d` is the degree of this field
        over the prime field:

        The element `g^{(p^d - 1)/(p^n - 1)}` generates the subfield of degree `n` for all divisors `n` of `d`.

        INPUT:

        - ``degree`` -- integer; degree of the subfield

        - ``name`` -- string; name of the generator of the subfield

        - ``map`` -- boolean (default: ``False``); whether to also return the inclusion map

        EXAMPLES::

            sage: k = GF(2^21)
            sage: k.subfield(3)
            Finite Field in z3 of size 2^3
            sage: k.subfield(7, 'a')
            Finite Field in a of size 2^7
            sage: k.coerce_map_from(_)
            Ring morphism:
              From: Finite Field in a of size 2^7
              To:   Finite Field in z21 of size 2^21
              Defn: a |--> z21^20 + z21^19 + z21^17 + z21^15 + z21^14 + z21^6 + z21^4 + z21^3 + z21
            sage: k.subfield(8)
            Traceback (most recent call last):
            ...
            ValueError: no subfield of order 2^8

        TESTS:

        We check that :issue:`23801` is resolved::

            sage: k.<a> = GF(5^240)
            sage: l, inc = k.subfield(3, 'z', map=True); l
            Finite Field in z of size 5^3
            sage: inc
            Ring morphism:
              From: Finite Field in z of size 5^3
              To:   Finite Field in a of size 5^240
              Defn: z |--> ...

        There is no coercion since we can't ensure compatibility with larger
        fields in this case::

            sage: k.has_coerce_map_from(l)
            False

        But there is still a compatibility among the generators chosen for the subfields::

            sage: ll, iinc = k.subfield(12, 'w', map=True)
            sage: x = iinc(ll.gen())^((5^12-1)/(5^3-1))
            sage: x.minimal_polynomial() == l.modulus()
            True

            sage: S = GF(37^16).subfields()
            sage: len(S) == len(16.divisors())
            True
            sage: all(f is not None for (l, f) in S)
            True

            sage: S = GF(2^93).subfields()
            sage: len(S) == len(93.divisors())
            True
            sage: all(f is not None for (l, f) in S)
            True

        We choose a default variable name::

            sage: GF(3^8, 'a').subfield(4)
            Finite Field in a4 of size 3^4"""
    @overload
    def subfields(self, degree=..., name=...) -> Any:
        """FiniteField.subfields(self, degree=0, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1637)

        Return all subfields of ``self`` of the given ``degree``,
        or all possible degrees if ``degree`` is `0`.

        The subfields are returned as absolute fields together with
        an embedding into ``self``.

        INPUT:

        - ``degree`` -- integer (default: `0`)

        - ``name`` -- string; a dictionary or ``None``:

          - If ``degree`` is nonzero, then ``name`` must be a string
            (or ``None``, if this is a pseudo-Conway extension),
            and will be the variable name of the returned field.
          - If ``degree`` is zero, the dictionary should have keys the divisors
            of the degree of this field, with the desired variable name for the
            field of that degree as an entry.
          - As a shortcut, you can provide a string and the degree of each
            subfield will be appended for the variable name of that subfield.
          - If ``None``, uses the prefix of this field.

        OUTPUT:

        A list of pairs ``(K, e)``, where ``K`` ranges over the subfields of
        this field and ``e`` gives an embedding of ``K`` into ``self``.

        EXAMPLES::

            sage: k = GF(2^21)
            sage: k.subfields()
            [(Finite Field of size 2,
              Ring morphism:
                  From: Finite Field of size 2
                  To:   Finite Field in z21 of size 2^21
                  Defn: 1 |--> 1),
             (Finite Field in z3 of size 2^3,
              Ring morphism:
                  From: Finite Field in z3 of size 2^3
                  To:   Finite Field in z21 of size 2^21
                  Defn: z3 |--> z21^20 + z21^19 + z21^17 + z21^15 + z21^11
                                 + z21^9 + z21^8 + z21^6 + z21^2),
             (Finite Field in z7 of size 2^7,
              Ring morphism:
                  From: Finite Field in z7 of size 2^7
                  To:   Finite Field in z21 of size 2^21
                  Defn: z7 |--> z21^20 + z21^19 + z21^17 + z21^15 + z21^14
                                 + z21^6 + z21^4 + z21^3 + z21),
             (Finite Field in z21 of size 2^21,
              Identity endomorphism of Finite Field in z21 of size 2^21)]"""
    @overload
    def subfields(self) -> Any:
        """FiniteField.subfields(self, degree=0, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 1637)

        Return all subfields of ``self`` of the given ``degree``,
        or all possible degrees if ``degree`` is `0`.

        The subfields are returned as absolute fields together with
        an embedding into ``self``.

        INPUT:

        - ``degree`` -- integer (default: `0`)

        - ``name`` -- string; a dictionary or ``None``:

          - If ``degree`` is nonzero, then ``name`` must be a string
            (or ``None``, if this is a pseudo-Conway extension),
            and will be the variable name of the returned field.
          - If ``degree`` is zero, the dictionary should have keys the divisors
            of the degree of this field, with the desired variable name for the
            field of that degree as an entry.
          - As a shortcut, you can provide a string and the degree of each
            subfield will be appended for the variable name of that subfield.
          - If ``None``, uses the prefix of this field.

        OUTPUT:

        A list of pairs ``(K, e)``, where ``K`` ranges over the subfields of
        this field and ``e`` gives an embedding of ``K`` into ``self``.

        EXAMPLES::

            sage: k = GF(2^21)
            sage: k.subfields()
            [(Finite Field of size 2,
              Ring morphism:
                  From: Finite Field of size 2
                  To:   Finite Field in z21 of size 2^21
                  Defn: 1 |--> 1),
             (Finite Field in z3 of size 2^3,
              Ring morphism:
                  From: Finite Field in z3 of size 2^3
                  To:   Finite Field in z21 of size 2^21
                  Defn: z3 |--> z21^20 + z21^19 + z21^17 + z21^15 + z21^11
                                 + z21^9 + z21^8 + z21^6 + z21^2),
             (Finite Field in z7 of size 2^7,
              Ring morphism:
                  From: Finite Field in z7 of size 2^7
                  To:   Finite Field in z21 of size 2^21
                  Defn: z7 |--> z21^20 + z21^19 + z21^17 + z21^15 + z21^14
                                 + z21^6 + z21^4 + z21^3 + z21),
             (Finite Field in z21 of size 2^21,
              Identity endomorphism of Finite Field in z21 of size 2^21)]"""
    @overload
    def unit_group_exponent(self) -> Any:
        """FiniteField.unit_group_exponent(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 983)

        The exponent of the unit group of the finite field.  For a
        finite field, this is always the order minus 1.

        EXAMPLES::

            sage: k = GF(2^10, 'a')
            sage: k.order()
            1024
            sage: k.unit_group_exponent()
            1023"""
    @overload
    def unit_group_exponent(self) -> Any:
        """FiniteField.unit_group_exponent(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 983)

        The exponent of the unit group of the finite field.  For a
        finite field, this is always the order minus 1.

        EXAMPLES::

            sage: k = GF(2^10, 'a')
            sage: k.order()
            1024
            sage: k.unit_group_exponent()
            1023"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """FiniteField.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 82)

        The hash provided by this class coincides with that of ``<class 'object'>``.

        TESTS::

            sage: F.<a> = FiniteField(2^3)
            sage: hash(F) == hash(F)
            True
            sage: hash(F) == object.__hash__(F)
            True"""
    @overload
    def __hash__(self, F) -> Any:
        """FiniteField.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 82)

        The hash provided by this class coincides with that of ``<class 'object'>``.

        TESTS::

            sage: F.<a> = FiniteField(2^3)
            sage: hash(F) == hash(F)
            True
            sage: hash(F) == object.__hash__(F)
            True"""
    def __iter__(self) -> Any:
        """FiniteField.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 300)

        Iterate over all elements of this finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='pari')
            sage: list(k)
            [0, 1, 2, a, a + 1, a + 2, 2*a, 2*a + 1, 2*a + 2]

        Partial iteration of a very large finite field::

            sage: p = next_prime(2^64)
            sage: k.<a> = FiniteField(p^2, impl='pari')
            sage: it = iter(k); it
            <...generator object at ...>
            sage: [next(it) for i in range(10)]
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Check that the generic implementation works in all cases::

            sage: L = []
            sage: from sage.rings.finite_rings.finite_field_base import FiniteField
            sage: print(list(FiniteField.__iter__(GF(8, impl='givaro', names='z'))))    # needs sage.libs.linbox
            [0, 1, z, z + 1, z^2, z^2 + 1, z^2 + z, z^2 + z + 1]
            sage: print(list(FiniteField.__iter__(GF(8, impl='pari', names='z'))))
            [0, 1, z, z + 1, z^2, z^2 + 1, z^2 + z, z^2 + z + 1]
            sage: print(list(FiniteField.__iter__(GF(8, impl='ntl', names='z'))))       # needs sage.libs.ntl
            [0, 1, z, z + 1, z^2, z^2 + 1, z^2 + z, z^2 + z + 1]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> int:
        """FiniteField.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/finite_field_base.pyx (starting at line 811)

        Return the cardinality of ``self``.

        Same as :meth:`order`.

        EXAMPLES::

            sage: GF(997).cardinality()
            997"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
