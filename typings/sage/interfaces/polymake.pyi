from .interface import Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunctionElement as InterfaceFunctionElement
from _typeshed import Incomplete
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.verbose import get_verbose as get_verbose
from sage.structure.richcmp import rich_to_bool as rich_to_bool

class PolymakeError(RuntimeError):
    '''
    Raised if polymake yields an error message.

    TESTS::

        sage: polymake.eval(\'print foo;\')    # optional - jupymake
        Traceback (most recent call last):
        ...
        PolymakeError: Unquoted string "foo" may clash with future reserved word...
    '''

def polymake_console(command: str = '') -> None:
    """
    Spawn a new polymake command-line session.

    EXAMPLES::

        sage: from sage.interfaces.polymake import polymake_console
        sage: polymake_console()        # not tested
        Welcome to polymake version ...
        ...
        Ewgenij Gawrilow, Michael Joswig (TU Berlin)
        http://www.polymake.org

        This is free software licensed under GPL; see the source for copying conditions.
        There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

        Press F1 or enter 'help;' for basic instructions.

        Application polytope currently uses following third-party software packages:
        4ti2, bliss, cdd, latte, libnormaliz, lrs, permlib, ppl, sketch, sympol, threejs, tikz, topcom, tosimplex
        For more details:  show_credits;
        polytope >
    """

