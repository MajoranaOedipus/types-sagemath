from sage.misc.sageinspect import find_object_modules as find_object_modules

def runsnake(command) -> None:
    '''
    Graphical profiling with ``runsnake``.

    INPUT:

    - ``command`` -- the command to be run as a string

    EXAMPLES::

        sage: from sage.misc.dev_tools import runsnake
        sage: runsnake("list(SymmetricGroup(3))")        # optional - runsnake
        ...

    ``command`` is first preparsed (see :func:`preparse`)::

        sage: runsnake(\'for x in range(1,4): print(x^2)\') # optional - runsnake
        1
        4
        9

    :func:`runsnake` requires the program ``runsnake``. Due to non
    trivial dependencies (python-wxgtk, ...), installing it within the
    Sage distribution is unpractical. Hence, we recommend installing
    it with the system wide Python. On Ubuntu 10.10, this can be done
    with::

        > sudo apt-get install python-profiler python-wxgtk2.8 python-setuptools
        > sudo easy_install RunSnakeRun

    See the ``runsnake`` website for instructions for other platforms.

    :func:`runsnake` further assumes that the system wide Python is
    installed in ``/usr/bin/python``.

    .. SEEALSO::

        - `The runsnake website <http://www.vrplumber.com/programming/runsnakerun/>`_
        - ``%prun``
        - :class:`Profiler`
    '''
def import_statement_string(module, names, lazy):
    '''
    Return a (lazy) import statement for ``names`` from ``module``.

    INPUT:

    - ``module`` -- the name of a module

    - ``names`` -- list of 2-tuples containing names and alias to
      import

    - ``lazy`` -- boolean; whether to return a lazy import statement

    EXAMPLES::

        sage: import sage.misc.dev_tools as dt
        sage: modname = \'sage.misc.dev_tools\'
        sage: names_and_aliases = [(\'import_statement_string\', \'iss\')]
        sage: dt.import_statement_string(modname, names_and_aliases, False)
        \'from sage.misc.dev_tools import import_statement_string as iss\'
        sage: dt.import_statement_string(modname, names_and_aliases, True)
        "lazy_import(\'sage.misc.dev_tools\', \'import_statement_string\', \'iss\')"
        sage: dt.import_statement_string(modname, [(\'a\',\'b\'),(\'c\',\'c\'),(\'d\',\'e\')], False)
        \'from sage.misc.dev_tools import a as b, c, d as e\'
        sage: dt.import_statement_string(modname, [(None,None)], False)
        \'import sage.misc.dev_tools\'
    '''
def load_submodules(module=None, exclude_pattern=None) -> None:
    '''
    Load all submodules of a given modules.

    This method is intended to be used by developers and especially the one
    who uses :func:`import_statements`. By default it load the sage library and
    it takes around a minute.

    INPUT:

    - ``module`` -- an optional module

    - ``exclude_pattern`` -- an optional regular expression pattern of module
      names that have to be excluded

    EXAMPLES::

        sage: sage.misc.dev_tools.load_submodules(sage.combinat)
        load sage.combinat.algebraic_combinatorics... succeeded
        ...
        load sage.combinat.words.suffix_trees... succeeded

    Calling a second time has no effect (since the function does not import
    modules already imported)::

        sage: sage.misc.dev_tools.load_submodules(sage.combinat)

    The second argument allows to exclude a pattern::

        sage: sage.misc.dev_tools.load_submodules(sage.geometry, "database$|lattice")
        load sage.geometry.cone... succeeded
        load sage.geometry.cone_catalog... succeeded
        load sage.geometry.fan_isomorphism... succeeded
        ...
        load sage.geometry.riemannian_manifolds.surface3d_generators... succeeded

        sage: sage.misc.dev_tools.load_submodules(sage.geometry)
        load sage.geometry.polyhedron.lattice_euclidean_group_element... succeeded
        load sage.geometry.polyhedron.palp_database... succeeded
        load sage.geometry.polyhedron.ppl_lattice_polygon... succeeded
    '''
