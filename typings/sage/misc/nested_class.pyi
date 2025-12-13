import _cython_3_2_1
from typing import Any, overload

modify_for_nested_pickle: _cython_3_2_1.cython_function_or_method
nested_pickle: _cython_3_2_1.cython_function_or_method

class A1:
    class A2:
        class A3: ...

class CopiedClass:
    """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 369)

        A simple class to test nested_pickle.

        EXAMPLES::

            sage: from sage.misc.nested_class import CopiedClass
            sage: loads(dumps(CopiedClass.NestedClass()))
            <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
            sage: loads(dumps(CopiedClass.NestedSubClass()))
            <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
    """

    class NestedClass:
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 307)

                EXAMPLES::

                    sage: from sage.misc.nested_class import *
                    sage: loads(dumps(MainClass.NestedClass()))
                    <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
        """

        class NestedSubClass:
            """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 316)

                        EXAMPLES::

                            sage: from sage.misc.nested_class import *
                            sage: loads(dumps(MainClass.NestedClass.NestedSubClass()))
                            <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
                            sage: getattr(sage.misc.nested_class, 'MainClass.NestedClass.NestedSubClass')
                            <class 'sage.misc.nested_class.MainClass.NestedClass.NestedSubClass'>
                            sage: MainClass.NestedClass.NestedSubClass.__name__
                            'MainClass.NestedClass.NestedSubClass'
            """
            @overload
            def dummy(self, x, *args, r=..., **kwds) -> Any:
                """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

                File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

                A dummy method to demonstrate the embedding of
                method signature for nested classes.

                TESTS::

                    sage: from sage.misc.nested_class import MainClass
                    sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                    NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                    File: ...sage/misc/nested_class.pyx (starting at line ...)
                    <BLANKLINE>
                                    A dummy method to demonstrate the embedding of
                                    method signature for nested classes.
                    ..."""
            @overload
            def dummy(self, x, *args, r=..., **kwds) -> Any:
                """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

                File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

                A dummy method to demonstrate the embedding of
                method signature for nested classes.

                TESTS::

                    sage: from sage.misc.nested_class import MainClass
                    sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                    NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                    File: ...sage/misc/nested_class.pyx (starting at line ...)
                    <BLANKLINE>
                                    A dummy method to demonstrate the embedding of
                                    method signature for nested classes.
                    ..."""

    class NestedSubClass:
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 316)

                    EXAMPLES::

                        sage: from sage.misc.nested_class import *
                        sage: loads(dumps(MainClass.NestedClass.NestedSubClass()))
                        <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
                        sage: getattr(sage.misc.nested_class, 'MainClass.NestedClass.NestedSubClass')
                        <class 'sage.misc.nested_class.MainClass.NestedClass.NestedSubClass'>
                        sage: MainClass.NestedClass.NestedSubClass.__name__
                        'MainClass.NestedClass.NestedSubClass'
            """
        @overload
        def dummy(self, x, *args, r=..., **kwds) -> Any:
            """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

            File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

            A dummy method to demonstrate the embedding of
            method signature for nested classes.

            TESTS::

                sage: from sage.misc.nested_class import MainClass
                sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                File: ...sage/misc/nested_class.pyx (starting at line ...)
                <BLANKLINE>
                                A dummy method to demonstrate the embedding of
                                method signature for nested classes.
                ..."""
        @overload
        def dummy(self, x, *args, r=..., **kwds) -> Any:
            """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

            File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

            A dummy method to demonstrate the embedding of
            method signature for nested classes.

            TESTS::

                sage: from sage.misc.nested_class import MainClass
                sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                File: ...sage/misc/nested_class.pyx (starting at line ...)
                <BLANKLINE>
                                A dummy method to demonstrate the embedding of
                                method signature for nested classes.
                ..."""

    class SubClass(MainClass):
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 347)

            A simple class to test nested_pickle.

            EXAMPLES::

                sage: from sage.misc.nested_class import SubClass
                sage: loads(dumps(SubClass.NestedClass()))
                <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
                sage: loads(dumps(SubClass()))
                <sage.misc.nested_class.SubClass object at 0x...>
    """

class MainClass:
    """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 296)

        A simple class to test nested_pickle.

        EXAMPLES::

            sage: from sage.misc.nested_class import *
            sage: loads(dumps(MainClass()))
            <sage.misc.nested_class.MainClass object at 0x...>
    """

    class NestedClass:
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 307)

                EXAMPLES::

                    sage: from sage.misc.nested_class import *
                    sage: loads(dumps(MainClass.NestedClass()))
                    <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
        """

        class NestedSubClass:
            """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 316)

                        EXAMPLES::

                            sage: from sage.misc.nested_class import *
                            sage: loads(dumps(MainClass.NestedClass.NestedSubClass()))
                            <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
                            sage: getattr(sage.misc.nested_class, 'MainClass.NestedClass.NestedSubClass')
                            <class 'sage.misc.nested_class.MainClass.NestedClass.NestedSubClass'>
                            sage: MainClass.NestedClass.NestedSubClass.__name__
                            'MainClass.NestedClass.NestedSubClass'
            """
            @overload
            def dummy(self, x, *args, r=..., **kwds) -> Any:
                """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

                File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

                A dummy method to demonstrate the embedding of
                method signature for nested classes.

                TESTS::

                    sage: from sage.misc.nested_class import MainClass
                    sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                    NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                    File: ...sage/misc/nested_class.pyx (starting at line ...)
                    <BLANKLINE>
                                    A dummy method to demonstrate the embedding of
                                    method signature for nested classes.
                    ..."""
            @overload
            def dummy(self, x, *args, r=..., **kwds) -> Any:
                """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

                File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

                A dummy method to demonstrate the embedding of
                method signature for nested classes.

                TESTS::

                    sage: from sage.misc.nested_class import MainClass
                    sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                    NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                    File: ...sage/misc/nested_class.pyx (starting at line ...)
                    <BLANKLINE>
                                    A dummy method to demonstrate the embedding of
                                    method signature for nested classes.
                    ..."""

