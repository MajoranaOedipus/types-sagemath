from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import catalan_number as catalan_number
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.functions.trig import cos as cos, sin as sin
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import sqrt as sqrt
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.latex import latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute, lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.sets.set import Set as Set
from sage.structure.list_clone import ClonableList as ClonableList
from sage.structure.set_factories import ParentWithSetFactory as ParentWithSetFactory, SetFactory as SetFactory, TopMostParentPolicy as TopMostParentPolicy
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LocalOptions:
    '''
    This class allow to add local options to an object.
    LocalOptions is like a dictionary, it has keys and values that represent
    options and the values associated to the option. This is useful to
    decorate an object with some optional informations.

    :class:`LocalOptions` should be used as follow.

    INPUT:

    - ``name`` -- the name of the LocalOptions

    - ``<options>=dict(...)`` -- dictionary specifying an option

    The options are specified by keyword arguments with their values
    being a dictionary which describes the option. The
    allowed/expected keys in the dictionary are:

    - ``checker`` -- a function for checking whether a particular value for
      the option is valid
    - ``default`` -- the default value of the option
    - ``values`` -- dictionary of the legal values for this option (this
      automatically defines the corresponding ``checker``); this dictionary
      gives the possible options, as keys, together with a brief description
      of them

    ::

        sage: from sage.combinat.parallelogram_polyomino import LocalOptions
        sage: o = LocalOptions(
        ....:     \'Name Example\',
        ....:     delim=dict(
        ....:         default=\'b\',
        ....:         values={\'b\':\'the option b\', \'p\':\'the option p\'}
        ....:     )
        ....: )
        sage: class Ex:
        ....:     options=o
        ....:     def _repr_b(self): return "b"
        ....:     def _repr_p(self): return "p"
        ....:     def __repr__(self): return self.options._dispatch(
        ....:         self, \'_repr_\',\'delim\'
        ....:     )
        sage: e = Ex(); e
        b
        sage: e.options(delim=\'p\'); e
        p

    This class is temporary, in the future, this class should be integrated in
    sage.structure.global_options.py. We should split global_option in two
    classes LocalOptions and GlobalOptions.
    '''
    def __init__(self, name: str = '', **options) -> None:
        '''
        Construct a new LocalOptions.

        INPUT:

        - ``name`` -- the name of the LocalOptions

        - ``<options>=dict(...)`` -- dictionary specifying an option

        The options are specified by keyword arguments with their values
        being a dictionary which describes the option. The
        allowed/expected keys in the dictionary are:

        - ``checker`` -- a function for checking whether a particular value for
          the option is valid
        - ``default`` -- the default value of the option
        - ``values`` -- dictionary of the legal values for this option (this
          automatically defines the corresponding ``checker``); this dictionary
          gives the possible options, as keys, together with a brief
          description of them.

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     )
            ....: )
        '''
    def __setitem__(self, key, value) -> None:
        '''
        The ``__setitem__`` method is used to change the current values of the
        options. It also checks that the supplied options are valid and changes
        any alias to its generic value.

        INPUT:

        - ``key`` -- an option

        - ``value`` -- the value

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     ),
            ....:     size=dict(
            ....:         default=1,
            ....:         checker=lambda x : x in NN
            ....:     )
            ....: )
            sage: o("display")
            \'list\'
            sage: o["display"]="diagram"
            sage: o("display")
            \'diagram\'
            sage: o["display"]="?"
            Current value : diagram
            {\'default\': \'list\', \'values\':
            {\'diagram\': \'diagram representation\',
            \'list\': \'list representation\'}}
            sage: o("size")
            1
            sage: o["size"]=3
            sage: o("size")
            3
            sage: o["size"]=-6
        '''
    def __call__(self, *get_values, **options):
        '''
        Get or set value of the option ``option``.

        INPUT:

        - ``get_values`` -- the options to be printed

        - ``<options>=dict(...)`` -- dictionary specifying an option see
          :class:`LocalOptions` for more details

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     )
            ....: )
            sage: o("display")
            \'list\'
            sage: o(display=\'diagram\')
            sage: o("display")
            \'diagram\'
            sage: o(display=\'?\')
            Current value : diagram
            {\'default\': \'list\', \'values\':
            {\'diagram\': \'diagram representation\',
            \'list\': \'list representation\'}}
        '''
    def __getitem__(self, key):
        '''
        Return the current value of the option ``key``.

        INPUT:

        - ``key`` -- an option

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     )
            ....: )
            sage: o["display"]
            \'list\'
        '''
    def __iter__(self):
        '''
        A generator for the options in ``self``.

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     )
            ....: )
            sage: all(key in [\'tikz_options\',\'display\'] for key in o)
            True
        '''
    def keys(self) -> list[str]:
        '''
        Return the list of the options in ``self``.

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     LocalOptions
            ....: )
            sage: o = LocalOptions(
            ....:     "Name Example",
            ....:     tikz_options=dict(
            ....:         default=\'toto\',
            ....:         values=dict(
            ....:             toto=\'name\',
            ....:             x="3"
            ....:         )
            ....:     ),
            ....:     display=dict(
            ....:         default=\'list\',
            ....:         values=dict(
            ....:             list="list representation",
            ....:             diagram="diagram representation"
            ....:         )
            ....:     )
            ....: )
            sage: keys=o.keys()
            sage: keys.sort()
            sage: keys
            [\'display\', \'tikz_options\']
        '''

default_tikz_options: Incomplete
ParallelogramPolyominoesOptions: Incomplete

