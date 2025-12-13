from . import classical as classical
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.combinat.sf.sfa import SymmetricFunctionsFunctor as SymmetricFunctionsFunctor
from sage.matrix.constructor import matrix as matrix
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class SymmetricFunctionAlgebra_dual(classical.SymmetricFunctionAlgebra_classical):
    @staticmethod
    def __classcall__(cls, dual_basis, scalar, scalar_name: str = '', basis_name=None, prefix=None):
        """
        Normalize the arguments.

        TESTS::

            sage: w = SymmetricFunctions(QQ).w()
            sage: B1 = w.dual_basis()
            sage: B2 = w.dual_basis(prefix='d_w')
            sage: B1 is B2
            True
        """
    def __init__(self, dual_basis, scalar, scalar_name, basis_name, prefix) -> None:
        '''
        Generic dual basis of a basis of symmetric functions.

        INPUT:

        - ``dual_basis`` -- a basis of the ring of symmetric functions

        - ``scalar`` -- a function `z` on partitions which determines the
          scalar product on the power sum basis by
          `\\langle p_{\\mu}, p_{\\mu} \\rangle = z(\\mu)`. (Independently on the
          function chosen, the power sum basis will always be orthogonal; the
          function ``scalar`` only determines the norms of the basis elements.)
          This defaults to the function ``zee`` defined in
          ``sage.combinat.sf.sfa``, that is, the function is defined by:

          .. MATH::

              \\lambda \\mapsto \\prod_{i = 1}^\\infty m_i(\\lambda)!
              i^{m_i(\\lambda)}`,

          where `m_i(\\lambda)` means the number of times `i` appears in
          `\\lambda`. This default function gives the standard Hall scalar
          product on the ring of symmetric functions.

        - ``scalar_name`` -- (default: the empty string) a string giving a
          description of the scalar product specified by the parameter
          ``scalar``

        - ``basis_name`` -- (optional) a string to serve as name for the basis
          to be generated (such as "forgotten" in "the forgotten basis"); don\'t
          set it to any of the already existing basis names (such as
          ``homogeneous``, ``monomial``, ``forgotten``, etc.).

        - ``prefix`` -- (default: ``\'d\'`` and the prefix for ``dual_basis``)
          a string to use as the symbol for the basis

        OUTPUT:

        The basis of the ring of symmetric functions dual to the basis
        ``dual_basis`` with respect to the scalar product determined
        by ``scalar``.

        EXAMPLES::

            sage: e = SymmetricFunctions(QQ).e()
            sage: f = e.dual_basis(prefix=\'m\', basis_name="Forgotten symmetric functions"); f
            Symmetric Functions over Rational Field in the Forgotten symmetric functions basis
            sage: TestSuite(f).run(elements=[f[1,1]+2*f[2], f[1]+3*f[1,1]])
            sage: TestSuite(f).run() # long time (11s on sage.math, 2011)

        This class defines canonical coercions between ``self`` and
        ``self^*``, as follow:

        Lookup for the canonical isomorphism from ``self`` to `P`
        (=powersum), and build the adjoint isomorphism from `P^*` to
        ``self^*``. Since `P` is self-adjoint for this scalar product,
        derive an isomorphism from `P` to ``self^*``, and by composition
        with the above get an isomorphism from ``self`` to ``self^*`` (and
        similarly for the isomorphism ``self^*`` to ``self``).

        This should be striped down to just (auto?) defining canonical
        isomorphism by adjunction (as in MuPAD-Combinat), and let
        the coercion handle the rest.

        Inversions may not be possible if the base ring is not a field::

            sage: m = SymmetricFunctions(ZZ).m()
            sage: h = m.dual_basis(lambda x: 1)
            sage: h[2,1]
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        By transitivity, this defines indirect coercions to and from all other bases::

            sage: s = SymmetricFunctions(QQ[\'t\'].fraction_field()).s()
            sage: t = QQ[\'t\'].fraction_field().gen()
            sage: zee_hl = lambda x: x.centralizer_size(t=t)
            sage: S = s.dual_basis(zee_hl)
            sage: S(s([2,1]))
            (-t/(t^5-2*t^4+t^3-t^2+2*t-1))*d_s[1, 1, 1] + ((-t^2-1)/(t^5-2*t^4+t^3-t^2+2*t-1))*d_s[2, 1] + (-t/(t^5-2*t^4+t^3-t^2+2*t-1))*d_s[3]

        TESTS:

        Regression test for :issue:`12489`. This issue improving
        equality test revealed that the conversion back from the dual
        basis did not strip cancelled terms from the dictionary::

            sage: y = e[1, 1, 1, 1] - 2*e[2, 1, 1] + e[2, 2]
            sage: sorted(f.element_class(f, dual = y))
            [([1, 1, 1, 1], 6), ([2, 1, 1], 2), ([2, 2], 1)]
        '''
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: w = SymmetricFunctions(ZZ).witt()
            sage: w.dual_basis().construction()
            (SymmetricFunctionsFunctor[dual Witt], Integer Ring)
        """
    def basis_name(self):
        """
        Return the name of the basis of ``self``.

        This is used for output and, for the classical bases of
        symmetric functions, to connect this basis with :ref:`Symmetrica <spkg_symmetrica>`.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: f = Sym.f()
            sage: f.basis_name()
            'forgotten'
        """
    def transition_matrix(self, basis, n):
        """
        Return the transition matrix between the `n`-th homogeneous components
        of ``self`` and ``basis``.

        INPUT:

        - ``basis`` -- a target basis of the ring of symmetric functions
        - ``n`` -- nonnegative integer

        OUTPUT:

        - A transition matrix from ``self`` to ``basis`` for the elements
          of degree ``n``.  The indexing order of the rows and
          columns is the order of ``Partitions(n)``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.schur()
            sage: e = Sym.elementary()
            sage: f = e.dual_basis()
            sage: f.transition_matrix(s, 5)
            [ 1 -1  0  1  0 -1  1]
            [-2  1  1 -1 -1  1  0]
            [-2  2 -1 -1  1  0  0]
            [ 3 -1 -1  1  0  0  0]
            [ 3 -2  1  0  0  0  0]
            [-4  1  0  0  0  0  0]
            [ 1  0  0  0  0  0  0]
            sage: Partitions(5).list()
            [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
            sage: s(f[2,2,1])
            s[3, 2] - 2*s[4, 1] + 3*s[5]
            sage: e.transition_matrix(s, 5).inverse().transpose()
            [ 1 -1  0  1  0 -1  1]
            [-2  1  1 -1 -1  1  0]
            [-2  2 -1 -1  1  0  0]
            [ 3 -1 -1  1  0  0  0]
            [ 3 -2  1  0  0  0  0]
            [-4  1  0  0  0  0  0]
            [ 1  0  0  0  0  0  0]
        """
    def product(self, left, right):
        """
        Return product of ``left`` and ``right``.

        Multiplication is done by performing the multiplication in the dual
        basis of ``self`` and then converting back to ``self``.

        INPUT:

        - ``left``, ``right`` -- elements of ``self``

        OUTPUT: the product of ``left`` and ``right`` in the basis ``self``

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).monomial()
            sage: zee = sage.combinat.sf.sfa.zee
            sage: h = m.dual_basis(scalar=zee)
            sage: a = h([2])
            sage: b = a*a; b # indirect doctest
            d_m[2, 2]
            sage: b.dual()
            6*m[1, 1, 1, 1] + 4*m[2, 1, 1] + 3*m[2, 2] + 2*m[3, 1] + m[4]
        """
    class Element(classical.SymmetricFunctionAlgebra_classical.Element):
        """
        An element in the dual basis.

        INPUT:

        At least one of the following must be specified. The one (if
        any) which is not provided will be computed.

        - ``dictionary`` -- an internal dictionary for the
          monomials and coefficients of ``self``

        - ``dual`` -- self as an element of the dual basis
        """
        def __init__(self, A, dictionary=None, dual=None) -> None:
            """
            Create an element of a dual basis.

            TESTS::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(scalar=zee, prefix='h')
                sage: a = h([2])
                sage: ec = h._element_class
                sage: ec(h, dual=m([2]))
                -h[1, 1] + 2*h[2]
                sage: h(m([2]))
                -h[1, 1] + 2*h[2]
                sage: h([2])
                h[2]
                sage: h([2])._dual
                m[1, 1] + m[2]
                sage: m(h([2]))
                m[1, 1] + m[2]
            """
        def dual(self):
            """
            Return ``self`` in the dual basis.

            OUTPUT:

            - the element ``self`` expanded in the dual basis to ``self.parent()``

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(scalar=zee)
                sage: a = h([2,1])
                sage: a.parent()
                Dual basis to Symmetric Functions over Rational Field in the monomial basis
                sage: a.dual()
                3*m[1, 1, 1] + 2*m[2, 1] + m[3]
            """
        def omega(self):
            """
            Return the image of ``self`` under the omega automorphism.

            The *omega automorphism* is defined to be the unique algebra
            endomorphism `\\omega` of the ring of symmetric functions that
            satisfies `\\omega(e_k) = h_k` for all positive integers `k`
            (where `e_k` stands for the `k`-th elementary symmetric
            function, and `h_k` stands for the `k`-th complete homogeneous
            symmetric function). It furthermore is a Hopf algebra
            endomorphism and an involution, and it is also known as the
            *omega involution*. It sends the power-sum symmetric function
            `p_k` to `(-1)^{k-1} p_k` for every positive integer `k`.

            The images of some bases under the omega automorphism are given by

            .. MATH::

                \\omega(e_{\\lambda}) = h_{\\lambda}, \\qquad
                \\omega(h_{\\lambda}) = e_{\\lambda}, \\qquad
                \\omega(p_{\\lambda}) = (-1)^{|\\lambda| - \\ell(\\lambda)}
                p_{\\lambda}, \\qquad
                \\omega(s_{\\lambda}) = s_{\\lambda^{\\prime}},

            where `\\lambda` is any partition, where `\\ell(\\lambda)` denotes
            the length (:meth:`~sage.combinat.partition.Partition.length`)
            of the partition `\\lambda`, where `\\lambda^{\\prime}` denotes the
            conjugate partition
            (:meth:`~sage.combinat.partition.Partition.conjugate`) of
            `\\lambda`, and where the usual notations for bases are used
            (`e` = elementary, `h` = complete homogeneous, `p` = powersum,
            `s` = Schur).

            :meth:`omega_involution` is a synonym for the :meth:`omega`
            method.

            OUTPUT: the result of applying omega to ``self``

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(zee)
                sage: hh = SymmetricFunctions(QQ).homogeneous()
                sage: hh([2,1]).omega()
                h[1, 1, 1] - h[2, 1]
                sage: h([2,1]).omega()
                d_m[1, 1, 1] - d_m[2, 1]
            """
        omega_involution = omega
        def scalar(self, x):
            """
            Return the standard scalar product of ``self`` and ``x``.

            INPUT:

            - ``x`` -- element of the symmetric functions

            OUTPUT: the scalar product between ``x`` and ``self``

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(scalar=zee)
                sage: a = h([2,1])
                sage: a.scalar(a)
                2
            """
        def scalar_hl(self, x):
            """
            Return the Hall-Littlewood scalar product of ``self`` and ``x``.

            INPUT:

            - ``x`` -- element of the same dual basis as ``self``

            OUTPUT: the Hall-Littlewood scalar product between ``x`` and ``self``

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(scalar=zee)
                sage: a = h([2,1])
                sage: a.scalar_hl(a)
                (-t - 2)/(t^4 - 2*t^3 + 2*t - 1)
            """
        def __invert__(self):
            """
            Invert ``self`` (only possible if ``self`` is a scalar
            multiple of `1` and we are working over a field).

            OUTPUT: multiplicative inverse of ``self`` if possible

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(zee)
                sage: a = h(2); a
                2*d_m[]
                sage: ~a
                1/2*d_m[]
                sage: a = 3*h[1]
                sage: a.__invert__()
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= 3*m[1])
            """
        def expand(self, n, alphabet: str = 'x'):
            """
            Expand the symmetric function ``self`` as a symmetric polynomial
            in ``n`` variables.

            INPUT:

            - ``n`` -- nonnegative integer

            - ``alphabet`` -- (default: ``'x'``) a variable for the expansion

            OUTPUT:

            A monomial expansion of ``self`` in the `n` variables
            labelled by ``alphabet``.

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).monomial()
                sage: zee = sage.combinat.sf.sfa.zee
                sage: h = m.dual_basis(zee)
                sage: a = h([2,1])+h([3])
                sage: a.expand(2)
                2*x0^3 + 3*x0^2*x1 + 3*x0*x1^2 + 2*x1^3
                sage: a.dual().expand(2)
                2*x0^3 + 3*x0^2*x1 + 3*x0*x1^2 + 2*x1^3
                sage: a.expand(2,alphabet='y')
                2*y0^3 + 3*y0^2*y1 + 3*y0*y1^2 + 2*y1^3
                sage: a.expand(2,alphabet='x,y')
                2*x^3 + 3*x^2*y + 3*x*y^2 + 2*y^3
                sage: h([1]).expand(0)
                0
                sage: (3*h([])).expand(0)
                3
            """

class DualBasisFunctor(SymmetricFunctionsFunctor):
    """
    A constructor for algebras of symmetric functions constructed by
    duality.

    EXAMPLES::

        sage: w = SymmetricFunctions(ZZ).witt()
        sage: w.dual_basis().construction()
        (SymmetricFunctionsFunctor[dual Witt], Integer Ring)
    """
    def __init__(self, basis) -> None:
        """
        Initialize the functor.

        INPUT:

        - ``basis`` -- the basis of the symmetric function algebra

        TESTS::

            sage: w = SymmetricFunctions(ZZ).witt()
            sage: F = w.dual_basis().construction()[0]
            sage: TestSuite(F).run()
        """