class PolymakeAbstract(ExtraTabCompletion, Interface):
    """
    Abstract interface to the polymake interpreter.

    This class should not be instantiated directly,
    but through its subclasses Polymake (Pexpect interface)
    or PolymakeJuPyMake (JuPyMake interface).

    EXAMPLES::

        sage: from sage.interfaces.polymake import PolymakeAbstract, polymake_jupymake

    We test the verbosity management with very early doctests
    because messages will not be repeated.

    Testing the JuPyMake interface::

        sage: isinstance(polymake_jupymake, PolymakeAbstract)
        True
        sage: p = polymake_jupymake.rand_sphere(4, 20, seed=5)       # optional - jupymake
        sage: p                                             # optional - jupymake
        Random spherical polytope of dimension 4; seed=5...
        sage: set_verbose(3)
        sage: p.H_VECTOR                                    # optional - jupymake
        polymake: used package ppl
          The Parma Polyhedra Library ...
        1 16 40 16 1
        sage: set_verbose(0)
        sage: p.F_VECTOR                                    # optional - jupymake
        20 94 148 74
    """
    def __init__(self, seed=None) -> None:
        """
        TESTS::

            sage: from sage.interfaces.polymake import PolymakeAbstract
            sage: PolymakeAbstract()
            Polymake
        """
    @cached_method
    def version(self):
        """
        Version of the polymake installation.

        EXAMPLES::

            sage: polymake.version()               # optional - jupymake # random
            '4...'
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: from sage.interfaces.polymake import polymake
            sage: loads(dumps(polymake)) is polymake
            True
        """
    def function_call(self, function, args=None, kwds=None):
        """
        EXAMPLES::

            sage: polymake.rand_sphere(4, 30, seed=15)           # optional - jupymake  # indirect doctest
            Random spherical polytope of dimension 4; seed=15...
        """
    def console(self) -> None:
        """
        Raise an error, pointing to :meth:`~sage.interfaces.interface.Interface.interact` and :func:`polymake_console`.

        EXAMPLES::

            sage: polymake.console()
            Traceback (most recent call last):
            ...
            NotImplementedError: Please use polymake_console() function or the .interact() method
        """
    def clear(self, var) -> None:
        """
        Clear the variable named ``var``.

        .. NOTE::

            This is implicitly done when deleting an element in the interface.

        TESTS::

            sage: # optional - jupymake
            sage: from sage.interfaces.polymake import polymake
            sage: c = polymake.cube(15)
            sage: polymake._available_vars = []
            sage: old = c._name
            sage: del c
            sage: len(polymake._available_vars)
            1
            sage: polymake._next_var_name() in old
            True
        """
    def set(self, var, value) -> None:
        '''
        Set the variable var to the given value.

        Eventually, ``var`` is a reference to ``value``.

        .. WARNING::

            This method, although it doesn\'t start with an underscore, is
            an internal method and not part of the interface. So, please do
            not try to call it explicitly. Instead, use the polymake interface
            as shown in the examples.

        REMARK:

        Polymake\'s user language is Perl. In Perl, if one wants to assign
        the return value of a function to a variable, the syntax to do so
        depends on the type of the return value. While this is fine in
        compiled code, it seems quite awkward in user interaction.

        To make this polymake pexpect interface a bit more user friendly,
        we treat *all* variables as arrays. A scalar value (most typically
        a reference) is thus interpreted as the only item in an array of
        length one. It is, of course, possible to use the interface without
        knowing these details.

        EXAMPLES::

            sage: c = polymake(\'cube(3)\')                       # optional - jupymake # indirect doctest
            sage: d = polymake.cube(3)                          # optional - jupymake

        Equality is, for "big" objects such as polytopes, comparison by
        identity::

            sage: c == d                                        # optional - jupymake
            False

        However, the list of vertices is equal::

            sage: c.VERTICES == d.VERTICES                      # optional - jupymake
            True

        TESTS:

        The following shows how polymake variables are wrapped in our interface.
        It should, however, **never** be needed to do the following
        *explicitly*::

            sage: polymake.set(\'myvar\', \'cube(3)\')              # optional - jupymake
            sage: polymake.get(\'$myvar[0]\')                     # optional - jupymake
            \'Polymake::polytope::Polytope__Rational=ARRAY(...)\'

        The following tests against :issue:`22658`::

            sage: P = polymake.new_object("Polytope", FACETS=[[12, -2, -3, -5, -8, -13, -21, -34, -55],   # optional - jupymake
            ....:  [0, 1, 0, 0, 0, 0, 0, 0, 0],
            ....:  [0, 0, 0, 0, 0, 0, 0, 0, 1],
            ....:  [0, 0, 0, 0, 0, 0, 0, 1, 0],
            ....:  [0, 0, 0, 0, 0, 0, 1, 0, 0],
            ....:  [0, 0, 0, 0, 0, 1, 0, 0, 0],
            ....:  [0, 0, 0, 0, 1, 0, 0, 0, 0],
            ....:  [0, 0, 0, 1, 0, 0, 0, 0, 0],
            ....:  [0, 0, 1, 0, 0, 0, 0, 0, 0]])
            sage: P.VERTICES                        # optional - jupymake
            1 6 0 0 0 0 0 0 0
            1 0 4 0 0 0 0 0 0
            1 0 0 0 0 0 0 0 0
            1 0 0 12/5 0 0 0 0 0
            1 0 0 0 0 0 0 0 12/55
            1 0 0 0 0 0 0 6/17 0
            1 0 0 0 0 0 4/7 0 0
            1 0 0 0 0 12/13 0 0 0
            1 0 0 0 3/2 0 0 0 0
            sage: P.F_VECTOR                        # optional - jupymake
            9 36 84 126 126 84 36 9
        '''
    def get(self, cmd):
        '''
        Return the string representation of an object in the polymake interface.

        EXAMPLES::

            sage: polymake.get(\'cube(3)\')                     # optional - jupymake
            \'Polymake::polytope::Polytope__Rational=ARRAY(...)\'

        Note that the above string representation is what polymake provides.
        In our interface, we use what polymake calls a "description"::

            sage: polymake(\'cube(3)\')                         # optional - jupymake
            cube of dimension 3
        '''
    def help(self, topic, pager: bool = True):
        '''
        Displays polymake\'s help on a given topic, as a string.

        INPUT:

        - ``topic`` -- string
        - ``pager`` -- boolean (default: ``True``); when ``True``, display
          help, otherwise return as a string

        EXAMPLES::

            sage: print(polymake.help(\'Polytope\', pager=False))         # optional - jupymake # random
            objects/Polytope:
             Not necessarily bounded or unbounded polyhedron.
             Nonetheless, the name "Polytope" is used for two reasons:
             Firstly, combinatorially we always deal with polytopes; see the description of VERTICES_IN_FACETS for details.
             The second reason is historical.
             We use homogeneous coordinates, which is why Polytope is derived from Cone.
             Note that a pointed polyhedron is projectively equivalent to a polytope.
             Scalar is the numeric data type used for the coordinates.

        In some cases, polymake expects user interaction to choose from
        different available help topics. In these cases, a warning is given,
        and the available help topics are displayed resp. printed, without
        user interaction::

            sage: polymake.help(\'TRIANGULATION\')                        # optional - jupymake # random
            doctest:warning
            ...
            UserWarning: Polymake expects user interaction. We abort and return the options that Polymake provides.
            There are 5 help topics matching \'TRIANGULATION\':
            1: objects/Visualization/Visual::Polytope/methods/TRIANGULATION
            2: objects/Visualization/Visual::PointConfiguration/methods/TRIANGULATION
            3: objects/Cone/properties/Triangulation and volume/TRIANGULATION
            4: objects/PointConfiguration/properties/Triangulation and volume/TRIANGULATION
            5: objects/Polytope/properties/Triangulation and volume/TRIANGULATION

        If an unknown help topic is requested, a :exc:`PolymakeError`
        results::

            sage: polymake.help(\'Triangulation\')      # optional - jupymake
            Traceback (most recent call last):
            ...
            PolymakeError: unknown help topic \'Triangulation\'
        '''
    def application(self, app) -> None:
        '''
        Change to a given polymake application.

        INPUT:

        - ``app`` -- string; one of ``\'common\'``, ``\'fulton\'``, ``\'group\'``,
          ``\'matroid\'``, ``\'topaz\'``, ``\'fan\'``, ``\'graph\'``, ``\'ideal\'``,
          ``\'polytope\'``, ``\'tropical\'``

        EXAMPLES:

        We expose a computation that uses both the \'polytope\' and the \'fan\'
        application of polymake. Let us start by defining a polytope `q` in
        terms of inequalities. Polymake knows to compute the f- and h-vector
        and finds that the polytope is very ample::

            sage: # optional - jupymake
            sage: q = polymake.new_object("Polytope", INEQUALITIES=[[5,-4,0,1],[-3,0,-4,1],[-2,1,0,0],[-4,4,4,-1],[0,0,1,0],[8,0,0,-1],[1,0,-1,0],[3,-1,0,0]])
            sage: q.H_VECTOR
            1 5 5 1
            sage: q.F_VECTOR
            8 14 8
            sage: q.VERY_AMPLE
            true

        In the application \'fan\', polymake can now compute the normal fan
        of `q` and its (primitive) rays::

            sage: # optional - jupymake
            sage: polymake.application(\'fan\')
            sage: g = q.normal_fan()
            sage: g.RAYS
            -1 0 1/4
            0 -1 1/4
            1 0 0
            1 1 -1/4
            0 1 0
            0 0 -1
            0 -1 0
            -1 0 0
            sage: g.RAYS.primitive()
            -4 0 1
            0 -4 1
            1 0 0
            4 4 -1
            0 1 0
            0 0 -1
            0 -1 0
            -1 0 0

        Note that the list of functions available by tab completion depends
        on the application.

        TESTS:

        Since \'trop_witness\' is not defined in the polymake application \'polytope\'
        but only in \'tropical\', the following shows the effect of changing
        the application. ::

            sage: # optional - jupymake
            sage: polymake.application(\'polytope\')
            sage: \'trop_witness\' in dir(polymake)
            False
            sage: polymake.application(\'tropical\')
            sage: \'trop_witness\' in dir(polymake)
            True
            sage: polymake.application(\'polytope\')
            sage: \'trop_witness\' in dir(polymake)
            False

        For completeness, we show what happens when asking for an application
        that doesn\'t exist::

            sage: polymake.application(\'killerapp\')                  # optional - jupymake
            Traceback (most recent call last):
            ...
            ValueError: Unknown polymake application \'killerapp\'

        Of course, a different error results when we send an explicit
        command in polymake to change to an unknown application::

            sage: polymake.eval(\'application "killerapp";\')         # optional - jupymake
            Traceback (most recent call last):
            ...
            PolymakeError: Unknown application killerapp
        '''
    def new_object(self, name, *args, **kwds):
        '''
        Return a new instance of a given polymake type, with given positional or named arguments.

        INPUT:

        - ``name`` of a polymake class (potentially templated), as string.
        - further positional or named arguments, to be passed to the constructor.

        EXAMPLES::

            sage: # optional - jupymake
            sage: q = polymake.new_object("Polytope<Rational>", INEQUALITIES=[[4,-4,0,1],[-4,0,-4,1],[-2,1,0,0],[-4,4,4,-1],[0,0,1,0],[8,0,0,-1]])
            sage: q.N_VERTICES
            4
            sage: q.BOUNDED
            true
            sage: q.VERTICES
            1 2 0 4
            1 3 0 8
            1 2 1 8
            1 3 1 8
            sage: q.full_typename()
            \'Polytope<Rational>\'
        '''

