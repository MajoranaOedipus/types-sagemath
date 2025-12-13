from _typeshed import Incomplete
from collections.abc import MutableMapping

colors_dict: Incomplete

def mod_one(x):
    """
    Reduce a number modulo 1.

    INPUT:

    - ``x`` -- an instance of Integer, int, RealNumber, etc.; the
      number to reduce

    OUTPUT: float

    EXAMPLES::

        sage: from sage.plot.colors import mod_one
        sage: mod_one(1)
        1.0
        sage: mod_one(7.0)
        0.0
        sage: mod_one(-11/7)
        0.4285714285714286
        sage: mod_one(pi) + mod_one(-pi)                                                # needs sage.symbolic
        1.0
    """
def html_to_float(c):
    """
    Convert a HTML hex color to a Red-Green-Blue (RGB) tuple.

    INPUT:

    - ``c`` -- string; a valid HTML hex color

    OUTPUT: a RGB 3-tuple of floats in the interval [0.0, 1.0]

    EXAMPLES::

        sage: from sage.plot.colors import html_to_float
        sage: html_to_float('#fff')
        (1.0, 1.0, 1.0)
        sage: html_to_float('#abcdef')
        (0.6705882352941176, 0.803921568627451, 0.9372549019607843)
        sage: html_to_float('#123xyz')
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for int() with base 16: '3x'
    """
def rgbcolor(c, space: str = 'rgb'):
    """
    Convert a color (string, tuple, list, or :class:`Color`) to a
    mod-one reduced (see :func:`mod_one`) valid Red-Green-Blue (RGB)
    tuple.  The returned tuple is also a valid matplotlib RGB color.

    INPUT:

    - ``c`` -- a :class:`Color` instance, string (name or HTML hex),
      3-tuple, or 3-list; the color to convert

    - ``space`` -- string (default: ``'rgb'``); the color space
      coordinate system (other choices are ``'hsl'``, ``'hls'``, and ``'hsv'``)
      in which to interpret a 3-tuple or 3-list

    OUTPUT: a RGB 3-tuple of floats in the interval [0.0, 1.0]

    EXAMPLES::

        sage: from sage.plot.colors import rgbcolor
        sage: rgbcolor(Color(0.25, 0.4, 0.9))
        (0.25, 0.4, 0.9)
        sage: rgbcolor('purple')
        (0.5019607843137255, 0.0, 0.5019607843137255)
        sage: rgbcolor('#fa0')
        (1.0, 0.6666666666666666, 0.0)
        sage: rgbcolor('#ffffff')
        (1.0, 1.0, 1.0)
        sage: rgbcolor((1,1/2,1/3))
        (1.0, 0.5, 0.3333333333333333)
        sage: rgbcolor([1,1/2,1/3])
        (1.0, 0.5, 0.3333333333333333)
        sage: rgbcolor((1,1,1), space='hsv')
        (1.0, 0.0, 0.0)
        sage: rgbcolor((0.5,0.75,1), space='hls')
        (0.5, 0.9999999999999999, 1.0)
        sage: rgbcolor((0.5,1.0,0.75), space='hsl')
        (0.5, 0.9999999999999999, 1.0)
        sage: rgbcolor([1,2,255])   # WARNING -- numbers are reduced mod 1!!
        (1.0, 0.0, 0.0)
        sage: rgbcolor('#abcd')
        Traceback (most recent call last):
        ...
        ValueError: color hex string (= 'abcd') must have length 3 or 6
        sage: rgbcolor('fff')
        Traceback (most recent call last):
        ...
        ValueError: unknown color 'fff'
        sage: rgbcolor(1)
        Traceback (most recent call last):
        ...
        TypeError: '1' must be a Color, list, tuple, or string
        sage: rgbcolor((0.2,0.8,1), space='grassmann')
        Traceback (most recent call last):
        ...
        ValueError: space must be one of 'rgb', 'hsv', 'hsl', 'hls'
        sage: rgbcolor([0.4, 0.1])
        Traceback (most recent call last):
        ...
        ValueError: color list or tuple '[0.400000000000000, 0.100000000000000]' must have 3 entries, one for each RGB, HSV, HLS, or HSL channel
    """
to_mpl_color = rgbcolor

