from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ImaginaryElement(AdditiveGroupElement):
    """
    An element of :class:`ImaginaryGroup`.

    INPUT:

    - ``parent`` -- a SageMath parent

    - ``imag`` -- an element of parent's base
    """
    def __init__(self, parent, imag) -> None:
        """
        See :class:`ImaginaryGroup` for more information.

        TESTS::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: J(imag=-42)  # indirect doctest
            -42*I
        """
    def imag(self):
        """
        Return the imaginary part of this imaginary element.

        EXAMPLES::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: J(I).imag()                                                           # needs sage.symbolic
            1
            sage: imag_part(J(I))  # indirect doctest                                   # needs sage.symbolic
            1
        """
    def real(self):
        """
        Return the real part (`=0`) of this imaginary element.

        EXAMPLES::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: J(I).real()                                                           # needs sage.symbolic
            0
            sage: real_part(J(I))  # indirect doctest                                   # needs sage.symbolic
            0
        """
    def __hash__(self):
        """
        Return a hash value of this imaginary element.

        TESTS::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: hash(J(I))  # indirect doctest, random                                # needs sage.symbolic
            42
        """
    def __neg__(self):
        """
        Return the negative of this imaginary element.

        TESTS::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: -J(imag=-2)  # indirect doctest
            2*I
        """

class ImaginaryGroup(UniqueRepresentation, Parent):
    """
    A group whose elements are purely imaginary.

    INPUT:

    - ``base`` -- a SageMath parent

    - ``category`` -- a category

    EXAMPLES::

        sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
        sage: J = ImaginaryGroup(ZZ)
        sage: J(0)
        0
        sage: J(imag=100)
        100*I
        sage: J(3*I)                                                                    # needs sage.symbolic
        3*I
        sage: J(1 + 2*I)                                                                # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: 2*I + 1 is not in
        Imaginary Group over Integer Ring
        because it is not purely imaginary
    """
    Element = ImaginaryElement
    @staticmethod
    def __classcall__(cls, base, category=None):
        """
        See :class:`ImaginaryGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)  # indirect doctest
            sage: J.category()
            Category of commutative additive groups
        """
    def __init__(self, base, category) -> None:
        """
        See :class:`ImaginaryGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)  # indirect doctest
        """
    def __hash__(self):
        """
        Return a hash value of this imaginary group.

        TESTS::

            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: J = ImaginaryGroup(ZZ)
            sage: hash(J)  # indirect doctest, random
            42
        """
