from .backend_cdd import Polyhedron_cdd as Polyhedron_cdd
from .base_RDF import Polyhedron_RDF as Polyhedron_RDF

class Polyhedron_RDF_cdd(Polyhedron_cdd, Polyhedron_RDF):
    """
    Polyhedra over RDF with cdd.

    INPUT:

    - ``ambient_dim`` -- integer; the dimension of the ambient space

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: parent = Polyhedra(RDF, 2, backend='cdd')
        sage: from sage.geometry.polyhedron.backend_cdd_rdf import Polyhedron_RDF_cdd
        sage: Polyhedron_RDF_cdd(parent, [ [(1,0),(0,1),(0,0)], [], []], None, verbose=False)
        A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 3 vertices

    TESTS:

    Checks that :issue:`24877` is fixed::

        sage: n1 = 1045602428815736513789288687833080060779
        sage: n2 = 76591188009721216624438400001815308369088648782156930777145
        sage: n3 = 141046287872967162025203834781636948939209065735662536571684677443277621519222367249160281646288602157866548267640061850035
        sage: n4 = 169296796161110084211548448622149955145002732358082778064645608216077666698460018565094060494217
        sage: verts = [[159852/261157, 227425/261157],
        ....:  [9/10, 7/10],
        ....:  [132/179, 143/179],
        ....:  [8/11, -59/33],
        ....:  [174/167, 95/167],
        ....:  [3/2, -1/2],
        ....:  [-1162016360399650274197433414376009691155/n1,
        ....:    1626522696050475596930360993440360903664/n1],
        ....:  [-112565666321600055047037445519656973805313121630809713051718/n2,
        ....:    -15318574020578896781701071673537253327221557273483622682053/n2],
        ....:  [-222823992658914823798345935660863293259608796350232624336738123149601409997996952470726909468671437285720616325991022633438/n3,
        ....:   (-20857694835570598502487921801401627779907095024585170129381924208334510445828894861553290291713792691651471189597832832973*5)/n3],
        ....:  [-100432602675156818915933977983765863676402454634873648118147187022041830166292457614016362515164/n4,
        ....:   -429364759737031049317769174492863890735634068814210512342503744054527903830844433491149538512537/n4]]
        sage: P = Polyhedron(verts, base_ring=RDF)
        sage: len(P.faces(1))
        10
        sage: P.n_vertices()
        10
        sage: P.n_facets()
        10

    Check that :issue:`19803` is fixed::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: P_cdd = Polyhedra(RDF, 3, 'cdd')
        sage: P_cdd([[],[],[]], None)
        The empty polyhedron in RDF^3
        sage: Polyhedron(vertices=[], backend='cdd', base_ring=RDF)
        The empty polyhedron in RDF^0
    """
    def __init__(self, parent, Vrep, Hrep, **kwds) -> None:
        """
        The Python constructor.

        See :class:`Polyhedron_base` for a description of the input
        data.

        TESTS::

            sage: p = Polyhedron(backend='cdd', base_ring=RDF)
            sage: type(p)
            <class 'sage.geometry.polyhedron.parent.Polyhedra_RDF_cdd_with_category.element_class'>
            sage: TestSuite(p).run()
        """
