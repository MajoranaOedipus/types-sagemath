r"""
Factories to construct function fields

This module provides factories to construct function fields. These factories
are only for internal use.

EXAMPLES::

    sage: K.<x> = FunctionField(QQ); K
    Rational function field in x over Rational Field
    sage: L.<x> = FunctionField(QQ); L
    Rational function field in x over Rational Field
    sage: K is L
    True

AUTHORS:

- William Stein (2010): initial version

- Maarten Derickx (2011-09-11): added ``FunctionField_polymod_Constructor``,
  use ``@cached_function``

- Julian Rueth (2011-09-14): replaced ``@cached_function`` with
  ``UniqueFactory``
"""
from sage.structure.factory import UniqueFactory as UniqueFactory

class FunctionFieldFactory(UniqueFactory):
    """
    Return the function field in one variable with constant field ``F``. The
    function field returned is unique in the sense that if you call this
    function twice with the same base field and name then you get the same
    python object back.

    INPUT:

    - ``F`` -- field

    - ``names`` -- name of variable as a string or a tuple containing a string

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ); K
        Rational function field in x over Rational Field
        sage: L.<y> = FunctionField(GF(7)); L
        Rational function field in y over Finite Field of size 7
        sage: R.<z> = L[]
        sage: M.<z> = L.extension(z^7 - z - y); M                                       # needs sage.rings.finite_rings sage.rings.function_field
        Function field in z defined by z^7 + 6*z + 6*y

    TESTS::

        sage: K.<x> = FunctionField(QQ)
        sage: L.<x> = FunctionField(QQ)
        sage: K is L
        True
        sage: M.<x> = FunctionField(GF(7))
        sage: K is M
        False
        sage: N.<y> = FunctionField(QQ)
        sage: K is N
        False
    """
    def create_key(self, F, names):
        """
        Given the arguments and keywords, create a key that uniquely
        determines this object.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ) # indirect doctest
        """
    def create_object(self, version, key, **extra_args):
        """
        Create the object from the key and extra arguments. This is only
        called if the object was not found in the cache.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)  # indirect doctest
            sage: L.<x> = FunctionField(QQ)  # indirect doctest
            sage: K is L
            True
        """

FunctionField: FunctionFieldFactory

class FunctionFieldExtensionFactory(UniqueFactory):
    """
    Create a function field defined as an extension of another
    function field by adjoining a root of a univariate polynomial.
    The returned function field is unique in the sense that if you
    call this function twice with an equal ``polynomial`` and ``names``
    it returns the same python object in both calls.

    INPUT:

    - ``polynomial`` -- univariate polynomial over a function field

    - ``names`` -- variable names (as a tuple of length 1 or string)

    - ``category`` -- category (defaults to category of function fields)

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: y2 = y*1
        sage: y2 is y
        False
        sage: L.<w> = K.extension(x - y^2)                                              # needs sage.rings.function_field
        sage: M.<w> = K.extension(x - y2^2)                                             # needs sage.rings.function_field
        sage: L is M                                                                    # needs sage.rings.function_field
        True
    """
    def create_key(self, polynomial, names):
        """
        Given the arguments and keywords, create a key that uniquely
        determines this object.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<w> = K.extension(x - y^2)  # indirect doctest                      # needs sage.rings.function_field

        TESTS:

        Verify that :issue:`16530` has been resolved::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z - 1)
            sage: R.<z> = K[]
            sage: N.<z> = K.extension(z - 1)
            sage: M is N
            False
        """
    def create_object(self, version, key, **extra_args):
        """
        Create the object from the key and extra arguments. This is only
        called if the object was not found in the cache.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<w> = K.extension(x - y^2)   # indirect doctest                     # needs sage.rings.function_field
            sage: y2 = y*1
            sage: M.<w> = K.extension(x - y2^2)  # indirect doctest                     # needs sage.rings.function_field
            sage: L is M                                                                # needs sage.rings.function_field
            True
        """

FunctionFieldExtension: FunctionFieldExtensionFactory
