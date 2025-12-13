from _typeshed import Incomplete
from sage.typeset.character_art import CharacterArt as CharacterArt
from sage.typeset.character_art_factory import CharacterArtFactory as CharacterArtFactory

class AsciiArt(CharacterArt):
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
        sage: ascii_art(sum(pi^i/factorial(i)*x^i, i, 0, oo))                           # needs sage.symbolic
         pi*x
        e
    """

empty_ascii_art: Incomplete

def ascii_art(*obj, **kwds):
    """
    Return an ASCII art representation.

    INPUT:

    - ``*obj`` -- any number of positional arguments, of arbitrary
      type. The objects whose ascii art representation we want.

    - ``sep`` -- (optional) ``'sep=...'`` keyword argument (or ``'separator'``).
      Anything that can be converted to ascii art (default: empty ascii
      art). The separator in-between a list of objects. Only used if
      more than one object given.

    - ``baseline`` -- (default: 0) the baseline for the object

    - ``sep_baseline`` -- (default: 0) the baseline for the separator

    OUTPUT: :class:`AsciiArt` instance

    EXAMPLES::

        sage: result = ascii_art(integral(exp(x+x^2)/(x+1), x))                         # needs sage.symbolic
        ...
        sage: result                                                                    # needs sage.symbolic
            /
           |
           |   2
           |  x  + x
           | e
           | ------- dx
           |  x + 1
           |
          /

    We can specify a separator object::

        sage: ident = lambda n: identity_matrix(ZZ, n)
        sage: ascii_art(ident(1), ident(2), ident(3), sep=' : ')                        # needs sage.modules
                      [1 0 0]
              [1 0]   [0 1 0]
        [1] : [0 1] : [0 0 1]

    We can specify the baseline::

        sage: ascii_art(ident(2), baseline=-1) + ascii_art(ident(3))                    # needs sage.modules
        [1 0][1 0 0]
        [0 1][0 1 0]
             [0 0 1]

    We can determine the baseline of the separator::

        sage: ascii_art(ident(1), ident(2), ident(3), sep=' -- ', sep_baseline=-1)      # needs sage.modules
                        [1 0 0]
            -- [1 0] -- [0 1 0]
        [1]    [0 1]    [0 0 1]

    If specified, the ``sep_baseline`` overrides the baseline of
    an ascii art separator::

        sage: sep_line = ascii_art('\\n'.join(' | ' for _ in range(6)), baseline=6)
        sage: ascii_art(*Partitions(6), separator=sep_line, sep_baseline=0)             # needs sage.combinat sage.libs.flint
               |       |      |      |     |     |     |    |    |    | *
               |       |      |      |     |     |     |    |    | ** | *
               |       |      |      |     |     | *** |    | ** | *  | *
               |       |      | **** |     | *** | *   | ** | ** | *  | *
               | ***** | **** | *    | *** | **  | *   | ** | *  | *  | *
        ****** | *     | **   | *    | *** | *   | *   | ** | *  | *  | *

    TESTS::

        sage: n = var('n')                                                              # needs sage.symbolic
        sage: ascii_art(sum(binomial(2 * n, n + 1) * x^n, n, 0, oo))                    # needs sage.symbolic
         /        _________    \\\n        -\\2*x + \\/ 1 - 4*x  - 1/
        -------------------------
                   _________
             2*x*\\/ 1 - 4*x
        sage: ascii_art(list(DyckWords(3)))                                             # needs sage.combinat
        [                                   /\\   ]
        [            /\\    /\\      /\\/\\    /  \\  ]
        [ /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ ]
        sage: ascii_art(1)
        1
    """
