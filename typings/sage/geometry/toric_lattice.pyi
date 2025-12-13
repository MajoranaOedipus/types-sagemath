from _typeshed import Incomplete
from sage.geometry.toric_lattice_element import ToricLatticeElement as ToricLatticeElement
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.fg_pid.fgp_element import FGP_Element as FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class as FGP_Module_class
from sage.modules.free_module import FreeModule_ambient_pid as FreeModule_ambient_pid, FreeModule_generic_pid as FreeModule_generic_pid, FreeModule_submodule_pid as FreeModule_submodule_pid, FreeModule_submodule_with_basis_pid as FreeModule_submodule_with_basis_pid
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.all import parent as parent
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

def is_ToricLattice(x):
    """
    Check if ``x`` is a toric lattice.

    INPUT:

    - ``x`` -- anything

    OUTPUT: ``True`` if ``x`` is a toric lattice and ``False`` otherwise

    EXAMPLES::

        sage: from sage.geometry.toric_lattice import (
        ....:   is_ToricLattice)
        sage: is_ToricLattice(1)
        doctest:warning...
        DeprecationWarning: The function is_ToricLattice is deprecated;
        use 'isinstance(..., ToricLattice_generic)' instead.
        See https://github.com/sagemath/sage/issues/38126 for details.
        False
        sage: N = ToricLattice(3)
        sage: N
        3-d lattice N
        sage: is_ToricLattice(N)
        True
    """
def is_ToricLatticeQuotient(x):
    """
    Check if ``x`` is a toric lattice quotient.

    INPUT:

    - ``x`` -- anything

    OUTPUT: ``True`` if ``x`` is a toric lattice quotient and ``False`` otherwise

    EXAMPLES::

        sage: from sage.geometry.toric_lattice import (
        ....:   is_ToricLatticeQuotient)
        sage: is_ToricLatticeQuotient(1)
        doctest:warning...
        DeprecationWarning: The function is_ToricLatticeQuotient is deprecated;
        use 'isinstance(..., ToricLattice_quotient)' instead.
        See https://github.com/sagemath/sage/issues/38126 for details.
        False
        sage: N = ToricLattice(3)
        sage: N
        3-d lattice N
        sage: is_ToricLatticeQuotient(N)
        False
        sage: Q = N / N.submodule([(1,2,3), (3,2,1)])
        sage: Q
        Quotient with torsion of 3-d lattice N
        by Sublattice <N(1, 2, 3), N(0, 4, 8)>
        sage: is_ToricLatticeQuotient(Q)
        True
    """

class ToricLatticeFactory(UniqueFactory):
    '''
    Create a lattice for toric geometry objects.

    INPUT:

    - ``rank`` -- nonnegative integer; the only mandatory parameter

    - ``name`` -- string

    - ``dual_name`` -- string

    - ``latex_name`` -- string

    - ``latex_dual_name`` -- string

    OUTPUT: lattice

    A toric lattice is uniquely determined by its rank and associated names.
    There are four such "associated names" whose meaning should be clear from
    the names of the corresponding parameters, but the choice of default
    values is a little bit involved. So here is the full description of the
    "naming algorithm":

    #. If no names were given at all, then this lattice will be called "N" and
       the dual one "M". These are the standard choices in toric geometry.

    #. If ``name`` was given and ``dual_name`` was not, then ``dual_name``
       will be ``name`` followed by "*".

    #. If LaTeX names were not given, they will coincide with the "usual"
       names, but if ``dual_name`` was constructed automatically, the trailing
       star will be typeset as a superscript.

    EXAMPLES:

    Let\'s start with no names at all and see how automatic names are given::

        sage: L1 = ToricLattice(3)
        sage: L1
        3-d lattice N
        sage: L1.dual()
        3-d lattice M

    If we give the name "N" explicitly, the dual lattice will be called "N*"::

        sage: L2 = ToricLattice(3, "N")
        sage: L2
        3-d lattice N
        sage: L2.dual()
        3-d lattice N*

    However, we can give an explicit name for it too::

        sage: L3 = ToricLattice(3, "N", "M")
        sage: L3
        3-d lattice N
        sage: L3.dual()
        3-d lattice M

    If you want, you may also give explicit LaTeX names::

        sage: L4 = ToricLattice(3, "N", "M", r"\\mathbb{N}", r"\\mathbb{M}")
        sage: latex(L4)
        \\mathbb{N}
        sage: latex(L4.dual())
        \\mathbb{M}

    While all four lattices above are called "N", only two of them are equal
    (and are actually the same)::

        sage: L1 == L2
        False
        sage: L1 == L3
        True
        sage: L1 is L3
        True
        sage: L1 == L4
        False

    The reason for this is that ``L2`` and ``L4`` have different names either
    for dual lattices or for LaTeX typesetting.
    '''
    def create_key(self, rank, name=None, dual_name=None, latex_name=None, latex_dual_name=None):
        """
        Create a key that uniquely identifies this toric lattice.

        See :class:`ToricLattice <ToricLatticeFactory>` for documentation.

        .. WARNING::

            You probably should not use this function directly.

        TESTS::

            sage: ToricLattice.create_key(3)
            (3, 'N', 'M', 'N', 'M')
            sage: N = ToricLattice(3)
            sage: loads(dumps(N)) is N
            True
            sage: TestSuite(N).run()
        """
    def create_object(self, version, key):
        """
        Create the toric lattice described by ``key``.

        See :class:`ToricLattice <ToricLatticeFactory>` for documentation.

        .. WARNING::

            You probably should not use this function directly.

        TESTS::

            sage: key = ToricLattice.create_key(3)
            sage: ToricLattice.create_object(1, key)
            3-d lattice N
        """

