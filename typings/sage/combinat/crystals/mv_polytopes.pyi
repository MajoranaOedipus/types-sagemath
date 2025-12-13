from sage.combinat.crystals.pbw_crystal import PBWCrystal as PBWCrystal, PBWCrystalElement as PBWCrystalElement

class MVPolytope(PBWCrystalElement):
    """
    A Mirković-Vilonen (MV) polytope.

    EXAMPLES:

    We can create an animation showing how the MV polytope changes
    under a string of crystal operators::

        sage: MV = crystals.infinity.MVPolytopes(['C', 2])
        sage: u = MV.highest_weight_vector()
        sage: L = RootSystem(['C',2,1]).ambient_space()
        sage: s = [1,2,1,2,2,2,1,1,1,1,2,1,2,2,1,2]
        sage: BB = [[-9, 2], [-10, 2]]
        sage: p = L.plot(reflection_hyperplanes=False, bounding_box=BB)  # long time
        sage: frames = [p + L.plot_mv_polytope(u.f_string(s[:i]),  # long time
        ....:                                  circle_size=0.1,
        ....:                                  wireframe='green',
        ....:                                  fill='purple',
        ....:                                  bounding_box=BB)
        ....:           for i in range(len(s))]
        sage: for f in frames:  # long time
        ....:     f.axes(False)
        sage: animate(frames).show(delay=60) # optional -- ImageMagick # long time
    """
    def polytope(self, P=None):
        """
        Return a polytope of ``self``.

        INPUT:

        - ``P`` -- (optional) a space to realize the polytope; default is
          the weight lattice realization of the crystal

        EXAMPLES::

            sage: MV = crystals.infinity.MVPolytopes(['C', 3])
            sage: b = MV.module_generators[0].f_string([3,2,3,2,1])
            sage: P = b.polytope(); P
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 6 vertices
            sage: P.vertices()
            (A vertex at (0, 0, 0),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, -1, 0),
             A vertex at (1, 1, -2),
             A vertex at (1, 1, 2))
        """
    def plot(self, P=None, **options):
        """
        Plot ``self``.

        INPUT:

        - ``P`` -- (optional) a space to realize the polytope; default is
          the weight lattice realization of the crystal

        .. SEEALSO::

            :meth:`~sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods.plot_mv_polytope`

        EXAMPLES::

            sage: MV = crystals.infinity.MVPolytopes(['C', 2])
            sage: b = MV.highest_weight_vector().f_string([1,2,1,2,2,2,1,1,1,1,2,1])
            sage: b.plot()                                                              # needs sage.plot
            Graphics object consisting of 12 graphics primitives

        Here is the above example placed inside the ambient space
        of type `C_2`:

        .. PLOT::
            :width: 300 px

            MV = crystals.infinity.MVPolytopes(['C', 2])
            b = MV.highest_weight_vector().f_string([1,2,1,2,2,2,1,1,1,1,2,1])
            L = RootSystem(['C', 2, 1]).ambient_space()
            p = L.plot(reflection_hyperplanes=False, bounding_box=[[-8,2], [-8,2]])
            p += b.plot()
            p.axes(False)
            sphinx_plot(p)
        """

