from _typeshed import Incomplete
from sage.categories.sets_cat import Sets as Sets
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as TotallyOrderedFiniteSet

set_of_letters: Incomplete

def build_alphabet(data=None, names=None, name=None):
    '''
    Return an object representing an ordered alphabet.

    INPUT:

    - ``data`` -- the letters of the alphabet; it can be:

      * a list/tuple/iterable of letters; the iterable may be infinite
      * an integer `n` to represent `\\{1, \\ldots, n\\}`, or infinity to
        represent `\\NN`

    - ``names`` -- (optional) a list for the letters (i.e. variable names) or
      a string for prefix for all letters; if given a list, it must have the
      same cardinality as the set represented by ``data``

    - ``name`` -- (optional) if given, then return a named set and can be
      equal to : ``\'lower\', \'upper\', \'space\',
      \'underscore\', \'punctuation\', \'printable\', \'binary\', \'octal\', \'decimal\',
      \'hexadecimal\', \'radix64\'``.

      You can use many of them at once, separated by spaces : ``\'lower
      punctuation\'`` represents the union of the two alphabets ``\'lower\'`` and
      ``\'punctuation\'``.

      Alternatively, ``name`` can be set to ``\'positive integers\'`` (or
      ``\'PP\'``) or ``\'natural numbers\'`` (or ``\'NN\'``).

      ``name`` cannot be combined with ``data``.

    EXAMPLES:

    If the argument is a Set, it just returns it::

        sage: build_alphabet(ZZ) is ZZ
        True
        sage: F = FiniteEnumeratedSet(\'abc\')
        sage: build_alphabet(F) is F
        True

    If a list, tuple or string is provided, then it builds a proper Sage class
    (:class:`~sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet`)::

        sage: build_alphabet([0,1,2])
        {0, 1, 2}
        sage: F = build_alphabet(\'abc\'); F
        {\'a\', \'b\', \'c\'}
        sage: print(type(F).__name__)
        TotallyOrderedFiniteSet_with_category

    If an integer and a set is given, then it constructs a
    :class:`~sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet`::

        sage: build_alphabet(3, [\'a\',\'b\',\'c\'])
        {\'a\', \'b\', \'c\'}

    If an integer and a string is given, then it considers that string as a
    prefix::

        sage: build_alphabet(3, \'x\')
        {\'x0\', \'x1\', \'x2\'}

    If no data is provided, ``name`` may be a string which describe an alphabet.
    The available names decompose into two families. The first one are \'positive
    integers\', \'PP\', \'natural numbers\' or \'NN\' which refer to standard set of
    numbers::

        sage: build_alphabet(name="positive integers")
        Positive integers
        sage: build_alphabet(name=\'PP\')
        Positive integers
        sage: build_alphabet(name="natural numbers")
        Non negative integers
        sage: build_alphabet(name="NN")
        Non negative integers

    The other families for the option ``name`` are among \'lower\', \'upper\',
    \'space\', \'underscore\', \'punctuation\', \'printable\', \'binary\', \'octal\',
    \'decimal\', \'hexadecimal\', \'radix64\' which refer to standard set of
    characters. Theses names may be combined by separating them by a space::

        sage: build_alphabet(name=\'lower\')
        {\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\'}
        sage: build_alphabet(name=\'hexadecimal\')
        {\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\'}
        sage: build_alphabet(name="decimal punctuation")
        {\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \' \', \',\', \'.\', \';\', \':\', \'!\', \'?\'}

    In the case the alphabet is built from a list or a tuple, the order on the
    alphabet is given by the elements themselves::

        sage: A = build_alphabet([0,2,1])
        sage: A(0) < A(2)
        True
        sage: A(2) < A(1)
        False

    If a different order is needed, you may use
    :class:`~sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet` and
    set the option ``facade`` to ``False``. That way, the comparison fits the
    order of the input::

        sage: A = TotallyOrderedFiniteSet([4,2,6,1], facade=False)
        sage: A(4) < A(2)
        True
        sage: A(1) < A(6)
        False

    Be careful, the element of the set in the last example are no more
    integers and do not compare equal with integers::

        sage: type(A.an_element())
        <class \'sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet_with_category.element_class\'>
        sage: A(1) == 1
        False
        sage: 1 == A(1)
        False

    We give an example of an infinite alphabet indexed by the positive
    integers and the prime numbers::

        sage: build_alphabet(oo, \'x\')
        Lazy family (x(i))_{i in Non negative integers}
        sage: build_alphabet(Primes(), \'y\')
        Lazy family (y(i))_{i in Set of all prime numbers: 2, 3, 5, 7, ...}

    TESTS::

        sage: Alphabet(3, name=\'punctuation\')
        Traceback (most recent call last):
        ...
        ValueError: name cannot be specified with any other argument
        sage: Alphabet(8, [\'e\']*10)
        Traceback (most recent call last):
        ...
        ValueError: invalid value for names
        sage: Alphabet(8, x)                                                            # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: invalid value for names
        sage: Alphabet(name=x, names=\'punctuation\')                                     # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: name cannot be specified with any other argument
        sage: Alphabet(x)                                                               # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: unable to construct an alphabet from the given parameters
    '''
Alphabet = build_alphabet
