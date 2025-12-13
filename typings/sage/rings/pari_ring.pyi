from sage.categories.rings import Rings as Rings
from sage.libs.pari import pari as pari
from sage.misc.fast_methods import Singleton as Singleton
from sage.structure.element import RingElement as RingElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp

class Pari(RingElement):
    """
    Element of Pari pseudo-ring.
    """
    def __init__(self, x, parent=None) -> None:
        """
        EXAMPLES::

            sage: R = PariRing()
            sage: f = R('x^3 + 1/2')
            sage: f
            x^3 + 1/2
            sage: type(f)
            <class 'sage.rings.pari_ring.PariRing_with_category.element_class'>
            sage: loads(f.dumps()) == f
            True
        """
    def __neg__(self):
        """
        EXAMPLES::

            sage: R = PariRing()
            sage: a = R(3)
            sage: -a
            -3
        """
    def __pow__(self, other):
        """
        EXAMPLES::

            sage: R = PariRing()
            sage: a = R(3)
            sage: a^2
            9
        """
    def __invert__(self):
        """
        EXAMPLES::

            sage: R = PariRing()
            sage: a = R(3)
            sage: ~a
            1/3
        """
    def __int__(self) -> int: ...

class PariRing(Singleton, Parent):
    """
    EXAMPLES::

        sage: R = PariRing(); R
        Pseudoring of all PARI objects.
        sage: loads(R.dumps()) is R
        True
    """
    Element = Pari
    def __init__(self) -> None: ...
    def is_field(self, proof: bool = True) -> bool: ...
    def characteristic(self) -> None: ...
    def random_element(self, x=None, y=None, distribution=None):
        """
        Return a random integer in Pari.

        .. NOTE::

            The given arguments are passed to ``ZZ.random_element(...)``.

        INPUT:

        - `x`, `y` -- optional integers, that are lower and upper bound
          for the result. If only `x` is provided, then the result is
          between 0 and `x-1`, inclusive. If both are provided, then the
          result is between `x` and `y-1`, inclusive.

        - ``distribution`` -- (optional) string, so that ``ZZ`` can make sense
          of it as a probability distribution

        EXAMPLES::

            sage: R = PariRing()
            sage: R.random_element().parent() is R
            True
            sage: R(5) <= R.random_element(5,13) < R(13)
            True
            sage: R.random_element(distribution='1/n').parent() is R
            True
        """
    def zeta(self):
        """
        Return -1.

        EXAMPLES::

            sage: R = PariRing()
            sage: R.zeta()
            -1
        """