class PolymakeElement(ExtraTabCompletion, InterfaceElement):
    '''
    Elements in the polymake interface.

    EXAMPLES:

    We support all "big" polymake types, Perl arrays of length
    different from one, and Perl scalars::

        sage: p = polymake.rand_sphere(4, 20, seed=5)            # optional - jupymake
        sage: p.typename()                                      # optional - jupymake
        \'Polytope\'
        sage: p                                                 # optional - jupymake
        Random spherical polytope of dimension 4; seed=5...

    Now, one can work with that element in Python syntax, for example::

        sage: p.VERTICES[2][2]                                  # optional - jupymake
        1450479926727001/2251799813685248
    '''
    def __bool__(self) -> bool:
        """
        Return whether this polymake element is equal to ``True``.

        EXAMPLES::

            sage: from sage.interfaces.polymake import polymake
            sage: bool(polymake(0))                # optional - jupymake
            False
            sage: bool(polymake(1))                # optional - jupymake
            True
        """
    def known_properties(self):
        """
        List the names of properties that have been computed so far on this element.

        .. NOTE::

            This is in many cases equivalent to use polymake's
            ``list_properties``, which returns a blank separated string
            representation of the list of properties. However, on some
            elements, ``list_properties`` would simply result in an error.

        EXAMPLES::

            sage: c = polymake.cube(4)                      # optional - jupymake
            sage: c.known_properties()                      # optional - jupymake
            ['AFFINE_HULL',
             'BOUNDED',
             'CONE_AMBIENT_DIM',
             'CONE_DIM',
            ...
             'VERTICES_IN_FACETS']
            sage: c.list_properties()                       # optional - jupymake
            CONE_AMBIENT_DIM, CONE_DIM, FACETS, AFFINE_HULL, VERTICES_IN_FACETS,
            BOUNDED...

        A computation can change the list of known properties::

            sage: c.F_VECTOR                                # optional - jupymake
            16 32 24 8
            sage: c.known_properties()                      # optional - jupymake
            ['AFFINE_HULL',
             'BOUNDED',
             'COMBINATORIAL_DIM',
             'CONE_AMBIENT_DIM',
             'CONE_DIM',
            ...
             'VERTICES_IN_FACETS']
        """
    def typename(self):
        """
        The name of the underlying base type of this element in polymake.

        EXAMPLES::

            sage: c = polymake.cube(4)          # optional - jupymake
            sage: c.typename()                  # optional - jupymake
            'Polytope'
            sage: c.VERTICES.typename()         # optional - jupymake
            'Matrix'
        """
    def full_typename(self):
        """
        The name of the specialised type of this element.

        EXAMPLES::

            sage: c = polymake.cube(4)          # optional - jupymake
            sage: c.full_typename()             # optional - jupymake
            'Polytope<Rational>'
            sage: c.VERTICES.full_typename()    # optional - jupymake
            'Matrix<Rational, NonSymmetric>'
        """
    def qualified_typename(self):
        """
        The qualified name of the type of this element.

        EXAMPLES::

            sage: c = polymake.cube(4)              # optional - jupymake
            sage: c.qualified_typename()            # optional - jupymake
            'polytope::Polytope<Rational>'
            sage: c.VERTICES.qualified_typename()   # optional - jupymake
            'common::Matrix<Rational, NonSymmetric>'
        """
    def __getattr__(self, attrname):
        """
        Return a property of this element, or a polymake function with this
        element as first argument, or a member function of this element.

        .. NOTE::

            If the attribute name is known as the name of a property, it is
            interpreted as such. Otherwise, if it is known as a function in
            the current application, the function is returned with this
            element inserted as first argument, and potential further arguments,
            when called. Otherwise, it is assumed that it is a member function
            of this element, and treated as such. Note that member functions
            are currently invisible in tab completion, thus, the user has
            to know the name of the member function.

        EXAMPLES:

        A property::

            sage: # optional - jupymake
            sage: c = polymake.cube(3)
            sage: c.H_VECTOR
            1 5 5 1
            sage: c.N_VERTICES
            8
            sage: d = polymake.cross(3)
            sage: d.N_VERTICES
            6

        A function::

            sage: # optional - jupymake
            sage: c.minkowski_sum_fukuda
            minkowski_sum_fukuda (bound to Polymake::polytope::Polytope__Rational object)
            sage: s = c.minkowski_sum_fukuda(d)
            sage: s.N_VERTICES
            24
            sage: s
            Polytope<Rational>[SAGE...]

        A member function::

            sage: # optional - jupymake
            sage: c = polymake.cube(2)
            sage: V = polymake.new_object('Vector', [1,0,0])
            sage: V
            1 0 0
            sage: c.contains
            Member function 'contains' of Polymake::polytope::Polytope__Rational object
            sage: c.contains(V)
            true
        """
    def get_member_function(self, attrname):
        '''
        Request a member function of this element.

        .. NOTE::

            It is not checked whether a member function with the given name
            exists.

        EXAMPLES::

            sage: # optional - jupymake
            sage: c = polymake.cube(2)
            sage: c.contains
            Member function \'contains\' of Polymake::polytope::Polytope__Rational object
            sage: V = polymake.new_object(\'Vector\', [1,0,0])
            sage: V
            1 0 0
            sage: c.contains(V)
            true

        Whether a member function of the given name actually exists for that
        object will only be clear when calling it::

            sage: c.get_member_function("foo")                          # optional - jupymake
            Member function \'foo\' of Polymake::polytope::Polytope__Rational object
            sage: c.get_member_function("foo")()                        # optional - jupymake
            Traceback (most recent call last):
            ...
            TypeError: Can\'t locate object method "foo" via package "Polymake::polytope::Polytope__Rational"
        '''
    def get_member(self, attrname):
        """
        Get a member/property of this element.

        .. NOTE::

            Normally, it should be possible to just access the property
            in the usual Python syntax for attribute access. However, if
            that fails, one can request the member explicitly.

        EXAMPLES::

            sage: p = polymake.rand_sphere(4, 20, seed=5)    # optional - jupymake

        Normally, a property would be accessed as follows::

            sage: p.F_VECTOR                                # optional - jupymake
            20 94 148 74

        However, explicit access is possible as well::

            sage: p.get_member('F_VECTOR')                  # optional - jupymake
            20 94 148 74

        In some cases, the explicit access works better::

            sage: p.type                                    # optional - jupymake
            Member function 'type' of Polymake::polytope::Polytope__Rational object
            sage: p.get_member('type')                      # optional - jupymake
            Polytope<Rational>[SAGE...]
            sage: p.get_member('type').get_member('name')   # optional - jupymake
            Polytope

        Note that in the last example calling the erroneously constructed
        member function ``type`` still works::

            sage: p.type()                                  # optional - jupymake
            Polytope<Rational>[SAGE...]
        """
    def __getitem__(self, key):
        """
        Indexing and slicing.

        Slicing returns a Python list.

        EXAMPLES::

            sage: p = polymake.rand_sphere(3, 12, seed=15)  # optional - jupymake
            sage: p.VERTICES[3]                             # optional - jupymake
            1 7977905618560809/18014398509481984 -1671539598851959/144115188075855872 8075083879632623/9007199254740992
            sage: p.list_properties()[2]                    # optional - jupymake
            BOUNDED

        Slicing::

            sage: p.F_VECTOR[:]                             # optional - jupymake
            [12, 30, 20]
            sage: p.F_VECTOR[0:1]                           # optional - jupymake
            [12]
            sage: p.F_VECTOR[0:3:2]                         # optional - jupymake
            [12, 20]
        """
    def __iter__(self):
        """
        Return an iterator for ``self``.

        OUTPUT: iterator

        EXAMPLES::

            sage: p = polymake.rand_sphere(3, 12, seed=15)  # optional - jupymake
            sage: [ x for x in p.VERTICES[3] ]              # optional - jupymake
            [1, 7977905618560809/18014398509481984, -1671539598851959/144115188075855872, 8075083879632623/9007199254740992]
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: p = polymake.rand_sphere(3, 12, seed=15)           # optional - jupymake
            sage: len(p.FACETS)                                     # optional - jupymake
            20
            sage: len(p.list_properties()) >= 12                     # optional - jupymake
            True
        """
    @cached_method
    def typeof(self):
        '''
        Return the type of a polymake "big" object, and its
        underlying Perl type.

        .. NOTE::

            This is mainly for internal use.

        EXAMPLES::

            sage: # optional - jupymake
            sage: p = polymake.rand_sphere(3, 13, seed=12)
            sage: p.typeof()
            (\'Polymake::polytope::Polytope__Rational\', \'ARRAY\')
            sage: p.VERTICES.typeof()
            (\'Polymake::common::Matrix_A_Rational_I_NonSymmetric_Z\', \'ARRAY\')
            sage: p.get_schedule(\'"F_VECTOR"\').typeof()
            (\'Polymake::Core::Scheduler::RuleChain\', \'ARRAY\')

        On "small" objects, it just returns empty strings::

            sage: p.N_VERTICES.typeof()                                 # optional - jupymake
            (\'\', \'\')
            sage: p.list_properties().typeof()                          # optional - jupymake
            (\'\', \'\')
        '''

