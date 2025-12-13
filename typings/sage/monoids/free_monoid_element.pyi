from sage.rings.integer import Integer as Integer
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.structure.element import MonoidElement as MonoidElement
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal

def is_FreeMonoidElement(x): ...

class FreeMonoidElement(MonoidElement):
    """
    Element of a free monoid.

    EXAMPLES::

        sage: a = FreeMonoid(5, 'a').gens()
        sage: x = a[0]*a[1]*a[4]**3
        sage: x**3
        a0*a1*a4^3*a0*a1*a4^3*a0*a1*a4^3
        sage: x**0
        1
        sage: x**(-1)
        Traceback (most recent call last):
        ...
        NotImplementedError
    """
    def __init__(self, F, x, check: bool = True) -> None:
        """
        Create the element `x` of the FreeMonoid `F`.

        This should typically be called by a FreeMonoid.
        """
    def __hash__(self):
        """
        TESTS::

            sage: R.<x,y> = FreeMonoid(2)
            sage: hash(x) == hash(((0, 1),))
            True
            sage: hash(y) == hash(((1, 1),))
            True
            sage: hash(x*y) == hash(((0, 1), (1, 1)))
            True
        """
    def __iter__(self):
        """
        Return an iterator which yields tuples of variable and exponent.

        EXAMPLES::

            sage: a = FreeMonoid(5, 'a').gens()
            sage: list(a[0]*a[1]*a[4]**3*a[0])
            [(a0, 1), (a1, 1), (a4, 3), (a0, 1)]
        """
    def __call__(self, *x, **kwds):
        """
        EXAMPLES::

            sage: M.<x,y> = FreeMonoid(2)
            sage: (x*y).substitute(x=1)
            y

            sage: M.<a> = FreeMonoid(1)
            sage: a.substitute(a=5)
            5

            sage: M.<x,y,z> = FreeMonoid(3)
            sage: (x*y).subs(x=1,y=2,z=14)
            2
            sage: (x*y).subs({x:z,y:z})
            z^2

        It is still possible to substitute elements
        that have no common parent::

            sage: M1 = MatrixSpace(ZZ,1,2)                                              # needs sage.modules
            sage: M2 = MatrixSpace(ZZ,2,1)                                              # needs sage.modules
            sage: (x*y).subs({x: M1([1,2]), y: M2([3,4])})                              # needs sage.modules
            [11]

        TESTS::

            sage: M.<x,y> = FreeMonoid(2)
            sage: (x*y)(QQ(4),QQ(5)).parent()
            Rational Field

        The codomain is by default the first parent::

            sage: M.one()(QQ(4),QQ(5)).parent()
            Rational Field

        unless there is no variable and no substitution::

            sage: M = FreeMonoid(0, [])
            sage: M.one()().parent()
            Free monoid on 0 generators ()

        AUTHORS:

        - Joel B. Mohler (2007-10-27)
        """
    def __invert__(self) -> None:
        """
        EXAMPLES::

            sage: a = FreeMonoid(5, 'a').gens()
            sage: x = a[0]*a[1]*a[4]**3
            sage: x**(-1)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __len__(self) -> int:
        """
        Return the degree of the monoid element ``self``, where each
        generator of the free monoid is given degree `1`.

        For example, the length of the identity is `0`, and the
        length of `x_0^2x_1` is `3`.

        EXAMPLES::

            sage: F = FreeMonoid(3, 'a')
            sage: z = F(1)
            sage: len(z)
            0
            sage: a = F.gens()
            sage: len(a[0]**2 * a[1])
            3
        """
    def to_word(self, alph=None):
        """
        Return ``self`` as a word.

        INPUT:

        - ``alph`` -- (optional) the alphabet which the result should
          be specified in

        EXAMPLES::

            sage: M.<x,y,z> = FreeMonoid(3)
            sage: a = x * x * y * x
            sage: w = a.to_word(); w
            word: xxyx
            sage: w.to_monoid_element() == a
            True

        .. SEEALSO::

            :meth:`to_list`
        """
    def to_list(self, indices: bool = False) -> list:
        """
        Return ``self`` as a list of generators.

        If ``self`` equals `x_{i_1} x_{i_2} \\cdots x_{i_n}`, with
        `x_{i_1}, x_{i_2}, \\ldots, x_{i_n}` being some of the
        generators of the free monoid, then this method returns
        the list `[x_{i_1}, x_{i_2}, \\ldots, x_{i_n}]`.

        If the optional argument ``indices`` is set to ``True``,
        then the list `[i_1, i_2, \\ldots, i_n]` is returned instead.

        EXAMPLES::

            sage: M.<x,y,z> = FreeMonoid(3)
            sage: a = x * x * y * x
            sage: w = a.to_list(); w
            [x, x, y, x]
            sage: M.prod(w) == a
            True
            sage: w = a.to_list(indices=True); w
            [0, 0, 1, 0]
            sage: a = M.one()
            sage: a.to_list()
            []

        .. SEEALSO::

            :meth:`to_word`
        """
