r"""
Object persistence

You can load and save most Sage object to disk using the load and
save member functions and commands.

.. NOTE::

   It is impossible to save certain Sage objects to disk. For example,
   if `x` is a MAGMA object, i.e., a wrapper around an object
   that is defined in MAGMA, there is no way to save `x` to
   disk, since MAGMA doesn't support saving of individual objects to
   disk.


-  Versions: Loading and saving of objects is guaranteed to work
   even if the version of Python changes. Saved objects can be loaded
   in future versions of Python. However, if the data structure that
   defines the object, e.g., in Sage code, changes drastically (or
   changes name or disappears), then the object might not load
   correctly or work correctly.

-  Objects are zlib compressed for space efficiency.
"""

import pickle
from sage.misc.sage_unittest import TestSuite as TestSuite
from sage.misc.superseded import deprecation as deprecation
from typing import Any, ClassVar

def load(*filename: str, compress=True, verbose=True, **kwargs) -> Any:
    r"""
    Load Sage object from the file with name filename, which will have
    an ``.sobj`` extension added if it doesn't have one.  Or, if the input
    is a filename ending in ``.py``, ``.pyx``, ``.sage``, ``.spyx``,
    ``.f``, ``.f90`` or ``.m``, load that file into the current running
    session using :func:`sage.repl.load.load`.

    Loaded files are not loaded into their own namespace, i.e., this is
    much more like Python's ``execfile`` than Python's ``import``.

    This function also loads a ``.sobj`` file over a network by
    specifying the full URL.  (Setting ``verbose = False`` suppresses
    the loading progress indicator.)

    When a pickle created with Python 2 is unpickled in Python 3, Sage
    uses the default encoding ``latin1`` to unpickle data of type :class:`str`.

    Finally, if you give multiple positional input arguments, then all
    of those files are loaded, or all of the objects are loaded and a
    list of the corresponding loaded objects is returned.

    If ``compress`` is true (the default), then the data stored in the file
    are supposed to be compressed. If ``verbose`` is true (the default), then
    some logging is printed when accessing remote files. Further keyword
    arguments are passed to :func:`pickle.load`.

    EXAMPLES::

        sage: u = 'https://www.sagemath.org/files/test.sobj'
        sage: s = load(u)                                                  # optional - internet
        Attempting to load remote file: https://www.sagemath.org/files/test.sobj
        Loading started
        Loading ended
        sage: s                                                            # optional - internet
        'hello SageMath'

    We test loading a file or multiple files or even mixing loading files and objects::

        sage: t = tmp_filename(ext='.py')
        sage: with open(t, 'w') as f:
        ....:     _ = f.write("print('hello world')")
        sage: load(t)
        hello world
        sage: load(t,t)
        hello world
        hello world
        sage: t2 = tmp_filename(); save(2/3,t2)
        sage: load(t,t,t2)
        hello world
        hello world
        [None, None, 2/3]

    Files with a ``.sage`` extension are preparsed. Also note that we
    can access global variables::

        sage: t = tmp_filename(ext='.sage')
        sage: with open(t, 'w') as f:
        ....:     _ = f.write("a += Mod(2/3, 11)")  # This evaluates to Mod(8, 11)
        sage: a = -1
        sage: load(t)
        sage: a
        7

    We can load Fortran files::

        sage: code = '      subroutine hello\n         print *, "Hello World!"\n      end subroutine hello\n'
        sage: t = tmp_filename(ext='.F')
        sage: with open(t, 'w') as f:
        ....:     _ = f.write(code)
        sage: load(t)                                                                   # needs numpy
        sage: hello                                                                     # needs numpy
        <fortran ...>

    Path objects are supported::

        sage: from pathlib import Path
        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     p = Path(d) / "test_path"
        ....:     save(1, p)
        ....:     load(p)
        1
    """