class MainClass.NestedClass:
    """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 307)

            EXAMPLES::

                sage: from sage.misc.nested_class import *
                sage: loads(dumps(MainClass.NestedClass()))
                <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
        """

    class NestedSubClass:
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 316)

                    EXAMPLES::

                        sage: from sage.misc.nested_class import *
                        sage: loads(dumps(MainClass.NestedClass.NestedSubClass()))
                        <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
                        sage: getattr(sage.misc.nested_class, 'MainClass.NestedClass.NestedSubClass')
                        <class 'sage.misc.nested_class.MainClass.NestedClass.NestedSubClass'>
                        sage: MainClass.NestedClass.NestedSubClass.__name__
                        'MainClass.NestedClass.NestedSubClass'
            """
        @overload
        def dummy(self, x, *args, r=..., **kwds) -> Any:
            """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

            File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

            A dummy method to demonstrate the embedding of
            method signature for nested classes.

            TESTS::

                sage: from sage.misc.nested_class import MainClass
                sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                File: ...sage/misc/nested_class.pyx (starting at line ...)
                <BLANKLINE>
                                A dummy method to demonstrate the embedding of
                                method signature for nested classes.
                ..."""
        @overload
        def dummy(self, x, *args, r=..., **kwds) -> Any:
            """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

            File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

            A dummy method to demonstrate the embedding of
            method signature for nested classes.

            TESTS::

                sage: from sage.misc.nested_class import MainClass
                sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
                NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
                File: ...sage/misc/nested_class.pyx (starting at line ...)
                <BLANKLINE>
                                A dummy method to demonstrate the embedding of
                                method signature for nested classes.
                ..."""

class MainClass.NestedClass.NestedSubClass:
    """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 316)

                EXAMPLES::

                    sage: from sage.misc.nested_class import *
                    sage: loads(dumps(MainClass.NestedClass.NestedSubClass()))
                    <sage.misc.nested_class.MainClass.NestedClass.NestedSubClass object at 0x...>
                    sage: getattr(sage.misc.nested_class, 'MainClass.NestedClass.NestedSubClass')
                    <class 'sage.misc.nested_class.MainClass.NestedClass.NestedSubClass'>
                    sage: MainClass.NestedClass.NestedSubClass.__name__
                    'MainClass.NestedClass.NestedSubClass'
            """
    @overload
    def dummy(self, x, *args, r=..., **kwds) -> Any:
        """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

        A dummy method to demonstrate the embedding of
        method signature for nested classes.

        TESTS::

            sage: from sage.misc.nested_class import MainClass
            sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
            NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
            File: ...sage/misc/nested_class.pyx (starting at line ...)
            <BLANKLINE>
                            A dummy method to demonstrate the embedding of
                            method signature for nested classes.
            ..."""
    @overload
    def dummy(self, x, *args, r=..., **kwds) -> Any:
        """NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)

        File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 328)

        A dummy method to demonstrate the embedding of
        method signature for nested classes.

        TESTS::

            sage: from sage.misc.nested_class import MainClass
            sage: print(MainClass.NestedClass.NestedSubClass.dummy.__doc__)
            NestedSubClass.dummy(self, x, *args, r=(1, 2, 3.4), **kwds)
            File: ...sage/misc/nested_class.pyx (starting at line ...)
            <BLANKLINE>
                            A dummy method to demonstrate the embedding of
                            method signature for nested classes.
            ..."""

class NestedClassMetaclass(type):
    """NestedClassMetaclass(*args)

    File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 260)

    A metaclass for nested pickling.

    Check that one can use a metaclass to ensure nested_pickle is called on any
    derived subclass::

        sage: from sage.misc.nested_class import NestedClassMetaclass
        sage: class ASuperClass(object, metaclass=NestedClassMetaclass):
        ....:     pass
        sage: class A3(ASuperClass):
        ....:     class B():
        ....:         pass
        sage: A3.B.__name__
        'A3.B'
        sage: getattr(sys.modules['__main__'], 'A3.B', 'Not found')
        <class '__main__.A3.B'>"""
    def __init__(self, *args) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 278)

                This invokes the nested_pickle on construction.

                EXAMPLES::

                    sage: from sage.misc.nested_class import NestedClassMetaclass
                    sage: class A(object, metaclass=NestedClassMetaclass):
                    ....:     class B():
                    ....:         pass
                    sage: A.B
                    <class '__main__.A.B'>
                    sage: getattr(sys.modules['__main__'], 'A.B', 'Not found')
                    <class '__main__.A.B'>
        """

class SubClass(MainClass):
    """File: /build/sagemath/src/sage/src/sage/misc/nested_class.pyx (starting at line 347)

        A simple class to test nested_pickle.

        EXAMPLES::

            sage: from sage.misc.nested_class import SubClass
            sage: loads(dumps(SubClass.NestedClass()))
            <sage.misc.nested_class.MainClass.NestedClass object at 0x...>
            sage: loads(dumps(SubClass()))
            <sage.misc.nested_class.SubClass object at 0x...>
    """
