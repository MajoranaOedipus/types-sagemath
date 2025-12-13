import sage.misc.lazy_import
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.misc.persist import dumps as dumps, load as load, loads as loads, make_None as make_None, register_unpickle_override as register_unpickle_override, save as save, unpickle_all as unpickle_all, unpickle_global as unpickle_global
from typing import Any, overload

unpickle_override: sage.misc.lazy_import.LazyImport

class SageObject:
    """File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 36)

        Base class for all (user-visible) objects in Sage

        Every object that can end up being returned to the user should
        inherit from :class:`SageObject`.

        .. automethod:: _ascii_art_
        .. automethod:: _cache_key
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def category(self) -> Any:
        """SageObject.category(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 514)"""
    def dump(self, filename, compress=...) -> Any:
        """SageObject.dump(self, filename, compress=True)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 475)

        Same as self.save(filename, compress)"""
    @overload
    def dumps(self, compress=...) -> Any:
        """SageObject.dumps(self, compress=True)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 481)

        Dump ``self`` to a string ``s``, which can later be reconstituted
        as ``self`` using ``loads(s)``.

        There is an optional boolean argument ``compress`` which defaults to ``True``.

        EXAMPLES::

            sage: from sage.misc.persist import comp
            sage: O = SageObject()
            sage: p_comp = O.dumps()
            sage: p_uncomp = O.dumps(compress=False)
            sage: comp.decompress(p_comp) == p_uncomp
            True
            sage: import pickletools
            sage: pickletools.dis(p_uncomp)
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.structure.sage_object SageObject'
               41: q    BINPUT     ...
               43: )    EMPTY_TUPLE
               44: \\x81 NEWOBJ
               45: q    BINPUT     ...
               47: .    STOP
            highest protocol among opcodes = 2"""
    @overload
    def dumps(self) -> Any:
        """SageObject.dumps(self, compress=True)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 481)

        Dump ``self`` to a string ``s``, which can later be reconstituted
        as ``self`` using ``loads(s)``.

        There is an optional boolean argument ``compress`` which defaults to ``True``.

        EXAMPLES::

            sage: from sage.misc.persist import comp
            sage: O = SageObject()
            sage: p_comp = O.dumps()
            sage: p_uncomp = O.dumps(compress=False)
            sage: comp.decompress(p_comp) == p_uncomp
            True
            sage: import pickletools
            sage: pickletools.dis(p_uncomp)
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.structure.sage_object SageObject'
               41: q    BINPUT     ...
               43: )    EMPTY_TUPLE
               44: \\x81 NEWOBJ
               45: q    BINPUT     ...
               47: .    STOP
            highest protocol among opcodes = 2"""
    @overload
    def dumps(self, compress=...) -> Any:
        """SageObject.dumps(self, compress=True)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 481)

        Dump ``self`` to a string ``s``, which can later be reconstituted
        as ``self`` using ``loads(s)``.

        There is an optional boolean argument ``compress`` which defaults to ``True``.

        EXAMPLES::

            sage: from sage.misc.persist import comp
            sage: O = SageObject()
            sage: p_comp = O.dumps()
            sage: p_uncomp = O.dumps(compress=False)
            sage: comp.decompress(p_comp) == p_uncomp
            True
            sage: import pickletools
            sage: pickletools.dis(p_uncomp)
                0: \\x80 PROTO      2
                2: c    GLOBAL     'sage.structure.sage_object SageObject'
               41: q    BINPUT     ...
               43: )    EMPTY_TUPLE
               44: \\x81 NEWOBJ
               45: q    BINPUT     ...
               47: .    STOP
            highest protocol among opcodes = 2"""
    @overload
    def get_custom_name(self) -> Any:
        """SageObject.get_custom_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 150)

        Return the custom name of this object, or ``None`` if it is not
        renamed.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P.get_custom_name() is None
            True
            sage: P.rename('A polynomial ring')
            sage: P.get_custom_name()
            'A polynomial ring'
            sage: P.reset_name()
            sage: P.get_custom_name() is None
            True"""
    @overload
    def get_custom_name(self) -> Any:
        """SageObject.get_custom_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 150)

        Return the custom name of this object, or ``None`` if it is not
        renamed.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P.get_custom_name() is None
            True
            sage: P.rename('A polynomial ring')
            sage: P.get_custom_name()
            'A polynomial ring'
            sage: P.reset_name()
            sage: P.get_custom_name() is None
            True"""
    @overload
    def get_custom_name(self) -> Any:
        """SageObject.get_custom_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 150)

        Return the custom name of this object, or ``None`` if it is not
        renamed.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P.get_custom_name() is None
            True
            sage: P.rename('A polynomial ring')
            sage: P.get_custom_name()
            'A polynomial ring'
            sage: P.reset_name()
            sage: P.get_custom_name() is None
            True"""
    @overload
    def get_custom_name(self) -> Any:
        """SageObject.get_custom_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 150)

        Return the custom name of this object, or ``None`` if it is not
        renamed.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P.get_custom_name() is None
            True
            sage: P.rename('A polynomial ring')
            sage: P.get_custom_name()
            'A polynomial ring'
            sage: P.reset_name()
            sage: P.get_custom_name() is None
            True"""
    @overload
    def parent(self) -> Any:
        """SageObject.parent(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 549)

        Return the type of ``self`` to support the coercion framework.

        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t                            # needs sage.symbolic
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: u = t.maxima_methods()                                                # needs sage.symbolic
            sage: u.parent()                                                            # needs sage.symbolic
            <class 'sage.symbolic.maxima_wrapper.MaximaWrapper'>"""
    @overload
    def parent(self) -> Any:
        """SageObject.parent(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 549)

        Return the type of ``self`` to support the coercion framework.

        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t                            # needs sage.symbolic
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: u = t.maxima_methods()                                                # needs sage.symbolic
            sage: u.parent()                                                            # needs sage.symbolic
            <class 'sage.symbolic.maxima_wrapper.MaximaWrapper'>"""
    @overload
    def rename(self, x=...) -> Any:
        """SageObject.rename(self, x=None)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 68)

        Change ``self`` so it prints as x, where x is a string.

        If x is ``None``, the existing custom name is removed.

        .. NOTE::

           This is *only* supported for Python classes that derive
           from SageObject.

        EXAMPLES::

            sage: x = PolynomialRing(QQ, 'x', sparse=True).gen()
            sage: g = x^3 + x - 5
            sage: g
            x^3 + x - 5
            sage: g.rename('a polynomial')
            sage: g
            a polynomial
            sage: g + x
            x^3 + 2*x - 5
            sage: h = g^100
            sage: str(h)[:20]
            'x^300 + 100*x^298 - '
            sage: h.rename('x^300 + ...')
            sage: h
            x^300 + ...
            sage: g.rename(None)
            sage: g
            x^3 + x - 5

        Real numbers are not Python classes, so rename is not supported::

            sage: a = 3.14
            sage: type(a)                                                               # needs sage.rings.real_mpfr
            <... 'sage.rings.real_mpfr.RealLiteral'>
            sage: a.rename('pi')                                                        # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            NotImplementedError: object does not support renaming: 3.14000000000000

        .. NOTE::

           The reason C-extension types are not supported by default
           is if they were then every single one would have to carry
           around an extra attribute, which would be slower and waste
           a lot of memory.

           To support them for a specific class, add a
           ``cdef public _SageObject__custom_name`` attribute."""
    @overload
    def rename(self, _None) -> Any:
        """SageObject.rename(self, x=None)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 68)

        Change ``self`` so it prints as x, where x is a string.

        If x is ``None``, the existing custom name is removed.

        .. NOTE::

           This is *only* supported for Python classes that derive
           from SageObject.

        EXAMPLES::

            sage: x = PolynomialRing(QQ, 'x', sparse=True).gen()
            sage: g = x^3 + x - 5
            sage: g
            x^3 + x - 5
            sage: g.rename('a polynomial')
            sage: g
            a polynomial
            sage: g + x
            x^3 + 2*x - 5
            sage: h = g^100
            sage: str(h)[:20]
            'x^300 + 100*x^298 - '
            sage: h.rename('x^300 + ...')
            sage: h
            x^300 + ...
            sage: g.rename(None)
            sage: g
            x^3 + x - 5

        Real numbers are not Python classes, so rename is not supported::

            sage: a = 3.14
            sage: type(a)                                                               # needs sage.rings.real_mpfr
            <... 'sage.rings.real_mpfr.RealLiteral'>
            sage: a.rename('pi')                                                        # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            NotImplementedError: object does not support renaming: 3.14000000000000

        .. NOTE::

           The reason C-extension types are not supported by default
           is if they were then every single one would have to carry
           around an extra attribute, which would be slower and waste
           a lot of memory.

           To support them for a specific class, add a
           ``cdef public _SageObject__custom_name`` attribute."""
    @overload
    def reset_name(self) -> Any:
        """SageObject.reset_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 131)

        Remove the custom name of an object.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P
            Univariate Polynomial Ring in x over Rational Field
            sage: P.rename('A polynomial ring')
            sage: P
            A polynomial ring
            sage: P.reset_name()
            sage: P
            Univariate Polynomial Ring in x over Rational Field"""
    @overload
    def reset_name(self) -> Any:
        """SageObject.reset_name(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 131)

        Remove the custom name of an object.

        EXAMPLES::

            sage: P.<x> = QQ[]
            sage: P
            Univariate Polynomial Ring in x over Rational Field
            sage: P.rename('A polynomial ring')
            sage: P
            A polynomial ring
            sage: P.reset_name()
            sage: P
            Univariate Polynomial Ring in x over Rational Field"""
    def save(self, filename=..., compress=...) -> Any:
        '''SageObject.save(self, filename=None, compress=True)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 446)

        Save ``self`` to the given filename.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x = SR.var("x")
            sage: f = x^3 + 5
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(suffix=\'.sobj\') as t:
            ....:     f.save(t.name)
            ....:     load(t.name)
            x^3 + 5'''
    def __hash__(self) -> Any:
        """SageObject.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 363)

        Not implemented: mutable objects inherit from this class.

        EXAMPLES::

            sage: hash(SageObject())
            Traceback (most recent call last):
            ...
            TypeError: <... 'sage.structure.sage_object.SageObject'> is not hashable"""
    def __pari__(self) -> Any:
        """SageObject.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/structure/sage_object.pyx (starting at line 969)"""