def save(obj: object, filename: str, compress=True, **kwargs):
    """
    Save ``obj`` to the file with name ``filename``, which will have an
    ``.sobj`` extension added if it doesn't have one and if ``obj``
    doesn't have its own ``save()`` method, like e.g. Python tuples.

    For image objects and the like (which have their own ``save()`` method),
    you may have to specify a specific extension, e.g. ``.png``, if you
    don't want the object to be saved as a Sage object (or likewise, if
    ``filename`` could be interpreted as already having some extension).

    .. WARNING::

       This will *replace* the contents of the file if it already exists.

    EXAMPLES::

        sage: import tempfile
        sage: d = tempfile.TemporaryDirectory()
        sage: a = matrix(2, [1,2, 3,-5/2])                                              # needs sage.modules
        sage: objfile = os.path.join(d.name, 'test.sobj')
        sage: objfile_short = os.path.join(d.name, 'test')
        sage: save(a, objfile)                                                          # needs sage.modules
        sage: load(objfile_short)                                                       # needs sage.modules
        [   1    2]
        [   3 -5/2]

        sage: # needs sage.plot sage.schemes
        sage: E = EllipticCurve([-1,0])
        sage: P = plot(E)
        sage: save(P, objfile_short)   # saves the plot to "test.sobj"
        sage: save(P, filename=os.path.join(d.name, "sage.png"), xmin=-2)
        sage: save(P, os.path.join(d.name, "filename.with.some.wrong.ext"))
        Traceback (most recent call last):
        ...
        ValueError: allowed file extensions for images are
        '.eps', '.pdf', '.pgf', '.png', '.ps', '.sobj', '.svg'!
        sage: print(load(objfile))
        Graphics object consisting of 2 graphics primitives

        sage: save("A python string", os.path.join(d.name, 'test'))
        sage: load(objfile)
        'A python string'
        sage: load(objfile_short)
        'A python string'
        sage: d.cleanup()

    TESTS:

    Check that :issue:`11577` is fixed::

        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(suffix='.bar') as f:
        ....:     save((1,1), f.name)
        ....:     load(f.name)
        (1, 1)

    Check that Path objects work::

        sage: from pathlib import Path
        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     p = Path(d) / "test_path"
        ....:     save(1, p)
        ....:     load(p)
        1
    """
def dumps(obj: object, compress=True) -> str:
    """
    Dump obj to a string s.  To recover obj, use ``loads(s)``.

    .. SEEALSO:: :func:`loads`

    EXAMPLES::

        sage: a = 2/3
        sage: s = dumps(a)
        sage: a2 = loads(s)
        sage: type(a) is type(a2)
        True
        sage: a2
        2/3
    """

already_pickled: dict
already_unpickled: dict

