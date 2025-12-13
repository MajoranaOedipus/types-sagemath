import re
from _typeshed import Incomplete
from sage.doctest.marked_output import MarkedOutput as MarkedOutput
from sage.doctest.rif_tol import RIFtol as RIFtol, add_tolerance as add_tolerance

float_without_sign: str
float_regex: Incomplete

class ToleranceExceededError(BaseException): ...

def check_tolerance_real_domain(want: MarkedOutput, got: str) -> tuple[str, str]:
    """
    Compare want and got over real domain with tolerance

    INPUT:

    - ``want`` -- a string, what you want
    - ``got`` -- a string, what you got

    OUTPUT:

    The strings to compare, but with matching float numbers replaced by asterisk.

    EXAMPLES::

        sage: from sage.doctest.check_tolerance import check_tolerance_real_domain
        sage: from sage.doctest.marked_output import MarkedOutput
        sage: check_tolerance_real_domain(
        ....:     MarkedOutput('foo:0.2').update(abs_tol=0.3),
        ....:     'bar:0.4')
        ['foo:*', 'bar:*']
        sage: check_tolerance_real_domain(
        ....:     MarkedOutput('foo:0.2').update(abs_tol=0.3),
        ....:     'bar:0.6')
        Traceback (most recent call last):
        ...
        sage.doctest.check_tolerance.ToleranceExceededError
    """

real_plus_optional_imag: Incomplete
only_imag: Incomplete
imaginary_unit: str
complex_regex: Incomplete

def complex_match_to_real_and_imag(m: re.Match) -> tuple[str, str]:
    """
    Extract real and imaginary part from match

    INPUT:

    - ``m`` -- match from ``complex_regex``

    OUTPUT:

    Pair of real and complex parts (as string)

    EXAMPLES::

        sage: from sage.doctest.check_tolerance import complex_match_to_real_and_imag, complex_regex
        sage: complex_match_to_real_and_imag(complex_regex.match('1.0'))
        ('1.0', '0')
        sage: complex_match_to_real_and_imag(complex_regex.match('-1.0 - I'))
        ('-1.0', '-1')
        sage: complex_match_to_real_and_imag(complex_regex.match('1.0 - 3.0*I'))
        ('1.0', '- 3.0')
        sage: complex_match_to_real_and_imag(complex_regex.match('1.0*I'))
        ('0', '1.0')
        sage: complex_match_to_real_and_imag(complex_regex.match('- 2.0*I'))
        ('0', '- 2.0')
        sage: complex_match_to_real_and_imag(complex_regex.match('-I'))
        ('0', '-1')
        sage: for match in complex_regex.finditer('[1, -1, I, -1, -I]'):
        ....:     print(complex_match_to_real_and_imag(match))
        ('1', '0')
        ('-1', '0')
        ('0', '1')
        ('-1', '0')
        ('0', '-1')
        sage: for match in complex_regex.finditer('[1, -1.3, -1.5 + 0.1*I, 0.5 - 0.1*I, -1.5*I]'):
        ....:     print(complex_match_to_real_and_imag(match))
        ('1', '0')
        ('-1.3', '0')
        ('-1.5', '+ 0.1')
        ('0.5', '- 0.1')
        ('0', '-1.5')
    """
def complex_star_repl(m: re.Match):
    """
    Replace the complex number in the match with '*'
    """
def check_tolerance_complex_domain(want: MarkedOutput, got: str) -> tuple[str, str]:
    """
    Compare want and got over complex domain with tolerance

    INPUT:

    - ``want`` -- a string, what you want
    - ``got`` -- a string, what you got

    OUTPUT:

    The strings to compare, but with matching complex numbers replaced by asterisk.

    EXAMPLES::

        sage: from sage.doctest.check_tolerance import check_tolerance_complex_domain
        sage: from sage.doctest.marked_output import MarkedOutput
        sage: check_tolerance_complex_domain(
        ....:     MarkedOutput('foo:[0.2 + 0.1*I]').update(abs_tol=0.3),
        ....:     'bar:[0.4]')
        ['foo:[*]', 'bar:[*]']
        sage: check_tolerance_complex_domain(
        ....:     MarkedOutput('foo:-0.5 - 0.1*I').update(abs_tol=2),
        ....:     'bar:1')
        ['foo:*', 'bar:*']
        sage: check_tolerance_complex_domain(
        ....:     MarkedOutput('foo:[1.0*I]').update(abs_tol=0.3),
        ....:     'bar:[I]')
        ['foo:[*]', 'bar:[*]']
        sage: check_tolerance_complex_domain(MarkedOutput('foo:0.2 + 0.1*I').update(abs_tol=0.3), 'bar:0.6')
        Traceback (most recent call last):
        ...
        sage.doctest.check_tolerance.ToleranceExceededError
    """
