from _typeshed import Incomplete
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer

class gosper_iterator:
    """
    Iterable for the partial quotients of `(a*x+b)/(c*x+d)`, where `a, b, c, d`
    are integers, and `x` is a continued fraction.
    """
    a: Incomplete
    b: Incomplete
    c: Incomplete
    d: Incomplete
    x: Incomplete
    states: Incomplete
    states_to_currently_emitted: Incomplete
    currently_emitted: int
    currently_read: int
    input_preperiod_length: Incomplete
    input_period_length: Incomplete
    output_preperiod_length: int
    def __init__(self, a, b, c, d, x) -> None:
        """
        Construct the class.

        INPUT:

        - ``a``, ``b``, ``c``, ``d`` -- integer coefficients of the transformation

        - ``x`` -- a continued fraction

        TESTS::

            sage: a = Integer(randint(-10,10)); b = Integer(randint(-10,10));
            sage: c = Integer(randint(-10,10)); d = Integer(randint(-10,10));
            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: x = continued_fraction(([1,2],[3,4])); i = iter(gosper_iterator(a,b,c,d,x))
            sage: l = list(i)
            sage: preperiod_length = i.output_preperiod_length
            sage: preperiod = l[:preperiod_length]
            sage: period = l[preperiod_length:]
            sage: c == d == 0 or continued_fraction((preperiod, period), x.value()) == continued_fraction((a*x.value()+b)/(c*x.value()+d))  # not tested, known bug (see :issue:`32127`)
            True

        Infinity::

            sage: cf = continued_fraction(2/3)
            sage: list(gosper_iterator(0, 1, 3, -2, cf))
            []
        """
    def __iter__(self):
        """
        Return the iterable instance of the class.

        Is called upon `iter(gosper_iterator(a,b,c,d,x))`.

        TESTS::

            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: a, b, c, d = (Integer(randint(-100,100)) for _ in range(4))
            sage: ig = iter(gosper_iterator(a, b, c, d, continued_fraction(pi)))        # needs sage.symbolic
            sage: icf = iter(continued_fraction((a*pi + b) / (c*pi + d)));              # needs sage.symbolic
            sage: for i in range(10):                                                   # needs sage.symbolic
            ....:     try:
            ....:         assert next(ig) == next(icf)
            ....:     except StopIteration:
            ....:         break
        """
    def __next__(self):
        """
        Return the next term of the transformation.

        TESTS::

            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: it = gosper_iterator(1, 0, 0, 1, continued_fraction(pi))              # needs sage.symbolic
            sage: list(next(it) for _ in range(10))                                     # needs sage.symbolic
            [3, 7, 15, 1, 292, 1, 1, 1, 2, 1]
        """
    def emit(self, q) -> None:
        """
        Change the state of the iterator, emitting the term `q`.

        TESTS::

            sage: a = Integer(randint(-100,100)); b = Integer(randint(-100,100));
            sage: c = Integer(randint(-100,100)); d = Integer(randint(-100,100));
            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: gi = gosper_iterator(a, b, c, d, continued_fraction(pi))              # needs sage.symbolic
            sage: for i in range(10):                                                   # needs sage.symbolic
            ....:     gi.emit(i)
            sage: gi.currently_emitted                                                  # needs sage.symbolic
            10
        """
    def ingest(self) -> None:
        """
        Change the state of the iterator, ingesting another term from the input continued fraction.

        TESTS::

            sage: a = Integer(randint(-100,100)); b = Integer(randint(-100,100));
            sage: c = Integer(randint(-100,100)); d = Integer(randint(-100,100));
            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: gi = gosper_iterator(a, b, c, d, continued_fraction(pi))              # needs sage.symbolic
            sage: for i in range(10):                                                   # needs sage.symbolic
            ....:     gi.ingest()
            sage: gi.currently_read                                                     # needs sage.symbolic
            10
        """
    @staticmethod
    def bound(n, d):
        """
        Helper function for division. Return infinity if denominator is zero.

        TESTS::

            sage: from sage.rings.continued_fraction_gosper import gosper_iterator
            sage: gosper_iterator.bound(1,0)
            +Infinity
        """