def find_objects_from_name(name, module_name=None, include_lazy_imports: bool = False):
    """
    Return the list of objects from ``module_name`` whose name is ``name``.

    INPUT:

    - ``name`` -- string

    - ``module_name`` -- string or ``None``:

      - If ``module_name`` is ``None``, the function runs through all
        loaded modules and returns the list of objects whose name matches ``name``.

      - If ``module_name`` is a string, then search only in submodules of
        ``module_name``.

    - ``include_lazy_imports`` -- boolean (default: ``False``); whether to
      include unresolved lazy imports (i.e., :class:`~sage.misc.lazy_import.LazyImport`
      objects) in the output.

    In order to search through more modules you might use the function
    :func:`load_submodules`.

    EXAMPLES::

        sage: import sage.misc.dev_tools as dt
        sage: dt.find_objects_from_name('FareySymbol')                                  # needs sage.modular
        [<class 'sage.modular.arithgroup.farey_symbol.Farey'>]

        sage: # needs sympy
        sage: import sympy
        sage: dt.find_objects_from_name('RR')
        [Real Field with 53 bits of precision, RR]
        sage: dt.find_objects_from_name('RR', 'sage')
        [Real Field with 53 bits of precision]
        sage: dt.find_objects_from_name('RR', 'sympy')
        [RR]

    Examples that do not belong to the global namespace but in a loaded module::

        sage: 'find_objects_from_name' in globals()
        False
        sage: objs = dt.find_objects_from_name('find_objects_from_name')
        sage: len(objs)
        1
        sage: dt.find_objects_from_name is dt.find_objects_from_name
        True

    When ``include_lazy_imports=True`` is used, several
    :class:`~sage.misc.lazy_import.LazyImport` objects that are resolving to the
    same object may be included in the output::

        sage: dt.find_objects_from_name('RR', include_lazy_imports=True)                # needs sage.rings.real_mpfr
        [Real Field with 53 bits of precision,
         ...
         Real Field with 53 bits of precision,
         RR]

    .. NOTE::

        It might be a good idea to move this function into
        :mod:`sage.misc.sageinspect`.
    """
