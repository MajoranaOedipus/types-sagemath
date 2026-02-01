"""

Conversion functions for bytes/unicode
"""
from __future__ import annotations
import builtins as __builtins__
import sys as sys
__all__: list[str] = ['encoding', 'sys', 'to_bytes', 'to_string', 'to_unicode']
def to_bytes(s):
    """
    
        Converts bytes and unicode ``s`` to bytes.
    
        Examples:
    
        >>> from cypari2.string_utils import to_bytes
        >>> s1 = to_bytes(b'hello')
        >>> s2 = to_bytes('hello')
        >>> s3 = to_bytes(u'hello')
        >>> type(s1) is type(s2) is type(s3) is bytes
        True
        >>> s1 == s2 == s3 == b'hello'
        True
    
        >>> type(to_bytes(1234)) is bytes
        True
        >>> int(to_bytes(1234))
        1234
        
    """
def to_string(s):
    """
    
        Converts a bytes and unicode ``s`` to a string.
    
        String means bytes in Python2 and unicode in Python3
    
        Examples:
    
        >>> from cypari2.string_utils import to_string
        >>> s1 = to_string(b'hello')
        >>> s2 = to_string('hello')
        >>> s3 = to_string(u'hello')
        >>> type(s1) == type(s2) == type(s3) == str
        True
        >>> s1 == s2 == s3 == 'hello'
        True
        
    """
def to_unicode(s):
    """
    
        Converts bytes and unicode ``s`` to unicode.
    
        Examples:
    
        >>> from cypari2.string_utils import to_unicode
        >>> s1 = to_unicode(b'hello')
        >>> s2 = to_unicode('hello')
        >>> s3 = to_unicode(u'hello')
        >>> type(s1) is type(s2) is type(s3) is type(u"")
        True
        >>> s1 == s2 == s3 == u'hello'
        True
    
        >>> print(to_unicode(1234))
        1234
        >>> type(to_unicode(1234)) is type(u"")
        True
        
    """
__pyx_capi__: dict  # value = {'to_bytes': <capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x792fd7535670>, 'to_unicode': <capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x792fd75356c0>}
__test__: dict = {'to_bytes (line 10)': "\n    Converts bytes and unicode ``s`` to bytes.\n\n    Examples:\n\n    >>> from cypari2.string_utils import to_bytes\n    >>> s1 = to_bytes(b'hello')\n    >>> s2 = to_bytes('hello')\n    >>> s3 = to_bytes(u'hello')\n    >>> type(s1) is type(s2) is type(s3) is bytes\n    True\n    >>> s1 == s2 == s3 == b'hello'\n    True\n\n    >>> type(to_bytes(1234)) is bytes\n    True\n    >>> int(to_bytes(1234))\n    1234\n    ", 'to_unicode (line 41)': '\n    Converts bytes and unicode ``s`` to unicode.\n\n    Examples:\n\n    >>> from cypari2.string_utils import to_unicode\n    >>> s1 = to_unicode(b\'hello\')\n    >>> s2 = to_unicode(\'hello\')\n    >>> s3 = to_unicode(u\'hello\')\n    >>> type(s1) is type(s2) is type(s3) is type(u"")\n    True\n    >>> s1 == s2 == s3 == u\'hello\'\n    True\n\n    >>> print(to_unicode(1234))\n    1234\n    >>> type(to_unicode(1234)) is type(u"")\n    True\n    '}
encoding: str = 'utf-8'