def register_unpickle_override(module, name: str, callable, call_name=None):
    """
Python pickles include the module and class name of classes.
This means that rearranging the Sage source can invalidate old
pickles.  To keep the old pickles working, you can call
register_unpickle_override with an old module name and class name,
and the Python callable (function, class with __call__ method, etc.)
to use for unpickling.  (If this callable is a value in some module,
you can specify the module name and class name, for the benefit of
:func:`~sage.misc.explain_pickle.explain_pickle` when called with ``in_current_sage=True``).)

EXAMPLES:

Imagine that there used to be an ``old_integer`` module and old
pickles essentially trying to do the following::

    sage: unpickle_global('sage.rings.old_integer', 'OldInteger')
    Traceback (most recent call last):
    ...
    ImportError: cannot import OldInteger from sage.rings.old_integer, call register_unpickle_override('sage.rings.old_integer', 'OldInteger', ...) to fix this

After following the advice from the error message, unpickling
works::

    sage: from sage.misc.persist import register_unpickle_override
    sage: register_unpickle_override('sage.rings.old_integer', 'OldInteger', Integer)
    sage: unpickle_global('sage.rings.old_integer', 'OldInteger')
    <... 'sage.rings.integer.Integer'>

In many cases, unpickling problems for old pickles can be resolved with a
simple call to ``register_unpickle_override``, as in the example above and
in many of the ``sage`` source files.  However, if the underlying data
structure has changed significantly then unpickling may fail and it
will be necessary to explicitly implement unpickling methods for the
associated objects. The python pickle protocol is described in detail on the
web and, in particular, in the `python pickling documentation`_. For example, the
following excerpt from this documentation shows that the unpickling of
classes is controlled by their :meth:`__setstate__` method.

::

    object.__setstate__(state)

        Upon unpickling, if the class also defines the method :meth:`__setstate__`, it is
        called with the unpickled state. If there is no :meth:`__setstate__` method,
        the pickled state must be a dictionary and its items are assigned to the new
        instance's dictionary. If a class defines both :meth:`__getstate__` and
        :meth:`__setstate__`, the state object needn't be a dictionary and these methods
        can do what they want.

.. _python pickling documentation: https://docs.python.org/library/pickle.html#pickle-protocol

By implementing a :meth:`__setstate__` method for a class it should be
possible to fix any unpickling problems for the class. As an example of what
needs to be done, we show how to unpickle a :class:`CombinatorialObject`
object using a class which also inherits from
:class:`~sage.structure.element.Element`. This exact problem often arises
when refactoring old code into the element framework. First we create a
pickle to play with::

    sage: from sage.structure.element import Element
    sage: class SourPickle(CombinatorialObject): pass
    sage: class SweetPickle(CombinatorialObject, Element): pass
    sage: import __main__
    sage: __main__.SourPickle = SourPickle
    sage: __main__.SweetPickle = SweetPickle  # a hack to allow us to pickle command line classes
    sage: gherkin = dumps(SourPickle([1, 2, 3]))

Using :func:`register_unpickle_override` we try to sweeten our pickle, but
we are unable to eat it::

    sage: from sage.misc.persist import register_unpickle_override
    sage: register_unpickle_override('__main__', 'SourPickle', SweetPickle)
    sage: loads(gherkin)
    Traceback (most recent call last):
    ...
    KeyError: 0

The problem is that the ``SweetPickle`` has inherited a
:meth:`~sage.structure.element.Element.__setstate__` method from
:class:`~sage.structure.element.Element` which is not compatible with
unpickling for :class:`CombinatorialObject`. We can fix this by explicitly
defining a new :meth:`__setstate__` method::

    sage: class SweeterPickle(CombinatorialObject, Element):
    ....:     def __setstate__(self, state):
    ....:         # a pickle from CombinatorialObject is just its instance
    ....:         # dictionary
    ....:         if isinstance(state, dict):
    ....:             # this is a fudge: we need an appropriate parent here
    ....:             self._set_parent(Tableaux())
    ....:             self.__dict__ = state
    ....:         else:
    ....:             P, D = state
    ....:             if P is not None:
    ....:                 self._set_parent(P)
    ....:             self.__dict__ = D
    sage: __main__.SweeterPickle = SweeterPickle
    sage: register_unpickle_override('__main__', 'SourPickle', SweeterPickle)
    sage: loads(gherkin)                                                            # needs sage.combinat
    [1, 2, 3]
    sage: loads(dumps(SweeterPickle([1, 2, 3])))  # check that pickles work for SweeterPickle
    [1, 2, 3]

The ``state`` passed to :meth:`__setstate__` will usually be something like
the instance dictionary of the pickled object, however, with some older
classes such as :class:`CombinatorialObject` it will be a tuple. In general,
the ``state`` can be any python object.  ``Sage`` provides a special tool,
:func:`~sage.misc.explain_pickle.explain_pickle`, which can help in figuring
out the contents of an old pickle. Here is a second example.

::

    sage: class A():
    ....:    def __init__(self, value):
    ....:        self.original_attribute = value
    ....:    def __repr__(self):
    ....:        return 'A(%s)' % self.original_attribute
    sage: class B():
    ....:    def __init__(self, value):
    ....:        self.new_attribute = value
    ....:    def __setstate__(self, state):
    ....:        try:
    ....:            self.new_attribute = state['new_attribute']
    ....:        except KeyError:      # an old pickle
    ....:            self.new_attribute = state['original_attribute']
    ....:    def __repr__(self):
    ....:        return 'B(%s)' % self.new_attribute
    sage: import __main__
    sage: # a hack to allow us to pickle command line classes
    sage: __main__.A = A
    sage: __main__.B = B
    sage: A(10)
    A(10)
    sage: loads(dumps(A(10)))
    A(10)
    sage: sage.misc.explain_pickle.explain_pickle(dumps(A(10)))
    pg_A = unpickle_global('__main__', 'A')
    si = unpickle_newobj(pg_A, ())
    pg_make_integer = unpickle_global('sage.rings.integer', 'make_integer')
    unpickle_build(si, {'original_attribute':pg_make_integer('a')})
    si
    sage: from sage.misc.persist import register_unpickle_override
    sage: register_unpickle_override('__main__', 'A', B)
    sage: loads(dumps(A(10)))
    B(10)
    sage: loads(dumps(B(10)))
    B(10)

Pickling for python classes and extension classes, such as cython, is
different -- again this is discussed in the `python pickling
documentation`_. For the unpickling of extension classes you need to write
a :meth:`__reduce__` method which typically returns a tuple ``(f,
args,...)`` such that ``f(*args)`` returns (a copy of) the original object.
The following code snippet is the
:meth:`~sage.rings.integer.Integer.__reduce__` method from
:class:`sage.rings.integer.Integer`.

.. code-block:: cython

    def __reduce__(self):
        'Including the documentation properly causes a doc-test failure so we include it as a comment:'
        #* '''
        #* This is used when pickling integers.
        #*
        #* EXAMPLES::
        #*
        #*     sage: n = 5
        #*     sage: t = n.__reduce__(); t
        #*     (<built-in function make_integer>, ('5',))
        #*     sage: t[0](*t[1])
        #*     5
        #*     sage: loads(dumps(n)) == n
        #*     True
        #* '''
        # This single line below took me HOURS to figure out.
        # It is the *trick* needed to pickle Cython extension types.
        # The trick is that you must put a pure Python function
        # as the first argument, and that function must return
        # the result of unpickling with the argument in the second
        # tuple as input. All kinds of problems happen
        # if we don't do this.
        return sage.rings.integer.make_integer, (self.str(32),)
"""
    ...