class PolymakeFunctionElement(InterfaceFunctionElement):
    """
    A callable (function or member function) bound to a polymake element.

    EXAMPLES::

        sage: # optional - jupymake
        sage: c = polymake.cube(2)
        sage: V = polymake.new_object('Vector', [1,0,0])
        sage: V
        1 0 0
        sage: c.contains
        Member function 'contains' of Polymake::polytope::Polytope__Rational object
        sage: c.contains(V)
        true
    """
    def __init__(self, obj, name, memberfunction: bool = False) -> None:
        '''
        INPUT:

        - ``obj`` -- Polymake object that this function is bound to
        - ``name`` -- string; it actually says how to call this function in
          polymake. So, if it is a member function, it will look like
          `"$SAGE123[0]->func_name"`.
        - ``memberfunction`` -- boolean (default: ``False``); whether this is a
          member function or a plain function applied with this element as
          first argument

        EXAMPLES::

            sage: p = polymake.rand_sphere(3, 13, seed=12)   # optional - jupymake
            sage: p.minkowski_sum_fukuda                    # optional - jupymake
            minkowski_sum_fukuda (bound to Polymake::polytope::Polytope__Rational object)
            sage: p.get_schedule                            # optional - jupymake
            Member function \'get_schedule\' of Polymake::polytope::Polytope__Rational object
        '''
    def __call__(self, *args, **kwds):
        '''
        EXAMPLES:

        We consider both member functions of an element and global functions
        bound to an element::

            sage: p = polymake.rand_sphere(3, 13, seed=12)      # optional - jupymake
            sage: p.get_schedule(\'"VERTICES"\')                    # optional - jupymake  # random
            sensitivity check for VertexPerm
            cdd.convex_hull.canon: POINTED, RAYS, LINEALITY_SPACE : INPUT_RAYS
            sage: p.minkowski_sum_fukuda(p).F_VECTOR            # optional - jupymake # not tested
            13 33 22
        '''