class Color:
    def __init__(self, r: str = '#0000ff', g=None, b=None, space: str = 'rgb') -> None:
        """
        A Red-Green-Blue (RGB) color model color object.  For most
        consumer-grade devices (e.g., CRTs, LCDs, and printers), as
        well as internet applications, this is a point in the sRGB
        absolute color space.  The Hue-Saturation-Lightness (HSL),
        Hue-Lightness-Saturation (HLS), and Hue-Saturation-Value (HSV)
        spaces are useful alternate representations, or coordinate
        transformations, of this space.  Coordinates in all of these
        spaces are floating point values in the interval [0.0, 1.0].

        .. NOTE:: All instantiations of :class:`Color` are converted
                  to an internal RGB floating point 3-tuple.  This is
                  likely to degrade precision.

        INPUT:

        - ``r``, ``g``, ``b`` -- either a triple of floats between 0 and 1,
          OR ``r`` - a color name string or HTML color hex string

        - ``space`` -- string (default: ``'rgb'``); the coordinate system
          (other choices are ``'hsl'``, ``'hls'``, and ``'hsv'``) in which to
          interpret a triple of floats

        EXAMPLES::

            sage: Color('purple')
            RGB color (0.5019607843137255, 0.0, 0.5019607843137255)
            sage: Color('#8000ff')
            RGB color (0.5019607843137255, 0.0, 1.0)
            sage: Color(0.5,0,1)
            RGB color (0.5, 0.0, 1.0)
            sage: Color(0.5, 1.0, 1, space='hsv')
            RGB color (0.0, 1.0, 1.0)
            sage: Color(0.25, 0.5, 0.5, space='hls')
            RGB color (0.5000000000000001, 0.75, 0.25)
            sage: Color(1, 0, 1/3, space='hsl')
            RGB color (0.3333333333333333, 0.3333333333333333, 0.3333333333333333)
            sage: from sage.plot.colors import chocolate
            sage: Color(chocolate)
            RGB color (0.8235294117647058, 0.4117647058823529, 0.11764705882352941)
        """
    def __lt__(self, right):
        '''
        Check whether a :class:`Color` object is less than some other
        object. This doesn\'t make sense, and so we conclude that it is
        not less than the other object.

        INPUT:

        - ``right`` -- an object

        OUTPUT: boolean; ``False``

        EXAMPLES::

            sage: Color(\'red\') < Color(\'red\')
            False
            sage: Color(\'blue\') < Color(\'red\')
            False
            sage: Color(\'red\') < "xyzzy"
            False
        '''
    def __le__(self, right):
        '''
        Check whether a :class:`Color` object is less than or equal to
        some other object. It wouldn\'t make sense for it to be less than
        the other object, so we treat this the same as an equality
        check.

        INPUT:

        - ``right`` -- an object

        OUTPUT: boolean; ``False``

        EXAMPLES::

            sage: Color(\'red\') <= Color(\'red\')
            True
            sage: Color(\'blue\') <= Color(\'red\')
            False
            sage: Color(\'red\') <= "xyzzy"
            False
        '''
    def __eq__(self, right):
        """
        Compare two :class:`Color` objects to determine whether
        they refer to the same color.

        INPUT:

        - ``right`` -- a :class:`Color` instance

        OUTPUT: boolean; ``True`` if the two colors are the same, ``False``
        if different

        EXAMPLES::

            sage: Color('red') == Color((1,0,0))
            True
            sage: Color('blue') == Color((0,1,0))
            False
            sage: Color('blue') + Color((0,1,0)) == Color((0,0.5,0.5))
            True
            sage: Color(0.2,0.3,0.2) == False
            False
        """
    def __ne__(self, right):
        """
        Compare two :class:`Color` objects to determine whether
        they refer to different colors.

        INPUT:

        - ``right`` -- a :class:`Color` instance

        OUTPUT:

        boolean; ``True`` if the two colors are different, ``False`` if they're
        the same.

        EXAMPLES::

            sage: Color('green') != Color('yellow')
            True
            sage: Color('red') != Color(1,0,0)
            False
            sage: Color('yellow') != Color(1,1,0)
            False
            sage: Color('blue') != 23
            True
        """
    def __gt__(self, right):
        '''
        Check whether a :class:`Color` object is greater than some other
        object. This doesn\'t make sense, and so we conclude that it is
        not greater than the other object.

        INPUT:

        - ``right`` -- an object

        OUTPUT: boolean; ``False``

        EXAMPLES::

            sage: Color(\'red\') > Color(\'red\')
            False
            sage: Color(\'blue\') > Color(\'red\')
            False
            sage: Color(\'red\') > "xyzzy"
            False
        '''
    def __ge__(self, right):
        '''
        Check whether a :class:`Color` object is greater than or equal
        to some other object. It wouldn\'t make sense for it to be
        greater than the other object, so we treat this the same as an
        equality check.

        INPUT:

        - ``right`` -- an object

        OUTPUT: boolean; ``False``

        EXAMPLES::

            sage: Color(\'red\') >= Color(\'red\')
            True
            sage: Color(\'blue\') >= Color(\'red\')
            False
            sage: Color(\'red\') >= "xyzzy"
            False
        '''
    def __hash__(self):
        """
        Return the hash value of a color.
        Equal colors return equal hash values.

        OUTPUT: a hash value

        EXAMPLES::

            sage: hash(Color('red')) # random
            873150856
            sage: hash(Color('red')) == hash(Color((1,0,0)))
            True
        """
    def blend(self, color, fraction: float = 0.5):
        """
        Return a color blended with the given ``color`` by a given
        ``fraction``.  The algorithm interpolates linearly between the
        colors' corresponding R, G, and B coordinates.

        INPUT:

        - ``color`` -- a :class:`Color` instance or float-convertible
          3-tuple/list; the color with which to blend this color

        - ``fraction`` -- a float-convertible number; the fraction of
          ``color`` to blend with this color

        OUTPUT: a **new** :class:`Color` instance

        EXAMPLES::

            sage: from sage.plot.colors import red, blue, lime
            sage: red.blend(blue)
            RGB color (0.5, 0.0, 0.5)
            sage: red.blend(blue, fraction=0.0)
            RGB color (1.0, 0.0, 0.0)
            sage: red.blend(blue, fraction=1.0)
            RGB color (0.0, 0.0, 1.0)
            sage: lime.blend((0.3, 0.5, 0.7))
            RGB color (0.15, 0.75, 0.35)
            sage: blue.blend(blue)
            RGB color (0.0, 0.0, 1.0)
            sage: red.blend(lime, fraction=0.3)
            RGB color (0.7, 0.3, 0.0)
            sage: blue.blend((0.0, 0.9, 0.2), fraction=0.2)
            RGB color (0.0, 0.18000000000000002, 0.8400000000000001)
            sage: red.blend(0.2)
            Traceback (most recent call last):
            ...
            TypeError: 0.200000000000000 must be a Color or float-convertible 3-tuple/list
        """
    def __add__(self, right):
        '''
        Return a color "added" on the right to another color, with
        :meth:`blend`.

        INPUT:

        - ``right`` -- a :class:`Color` instance or float-convertible
          3-tuple/list

        OUTPUT: a **new** :class:`Color` instance

        EXAMPLES::

            sage: from sage.plot.colors import red, blue, lime
            sage: red + blue + lime
            RGB color (0.25, 0.5, 0.25)
            sage: from sage.plot.colors import cyan, magenta, yellow
            sage: cyan + magenta + yellow
            RGB color (0.75, 0.75, 0.5)
            sage: c1 = Color(0.1, 0.5, 0.8); c2 = Color(0.2, 0.4, 0.7, space=\'hsv\')
            sage: c1 + 0.1
            Traceback (most recent call last):
            ...
            TypeError: 0.100000000000000 must be a Color or float-convertible 3-tuple/list
            sage: c2 + [0.5, 0.2, 0.9]
            RGB color (0.572, 0.44999999999999996, 0.66)
            sage: c1.__add__(red).__add__((0.9, 0.2, 1/3))
            RGB color (0.7250000000000001, 0.225, 0.3666666666666667)
            sage: c1 + c2
            RGB color (0.37199999999999994, 0.6, 0.61)
        '''
    def __radd__(self, left):
        '''
        Return a color "added" on the left to another color, with
        :meth:`blend`.

        INPUT:

        - ``left`` -- a :class:`Color` instance or float-convertible
          3-tuple/list

        OUTPUT: a **new** :class:`Color` instance

        EXAMPLES::

            sage: from sage.plot.colors import olive, orchid
            sage: olive + orchid
            RGB color (0.6784313725490196, 0.47058823529411764, 0.4196078431372549)
            sage: d1 = Color(0.1, 0.5, 0.8, space=\'hls\'); d2 = Color(0.2, 0.4, 0.7)
            sage: [0.5, 0.2, 0.9] + d2
            RGB color (0.35, 0.30000000000000004, 0.8)
            sage: 0.1 + d1
            Traceback (most recent call last):
            ...
            TypeError: 0.100000000000000 must be a Color or float-convertible 3-tuple/list
            sage: d2.__radd__(Color(\'brown\')).__radd__((0.9, 0.2, 1/3))
            RGB color (0.661764705882353, 0.2411764705882353, 0.38284313725490193)
        '''
    def __mul__(self, right):
        """
        Return a color whose RGB coordinates are this color's
        coordinates multiplied on the right by a scalar.

        INPUT:

        - ``right`` -- a float-convertible number

        OUTPUT: a **new** :class:`Color` instance

        EXAMPLES::

            sage: Color('yellow') * 0.5
            RGB color (0.5, 0.5, 0.0)
            sage: Color('yellow') * (9.0 / 8.0)   # reduced modulo 1.0
            RGB color (0.125, 0.125, 0.0)
            sage: from sage.plot.colors import cyan, grey, indianred
            sage: cyan * 0.3 + grey * 0.1 + indianred * 0.6
            RGB color (0.25372549019607843, 0.1957843137254902, 0.1957843137254902)
            sage: indianred.__mul__(42)
            RGB color (0.764705882352942, 0.1529411764705877, 0.1529411764705877)
        """
    def __rmul__(self, left):
        """
        Return a color whose RGB coordinates are this color's
        coordinates multiplied on the left by a scalar.

        INPUT:

        - ``left`` -- a float-convertible number

        OUTPUT: a **new** :class:`Color` instance

        EXAMPLES::

            sage: from sage.plot.colors import aqua, cornsilk, tomato
            sage: 0.3 * aqua
            RGB color (0.0, 0.3, 0.3)
            sage: Color('indianred').__rmul__(42)
            RGB color (0.764705882352942, 0.1529411764705877, 0.1529411764705877)
        """
    def __truediv__(self, right):
        """
        Return a color whose RGB coordinates are this color's
        coordinates divided by a scalar.

        INPUT:

        - ``right`` -- a float-convertible, nonzero number

        OUTPUT: a **new** instance of :class:`Color`

        EXAMPLES::

            sage: from sage.plot.colors import papayawhip, yellow
            sage: yellow / 4
            RGB color (0.25, 0.25, 0.0)
            sage: yellow.__truediv__(4)
            RGB color (0.25, 0.25, 0.0)
            sage: (papayawhip + Color(0.5, 0.5, 0.1) + yellow) / 3.0
            RGB color (0.29166666666666663, 0.286437908496732, 0.07794117647058824)
            sage: vector((papayawhip / 2).rgb()) == vector((papayawhip * 0.5).rgb())
            True
            sage: yellow.__truediv__(1/4)
            RGB color (0.0, 0.0, 0.0)

        TESTS::

            sage: Color('black') / 0.0
            Traceback (most recent call last):
            ...
            ZeroDivisionError: float division by zero

            sage: papayawhip / yellow
            Traceback (most recent call last):
            ...
            TypeError: float() argument must be a string or a... number...
        """
    def __int__(self) -> int:
        """
        Return the integer representation of this colour.

        OUTPUT:

        The integer 256^2 r_int + 256 g_int + b_int, where r_int, g_int,
        and b_int are obtained from r, g, and b by converting from the
        real interval [0.0, 1.0] to the integer range 0, 1, ..., 255.

        EXAMPLES::

            sage: from sage.plot.colors import whitesmoke
            sage: int(whitesmoke)
            16119285
        """
    def __iter__(self):
        """
        Return an iterator over the RGB coordinates of this color.

        OUTPUT: a tupleiterator

        EXAMPLES::

            sage: from sage.plot.colors import dodgerblue, maroon
            sage: r, g, b = dodgerblue
            sage: r
            0.11764705882352941
            sage: g
            0.5647058823529412
            sage: b
            1.0
            sage: vector(maroon) == vector(Color(maroon)) == vector(Color('maroon'))
            True
        """
    def __getitem__(self, i):
        """
        Return the Red (0th), Green (1st), or Blue (2nd) coordinate of this
        color via index access.

        INPUT:

        - ``i`` -- integer; the 0-based coordinate to retrieve

        OUTPUT: float

        EXAMPLES::

            sage: from sage.plot.colors import crimson, midnightblue
            sage: Color('#badfad')[0]
            0.7294117647058823
            sage: (crimson[0], crimson[1], crimson[2]) == crimson.rgb()
            True
            sage: midnightblue[2] == midnightblue[-1]
            True
            sage: midnightblue[3]
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
    def rgb(self):
        """
        Return the underlying Red-Green-Blue (RGB) coordinates of this
        color.

        OUTPUT: a 3-tuple of floats

        EXAMPLES::

            sage: Color(0.3, 0.5, 0.7).rgb()
            (0.3, 0.5, 0.7)
            sage: Color('#8000ff').rgb()
            (0.5019607843137255, 0.0, 1.0)
            sage: from sage.plot.colors import orange
            sage: orange.rgb()
            (1.0, 0.6470588235294118, 0.0)
            sage: Color('magenta').rgb()
            (1.0, 0.0, 1.0)
            sage: Color(1, 0.7, 0.9, space='hsv').rgb()
            (0.9, 0.2700000000000001, 0.2700000000000001)
        """
    def hls(self):
        """
        Return the Hue-Lightness-Saturation (HLS) coordinates of this
        color.

        OUTPUT: a 3-tuple of floats

        EXAMPLES::

            sage: Color(0.3, 0.5, 0.7, space='hls').hls()
            (0.30000000000000004, 0.5, 0.7)
            sage: Color(0.3, 0.5, 0.7, space='hsl').hls() # abs tol 1e-15
            (0.30000000000000004, 0.7, 0.5000000000000001)
            sage: Color('#aabbcc').hls() # abs tol 1e-15
            (0.5833333333333334, 0.7333333333333334, 0.25000000000000017)
            sage: from sage.plot.colors import orchid
            sage: orchid.hls() # abs tol 1e-15
            (0.8396226415094339, 0.6470588235294117, 0.5888888888888889)
        """
    def hsl(self):
        """
        Return the Hue-Saturation-Lightness (HSL) coordinates of this
        color.

        OUTPUT: a 3-tuple of floats

        EXAMPLES::

            sage: Color(1,0,0).hsl()
            (0.0, 1.0, 0.5)
            sage: from sage.plot.colors import orchid
            sage: orchid.hsl() # abs tol 1e-15
            (0.8396226415094339, 0.5888888888888889, 0.6470588235294117)
            sage: Color('#aabbcc').hsl() # abs tol 1e-15
            (0.5833333333333334, 0.25000000000000017, 0.7333333333333334)
        """
    def hsv(self):
        """
        Return the Hue-Saturation-Value (HSV) coordinates of this
        color.

        OUTPUT: a 3-tuple of floats

        EXAMPLES::

            sage: from sage.plot.colors import red
            sage: red.hsv()
            (0.0, 1.0, 1.0)
            sage: Color(1,1,1).hsv()
            (0.0, 0.0, 1.0)
            sage: Color('gray').hsv()
            (0.0, 0.0, 0.5019607843137255)
        """
    def html_color(self):
        """
        Return a HTML hex representation for this color.

        OUTPUT: string of length 7

        EXAMPLES::

            sage: Color('yellow').html_color()
            '#ffff00'
            sage: Color('#fedcba').html_color()
            '#fedcba'
            sage: Color(0.0, 1.0, 0.0).html_color()
            '#00ff00'
            sage: from sage.plot.colors import honeydew
            sage: honeydew.html_color()
            '#f0fff0'
        """
    def lighter(self, fraction=...):
        '''
        Return a lighter "shade" of this RGB color by
        :meth:`blend`-ing it with white.  This is **not** an inverse
        of :meth:`darker`.

        INPUT:

        - ``fraction`` -- a float (default: 1/3); blending fraction
          to apply

        OUTPUT: a **new** instance of :class:`Color`

        EXAMPLES::

            sage: from sage.plot.colors import khaki
            sage: khaki.lighter()
            RGB color (0.9607843137254903, 0.934640522875817, 0.6993464052287582)
            sage: Color(\'white\').lighter().darker()
            RGB color (0.6666666666666667, 0.6666666666666667, 0.6666666666666667)
            sage: Color(\'#abcdef\').lighter(1/4)
            RGB color (0.7529411764705882, 0.8529411764705883, 0.9529411764705882)
            sage: Color(1, 0, 8/9, space=\'hsv\').lighter()
            RGB color (0.925925925925926, 0.925925925925926, 0.925925925925926)
        '''
    def darker(self, fraction=...):
        '''
        Return a darker "shade" of this RGB color by :meth:`blend`-ing
        it with black.  This is **not** an inverse of :meth:`lighter`.

        INPUT:

        - ``fraction`` -- a float (default: 1/3); blending fraction
          to apply

        OUTPUT: a new instance of :class:`Color`

        EXAMPLES::

            sage: from sage.plot.colors import black
            sage: vector(black.darker().rgb()) == vector(black.rgb())
            True
            sage: Color(0.4, 0.6, 0.8).darker(0.1)
            RGB color (0.36000000000000004, 0.54, 0.7200000000000001)
            sage: Color(.1,.2,.3,space=\'hsl\').darker()
            RGB color (0.24000000000000002, 0.20800000000000002, 0.16)
        '''

class ColorsDict(dict):
    """
    A dict-like collection of colors, accessible via key or attribute.
    For a list of color names, evaluate::

        sage: sorted(colors)
        ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', ...]
    """
    def __init__(self) -> None:
        """
        Construct a dict-like collection of colors.  The keys are the
        color names (i.e., strings) and the values are RGB 3-tuples of
        floats.

        EXAMPLES::

            sage: from sage.plot.colors import ColorsDict
            sage: cols = ColorsDict()
            sage: set([(type(c), type(cols[c])) for c in cols])
            {(<... 'str'>, <class 'sage.plot.colors.Color'>)}
            sage: sorted(cols)
            ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', ...]
            sage: len(cols)
            148
        """
    def __getattr__(self, name):
        """
        Get a color via attribute access.

        INPUT:

        - ``name`` -- string; the name of the color to return

        OUTPUT: a RGB 3-tuple of floats

        EXAMPLES::

            sage: from sage.plot.colors import ColorsDict, blue
            sage: cols = ColorsDict()
            sage: cols.blue
            RGB color (0.0, 0.0, 1.0)
            sage: cols['blue']
            RGB color (0.0, 0.0, 1.0)
            sage: blue
            RGB color (0.0, 0.0, 1.0)
            sage: cols.punk
            Traceback (most recent call last):
            ...
            AttributeError: 'ColorsDict' has no attribute or colormap punk...
        """
    def __dir__(self):
        """
        Return an approximate list of attribute names, including the
        color names.

        OUTPUT: list of strings

        EXAMPLES::

            sage: from sage.plot.colors import ColorsDict
            sage: cols = ColorsDict()
            sage: 'green' in dir(cols)
            True
        """

colors: Incomplete

def hue(h, s: int = 1, v: int = 1):
    """
    Convert a Hue-Saturation-Value (HSV) color tuple to a valid
    Red-Green-Blue (RGB) tuple.  All three inputs should lie in the
    interval [0.0, 1.0]; otherwise, they are reduced modulo 1 (see
    :func:`mod_one`).  In particular ``h=0`` and ``h=1`` yield red,
    with the intermediate hues orange, yellow, green, cyan, blue, and
    violet as ``h`` increases.

    This function makes it easy to sample a broad range of colors for
    graphics::

        sage: # needs sage.symbolic
        sage: p = Graphics()
        sage: for phi in xsrange(0, 2 * pi, 1 / pi):
        ....:     p += plot(sin(x + phi), (x, -7, 7), rgbcolor=hue(phi))
        sage: p
        Graphics object consisting of 20 graphics primitives

    INPUT:

    - ``h`` -- a number; the color's hue

    - ``s`` -- a number (default: 1); the color's saturation

    - ``v`` -- a number (default: 1); the color's value

    OUTPUT: a RGB 3-tuple of floats in the interval [0.0, 1.0]

    EXAMPLES::

        sage: hue(0.6)
        (0.0, 0.40000000000000036, 1.0)
        sage: from sage.plot.colors import royalblue
        sage: royalblue
        RGB color (0.2549019607843137, 0.4117647058823529, 0.8823529411764706)
        sage: hue(*royalblue.hsv())
        (0.2549019607843137, 0.4117647058823529, 0.8823529411764706)
        sage: hue(.5, .5, .5)
        (0.25, 0.5, 0.5)

    .. NOTE::

        The HSV to RGB coordinate transformation itself is
        given in the source code for the Python library's
        :mod:`colorsys` module::

            sage: from colorsys import hsv_to_rgb    # not tested
            sage: hsv_to_rgb??                       # not tested
    """
def float_to_html(r, g, b):
    '''
    Convert a Red-Green-Blue (RGB) color tuple to a HTML hex color.

    Each input value should be in the interval [0.0, 1.0]; otherwise,
    the values are first reduced modulo one (see :func:`mod_one`).

    INPUT:

    - ``r`` -- a real number; the RGB color\'s "red" intensity

    - ``g`` -- a real number; the RGB color\'s "green" intensity

    - ``b`` -- a real number; the RGB color\'s "blue" intensity

    OUTPUT: string of length 7, starting with ``\'#\'``

    EXAMPLES::

        sage: from sage.plot.colors import float_to_html
        sage: float_to_html(1.,1.,0.)
        \'#ffff00\'
        sage: float_to_html(.03,.06,.02)
        \'#070f05\'
        sage: float_to_html(*Color(\'brown\').rgb())
        \'#a52a2a\'

    TESTS::

        sage: float_to_html((0.2, 0.6, 0.8))
        Traceback (most recent call last):
        ...
        TypeError: ...float_to_html() missing 2 required positional arguments: \'g\' and \'b\'
    '''
def float_to_integer(r, g, b):
    '''
    Convert a Red-Green-Blue (RGB) color tuple to an integer.

    Each input value should be in the interval [0.0, 1.0]; otherwise,
    the values are first reduced modulo one (see :func:`mod_one`).

    INPUT:

    - ``r`` -- a real number; the RGB color\'s "red" intensity

    - ``g`` -- a real number; the RGB color\'s "green" intensity

    - ``b`` -- a real number; the RGB color\'s "blue" intensity

    OUTPUT:

    The integer 256^2 r_int + 256 g_int + b_int, where r_int, g_int, and
    b_int are obtained from r, g, and b by converting from the real
    interval [0.0, 1.0] to the integer range 0, 1, ..., 255.

    EXAMPLES::

        sage: from sage.plot.colors import float_to_integer
        sage: float_to_integer(1.,1.,0.)
        16776960
        sage: float_to_integer(.03,.06,.02)
        462597
        sage: float_to_integer(*Color(\'brown\').rgb())
        10824234

    TESTS::

        sage: float_to_integer((0.2, 0.6, 0.8))
        Traceback (most recent call last):
        ...
        TypeError: ...float_to_integer() missing 2 required positional arguments: \'g\' and \'b\'
    '''
def rainbow(n, format: str = 'hex'):
    """
    Return a list of colors sampled at equal intervals over the
    spectrum, from Hue-Saturation-Value (HSV) coordinates (0, 1, 1) to
    (1, 1, 1).  This range is red at the extremes, but it covers
    orange, yellow, green, cyan, blue, violet, and many other hues in
    between.  This function is particularly useful for representing
    vertex partitions on graphs.

    INPUT:

    - ``n`` -- a number; the length of the list

    - ``format`` -- string (default: ``'hex'``); the output format for
      each color in the list. The other choice is ``'rgbtuple'``.

    OUTPUT: a list of strings or RGB 3-tuples of floats in the interval
    [0.0, 1.0]

    EXAMPLES::

        sage: from sage.plot.colors import rainbow
        sage: rainbow(7)
        ['#ff0000', '#ffda00', '#48ff00', '#00ff91', '#0091ff', '#4800ff', '#ff00da']
        sage: rainbow(int(7))
        ['#ff0000', '#ffda00', '#48ff00', '#00ff91', '#0091ff', '#4800ff', '#ff00da']
        sage: rainbow(7, 'rgbtuple')
        [(1.0, 0.0, 0.0), (1.0, 0.8571428571428571, 0.0), (0.2857142857142858, 1.0, 0.0), (0.0, 1.0, 0.5714285714285712), (0.0, 0.5714285714285716, 1.0), (0.2857142857142856, 0.0, 1.0), (1.0, 0.0, 0.8571428571428577)]

    AUTHORS:

    - Robert L. Miller

    - Karl-Dieter Crisman (directly use :func:`hsv_to_rgb` for hues)
    """
def get_cmap(cmap):
    '''
    Return a color map (actually, a matplotlib :class:`Colormap`
    object), given its name or a [mixed] list/tuple of RGB list/tuples
    and color names.  For a list of map names, evaluate::

        sage: sorted(colormaps)
        [\'Accent\', ...]

    See :func:`rgbcolor` for valid list/tuple element formats.

    INPUT:

    - ``cmap`` -- string, list, tuple, or :class:`matplotlib.colors.Colormap`;
      a string must be a valid color map name

    OUTPUT: a :class:`matplotlib.colors.Colormap` instance

    EXAMPLES::

        sage: from sage.plot.colors import get_cmap
        sage: get_cmap(\'jet\')
        <matplotlib.colors.LinearSegmentedColormap object at 0x...>
        sage: get_cmap([(0,0,0), (0.5,0.5,0.5), (1,1,1)])
        <matplotlib.colors.ListedColormap object at 0x...>
        sage: get_cmap([\'green\', \'lightblue\', \'blue\'])
        <matplotlib.colors.ListedColormap object at 0x...>
        sage: get_cmap(((0.5, 0.3, 0.2), [1.0, 0.0, 0.5], \'purple\', Color(0.5,0.5,1, space=\'hsv\')))
        <matplotlib.colors.ListedColormap object at 0x...>
        sage: get_cmap(\'jolies\')
        Traceback (most recent call last):
        ...
        RuntimeError: Color map jolies not known (type "import matplotlib; list(matplotlib.colormaps.keys())" for valid names)
        sage: get_cmap(\'mpl\')
        Traceback (most recent call last):
        ...
        RuntimeError: Color map mpl not known (type "import matplotlib; list(matplotlib.colormaps.keys())" for valid names)

    TESTS:

    Check that :issue:`33491` is fixed::

        sage: get_cmap(\'turbo\')
        <matplotlib.colors.ListedColormap object at 0x...>
    '''
def check_color_data(cfcm):
    """
    Make sure that the arguments are in order (coloring function, colormap).

    This will allow users to use both possible orders.

    EXAMPLES::

        sage: from sage.plot.colors import check_color_data
        sage: cf = lambda x,y : (x+y) % 1
        sage: cm = colormaps.autumn
        sage: check_color_data((cf, cm)) == (cf, cm)
        True
        sage: check_color_data((cm, cf)) == (cf, cm)
        True

    TESTS::

        sage: check_color_data(('a', 33))
        Traceback (most recent call last):
        ...
        ValueError: color data must be (color function, colormap)
    """

class Colormaps(MutableMapping):
    """
    A dict-like collection of lazily-loaded matplotlib color maps.
    For a list of map names, evaluate::

        sage: sorted(colormaps)
        ['Accent', ...]
    """
    maps: Incomplete
    def __init__(self) -> None:
        """
        Construct an empty mutable collection of color maps.

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: len(maps.maps)
            0
        """
    def load_maps(self) -> None:
        """
        If it's necessary, loads matplotlib's color maps and adds them
        to the collection.

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: len(maps.maps)
            0
            sage: maps.load_maps()
            sage: len(maps.maps)>60
            True
            sage: 'viridis' in maps
            True
        """
    def __dir__(self):
        """
        Return an approximate list of attribute names, including the
        color map names.

        OUTPUT: list of strings

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: 'Accent' in dir(maps)
            True
        """
    def __len__(self) -> int:
        """
        Return the number of color maps.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: len(maps)>60
            True
        """
    def __iter__(self):
        """
        Return an iterator over the color map collection.

        OUTPUT: a dictionary key iterator instance

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: count = 0
            sage: for m in maps: count += 1
            sage: count == len(maps)
            True
        """
    def __contains__(self, name) -> bool:
        """
        Return whether a map is in the color maps collection.

        INPUT:

        - ``name`` -- string; the name of the map to query

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: 'summer' in maps
            True
            sage: 'not really a color map' in maps
            False
        """
    def __getitem__(self, name):
        '''
        Get a color map from the collection via key access.

        INPUT:

        - ``name`` -- string; the name of the map return

        OUTPUT: an instance of :class:`matplotlib.colors.Colormap`

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: maps.get(\'Oranges\')
            <matplotlib.colors.LinearSegmentedColormap object at ...>
            sage: maps[\'copper\']
            <matplotlib.colors.LinearSegmentedColormap object at ...>
            sage: maps.get(\'not a color map\')
            sage: maps[\'not a color map\']
            Traceback (most recent call last):
            ...
            KeyError: "no colormap with name \'not a color map\'"
        '''
    def __getattr__(self, name):
        '''
        Get a color map from the collection via attribute access.

        INPUT:

        - ``name`` -- string; the name of the map to return

        OUTPUT: an instance of :class:`matplotlib.colors.Colormap`

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: maps.pink
            <matplotlib.colors.LinearSegmentedColormap object at ...>
            sage: maps.punk
            Traceback (most recent call last):
            ...
            AttributeError: \'Colormaps\' has no attribute or colormap punk...
            sage: maps[\'punk\']
            Traceback (most recent call last):
            ...
            KeyError: "no colormap with name \'punk\'"
            sage: maps[\'bone\'] == maps.bone
            True
        '''
    def __setitem__(self, name, colormap) -> None:
        """
        Add a color map to the collection.

        INPUT:

        - ``name`` -- string; the name of the map to add

        - ``colormap`` -- an instance of
          :class:`matplotlib.colors.Colormap`; the color map to add

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps, get_cmap
            sage: maps = Colormaps()
            sage: count = len(maps)
            sage: my_map = get_cmap(['chartreuse', '#007', (1.0, 0.0, 0.0)])
            sage: maps['my_map'] = my_map
            sage: 'my_map' in maps
            True
            sage: count + 1 == len(maps)
            True
        """
    def __delitem__(self, name) -> None:
        """
        Removes a color map from the collection.

        INPUT:

        - ``name`` -- string; the name of the map to remove

        EXAMPLES::

            sage: from sage.plot.colors import Colormaps
            sage: maps = Colormaps()
            sage: count = len(maps)
            sage: maps.popitem()  # random
            ('Spectral', <matplotlib.colors.LinearSegmentedColormap object at ...>)
            sage: count - 1 == len(maps)
            True
        """

colormaps: Incomplete
