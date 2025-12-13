from sage.categories.morphism import Morphism as Morphism

class FiniteFieldVectorSpaceIsomorphism(Morphism):
    """
    Base class of the vector space isomorphism between a finite field
    and a vector space over a subfield of the finite field.
    """
    def is_injective(self):
        """
        EXAMPLES::

            sage: E = GF(9)
            sage: F = GF(3)
            sage: V, phi, psi = E.vector_space(E, map=True)
            sage: phi.is_injective()
            True
        """
    def is_surjective(self):
        """
        EXAMPLES::

            sage: E = GF(9)
            sage: F = GF(3)
            sage: V, phi, psi = E.vector_space(E, map=True)
            sage: phi.is_surjective()
            True
        """

class MorphismVectorSpaceToFiniteField(FiniteFieldVectorSpaceIsomorphism):
    """
    Isomorphisms from vector spaces to finite fields.
    """
    def __init__(self, V, K, C) -> None:
        """
        Initialize.

        INPUT:

        - ``V`` -- vector space

        - ``K`` -- finite field

        - ``C`` -- matrix

        EXAMPLES::

            sage: E = GF(16)
            sage: F = GF(4)
            sage: V, phi, psi = E.vector_space(E, map=True)
            sage: phi
            Isomorphism:
              From: Vector space of dimension 1 over Finite Field in z4 of size 2^4
              To:   Finite Field in z4 of size 2^4
        """

class MorphismFiniteFieldToVectorSpace(FiniteFieldVectorSpaceIsomorphism):
    """
    Isomorphisms from finite fields to vector spaces
    """
    def __init__(self, K, V, C) -> None:
        """
        Initialize.

        INPUT:

        - ``K`` -- finite field GF((p^m)^n)

        - ``V`` -- vector space of rank n over GF(p^m)

        - ``C`` -- matrix

        EXAMPLES::

            sage: E = GF(16)
            sage: F = GF(4)
            sage: V, phi, psi = E.vector_space(E, map=True)
            sage: psi
            Isomorphism:
              From: Finite Field in z4 of size 2^4
              To:   Vector space of dimension 1 over Finite Field in z4 of size 2^4
        """
