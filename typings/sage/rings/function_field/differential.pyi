from sage.categories.modules import Modules as Modules
from sage.categories.morphism import Morphism as Morphism
from sage.misc.latex import latex as latex
from sage.sets.family import Family as Family
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FunctionFieldDifferential(ModuleElement):
    """
    Base class for differentials on function fields.

    INPUT:

    - ``f`` -- element of the function field

    - ``t`` -- element of the function field; if `t` is not specified, the generator
      of the base differential is assumed

    EXAMPLES::

        sage: F.<x> = FunctionField(QQ)
        sage: f = x/(x^2 + x + 1)
        sage: f.differential()
        ((-x^2 + 1)/(x^4 + 2*x^3 + 3*x^2 + 2*x + 1)) d(x)

    ::

        sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                      # needs sage.rings.function_field
        sage: L(x).differential()                                                       # needs sage.rings.function_field
        d(x)
        sage: y.differential()                                                          # needs sage.rings.function_field
        ((21/4*x/(x^7 + 27/4))*y^2 + ((3/2*x^7 + 9/4)/(x^8 + 27/4*x))*y + 7/2*x^4/(x^7 + 27/4)) d(x)
    """
    def __init__(self, parent, f, t=None) -> None:
        """
        Initialize the differential `fdt`.

        TESTS::

            sage: F.<x> = FunctionField(GF(7))
            sage: f = x/(x^2 + x + 1)
            sage: w = f.differential()
            sage: TestSuite(w).run()
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: {x.differential(): 1}
            {d(x): 1}
            sage: {y.differential(): 1}                                                 # needs sage.rings.function_field
            {(x*y^2 + 1/x*y) d(x): 1}
        """
    def divisor(self):
        """
        Return the divisor of the differential.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: w = (1/y) * y.differential()                                          # needs sage.rings.function_field
            sage: w.divisor()                                                           # needs sage.rings.function_field
            - Place (1/x, 1/x^3*y^2 + 1/x)
             - Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1)
             - Place (x, y)
             + Place (x + 2, y + 3)
             + Place (x^6 + 3*x^5 + 4*x^4 + 2*x^3 + x^2 + 3*x + 4, y + x^5)

        ::

            sage: F.<x> = FunctionField(QQ)
            sage: w = (1/x).differential()
            sage: w.divisor()                                                           # needs sage.libs.pari
            -2*Place (x)
        """
    def valuation(self, place):
        """
        Return the valuation of the differential at the place.

        INPUT:

        - ``place`` -- a place of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: w = (1/y) * y.differential()                                          # needs sage.rings.function_field
            sage: [w.valuation(p) for p in L.places()]                                  # needs sage.rings.function_field
            [-1, -1, -1, 0, 1, 0]
        """
    def residue(self, place):
        """
        Return the residue of the differential at the place.

        INPUT:

        - ``place`` -- a place of the function field

        OUTPUT: an element of the residue field of the place

        EXAMPLES:

        We verify the residue theorem in a rational function field::

            sage: # needs sage.rings.finite_rings
            sage: F.<x> = FunctionField(GF(4))
            sage: f = 0
            sage: while f == 0:
            ....:     f = F.random_element()
            sage: w = 1/f * f.differential()
            sage: d = f.divisor()
            sage: s = d.support()
            sage: sum([w.residue(p).trace() for p in s])                                # needs sage.rings.function_field
            0

        and in an extension field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: f = 0
            sage: while f == 0:
            ....:     f = L.random_element()
            sage: w = 1/f * f.differential()
            sage: d = f.divisor()
            sage: s = d.support()
            sage: sum([w.residue(p).trace() for p in s])
            0

        and also in a function field of characteristic zero::

            sage: # needs sage.rings.function_field
            sage: R.<x> = FunctionField(QQ)
            sage: L.<Y> = R[]
            sage: F.<y> = R.extension(Y^2 - x^4 - 4*x^3 - 2*x^2 - 1)
            sage: a = 6*x^2 + 5*x + 7
            sage: b = 2*x^6 + 8*x^5 + 3*x^4 - 4*x^3 - 1
            sage: w = y*a/b*x.differential()
            sage: d = w.divisor()
            sage: sum([QQ(w.residue(p)) for p in d.support()])
            0
        """
    def monomial_coefficients(self, copy: bool = True):
        """
        Return a dictionary whose keys are indices of basis elements in the
        support of ``self`` and whose values are the corresponding coefficients.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: d = y.differential()                                                  # needs sage.rings.function_field
            sage: d                                                                     # needs sage.rings.function_field
            ((4*x/(x^7 + 3))*y^2 + ((4*x^7 + 1)/(x^8 + 3*x))*y + x^4/(x^7 + 3)) d(x)
            sage: d.monomial_coefficients()                                             # needs sage.rings.function_field
            {0: (4*x/(x^7 + 3))*y^2 + ((4*x^7 + 1)/(x^8 + 3*x))*y + x^4/(x^7 + 3)}
        """

