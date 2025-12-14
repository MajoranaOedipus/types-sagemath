import _cython_3_2_1
import _pickle
from sage.misc.sage_unittest import TestSuite as TestSuite
from sage.misc.superseded import deprecation as deprecation
from typing import Any, ClassVar

already_pickled: dict
already_unpickled: dict
db: _cython_3_2_1.cython_function_or_method
db_save: _cython_3_2_1.cython_function_or_method
dumps: _cython_3_2_1.cython_function_or_method
load: _cython_3_2_1.cython_function_or_method
load_sage_element: _cython_3_2_1.cython_function_or_method
load_sage_object: _cython_3_2_1.cython_function_or_method
loads: _cython_3_2_1.cython_function_or_method
make_None: _cython_3_2_1.cython_function_or_method
picklejar: _cython_3_2_1.cython_function_or_method

def register_unpickle_override(module, name, callable, call_name=None):
    """register_unpickle_override(module, name, callable, call_name=None)

File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 349)

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

save: _cython_3_2_1.cython_function_or_method
unpickle_all: _cython_3_2_1.cython_function_or_method
unpickle_global: _cython_3_2_1.cython_function_or_method
unpickle_override: dict

class SagePickler(_BasePickler):
    '''File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 711)

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
    dumps: ClassVar[method] = ...
    def __init__(self, file_obj, persistent_id=..., py2compat=...) -> Any:
        """SagePickler.__init__(self, file_obj, persistent_id=None, py2compat=True)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 795)"""

class SageUnpickler(_BaseUnpickler):
    '''File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 835)

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
    loads: ClassVar[method] = ...

class _BasePickler(_pickle.Pickler):
    """File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 617)

        Provides the Python 3 implementation for
        :class:`sage.misc.persist.SagePickler`.

        This is simpler than the Python 2 case since ``pickle.Pickler`` is a
        modern built-in type which can be easily subclassed to provide new
        functionality.

        See the documentation for that class for tests and examples.
    """
    def __init__(self, file_obj, protocol=..., persistent_id=..., fix_imports=...) -> Any:
        """_BasePickler.__init__(self, file_obj, protocol=None, persistent_id=None, *, fix_imports=True)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 629)"""

class _BaseUnpickler(_pickle.Unpickler):
    """File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 656)

        Provides the Python 3 implementation for
        :class:`sage.misc.persist.SageUnpickler`.

        This is simpler than the Python 2 case since ``pickle.Unpickler`` is
        a modern built-in type which can be easily subclassed to provide new
        functionality.

        See the documentation for that class for tests and examples.
    """
    def __init__(self, file_obj, persistent_load=..., **kwargs) -> Any:
        """_BaseUnpickler.__init__(self, file_obj, persistent_load=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 668)"""
    def find_class(self, module, name) -> Any:
        """_BaseUnpickler.find_class(self, module, name)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 688)

        The Unpickler uses this class to load module-level objects.
        Contrary to the name, it is used for functions as well as classes.

        (This is equivalent to what was previously called ``find_global``
        which seems like a better name, albeit still somewhat misleading).

        This is just a thin wrapper around
        :func:`sage.misc.persist.unpickle_global`"""
    def persistent_load(self, pid) -> Any:
        """_BaseUnpickler.persistent_load(self, pid)

        File: /build/sagemath/src/sage/src/sage/misc/persist.pyx (starting at line 673)

        Implement persistent loading with the ``persistent_load`` function
        given at instantiation, if any.  Otherwise raises a
        ``pickle.UnpicklingError`` as in the base class.

        See the documentation for :class:`sage.misc.persist.SageUnpickler`
        for more details."""
