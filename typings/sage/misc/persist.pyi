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
register_unpickle_override: _cython_3_2_1.cython_function_or_method
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
