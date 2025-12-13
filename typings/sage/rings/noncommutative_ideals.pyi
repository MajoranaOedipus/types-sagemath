import sage.rings.ideal
import sage.rings.ideal_monoid
from sage.categories.category import ZZ as ZZ
from sage.categories.monoids import Monoids as Monoids
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.ideal_monoid import IdealMonoid_c as IdealMonoid_c
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

class IdealMonoid_nc(sage.rings.ideal_monoid.IdealMonoid_c):
    """File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 71)

        Base class for the monoid of ideals over a non-commutative ring.

        .. NOTE::

            This class is essentially the same as
            :class:`~sage.rings.ideal_monoid.IdealMonoid_c`,
            but does not complain about non-commutative rings.

        EXAMPLES::

            sage: MS = MatrixSpace(ZZ,2,2)
            sage: MS.ideal_monoid()
            Monoid of ideals of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
    """
    def __init__(self, R) -> Any:
        """IdealMonoid_nc.__init__(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 87)

        Initialize ``self``.

        INPUT:

        - ``R`` -- a ring

        TESTS::

            sage: from sage.rings.noncommutative_ideals import IdealMonoid_nc
            sage: MS = MatrixSpace(ZZ,2,2)
            sage: IdealMonoid_nc(MS)
            Monoid of ideals of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring"""

class Ideal_nc(sage.rings.ideal.Ideal_generic):
    """File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 150)

        Generic non-commutative ideal.

        All fancy stuff such as the computation of Groebner bases must be
        implemented in sub-classes. See :class:`~sage.algebras.letterplace.letterplace_ideal.LetterplaceIdeal`
        for an example.

        EXAMPLES::

            sage: MS = MatrixSpace(QQ,2,2)
            sage: I = MS*[MS.1,MS.2]; I
            Left Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: [MS.1,MS.2]*MS
            Right Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: MS*[MS.1,MS.2]*MS
            Twosided Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
    """
    def __init__(self, ring, gens, coerce=..., side=...) -> Any:
        """Ideal_nc.__init__(self, ring, gens, coerce=True, side='twosided')

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 192)

        Initialize ``self``.

        INPUT:

        - ``ring`` -- a ring

        - ``gens`` -- list or tuple of elements

        - ``coerce`` -- boolean (default: ``True``); first coerce the given
          list of elements into the given ring

        - ``side`` -- string (default ``'twosided'``); must be ``'left'``,
          ``'right'`` or ``'twosided'``. Determines whether the ideal is a
          left, right or twosided ideal.

        TESTS::

            sage: MS = MatrixSpace(ZZ,2,2)
            sage: from sage.rings.noncommutative_ideals import Ideal_nc
            sage: Ideal_nc(MS,[MS.1,MS.2], side='left')
            Left Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
            sage: Ideal_nc(MS,[MS.1,MS.2], side='right')
            Right Ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring"""
    @overload
    def side(self) -> Any:
        """Ideal_nc.side(self)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 321)

        Return a string that describes the sidedness of this ideal.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IL.side()
            'left'
            sage: IR.side()
            'right'
            sage: IT.side()
            'twosided'"""
    @overload
    def side(self) -> Any:
        """Ideal_nc.side(self)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 321)

        Return a string that describes the sidedness of this ideal.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IL.side()
            'left'
            sage: IR.side()
            'right'
            sage: IT.side()
            'twosided'"""
    @overload
    def side(self) -> Any:
        """Ideal_nc.side(self)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 321)

        Return a string that describes the sidedness of this ideal.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IL.side()
            'left'
            sage: IR.side()
            'right'
            sage: IT.side()
            'twosided'"""
    @overload
    def side(self) -> Any:
        """Ideal_nc.side(self)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 321)

        Return a string that describes the sidedness of this ideal.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IL.side()
            'left'
            sage: IR.side()
            'right'
            sage: IT.side()
            'twosided'"""
    def __eq__(self, right) -> Any:
        """Ideal_nc.__eq__(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 257)

        Ideals of different sidedness do not compare equal. Apart from
        that, the generators are compared.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IT == IL
            False
            sage: IR == [A.1+A.2,A.1^2]*A
            True"""
    def __hash__(self) -> Any:
        """Ideal_nc.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 303)

        Return the hash of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: hash(IT) == hash(IL)
            False
            sage: hash(IR) == hash([A.1^2,A.1+A.2]*A)
            True"""
    def __mul__(self, other) -> Any:
        """Ideal_nc.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 341)

        Multiply ``self`` with ``other``.

        Multiplication of a one-sided ideal with its ring from the other side
        yields a two-sided ideal.

        Let `L` (resp. `R`) be a left (resp. right) ideal, then the product
        `LR` is a twosided ideal generated by `x y`, where `x` (resp. `y`)
        is a generator of `L` (resp. `R`).

        .. TODO::

            The product of left (resp. right) ideals is a left
            (resp. right) ideal. However, these do not necessarily have
            simple generating sets.

        TESTS::

            sage: MS = MatrixSpace(QQ,2,2)
            sage: IL = MS * [2*MS.0,3*MS.1]; IL
            Left Ideal
            (
              [2 0]
              [0 0],
            <BLANKLINE>
              [0 3]
              [0 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: IR = MS.3*MS; IR
            Right Ideal
            (
              [0 0]
              [0 1]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: IL * MS
            Twosided Ideal
            (
              [2 0]
              [0 0],
            <BLANKLINE>
              [0 3]
              [0 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: IL * IR
            Twosided Ideal
            (
              [0 3]
              [0 0]
            )
             of Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: IR * IR
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot multiply non-commutative ideals"""
    def __ne__(self, right) -> Any:
        """Ideal_nc.__ne__(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/noncommutative_ideals.pyx (starting at line 284)

        Ideals of different sidedness do not compare equal. Apart from
        that, the generators are compared.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: A = SteenrodAlgebra(2)
            sage: IR = [A.1+A.2,A.1^2]*A
            sage: IL = A*[A.1+A.2,A.1^2]
            sage: IT = A*[A.1+A.2,A.1^2]*A
            sage: IT != IL
            True
            sage: IR != [A.1+A.2,A.1^2]*A
            False"""