class MVPolytopes(PBWCrystal):
    """
    The crystal of Mirković-Vilonen (MV) polytopes.

    Let `W` denote the corresponding Weyl group and `P_{\\RR} = \\RR \\otimes P`.
    Let `\\Gamma = \\{ w \\Lambda_i \\mid w \\in W, i \\in I \\}`. Consider
    `M = (M_{\\gamma} \\in \\ZZ)_{\\gamma \\in \\Gamma}` that satisfy the
    *tropical Plücker relations* (see Proposition 7.1 of [BZ01]_).
    The *MV polytope* is defined as

    .. MATH::

        P(M) = \\{ \\alpha \\in P_{\\RR} \\mid
        \\langle \\alpha, \\gamma \\rangle \\geq M_{\\gamma}
        \\text{ for all } \\gamma \\in \\Gamma \\}.

    The vertices `\\{\\mu_w\\}_{w \\in W}` are given by

    .. MATH::

        \\langle \\mu_w, \\gamma \\rangle = M_{\\gamma}

    and are known as the GGMS datum of the MV polytope.

    Each path from `\\mu_e` to `\\mu_{w_0}` corresponds to a reduced
    expression `\\mathbf{i} = (i_1, \\ldots, i_m)` for `w_0` and the
    corresponding edge lengths `(n_k)_{k=1}^m` from the Lusztig datum
    with respect to `\\mathbf{i}`. Explicitly, we have

    .. MATH::

        \\begin{aligned}
        n_k & = -M_{w_{k-1} \\Lambda_{i_k}} - M_{w_k \\Lambda_{i_k}}
        - \\sum_{j \\neq i} a_{ji} M_{w_k \\Lambda_j},
        \\\\ \\mu_{w_k} - \\mu_{w_{k-1}} & = n_k w_{k-1} \\alpha_{i_k},
        \\end{aligned}

    where `w_k = s_{i_1} \\cdots s_{i_k}` and `(a_{ji})` is the Cartan matrix.

    MV polytopes have a crystal structure that corresponds to the
    crystal structure, which is isomorphic to `\\mathcal{B}(\\infty)`
    with `\\mu_{w_0} = 0`, on
    :class:`PBW data <sage.combinat.crystals.pbw_crystal.PBWCrystal>`.
    Specifically, we have `f_j P(M)` as being the unique MV polytope
    given by shifting `\\mu_e` by `-\\alpha_j` and fixing the vertices
    `\\mu_w` when `s_j w < w` (in Bruhat order) and the weight is given by
    `\\mu_e`. Furthermore, the `*`-involution is given by negating `P(M)`.

    INPUT:

    - ``cartan_type`` -- a Cartan type

    EXAMPLES::

        sage: MV = crystals.infinity.MVPolytopes(['B', 3])
        sage: hw = MV.highest_weight_vector()
        sage: x = hw.f_string([1,2,2,3,3,1,3,3,2,3,2,1,3,1,2,3,1,2,1,3,2]); x
        MV polytope with Lusztig datum (1, 1, 1, 3, 1, 0, 0, 1, 1)

    Elements are expressed in terms of Lusztig datum for a fixed
    reduced expression of `w_0`::

        sage: MV.default_long_word()
        [1, 3, 2, 3, 1, 2, 3, 1, 2]
        sage: MV.set_default_long_word([2,1,3,2,1,3,2,3,1])
        sage: x
        MV polytope with Lusztig datum (3, 1, 1, 0, 1, 0, 1, 3, 4)
        sage: MV.set_default_long_word([1, 3, 2, 3, 1, 2, 3, 1, 2])

    We can construct elements by giving it Lusztig data (with respect
    to the default long word reduced expression)::

        sage: MV([1,1,1,3,1,0,0,1,1])
        MV polytope with Lusztig datum (1, 1, 1, 3, 1, 0, 0, 1, 1)

    We can also construct elements by passing in a reduced expression
    for a long word::

        sage: x = MV([1,1,1,3,1,0,0,1,1], [3,2,1,3,2,3,2,1,2]); x
        MV polytope with Lusztig datum (1, 1, 1, 0, 1, 0, 5, 1, 1)
        sage: x.to_highest_weight()[1]
        [1, 2, 2, 2, 2, 2, 1, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1, 3]

    The highest weight crystal `B(\\lambda) \\subseteq B(\\infty)` is
    characterized by the MV polytopes that sit inside of `W \\lambda`
    (translating `\\mu_{w_0} \\mapsto \\lambda`)::

        sage: MV = crystals.infinity.MVPolytopes(['A',2])
        sage: La = MV.weight_lattice_realization().fundamental_weights()
        sage: R = crystals.elementary.R(La[1]+La[2])
        sage: T = tensor([R, MV])
        sage: x = T(R.module_generators[0], MV.highest_weight_vector())
        sage: lw = x.to_lowest_weight()[0]; lw
        [(2, 1, 0), MV polytope with Lusztig datum (1, 1, 1)]
        sage: lw[1].polytope().vertices()
        (A vertex at (0, 0, 0),
         A vertex at (0, 1, -1),
         A vertex at (1, -1, 0),
         A vertex at (1, 1, -2),
         A vertex at (2, -1, -1),
         A vertex at (2, 0, -2))

    .. PLOT::
        :width: 300 px

        MV = crystals.infinity.MVPolytopes(['A',2])
        x = MV.module_generators[0].f_string([1,2,2,1])
        L = RootSystem(['A',2,1]).ambient_space()
        p = L.plot(bounding_box=[[-2,2],[-4,2]]) + x.plot()
        p.axes(False)
        sphinx_plot(x.plot())

    REFERENCES:

    - [Kam2007]_
    - [Kam2010]_
    """
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: MV = crystals.infinity.MVPolytopes(['B', 2])
            sage: TestSuite(MV).run()
        """
    def set_latex_options(self, **kwds) -> None:
        """
        Set the latex options for the elements of ``self``.

        INPUT:

        - ``projection`` -- the projection; set to ``True`` to use the
          default projection of the specified weight lattice realization
          (initial: ``True``)
        - ``P`` -- the weight lattice realization to use (initial: the
          weight lattice realization of ``self``)
        - ``mark_endpoints`` -- whether to mark the endpoints (initial: ``True``)
        - ``circle_size`` -- the size of the endpoint circles (initial: 0.1)

        EXAMPLES::

            sage: MV = crystals.infinity.MVPolytopes(['C', 2])
            sage: P = RootSystem(['C', 2]).weight_lattice()
            sage: b = MV.highest_weight_vector().f_string([1,2,1,2])
            sage: latex(b)
            \\begin{tikzpicture}
            \\draw (0, 0) -- (0, -2) -- (-1, -3) -- (-1, -3) -- (-2, -2);
            \\draw (0, 0) -- (-1, 1) -- (-1, 1) -- (-2, 0) -- (-2, -2);
            \\draw[fill=black] (0, 0) circle (0.1);
            \\draw[fill=black] (-2, -2) circle (0.1);
            \\end{tikzpicture}
            sage: MV.set_latex_options(P=P, circle_size=float(0.2))
            sage: latex(b)
            \\begin{tikzpicture}
            \\draw (0, 0) -- (2, -2) -- (2, -3) -- (2, -3) -- (0, -2);
            \\draw (0, 0) -- (-2, 1) -- (-2, 1) -- (-2, 0) -- (0, -2);
            \\draw[fill=black] (0, 0) circle (0.2);
            \\draw[fill=black] (0, -2) circle (0.2);
            \\end{tikzpicture}
            sage: MV.set_latex_options(mark_endpoints=False)
            sage: latex(b)
            \\begin{tikzpicture}
            \\draw (0, 0) -- (2, -2) -- (2, -3) -- (2, -3) -- (0, -2);
            \\draw (0, 0) -- (-2, 1) -- (-2, 1) -- (-2, 0) -- (0, -2);
            \\end{tikzpicture}
            sage: MV.set_latex_options(P=MV.weight_lattice_realization(),
            ....:                      circle_size=0.2,
            ....:                      mark_endpoints=True)
        """
    def latex_options(self):
        """
        Return the latex options of ``self``.

        EXAMPLES::

            sage: MV = crystals.infinity.MVPolytopes(['F', 4])
            sage: MV.latex_options()
            {'P': Ambient space of the Root system of type ['F', 4],
             'circle_size': 0.1,
             'mark_endpoints': True,
             'projection': True}
        """
    Element = MVPolytope
