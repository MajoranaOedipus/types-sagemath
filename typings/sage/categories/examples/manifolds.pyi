from sage.categories.manifolds import Manifolds as Manifolds
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Plane(UniqueRepresentation, Parent):
    """
    An example of a manifold: the `n`-dimensional plane.

    This class illustrates a minimal implementation of a manifold.

    EXAMPLES::

        sage: from sage.categories.manifolds import Manifolds
        sage: M = Manifolds(QQ).example(); M
        An example of a Rational Field manifold: the 3-dimensional plane

        sage: M.category()
        Category of manifolds over Rational Field

    We conclude by running systematic tests on this manifold::

        sage: TestSuite(M).run()
    """
    def __init__(self, n: int = 3, base_ring=None) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.manifolds import Manifolds
            sage: M = Manifolds(QQ).example(6); M
            An example of a Rational Field manifold: the 6-dimensional plane

        TESTS::

            sage: TestSuite(M).run()
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: from sage.categories.manifolds import Manifolds
            sage: M = Manifolds(QQ).example()
            sage: M.dimension()
            3
        """
    def an_element(self):
        """
        Return an element of the manifold, as per
        :meth:`Sets.ParentMethods.an_element`.

        EXAMPLES::

            sage: from sage.categories.manifolds import Manifolds
            sage: M = Manifolds(QQ).example()
            sage: M.an_element()
            (0, 0, 0)
        """
    Element = ElementWrapper
Example = Plane