def import_statements(*objects, **kwds):
    '''
    Print import statements for the given objects.

    INPUT:

    - ``*objects`` -- a sequence of objects or comma-separated strings of names

    - ``lazy`` -- boolean (default: ``False``); whether to print a lazy import
      statement

    - ``verbose`` -- boolean (default: ``True``); whether to print information
      in case of ambiguity

    - ``answer_as_str`` -- boolean (default: ``False``); if ``True`` return a
      string instead of printing the statement

    EXAMPLES::

        sage: import_statements(WeylGroup, lazy_attribute)                              # needs sage.libs.gap
        from sage.combinat.root_system.weyl_group import WeylGroup
        from sage.misc.lazy_attribute import lazy_attribute

        sage: import_statements(IntegerRing)
        from sage.rings.integer_ring import IntegerRing

    If ``lazy`` is True, then :func:`lazy_import` statements are
    displayed instead::

        sage: import_statements(WeylGroup, lazy_attribute, lazy=True)                   # needs sage.libs.gap
        from sage.misc.lazy_import import lazy_import
        lazy_import(\'sage.combinat.root_system.weyl_group\', \'WeylGroup\')
        lazy_import(\'sage.misc.lazy_attribute\', \'lazy_attribute\')

    In principle, the function should also work on object which are instances.
    In case of ambiguity, one or two warning lines are printed::

        sage: import_statements(RDF)
        from sage.rings.real_double import RDF

        sage: import_statements(ZZ)
        # ** Warning **: several names for that object: Z, ZZ
        from sage.rings.integer_ring import Z

        sage: import_statements(euler_phi)
        from sage.arith.misc import euler_phi

        sage: import_statements(x)                                                      # needs sage.symbolic
        from sage.calculus.predefined import x

    If you don\'t like the warning you can disable them with the option ``verbose``::

        sage: import_statements(ZZ, verbose=False)
        from sage.rings.integer_ring import Z

        sage: import_statements(x, verbose=False)                                       # needs sage.symbolic
        from sage.calculus.predefined import x

    If the object has several names, an other way to get the import
    statement you expect is to use a string instead of the object::

        sage: import_statements(matrix)                                                 # needs sage.modules
        # ** Warning **: several names for that object: Matrix, matrix
        from sage.matrix.constructor import Matrix

        sage: import_statements(\'cached_function\')
        from sage.misc.cachefunc import cached_function
        sage: import_statements(\'Z\')
        # **Warning**: distinct objects with name \'Z\' in:
        #   - sage.calculus.predefined
        #   - sage.rings.integer_ring
        from sage.rings.integer_ring import Z

    The strings are allowed to be comma-separated names, and parenthesis
    are stripped for convenience::

        sage: import_statements(\'(floor, ceil)\')                                        # needs sage.symbolic
        from sage.functions.other import floor, ceil

    Specifying a string is also useful for objects that are not
    imported in the Sage interpreter namespace by default. In this
    case, an object with that name is looked up in all the modules
    that have been imported in this session::

        sage: import_statement_string
        Traceback (most recent call last):
        ...
        NameError: name \'import_statement_string\' is not defined

        sage: import_statements("import_statement_string")
        from sage.misc.dev_tools import import_statement_string

    Sometimes objects are imported as an alias (from XXX import YYY as ZZZ) or
    are affected (XXX = YYY) and the function might detect it::

        sage: import_statements(\'FareySymbol\')
        from sage.modular.arithgroup.farey_symbol import Farey as FareySymbol

        sage: import_statements(\'power\')
        from sage.arith.power import generic_power as power

    In order to be able to detect functions that belong to a non-loaded module,
    you might call the helper :func:`load_submodules` as in the following::

        sage: import_statements(\'HeckeMonoid\')
        Traceback (most recent call last):
        ...
        LookupError: no object named \'HeckeMonoid\'
        sage: from sage.misc.dev_tools import load_submodules
        sage: load_submodules(sage.monoids)
        load sage.monoids.automatic_semigroup... succeeded
        load sage.monoids.hecke_monoid... succeeded
        load sage.monoids.indexed_free_monoid... succeeded
        sage: import_statements(\'HeckeMonoid\')
        from sage.monoids.hecke_monoid import HeckeMonoid

    We test different objects which have no appropriate answer::

        sage: import_statements(\'my_tailor_is_rich\')
        Traceback (most recent call last):
        ...
        LookupError: no object named \'my_tailor_is_rich\'
        sage: import_statements(5)
        Traceback (most recent call last):
        ...
        ValueError: no import statement found for \'5\'.

    We test that it behaves well with lazy imported objects (:issue:`14767`)::

        sage: import_statements(NN)
        from sage.rings.semirings.non_negative_integer_semiring import NN
        sage: import_statements(\'NN\')
        from sage.rings.semirings.non_negative_integer_semiring import NN

    Deprecated lazy imports are ignored (see :issue:`17458`)::

        sage: lazy_import(\'sage.all\', \'RR\', \'deprecated_RR\', namespace=sage.__dict__, deprecation=17458)
        sage: import_statements(\'deprecated_RR\')
        Traceback (most recent call last):
        ...
        LookupError: object named \'deprecated_RR\' is deprecated (see Issue #17458)
        sage: lazy_import(\'sage.all\', \'RR\', namespace=sage.__dict__, deprecation=17458)
        sage: import_statements(\'RR\')
        from sage.rings.real_mpfr import RR

    The following were fixed with :issue:`15351`::

        sage: import_statements(\'Rationals\')
        from sage.rings.rational_field import RationalField as Rationals
        sage: import_statements(sage.combinat.partition_algebra.SetPartitionsAk)
        from sage.combinat.partition_algebra import SetPartitionsAk
        sage: import_statements(CIF)
        from sage.rings.cif import CIF
        sage: import_statements(NaN)                                                    # needs sage.symbolic
        from sage.symbolic.constants import NaN
        sage: import_statements(pi)                                                     # needs sage.symbolic
        from sage.symbolic.constants import pi
        sage: import_statements(\'SAGE_ENV\')
        from sage.env import SAGE_ENV
        sage: import_statements(\'graph_decompositions\')
        import sage.graphs.graph_decompositions

    Check that a name from the global namespace is properly found (see
    :issue:`23779`)::

        sage: import_statements(\'log\')
        from sage.misc.functional import log

    .. NOTE::

        The programmers try to made this function as smart as possible.
        Nevertheless it is far from being perfect (for example it does not
        detect deprecated stuff). So, if you use it, double check the answer and
        report weird behaviors.
    '''