def unpickle_global(module, name: str):
    r"""
    Given a module name and a name within that module (typically a class
    name), retrieve the corresponding object.  This normally just looks
    up the name in the module, but it can be overridden by
    register_unpickle_override.  This is used in the Sage unpickling
    mechanism, so if the Sage source code organization changes,
    register_unpickle_override can allow old pickles to continue to work.

    EXAMPLES::

        sage: from sage.misc.persist import unpickle_override, register_unpickle_override
        sage: unpickle_global('sage.rings.integer', 'Integer')
        <class 'sage.rings.integer.Integer'>

    Now we horribly break the pickling system::

        sage: register_unpickle_override('sage.rings.integer', 'Integer', Rational, call_name=('sage.rings.rational', 'Rational'))
        sage: unpickle_global('sage.rings.integer', 'Integer')
        <class 'sage.rings.rational.Rational'>

    and we reach into the internals and put it back::

        sage: del unpickle_override[('sage.rings.integer', 'Integer')]
        sage: unpickle_global('sage.rings.integer', 'Integer')
        <class 'sage.rings.integer.Integer'>

    A meaningful error message with resolution instructions is displayed for
    old pickles that accidentally got broken because a class or entire module
    was moved or renamed::

        sage: unpickle_global('sage.all', 'some_old_class')
        Traceback (most recent call last):
        ...
        ImportError: cannot import some_old_class from sage.all, call
        register_unpickle_override('sage.all', 'some_old_class', ...)
        to fix this

        sage: unpickle_global('sage.some_old_module', 'some_old_class')
        Traceback (most recent call last):
        ...
        ImportError: cannot import some_old_class from sage.some_old_module, call
        register_unpickle_override('sage.some_old_module', 'some_old_class', ...)
        to fix this

    TESTS:

    Test that :func:`register_unpickle_override` calls in lazily imported modules
    are respected::

        sage: unpickle_global('sage.combinat.root_system.type_A', 'ambient_space')      # needs sage.modules
        <class 'sage.combinat.root_system.type_A.AmbientSpace'>
    """

