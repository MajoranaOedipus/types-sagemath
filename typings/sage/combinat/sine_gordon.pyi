from sage.functions.log import exp as exp
from sage.functions.other import ceil as ceil, imag_part as imag_part, real_part as real_part
from sage.functions.trig import cos as cos, sin as sin
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_mpfr import RR as RR
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.structure.sage_object import SageObject as SageObject
from sage.symbolic.constants import I as I, pi as pi
from sage.symbolic.ring import SR as SR

class SineGordonYsystem(SageObject):
    """
    A class to model a (reduced) sine-Gordon Y-system.

    Note that the generations, together with all integer tuples, in this
    implementation are numbered from 0 while in [NS]_ they are numbered from 1

    INPUT:

    - ``X`` -- the type of the Y-system to construct (either 'A' or 'D')
    - ``na`` -- the tuple of positive integers defining the Y-system
      with ``na[0] > 2``

    See [NS]_

    EXAMPLES::

        sage: Y = SineGordonYsystem('A',(6,4,3)); Y
        A sine-Gordon Y-system of type A with defining integer tuple (6, 4, 3)
        sage: Y.intervals()
        (((0, 0, 'R'),),
         ((0, 17, 'L'),
          (17, 34, 'L'),
        ...
          (104, 105, 'R'),
          (105, 0, 'R')))
        sage: Y.triangulation()
        ((17, 89),
         (17, 72),
         (34, 72),
        ...
         (102, 105),
         (103, 105))
        sage: Y.plot()     #not tested
    """
    def __init__(self, X, na) -> None:
        """
        TESTS::

            sage: Y = SineGordonYsystem('A',(6,4,3)); Y  # indirect doctest
            A sine-Gordon Y-system of type A with defining integer tuple
            (6, 4, 3)

            sage: SineGordonYsystem('E',(6,4,3))
            Traceback (most recent call last):
            ...
            ValueError: the type must be either 'A' or 'D'
            sage: SineGordonYsystem('A',(2,4,3))
            Traceback (most recent call last):
            ...
            ValueError: the first integer in the defining sequence must be
            greater than 2
            sage: SineGordonYsystem('A',(6,-4,3))
            Traceback (most recent call last):
            ...
            ValueError: the defining sequence must contain only positive
            integers
            sage: SineGordonYsystem('A',(3,))
            Traceback (most recent call last):
            ...
            ValueError: the integer sequence (3,) in type 'A' is not allowed
            as input
        """
    def type(self):
        """
        Return the type of ``self``.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.type()
            'A'
        """
    def F(self):
        """
        Return the number of generations in ``self``.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.F()
            3
        """
    def na(self):
        """
        Return the sequence of the integers `n_a` defining ``self``.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.na()
            (6, 4, 3)
        """
    @cached_method
    def rk(self):
        """
        Return the sequence of integers ``r^{(k)}``, i.e. the width of
        an interval of type 'L' or 'R' in the ``k``-th generation.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.rk()
            (106, 17, 4)
        """
    @cached_method
    def pa(self):
        """
        Return the sequence of integers  ``p_a``, i.e. the total number of
        intervals of types 'NL' and 'NR' in the ``(a+1)``-th generation.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.pa()
            (1, 6, 25)
        """
    @cached_method
    def qa(self):
        """
        Return the sequence of integers  ``q_a``, i.e. the total number of
        intervals of types 'L' and 'R' in the ``(a+1)``-th generation.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.qa()
            (6, 25, 81)
        """
    @cached_method
    def r(self):
        """
        Return the number of vertices in the polygon realizing ``self``.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.r()
            106
        """
    @cached_method
    def vertices(self):
        """
        Return the vertices of the polygon realizing ``self`` as the ring of
        integers modulo ``self.r()``.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.vertices()
            Ring of integers modulo 106
        """
    @cached_method
    def triangulation(self):
        """
        Return the initial triangulation of the polygon realizing
        ``self`` as a tuple of pairs of vertices.

        .. WARNING::

            In type 'D' the returned triangulation does NOT contain the two
            radii.

        ALGORITHM:

        We implement the four cases described by Figure 14 in [NS]_.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.triangulation()
            ((17, 89),
             (17, 72),
            ...
             (102, 105),
             (103, 105))
        """
    @cached_method
    def intervals(self):
        """
        Return, divided by generation, the list of intervals used to construct
        the initial triangulation.

        Each such interval is a triple ``(p, q, X)`` where ``p`` and
        ``q`` are the two extremal vertices of the interval and ``X``
        is the type of the interval (one of 'L', 'R', 'NL', 'NR').

        ALGORITHM:

        The algorithm used here is the one described in section 5.1 of [NS]_.
        The only difference is that we get rid of the special case of the first
        generation by treating the whole disk as a type 'R' interval.

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.intervals()
            (((0, 0, 'R'),),
             ((0, 17, 'L'),
              (17, 34, 'L'),
            ...
              (104, 105, 'R'),
              (105, 0, 'R')))
        """
    def plot(self, **kwds):
        """
        Plot the initial triangulation associated to ``self``.

        INPUT:

        - ``radius`` -- the radius of the disk; by default the length of
          the circle is the number of vertices
        - ``points_color`` -- the color of the vertices; default 'black'
        - ``points_size`` -- the size of the vertices; default 7
        - ``triangulation_color`` -- the color of the arcs; default 'black'
        - ``triangulation_thickness`` -- the thickness of the arcs; default 0.5
        - ``shading_color`` -- the color of the shading used on neuter
          intervals; default 'lightgray'
        - ``reflections_color`` -- the color of the reflection axes; default
          'blue'
        - ``reflections_thickness`` -- the thickness of the reflection axes;
          default 1

        EXAMPLES::

            sage: Y = SineGordonYsystem('A',(6,4,3))
            sage: Y.plot()                      # long time (2s)                        # needs sage.plot
            Graphics object consisting of 219 graphics primitives
        """