class PolymakeJuPyMake(PolymakeAbstract):
    '''
    Interface to the polymake interpreter using JuPyMake.

    In order to use this interface, you need to either install the
    optional polymake package for Sage, or install polymake system-wide
    on your computer; it is available from https://polymake.org.
    Also install the jupymake Python package.

    Type ``polymake.[tab]`` for a list of most functions
    available from your polymake install. Type
    ``polymake.Function?`` for polymake\'s help about a given ``Function``.
    Type ``polymake(...)`` to create a new polymake
    object, and ``polymake.eval(...)`` to run a string using
    polymake and get the result back as a string.

    EXAMPLES::

        sage: from sage.interfaces.polymake import polymake_jupymake as polymake
        sage: type(polymake)
        <...sage.interfaces.polymake.PolymakeJuPyMake...
        sage: p = polymake.rand_sphere(4, 20, seed=5)       # optional - jupymake
        sage: p                                             # optional - jupymake
        Random spherical polytope of dimension 4; seed=5...
        sage: set_verbose(3)
        sage: p.H_VECTOR;                                   # optional - jupymake # random
        used package ppl
          The Parma Polyhedra Library ...
        sage: p.H_VECTOR                                    # optional - jupymake
        1 16 40 16 1
        sage: set_verbose(0)
        sage: p.F_VECTOR                                    # optional - jupymake
        20 94 148 74
        sage: print(p.F_VECTOR._sage_doc_())                # optional - jupymake # random
        property_types/Algebraic Types/Vector:
         A type for vectors with entries of type Element.

         You can perform algebraic operations such as addition or scalar multiplication.

         You can create a new Vector by entering its elements, e.g.:
            $v = new Vector<Int>(1,2,3);
         or
            $v = new Vector<Int>([1,2,3]);

    Python strings are translated to polymake (Perl) identifiers.
    To obtain Perl strings, use strings containing double-quote characters.
    Python dicts are translated to Perl hashes.

    ::

         sage: # long time, optional - internet jupymake perl_mongodb
         sage: L = polymake.db_query({\'"_id"\': \'"F.4D.0047"\'},
         ....:                       db=\'"LatticePolytopes"\',
         ....:                       collection=\'"SmoothReflexive"\'); L
         BigObjectArray
         sage: len(L)
         1
         sage: P = L[0]
         sage: sorted(P.list_properties(), key=str)
         [..., LATTICE_POINTS_GENERATORS, ..., POINTED, ...]
         sage: P.F_VECTOR
         20 40 29 9
    '''
    def __init__(self, seed=None, verbose: bool = False) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); whether to print the
          commands passed to polymake

        TESTS::

            sage: from sage.interfaces.polymake import PolymakeJuPyMake
            sage: PolymakeJuPyMake()
            Polymake
        """
    def is_running(self):
        """
        Return ``True`` if ``self`` is currently running.

        TESTS::

            sage: from sage.interfaces.polymake import PolymakeJuPyMake
            sage: pm = PolymakeJuPyMake()
            sage: pm(1)                         # optional - jupymake
            1
            sage: pm.is_running()               # optional - jupymake
            True

        Several PolymakeJuPyMake interfaces can be created, but they all
        talk to the same polymake interpreter::

            sage: pm2 = PolymakeJuPyMake()
            sage: pm2.is_running()              # optional - jupymake
            True
        """
    def eval(self, code, **kwds):
        '''
        Evaluate a command.

        INPUT:

        - ``code`` -- a command (string) to be evaluated

        Different reaction types of polymake, including warnings, comments,
        errors, request for user interaction, and yielding a continuation prompt,
        are taken into account.

        EXAMPLES::

            sage: from sage.interfaces.polymake import polymake_jupymake as polymake
            sage: p = polymake.cube(3)              # optional - jupymake  # indirect doctest

        Here we see that remarks printed by polymake are displayed if
        the verbosity is positive::

            sage: set_verbose(1)
            sage: p.N_LATTICE_POINTS                # optional - jupymake # random
            used package latte
              LattE (Lattice point Enumeration) is a computer software dedicated to the
              problems of counting lattice points and integration inside convex polytopes.
              Copyright by Matthias Koeppe, Jesus A. De Loera and others.
              http://www.math.ucdavis.edu/~latte/
            27
            sage: set_verbose(0)

        If polymake raises an error, the polymake *interface* raises
        a :exc:`PolymakeError`::

            sage: polymake.eval(\'FOOBAR(3);\')       # optional - jupymake
            Traceback (most recent call last):
            ...
            PolymakeError: Undefined subroutine &Polymake::User::FOOBAR called...

        If a command is incomplete, then polymake returns a continuation
        prompt. In that case, we raise an error::

            sage: polymake.eval(\'print 3\')          # optional - jupymake
            Traceback (most recent call last):
            ...
            SyntaxError: Incomplete polymake command \'print 3\'
            sage: polymake.eval(\'print 3;\')         # optional - jupymake
            \'3\'

        However, if the command contains line breaks but eventually is complete,
        no error is raised::

            sage: print(polymake.eval(\'$tmp="abc";\\nprint $tmp;\'))  # optional - jupymake
            abc

        When requesting help, polymake sometimes expects the user to choose
        from a list. In that situation, we abort with a warning, and show
        the list from which the user can choose; we could demonstrate this using
        the :meth:`~sage.interfaces.polymake.PolymakeAbstract.help` method,
        but here we use an explicit code evaluation::

            sage: print(polymake.eval(\'help "TRIANGULATION";\'))     # optional - jupymake # random
            doctest:warning
            ...
            UserWarning: Polymake expects user interaction. We abort and return
            the options that Polymake provides.
            There are 5 help topics matching \'TRIANGULATION\':
            1: objects/Cone/properties/Triangulation and volume/TRIANGULATION
            2: objects/Polytope/properties/Triangulation and volume/TRIANGULATION
            3: objects/Visualization/Visual::PointConfiguration/methods/TRIANGULATION
            4: objects/Visualization/Visual::Polytope/methods/TRIANGULATION
            5: objects/PointConfiguration/properties/Triangulation and volume/TRIANGULATION

        By default, we just wait until polymake returns a result. However,
        it is possible to explicitly set a timeout. The following usually does
        work in an interactive session and often in doc tests, too. However,
        sometimes it hangs, and therefore we remove it from the tests, for now::

            sage: c = polymake.cube(15)             # optional - jupymake
            sage: polymake.eval(\'print {}->F_VECTOR;\'.format(c.name()), timeout=1) # not tested # optional - jupymake
            Traceback (most recent call last):
            ...
            RuntimeError: Polymake fails to respond timely

        We verify that after the timeout, polymake is still able
        to give answers::

            sage: c                                 # optional - jupymake
            cube of dimension 15
            sage: c.N_VERTICES                      # optional - jupymake
            32768

        Note, however, that the recovery after a timeout is not perfect.
        It may happen that in some situation the interface collapses and
        thus polymake would automatically be restarted, thereby losing all
        data that have been computed before.
        '''

def reduce_load_Polymake():
    """
    Return the polymake interface object defined in :mod:`sage.interfaces.polymake`.

    EXAMPLES::

        sage: from sage.interfaces.polymake import reduce_load_Polymake
        sage: reduce_load_Polymake()
        Polymake
    """
Polymake = PolymakeJuPyMake
polymake: Incomplete
polymake_jupymake: Incomplete
