import _cython_3_2_1
from typing import Any, overload

instancedoc: _cython_3_2_1.cython_function_or_method

class InstanceDocDescriptor:
    '''InstanceDocDescriptor(classdoc, instancedoc, attr=\'__doc__\')

    File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 133)

    Descriptor for dynamic documentation, to be installed as the
    ``__doc__`` attribute.

    INPUT:

    - ``classdoc`` -- string; class documentation

    - ``instancedoc`` -- (method) documentation for an instance

    - ``attr`` -- string (default: ``__doc__``); attribute name to use
      for custom docstring on the instance

    EXAMPLES::

        sage: from sage.misc.instancedoc import InstanceDocDescriptor
        sage: def instancedoc(self):
        ....:     return "Instance doc"
        sage: docattr = InstanceDocDescriptor("Class doc", instancedoc)
        sage: class Z():
        ....:     __doc__ = InstanceDocDescriptor("Class doc", instancedoc)
        sage: Z.__doc__
        \'Class doc\'
        sage: Z().__doc__
        \'Instance doc\'

    We can still override the ``__doc__`` attribute of the instance::

        sage: obj = Z()
        sage: obj.__doc__ = "Custom doc"
        sage: obj.__doc__
        \'Custom doc\'
        sage: del obj.__doc__
        sage: obj.__doc__
        \'Instance doc\''''
    def __init__(self, classdoc, instancedoc, attr=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 174)

                TESTS::

                    sage: from sage.misc.instancedoc import InstanceDocDescriptor
                    sage: InstanceDocDescriptor(None, None)
                    <sage.misc.instancedoc.InstanceDocDescriptor object at ...>
        """
    @overload
    def __delete__(self, obj) -> Any:
        '''InstanceDocDescriptor.__delete__(self, obj)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 243)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: class X(): pass
            sage: obj = X()
            sage: obj.__doc__ = "Custom doc"
            sage: descr.__delete__(obj)
            sage: print(obj.__doc__)
            None
            sage: descr.__delete__(obj)
            Traceback (most recent call last):
            ...
            AttributeError: \'X\' object has no attribute \'__doc__\'...

            sage: descr.__delete__([])
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'list\' objects is not writable
            sage: descr.__delete__(object)
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'type\' objects is not writable'''
    @overload
    def __delete__(self, obj) -> Any:
        '''InstanceDocDescriptor.__delete__(self, obj)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 243)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: class X(): pass
            sage: obj = X()
            sage: obj.__doc__ = "Custom doc"
            sage: descr.__delete__(obj)
            sage: print(obj.__doc__)
            None
            sage: descr.__delete__(obj)
            Traceback (most recent call last):
            ...
            AttributeError: \'X\' object has no attribute \'__doc__\'...

            sage: descr.__delete__([])
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'list\' objects is not writable
            sage: descr.__delete__(object)
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'type\' objects is not writable'''
    @overload
    def __delete__(self, obj) -> Any:
        '''InstanceDocDescriptor.__delete__(self, obj)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 243)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: class X(): pass
            sage: obj = X()
            sage: obj.__doc__ = "Custom doc"
            sage: descr.__delete__(obj)
            sage: print(obj.__doc__)
            None
            sage: descr.__delete__(obj)
            Traceback (most recent call last):
            ...
            AttributeError: \'X\' object has no attribute \'__doc__\'...

            sage: descr.__delete__([])
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'list\' objects is not writable
            sage: descr.__delete__(object)
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'type\' objects is not writable'''
    @overload
    def __delete__(self, object) -> Any:
        '''InstanceDocDescriptor.__delete__(self, obj)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 243)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: class X(): pass
            sage: obj = X()
            sage: obj.__doc__ = "Custom doc"
            sage: descr.__delete__(obj)
            sage: print(obj.__doc__)
            None
            sage: descr.__delete__(obj)
            Traceback (most recent call last):
            ...
            AttributeError: \'X\' object has no attribute \'__doc__\'...

            sage: descr.__delete__([])
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'list\' objects is not writable
            sage: descr.__delete__(object)
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'type\' objects is not writable'''
    @overload
    def __get__(self, obj, typ) -> Any:
        '''InstanceDocDescriptor.__get__(self, obj, typ)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 186)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: descr.__get__(None, object)
            \'Class doc\'
            sage: descr.__get__(42, type(42))
            \'Doc for 42\''''
    @overload
    def __get__(self, _None, object) -> Any:
        '''InstanceDocDescriptor.__get__(self, obj, typ)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 186)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: descr.__get__(None, object)
            \'Class doc\'
            sage: descr.__get__(42, type(42))
            \'Doc for 42\''''
    def __set__(self, obj, value) -> Any:
        '''InstanceDocDescriptor.__set__(self, obj, value)

        File: /build/sagemath/src/sage/src/sage/misc/instancedoc.pyx (starting at line 215)

        TESTS::

            sage: from sage.misc.instancedoc import InstanceDocDescriptor
            sage: def instancedoc(self):
            ....:     return "Doc for {!r}".format(self)
            sage: descr = InstanceDocDescriptor("Class doc", instancedoc)
            sage: class X(): pass
            sage: obj = X()
            sage: descr.__set__(obj, "Custom doc")
            sage: obj.__doc__
            \'Custom doc\'

            sage: descr.__set__([], "Custom doc")
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'list\' objects is not writable
            sage: descr.__set__(object, "Custom doc")
            Traceback (most recent call last):
            ...
            AttributeError: attribute \'__doc__\' of \'type\' objects is not writable'''
