from .expression import Expression as Expression
from .ring import SR as SR
from _typeshed import Incomplete
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.rings.rational_field import QQ as QQ

one: Incomplete
unitdict: Incomplete
unit_to_type: Incomplete
value_to_unit: Incomplete

def evalunitdict() -> None:
    """
    Replace all the string values of the unitdict variable by their
    evaluated forms, and builds some other tables for ease of use.
    This function is mainly used internally, for efficiency (and
    flexibility) purposes, making it easier to describe the units.

    EXAMPLES::

        sage: sage.symbolic.units.evalunitdict()
    """

unit_docs: Incomplete
unit_derivations: Incomplete

def vars_in_str(s):
    """
    Given a string like ``'mass/(length*time)'``, return the list
    ``['mass', 'length', 'time']``.

    INPUT:

    - ``s`` -- string

    OUTPUT: list of strings (unit names)

    EXAMPLES::

        sage: sage.symbolic.units.vars_in_str('mass/(length*time)')
        ['mass', 'length', 'time']
    """
def unit_derivations_expr(v):
    """
    Given derived units name, returns the corresponding units expression.

    For example, given ``'acceleration'`` output the symbolic expression
    ``length/time^2``.

    INPUT:

    - ``v`` -- string; name of a unit type such as ``'area'``, ``'volume'``, etc.

    OUTPUT: a symbolic expression

    EXAMPLES::

        sage: sage.symbolic.units.unit_derivations_expr('volume')
        length^3
        sage: sage.symbolic.units.unit_derivations_expr('electric_potential')
        length^2*mass/(current*time^3)

    If the unit name is unknown, a :exc:`KeyError` is raised::

        sage: sage.symbolic.units.unit_derivations_expr('invalid')
        Traceback (most recent call last):
        ...
        KeyError: 'invalid'
    """

class UnitExpression(Expression):
    """
    A symbolic unit.

    EXAMPLES::

        sage: acre = units.area.acre
        sage: type(acre)
        <class 'sage.symbolic.units.UnitExpression'>

    TESTS::

        sage: bool(loads(dumps(acre)) == acre)
        True
        sage: type(loads(dumps(acre)))
        <class 'sage.symbolic.units.UnitExpression'>
    """

def str_to_unit(name):
    """
    Create the symbolic unit with given name.  A symbolic unit is a
    class that derives from symbolic expression, and has a specialized
    docstring.

    INPUT:

    - ``name`` -- string

    OUTPUT: a :class:`UnitExpression`

    EXAMPLES::

        sage: sage.symbolic.units.str_to_unit('acre')
        acre
        sage: type(sage.symbolic.units.str_to_unit('acre'))
        <class 'sage.symbolic.units.UnitExpression'>
    """

class Units(ExtraTabCompletion):
    """
    A collection of units of some type.

    EXAMPLES::

        sage: units.power
        Collection of units of power: cheval_vapeur horsepower watt
    """
    def __init__(self, data, name: str = '') -> None:
        """
        EXAMPLES::

            sage: sage.symbolic.units.Units(sage.symbolic.units.unitdict, 'all units')
            Collection of units of all units: acceleration ... volume
        """
    def __eq__(self, other):
        """
        Compare two collections of units, or a collection of units
        with some other object.

        EXAMPLES::

            sage: units.length == 10
            False
            sage: units.length == units.length
            True
            sage: units.length == units.mass
            False
        """
    def __ne__(self, other):
        """
        Test for unequality.

        EXAMPLES::

            sage: units.length != 5
            True
            sage: units.length != units.length
            False
            sage: units.length != units.mass
            True
        """
    def __getattr__(self, name):
        """
        Return the unit with the given name.

        EXAMPLES::

            sage: units.area
            Collection of units of area: acre are barn hectare rood section square_chain square_meter township
            sage: units.area.barn
            barn

        Units are cached::

            sage: units.area.acre is units.area.acre
            True
        """

units: Incomplete

def unitdocs(unit):
    """
    Return docstring for the given unit.

    INPUT:

    - ``unit`` -- a unit

    OUTPUT: string

    EXAMPLES::

        sage: sage.symbolic.units.unitdocs('meter')
        'SI base unit of length.\\nDefined to be the distance light travels in vacuum in 1/299792458 of a second.'
        sage: sage.symbolic.units.unitdocs('amu')
        'Abbreviation for atomic mass unit.\\nApproximately equal to 1.660538782*10^-27 kilograms.'

    Units not in the list unit_docs will raise a :exc:`ValueError`::

        sage: sage.symbolic.units.unitdocs('earth')
        Traceback (most recent call last):
        ...
        ValueError: no documentation exists for the unit earth
    """