class _drawing_tool:
    """
    Technical class to produce TIKZ drawing.

    This class contains some 2D geometric tools to produce some TIKZ
    drawings.

    With that classes you can use options to set up drawing informations.
    Then the class will produce a drawing by using those informations.

    EXAMPLES::

        sage: from sage.combinat.parallelogram_polyomino import (
        ....:     _drawing_tool, default_tikz_options,
        ....:     ParallelogramPolyominoesOptions
        ....: )
        sage: opt = ParallelogramPolyominoesOptions['tikz_options']
        sage: dt = _drawing_tool(opt)
        sage: dt.draw_line([1, 1], [-1, -1])
        '\\n  \\\\draw[color=black, line width=1] (1.000000, 1.000000) --
        (-1.000000, -1.000000);'

        sage: fct = lambda vec: [2*vec[0], vec[1]]
        sage: dt = _drawing_tool(opt, fct)
        sage: dt.draw_line([1, 1], [-1, -1])
        '\\n  \\\\draw[color=black, line width=1] (2.000000, 1.000000) --
        (-2.000000, -1.000000);'

        sage: import copy
        sage: opt = copy.deepcopy(opt)
        sage: opt['mirror'] = [0,1]
        sage: dt = _drawing_tool(opt)
        sage: dt.draw_line([1, 1], [-1, -1])
        '\\n  \\\\draw[color=black, line width=1] (-1.000000, 1.000000) --
        (1.000000, -1.000000);'
    """
    def __init__(self, options, XY=...) -> None:
        """
        Construct a drawing tools to produce some TIKZ drawing.

        INPUT:

        - ``options`` -- drawing options

        - ``XY`` -- a user function to convert vector in other vector
          (default: identity function)

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     _drawing_tool, default_tikz_options,
            ....:     ParallelogramPolyominoesOptions
            ....: )
            sage: opt = ParallelogramPolyominoesOptions['tikz_options']
            sage: dt = _drawing_tool(opt)
            sage: dt.draw_line([1, 1], [-1, -1])
            '\\n  \\\\draw[color=black, line width=1] (1.000000, 1.000000) --
            (-1.000000, -1.000000);'
        """
    def XY(self, v):
        """
        This function give the image of v by some transformation given by the
        drawing option of ``_drawing_tool``.

        The transformation is the composition of rotation, mirror, translation
        and XY user function.

        First we apply XY function, then the translation, then the mirror and
        finally the rotation.

        INPUT:

        - ``v`` -- the vector to transform

        OUTPUT: list of 2 floats encoding a vector

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     _drawing_tool, ParallelogramPolyominoesOptions
            ....: )
            sage: opt = ParallelogramPolyominoesOptions['tikz_options']
            sage: dt = _drawing_tool(opt)
            sage: dt.XY([1, 1])
            [1.0, 1.0]

            sage: fct = lambda vec: [2*vec[0], vec[1]]
            sage: dt = _drawing_tool(opt, fct)
            sage: dt.XY([1, 1])
            [2.0, 1.0]

            sage: import copy
            sage: opt = copy.deepcopy(opt)
            sage: opt['mirror'] = [0, 1]
            sage: dt = _drawing_tool(opt)
            sage: dt.XY([1, 1])
            [-1.0, 1.0]
        """
    def draw_line(self, v1, v2, color=None, size=None):
        """
        Return the TIKZ code for a line.

        INPUT:

        - ``v1`` -- point, The first point of the line

        - ``v2`` -- point, The second point of the line

        - ``color`` -- string (default: ``None``); the color of the line.
          If set to ``None``, the color is chosen according the
          drawing option given by ``_drawing_tool``.

        - ``size`` -- integer (default: ``None``); the size of the line.
          If set to ``None``, the size is chosen according the
          drawing option given by ``_drawing_tool``.

        OUTPUT: the code of a line in TIKZ

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     _drawing_tool, ParallelogramPolyominoesOptions
            ....: )
            sage: opt = ParallelogramPolyominoesOptions['tikz_options']
            sage: dt = _drawing_tool(opt)
            sage: dt.draw_line([1, 1], [-1, -1])
            '\\n  \\\\draw[color=black, line width=1] (1.000000, 1.000000) --
            (-1.000000, -1.000000);'
        """
    def draw_polyline(self, list_of_vertices, color=None, size=None):
        """
        Return the TIKZ code for a polyline.

        INPUT:

        - ``list_of_vertices`` -- list of points

        - ``color`` -- string (default: ``None``); the color of the line.
          If set to ``None``, the color is chosen according the
          drawing option given by ``_drawing_tool``.

        - ``size`` -- integer (default: ``None``); the size of the line.
          If set to ``None``, the size is chosen according the
          drawing option given by ``_drawing_tool``.

        OUTPUT: the code of a polyline in TIKZ

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     _drawing_tool, ParallelogramPolyominoesOptions
            ....: )
            sage: opt = ParallelogramPolyominoesOptions['tikz_options']
            sage: dt = _drawing_tool(opt)
            sage: dt.draw_polyline([[1, 1], [-1, -1], [0,0]])
            '\\n  \\\\draw[color=black, line width=1] (1.000000, 1.000000) --
            (-1.000000, -1.000000);\\n  \\\\draw[color=black, line width=1]
            (-1.000000, -1.000000) -- (0.000000, 0.000000);'
        """
    def draw_point(self, p1, color=None, size=None):
        """
        Return the TIKZ code for a point.

        INPUT:

        - ``p1`` -- a point

        - ``color`` -- string (default: ``None``); the color of the line.
          If set to ``None``, the color is chosen according the
          drawing option given by ``_drawing_tool``.

        - ``size`` -- integer (default: ``None``); the size of the line.
          If set to ``None``, the size is chosen according the
          drawing option given by ``_drawing_tool``.

        OUTPUT: the code of a point in TIKZ

        EXAMPLES::

            sage: from sage.combinat.parallelogram_polyomino import (
            ....:     _drawing_tool, ParallelogramPolyominoesOptions
            ....: )
            sage: opt = ParallelogramPolyominoesOptions['tikz_options']
            sage: dt = _drawing_tool(opt)
            sage: dt.draw_point([1, 1])
            '\\n  \\\\filldraw[color=black] (1.000000, 1.000000) circle (3.5pt);'
        """

