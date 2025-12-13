import sage.structure.parent
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.superseded import deprecation as deprecation
from typing import ClassVar

class Parent(sage.structure.parent.Parent):
    """Parent(category=None, *)

    File: /build/sagemath/src/sage/src/sage/structure/parent_old.pyx (starting at line 44)

    Parents are the Sage / mathematical analogues of container objects
    in computer science.

    TESTS::

        sage: # needs sage.modules
        sage: V = VectorSpace(GF(2,'a'), 2)
        sage: V.list()
        [(0, 0), (1, 0), (0, 1), (1, 1)]
        sage: MatrixSpace(GF(3), 1, 1).list()
        [[0], [1], [2]]
        sage: DirichletGroup(3).list()                                                  # needs sage.libs.pari sage.modular
        [Dirichlet character modulo 3 of conductor 1 mapping 2 |--> 1,
         Dirichlet character modulo 3 of conductor 3 mapping 2 |--> -1]

        sage: # needs sage.rings.finite_rings
        sage: K = GF(7^6,'a')
        sage: K.list()[:10]                     # long time
        [0, 1, 2, 3, 4, 5, 6, a, a + 1, a + 2]
        sage: K.<a> = GF(4)
        sage: K.list()
        [0, a, a + 1, 1]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/structure/parent_old.pyx (starting at line 73)"""
