import _cython_3_2_1
from typing import Any, ClassVar, overload

__pyx_capi__: dict
benchmark_libc: _cython_3_2_1.cython_function_or_method
benchmark_mt: _cython_3_2_1.cython_function_or_method
current_randstate: _cython_3_2_1.cython_function_or_method
initial_seed: _cython_3_2_1.cython_function_or_method
random: _cython_3_2_1.cython_function_or_method
randstate_stack: list
set_random_seed: _cython_3_2_1.cython_function_or_method
use_urandom: bool

class randstate:
    """randstate(seed=None)

    File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 487)

    The :class:`randstate` class.  This class keeps track of random number
    states and seeds.  Type ``sage.misc.randstate?`` for much more
    information on random numbers in Sage."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 513)

                Initialize a new :class:`randstate` object with the given seed
                (which must be coercible to a Python long).

                If no seed is given, then a seed is automatically selected
                using :func:`os.urandom` if it is available, or the current
                time otherwise.

                EXAMPLES::

                    sage: from sage.misc.randstate import randstate
                    sage: r = randstate(54321); r
                    <sage.misc.randstate.randstate object at 0x...>
                    sage: r.seed()
                    54321
                    sage: r = randstate(); r
                    <sage.misc.randstate.randstate object at 0x...>
                    sage: r.seed()     # random
                    305866218880103397618377824640007711767

                Note that creating a :class:`randstate` with a seed of 0
                is vastly faster than any other seed (over a thousand times
                faster in my test). ::

                    sage: timeit('randstate(0)') # random
                    625 loops, best of 3: 1.38 us per loop
                    sage: timeit('randstate(1)') # random
                    125 loops, best of 3: 3.59 ms per loop
        """
    @overload
    def ZZ_seed(self) -> Any:
        """randstate.ZZ_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 629)

        When called on the current :class:`randstate`, returns a 128-bit
        :mod:`Integer <sage.rings.integer_ring>` suitable for seeding another
        random number generator.

        EXAMPLES::

            sage: set_random_seed(1414)
            sage: current_randstate().ZZ_seed()
            48314508034782595865062786044921182484"""
    @overload
    def ZZ_seed(self) -> Any:
        """randstate.ZZ_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 629)

        When called on the current :class:`randstate`, returns a 128-bit
        :mod:`Integer <sage.rings.integer_ring>` suitable for seeding another
        random number generator.

        EXAMPLES::

            sage: set_random_seed(1414)
            sage: current_randstate().ZZ_seed()
            48314508034782595865062786044921182484"""
    @overload
    def c_rand_double(self) -> double:
        """randstate.c_rand_double(self) -> double

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 846)

        Return a random floating-point number between 0 and 1.

        EXAMPLES::

            sage: set_random_seed(2718281828)
            sage: current_randstate().c_rand_double()
            0.22437207488974298"""
    @overload
    def c_rand_double(self) -> Any:
        """randstate.c_rand_double(self) -> double

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 846)

        Return a random floating-point number between 0 and 1.

        EXAMPLES::

            sage: set_random_seed(2718281828)
            sage: current_randstate().c_rand_double()
            0.22437207488974298"""
    @overload
    def c_random(self) -> int:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def c_random(self) -> Any:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def c_random(self) -> Any:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def long_seed(self) -> Any:
        """randstate.long_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 644)

        When called on the current :class:`randstate`, returns a 128-bit
        Python long suitable for seeding another random number generator.

        EXAMPLES::

            sage: set_random_seed(1618)
            sage: current_randstate().long_seed()
            256056279774514099508607350947089272595"""
    @overload
    def long_seed(self) -> Any:
        """randstate.long_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 644)

        When called on the current :class:`randstate`, returns a 128-bit
        Python long suitable for seeding another random number generator.

        EXAMPLES::

            sage: set_random_seed(1618)
            sage: current_randstate().long_seed()
            256056279774514099508607350947089272595"""
    @overload
    def python_random(self, cls=..., seed=...) -> Any:
        """randstate.python_random(self, cls=None, seed=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 583)

        Return a :class:`random.Random` object.  The first time it is
        called on a given :class:`randstate`, a new :class:`random.Random`
        is created (seeded from the *current* :class:`randstate`);
        the same object is returned on subsequent calls.

        It is expected that ``python_random`` will only be
        called on the current :class:`randstate`.

        INPUT:

        - ``cls`` -- (optional) a class with the same interface as
          :class:`random.Random` (e.g. a subclass thereof) to use as the
          Python RNG interface.  Otherwise the standard :class:`random.Random`
          is used.

        - ``seed`` -- (optional) an integer to seed the :class:`random.Random`
          instance with upon creation; if not specified it is seeded using
          ``ZZ.random_element(1 << 128)``.

        EXAMPLES::

            sage: set_random_seed(5)
            sage: rnd = current_randstate().python_random()
            sage: rnd.random()
            0.013558022446944151
            sage: rnd.randrange(1000)
            544"""
    @overload
    def python_random(self) -> Any:
        """randstate.python_random(self, cls=None, seed=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 583)

        Return a :class:`random.Random` object.  The first time it is
        called on a given :class:`randstate`, a new :class:`random.Random`
        is created (seeded from the *current* :class:`randstate`);
        the same object is returned on subsequent calls.

        It is expected that ``python_random`` will only be
        called on the current :class:`randstate`.

        INPUT:

        - ``cls`` -- (optional) a class with the same interface as
          :class:`random.Random` (e.g. a subclass thereof) to use as the
          Python RNG interface.  Otherwise the standard :class:`random.Random`
          is used.

        - ``seed`` -- (optional) an integer to seed the :class:`random.Random`
          instance with upon creation; if not specified it is seeded using
          ``ZZ.random_element(1 << 128)``.

        EXAMPLES::

            sage: set_random_seed(5)
            sage: rnd = current_randstate().python_random()
            sage: rnd.random()
            0.013558022446944151
            sage: rnd.randrange(1000)
            544"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def set_seed_gap(self) -> Any:
        """randstate.set_seed_gap(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 709)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the GAP random number generator.  If not, seeds
        the generator.

        EXAMPLES::

            sage: set_random_seed(99900000999)
            sage: current_randstate().set_seed_gap()
            sage: gap.Random(1, 10^50)
            1496738263332555434474532297768680634540939580077
            sage: gap(35).SCRRandomString()
            [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
              1, 0, 0, 1, 1, 1, 1, 1, 0, 1 ]"""
    @overload
    def set_seed_gap(self) -> Any:
        """randstate.set_seed_gap(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 709)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the GAP random number generator.  If not, seeds
        the generator.

        EXAMPLES::

            sage: set_random_seed(99900000999)
            sage: current_randstate().set_seed_gap()
            sage: gap.Random(1, 10^50)
            1496738263332555434474532297768680634540939580077
            sage: gap(35).SCRRandomString()
            [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
              1, 0, 0, 1, 1, 1, 1, 1, 0, 1 ]"""
    @overload
    def set_seed_gp(self, gp=...) -> Any:
        """randstate.set_seed_gp(self, gp=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 746)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the random number generator in the given instance
        of gp.  (If no instance is given, uses the one in
        :class:`gp <sage.interfaces.gp.Gp>`.)  If not, seeds the generator.

        EXAMPLES::

            sage: set_random_seed(987654321)
            sage: current_randstate().set_seed_gp()
            sage: gp.random()
            23289294"""
    @overload
    def set_seed_gp(self) -> Any:
        """randstate.set_seed_gp(self, gp=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 746)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the random number generator in the given instance
        of gp.  (If no instance is given, uses the one in
        :class:`gp <sage.interfaces.gp.Gp>`.)  If not, seeds the generator.

        EXAMPLES::

            sage: set_random_seed(987654321)
            sage: current_randstate().set_seed_gp()
            sage: gp.random()
            23289294"""
    @overload
    def set_seed_libc(self, boolforce) -> Any:
        """randstate.set_seed_libc(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 658)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the libc random number generator.  If not, seeds the
        libc random number generator.  (Do not use the libc random
        number generator if you have a choice; its randomness is poor,
        and the random number sequences it produces are not portable
        across operating systems.)

        If the argument ``force`` is ``True``, seeds the generator
        unconditionally.

        EXAMPLES::

            sage: from sage.misc.randstate import _doctest_libc_random
            sage: set_random_seed(0xBAD)
            sage: current_randstate().set_seed_libc(False)
            sage: _doctest_libc_random()   # random
            1070075918"""
    @overload
    def set_seed_libc(self, _False) -> Any:
        """randstate.set_seed_libc(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 658)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the libc random number generator.  If not, seeds the
        libc random number generator.  (Do not use the libc random
        number generator if you have a choice; its randomness is poor,
        and the random number sequences it produces are not portable
        across operating systems.)

        If the argument ``force`` is ``True``, seeds the generator
        unconditionally.

        EXAMPLES::

            sage: from sage.misc.randstate import _doctest_libc_random
            sage: set_random_seed(0xBAD)
            sage: current_randstate().set_seed_libc(False)
            sage: _doctest_libc_random()   # random
            1070075918"""
    @overload
    def set_seed_ntl(self, boolforce) -> Any:
        """randstate.set_seed_ntl(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 683)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the NTL random number generator.  If not, seeds
        the generator.  If the argument ``force`` is ``True``,
        seeds the generator unconditionally.

        EXAMPLES::

            sage: set_random_seed(2008)

        This call is actually redundant; :func:`ntl.ZZ_random` will
        seed the generator itself.  However, we put the call in
        to make the coverage tester happy. ::

            sage: current_randstate().set_seed_ntl(False)
            sage: ntl.ZZ_random(10^40)
            1495283511775355459459209288047895196007"""
    @overload
    def set_seed_ntl(self, _False) -> Any:
        """randstate.set_seed_ntl(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 683)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the NTL random number generator.  If not, seeds
        the generator.  If the argument ``force`` is ``True``,
        seeds the generator unconditionally.

        EXAMPLES::

            sage: set_random_seed(2008)

        This call is actually redundant; :func:`ntl.ZZ_random` will
        seed the generator itself.  However, we put the call in
        to make the coverage tester happy. ::

            sage: current_randstate().set_seed_ntl(False)
            sage: ntl.ZZ_random(10^40)
            1495283511775355459459209288047895196007"""
    def set_seed_pari(self) -> Any:
        """randstate.set_seed_pari(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 787)

        Check to see if ``self`` was the most recent :class:`randstate` to
        seed the Pari random number generator.  If not, seeds the
        generator.

        .. NOTE::

           Since pari 2.4.3, pari's random number generator has
           changed a lot.  the seed output by getrand() is now a
           vector of integers.

        EXAMPLES::

            sage: set_random_seed(5551212)
            sage: current_randstate().set_seed_pari()
            sage: pari.getrand().type()
            't_INT'"""
    def __enter__(self) -> Any:
        """randstate.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 873)

        Use a :class:`randstate` object as a ``with`` statement context
        manager; switches this :class:`randstate` to be the current
        :class:`randstate`, to be switched back on exit from the ``with``
        statement.

        For this purpose, we usually use the ``seed`` alias for
        :class:`randstate`.

        EXAMPLES::

            sage: from sage.misc.randstate import randstate
            sage: seed is randstate
            True
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: with seed(12345):
            ....:     ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983"""
    def __exit__(self, ty, value, traceback) -> Any:
        """randstate.__exit__(self, ty, value, traceback)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 907)

        Use a :class:`randstate` object as a ``with`` statement context
        manager; restores the previous :class:`randstate` as the current
        :class:`randstate`.

        For this purpose, we usually use the ``seed`` alias for
        :class:`randstate`.

        EXAMPLES::

            sage: from sage.misc.randstate import randstate
            sage: seed is randstate
            True
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: with seed(12345):
            ....:     ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983"""

class seed:
    """randstate(seed=None)

    File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 487)

    The :class:`randstate` class.  This class keeps track of random number
    states and seeds.  Type ``sage.misc.randstate?`` for much more
    information on random numbers in Sage."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 513)

                Initialize a new :class:`randstate` object with the given seed
                (which must be coercible to a Python long).

                If no seed is given, then a seed is automatically selected
                using :func:`os.urandom` if it is available, or the current
                time otherwise.

                EXAMPLES::

                    sage: from sage.misc.randstate import randstate
                    sage: r = randstate(54321); r
                    <sage.misc.randstate.randstate object at 0x...>
                    sage: r.seed()
                    54321
                    sage: r = randstate(); r
                    <sage.misc.randstate.randstate object at 0x...>
                    sage: r.seed()     # random
                    305866218880103397618377824640007711767

                Note that creating a :class:`randstate` with a seed of 0
                is vastly faster than any other seed (over a thousand times
                faster in my test). ::

                    sage: timeit('randstate(0)') # random
                    625 loops, best of 3: 1.38 us per loop
                    sage: timeit('randstate(1)') # random
                    125 loops, best of 3: 3.59 ms per loop
        """
    @overload
    def ZZ_seed(self) -> Any:
        """randstate.ZZ_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 629)

        When called on the current :class:`randstate`, returns a 128-bit
        :mod:`Integer <sage.rings.integer_ring>` suitable for seeding another
        random number generator.

        EXAMPLES::

            sage: set_random_seed(1414)
            sage: current_randstate().ZZ_seed()
            48314508034782595865062786044921182484"""
    @overload
    def ZZ_seed(self) -> Any:
        """randstate.ZZ_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 629)

        When called on the current :class:`randstate`, returns a 128-bit
        :mod:`Integer <sage.rings.integer_ring>` suitable for seeding another
        random number generator.

        EXAMPLES::

            sage: set_random_seed(1414)
            sage: current_randstate().ZZ_seed()
            48314508034782595865062786044921182484"""
    @overload
    def c_rand_double(self) -> double:
        """randstate.c_rand_double(self) -> double

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 846)

        Return a random floating-point number between 0 and 1.

        EXAMPLES::

            sage: set_random_seed(2718281828)
            sage: current_randstate().c_rand_double()
            0.22437207488974298"""
    @overload
    def c_rand_double(self) -> Any:
        """randstate.c_rand_double(self) -> double

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 846)

        Return a random floating-point number between 0 and 1.

        EXAMPLES::

            sage: set_random_seed(2718281828)
            sage: current_randstate().c_rand_double()
            0.22437207488974298"""
    @overload
    def c_random(self) -> int:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def c_random(self) -> Any:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def c_random(self) -> Any:
        """randstate.c_random(self) -> int

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 823)

        Return a 31-bit random number.  Intended for internal
        use only; instead of calling ``current_randstate().c_random()``,
        it is equivalent (but probably faster) to call the
        :meth:`random <sage.misc.randstate.random>` method of this
        :class:`randstate` class.

        EXAMPLES::

            sage: set_random_seed(1207)
            sage: current_randstate().c_random()
            2008037228

        We verify the equivalence mentioned above. ::

            sage: from sage.misc.randstate import random
            sage: set_random_seed(1207)
            sage: random()
            2008037228"""
    @overload
    def long_seed(self) -> Any:
        """randstate.long_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 644)

        When called on the current :class:`randstate`, returns a 128-bit
        Python long suitable for seeding another random number generator.

        EXAMPLES::

            sage: set_random_seed(1618)
            sage: current_randstate().long_seed()
            256056279774514099508607350947089272595"""
    @overload
    def long_seed(self) -> Any:
        """randstate.long_seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 644)

        When called on the current :class:`randstate`, returns a 128-bit
        Python long suitable for seeding another random number generator.

        EXAMPLES::

            sage: set_random_seed(1618)
            sage: current_randstate().long_seed()
            256056279774514099508607350947089272595"""
    @overload
    def python_random(self, cls=..., seed=...) -> Any:
        """randstate.python_random(self, cls=None, seed=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 583)

        Return a :class:`random.Random` object.  The first time it is
        called on a given :class:`randstate`, a new :class:`random.Random`
        is created (seeded from the *current* :class:`randstate`);
        the same object is returned on subsequent calls.

        It is expected that ``python_random`` will only be
        called on the current :class:`randstate`.

        INPUT:

        - ``cls`` -- (optional) a class with the same interface as
          :class:`random.Random` (e.g. a subclass thereof) to use as the
          Python RNG interface.  Otherwise the standard :class:`random.Random`
          is used.

        - ``seed`` -- (optional) an integer to seed the :class:`random.Random`
          instance with upon creation; if not specified it is seeded using
          ``ZZ.random_element(1 << 128)``.

        EXAMPLES::

            sage: set_random_seed(5)
            sage: rnd = current_randstate().python_random()
            sage: rnd.random()
            0.013558022446944151
            sage: rnd.randrange(1000)
            544"""
    @overload
    def python_random(self) -> Any:
        """randstate.python_random(self, cls=None, seed=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 583)

        Return a :class:`random.Random` object.  The first time it is
        called on a given :class:`randstate`, a new :class:`random.Random`
        is created (seeded from the *current* :class:`randstate`);
        the same object is returned on subsequent calls.

        It is expected that ``python_random`` will only be
        called on the current :class:`randstate`.

        INPUT:

        - ``cls`` -- (optional) a class with the same interface as
          :class:`random.Random` (e.g. a subclass thereof) to use as the
          Python RNG interface.  Otherwise the standard :class:`random.Random`
          is used.

        - ``seed`` -- (optional) an integer to seed the :class:`random.Random`
          instance with upon creation; if not specified it is seeded using
          ``ZZ.random_element(1 << 128)``.

        EXAMPLES::

            sage: set_random_seed(5)
            sage: rnd = current_randstate().python_random()
            sage: rnd.random()
            0.013558022446944151
            sage: rnd.randrange(1000)
            544"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def seed(self) -> Any:
        """randstate.seed(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 563)

        Return the initial seed of a :class:`randstate` object.  (This is not
        the current state; it does not change when you get random
        numbers.)

        EXAMPLES::

            sage: set_random_seed(0)
            sage: from sage.misc.randstate import randstate
            sage: r = randstate(314159)
            sage: r.seed()
            314159
            sage: r.python_random().random()
            0.111439293741037
            sage: r.seed()
            314159"""
    @overload
    def set_seed_gap(self) -> Any:
        """randstate.set_seed_gap(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 709)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the GAP random number generator.  If not, seeds
        the generator.

        EXAMPLES::

            sage: set_random_seed(99900000999)
            sage: current_randstate().set_seed_gap()
            sage: gap.Random(1, 10^50)
            1496738263332555434474532297768680634540939580077
            sage: gap(35).SCRRandomString()
            [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
              1, 0, 0, 1, 1, 1, 1, 1, 0, 1 ]"""
    @overload
    def set_seed_gap(self) -> Any:
        """randstate.set_seed_gap(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 709)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the GAP random number generator.  If not, seeds
        the generator.

        EXAMPLES::

            sage: set_random_seed(99900000999)
            sage: current_randstate().set_seed_gap()
            sage: gap.Random(1, 10^50)
            1496738263332555434474532297768680634540939580077
            sage: gap(35).SCRRandomString()
            [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
              1, 0, 0, 1, 1, 1, 1, 1, 0, 1 ]"""
    @overload
    def set_seed_gp(self, gp=...) -> Any:
        """randstate.set_seed_gp(self, gp=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 746)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the random number generator in the given instance
        of gp.  (If no instance is given, uses the one in
        :class:`gp <sage.interfaces.gp.Gp>`.)  If not, seeds the generator.

        EXAMPLES::

            sage: set_random_seed(987654321)
            sage: current_randstate().set_seed_gp()
            sage: gp.random()
            23289294"""
    @overload
    def set_seed_gp(self) -> Any:
        """randstate.set_seed_gp(self, gp=None)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 746)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the random number generator in the given instance
        of gp.  (If no instance is given, uses the one in
        :class:`gp <sage.interfaces.gp.Gp>`.)  If not, seeds the generator.

        EXAMPLES::

            sage: set_random_seed(987654321)
            sage: current_randstate().set_seed_gp()
            sage: gp.random()
            23289294"""
    @overload
    def set_seed_libc(self, boolforce) -> Any:
        """randstate.set_seed_libc(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 658)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the libc random number generator.  If not, seeds the
        libc random number generator.  (Do not use the libc random
        number generator if you have a choice; its randomness is poor,
        and the random number sequences it produces are not portable
        across operating systems.)

        If the argument ``force`` is ``True``, seeds the generator
        unconditionally.

        EXAMPLES::

            sage: from sage.misc.randstate import _doctest_libc_random
            sage: set_random_seed(0xBAD)
            sage: current_randstate().set_seed_libc(False)
            sage: _doctest_libc_random()   # random
            1070075918"""
    @overload
    def set_seed_libc(self, _False) -> Any:
        """randstate.set_seed_libc(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 658)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the libc random number generator.  If not, seeds the
        libc random number generator.  (Do not use the libc random
        number generator if you have a choice; its randomness is poor,
        and the random number sequences it produces are not portable
        across operating systems.)

        If the argument ``force`` is ``True``, seeds the generator
        unconditionally.

        EXAMPLES::

            sage: from sage.misc.randstate import _doctest_libc_random
            sage: set_random_seed(0xBAD)
            sage: current_randstate().set_seed_libc(False)
            sage: _doctest_libc_random()   # random
            1070075918"""
    @overload
    def set_seed_ntl(self, boolforce) -> Any:
        """randstate.set_seed_ntl(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 683)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the NTL random number generator.  If not, seeds
        the generator.  If the argument ``force`` is ``True``,
        seeds the generator unconditionally.

        EXAMPLES::

            sage: set_random_seed(2008)

        This call is actually redundant; :func:`ntl.ZZ_random` will
        seed the generator itself.  However, we put the call in
        to make the coverage tester happy. ::

            sage: current_randstate().set_seed_ntl(False)
            sage: ntl.ZZ_random(10^40)
            1495283511775355459459209288047895196007"""
    @overload
    def set_seed_ntl(self, _False) -> Any:
        """randstate.set_seed_ntl(self, bool force)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 683)

        Check to see if ``self`` was the most recent :class:`randstate`
        to seed the NTL random number generator.  If not, seeds
        the generator.  If the argument ``force`` is ``True``,
        seeds the generator unconditionally.

        EXAMPLES::

            sage: set_random_seed(2008)

        This call is actually redundant; :func:`ntl.ZZ_random` will
        seed the generator itself.  However, we put the call in
        to make the coverage tester happy. ::

            sage: current_randstate().set_seed_ntl(False)
            sage: ntl.ZZ_random(10^40)
            1495283511775355459459209288047895196007"""
    def set_seed_pari(self) -> Any:
        """randstate.set_seed_pari(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 787)

        Check to see if ``self`` was the most recent :class:`randstate` to
        seed the Pari random number generator.  If not, seeds the
        generator.

        .. NOTE::

           Since pari 2.4.3, pari's random number generator has
           changed a lot.  the seed output by getrand() is now a
           vector of integers.

        EXAMPLES::

            sage: set_random_seed(5551212)
            sage: current_randstate().set_seed_pari()
            sage: pari.getrand().type()
            't_INT'"""
    def __enter__(self) -> Any:
        """randstate.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 873)

        Use a :class:`randstate` object as a ``with`` statement context
        manager; switches this :class:`randstate` to be the current
        :class:`randstate`, to be switched back on exit from the ``with``
        statement.

        For this purpose, we usually use the ``seed`` alias for
        :class:`randstate`.

        EXAMPLES::

            sage: from sage.misc.randstate import randstate
            sage: seed is randstate
            True
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: with seed(12345):
            ....:     ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983"""
    def __exit__(self, ty, value, traceback) -> Any:
        """randstate.__exit__(self, ty, value, traceback)

        File: /build/sagemath/src/sage/src/sage/misc/randstate.pyx (starting at line 907)

        Use a :class:`randstate` object as a ``with`` statement context
        manager; restores the previous :class:`randstate` as the current
        :class:`randstate`.

        For this purpose, we usually use the ``seed`` alias for
        :class:`randstate`.

        EXAMPLES::

            sage: from sage.misc.randstate import randstate
            sage: seed is randstate
            True
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983
            sage: set_random_seed(-12345)
            sage: ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: with seed(12345):
            ....:     ZZ.random_element(10^30)
            197130468050826967386035500824
            sage: ZZ.random_element(10^30)
            601704412330400807050962541983"""
