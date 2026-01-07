"""
Examples of Sandpile

AUTHORS:

- David Perkinson (2015-05) [Using `examples.py` from homology as
  template.]

This file constructs some examples of Sandpiles.

The examples are accessible by typing ``sandpiles.NAME``, where
``NAME`` is the name of the example.  You can get a list by typing
``sandpiles.`` and hitting the :kbd:`Tab` key::

   sandpiles.Complete
   sandpiles.Cycle
   sandpiles.Diamond
   sandpiles.Grid
   sandpiles.House

See the documentation for each particular type of example for full details.
"""
from sage.graphs.graph_generators import graphs as graphs
from sage.sandpiles.sandpile import Sandpile as Sandpile

class SandpileExamples:
    """
    Some examples of sandpiles.

    Here are the available examples; you can also type
    ``sandpiles.``  and hit tab to get a list:

    - :meth:`Complete`
    - :meth:`Cycle`
    - :meth:`Diamond`
    - :meth:`Grid`
    - :meth:`House`

    EXAMPLES::

        sage: s = sandpiles.Complete(4)
        sage: s.invariant_factors()
        [1, 4, 4]
        sage: s.laplacian()
        [ 3 -1 -1 -1]
        [-1  3 -1 -1]
        [-1 -1  3 -1]
        [-1 -1 -1  3]
    """
    def __call__(self) -> None:
        """
        If ``sandpiles()`` is executed, return a helpful message.

        OUTPUT: none

        EXAMPLES::

            sage: sandpiles()
            Try sandpiles.FOO() where FOO is in the list:
            <BLANKLINE>
                Complete, Cycle, Diamond, Fan, Grid, House, Wheel
        """
    def Complete(self, n):
        """
        The complete sandpile graph with `n` vertices.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT: Sandpile

        EXAMPLES::

            sage: s = sandpiles.Complete(4)
            sage: s.group_order()
            16
            sage: sandpiles.Complete(3) == sandpiles.Cycle(3)
            True
        """
    def Cycle(self, n):
        """
        Sandpile on the cycle graph with `n` vertices.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: Sandpile

        EXAMPLES::

            sage: s = sandpiles.Cycle(4)
            sage: s.edges(sort=True)
            [(0, 1, 1),
             (0, 3, 1),
             (1, 0, 1),
             (1, 2, 1),
             (2, 1, 1),
             (2, 3, 1),
             (3, 0, 1),
             (3, 2, 1)]
        """
    def Diamond(self):
        """
        Sandpile on the diamond graph.

        OUTPUT: Sandpile

        EXAMPLES::

            sage: s = sandpiles.Diamond()
            sage: s.invariant_factors()
            [1, 1, 8]
        """
    def Fan(self, n, deg_three_verts: bool = False):
        """
        Sandpile on the Fan graph with a total of `n` vertices.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: Sandpile

        EXAMPLES::

            sage: f = sandpiles.Fan(10)
            sage: f.group_order() == fibonacci(18)                                      # needs sage.libs.pari
            True
            sage: f = sandpiles.Fan(10,True)  # all nonsink vertices have deg 3
            sage: f.group_order() == fibonacci(20)                                      # needs sage.libs.pari
            True
        """
    def Grid(self, m, n):
        """
        Sandpile on the diamond graph.

        INPUT:

        - ``m``, ``n`` -- negative integers

        OUTPUT: Sandpile

        EXAMPLES::

            sage: s = sandpiles.Grid(2,3)
            sage: s.vertices(sort=True)
            [(0, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
            sage: s.invariant_factors()
            [1, 1, 1, 1, 1, 2415]
            sage: s = sandpiles.Grid(1,1)
            sage: s.dict()
            {(0, 0): {(1, 1): 4}, (1, 1): {(0, 0): 4}}
        """
    def House(self):
        """
        Sandpile on the House graph.

        OUTPUT: Sandpile

        EXAMPLES::

            sage: s = sandpiles.House()
            sage: s.invariant_factors()
            [1, 1, 1, 11]
        """
    def Wheel(self, n):
        """
        Sandpile on the wheel graph with a total of `n` vertices.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: Sandpile

        EXAMPLES::

            sage: w = sandpiles.Wheel(6)
            sage: w.invariant_factors()
            [1, 1, 1, 11, 11]
        """

sandpiles: SandpileExamples