ToricLattice: Incomplete

class ToricLattice_generic(FreeModule_generic_pid):
    """
    Abstract base class for toric lattices.
    """
    Element = ToricLatticeElement
    def __call__(self, *args, **kwds):
        """
        Construct a new element of ``self``.

        INPUT:

        - anything that can be interpreted as coordinates, except for elements
          of other lattices.

        OUTPUT: :class:`~sage.geometry.toric_lattice_element.ToricLatticeElement`

        TESTS::

            sage: N = ToricLattice(3)
            sage: N.__call__([1,2,3])
            N(1, 2, 3)
            sage: N([1,2,3])    # indirect test
            N(1, 2, 3)

        The point of overriding this function was to allow writing the above
        command as::

            sage: N(1,2,3)
            N(1, 2, 3)

        We also test that the special treatment of zero still works::

            sage: N(0)
            N(0, 0, 0)

        Quotients of toric lattices can be converted to a new toric
        lattice of the appropriate dimension::

            sage: N3 = ToricLattice(3, 'N3')
            sage: Q = N3 / N3.span([ N3(1,2,3) ])
            sage: Q.an_element()
            N3[1, 0, 0]
            sage: N2 = ToricLattice(2, 'N2')
            sage: N2( Q.an_element() )
            N2(1, 0)
        """
    def __contains__(self, point) -> bool:
        '''
        Check if ``point`` is an element of ``self``.

        INPUT:

        - ``point`` -- anything

        OUTPUT: ``True`` if ``point`` is an element of ``self``, ``False``
        otherwise

        TESTS::

            sage: N = ToricLattice(3)
            sage: M = N.dual()
            sage: L = ToricLattice(3, "L")
            sage: 1 in N
            False
            sage: (1,0) in N
            False
            sage: (1,0,0) in N
            True
            sage: N(1,0,0) in N
            True
            sage: M(1,0,0) in N
            False
            sage: L(1,0,0) in N
            False
            sage: (1/2,0,0) in N
            False
            sage: (2/2,0,0) in N
            True
        '''
    def construction(self) -> None:
        """
        Return the functorial construction of ``self``.

        OUTPUT:

        ``None``, we do not think of toric lattices as constructed from
        simpler objects since we do not want to perform arithmetic involving
        different lattices.

        TESTS::

            sage: print(ToricLattice(3).construction())
            None
        """
    def direct_sum(self, other):
        """
        Return the direct sum with ``other``.

        INPUT:

        - ``other`` -- a toric lattice or more general module

        OUTPUT:

        The direct sum of ``self`` and ``other`` as `\\ZZ`-modules. If
        ``other`` is a :class:`ToricLattice <ToricLatticeFactory>`,
        another toric lattice will be returned.

        EXAMPLES::

            sage: K = ToricLattice(3, 'K')
            sage: L = ToricLattice(3, 'L')
            sage: N = K.direct_sum(L); N
            6-d lattice K+L
            sage: N, N.dual(), latex(N), latex(N.dual())
            (6-d lattice K+L, 6-d lattice K*+L*, K \\oplus L, K^* \\oplus L^*)

        With default names::

            sage: N = ToricLattice(3).direct_sum(ToricLattice(2))
            sage: N, N.dual(), latex(N), latex(N.dual())
            (5-d lattice N+N, 5-d lattice M+M, N \\oplus N, M \\oplus M)

        If ``other`` is not a :class:`ToricLattice
        <ToricLatticeFactory>`, fall back to sum of modules::

            sage: ToricLattice(3).direct_sum(ZZ^2)
            Free module of degree 5 and rank 5 over Integer Ring
            Echelon basis matrix:
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a toric (sub)lattice.dual

        OUTPUT:

        - a toric (sub)lattice.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns1 = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Ns2 = N.submodule([N(1,4,9), N(9,2,0)])
            sage: Ns1.intersection(Ns2)
            Sublattice <N(54, 12, 0)>

        Note that if one of the intersecting sublattices is a sublattice of
        another, no new lattices will be constructed::

            sage: N.intersection(N) is N
            True
            sage: Ns1.intersection(N) is Ns1
            True
            sage: N.intersection(Ns1) is Ns1
            True
        """
    def quotient(self, sub, check: bool = True, positive_point=None, positive_dual_point=None, **kwds):
        """
        Return the quotient of ``self`` by the given sublattice ``sub``.

        INPUT:

        - ``sub`` -- sublattice of self

        - ``check`` -- boolean (default: ``True``); whether or not to check that ``sub`` is
          a valid sublattice

        If the quotient is one-dimensional and torsion free, the
        following two mutually exclusive keyword arguments are also
        allowed. They decide the sign choice for the (single)
        generator of the quotient lattice:

        - ``positive_point`` -- a lattice point of ``self`` not in the
          sublattice ``sub`` (that is, not zero in the quotient
          lattice). The quotient generator will be in the same
          direction as ``positive_point``.

        - ``positive_dual_point`` -- a dual lattice point. The
          quotient generator will be chosen such that its lift has a
          positive product with ``positive_dual_point``. Note: if
          ``positive_dual_point`` is not zero on the sublattice
          ``sub``, then the notion of positivity will depend on the
          choice of lift!

        Further named arguments are passed to the constructor of a toric lattice
        quotient.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Q = N/Ns
            sage: Q
            Quotient with torsion of 3-d lattice N
            by Sublattice <N(1, 8, 0), N(0, 12, 0)>

        Attempting to quotient one lattice by a sublattice of another
        will result in a :exc:`ValueError`::

            sage: N = ToricLattice(3)
            sage: M = ToricLattice(3, name='M')
            sage: Ms = M.submodule([M(2,4,0), M(9,12,0)])
            sage: N.quotient(Ms)
            Traceback (most recent call last):
            ...
            ValueError: M(1, 8, 0) cannot generate a sublattice of
            3-d lattice N

        However, if we forget the sublattice structure, then it is
        possible to quotient by vector spaces or modules constructed
        from any sublattice::

            sage: N = ToricLattice(3)
            sage: M = ToricLattice(3, name='M')
            sage: Ms = M.submodule([M(2,4,0), M(9,12,0)])
            sage: N.quotient(Ms.vector_space())
            Quotient with torsion of 3-d lattice N by Sublattice
            <N(1, 8, 0), N(0, 12, 0)>
            sage: N.quotient(Ms.sparse_module())
            Quotient with torsion of 3-d lattice N by Sublattice
            <N(1, 8, 0), N(0, 12, 0)>

        See :class:`ToricLattice_quotient` for more examples.

        TESTS:

        We check that :issue:`19603` is fixed::

            sage: K = Cone([(1,0,0),(0,1,0)])
            sage: K.lattice()
            3-d lattice N
            sage: K.orthogonal_sublattice()
            Sublattice <M(0, 0, 1)>
            sage: K.lattice().quotient(K.orthogonal_sublattice())
            Traceback (most recent call last):
            ...
            ValueError: M(0, 0, 1) cannot generate a sublattice of
            3-d lattice N

        We can quotient by the trivial sublattice::

            sage: N = ToricLattice(3)
            sage: N.quotient(N.zero_submodule())
            3-d lattice, quotient of 3-d lattice N by Sublattice <>

        We can quotient a lattice by itself::

            sage: N = ToricLattice(3)
            sage: N.quotient(N)
            0-d lattice, quotient of 3-d lattice N by Sublattice
            <N(1, 0, 0), N(0, 1, 0), N(0, 0, 1)>
        """
    def saturation(self):
        """
        Return the saturation of ``self``.

        OUTPUT: a :class:`toric lattice <ToricLatticeFactory>`

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([(1,2,3), (4,5,6)])
            sage: Ns
            Sublattice <N(1, 2, 3), N(0, 3, 6)>
            sage: Ns_sat = Ns.saturation()
            sage: Ns_sat
            Sublattice <N(1, 0, -1), N(0, 1, 2)>
            sage: Ns_sat is Ns_sat.saturation()
            True
        """
    def span(self, gens, base_ring=..., *args, **kwds):
        """
        Return the span of the given generators.

        INPUT:

        - ``gens`` -- list of elements of the ambient vector space of
          ``self``

        - ``base_ring`` -- (default: `\\ZZ`) base ring for the generated module

        OUTPUT: submodule spanned by ``gens``

        .. NOTE::

            The output need not be a submodule of ``self``, nor even of the
            ambient space. It must, however, be contained in the ambient
            vector space.

        See also :meth:`span_of_basis`,
        :meth:`~sage.modules.free_module.FreeModule_generic_pid.submodule`,
        and
        :meth:`~sage.modules.free_module.FreeModule_generic_pid.submodule_with_basis`,

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N.gen(0)])
            sage: Ns.span([N.gen(1)])
            Sublattice <N(0, 1, 0)>
            sage: Ns.submodule([N.gen(1)])
            Traceback (most recent call last):
            ...
            ArithmeticError: argument gens (= [N(0, 1, 0)]) does not generate a submodule of self
        """
    def span_of_basis(self, basis, base_ring=..., *args, **kwds):
        """
        Return the submodule with the given ``basis``.

        INPUT:

        - ``basis`` -- list of elements of the ambient vector space of
          ``self``

        - ``base_ring`` -- (default: `\\ZZ`) base ring for the generated module

        OUTPUT: submodule spanned by ``basis``

        .. NOTE::

            The output need not be a submodule of ``self``, nor even of the
            ambient space. It must, however, be contained in the ambient
            vector space.

        See also :meth:`span`,
        :meth:`~sage.modules.free_module.FreeModule_generic_pid.submodule`,
        and
        :meth:`~sage.modules.free_module.FreeModule_generic_pid.submodule_with_basis`,

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.span_of_basis([(1,2,3)])
            sage: Ns.span_of_basis([(2,4,0)])
            Sublattice <N(2, 4, 0)>
            sage: Ns.span_of_basis([(1/5,2/5,0), (1/7,1/7,0)])
            Free module of degree 3 and rank 2 over Integer Ring
            User basis matrix:
            [1/5 2/5   0]
            [1/7 1/7   0]

        Of course the input basis vectors must be linearly independent::

            sage: Ns.span_of_basis([(1,2,0), (2,4,0)])
            Traceback (most recent call last):
            ...
            ValueError: The given basis vectors must be linearly independent.
        """