class FunctionFieldDifferential_global(FunctionFieldDifferential):
    """
    Differentials on global function fields.

    EXAMPLES::

        sage: F.<x> = FunctionField(GF(7))
        sage: f = x/(x^2 + x + 1)
        sage: f.differential()
        ((6*x^2 + 1)/(x^4 + 2*x^3 + 3*x^2 + 2*x + 1)) d(x)

    ::

        sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                      # needs sage.rings.finite_rings sage.rings.function_field
        sage: y.differential()                                                          # needs sage.rings.finite_rings sage.rings.function_field
        (x*y^2 + 1/x*y) d(x)
    """
    def cartier(self):
        """
        Return the image of the differential by the Cartier operator.

        The Cartier operator operates on differentials. Let `x` be a separating
        element of the function field.  If a differential `\\omega` is written
        in prime-power representation
        `\\omega=(f_0^p+f_1^px+\\dots+f_{p-1}^px^{p-1})dx`, then the Cartier
        operator maps `\\omega` to `f_{p-1}dx`. It is known that this definition
        does not depend on the choice of `x`.

        The Cartier operator has interesting properties. Notably, the set of
        exact differentials is precisely the kernel of the Cartier operator and
        logarithmic differentials are stable under the Cartier operation.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: f = x/y
            sage: w = 1/f*f.differential()
            sage: w.cartier() == w
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<x> = FunctionField(GF(4))
            sage: f = x/(x^2 + x + 1)
            sage: w = 1/f*f.differential()
            sage: w.cartier() == w                                                      # needs sage.rings.function_field
            True
        """

class DifferentialsSpace(UniqueRepresentation, Parent):
    """
    Space of differentials of a function field.

    INPUT:

    - ``field`` -- function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                      # needs sage.rings.finite_rings sage.rings.function_field
        sage: L.space_of_differentials()                                                # needs sage.rings.finite_rings sage.rings.function_field
        Space of differentials of Function field in y defined by y^3 + x^3*y + x

    The space of differentials is a one-dimensional module over the function
    field. So a base differential is chosen to represent differentials.
    Usually the generator of the base rational function field is a separating
    element and used to generate the base differential. Otherwise a separating
    element is automatically found and used to generate the base differential
    relative to which other differentials are denoted::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(GF(5))
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^5 - 1/x)
        sage: L(x).differential()
        0
        sage: y.differential()
        d(y)
        sage: (y^2).differential()
        (2*y) d(y)
    """
    Element = FunctionFieldDifferential
    def __init__(self, field, category=None) -> None:
        """
        Initialize the space of differentials of the function field.

        TESTS::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y>=K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: W = L.space_of_differentials()
            sage: TestSuite(W).run()
        """
    def function_field(self):
        """
        Return the function field to which the space of differentials
        is attached.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: S = L.space_of_differentials()
            sage: S.function_field()
            Function field in y defined by y^3 + x^3*y + x
        """
    def basis(self):
        """
        Return a basis.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: S = L.space_of_differentials()
            sage: S.basis()
            Family (d(x),)
        """

class DifferentialsSpace_global(DifferentialsSpace):
    """
    Space of differentials of a global function field.

    INPUT:

    - ``field`` -- function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                      # needs sage.rings.finite_rings sage.rings.function_field
        sage: L.space_of_differentials()                                                # needs sage.rings.finite_rings sage.rings.function_field
        Space of differentials of Function field in y defined by y^3 + x^3*y + x
    """
    Element = FunctionFieldDifferential_global

class DifferentialsSpaceInclusion(Morphism):
    """
    Inclusion morphisms for extensions of function fields.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                    # needs sage.rings.function_field
        sage: OK = K.space_of_differentials()
        sage: OL = L.space_of_differentials()                                           # needs sage.rings.function_field
        sage: OL.coerce_map_from(OK)                                                    # needs sage.rings.function_field
        Inclusion morphism:
          From: Space of differentials of Rational function field in x over Rational Field
          To:   Space of differentials of Function field in y defined by y^2 - x*y + 4*x^3
    """
    def is_injective(self):
        """
        Return ``True``, since the inclusion morphism is injective.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)                                # needs sage.rings.function_field
            sage: OK = K.space_of_differentials()
            sage: OL = L.space_of_differentials()                                       # needs sage.rings.function_field
            sage: OL.coerce_map_from(OK).is_injective()                                 # needs sage.rings.function_field
            True
        """
    def is_surjective(self):
        """
        Return ``True`` if the inclusion morphism is surjective.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: OK = K.space_of_differentials()
            sage: OL = L.space_of_differentials()
            sage: OL.coerce_map_from(OK).is_surjective()
            False
            sage: S.<z> = L[]
            sage: M.<z> = L.extension(z - 1)
            sage: OM = M.space_of_differentials()
            sage: OM.coerce_map_from(OL).is_surjective()
            True
        """
