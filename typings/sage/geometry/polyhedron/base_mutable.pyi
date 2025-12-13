from .base import Polyhedron_base as Polyhedron_base
from sage.misc.abstract_method import abstract_method as abstract_method

class Polyhedron_mutable(Polyhedron_base):
    """
    Base class for polyhedra that allow mutability.

    This should not be used directly.
    """
    def __hash__(self):
        """
        TESTS::

            sage: p = Polyhedron([[1, 1]], mutable=True)
            sage: set([p])
            Traceback (most recent call last):
            ...
            TypeError: mutable polyhedra are unhashable
            sage: p.set_immutable()
            sage: set([p])
            {A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex}
        """
    def is_mutable(self):
        """
        Return ``True`` if the polyhedron is mutable, i.e. it can be modified in place.

        EXAMPLES::

            sage: p = Polyhedron([[1, 1]], mutable=True)
            sage: p.is_mutable()
            True
            sage: p = Polyhedron([[1, 1]], mutable=False)
            sage: p.is_mutable()
            False
        """
    def is_immutable(self):
        """
        Return ``True`` if the polyhedron is immutable, i.e. it cannot be modified in place.

        EXAMPLES::

            sage: p = Polyhedron([[1, 1]], mutable=True)
            sage: p.is_immutable()
            False
            sage: p = Polyhedron([[1, 1]], mutable=False)
            sage: p.is_immutable()
            True
        """
    @abstract_method
    def set_immutable(self) -> None:
        """
        Make this polyhedron immutable. This operation cannot be undone.

        TESTS::

            sage: from sage.geometry.polyhedron.base_mutable import Polyhedron_mutable
            sage: p = polytopes.cube()
            sage: Polyhedron_mutable.set_immutable(p)
            Traceback (most recent call last):
            ...
            TypeError: 'AbstractMethod' object is not callable
        """
    @abstract_method
    def Vrepresentation(self) -> None:
        """
        A derived class must overwrite such that it restores Vrepresentation
        after clearing it.

        TESTS::

            sage: from sage.geometry.polyhedron.base_mutable import Polyhedron_mutable
            sage: p = polytopes.cube()
            sage: Polyhedron_mutable.Vrepresentation(p)
            Traceback (most recent call last):
            ...
            TypeError: 'AbstractMethod' object is not callable
        """
    @abstract_method
    def Hrepresentation(self) -> None:
        """
        A derived class must overwrite such that it restores Hrepresentation
        after clearing it.

        TESTS::

            sage: from sage.geometry.polyhedron.base_mutable import Polyhedron_mutable
            sage: p = polytopes.cube()
            sage: Polyhedron_mutable.Hrepresentation(p)
            Traceback (most recent call last):
            ...
            TypeError: 'AbstractMethod' object is not callable
        """