class ToricLattice_ambient(ToricLattice_generic, FreeModule_ambient_pid):
    '''
    Create a toric lattice.

    See :class:`ToricLattice <ToricLatticeFactory>` for documentation.

    .. WARNING::

        There should be only one toric lattice with the given rank and
        associated names. Using this class directly to create toric lattices
        may lead to unexpected results. Please, use :class:`ToricLattice
        <ToricLatticeFactory>` to create toric lattices.

    TESTS::

        sage: N = ToricLattice(3, "N", "M", "N", "M")
        sage: N
        3-d lattice N
        sage: TestSuite(N).run()
    '''
    Element = ToricLatticeElement
    def __init__(self, rank, name, dual_name, latex_name, latex_dual_name) -> None:
        '''
        See :class:`ToricLattice <ToricLatticeFactory>` for documentation.

        TESTS::

            sage: ToricLattice(3, "N", "M", "N", "M")
            3-d lattice N
        '''
    def __richcmp__(self, right, op):
        """
        Compare ``self`` and ``right``.

        INPUT:

        - ``right`` -- anything

        OUTPUT: boolean

        There is equality if ``right`` is a toric lattice of the same
        dimension as ``self`` and their associated names are the
        same.

        TESTS::

            sage: N3 = ToricLattice(3)
            sage: N4 = ToricLattice(4)
            sage: M3 = N3.dual()
            sage: N3 < N4
            True
            sage: N3 > M3
            True
            sage: N3 == ToricLattice(3)
            True
        """
    def ambient_module(self):
        """
        Return the ambient module of ``self``.

        OUTPUT: :class:`toric lattice <ToricLatticeFactory>`

        .. NOTE::

            For any ambient toric lattice its ambient module is the lattice
            itself.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: N.ambient_module()
            3-d lattice N
            sage: N.ambient_module() is N
            True
        """
    def dual(self):
        """
        Return the lattice dual to ``self``.

        OUTPUT: :class:`toric lattice <ToricLatticeFactory>`

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: N
            3-d lattice N
            sage: M = N.dual()
            sage: M
            3-d lattice M
            sage: M.dual() is N
            True

        Elements of dual lattices can act on each other::

            sage: n = N(1,2,3)
            sage: m = M(4,5,6)
            sage: n * m
            32
            sage: m * n
            32
        """
    def plot(self, **options):
        """
        Plot ``self``.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: N.plot()                                                              # needs sage.plot
            Graphics3d Object
        """

