"""
Cython interface to Cremona's ``eclib`` library (also known as ``mwrank``)

EXAMPLES::

    sage: from sage.libs.eclib.mwrank import _Curvedata, _mw
    sage: c = _Curvedata(1,2,3,4,5)

    sage: print(c)
    [1,2,3,4,5]
    b2 = 9       b4 = 11         b6 = 29         b8 = 35
    c4 = -183           c6 = -3429
    disc = -10351       (# real components = 1)
    #torsion not yet computed

    sage: t= _mw(c)
    sage: t.search(10)
    sage: t
    [[1:2:1]]
"""

from typings_sagemath import Int
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.integer import Integer as Integer

FS_ENCODING: str
def get_precision() -> int:
    """
    Return the working floating point bit precision of mwrank, which is
    equal to the global NTL real number precision.

    OUTPUT: integer; the current precision in bits

    See also :meth:`set_precision`.

    EXAMPLES::

        sage: mwrank_get_precision()
        150
    """
    ...
def initprimes(filename: str, verb: bool = False) -> None:
    """
    Initialises mwrank/eclib's internal prime list.

    INPUT:

    - ``filename`` -- string; the name of a file of primes

    - ``verb`` -- boolean (default: ``False``); verbose or not

    EXAMPLES::

        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(mode='w+t') as f:
        ....:     data = ' '.join(str(p) for p in prime_range(10^7, 10^7 + 20))
        ....:     _ = f.write(data)
        ....:     f.flush()
        ....:     mwrank_initprimes(f.name, verb=True)
        Computed 78519 primes, largest is 1000253
        reading primes from file ...
        read extra prime 10000019
        finished reading primes from file ...
        Extra primes in list: 10000019

        sage: mwrank_initprimes(f.name, True)
        Traceback (most recent call last):
        ...
        OSError: No such file or directory: ...
    """
def parse_point_list(s: str) -> list[list[Integer]]:
    r"""
    Parse a string representing a list of points.

    INPUT:

    - ``s`` -- string representation of a list of points; for
      example '[]', '[[1:2:3]]', or '[[1:2:3],[4:5:6]]'

    OUTPUT: list of triples of integers, for example [], [[1,2,3]],
    [[1,2,3],[4,5,6]]

    EXAMPLES::

        sage: from sage.libs.eclib.mwrank import parse_point_list
        sage: parse_point_list('[]')
        []
        sage: parse_point_list('[[1:2:3]]')
        [[1, 2, 3]]
        sage: parse_point_list('[[1:2:3],[4:5:6]]')
        [[1, 2, 3], [4, 5, 6]]
    """
def set_precision(n: Int) -> None:
    """
    Set the working floating point bit precision of mwrank, which is
    equal to the global NTL real number precision.

    NTL real number bit precision.  This has a massive effect on the
    speed of mwrank calculations.  The default (used if this function is
    not called) is ``n=150``, but it might have to be increased if a
    computation fails.

    INPUT:

    - ``n`` -- positive integer; the number of bits of precision

    .. warning::

       This change is global and affects *all* future calls of eclib
       functions by Sage.

    .. NOTE::

        The minimal value to which the precision may be set is 53.
        Lower values will be increased to 53.

    See also :meth:`get_precision`.

    EXAMPLES::

        sage: from sage.libs.eclib.mwrank import set_precision, get_precision
        sage: old_prec = get_precision(); old_prec
        150
        sage: set_precision(50)
        sage: get_precision()
        53
        sage: set_precision(old_prec)
        sage: get_precision()
        150
    """

