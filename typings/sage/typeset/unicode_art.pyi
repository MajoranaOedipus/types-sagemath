from _typeshed import Incomplete
from sage.typeset.character_art import CharacterArt as CharacterArt
from sage.typeset.character_art_factory import CharacterArtFactory as CharacterArtFactory

class UnicodeArt(CharacterArt):
    """
    An Ascii art object is an object with some specific representation for
    *printing*.

    INPUT:

    - ``lines`` -- the list of lines of the representation of the ascii art
      object

    - ``breakpoints`` -- the list of points where the representation can be
      split

    - ``baseline`` -- the reference line (from the bottom)

    EXAMPLES::

        sage: i = var('i')                                                              # needs sage.symbolic
        sage: unicode_art(sum(pi^i/factorial(i)*x^i, i, 0, oo))                         # needs sage.symbolic
         π⋅x
        ℯ
    """

empty_unicode_art: Incomplete

def unicode_art(*obj, **kwds):
    """
    Return an unicode art representation.

    INPUT:

    - ``*obj`` -- any number of positional arguments, of arbitrary
      type. The objects whose ascii art representation we want.

    - ``sep`` -- (optional) ``'sep=...'`` keyword argument (or ``'separator'``).
      Anything that can be converted to unicode art (default: empty unicode
      art). The separator in-between a list of objects. Only used if
      more than one object given.

    - ``baseline`` -- (default: 0) the baseline for the object

    - ``sep_baseline`` -- (default: 0) the baseline for the separator

    OUTPUT: :class:`UnicodeArt` instance

    EXAMPLES::

        sage: result = unicode_art(integral(exp(sqrt(x))/(x+pi), x))                    # needs sage.symbolic
        ...
        sage: result                                                                    # needs sage.symbolic
            ⌠
            ⎮   √x
            ⎮  ℯ
            ⎮ ───── dx
            ⎮ x + π
            ⌡
        sage: ident = lambda n: identity_matrix(ZZ, n)
        sage: unicode_art(ident(1), ident(2), ident(3), sep=' : ')                      # needs sage.modules
                      ⎛1 0 0⎞
              ⎛1 0⎞   ⎜0 1 0⎟
        (1) : ⎝0 1⎠ : ⎝0 0 1⎠

    If specified, the ``sep_baseline`` overrides the baseline of
    an unicode art separator::

        sage: sep_line = unicode_art('\\n'.join(' ⎟ ' for _ in range(5)), baseline=5)
        sage: unicode_art(*AlternatingSignMatrices(3),                                  # needs sage.combinat sage.modules
        ....:             separator=sep_line, sep_baseline=1)
                ⎟         ⎟         ⎟            ⎟         ⎟         ⎟
        ⎛1 0 0⎞ ⎟ ⎛0 1 0⎞ ⎟ ⎛1 0 0⎞ ⎟ ⎛ 0  1  0⎞ ⎟ ⎛0 0 1⎞ ⎟ ⎛0 1 0⎞ ⎟ ⎛0 0 1⎞
        ⎜0 1 0⎟ ⎟ ⎜1 0 0⎟ ⎟ ⎜0 0 1⎟ ⎟ ⎜ 1 -1  1⎟ ⎟ ⎜1 0 0⎟ ⎟ ⎜0 0 1⎟ ⎟ ⎜0 1 0⎟
        ⎝0 0 1⎠ ⎟ ⎝0 0 1⎠ ⎟ ⎝0 1 0⎠ ⎟ ⎝ 0  1  0⎠ ⎟ ⎝0 1 0⎠ ⎟ ⎝1 0 0⎠ ⎟ ⎝1 0 0⎠
                ⎟         ⎟         ⎟            ⎟         ⎟         ⎟

    TESTS::

        sage: n = var('n')                                                              # needs sage.symbolic
        sage: unicode_art(sum(binomial(2 * n, n + 1) * x^n, n, 0, oo))                  # needs sage.symbolic
         ⎛        _________    ⎞
        -⎝2⋅x + ╲╱ 1 - 4⋅x  - 1⎠
        ─────────────────────────
                   _________
             2⋅x⋅╲╱ 1 - 4⋅x
        sage: unicode_art(list(DyckWords(3)))                                           # needs sage.combinat
        ⎡                                   ╱╲   ⎤
        ⎢            ╱╲    ╱╲      ╱╲╱╲    ╱  ╲  ⎥
        ⎣ ╱╲╱╲╱╲, ╱╲╱  ╲, ╱  ╲╱╲, ╱    ╲, ╱    ╲ ⎦
        sage: unicode_art(1)
        1
    """
def unicode_superscript(x):
    """
    Return the rational number ``x`` as a superscript.

    EXAMPLES::

        sage: from sage.typeset.unicode_art import unicode_superscript
        sage: unicode_superscript(15123902)
        '¹⁵¹²³⁹⁰²'
        sage: unicode_superscript(-712/5)
        '⁻⁷¹²ᐟ⁵'
    """
def unicode_subscript(x):
    """
    Return the integer ``x`` as a superscript.

    EXAMPLES::

        sage: from sage.typeset.unicode_art import unicode_subscript
        sage: unicode_subscript(15123902)
        '₁₅₁₂₃₉₀₂'
        sage: unicode_subscript(-712)
        '₋₇₁₂'
    """
