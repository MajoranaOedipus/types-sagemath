from . import PythonModule as PythonModule, StaticFile as StaticFile
from .join_feature import JoinFeature as JoinFeature

class SAGE_SRC(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of the
    monolithic source tree of the Sage library.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import SAGE_SRC
            sage: isinstance(SAGE_SRC(), SAGE_SRC)
            True
        """

class sagemath_doc_html(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of the documentation
    of the Sage library in HTML format.

    Developers often use ``make build`` instead of ``make`` to avoid the
    long time it takes to compile the documentation. Although commands
    such as ``make ptest`` build the documentation before testing, other
    test commands such as ``make ptestlong-nodoc`` or ``./sage -t --all``
    do not.

    All doctests that refer to the built documentation need to be marked
    ``# needs sagemath_doc_html``.

    TESTS::

        sage: from sage.features.sagemath import sagemath_doc_html
        sage: sagemath_doc_html().is_present()                                          # needs sagemath_doc_html
        FeatureTestResult('sagemath_doc_html', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sagemath_doc_html
            sage: isinstance(sagemath_doc_html(), sagemath_doc_html)
            True
        """

class sage__combinat(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.combinat`.

    EXAMPLES:

    Python modules that provide elementary combinatorial objects such as :mod:`sage.combinat.subset`,
    :mod:`sage.combinat.composition`, :mod:`sage.combinat.permutation` are always available;
    there is no need for an ``# optional/needs`` tag::

        sage: Permutation([1,2,3]).is_even()
        True
        sage: Permutation([6,1,4,5,2,3]).bruhat_inversions()
        [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 4], [3, 5]]

    Use ``# needs sage.combinat`` for doctests that use any other Python modules
    from :mod:`sage.combinat`, for example :mod:`sage.combinat.tableau_tuple`::

        sage: TableauTuple([[[7,8,9]],[],[[1,2,3],[4,5],[6]]]).shape()                  # needs sage.combinat
        ([3], [], [3, 2, 1])

    Doctests that use Python modules from :mod:`sage.combinat` that involve trees,
    graphs, hypergraphs, posets, quivers, combinatorial designs,
    finite state machines etc. should be marked ``# needs sage.combinat sage.graphs``::

        sage: L = Poset({0: [1], 1: [2], 2:[3], 3:[4]})                                 # needs sage.combinat sage.graphs
        sage: L.is_chain()                                                              # needs sage.combinat sage.graphs
        True

    Doctests that use combinatorial modules/algebras, or root systems should use the tag
    ``# needs sage.combinat sage.modules``::

        sage: # needs sage.combinat sage.modules
        sage: A = SchurAlgebra(QQ, 2, 3)
        sage: a = A.an_element(); a
        2*S((1, 1, 1), (1, 1, 1)) + 2*S((1, 1, 1), (1, 1, 2))
         + 3*S((1, 1, 1), (1, 2, 2))
        sage: L = RootSystem(['A',3,1]).root_lattice()
        sage: PIR = L.positive_imaginary_roots(); PIR
        Positive imaginary roots of type ['A', 3, 1]

    Doctests that use lattices, semilattices, or Dynkin diagrams should use the tag
    ``# needs sage.combinat sage.graphs sage.modules``::

        sage: L = LatticePoset({0: [1,2], 1: [3], 2: [3,4], 3: [5], 4: [5]})            # needs sage.combinat sage.graphs sage.modules
        sage: L.meet_irreducibles()                                                     # needs sage.combinat sage.graphs sage.modules
        [1, 3, 4]

    TESTS::

        sage: from sage.features.sagemath import sage__combinat
        sage: sage__combinat().is_present()                                             # needs sage.combinat
        FeatureTestResult('sage.combinat', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__combinat
            sage: isinstance(sage__combinat(), sage__combinat)
            True
        """

class sage__geometry__polyhedron(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.geometry.polyhedron`.

    EXAMPLES:

    Doctests that use polyhedra, cones, geometric complexes, triangulations, etc. should use
    the tag ``# needs sage.geometry.polyhedron``::

        sage: co = polytopes.truncated_tetrahedron()                                    # needs sage.geometry.polyhedron
        sage: co.volume()                                                               # needs sage.geometry.polyhedron
        184/3

    Some constructions of polyhedra require additional tags::

        sage: # needs sage.combinat sage.geometry.polyhedron sage.rings.number_field
        sage: perm_a3_reg_nf = polytopes.generalized_permutahedron(
        ....:    ['A',3], regular=True, backend='number_field'); perm_a3_reg_nf
        A 3-dimensional polyhedron in AA^3 defined as the convex hull of 24 vertices

    TESTS::

        sage: from sage.features.sagemath import sage__geometry__polyhedron
        sage: sage__geometry__polyhedron().is_present()                                 # needs sage.geometry.polyhedron
        FeatureTestResult('sage.geometry.polyhedron', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__geometry__polyhedron
            sage: isinstance(sage__geometry__polyhedron(), sage__geometry__polyhedron)
            True
        """

class sage__graphs(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.graphs`.

    EXAMPLES:

    Doctests that use anything from :mod:`sage.graphs` (:class:`Graph`, :class:`DiGraph`, ...)
    should be marked ``# needs sage.graphs``. The same applies to any doctest that
    uses a :class:`~sage.combinat.posets.posets.Poset`, cluster algebra quiver, finite
    state machines, abelian sandpiles, or Dynkin diagrams::

        sage: g = graphs.PetersenGraph()                                                # needs sage.graphs
        sage: r, s = g.is_weakly_chordal(certificate=True); r                           # needs sage.graphs
        False

    Also any use of tree classes defined in :mod:`sage.combinat` (:class:`BinaryTree`,
    :class:`RootedTree`, ...) in doctests should be marked the same.

    By way of generalization, any use of :class:`SimplicialComplex` or other abstract complexes from
    :mod:`sage.topology`, hypergraphs, and combinatorial designs, should be marked
    ``# needs sage.graphs`` as well::

        sage: X = SimplicialComplex([[0,1,2], [1,2,3]])                                 # needs sage.graphs
        sage: X.link(Simplex([0]))                                                      # needs sage.graphs
        Simplicial complex with vertex set (1, 2) and facets {(1, 2)}

        sage: IncidenceStructure([[1,2,3],[1,4]]).degrees(2)                            # needs sage.graphs
        {(1, 2): 1, (1, 3): 1, (1, 4): 1, (2, 3): 1, (2, 4): 0, (3, 4): 0}

    On the other hand, matroids are not implemented as posets in Sage but are instead
    closely tied to linear algebra over fields; hence use ``# needs sage.modules`` instead::

        sage: # needs sage.modules
        sage: M = Matroid(Matrix(QQ, [[1, 0, 0, 0, 1, 1, 1],
        ....:                         [0, 1, 0, 1, 0, 1, 1],
        ....:                         [0, 0, 1, 1, 1, 0, 1]]))
        sage: N = (M / [2]).delete([3, 4])
        sage: sorted(N.groundset())
        [0, 1, 5, 6]

    However, many constructions (and some methods) of matroids do involve graphs::

        sage: # needs sage.modules
        sage: W = matroids.Wheel(3)     # despite the name, not created via graphs
        sage: W.is_isomorphic(N)           # goes through a graph isomorphism test      # needs sage.graphs
        False
        sage: K4 = matroids.CompleteGraphic(4)    # this one is created via graphs      # needs sage.graphs
        sage: K4.is_isomorphic(W)                                                       # needs sage.graphs
        True

    TESTS::

        sage: from sage.features.sagemath import sage__graphs
        sage: sage__graphs().is_present()                                               # needs sage.graphs
        FeatureTestResult('sage.graphs', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__graphs
            sage: isinstance(sage__graphs(), sage__graphs)
            True
        """

class sage__groups(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of ``sage.groups``.

    EXAMPLES:

    Permutations and sets of permutations are always available, but permutation groups are
    implemented in Sage using the :ref:`GAP <spkg_gap>` system and require the tag
    ``# needs sage.groups``::

        sage: p = Permutation([2,1,4,3])
        sage: p.to_permutation_group_element()                                          # needs sage.groups
        (1,2)(3,4)

    TESTS::

        sage: from sage.features.sagemath import sage__groups
        sage: sage__groups().is_present()                                               # needs sage.groups
        FeatureTestResult('sage.groups', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__groups
            sage: isinstance(sage__groups(), sage__groups)
            True
        """

class sage__libs__braiding(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.libs.braiding`.

    EXAMPLES::

        sage: from sage.features.sagemath import sage__libs__braiding
        sage: sage__libs__braiding().is_present()                                            # needs sage.libs.braiding
        FeatureTestResult('sage.libs.braiding', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__braiding
            sage: isinstance(sage__libs__braiding(), sage__libs__braiding)
            True
        """

class sage__libs__ecl(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.libs.ecl`.

    EXAMPLES::

        sage: from sage.features.sagemath import sage__libs__ecl
        sage: sage__libs__ecl().is_present()                        # optional - sage.libs.ecl
        FeatureTestResult('sage.libs.ecl', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__ecl
            sage: isinstance(sage__libs__ecl(), sage__libs__ecl)
            True
        """

class sage__libs__flint(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.flint`
    and other modules depending on FLINT.

    In addition to the modularization purposes that this tag serves, it also provides attribution
    to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__flint
        sage: sage__libs__flint().is_present()                                          # needs sage.libs.flint
        FeatureTestResult('sage.libs.flint', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__flint
            sage: isinstance(sage__libs__flint(), sage__libs__flint)
            True
        """

class sage__libs__gap(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.gap`
    (the library interface to :ref:`GAP <spkg_gap>`) and :mod:`sage.interfaces.gap` (the pexpect
    interface to GAP). By design, we do not distinguish between these two, in order
    to facilitate the conversion of code from the pexpect interface to the library
    interface.

    .. SEEALSO::

        :class:`Features for GAP packages <~sage.features.gap.GapPackage>`

    TESTS::

        sage: from sage.features.gap import sage__libs__gap
        sage: sage__libs__gap().is_present()                                            # needs sage.libs.gap
        FeatureTestResult('sage.libs.gap', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.gap import sage__libs__gap
            sage: isinstance(sage__libs__gap(), sage__libs__gap)
            True
        """

class sage__libs__linbox(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.linbox`
    and other modules depending on Givaro, FFLAS-FFPACK, LinBox.

    In addition to the modularization purposes that this tag serves, it also provides attribution
    to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__linbox
        sage: sage__libs__linbox().is_present()                                         # needs sage.libs.linbox
        FeatureTestResult('sage.libs.linbox', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__linbox
            sage: isinstance(sage__libs__linbox(), sage__libs__linbox)
            True
        """

class sage__libs__m4ri(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of Cython modules
    depending on the M4RI and/or M4RIe libraries.

    In addition to the modularization purposes that this tag serves,
    it also provides attribution to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__m4ri
        sage: sage__libs__m4ri().is_present()                                           # needs sage.libs.m4ri
        FeatureTestResult('sage.libs.m4ri', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__m4ri
            sage: isinstance(sage__libs__m4ri(), sage__libs__m4ri)
            True
        """

class sage__libs__ntl(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.ntl`
    and other modules depending on NTL.

    In addition to the modularization purposes that this tag serves,
    it also provides attribution to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__ntl
        sage: sage__libs__ntl().is_present()                                            # needs sage.libs.ntl
        FeatureTestResult('sage.libs.ntl', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__ntl
            sage: isinstance(sage__libs__ntl(), sage__libs__ntl)
            True
        """

class sage__libs__giac(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.giac`.

    In addition to the modularization purposes that this tag serves,
    it also provides attribution to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__giac
        sage: sage__libs__giac().is_present()                                           # needs sage.libs.giac
        FeatureTestResult('sage.libs.giac', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__giac
            sage: isinstance(sage__libs__giac(), sage__libs__giac)
            True
        """

class sage__libs__homfly(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.homfly`.

    In addition to the modularization purposes that this tag serves,
    it also provides attribution to the upstream project.

    TESTS::

        sage: from sage.features.sagemath import sage__libs__homfly
        sage: sage__libs__homfly().is_present()                                         # needs sage.libs.homfly
        FeatureTestResult('sage.libs.homfly', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__homfly
            sage: isinstance(sage__libs__homfly(), sage__libs__homfly)
            True
        """

class sage__libs__pari(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.libs.pari`.

    SageMath uses the :ref:`PARI <spkg_pari>` library (via :ref:`cypari2
    <spkg_cypari>`) for numerous purposes.  Doctests that involves such features
    should be marked ``# needs sage.libs.pari``.

    In addition to the modularization purposes that this tag serves, it also
    provides attribution to the upstream project.

    EXAMPLES::

        sage: R.<a> = QQ[]
        sage: S.<x> = R[]
        sage: f = x^2 + a; g = x^3 + a
        sage: r = f.resultant(g); r                                                     # needs sage.libs.pari
        a^3 + a^2

    TESTS::

        sage: from sage.features.sagemath import sage__libs__pari
        sage: sage__libs__pari().is_present()                                           # needs sage.libs.pari
        FeatureTestResult('sage.libs.pari', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__libs__pari
            sage: isinstance(sage__libs__pari(), sage__libs__pari)
            True
        """

class sage__libs__singular(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.libs.singular`
    (the library interface to Singular) and :mod:`sage.interfaces.singular` (the pexpect
    interface to Singular). By design, we do not distinguish between these two, in order
    to facilitate the conversion of code from the pexpect interface to the library
    interface.

    .. SEEALSO::

        :class:`Feature singular <~sage.features.singular.Singular>`

    TESTS::

        sage: from sage.features.singular import sage__libs__singular
        sage: sage__libs__singular().is_present()                                       # needs sage.libs.singular
        FeatureTestResult('sage.libs.singular', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.singular import sage__libs__singular
            sage: isinstance(sage__libs__singular(), sage__libs__singular)
            True
        """

class sage__modular(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.modular`.

    TESTS::

        sage: from sage.features.sagemath import sage__modular
        sage: sage__modular().is_present()                                              # needs sage.modular
        FeatureTestResult('sage.modular', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__modular
            sage: isinstance(sage__modular(), sage__modular)
            True
        """

class sage__modules(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.modules`.

    EXAMPLES:

    All uses of implementations of vector spaces / free modules in SageMath, whether
    :class:`sage.modules.free_module.FreeModule`,
    :class:`sage.combinat.free_module.CombinatorialFreeModule`,
    :class:`sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`, or
    additive abelian groups, should be marked ``# needs sage.modules``.

    The same holds for matrices, tensors, algebras, quadratic forms,
    point lattices, root systems, matrix/affine/Weyl/Coxeter groups, matroids,
    and ring derivations.

    Likewise, all uses of :mod:`sage.coding`, :mod:`sage.crypto`, and :mod:`sage.homology`
    in doctests should be marked ``# needs sage.modules``.

    TESTS::

        sage: from sage.features.sagemath import sage__modules
        sage: sage__modules().is_present()                                              # needs sage.modules
        FeatureTestResult('sage.modules', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__modules
            sage: isinstance(sage__modules(), sage__modules)
            True
        """

class sage__numerical__mip(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.numerical.mip`.

    TESTS::

        sage: from sage.features.sagemath import sage__numerical__mip
        sage: sage__numerical__mip().is_present()                                       # needs sage.numerical.mip
        FeatureTestResult('sage.numerical.mip', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__numerical__mip
            sage: isinstance(sage__numerical__mip(), sage__numerical__mip)
            True
        """

class sage__plot(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.plot`.

    TESTS::

        sage: from sage.features.sagemath import sage__plot
        sage: sage__plot().is_present()                                                 # needs sage.plot
        FeatureTestResult('sage.plot', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__plot
            sage: isinstance(sage__plot(), sage__plot)
            True
        """

class sage__rings__complex_double(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.complex_double`.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__complex_double
        sage: sage__rings__complex_double().is_present()                                # needs sage.rings.complex_double
        FeatureTestResult('sage.rings.complex_double', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__complex_double
            sage: isinstance(sage__rings__complex_double(), sage__rings__complex_double)
            True
        """

class sage__rings__finite_rings(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.finite_rings`;
    specifically, the element implementations using the :ref:`PARI <spkg_pari>` library.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__finite_rings
        sage: sage__rings__finite_rings().is_present()                                  # needs sage.rings.finite_rings
        FeatureTestResult('sage.rings.finite_rings', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__finite_rings
            sage: isinstance(sage__rings__finite_rings(), sage__rings__finite_rings)
            True
        """

class sage__rings__function_field(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.function_field`.

    EXAMPLES:

    Rational function fields are always available::

        sage: K.<x> = FunctionField(QQ)
        sage: K.maximal_order()
        Maximal order of Rational function field in x over Rational Field

    Use the tag ``# needs sage.rings.function_field`` whenever extensions
    of function fields (by adjoining a root of a univariate polynomial) come into play::

        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x)); L                         # needs sage.rings.function_field
        Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x

    Such extensions of function fields are implemented using Gröbner bases of polynomial rings;
    Sage makes essential use of the :ref:`Singular <spkg_singular>` system for this.
    (It is not necessary to use the tag ``# needs sage.libs.singular``; it is
    implied by ``# needs sage.rings.function_field``.)

    TESTS::

        sage: from sage.features.sagemath import sage__rings__function_field
        sage: sage__rings__function_field().is_present()                                # needs sage.rings.function_field
        FeatureTestResult('sage.rings.function_field', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__function_field
            sage: isinstance(sage__rings__function_field(), sage__rings__function_field)
            True
        """

class sage__rings__number_field(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.number_field`.

    Number fields are implemented in Sage using a complicated mixture of various libraries,
    including :ref:`FLINT <spkg_flint>`, :ref:`GAP <spkg_gap>`,
    :ref:`MPFI <spkg_mpfi>`, :ref:`NTL <spkg_ntl>`, and :ref:`PARI <spkg_pari>`.

    EXAMPLES:

    Rational numbers are, of course, always available::

        sage: QQ in NumberFields()
        True

    Doctests that construct algebraic number fields should be marked ``# needs sage.rings.number_field``::

        sage: # needs sage.rings.number_field
        sage: K.<cuberoot2> = NumberField(x^3 - 2)
        sage: L.<cuberoot3> = K.extension(x^3 - 3)
        sage: S.<sqrt2> = L.extension(x^2 - 2); S
        Number Field in sqrt2 with defining polynomial x^2 - 2 over its base field

        sage: # needs sage.rings.number_field
        sage: K.<zeta> = CyclotomicField(15)
        sage: CC(zeta)
        0.913545457642601 + 0.406736643075800*I

    Doctests that make use of the algebraic field ``QQbar`` or the algebraic real field ``AA``
    should be marked likewise::

        sage: # needs sage.rings.number_field
        sage: AA(-1)^(1/3)
        -1
        sage: QQbar(-1)^(1/3)
        0.500000000000000? + 0.866025403784439?*I

    Use of the universal cyclotomic field should be marked
    ``# needs sage.libs.gap sage.rings.number_field``.

        sage: # needs sage.libs.gap sage.rings.number_field
        sage: UCF = UniversalCyclotomicField(); UCF
        Universal Cyclotomic Field
        sage: E = UCF.gen
        sage: f = E(2) + E(3); f
        2*E(3) + E(3)^2
        sage: f.galois_conjugates()
        [2*E(3) + E(3)^2, E(3) + 2*E(3)^2]

    TESTS::

        sage: from sage.features.sagemath import sage__rings__number_field
        sage: sage__rings__number_field().is_present()                                  # needs sage.rings.number_field
        FeatureTestResult('sage.rings.number_field', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__number_field
            sage: isinstance(sage__rings__number_field(), sage__rings__number_field)
            True
        """

class sage__rings__padics(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of ``sage.rings.padics``.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__padics
        sage: sage__rings__padics().is_present()                                        # needs sage.rings.padics
        FeatureTestResult('sage.rings.padics', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__padics
            sage: isinstance(sage__rings__padics(), sage__rings__padics)
            True
        """

class sage__rings__polynomial__pbori(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of :mod:`sage.rings.polynomial.pbori`.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__polynomial__pbori
        sage: sage__rings__polynomial__pbori().is_present()                             # needs sage.rings.polynomial.pbori
        FeatureTestResult('sage.rings.polynomial.pbori', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__polynomial__pbori
            sage: isinstance(sage__rings__polynomial__pbori(), sage__rings__polynomial__pbori)
            True
        """

class sage__rings__real_double(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.real_double`.

    EXAMPLES:

    The Real Double Field is basically always available, and no ``# optional/needs`` tag is needed::

        sage: RDF.characteristic()
        0

    The feature exists for use in doctests of Python modules that are shipped by the
    most fundamental distributions.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__real_double
        sage: sage__rings__real_double().is_present()                                   # needs sage.rings.real_double
        FeatureTestResult('sage.rings.real_double', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__real_double
            sage: isinstance(sage__rings__real_double(), sage__rings__real_double)
            True
        """

class sage__rings__real_mpfr(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.rings.real_mpfr`.

    TESTS::

        sage: from sage.features.sagemath import sage__rings__real_mpfr
        sage: sage__rings__real_mpfr().is_present()                                     # needs sage.rings.real_mpfr
        FeatureTestResult('sage.rings.real_mpfr', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__rings__real_mpfr
            sage: isinstance(sage__rings__real_mpfr(), sage__rings__real_mpfr)
            True
        """

class sage__sat(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.sat`.

    TESTS::

        sage: from sage.features.sagemath import sage__sat
        sage: sage__sat().is_present()                                                  # needs sage.sat
        FeatureTestResult('sage.sat', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__sat
            sage: isinstance(sage__sat(), sage__sat)
            True
        """

class sage__schemes(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.schemes`.

    TESTS::

        sage: from sage.features.sagemath import sage__schemes
        sage: sage__schemes().is_present()                                              # needs sage.schemes
        FeatureTestResult('sage.schemes', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__schemes
            sage: isinstance(sage__schemes(), sage__schemes)
            True
        """

class sage__symbolic(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :mod:`sage.symbolic`.

    EXAMPLES:

    The symbolics subsystem of Sage will be provided by the distribution
    sagemath-symbolics, in preparation at :issue:`35095`. If it is not installed,
    Sage will be able to provide installation advice::

        sage: from sage.features.sagemath import sage__symbolic
        sage: print(sage__symbolic().resolution())                                      # optional - sage_spkg, not tested
        ...To install sagemath_symbolics...you can try to run...
        pip install sagemath-symbolics
        ...

    TESTS::

        sage: from sage.features.sagemath import sage__symbolic
        sage: sage__symbolic().is_present()                                             # needs sage.symbolic
        FeatureTestResult('sage.symbolic', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sagemath import sage__symbolic
            sage: isinstance(sage__symbolic(), sage__symbolic)
            True
        """

def all_features():
    """
    Return features corresponding to parts of the Sage library.

    These features are named after Python packages/modules (e.g., :mod:`sage.symbolic`),
    not distribution packages (**sagemath-symbolics**).

    This design is motivated by a separation of concerns: The author of a module that depends
    on some functionality provided by a Python module usually already knows the
    name of the Python module, so we do not want to force the author to also
    know about the distribution package that provides the Python module.

    Instead, we associate distribution packages to Python modules in
    :mod:`sage.features.sagemath` via the ``spkg`` parameter of
    :class:`~sage.features.Feature`.

    EXAMPLES::

        sage: from sage.features.sagemath import all_features
        sage: list(all_features())
        [...Feature('sage.combinat'), ...]
    """
