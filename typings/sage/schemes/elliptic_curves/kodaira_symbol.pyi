from sage.rings.integer import Integer as Integer
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class KodairaSymbol_class(SageObject):
    """
    Class to hold a Kodaira symbol of an elliptic curve over a
    `p`-adic local field.

    Users should use the ``KodairaSymbol()`` function to construct
    Kodaira Symbols rather than use the class constructor directly.
    """
    def __init__(self, symbol) -> None:
        """
        Constructor for Kodaira Symbol class.

        INPUT:

        - ``symbol`` -- string or integer; the string should be a
          standard string representation (e.g. III*) of a Kodaira
          symbol, which will be parsed.  Alternatively, use the PARI
          encoding of Kodaira symbols as integers.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.kodaira_symbol import KodairaSymbol_class
            sage: KodairaSymbol_class(14)
            I10
            sage: KodairaSymbol_class('III*')
            III*
            sage: latex(KodairaSymbol_class('In'))
            I_n
            sage: KodairaSymbol_class('In')
            In

        Check that :issue:`31147` is fixed::

            sage: latex(KodairaSymbol_class(-14))
            I_{10}^{*}
        """
    def __richcmp__(self, other, op):
        """
        Standard comparison function for Kodaira Symbols.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.kodaira_symbol import KodairaSymbol_class
            sage: KS1 = KodairaSymbol_class(15); KS1
            I11
            sage: KS2 = KodairaSymbol_class(-34); KS2
            I30*
            sage: KS1 < KS2
            True
            sage: KS2 < KS1
            False

        ::

            sage: Klist = [KodairaSymbol_class(i) for i in [-10..10] if i!=0]
            sage: Klist.sort()
            sage: Klist
            [I0,
            I0*,
            I1,
            I1*,
            I2,
            I2*,
            I3,
            I3*,
            I4,
            I4*,
            I5,
            I5*,
            I6,
            I6*,
            II,
            II*,
            III,
            III*,
            IV,
            IV*]
        """

def KodairaSymbol(symbol):
    '''
    Return the specified Kodaira symbol.

    INPUT:

    - ``symbol`` -- string or integer; either a string of the form
      "I0", "I1", ..., "In", "II", "III", "IV", "I0*", "I1*", ..., "In*", "II*", "III*", or "IV*",
      or an integer encoding a Kodaira symbol using PARI\'s conventions

    OUTPUT:

    (KodairaSymbol)  The corresponding Kodaira symbol.

    EXAMPLES::

        sage: KS = KodairaSymbol
        sage: [KS(n) for n in range(1,10)]
        [I0, II, III, IV, I1, I2, I3, I4, I5]
        sage: [KS(-n) for n in range(1,10)]
        [I0*, II*, III*, IV*, I1*, I2*, I3*, I4*, I5*]
        sage: all(KS(str(KS(n))) == KS(n) for n in range(-10,10) if n != 0)
        True
    '''