unpickle_override: dict

class SagePickler(_BasePickler):
    '''
        Subclass ``pickle.Pickler`` with Sage-specific default options, and
        built-in support for external object persistence.

        INPUT:

        - ``file_obj`` -- a readable file-like object returning ``bytes`` from
          which the pickle data will be loaded

        - ``persistent_id`` -- callable or None; if given this callable takes a
          single object to be pickled, and returns an "ID" (a key with which to
          restore the object upon unpickling, which may itself be any pickleable
          object).  See the Python documentation on `pickling and unpickling
          external objects`_ for more details.

        - ``py2compat`` -- on Python 3 only, this creates pickles that have a
          better chance of being read on Python 2, by using protocol version 2
          (instead of 4) and fixing up imports of standard library modules and
          types whose names changed between Python 2 and 3.  This is enabled by
          default for the best chances of cross-Python compatibility.

        - Further arguments are passed to :func:`pickle.load`, where in Python-3
          Sage sets the default ``encoding=\'latin1\'``. This is essential to make
          pickles readable in Python-3 that were created in Python-2. See
          :issue:`28444` for details.

        .. _pickling and unpickling external objects: https://docs.python.org/2.7/library/pickle.html#pickling-and-unpickling-external-objects

        EXAMPLES::

            sage: from sage.misc.persist import (
            ....:     unpickle_override, register_unpickle_override, SageUnpickler)
            sage: from sage.rings.integer import make_integer
            sage: from io import BytesIO
            sage: def fake_constructor(x):
            ....:     print("unpickling an Integer")
            ....:     return make_integer(x)
            sage: register_unpickle_override(\'sage.rings.integer\', \'make_integer\',
            ....:                            fake_constructor)
            sage: unp = SageUnpickler(BytesIO(dumps(1, compress=False)))
            sage: unp.load()
            unpickling an Integer
            1
            sage: del unpickle_override[(\'sage.rings.integer\', \'make_integer\')]

        The ``SagePickler`` can also be passed a ``persistent_id`` function::

            sage: table = {1: \'a\', 2: \'b\'}
            sage: # in practice this might be a database or something...
            sage: def load_object_from_table(obj_id):
            ....:     tag, obj_id
            ....:     return table[obj_id]

        TESTS:

        The following is an indirect doctest.
        ::

            sage: class Foo():
            ....:     def __init__(self, s):
            ....:         self.bar = s
            ....:     def __reduce__(self):
            ....:         return Foo, (self.bar,)
            ....:
            sage: import __main__
            sage: __main__.Foo = Foo

        The data that is passed to ``loads`` in the following line was created
        by ``dumps(Foo(\'\\x80\\x07\')`` in Python-2. We demonstrate that it can
        be correctly unpickled in Python-3::

            sage: g = loads(b\'x\\x9ck`J\\x8e\\x8f\\xcfM\\xcc\\xcc\\x8b\\x8f\\xe7r\\xcb\\xcf\\xe7*d\\x0cej`/dj\\r*d\\xd6\\x03\\x00\\x89\\xc5\\x08{\')
            sage: type(g), g.bar
            (<class \'__main__.Foo\'>, \'\\x80\\x07\')

        The following line demonstrates what would happen without :issue:`28444`::

            sage: loads(b\'x\\x9ck`J\\x8e\\x8f\\xcfM\\xcc\\xcc\\x8b\\x8f\\xe7r\\xcb\\xcf\\xe7*d\\x0cej`/dj\\r*d\\xd6\\x03\\x00\\x89\\xc5\\x08{\', encoding=\'ASCII\')
            Traceback (most recent call last):
            ...
            UnicodeDecodeError: \'ascii\' codec can...t decode byte 0x80 in position 0: ordinal not in range(128)
    '''
    @classmethod
    def dumps(cls, obj, **kwargs):
        """
        Equivalent to :func:`pickle.dumps` but using the
        :class:`sage.misc.persist.SagePickler`.

        INPUT:

        - ``obj`` -- the object to pickle

        - ``kwargs`` -- keyword arguments passed to the
          :class:`sage.misc.persist.SagePickler` constructor

        OUTPUT: ``pickle`` -- the pickled object as ``bytes``

        EXAMPLES::

            sage: import pickle
            sage: from sage.misc.persist import SagePickler
            sage: gherkin = SagePickler.dumps(1)
            sage: pickle.loads(gherkin)
            1
        """
    def __init__(self, file_obj, persistent_id=..., py2compat=...):
        """SagePickler.__init__(self, file_obj, persistent_id=None, py2compat=True)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 795)"""