class ToricLattice_sublattice_with_basis(ToricLattice_generic, FreeModule_submodule_with_basis_pid):
    '''
    Construct the sublattice of ``ambient`` toric lattice with given ``basis``.

    INPUT (same as for
    :class:`~sage.modules.free_module.FreeModule_submodule_with_basis_pid`):

    - ``ambient`` -- ambient :class:`toric lattice <ToricLatticeFactory>` for
      this sublattice

    - ``basis`` -- list of linearly independent elements of ``ambient``, these
      elements will be used as the default basis of the constructed
      sublattice

    - see the base class for other available options

    OUTPUT: sublattice of a toric lattice with a user-specified basis

    See also :class:`ToricLattice_sublattice` if you do not want to specify an
    explicit basis.

    EXAMPLES:

    The intended way to get objects of this class is to use
    :meth:`submodule_with_basis` method of toric lattices::

        sage: N = ToricLattice(3)
        sage: sublattice = N.submodule_with_basis([(1,1,0), (3,2,1)])
        sage: sublattice.has_user_basis()
        True
        sage: sublattice.basis()
        [N(1, 1, 0), N(3, 2, 1)]

    Even if you have provided your own basis, you still can access the
    "standard" one::

        sage: sublattice.echelonized_basis()
        [N(1, 0, 1), N(0, 1, -1)]
    '''
    def dual(self):
        """
        Return the lattice dual to ``self``.

        OUTPUT: a :class:`toric lattice quotient <ToricLattice_quotient>`

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([(1,1,0), (3,2,1)])
            sage: Ns.dual()
            2-d lattice, quotient of 3-d lattice M by Sublattice <M(1, -1, -1)>
        """
    def plot(self, **options):
        """
        Plot ``self``.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: sublattice = N.submodule_with_basis([(1,1,0), (3,2,1)])
            sage: sublattice.plot()                                                     # needs sage.plot
            Graphics3d Object

        Now we plot both the ambient lattice and its sublattice::

            sage: N.plot() + sublattice.plot(point_color='red')                         # needs sage.plot
            Graphics3d Object
        """

