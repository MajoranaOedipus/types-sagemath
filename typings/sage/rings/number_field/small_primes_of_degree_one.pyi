from sage.rings.integer_ring import ZZ as ZZ

class Small_primes_of_degree_one_iter:
    """
    Iterator that finds primes of a number field of absolute degree
    one and bounded small prime norm.

    INPUT:

    - ``field`` -- a :class:`NumberField`

    - ``num_integer_primes`` -- integer (default: 10000); we try to find
      primes of absolute norm no greater than the ``num_integer_primes``-th
      prime number. For example, if ``num_integer_primes`` is 2, the largest
      norm found will be 3, since the second prime is 3.

    - ``max_iterations`` -- integer (default: 100); we test ``max_iterations``
      integers to find small primes before raising :class:`StopIteration`

    AUTHOR:

    - Nick Alexander
    """
    def __init__(self, field, num_integer_primes: int = 10000, max_iterations: int = 100) -> None:
        """
        Construct a new iterator of small degree one primes.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K.primes_of_degree_one_list(3) # random
            [Fractional ideal (2*a + 1), Fractional ideal (-a + 4), Fractional ideal (3*a + 2)]
        """
    def __iter__(self):
        """
        Return ``self`` as an iterator.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: it = K.primes_of_degree_one_iter()
            sage: iter(it) == it # indirect doctest
            True
        """
    def __next__(self):
        """
        Return a prime of absolute degree one of small prime norm.

        Raises ``StopIteration`` if such a prime cannot be easily found.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: it = K.primes_of_degree_one_iter()
            sage: [ next(it) for i in range(3) ] # random
            [Fractional ideal (2*a + 1), Fractional ideal (-a + 4), Fractional ideal (3*a + 2)]

        TESTS:

        We test that :issue:`6396` is fixed. Note that the doctest is
        flagged as random since the string representation of ideals is
        somewhat unpredictable::

            sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
            sage: ids = N.primes_of_degree_one_list(10); ids  # random
            [Fractional ideal ((-1/2*b + 1/2)*a + 2),
             Fractional ideal (-b*a + 1/2*b + 1/2),
             Fractional ideal ((1/2*b + 3/2)*a - b),
             Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
             Fractional ideal (-b*a - b + 1),
             Fractional ideal (3*a + 1/2*b - 1/2),
             Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
             Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
             Fractional ideal (2*a - 3/2*b - 1/2),
             Fractional ideal (3*a + 1/2*b + 5/2)]
             sage: [x.absolute_norm() for x in ids]
             [29, 41, 61, 89, 101, 109, 149, 181, 229, 241]
             sage: ids[9] == N.ideal(3*a + 1/2*b + 5/2)
             True

        We test that :issue:`23468` is fixed::

            sage: R.<z> = QQ[]
            sage: K.<y> = QQ.extension(25*z^2 + 26*z + 5)
            sage: for p in K.primes_of_degree_one_list(10):
            ....:     assert p.is_prime()
        """
    next = __next__