class SageUnpickler(_BaseUnpickler):
    '''
        Subclass ``pickle.Unpickler`` to control how certain objects get unpickled
        (registered overrides, specifically).

        This is only needed in Python 3 and up.  On Python 2 the behavior of the
        ``cPickle`` module is customized differently.

        This class simply overrides ``Unpickler.find_class`` to wrap
        ``sage.misc.persist.unpickle_global``.

        INPUT:

        - ``file_obj`` -- a readable file-like object returning ``bytes`` from
          which the pickle data will be loaded

        - ``persistent_load`` -- callable or None; if given this callable
          implements loading of persistent external objects.  The function
          should take a single argument, the persistent object ID. See the
          Python documentation on `pickling and unpickling external objects`_
          for more details.

        - ``kwargs`` -- additional keyword arguments passed to the
          ``pickle.Unpickler`` constructor

        .. _pickling and unpickling external objects: https://docs.python.org/2.7/library/pickle.html#pickling-and-unpickling-external-objects

        EXAMPLES::

            sage: from sage.misc.persist import (
            ....:     unpickle_override, register_unpickle_override, SageUnpickler)
            sage: from sage.rings.integer import make_integer
            sage: from io import BytesIO
            sage: def fake_constructor(x):
            ....:     print("unpickling an Integer")
            ....:     return make_integer(x)
            sage: register_unpickle_override(\'sage.rings.integer\', \'make_integer\',
            ....:                            fake_constructor)
            sage: unp = SageUnpickler(BytesIO(dumps(1, compress=False)))
            sage: unp.load()
            unpickling an Integer
            1
            sage: del unpickle_override[(\'sage.rings.integer\', \'make_integer\')]

        The ``SageUnpickler`` can also be passed a ``persistent_load`` function::

            sage: table = {1: \'a\', 2: \'b\'}
            sage: # in practice this might be a database or something...
            sage: def load_object_from_table(obj_id):
            ....:     tag, obj_id
            ....:     return table[obj_id]
    '''
    @classmethod
    def loads(cls, data, **kwargs):
        """
        Equivalent to :func:`pickle.loads` but using the
        :class:`sage.misc.persist.SagePickler`.

        INPUT:

        - ``data`` -- the pickle data as ``bytes``

        - ``kwargs`` -- keyword arguments passed to the
          :class:`sage.misc.persist.SageUnpickler` constructor

        OUTPUT: ``obj`` -- the object that was serialized to the given pickle data

        EXAMPLES::

            sage: import pickle
            sage: from sage.misc.persist import SageUnpickler
            sage: gherkin = pickle.dumps(1)
            sage: SageUnpickler.loads(gherkin)
            1
        """

class _BasePickler(pickle.Pickler):
    """
        Provides the Python 3 implementation for
        :class:`sage.misc.persist.SagePickler`.

        This is simpler than the Python 2 case since ``pickle.Pickler`` is a
        modern built-in type which can be easily subclassed to provide new
        functionality.

        See the documentation for that class for tests and examples.
    """
    def __init__(self, file_obj, protocol=None, persistent_id=None, *, fix_imports=True):
        ...