class ToricLattice_sublattice(ToricLattice_sublattice_with_basis, FreeModule_submodule_pid):
    '''
    Construct the sublattice of ``ambient`` toric lattice generated by ``gens``.

    INPUT (same as for
    :class:`~sage.modules.free_module.FreeModule_submodule_pid`):

    - ``ambient`` -- ambient :class:`toric lattice <ToricLatticeFactory>` for
      this sublattice

    - ``gens`` -- list of elements of ``ambient`` generating the constructed
      sublattice

    - see the base class for other available options

    OUTPUT: sublattice of a toric lattice with an automatically chosen basis

    See also :class:`ToricLattice_sublattice_with_basis` if you want to
    specify an explicit basis.

    EXAMPLES:

    The intended way to get objects of this class is to use
    :meth:`submodule` method of toric lattices::

        sage: N = ToricLattice(3)
        sage: sublattice = N.submodule([(1,1,0), (3,2,1)])
        sage: sublattice.has_user_basis()
        False
        sage: sublattice.basis()
        [N(1, 0, 1), N(0, 1, -1)]

    For sublattices without user-specified basis, the basis obtained above is
    the same as the "standard" one::

        sage: sublattice.echelonized_basis()
        [N(1, 0, 1), N(0, 1, -1)]
    '''