def is_unit(s) -> bool:
    """
    Return a boolean when asked whether the input is in the list of units.

    INPUT:

    - ``s`` -- an object

    OUTPUT: boolean

    EXAMPLES::

        sage: sage.symbolic.units.is_unit(1)
        False
        sage: sage.symbolic.units.is_unit(units.length.meter)
        True

    The square of a unit is not a unit::

        sage: sage.symbolic.units.is_unit(units.length.meter^2)
        False

    You can also directly create units using var, though they won't have
    a nice docstring describing the unit::

        sage: sage.symbolic.units.is_unit(var('meter'))
        True
    """
def convert(expr, target):
    """
    Convert units between ``expr`` and ``target``. If ``target`` is ``None``
    then converts to SI base units.

    INPUT:

    - ``expr`` -- the symbolic expression converting from

    - ``target`` -- (default: ``None``) the symbolic expression converting to

    OUTPUT: a symbolic expression

    EXAMPLES::

        sage: sage.symbolic.units.convert(units.length.foot, None)
        381/1250*meter
        sage: sage.symbolic.units.convert(units.mass.kilogram, units.mass.pound)
        100000000/45359237*pound

    This raises :exc:`ValueError` if expr and target are not convertible::

        sage: sage.symbolic.units.convert(units.mass.kilogram, units.length.foot)
        Traceback (most recent call last):
        ...
        ValueError: Incompatible units
        sage: sage.symbolic.units.convert(units.length.meter^2, units.length.foot)
        Traceback (most recent call last):
        ...
        ValueError: Incompatible units

    Recognizes derived unit relationships to base units and other derived units::

        sage: sage.symbolic.units.convert(units.length.foot/units.time.second^2, units.acceleration.galileo)
        762/25*galileo
        sage: sage.symbolic.units.convert(units.mass.kilogram*units.length.meter/units.time.second^2, units.force.newton)
        newton
        sage: sage.symbolic.units.convert(units.length.foot^3, units.area.acre*units.length.inch)
        1/3630*(acre*inch)
        sage: sage.symbolic.units.convert(units.charge.coulomb, units.current.ampere*units.time.second)
        (ampere*second)
        sage: sage.symbolic.units.convert(units.pressure.pascal*units.si_prefixes.kilo, units.pressure.pounds_per_square_inch)
        1290320000000/8896443230521*pounds_per_square_inch

    For decimal answers multiply 1.0::

        sage: sage.symbolic.units.convert(units.pressure.pascal*units.si_prefixes.kilo, units.pressure.pounds_per_square_inch)*1.0
        0.145037737730209*pounds_per_square_inch

    You can also convert quantities of units::

        sage: sage.symbolic.units.convert(cos(50) * units.angles.radian, units.angles.degree)
        degree*(180*cos(50)/pi)
        sage: sage.symbolic.units.convert(cos(30) * units.angles.radian, units.angles.degree).polynomial(RR)
        8.83795706233228*degree
        sage: sage.symbolic.units.convert(50 * units.length.light_year / units.time.year, units.length.foot / units.time.second)
        6249954068750/127*(foot/second)

    Quantities may contain variables (not for temperature conversion, though)::

        sage: sage.symbolic.units.convert(50 * x * units.area.square_meter, units.area.acre)
        acre*(1953125/158080329*x)
    """
def base_units(unit):
    """
    Convert unit to base SI units.

    INPUT:

    - ``unit`` -- a unit

    OUTPUT: a symbolic expression

    EXAMPLES::

        sage: sage.symbolic.units.base_units(units.length.foot)
        381/1250*meter

    If unit is already a base unit, it just returns that unit::

        sage: sage.symbolic.units.base_units(units.length.meter)
        meter

    Derived units get broken down into their base parts::

        sage: sage.symbolic.units.base_units(units.force.newton)
        kilogram*meter/second^2
        sage: sage.symbolic.units.base_units(units.volume.liter)
        1/1000*meter^3

    Returns variable if ``unit`` is not a unit::

        sage: sage.symbolic.units.base_units(var('x'))
        x
    """
def convert_temperature(expr, target):
    """
    Function for converting between temperatures.

    INPUT:

    - ``expr`` -- a unit of temperature
    - ``target`` -- a units of temperature

    OUTPUT: a symbolic expression

    EXAMPLES::

        sage: t = 32*units.temperature.fahrenheit
        sage: t.convert(units.temperature.celsius)
        0
        sage: t.convert(units.temperature.kelvin)
        273.150000000000*kelvin

    If target is ``None`` then it defaults to kelvin::

        sage: t.convert()
        273.150000000000*kelvin

    This raises :exc:`ValueError` when either input is not a unit of temperature::

        sage: t.convert(units.length.foot)
        Traceback (most recent call last):
        ...
        ValueError: cannot convert
        sage: wrong = units.length.meter*units.temperature.fahrenheit
        sage: wrong.convert()
        Traceback (most recent call last):
        ...
        ValueError: cannot convert

    We directly call the convert_temperature function::

        sage: sage.symbolic.units.convert_temperature(37*units.temperature.celsius, units.temperature.fahrenheit)
        493/5*fahrenheit
        sage: 493/5.0
        98.6000000000000
    """