class _BaseUnpickler(pickle.Unpickler):
    """
        Provides the Python 3 implementation for
        :class:`sage.misc.persist.SageUnpickler`.

        This is simpler than the Python 2 case since ``pickle.Unpickler`` is
        a modern built-in type which can be easily subclassed to provide new
        functionality.

        See the documentation for that class for tests and examples.
    """
    def __init__(self, file_obj, persistent_load=None, **kwargs):
        ...
    def find_class(self, module, name):
        """
        The Unpickler uses this class to load module-level objects.
        Contrary to the name, it is used for functions as well as classes.

        (This is equivalent to what was previously called ``find_global``
        which seems like a better name, albeit still somewhat misleading).

        This is just a thin wrapper around
        :func:`sage.misc.persist.unpickle_global`"""
    def persistent_load(self, pid):
        """
        Implement persistent loading with the ``persistent_load`` function
        given at instantiation, if any.  Otherwise raises a
        ``pickle.UnpicklingError`` as in the base class.

        See the documentation for :class:`sage.misc.persist.SageUnpickler`
        for more details."""

def loads(s: str, compress=True, **kwargs):
    r"""
    Recover an object x that has been dumped to a string s
    using ``s = dumps(x)``.

    .. SEEALSO:: :func:`dumps`

    EXAMPLES::

        sage: a = matrix(2, [1,2, 3,-4/3])                                              # needs sage.modules
        sage: s = dumps(a)                                                              # needs sage.modules
        sage: loads(s)                                                                  # needs sage.modules
        [   1    2]
        [   3 -4/3]

    If compress is ``True`` (the default), it will try to decompress
    the data with zlib and with bz2 (in turn); if neither succeeds,
    it will assume the data is actually uncompressed.  If ``compress==False``
    is explicitly specified, then no decompression is attempted.
    Further arguments are passed to python's :func:`pickle.load`.

    ::

        sage: v = [1..10]
        sage: loads(dumps(v, compress=False)) == v
        True
        sage: loads(dumps(v, compress=False), compress=True) == v
        True
        sage: loads(dumps(v, compress=True), compress=False)
        Traceback (most recent call last):
        ...
        UnpicklingError: invalid load key, 'x'.

    The next example demonstrates that Sage strives to avoid data loss
    in the transition from Python-2 to Python-3. The problem is that Python-3
    by default would not be able to unpickle a non-ASCII Python-2 string appearing
    in a pickle. See :issue:`28444` for details.
    ::

        sage: class Foo():
        ....:     def __init__(self, s):
        ....:         self.bar = s
        ....:     def __reduce__(self):
        ....:         return Foo, (self.bar,)
        ....:
        sage: import __main__
        sage: __main__.Foo = Foo

    The data that is passed to ``loads`` in the following line was created
    by ``dumps(Foo('\x80\x07')`` in Python-2.
    ::

        sage: g = loads(b'x\x9ck`J\x8e\x8f\xcfM\xcc\xcc\x8b\x8f\xe7r\xcb\xcf\xe7*d\x0cej`/dj\r*d\xd6\x03\x00\x89\xc5\x08{')
        sage: type(g), g.bar
        (<class '__main__.Foo'>, '\x80\x07')

    The following line demonstrates what would happen without :issue:`28444`::

        sage: loads(b'x\x9ck`J\x8e\x8f\xcfM\xcc\xcc\x8b\x8f\xe7r\xcb\xcf\xe7*d\x0cej`/dj\r*d\xd6\x03\x00\x89\xc5\x08{', encoding='ASCII')
        Traceback (most recent call last):
        ...
        UnicodeDecodeError: 'ascii' codec can...t decode byte 0x80 in position 0: ordinal not in range(128)
    """
