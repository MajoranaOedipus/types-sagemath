import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ecl_eval: _cython_3_2_1.cython_function_or_method
init_ecl: _cython_3_2_1.cython_function_or_method
print_objects: _cython_3_2_1.cython_function_or_method
shutdown_ecl: _cython_3_2_1.cython_function_or_method
test_ecl_options: _cython_3_2_1.cython_function_or_method
test_sigint_before_ecl_sig_on: _cython_3_2_1.cython_function_or_method

class EclListIterator:
    '''EclListIterator(EclObject o)

    File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1241)

    Iterator object for an ECL list

    This class is used to implement the iterator protocol for EclObject.
    Do not instantiate this class directly but use the iterator method
    on an EclObject instead. It is an error if the EclObject is not a list.

    EXAMPLES::

        sage: from sage.libs.ecl import *
        sage: I=EclListIterator(EclObject("(1 2 3)"))
        sage: type(I)
        <class \'sage.libs.ecl.EclListIterator\'>
        sage: [i for i in I]
        [<ECL: 1>, <ECL: 2>, <ECL: 3>]
        sage: [i for i in EclObject("(1 2 3)")]
        [<ECL: 1>, <ECL: 2>, <ECL: 3>]
        sage: EclListIterator(EclObject("1"))
        Traceback (most recent call last):
        ...
        TypeError: ECL object is not iterable'''
    def __init__(self, EclObjecto) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1266)

                Initialize EclListIterator.

                EXAMPLES::

                    sage: from sage.libs.ecl import *
                    sage: I=EclListIterator(EclObject("(1 2 3)"))
                    sage: type(I)
                    <class \'sage.libs.ecl.EclListIterator\'>
        '''
    @overload
    def __iter__(self) -> Any:
        '''EclListIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1281)

        Return ``self``.

        It seems standard that iterators return themselves if asked to produce
        an iterator.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: I=EclListIterator(EclObject("(1 2 3)"))
            sage: id(I) == id(I.__iter__())
            True'''
    @overload
    def __iter__(self) -> Any:
        '''EclListIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1281)

        Return ``self``.

        It seems standard that iterators return themselves if asked to produce
        an iterator.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: I=EclListIterator(EclObject("(1 2 3)"))
            sage: id(I) == id(I.__iter__())
            True'''
    def __next__(self) -> Any:
        '''EclListIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1297)

        Get next element from iterator.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: I=EclListIterator(EclObject("(1 2 3)"))
            sage: next(I)
            <ECL: 1>
            sage: next(I)
            <ECL: 2>
            sage: next(I)
            <ECL: 3>
            sage: next(I)
            Traceback (most recent call last):
            ...
            StopIteration'''

class EclObject:
    '''EclObject(*args)

    File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 540)

    Python wrapper of ECL objects

    The ``EclObject`` forms a wrapper around ECL objects. The wrapper ensures
    that the data structure pointed to is protected from garbage collection in
    ECL by installing a pointer to it from a global data structure within the
    scope of the ECL garbage collector. This pointer is destroyed upon
    destruction of the EclObject.

    EclObject() takes a Python object and tries to find a representation of it
    in Lisp.

    EXAMPLES:

    Python lists get mapped to LISP lists. None and Boolean values to
    appropriate values in LISP::

        sage: from sage.libs.ecl import *
        sage: EclObject([None,true,false])
        <ECL: (NIL T NIL)>

    Numerical values are translated to the appropriate type in LISP::

        sage: EclObject(1)
        <ECL: 1>
        sage: EclObject(10**40)
        <ECL: 10000000000000000000000000000000000000000>

    Floats in Python are IEEE double, which LISP has as well. However,
    the printing of floating point types in LISP depends on settings::

        sage: a = EclObject(float(1.234e40))
        sage: ecl_eval("(setf *read-default-float-format* \'single-float)")
        <ECL: SINGLE-FLOAT>
        sage: a
        <ECL: 1.234d40>
        sage: ecl_eval("(setf *read-default-float-format* \'double-float)")
        <ECL: DOUBLE-FLOAT>
        sage: a
        <ECL: 1.234e40>

    Tuples are translated to dotted lists::

        sage: EclObject( (false, true))
        <ECL: (NIL . T)>
        sage: EclObject( (1, 2, 3) )
        <ECL: (1 2 . 3)>

    Strings are fed to the reader, so a string normally results in a symbol::

        sage: EclObject("Symbol")
        <ECL: SYMBOL>

    But with proper quotation one can construct a lisp string object too::

        sage: EclObject(\'"Symbol"\')
        <ECL: "Symbol">

    Or any other object that the Lisp reader can construct::

        sage: EclObject(\'#("I" am "just" a "simple" vector)\')
        <ECL: #("I" AM "just" A "simple" VECTOR)>

    By means of Lisp reader macros, you can include arbitrary objects::

        sage: EclObject([ 1, 2, \'\'\'#.(make-hash-table :test #\'equal)\'\'\', 4])
        <ECL: (1 2 #<hash-table ...> 4)>

    Using an optional argument, you can control how strings are handled::

        sage: EclObject("String", False)
        <ECL: "String">
        sage: EclObject(\'#(I may look like a vector but I am a string)\', False)
        <ECL: "#(I may look like a vector but I am a string)">

    This also affects strings within nested lists and tuples ::

        sage: EclObject([1, 2, "String", 4], False)
        <ECL: (1 2 "String" 4)>

    EclObjects translate to themselves, so one can mix::

        sage: EclObject([1,2, EclObject([3])])
        <ECL: (1 2 (3))>

    Calling an EclObject translates into the appropriate LISP ``apply``,
    where the argument is transformed into an EclObject itself, so one can
    flexibly apply LISP functions::

        sage: car = EclObject("car")
        sage: cdr = EclObject("cdr")
        sage: car(cdr([1,2,3]))
        <ECL: 2>

    and even construct and evaluate arbitrary S-expressions::

        sage: eval=EclObject("eval")
        sage: quote=EclObject("quote")
        sage: eval([car, [cdr, [quote,[1,2,3]]]])
        <ECL: 2>

    TESTS:

    We check that multiprecision integers are converted correctly::

        sage: i = 10 ^ (10 ^ 5)
        sage: EclObject(i) == EclObject(str(i))
        True
        sage: EclObject(-i) == EclObject(str(-i))
        True
        sage: EclObject(i).python() == i
        True
        sage: EclObject(-i).python() == -i
        True

    We check that symbols with Unicode names are converted correctly::

        sage: EclObject(\'λ\')
        <ECL: Λ>
        sage: EclObject(\'|λ|\')
        <ECL: |λ|>

    We check that Unicode strings are converted correctly::

        sage: EclObject(\'"Mαξιμα"\')
        <ECL: "Mαξιμα">'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, *args) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 679)

                Create an EclObject.

                See EclObject for full documentation.

                EXAMPLES::

                    sage: from sage.libs.ecl import *
                    sage: EclObject([None,true,false])
                    <ECL: (NIL T NIL)>
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 679)

                Create an EclObject.

                See EclObject for full documentation.

                EXAMPLES::

                    sage: from sage.libs.ecl import *
                    sage: EclObject([None,true,false])
                    <ECL: (NIL T NIL)>
        """
    @overload
    def atomp(self) -> Any:
        """EclObject.atomp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1213)

        Return ``True`` if ``self`` is atomic, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).atomp()
            True
            sage: EclObject([[]]).atomp()
            False"""
    @overload
    def atomp(self) -> Any:
        """EclObject.atomp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1213)

        Return ``True`` if ``self`` is atomic, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).atomp()
            True
            sage: EclObject([[]]).atomp()
            False"""
    @overload
    def atomp(self) -> Any:
        """EclObject.atomp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1213)

        Return ``True`` if ``self`` is atomic, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).atomp()
            True
            sage: EclObject([[]]).atomp()
            False"""
    @overload
    def caar(self) -> Any:
        """EclObject.caar(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1043)

        Return the caar of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def caar(self) -> Any:
        """EclObject.caar(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1043)

        Return the caar of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cadr(self) -> Any:
        """EclObject.cadr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1068)

        Return the cadr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cadr(self) -> Any:
        """EclObject.cadr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1068)

        Return the cadr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def car(self) -> Any:
        """EclObject.car(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 993)

        Return the car of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def car(self) -> Any:
        """EclObject.car(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 993)

        Return the car of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cdar(self) -> Any:
        """EclObject.cdar(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1093)

        Return the cdar of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cdar(self) -> Any:
        """EclObject.cdar(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1093)

        Return the cdar of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cddr(self) -> Any:
        """EclObject.cddr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1118)

        Return the cddr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cddr(self) -> Any:
        """EclObject.cddr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1118)

        Return the cddr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cdr(self) -> Any:
        """EclObject.cdr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1018)

        Return the cdr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def cdr(self) -> Any:
        """EclObject.cdr(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1018)

        Return the cdr of ``self``.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([[1,2],[3,4]])
            sage: L.car()
            <ECL: (1 2)>
            sage: L.cdr()
            <ECL: ((3 4))>
            sage: L.caar()
            <ECL: 1>
            sage: L.cadr()
            <ECL: (3 4)>
            sage: L.cdar()
            <ECL: (2)>
            sage: L.cddr()
            <ECL: NIL>"""
    @overload
    def characterp(self) -> Any:
        '''EclObject.characterp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1157)

        Return ``True`` if ``self`` is a character, ``False`` otherwise.

        Strings are not characters

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject(\'"a"\').characterp()
            False'''
    @overload
    def characterp(self) -> Any:
        '''EclObject.characterp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1157)

        Return ``True`` if ``self`` is a character, ``False`` otherwise.

        Strings are not characters

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject(\'"a"\').characterp()
            False'''
    @overload
    def cons(self, EclObjectd) -> Any:
        """EclObject.cons(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 941)

        Apply cons to ``self`` and argument and return the result.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: a=EclObject(1)
            sage: b=EclObject(2)
            sage: a.cons(b)
            <ECL: (1 . 2)>"""
    @overload
    def cons(self, b) -> Any:
        """EclObject.cons(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 941)

        Apply cons to ``self`` and argument and return the result.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: a=EclObject(1)
            sage: b=EclObject(2)
            sage: a.cons(b)
            <ECL: (1 . 2)>"""
    @overload
    def consp(self) -> Any:
        """EclObject.consp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1199)

        Return ``True`` if ``self`` is a cons, ``False`` otherwise. NIL is not a cons.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).consp()
            False
            sage: EclObject([[]]).consp()
            True"""
    @overload
    def consp(self) -> Any:
        """EclObject.consp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1199)

        Return ``True`` if ``self`` is a cons, ``False`` otherwise. NIL is not a cons.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).consp()
            False
            sage: EclObject([[]]).consp()
            True"""
    @overload
    def consp(self) -> Any:
        """EclObject.consp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1199)

        Return ``True`` if ``self`` is a cons, ``False`` otherwise. NIL is not a cons.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).consp()
            False
            sage: EclObject([[]]).consp()
            True"""
    @overload
    def eval(self) -> Any:
        '''EclObject.eval(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 922)

        Evaluate object as an S-Expression.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: S=EclObject("(+ 1 2)")
            sage: S
            <ECL: (+ 1 2)>
            sage: S.eval()
            <ECL: 3>'''
    @overload
    def eval(self) -> Any:
        '''EclObject.eval(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 922)

        Evaluate object as an S-Expression.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: S=EclObject("(+ 1 2)")
            sage: S
            <ECL: (+ 1 2)>
            sage: S.eval()
            <ECL: 3>'''
    @overload
    def fixnump(self) -> Any:
        """EclObject.fixnump(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1143)

        Return ``True`` if ``self`` is a fixnum, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject(2**3).fixnump()
            True
            sage: EclObject(2**200).fixnump()
            False"""
    @overload
    def fixnump(self) -> Any:
        """EclObject.fixnump(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1143)

        Return ``True`` if ``self`` is a fixnum, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject(2**3).fixnump()
            True
            sage: EclObject(2**200).fixnump()
            False"""
    @overload
    def fixnump(self) -> Any:
        """EclObject.fixnump(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1143)

        Return ``True`` if ``self`` is a fixnum, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject(2**3).fixnump()
            True
            sage: EclObject(2**200).fixnump()
            False"""
    @overload
    def listp(self) -> Any:
        """EclObject.listp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1185)

        Return ``True`` if ``self`` is a list, ``False`` otherwise. NIL is a list.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).listp()
            True
            sage: EclObject([[]]).listp()
            True"""
    @overload
    def listp(self) -> Any:
        """EclObject.listp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1185)

        Return ``True`` if ``self`` is a list, ``False`` otherwise. NIL is a list.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).listp()
            True
            sage: EclObject([[]]).listp()
            True"""
    @overload
    def listp(self) -> Any:
        """EclObject.listp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1185)

        Return ``True`` if ``self`` is a list, ``False`` otherwise. NIL is a list.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).listp()
            True
            sage: EclObject([[]]).listp()
            True"""
    @overload
    def nullp(self) -> Any:
        """EclObject.nullp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1171)

        Return ``True`` if ``self`` is NIL, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).nullp()
            True
            sage: EclObject([[]]).nullp()
            False"""
    @overload
    def nullp(self) -> Any:
        """EclObject.nullp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1171)

        Return ``True`` if ``self`` is NIL, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).nullp()
            True
            sage: EclObject([[]]).nullp()
            False"""
    @overload
    def nullp(self) -> Any:
        """EclObject.nullp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1171)

        Return ``True`` if ``self`` is NIL, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).nullp()
            True
            sage: EclObject([[]]).nullp()
            False"""
    @overload
    def python(self) -> Any:
        '''EclObject.python(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 724)

        Convert an EclObject to a python object.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L = EclObject([1,2,("three",\'"four"\')])
            sage: L.python()
            [1, 2, (\'THREE\', \'"four"\')]'''
    @overload
    def python(self) -> Any:
        '''EclObject.python(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 724)

        Convert an EclObject to a python object.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L = EclObject([1,2,("three",\'"four"\')])
            sage: L.python()
            [1, 2, (\'THREE\', \'"four"\')]'''
    @overload
    def rplaca(self, EclObjectd) -> Any:
        """EclObject.rplaca(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 955)

        Destructively replace car(self) with d.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject((1,2))
            sage: L
            <ECL: (1 . 2)>
            sage: a=EclObject(3)
            sage: L.rplaca(a)
            sage: L
            <ECL: (3 . 2)>"""
    @overload
    def rplaca(self, a) -> Any:
        """EclObject.rplaca(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 955)

        Destructively replace car(self) with d.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject((1,2))
            sage: L
            <ECL: (1 . 2)>
            sage: a=EclObject(3)
            sage: L.rplaca(a)
            sage: L
            <ECL: (3 . 2)>"""
    @overload
    def rplacd(self, EclObjectd) -> Any:
        """EclObject.rplacd(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 974)

        Destructively replace cdr(self) with d.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject((1,2))
            sage: L
            <ECL: (1 . 2)>
            sage: a=EclObject(3)
            sage: L.rplacd(a)
            sage: L
            <ECL: (1 . 3)>"""
    @overload
    def rplacd(self, a) -> Any:
        """EclObject.rplacd(self, EclObject d)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 974)

        Destructively replace cdr(self) with d.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject((1,2))
            sage: L
            <ECL: (1 . 2)>
            sage: a=EclObject(3)
            sage: L.rplacd(a)
            sage: L
            <ECL: (1 . 3)>"""
    @overload
    def symbolp(self) -> Any:
        """EclObject.symbolp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1227)

        Return ``True`` if ``self`` is a symbol, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).symbolp()
            True
            sage: EclObject([[]]).symbolp()
            False"""
    @overload
    def symbolp(self) -> Any:
        """EclObject.symbolp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1227)

        Return ``True`` if ``self`` is a symbol, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).symbolp()
            True
            sage: EclObject([[]]).symbolp()
            False"""
    @overload
    def symbolp(self) -> Any:
        """EclObject.symbolp(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 1227)

        Return ``True`` if ``self`` is a symbol, ``False`` otherwise.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: EclObject([]).symbolp()
            True
            sage: EclObject([[]]).symbolp()
            False"""
    def __call__(self, *args) -> Any:
        '''EclObject.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 816)

        Apply ``self`` to arguments.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: sqr=EclObject("(lambda (x) (* x x))").eval()
            sage: sqr(10)
            <ECL: 100>'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """EclObject.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 787)

        Return a hash value of the object.

        Returns the hash value returned by SXHASH, which is a routine that is
        specified in Common Lisp. According to the specification, lisp objects that
        are EQUAL have the same SXHASH value. Since two EclObjects are equal if
        their wrapped objects are EQUAL according to lisp, this is compatible with
        Python's concept of hash values.

        It is not possible to enforce immutability of lisp objects, so care should
        be taken in using EclObjects as dictionary keys.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: L=EclObject([1,2])
            sage: L
            <ECL: (1 2)>
            sage: hash(L) #random
            463816586
            sage: L.rplacd(EclObject(3))
            sage: L
            <ECL: (1 . 3)>
            sage: hash(L) #random
            140404060"""
    def __iter__(self) -> Any:
        '''EclObject.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 870)

        Implement the iterator protocol for EclObject.

        EclObject implements the iterator protocol for lists. This means
        one can use an EclObject in the context where an iterator is
        expected (for instance, in a list comprehension or in a for loop).
        The iterator produces EclObjects wrapping the members of the list that
        the original EclObject wraps.

        The wrappers returned are all newly constructed but refer to the
        original members of the list iterated over. This is usually what is
        intended but, just as in Python, can cause surprises if the original
        object is changed between calls to the iterator.

        Since EclObject translates Python Lists into LISP lists and Python
        tuples into LISP "dotted" lists (lists for which the final CDR is not
        necessarily NIL), and both these python structures are iterable, the
        corresponding EclObjects are iterable as well.

        EclObjects that are not lists are not iterable.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: [i for i in EclObject("(1 2 3)")]
            [<ECL: 1>, <ECL: 2>, <ECL: 3>]
            sage: [i for i in EclObject("(1 2 . 3)")]
            [<ECL: 1>, <ECL: 2>, <ECL: 3>]
            sage: [i for i in EclObject("NIL")]
            []

        TESTS:

        These show that Python lists and tuples behave as
        described above::

            sage: [i for i in EclObject([1,2,3])]
            [<ECL: 1>, <ECL: 2>, <ECL: 3>]
            sage: [i for i in EclObject((1,2,3))]
            [<ECL: 1>, <ECL: 2>, <ECL: 3>]

        This tests that we cannot iterate EclObjects we shouldn\'t,
        as described above::

            sage: [i for i in EclObject("T")]
            Traceback (most recent call last):
            ...
            TypeError: ECL object is not iterable'''
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    @overload
    def __reduce__(self) -> Any:
        """EclObject.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 700)

        This is used for pickling. Not implemented.

        Ecl does not natively support serialization of its objects, so the
        python wrapper class EclObject does not support pickling. There are
        independent efforts for developing serialization for Common Lisp, such as
        CL-STORE. Look at those if you need serialization of ECL objects.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: s=EclObject([1,2,3])
            sage: s.__reduce__()
            Traceback (most recent call last):
            ...
            NotImplementedError: EclObjects do not have a pickling method
            sage: s==loads(dumps(s))
            Traceback (most recent call last):
            ...
            NotImplementedError: EclObjects do not have a pickling method"""
    @overload
    def __reduce__(self) -> Any:
        """EclObject.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ecl.pyx (starting at line 700)

        This is used for pickling. Not implemented.

        Ecl does not natively support serialization of its objects, so the
        python wrapper class EclObject does not support pickling. There are
        independent efforts for developing serialization for Common Lisp, such as
        CL-STORE. Look at those if you need serialization of ECL objects.

        EXAMPLES::

            sage: from sage.libs.ecl import *
            sage: s=EclObject([1,2,3])
            sage: s.__reduce__()
            Traceback (most recent call last):
            ...
            NotImplementedError: EclObjects do not have a pickling method
            sage: s==loads(dumps(s))
            Traceback (most recent call last):
            ...
            NotImplementedError: EclObjects do not have a pickling method"""