class ParallelogramPolyomino(ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    Parallelogram Polyominoes.

    A parallelogram polyomino is a finite connected union of cells
    whose boundary can be decomposed in two paths, the upper and the lower
    paths, which are comprised of north and east unit steps and meet only at
    their starting and final points.

    Parallelogram Polyominoes can be defined with those two paths.

    EXAMPLES::

        sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
        sage: pp
        [[0, 1], [1, 0]]
    """
    @staticmethod
    def __classcall_private__(cls, *args, **opts):
        '''
        Ensure that parallelogram polyominoes created by the enumerated sets
        are instances of :class:`ParallelogramPolyomino` and have the same
        parent.

        TESTS::

            sage: issubclass(
            ....:     ParallelogramPolyominoes().element_class,
            ....:     ParallelogramPolyomino
            ....: )
            True
            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.parent()
            Parallelogram polyominoes
            sage: str(type(pp)) == (
            ....:      "<class \'sage.combinat.parallelogram_polyomino" +
            ....:      ".ParallelogramPolyominoes_all_with_category" +
            ....:      ".element_class\'>"
            ....: )
            True

            sage: pp1 = ParallelogramPolyominoes()([[0, 1], [1, 0]])
            sage: pp1.parent() is pp.parent()
            True
            sage: type(pp1) is type(pp)
            True

            sage: pp1 = ParallelogramPolyominoes(2)([[0, 1], [1, 0]])
            sage: pp1.parent() is pp.parent()
            True
            sage: type(pp1) is type(pp)
            True
        '''
    def check(self) -> None:
        """
        This method raises an error if the internal data of the class does not
        represent a parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp = ParallelogramPolyomino([[1], [1]])

            sage: pp = ParallelogramPolyomino(                # indirect doctest
            ....:     [[1, 0], [0, 1]]
            ....: )
            Traceback (most recent call last):
            ...
            ValueError: the lower and upper paths are crossing

            sage: pp = ParallelogramPolyomino([[1], [0, 1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the lower and upper paths have different sizes (2 != 1)

            sage: pp = ParallelogramPolyomino([[1], [0]])     # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the two paths have distinct ends

            sage: pp = ParallelogramPolyomino([[0], [1]])     # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the two paths have distinct ends

            sage: pp = ParallelogramPolyomino([[0], [0]])     # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the lower or the upper path can...t be equal to [0]

            sage: pp = ParallelogramPolyomino([[], [0]])      # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the lower or the upper path can...t be equal to []

            sage: pp = ParallelogramPolyomino([[0], []])      # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the lower or the upper path can...t be equal to []

            sage: pp = ParallelogramPolyomino([[], []])       # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the lower or the upper path can...t be equal to []
        """
    def __hash__(self):
        """
        Return the hash code of the parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: hash(pp) == hash((
            ....:     (0, 0, 0, 1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 0, 0, 1, 0, 0)
            ....: ))
            True

            sage: PPS = ParallelogramPolyominoes(8)
            sage: D = { PPS[0]: True, PPS[1]: True }
            sage: D[PPS[0]] = False
            sage: import pprint
            sage: pp = pprint.PrettyPrinter()
            sage: pp.pprint(D)
            {[[0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0]]: False,
             [[0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0]]: True}
        """
    def __copy__(self):
        """
        Copy a parallelogram Polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp1 = copy(pp)
            sage: pp1 is pp
            False
            sage: pp1 == pp
            True
            sage: pp1
            [[0, 0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 1, 0, 0]]
        """
    def __init__(self, parent, value, check: bool = True) -> None:
        """
        Construct a parallelogram polyomino.

        The input is a pair of lower path and upper path.

        The lower and upper paths of the empty parallelogram polyomino are
        [1] and [1].

        EXAMPLES::

            sage: lower_path = [0, 0, 1, 0, 1, 1]
            sage: upper_path = [1, 1, 0, 1, 0, 0]
            sage: pp = ParallelogramPolyomino([lower_path, upper_path])
            sage: pp
            [[0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0]]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp
            [[0, 1], [1, 0]]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp
            [[1], [1]]
        """
    def reflect(self) -> ParallelogramPolyomino:
        """
        Return the parallelogram polyomino obtained by switching rows and
        columns.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0,0,0,0,1,1,0,1,0,1], [1,0,1,0,0,1,1,0,0,0]])
            sage: pp.heights(), pp.upper_heights()
            ([4, 3, 2, 3], [0, 1, 3, 3])
            sage: pp = pp.reflect()
            sage: pp.widths(), pp.lower_widths()
            ([4, 3, 2, 3], [0, 1, 3, 3])

            sage: pp = ParallelogramPolyomino([[0,0,0,1,1], [1,0,0,1,0]])
            sage: ascii_art(pp)
            *
            *
            **
            sage: ascii_art(pp.reflect())
            ***
              *

        TESTS::

           sage: pp = ParallelogramPolyomino([[1], [1]])
           sage: pp.reflect()
           [[1], [1]]
        """
    def rotate(self) -> ParallelogramPolyomino:
        """
        Return the parallelogram polyomino obtained by rotation of 180 degrees.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0,0,0,1,1], [1,0,0,1,0]])
            sage: ascii_art(pp)
            *
            *
            **
            sage: ascii_art(pp.rotate())
            **
             *
             *
        """
    def to_dyck_word(self, bijection=None):
        """
        Convert to a Dyck word.

        INPUT:

        - ``bijection`` -- string or ``None`` (default: ``None``); the name of
          the bijection. If it is set to ``None`` then the ``'Delest-Viennot'``
          bijection is used.
          Expected values are ``None``, ``'Delest-Viennot'``, or ``'Delest-Viennot-beta'``.

        OUTPUT: a Dyck word

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0]])
            sage: pp.to_dyck_word()
            [1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
            sage: pp.to_dyck_word(bijection='Delest-Viennot')
            [1, 1, 0, 1, 1, 0, 1, 0, 0, 0]

            sage: pp.to_dyck_word(bijection='Delest-Viennot-beta')
            [1, 0, 1, 1, 1, 0, 1, 0, 0, 0]
        """
    @staticmethod
    def from_dyck_word(dyck, bijection=None):
        """
        Convert a Dyck word to parallelogram polyomino.

        INPUT:

        - ``dyck`` -- a Dyck word

        - ``bijection`` -- string or ``None`` (default: ``None``); the
          bijection to use. See :meth:`to_dyck_word` for more details.

        OUTPUT: a parallelogram polyomino

        EXAMPLES::

            sage: dyck = DyckWord([1, 1, 0, 1, 1, 0, 1, 0, 0, 0])
            sage: ParallelogramPolyomino.from_dyck_word(dyck)
            [[0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0]]
            sage: ParallelogramPolyomino.from_dyck_word(dyck, bijection='Delest-Viennot')
            [[0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0]]
            sage: ParallelogramPolyomino.from_dyck_word(dyck, bijection='Delest-Viennot-beta')
            [[0, 0, 1, 0, 1, 1], [1, 1, 1, 0, 0, 0]]
        """
    def to_binary_tree(self, bijection=None):
        """
        Convert to a binary tree.

        INPUT:

        - ``bijection`` -- string or ``None`` (default: ``None``); the name of
          bijection to use for the conversion. The possible values are ``None``
          or ``'Aval-Boussicault'``. The ``None`` value is equivalent to
          ``'Aval-Boussicault'``.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
            ....:     ]
            ....: )
            sage: pp.to_binary_tree()
            [[., [[., .], [[., [., .]], .]]], [[., .], .]]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.to_binary_tree()
            [., .]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.to_binary_tree()
            .
        """
    def to_ordered_tree(self, bijection=None):
        """
        Return an ordered tree from the parallelogram polyomino.

        Different bijections can be specified.

        The bijection 'via dyck and Delest-Viennot' is the composition of
        :meth:`_to_dyck_delest_viennot` and the classical bijection between
        dyck paths and ordered trees.

        The bijection between Dyck Word and ordered trees is described
        in [DerZak1980]_ (See page 12 and 13 and Figure 3.1).

        The bijection 'Boussicault-Socci' is described in [BRS2015]_.

        INPUT:

        - ``bijection`` -- string or ``None`` (default: ``None``); the name of
          bijection to use for the conversion. The possible value are ``None``,
          ``'Boussicault-Socci'`` or ``'via dyck and Delest-Viennot'``.
          The ``None`` value is equivalent to the ``'Boussicault-Socci'``
          value.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
            ....:     ]
            ....: )
            sage: pp.to_ordered_tree()
            [[[[[]], [[[]]]]], [[]]]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.to_ordered_tree()
            [[]]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.to_ordered_tree()
            []

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
            ....:     ]
            ....: )
            sage: pp.to_ordered_tree('via dyck and Delest-Viennot')
            [[[[]], [[[]], []]], [[]]]
        """
    def get_options(self):
        """
        Return all the options of the object.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.get_options()
            Current options for ParallelogramPolyominoes_size
              - display:            'list'
              - drawing_components: {'bounce_0': False,
             'bounce_1': False,
             'bounce_values': False,
             'diagram': True,
             'tree': False}
              - latex:              'drawing'
              - tikz_options:       {'color_bounce_0': 'red',
             'color_bounce_1': 'blue',
             'color_line': 'black',
             'color_point': 'black',
             'line_size': 1,
             'mirror': None,
             'point_size': 3.5,
             'rotation': 0,
             'scale': 1,
             'translation': [0, 0]}
        """
    def set_options(self, *get_value, **set_value) -> None:
        """
        Set new options to the object.
        See :class:`LocalOptions` for more info.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
            ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
            ....:     ]
            ....: )
            sage: pp
            [[0, 0, 0, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1, 0, 0, 0]]
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 0 0]
            [1 0 0]
            [1 0 0]
            [1 1 1]
            [0 1 1]
            [0 0 1]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: view(PP) # not tested
            sage: pp.set_options(
            ....:     drawing_components=dict(
            ....:         diagram = True,
            ....:         bounce_0 = True,
            ....:         bounce_1 = True,
            ....:     )
            ....: )
            sage: view(PP) # not tested
        """
    def upper_path(self) -> list:
        """
        Get the upper path of the parallelogram polyomino.

        EXAMPLES::

            sage: lower_path = [0, 0, 1, 0, 1, 1]
            sage: upper_path = [1, 1, 0, 1, 0, 0]
            sage: pp = ParallelogramPolyomino([lower_path, upper_path])
            sage: pp.upper_path()
            [1, 1, 0, 1, 0, 0]
        """
    def lower_path(self) -> list:
        """
        Get the lower path of the parallelogram polyomino.

        EXAMPLES::

            sage: lower_path = [0, 0, 1, 0, 1, 1]
            sage: upper_path = [1, 1, 0, 1, 0, 0]
            sage: pp = ParallelogramPolyomino([lower_path, upper_path])
            sage: pp.lower_path()
            [0, 0, 1, 0, 1, 1]
        """
    def upper_heights(self):
        """
        Return the list of heights associated to each vertical step of the
        parallelogram polyomino's upper path.

        OUTPUT: list of integers

        EXAMPLES::

            sage: ParallelogramPolyomino([[0, 1], [1, 0]]).upper_heights()
            [0]
            sage: ParallelogramPolyomino(
            ....:     [[0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 0]]
            ....: ).upper_heights()
            [0, 1, 1, 2, 2]
        """
    def lower_heights(self):
        """
        Return the list of heights associated to each vertical step of the
        parallelogram polyomino's lower path.

        OUTPUT: list of integers

        EXAMPLES::

            sage: ParallelogramPolyomino([[0, 1], [1, 0]]).lower_heights()
            [1]
            sage: ParallelogramPolyomino(
            ....:     [[0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 0]]
            ....: ).lower_heights()
            [2, 2, 3, 3, 3]
        """
    def upper_widths(self):
        """
        Return the list of widths associated to each horizontal step of the
        parallelogram polyomino's upper path.

        OUTPUT: list of integers

        EXAMPLES::

            sage: ParallelogramPolyomino([[0, 1], [1, 0]]).upper_widths()
            [1]
            sage: ParallelogramPolyomino(
            ....:     [[0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 0]]
            ....: ).upper_widths()
            [1, 3, 5]
        """
    def lower_widths(self):
        """
        Return the list of widths associated to each horizontal step of the
        parallelogram polyomino's lower path.

        OUTPUT: list of integers

        EXAMPLES::

            sage: ParallelogramPolyomino([[0, 1], [1, 0]]).lower_widths()
            [0]
            sage: ParallelogramPolyomino(
            ....:     [[0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 0]]
            ....: ).lower_widths()
            [0, 0, 2]
        """
    def widths(self) -> list:
        """
        Return a list of the widths of the parallelogram polyomino.

        Namely, the parallelogram polyomino is split row by row and the
        method returns the list containing the sizes of the rows.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.widths()
            [1, 3, 3, 3, 2]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.widths()
            [1]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.widths()
            []
        """
    def degree_convexity(self) -> int:
        """
        Return the degree convexity of a parallelogram polyomino.

        A convex polyomino is said to be k-convex if every pair of its cells
        can be connected by a monotone path (path with south and east steps)
        with at most k changes of direction.
        The degree of convexity of a convex polyomino P is the smallest integer
        k such that P is k-convex.

        If the parallelogram polyomino is empty, the function return -1.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.degree_convexity()
            3

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.degree_convexity()
            0

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.degree_convexity()
            -1
        """
    def is_flat(self) -> bool:
        """
        Return whether the two bounce paths join together in the rightmost cell
        of the bottom row of P.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.is_flat()
            False

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.is_flat()
            True

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.is_flat()
            True
        """
    def is_k_directed(self, k) -> bool:
        """
        Return whether the Polyomino Parallelogram is k-directed.

        A convex polyomino is said to be k-convex if every pair of its cells
        can be connected by a monotone path (path with south and east steps)
        with at most k changes of direction.

        The degree of convexity of a convex polyomino P is the smallest integer
        k such that P is k-convex.

        INPUT:

        - ``k`` -- nonnegative integer

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.is_k_directed(3)
            True
            sage: pp.is_k_directed(4)
            True
            sage: pp.is_k_directed(5)
            True
            sage: pp.is_k_directed(0)
            False
            sage: pp.is_k_directed(1)
            False
            sage: pp.is_k_directed(2)
            False

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.is_k_directed(0)
            True
            sage: pp.is_k_directed(1)
            True

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.is_k_directed(0)
            True
            sage: pp.is_k_directed(1)
            True
        """
    def heights(self) -> list:
        """
        Return a list of heights of the parallelogram polyomino.

        Namely, the parallelogram polyomino is split column by column and
        the method returns the list containing the sizes of the columns.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 1, 0, 1, 0, 1, 1],
            ....:         [1, 0, 1, 1, 0, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.heights()
            [3, 3, 4, 2]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.heights()
            [1]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.heights()
            [0]
        """
    def width(self):
        """
        Return the width of the parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
            ....:         [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
            ....:     ]
            ....: )
            sage: pp.width()
            6

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.width()
            1

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.width()
            1
        """
    def height(self):
        """
        Return the height of the parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
            ....:         [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
            ....:     ]
            ....: )
            sage: pp.height()
            4

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.height()
            1

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.height()
            0
        """
    def cell_is_inside(self, w, h):
        """
        Determine whether the cell at a given position
        is inside the parallelogram polyomino.

        INPUT:

        - ``w`` -- the x coordinate of the box position

        - ``h`` -- the y coordinate of the box position

        OUTPUT:

        Return 0 if there is no cell at the given position,
        return 1 if there is a cell.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
            ....:         [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
            ....:     ]
            ....: )
            sage: pp.cell_is_inside(0, 0)
            1
            sage: pp.cell_is_inside(1, 0)
            1
            sage: pp.cell_is_inside(0, 1)
            0
            sage: pp.cell_is_inside(3, 0)
            0
            sage: pp.cell_is_inside(pp.width()-1,pp.height()-1)
            1
            sage: pp.cell_is_inside(pp.width(),pp.height()-1)
            0
            sage: pp.cell_is_inside(pp.width()-1,pp.height())
            0
        """
    @cached_method
    def get_array(self):
        """
        Return an array of 0s and 1s such that the 1s represent the boxes of
        the parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
            ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
            ....:     ]
            ....: )
            sage: matrix(pp.get_array())
            [1 0 0]
            [1 0 0]
            [1 0 0]
            [1 1 1]
            [0 1 1]
            [0 0 1]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.get_array()
            [[1]]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.get_array()
            []
        """
    class _polyomino_row:
        """
        This is an internal class representing a single row of
        a parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
            ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
            ....:     ]
            ....: )
            sage: row = ParallelogramPolyomino._polyomino_row(pp, 4)
            sage: row
            [0, 1, 1]
        """
        polyomino: Incomplete
        row: Incomplete
        def __init__(self, polyomino, row) -> None:
            """
            The constructor of the class.

            EXAMPLES::

                sage: pp = ParallelogramPolyomino(
                ....:     [
                ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
                ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
                ....:     ]
                ....: )
                sage: row = ParallelogramPolyomino._polyomino_row(pp, 4)
            """
        def __getitem__(self, column):
            """
            Return 0 or 1 if the is a cell inside the specific column inside the
            row.

            EXAMPLES::

                sage: pp = ParallelogramPolyomino(
                ....:     [
                ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
                ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
                ....:     ]
                ....: )
                sage: matrix(pp.get_array())
                [1 0 0]
                [1 0 0]
                [1 0 0]
                [1 1 1]
                [0 1 1]
                [0 0 1]

                sage: row = ParallelogramPolyomino._polyomino_row(pp, 4)
                sage: [row[-1], row[0], row[1], row[2], row[3]]
                [0, 0, 1, 1, 0]
            """
        def is_inside(self) -> bool:
            """
            Return ``True`` if the row is inside the parallelogram polyomino,
            return ``False`` otherwise.

            EXAMPLES::

                sage: PP = ParallelogramPolyomino
                sage: pp = PP(
                ....:     [
                ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
                ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
                ....:     ]
                ....: )
                sage: matrix(pp.get_array())
                [1 0 0]
                [1 0 0]
                [1 0 0]
                [1 1 1]
                [0 1 1]
                [0 0 1]

                sage: [
                ....:     PP._polyomino_row(pp, i).is_inside()
                ....:     for i in [-1,0,3,5,6]
                ....: ]
                [False, True, True, True, False]
            """
        def is_outside(self) -> bool:
            """
            Return ``True`` if the row is outside the parallelogram polyomino,
            return ``False`` otherwise.

            EXAMPLES::

                sage: PP = ParallelogramPolyomino
                sage: pp = PP(
                ....:     [
                ....:         [0, 0, 0, 0, 1, 0, 1, 0, 1],
                ....:         [1, 0, 0, 0, 1, 1, 0, 0, 0]
                ....:     ]
                ....: )
                sage: matrix(pp.get_array())
                [1 0 0]
                [1 0 0]
                [1 0 0]
                [1 1 1]
                [0 1 1]
                [0 0 1]

                sage: [
                ....:     PP._polyomino_row(pp, i).is_outside()
                ....:     for i in [-1,0,3,5,6]
                ....: ]
                [True, False, False, False, True]
            """
    def __getitem__(self, row):
        """
        Return the row of the parallelogram polyomino.

        The index of the row can be out of range of the height of
        the parallelogram polyomino.
        In that case, the row returned is outside the parallelogram
        polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0]]
            ....: )
            sage: pp[0].is_inside()
            True
            sage: pp[3].is_outside()
            True
            sage: pp[-1].is_outside()
            True
            sage: pp[0][0]
            1
            sage: pp[[0, 1]]
            1
            sage: pp[2][0]
            0
            sage: pp[-1][0]
            0
            sage: pp[[4, 4]]
            0
        """
    def bounce_path(self, direction: int = 1):
        """
        Return the bounce path of the parallelogram polyomino.

        The bounce path is a path with two steps (1, 0) and (0, 1).

        If 'direction' is 1 (resp. 0), the bounce path is the path
        starting at position (h=1, w=0) (resp. (h=0, w=1)) with
        initial direction, the vector (0, 1) (resp. (1, 0)), and turning
        each time the path crosses the perimeter of the parallelogram
        polyomino.

        The path is coded by a list of integers. Each integer represents
        the size of the path between two turnings.

        You can visualize the two bounce paths by using the following
        commands.

        INPUT:

        - ``direction`` -- the initial direction of the bounce path (see above
          for the definition)

        EXAMPLES::

            sage: PP = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0]]
            ....: )
            sage: PP.bounce_path(direction=1)
            [2, 2, 1]
            sage: PP.bounce_path(direction=0)
            [2, 1, 1, 1]

            sage: PP = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 1, 1, 0, 0, 1, 1],
            ....:         [1, 1, 1, 0, 1, 1, 0, 0, 0]
            ....:     ]
            ....: )
            sage: PP.bounce_path(direction=1)
            [3, 1, 2, 2]
            sage: PP.bounce_path(direction=0)
            [2, 4, 2]

            sage: PP = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0]]
            ....: )
            sage: PP.set_options(
            ....:     drawing_components=dict(
            ....:         diagram = True
            ....:         , bounce_0 = True
            ....:         , bounce_1 = True
            ....:     )
            ....: )
            sage: view(PP) # not tested

            sage: PP = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: PP.bounce_path(direction=1)
            [1]
            sage: PP.bounce_path(direction=0)
            [1]

            sage: PP = ParallelogramPolyomino([[1], [1]])
            sage: PP.bounce_path(direction=1)
            []
            sage: PP.bounce_path(direction=0)
            []

        TESTS::

            sage: PP = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0]]
            ....: )
            sage: PP.bounce_path(direction=1)
            [2, 2, 1]
            sage: PP.bounce_path(direction=0)
            [2, 1, 1, 1]
        """
    def bounce(self, direction: int = 1):
        """
        Return the bounce of the parallelogram polyomino.

        Let ``p`` be the bounce path of the parallelogram
        polyomino (:meth:`bounce_path`). The bounce is defined by:

            ``sum([(1+ floor(i/2))*p[i] for i in range(len(p))])``

        INPUT:

        - ``direction`` -- the initial direction of the bounce path
          (see :meth:`bounce_path` for the definition)

        EXAMPLES::

            sage: PP = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0]]
            ....: )
            sage: PP.bounce(direction=1)
            6
            sage: PP.bounce(direction=0)
            7

            sage: PP = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 1, 1, 0, 0, 1, 1],
            ....:         [1, 1, 1, 0, 1, 1, 0, 0, 0]
            ....:     ]
            ....: )
            sage: PP.bounce(direction=1)
            12
            sage: PP.bounce(direction=0)
            10

            sage: PP = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: PP.bounce(direction=1)
            1
            sage: PP.bounce(direction=0)
            1

            sage: PP = ParallelogramPolyomino([[1], [1]])
            sage: PP.bounce(direction=1)
            0
            sage: PP.bounce(direction=0)
            0
        """
    def area(self):
        """
        Return the area of the parallelogram polyomino. The area of a
        parallelogram polyomino is the number of cells of the parallelogram
        polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [
            ....:         [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
            ....:         [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
            ....:     ]
            ....: )
            sage: pp.area()
            13

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.area()
            1

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.area()
            0
        """
    def get_tikz_options(self):
        """
        Return all the tikz options permitting to draw the parallelogram
        polyomino.

        See :class:`LocalOption` to have more informations about the
        modification of those options.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.get_tikz_options()
            {'color_bounce_0': 'red',
             'color_bounce_1': 'blue',
             'color_line': 'black',
             'color_point': 'black',
             'line_size': 1,
             'mirror': None,
             'point_size': 3.5,
             'rotation': 0,
             'scale': 1,
             'translation': [0, 0]}
        """
    def get_node_position_from_box(self, box_position, direction, nb_crossed_nodes=None):
        """
        This function starts from a cell inside a parallelogram polyomino and
        a direction.

        If ``direction`` is equal to 0, the function selects the column
        associated with the y-coordinate of ``box_position`` and then returns
        the topmost cell of the column that is on the top of ``box_position``
        (the cell of ``box_position`` is included).

        If ``direction`` is equal to 1, the function selects the row
        associated with the x-coordinate of ``box_position`` and then returns
        the leftmost cell of the row that is on the left of ``box_position``.
        (the cell of ``box_position`` is included).

        This function updates the entry of ``nb_crossed_nodes``. The function
        increases the entry of ``nb_crossed_nodes`` by the number of boxes that
        is a node (see ``box_is_node``) located on the top if ``direction``
        is 0 (resp. on the left if ``direction`` is 1) of ``box_position``
        (cell at ``box_position`` is excluded).

        INPUT:

        - ``box_position`` -- the position of the starting cell

        - ``direction`` -- the direction (0 or 1)

        - ``nb_crossed_nodes`` -- ``[0]`` (default) a list containing just one
          integer

        OUTPUT: a [row,column] position of the cell

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0]]
            ....: )
            sage: matrix(pp.get_array())
            [1 0 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: l = [0]
            sage: pp.get_node_position_from_box([3, 2], 0, l)
            [1, 2]
            sage: l
            [1]
            sage: l = [0]
            sage: pp.get_node_position_from_box([3, 2], 1, l)
            [3, 1]
            sage: l
            [1]
            sage: l = [0]
            sage: pp.get_node_position_from_box([1, 2], 0, l)
            [1, 2]
            sage: l
            [0]
            sage: l = [0]
            sage: pp.get_node_position_from_box([1, 2], 1, l)
            [1, 0]
            sage: l
            [2]
            sage: l = [0]
            sage: pp.get_node_position_from_box([3, 1], 0, l)
            [1, 1]
            sage: l
            [2]
            sage: l = [0]
            sage: pp.get_node_position_from_box([3, 1], 1, l)
            [3, 1]
            sage: l
            [0]
        """
    def box_is_node(self, pos) -> bool:
        """
        Return ``True`` if the box contains a node in the context of the
        Aval-Boussicault bijection between parallelogram polyomino and binary
        tree.

        A box is a node if there is no cell on the top of the box in the
        same column or on the left of the box.in the same row.

        INPUT:

        - ``pos`` -- the [x,y] coordinate of the box

        OUTPUT: boolean

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 1 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: pp.box_is_node([2,1])
            True
            sage: pp.box_is_node([2,0])
            False
            sage: pp.box_is_node([1,1])
            False
        """
    def box_is_root(self, box) -> bool:
        """
        Return ``True`` if the box contains the root of the tree : it
        is the top-left box of the parallelogram polyomino.

        INPUT:

        - ``box`` -- the x,y coordinate of the cell

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.box_is_root([0, 0])
            True
            sage: pp.box_is_root([0, 1])
            False
        """
    def get_BS_nodes(self):
        """
        Return the list of cells containing node of the left and right planar
        tree in the Boussicault-Socci bijection.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 1 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: sorted(pp.get_BS_nodes())
            [[0, 1], [1, 0], [1, 2], [2, 1], [3, 1], [4, 1]]

        You can draw the point inside the parallelogram polyomino by typing
        (the left nodes are in blue, and the right node are in red) ::

            sage: pp.set_options(drawing_components=dict(tree=True))
            sage: view(pp) # not tested
        """
    def get_right_BS_nodes(self):
        """
        Return the list of cells containing node of the right planar tree in
        the Boussicault-Socci bijection between parallelogram polyominoes
        and pair of ordered trees.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 1 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: sorted(pp.get_right_BS_nodes())
            [[1, 0], [1, 2]]

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 0 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: sorted(pp.get_right_BS_nodes())
            [[1, 0], [1, 1], [1, 2], [2, 1], [3, 1], [4, 1]]

        You can draw the point inside the parallelogram polyomino by typing,
        (the left nodes are in blue, and the right node are in red) ::

            sage: pp.set_options(drawing_components=dict(tree=True))
            sage: view(pp) # not tested
        """
    def get_left_BS_nodes(self):
        """
        Return the list of cells containing node of the left planar tree in
        the Boussicault-Socci bijection between parallelogram polyominoes
        and pair of ordered trees.

        OUTPUT: list of [row,column] position of cells

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 1 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: sorted(pp.get_left_BS_nodes())
            [[0, 1], [2, 1], [3, 1], [4, 1]]

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0]]
            ....: )
            sage: pp.set_options(display='drawing')
            sage: pp
            [1 0 0]
            [1 1 1]
            [0 1 1]
            [0 1 1]
            [0 1 1]
            sage: sorted(pp.get_left_BS_nodes())
            []

        You can draw the point inside the parallelogram polyomino by typing
        (the left nodes are in blue, and the right node are in red) ::

            sage: pp.set_options(drawing_components=dict(tree=True))
            sage: view(pp) # not tested
        """
    def to_tikz(self):
        """
        Return the tikz code of the parallelogram polyomino.

        This code is the code present inside a tikz latex environment.

        We can modify the output with the options.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0,0,0,1,1,0,1,0,0,1,1,1],[1,1,1,0,0,1,1,0,0,1,0,0]]
            ....: )
            sage: print(pp.to_tikz())
            <BLANKLINE>
              \\draw[color=black, line width=1] (0.000000, 6.000000) --
            (0.000000, 3.000000);
              \\draw[color=black, line width=1] (6.000000, 2.000000) --
            (6.000000, 0.000000);
              \\draw[color=black, line width=1] (0.000000, 6.000000) --
            (3.000000, 6.000000);
              \\draw[color=black, line width=1] (3.000000, 0.000000) --
            (6.000000, 0.000000);
              \\draw[color=black, line width=1] (1.000000, 6.000000) --
            (1.000000, 3.000000);
              \\draw[color=black, line width=1] (2.000000, 6.000000) --
            (2.000000, 2.000000);
              \\draw[color=black, line width=1] (3.000000, 6.000000) --
            (3.000000, 0.000000);
              \\draw[color=black, line width=1] (4.000000, 4.000000) --
            (4.000000, 0.000000);
              \\draw[color=black, line width=1] (5.000000, 4.000000) --
            (5.000000, 0.000000);
              \\draw[color=black, line width=1] (0.000000, 5.000000) --
            (3.000000, 5.000000);
              \\draw[color=black, line width=1] (0.000000, 4.000000) --
            (5.000000, 4.000000);
              \\draw[color=black, line width=1] (0.000000, 3.000000) --
            (5.000000, 3.000000);
              \\draw[color=black, line width=1] (2.000000, 2.000000) --
            (6.000000, 2.000000);
              \\draw[color=black, line width=1] (3.000000, 1.000000) --
            (6.000000, 1.000000);
            sage: pp.set_options(
            ....:     drawing_components=dict(
            ....:         diagram=True,
            ....:         tree=True,
            ....:         bounce_0=True,
            ....:         bounce_1=True
            ....:     )
            ....: )
            sage: print(pp.to_tikz())
            <BLANKLINE>
              \\draw[color=black, line width=1] (0.000000, 6.000000) --
            (0.000000, 3.000000);
              \\draw[color=black, line width=1] (6.000000, 2.000000) --
            (6.000000, 0.000000);
              \\draw[color=black, line width=1] (0.000000, 6.000000) --
            (3.000000, 6.000000);
              \\draw[color=black, line width=1] (3.000000, 0.000000) --
            (6.000000, 0.000000);
              \\draw[color=black, line width=1] (1.000000, 6.000000) --
            (1.000000, 3.000000);
              \\draw[color=black, line width=1] (2.000000, 6.000000) --
            (2.000000, 2.000000);
              \\draw[color=black, line width=1] (3.000000, 6.000000) --
            (3.000000, 0.000000);
              \\draw[color=black, line width=1] (4.000000, 4.000000) --
            (4.000000, 0.000000);
              \\draw[color=black, line width=1] (5.000000, 4.000000) --
            (5.000000, 0.000000);
              \\draw[color=black, line width=1] (0.000000, 5.000000) --
            (3.000000, 5.000000);
              \\draw[color=black, line width=1] (0.000000, 4.000000) --
            (5.000000, 4.000000);
              \\draw[color=black, line width=1] (0.000000, 3.000000) --
            (5.000000, 3.000000);
              \\draw[color=black, line width=1] (2.000000, 2.000000) --
            (6.000000, 2.000000);
              \\draw[color=black, line width=1] (3.000000, 1.000000) --
            (6.000000, 1.000000);
              \\draw[color=blue, line width=3] (0.000000, 5.000000) --
            (3.000000, 5.000000);
              \\draw[color=blue, line width=3] (3.000000, 5.000000) --
            (3.000000, 2.000000);
              \\draw[color=blue, line width=3] (3.000000, 2.000000) --
            (5.000000, 2.000000);
              \\draw[color=blue, line width=3] (5.000000, 2.000000) --
            (5.000000, 0.000000);
              \\draw[color=blue, line width=3] (5.000000, 0.000000) --
            (6.000000, 0.000000);
              \\draw[color=red, line width=2] (1.000000, 6.000000) --
            (1.000000, 3.000000);
              \\draw[color=red, line width=2] (1.000000, 3.000000) --
            (5.000000, 3.000000);
              \\draw[color=red, line width=2] (5.000000, 3.000000) --
            (5.000000, 0.000000);
              \\draw[color=red, line width=2] (5.000000, 0.000000) --
            (6.000000, 0.000000);
              \\filldraw[color=black] (0.500000, 4.500000) circle (3.5pt);
              \\filldraw[color=black] (0.500000, 3.500000) circle (3.5pt);
              \\filldraw[color=black] (2.500000, 2.500000) circle (3.5pt);
              \\filldraw[color=black] (3.500000, 1.500000) circle (3.5pt);
              \\filldraw[color=black] (3.500000, 0.500000) circle (3.5pt);
              \\filldraw[color=black] (1.500000, 5.500000) circle (3.5pt);
              \\filldraw[color=black] (2.500000, 5.500000) circle (3.5pt);
              \\filldraw[color=black] (3.500000, 3.500000) circle (3.5pt);
              \\filldraw[color=black] (4.500000, 3.500000) circle (3.5pt);
              \\filldraw[color=black] (5.500000, 1.500000) circle (3.5pt);
              \\filldraw[color=black] (0.500000, 5.500000) circle (3.5pt);
        """
    def geometry(self) -> list:
        """
        Return a pair [h, w] containing the height and the width of the
        parallelogram polyomino.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
            ....: )
            sage: pp.geometry()
            [1, 4]

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.geometry()
            [1, 1]

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.geometry()
            [0, 1]
        """
    def plot(self):
        """
        Return a plot of ``self``.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino([[0,1],[1,0]])
            sage: pp.plot()                                                             # needs sage.plot
            Graphics object consisting of 4 graphics primitives
            sage: pp.set_options(
            ....:     drawing_components=dict(
            ....:         diagram=True,
            ....:         bounce_0=True,
            ....:         bounce_1=True,
            ....:         bounce_values=0,
            ....:     )
            ....: )
            sage: pp.plot()                                                             # needs sage.plot
            Graphics object consisting of 7 graphics primitives
        """
    def size(self) -> int:
        """
        Return the size of the parallelogram polyomino.

        The size of a parallelogram polyomino is its half-perimeter.

        EXAMPLES::

            sage: pp = ParallelogramPolyomino(
            ....:     [[0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 0, 0]]
            ....: )
            sage: pp.size()
            8

            sage: pp = ParallelogramPolyomino([[0, 1], [1, 0]])
            sage: pp.size()
            2

            sage: pp = ParallelogramPolyomino([[1], [1]])
            sage: pp.size()
            1
        """

class ParallelogramPolyominoesFactory(SetFactory):
    """
    The parallelogram polyominoes factory.

    EXAMPLES::

        sage: PPS = ParallelogramPolyominoes(size=4)
        sage: PPS
        Parallelogram polyominoes of size 4

        sage: sorted(PPS)
        [[[0, 0, 0, 1], [1, 0, 0, 0]],
         [[0, 0, 1, 1], [1, 0, 1, 0]],
         [[0, 0, 1, 1], [1, 1, 0, 0]],
         [[0, 1, 0, 1], [1, 1, 0, 0]],
         [[0, 1, 1, 1], [1, 1, 1, 0]]]

        sage: PPS = ParallelogramPolyominoes()
        sage: PPS
        Parallelogram polyominoes
        sage: PPS.cardinality()
        +Infinity
    """
    def __call__(self, size=None, policy=None):
        """
        Return a family of parallelogram polyominoes enumerated with the
        parameter constraints.

        INPUT:

        - ``size`` -- integer (default: ``None``); the size of the parallelogram
                      polyominoes contained in the family.
                      If set to ``None``, the family returned contains all
                      the parallelogram polyominoes.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes(size=4)
            sage: PPS
            Parallelogram polyominoes of size 4
            sage: sorted(PPS)
            [[[0, 0, 0, 1], [1, 0, 0, 0]],
             [[0, 0, 1, 1], [1, 0, 1, 0]],
             [[0, 0, 1, 1], [1, 1, 0, 0]],
             [[0, 1, 0, 1], [1, 1, 0, 0]],
             [[0, 1, 1, 1], [1, 1, 1, 0]]]

            sage: PPS = ParallelogramPolyominoes()
            sage: PPS
            Parallelogram polyominoes
            sage: PPS.cardinality()
            +Infinity

            sage: PPS = ParallelogramPolyominoes(size=None)
            sage: PPS
            Parallelogram polyominoes
            sage: PPS.cardinality()
            +Infinity
        """

ParallelogramPolyominoes: Incomplete

class ParallelogramPolyominoes_size(ParentWithSetFactory, UniqueRepresentation):
    """
    The parallelogram polyominoes of size `n`.

    EXAMPLES::

        sage: PPS = ParallelogramPolyominoes(4)
        sage: PPS
        Parallelogram polyominoes of size 4
        sage: sorted(PPS)
        [[[0, 0, 0, 1], [1, 0, 0, 0]],
         [[0, 0, 1, 1], [1, 0, 1, 0]],
         [[0, 0, 1, 1], [1, 1, 0, 0]],
         [[0, 1, 0, 1], [1, 1, 0, 0]],
         [[0, 1, 1, 1], [1, 1, 1, 0]]]
    """
    def __init__(self, size, policy) -> None:
        """
        Construct a set of Parallelogram Polyominoes of a given size.

        EXAMPLES::

            sage: ParallelogramPolyominoes(4)
            Parallelogram polyominoes of size 4
        """
    def check_element(self, el, check) -> None:
        """
        Check is a given element `el` is in the set of parallelogram
        polyominoes of a fixed size.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes(3)
            sage: ParallelogramPolyomino(                     # indirect doctest
            ....:     [[0, 1, 1], [1, 1, 0]]
            ....: ) in PPS
            True
        """
    def cardinality(self):
        """
        Return the number of parallelogram polyominoes.

        The number of parallelogram polyominoes of size n is given by
        the Catalan number `c_{n-1}`.

        EXAMPLES::

            sage: ParallelogramPolyominoes(1).cardinality()
            1
            sage: ParallelogramPolyominoes(2).cardinality()
            1
            sage: ParallelogramPolyominoes(3).cardinality()
            2
            sage: ParallelogramPolyominoes(4).cardinality()
            5

            sage: all(
            ....:     ParallelogramPolyominoes(i).cardinality()
            ....:     == len(list(ParallelogramPolyominoes(i)))
            ....:     for i in range(1,7)
            ....: )
            True
        """
    def __iter__(self):
        """
        Return a parallelogram polyomino generator.

        EXAMPLES::

            sage: len(list(ParallelogramPolyominoes(4))) == 5
            True
            sage: all(
            ....:     pp in ParallelogramPolyominoes()
            ....:     for pp in ParallelogramPolyominoes(4)
            ....: )
            True
        """
    def get_options(self):
        """
        Return all the options associated with all the elements of
        the set of parallelogram polyominoes with a fixed size.

        EXAMPLES::

            sage: pps = ParallelogramPolyominoes(5)
            sage: pps.get_options()
            Current options for ParallelogramPolyominoes_size
              - display:            'list'
            ...
        """
    def size(self):
        """
        Return the size of the parallelogram polyominoes generated by this
        parent.

        EXAMPLES::

            sage: ParallelogramPolyominoes(0).size()
            0
            sage: ParallelogramPolyominoes(1).size()
            1
            sage: ParallelogramPolyominoes(5).size()
            5
        """
    def set_options(self, *get_value, **set_value) -> None:
        """
        Set new options to the object.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes(3)
            sage: PPS.set_options(
            ....:     drawing_components=dict(
            ....:         diagram = True,
            ....:         bounce_0 = True,
            ....:         bounce_1 = True,
            ....:     )
            ....: )
            sage: pp = PPS[0]
            sage: view(pp) # not tested
        """
    options = ParallelogramPolyominoesOptions

class ParallelogramPolyominoes_all(ParentWithSetFactory, DisjointUnionEnumeratedSets):
    """
    This class enumerates all the parallelogram polyominoes.

    EXAMPLES::

        sage: PPS = ParallelogramPolyominoes()
        sage: PPS
        Parallelogram polyominoes
    """
    def __init__(self, policy) -> None:
        """
        Construct the set of all parallelogram polyominoes.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes()
            sage: PPS
            Parallelogram polyominoes

            sage: ParallelogramPolyomino([[0, 1, 1], [1, 1, 0]])  in PPS
            True

            sage: PPS = ParallelogramPolyominoes()
            sage: next(PPS.__iter__()) in PPS
            True
        """
    def check_element(self, el, check) -> None:
        """
        Check is a given element `el` is in the set of parallelogram
        polyominoes.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes()
            sage: ParallelogramPolyomino(                     # indirect doctest
            ....:     [[0, 1, 1], [1, 1, 0]]
            ....: ) in PPS
            True
        """
    def get_options(self):
        """
        Return all the options associated with the set of
        parallelogram polyominoes.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes()
            sage: options = PPS.get_options()
            sage: options
            Current options for ParallelogramPolyominoes_size
              - display:            'list'
            ...
        """
    def set_options(self, *get_value, **set_value) -> None:
        """
        Set new options to the object.

        EXAMPLES::

            sage: PPS = ParallelogramPolyominoes()
            sage: PPS.set_options(
            ....:     drawing_components=dict(
            ....:         diagram = True,
            ....:         bounce_0 = True,
            ....:         bounce_1 = True,
            ....:     )
            ....: )
            sage: pp = next(iter(PPS))
            sage: view(pp) # not tested
        """
    options = ParallelogramPolyominoesOptions