class ToricLattice_quotient_element(FGP_Element):
    """
    Create an element of a toric lattice quotient.

    .. WARNING::

        You probably should not construct such elements explicitly.

    INPUT:

    - same as for :class:`~sage.modules.fg_pid.fgp_element.FGP_Element`.

    OUTPUT: element of a toric lattice quotient

    TESTS::

        sage: N = ToricLattice(3)
        sage: sublattice = N.submodule([(1,1,0), (3,2,1)])
        sage: Q = N/sublattice
        sage: e = Q(1,2,3)
        sage: e
        N[1, 2, 3]
        sage: e2 = Q(N(2,3,3))
        sage: e2
        N[2, 3, 3]
        sage: e == e2
        True
        sage: e.vector()
        (-4)
        sage: e2.vector()
        (-4)
    """
    def set_immutable(self) -> None:
        """
        Make ``self`` immutable.

        OUTPUT: none

        .. NOTE:: Elements of toric lattice quotients are always immutable, so
            this method does nothing, it is introduced for compatibility
            purposes only.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Q = N/Ns
            sage: Q.0.set_immutable()
        """

class ToricLattice_quotient(FGP_Module_class):
    """
    Construct the quotient of a toric lattice ``V`` by its sublattice ``W``.

    INPUT:

    - ``V`` -- ambient toric lattice

    - ``W`` -- sublattice of ``V``

    - ``check`` -- boolean (default: ``True``); whether to check correctness of input
      or not

    If the quotient is one-dimensional and torsion free, the following
    two mutually exclusive keyword arguments are also allowed. They
    decide the sign choice for the (single) generator of the quotient
    lattice:

    - ``positive_point`` -- a lattice point of ``self`` not in the
      sublattice ``sub`` (that is, not zero in the quotient
      lattice). The quotient generator will be in the same direction
      as ``positive_point``.

    - ``positive_dual_point`` -- a dual lattice point. The quotient
      generator will be chosen such that its lift has a positive
      product with ``positive_dual_point``. Note: if
      ``positive_dual_point`` is not zero on the sublattice ``sub``,
      then the notion of positivity will depend on the choice of lift!

    Further given named arguments are passed to the constructor of an FGP
    module.

    OUTPUT: quotient of ``V`` by ``W``

    EXAMPLES:

    The intended way to get objects of this class is to use
    :meth:`quotient` method of toric lattices::

        sage: N = ToricLattice(3)
        sage: sublattice = N.submodule([(1,1,0), (3,2,1)])
        sage: Q = N/sublattice
        sage: Q
        1-d lattice, quotient of 3-d lattice N by Sublattice <N(1, 0, 1), N(0, 1, -1)>
        sage: Q.gens()
        (N[1, 0, 0],)

    Here, ``sublattice`` happens to be of codimension one in ``N``. If
    you want to prescribe the sign of the quotient generator, you can
    do either::

        sage: Q = N.quotient(sublattice, positive_point=N(0,0,-1)); Q
        1-d lattice, quotient of 3-d lattice N by Sublattice <N(1, 0, 1), N(0, 1, -1)>
        sage: Q.gens()
        (N[1, 0, 0],)

    or::

        sage: M = N.dual()
        sage: Q = N.quotient(sublattice, positive_dual_point=M(1,0,0)); Q
        1-d lattice, quotient of 3-d lattice N by Sublattice <N(1, 0, 1), N(0, 1, -1)>
        sage: Q.gens()
        (N[1, 0, 0],)

    TESTS::

        sage: loads(dumps(Q)) == Q
        True
        sage: loads(dumps(Q)).gens() == Q.gens()
        True
    """
    def __init__(self, V, W, check: bool = True, positive_point=None, positive_dual_point=None, **kwds) -> None:
        """
        The constructor.

        See :class:`ToricLattice_quotient` for an explanation of the arguments.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: from sage.geometry.toric_lattice import ToricLattice_quotient
            sage: ToricLattice_quotient(N, N.span([N(1,2,3)]))
            2-d lattice, quotient of 3-d lattice N by Sublattice <N(1, 2, 3)>

        An :exc:`ArithmeticError` will be raised if ``W`` is not a
        sublattice of ``V``::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N.gen(0)])
            sage: Ns
            Sublattice <N(1, 0, 0)>
            sage: Ns.span([N.gen(1)])
            Sublattice <N(0, 1, 0)>
            sage: Ns.quotient(Ns.span([N.gen(1)]))
            Traceback (most recent call last):
            ...
            ArithmeticError: W must be a sublattice of V
        """
    def gens(self) -> tuple:
        """
        Return the generators of the quotient.

        OUTPUT:

        A tuple of :class:`ToricLattice_quotient_element` generating
        the quotient.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Q = N.quotient(N.span([N(1,2,3), N(0,2,1)]), positive_point=N(0,-1,0))
            sage: Q.gens()
            (N[0, -1, 0],)
        """
    Element = ToricLattice_quotient_element
    def base_extend(self, R):
        """
        Return the base change of ``self`` to the ring ``R``.

        INPUT:

        - ``R`` -- either `\\ZZ` or `\\QQ`

        OUTPUT: ``self`` if `R=\\ZZ`, quotient of the base extension of the ambient
        lattice by the base extension of the sublattice if `R=\\QQ`

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Q = N/Ns
            sage: Q.base_extend(ZZ) is Q
            True
            sage: Q.base_extend(QQ)
            Vector space quotient V/W of dimension 1 over Rational Field where
            V: Vector space of dimension 3 over Rational Field
            W: Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [1 0 0]
            [0 1 0]
        """
    def is_torsion_free(self):
        """
        Check if ``self`` is torsion-free.

        OUTPUT: ``True`` if ``self`` has no torsion and ``False`` otherwise

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Q = N/Ns
            sage: Q.is_torsion_free()
            False
            sage: Ns = N.submodule([N(1,4,0)])
            sage: Q = N/Ns
            sage: Q.is_torsion_free()
            True
        """
    def dual(self):
        """
        Return the lattice dual to ``self``.

        OUTPUT: a :class:`toric lattice quotient <ToricLattice_quotient>`

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([(1, -1, -1)])
            sage: Q = N / Ns
            sage: Q.dual()
            Sublattice <M(1, 0, 1), M(0, 1, -1)>
        """
    def rank(self):
        """
        Return the rank of ``self``.

        OUTPUT: integer; the dimension of the free part of the quotient

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Ns = N.submodule([N(2,4,0), N(9,12,0)])
            sage: Q = N/Ns
            sage: Q.ngens()
            2
            sage: Q.rank()
            1
            sage: Ns = N.submodule([N(1,4,0)])
            sage: Q = N/Ns
            sage: Q.ngens()
            2
            sage: Q.rank()
            2
        """
    dimension = rank
    def coordinate_vector(self, x, reduce: bool = False):
        """
        Return coordinates of ``x`` with respect to the optimized
        representation of ``self``.

        INPUT:

        - ``x`` -- element of ``self`` or convertible to ``self``

        - ``reduce`` -- (default: ``False``) if ``True``, reduce coefficients
          modulo invariants

        OUTPUT: the coordinates as a vector

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: Q = N.quotient(N.span([N(1,2,3), N(0,2,1)]), positive_point=N(0,-1,0))
            sage: q = Q.gen(0); q
            N[0, -1, 0]
            sage: q.vector()  # indirect test
            (1)
            sage: Q.coordinate_vector(q)
            (1)
        """