def picklejar(obj, dir=None):
    """
    Create pickled sobj of ``obj`` in ``dir``, with name the absolute
    value of the hash of the pickle of obj.  This is used in conjunction
    with :func:`unpickle_all`.

    To use this to test the whole Sage library right now, set the
    environment variable ``SAGE_PICKLE_JAR``, which will make it so
    :func:`dumps` will by default call :func:`picklejar` with the
    default dir.  Once you do that and doctest Sage, you'll find that
    the ``DOT_SAGE/pickle_jar`` directory contains a bunch of
    pickled objects along with corresponding txt descriptions of them.
    Use the :func:`unpickle_all` to see if they unpickle later.

    INPUT:

    - ``obj`` -- a pickleable object

    - ``dir`` -- string or ``None``; if ``None`` then ``dir`` defaults to
      ``DOT_SAGE/pickle_jar``

    EXAMPLES::

        sage: dir = tmp_dir()
        sage: sage.misc.persist.picklejar(1, dir)
        sage: sage.misc.persist.picklejar('test', dir)
        sage: len(os.listdir(dir))   # Two entries (sobj and txt) for each object
        4

    TESTS:

    Test an unaccessible directory::

        sage: import os, sys
        sage: s = os.stat(dir)
        sage: os.chmod(dir, 0o000)
        sage: try:
        ....:     uid = os.getuid()
        ....: except AttributeError:
        ....:     uid = -1
        sage: if uid == 0:
        ....:     print("OK (cannot test this as root)")
        ....: else:
        ....:     try:
        ....:         sage.misc.persist.picklejar(1, dir + '/noaccess')
        ....:     except PermissionError:
        ....:         print("OK (correctly raised PermissionError)")
        ....:     else:
        ....:         print("FAIL (did not raise an exception")
        OK...
        sage: os.chmod(dir, s.st_mode)
    """
    ...
def unpickle_all(target, debug=False, run_test_suite=False):
    """
    Unpickle all ``.sobj`` files in a directory or tar archive.

    INPUT:

    - ``target`` -- string; the name of a directory or of a (possibly
      compressed) tar archive that contains a single directory of
      ``.sobj`` files.  The tar archive can be in any format that
      python's ``tarfile`` module understands; for example,
      ``.tar.gz`` or ``.tar.bz2``.
    - ``debug`` -- boolean (default: ``False``)
      whether to report a stacktrace in case of failure
    - ``run_test_suite`` -- boolean (default: ``False``)
      whether to run ``TestSuite(x).run()`` on the unpickled objects

    OUTPUT:

    Typically, two lines are printed: the first reporting the number
    of successfully unpickled files, and the second reporting the
    number (zero) of failures. If there are failures, however, then a
    list of failed files will be printed before either of those lines,
    and the failure count will of course be nonzero.

    .. WARNING::

       You must only pass trusted data to this function, including tar
       archives. We use the "data" filter from PEP 706 if possible
       while extracting the archive, but even that is not a perfect
       solution.

    EXAMPLES::

        sage: dir = tmp_dir()
        sage: sage.misc.persist.picklejar('hello', dir)
        sage: sage.misc.persist.unpickle_all(dir)
        Successfully unpickled 1 objects.
        Failed to unpickle 0 objects.
    """
def make_None(*args, **kwds) -> None:
    """
    Do nothing and return ``None``. Used for overriding pickles when
    that pickle is no longer needed.

    EXAMPLES::

        sage: from sage.misc.persist import make_None
        sage: print(make_None(42, pi, foo='bar'))                                       # needs sage.symbolic
        None
    """
    return None
def load_sage_object(cls, dic):   # not used
    ...
def load_sage_element(cls, parent, dic_pic):
    ...
def db(name):
    r"""
    Load object with given name from the Sage database. Use x.db(name)
    or db_save(x, name) to save objects to the database.

    The database directory is ``$HOME/.sage/db``.
    """
    ...
def db_save(x, name=None):
    r"""
    Save x to the Sage database.

    The database directory is ``$HOME/.sage/db``.
    """
    ...
