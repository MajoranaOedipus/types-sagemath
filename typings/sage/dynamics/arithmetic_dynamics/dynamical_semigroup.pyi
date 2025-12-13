from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.semigroups import Semigroups as Semigroups
from sage.dynamics.arithmetic_dynamics.affine_ds import DynamicalSystem_affine as DynamicalSystem_affine
from sage.dynamics.arithmetic_dynamics.generic_ds import DynamicalSystem as DynamicalSystem
from sage.dynamics.arithmetic_dynamics.projective_ds import DynamicalSystem_projective as DynamicalSystem_projective
from sage.misc.classcall_metaclass import typecall as typecall
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent

class DynamicalSemigroup(Parent, metaclass=InheritComparisonClasscallMetaclass):
    """
    A dynamical semigroup defined by a multiple dynamical systems on projective or affine space.

    INPUT:

    - ``ds_data`` -- list or tuple of dynamical systems or objects that define dynamical systems

    OUTPUT:

    :class:`DynamicalSemigroup_affine` if ``ds_data`` only contains dynamical systems
    over affine space; and :class:`DynamicalSemigroup_projective` otherwise.

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: DynamicalSemigroup(([x, y], [x^2, y^2]))
        Dynamical semigroup over Projective Space of dimension 1 over Rational Field
         defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([x^2, y^2], P)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over Rational Field
         defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    ::

        sage: A.<x> = AffineSpace(QQ, 1)
        sage: f = DynamicalSystem_affine(x, A)
        sage: DynamicalSemigroup(f)
        Dynamical semigroup over Affine Space of dimension 1 over Rational Field
         defined by 1 dynamical system:
          Dynamical System of Affine Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x) to (x)

    ::

        sage: A.<x> = AffineSpace(QQ, 1)
        sage: f = DynamicalSystem(x, A)
        sage: g = DynamicalSystem(x^2, A)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Affine Space of dimension 1 over Rational Field
         defined by 2 dynamical systems:
          Dynamical System of Affine Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x) to (x)
          Dynamical System of Affine Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x) to (x^2)

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: X = P.subscheme(x - y)
        sage: f = DynamicalSystem_projective([x, y], X)
        sage: g = DynamicalSystem_projective([x^2, y^2], X)
        sage: DynamicalSemigroup_projective([f, g])
        Dynamical semigroup over Closed subscheme of Projective Space of dimension 1
         over Rational Field defined by: x - y
         defined by 2 dynamical systems:
          Dynamical System of Closed subscheme of Projective Space of dimension 1
           over Rational Field defined by: x - y
             Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Closed subscheme of Projective Space of dimension 1
           over Rational Field defined by: x - y
             Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    If a dynamical semigroup is built from dynamical systems with different base rings,
    all systems will be coerced to the largest base ring::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: Q.<z,w> = ProjectiveSpace(RR, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([z^2, w^2], Q)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over
         Real Field with 53 bits of precision defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1
           over Real Field with 53 bits of precision
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1
           over Real Field with 53 bits of precision
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    ::

        sage: A.<x> = AffineSpace(QQ, 1)
        sage: B.<y> = AffineSpace(RR, 1)
        sage: f = DynamicalSystem(x, A)
        sage: g = DynamicalSystem(y^2, B)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Affine Space of dimension 1 over
         Real Field with 53 bits of precision defined by 2 dynamical systems:
          Dynamical System of Affine Space of dimension 1 over
           Real Field with 53 bits of precision
            Defn: Defined on coordinates by sending (x) to (x)
          Dynamical System of Affine Space of dimension 1 over
           Real Field with 53 bits of precision
            Defn: Defined on coordinates by sending (x) to (x^2)

    If a dynamical semigroup is built from dynamical systems over number fields, a composite number field is created
    and all systems will be coerced to it. This composite number field contains all of the initial number fields::

        sage: # needs sage.rings.number_field
        sage: R.<r> = QQ[]
        sage: K.<k> = NumberField(r^2 - 2)
        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: Q.<x,y> = ProjectiveSpace(K, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([z^2, w^2], Q)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over
         Number Field in k with defining polynomial r^2 - 2 defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Number Field in k with defining polynomial r^2 - 2
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over
           Number Field in k with defining polynomial r^2 - 2
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    ::

        sage: # needs sage.rings.number_field
        sage: R.<r> = QQ[]
        sage: K.<k> = NumberField(r^2 - 2)
        sage: L.<l> = NumberField(r^2 - 3)
        sage: P.<x,y> = ProjectiveSpace(K, 1)
        sage: Q.<z,w> = ProjectiveSpace(L, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([z^2, w^2], Q)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over
         Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
         defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over
           Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    ::

        sage: # needs sage.rings.number_field
        sage: R.<r> = QQ[]
        sage: K.<k> = NumberField(r^2 - 2)
        sage: L.<l> = NumberField(r^2 - 3)
        sage: P.<x> = AffineSpace(K, 1)
        sage: Q.<y> = AffineSpace(L, 1)
        sage: f = DynamicalSystem(x, P)
        sage: g = DynamicalSystem(y^2, Q)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Affine Space of dimension 1 over
         Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
         defined by 2 dynamical systems:
          Dynamical System of Affine Space of dimension 1 over
           Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
            Defn: Defined on coordinates by sending (x) to (x)
          Dynamical System of Affine Space of dimension 1 over
           Number Field in kl with defining polynomial r^4 - 10*r^2 + 1
            Defn: Defined on coordinates by sending (x) to (x^2)

    A dynamical semigroup may contain dynamical systems over function fields::

        sage: R.<r> = QQ[]
        sage: P.<x,y> = ProjectiveSpace(R, 1)
        sage: f = DynamicalSystem([r * x, y], P)
        sage: g = DynamicalSystem([x, r * y], P)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over Univariate
         Polynomial Ring in r over Rational Field defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Univariate Polynomial Ring in r over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (r*x : y)
          Dynamical System of Projective Space of dimension 1 over
           Univariate Polynomial Ring in r over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : r*y)

    ::

        sage: R.<r> = QQ[]
        sage: P.<x,y> = ProjectiveSpace(R, 1)
        sage: f = DynamicalSystem([r * x, y], P)
        sage: g = DynamicalSystem([x, y], P)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over Univariate
         Polynomial Ring in r over Rational Field defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Univariate Polynomial Ring in r over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (r*x : y)
          Dynamical System of Projective Space of dimension 1 over
           Univariate Polynomial Ring in r over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : y)

    ::

        sage: R.<r,s> = QQ[]
        sage: P.<x,y> = ProjectiveSpace(R, 1)
        sage: f = DynamicalSystem([r * x, y], P)
        sage: g = DynamicalSystem([s * x, y], P)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over Multivariate
         Polynomial Ring in r, s over Rational Field defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Multivariate Polynomial Ring in r, s over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (r*x : y)
          Dynamical System of Projective Space of dimension 1 over
           Multivariate Polynomial Ring in r, s over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (s*x : y)

    ::

        sage: R.<r,s> = QQ[]
        sage: P.<x,y> = ProjectiveSpace(R, 1)
        sage: f = DynamicalSystem([r * x, s * y], P)
        sage: g = DynamicalSystem([s * x, r * y], P)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over
         Multivariate Polynomial Ring in r, s over Rational Field
         defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over
           Multivariate Polynomial Ring in r, s over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (r*x : s*y)
          Dynamical System of Projective Space of dimension 1 over
           Multivariate Polynomial Ring in r, s over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (s*x : r*y)

    A dynamical semigroup may contain dynamical systems over finite fields::

        sage: F = FiniteField(5)
        sage: P.<x,y> = ProjectiveSpace(F, 1)
        sage: DynamicalSemigroup(([x, y], [x^2, y^2]))
        Dynamical semigroup over Projective Space of dimension 1 over
         Finite Field of size 5 defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over Finite Field of size 5
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over Finite Field of size 5
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    If a dynamical semigroup is built from dynamical systems over both projective and
    affine spaces, all systems will be homogenized to dynamical systems over projective space::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: A.<z> = AffineSpace(QQ, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem(z^2, A)
        sage: DynamicalSemigroup((f, g))
        Dynamical semigroup over Projective Space of dimension 1 over Rational Field
         defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)

    TESTS::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: DynamicalSemigroup(1)
        Traceback (most recent call last):
        ...
        TypeError: 1 does not define a 'DynamicalSemigroup' object

    ::

        sage: # needs sage.rings.number_field
        sage: R.<r> = QQ[]
        sage: K.<k> = NumberField(r^2 - 2)
        sage: P.<x,y> = ProjectiveSpace(RR, 1)
        sage: Q.<z,w> = ProjectiveSpace(K, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([z^2, w^2], Q)
        sage: DynamicalSemigroup((f, g))
        Traceback (most recent call last):
        ...
        ValueError: given dynamical systems are not automorphic under global composition

    ::

        sage: F = FiniteField(5)
        sage: P.<x,y> = ProjectiveSpace(F, 1)
        sage: Q.<z,w> = ProjectiveSpace(QQ, 1)
        sage: f = DynamicalSystem([x, y], P)
        sage: g = DynamicalSystem([z^2, w^2], Q)
        sage: DynamicalSemigroup((f, g))
        Traceback (most recent call last):
        ...
        ValueError: given dynamical systems are not automorphic under global composition

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: Q.<u,v,w> = ProjectiveSpace(QQ, 2)
        sage: f = DynamicalSystem([x, y])
        sage: g = DynamicalSystem([u^2, v^2, w^2])
        sage: DynamicalSemigroup((f, g))
        Traceback (most recent call last):
        ...
        ValueError: domains of 'DynamicalSystem' objects must be of the same dimension
    """
    @staticmethod
    def __classcall_private__(cls, ds_data): ...
    def __init__(self, systems) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: DynamicalSemigroup(([x, y], [x^2, y^2]))
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field defined by 2 dynamical systems:
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x : y)
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 : y^2)
        """
    def __call__(self, input):
        """
        The result after evaluating this dynamical semigroup on a value.

        INPUT:

        - ``input`` -- one value that can be evaluated
          with the generators of this dynamical semigroup

        OUTPUT: a set of the resulting values after applying all of this
        dynamical semigroup's generators to ``input``

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f(2)
            {(2 : 1), (4 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f([2, 1])
            {(2 : 1), (4 : 1)}

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f(f(2))
            Traceback (most recent call last):
            ...
            TypeError: unable to convert {(4 : 1), (2 : 1)} to an element of Rational Field
        """
    def base_ring(self):
        """
        The base ring of this dynamical semigroup. This is identical
        to the base ring of all of its defining dynamical system.

        OUTPUT: a ring

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.base_ring()
            Rational Field
        """
    def change_ring(self, new_ring):
        """
        Return a new :class:`DynamicalSemigroup` whose generators
        are the initial dynamical systems coerced to ``new_ring``.

        INPUT:

        - ``new_ring`` -- a ring

        OUTPUT:

        A :class:`DynamicalSemigroup` defined by this dynamical
        semigroup's generators, but coerced to ``new_ring``.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.change_ring(RR)
            Dynamical semigroup over Projective Space of dimension 1 over
             Real Field with 53 bits of precision defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over
               Real Field with 53 bits of precision
                Defn: Defined on coordinates by sending (x : y) to (x : y)
              Dynamical System of Projective Space of dimension 1 over
               Real Field with 53 bits of precision
                Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)
        """
    def domain(self):
        """
        Return the domain of the generators of this dynamical semigroup.

        OUTPUT: a subscheme of a projective space or affine space

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.domain()
            Projective Space of dimension 1 over Rational Field
        """
    def codomain(self):
        """
        Return the codomain of the generators of this dynamical semigroup.

        OUTPUT: a subscheme of a projective space or affine space

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.codomain()
            Projective Space of dimension 1 over Rational Field
        """
    def defining_polynomials(self):
        """
        Return the set of polynomials that define the generators of this dynamical semigroup.

        OUTPUT: a set of polynomials

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.defining_polynomials()
            {(x, y), (x^2, y^2)}
        """
    def defining_systems(self):
        """
        Return the generators of this dynamical semigroup.

        OUTPUT: a tuple of dynamical systems

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f.defining_systems()
            (Dynamical System of Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y) to (x : y),
             Dynamical System of Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2))
        """
    def nth_iterate(self, p, n):
        """
        Return a set of values that results from evaluating this dynamical semigroup
        on the value ``p`` a total of ``n`` times.

        INPUT:

        - ``p`` -- a value on which dynamical systems can evaluate
        - ``n`` -- nonnegative integer

        OUTPUT: a set of values

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^2, y^2],))
            sage: f.nth_iterate(2, 0)
            {(2 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^2, y^2],))
            sage: f.nth_iterate(2, 1)
            {(4 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^2, y^2],))
            sage: f.nth_iterate(2, 2)
            {(16 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(2, 0)
            {(2 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(2, 1)
            {(3 : 1), (4 : 1)}

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(2, 2)
            {(5/3 : 1), (2 : 1), (9 : 1), (16 : 1)}

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(2, 3.5)
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(2, -3)
            Traceback (most recent call last):
            ...
            ValueError: -3 must be a nonnegative integer

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: f.nth_iterate(3, 2) == (f * f)(3)
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x + y, x - y], [x^2, y^2]))
            sage: one = QQ(1)
            sage: f.nth_iterate(2, one)
            {(3 : 1), (4 : 1)}
        """
    def orbit(self, p, n):
        """
        If ``n`` is an integer, return `(p, f(p), f^2(p), \\dots, f^n(p))`. If ``n`` is a list or tuple in interval
        notation `[a, b]`, return `(f^a(p), \\dots, f^b(p))`.

        INPUT:

        - ``p`` -- value on which this dynamical semigroup can be evaluated
        - ``n`` -- nonnegative integer or a list or tuple of length 2 describing an
          interval of the number line containing entirely nonnegative integers

        OUTPUT: a tuple of sets of values on the domain of this dynamical semigroup

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, 0)
            ({(2 : 1)},)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, 1)
            ({(2 : 1)}, {(2 : 1), (4 : 1)})

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, 2)
            ({(2 : 1)}, {(2 : 1), (4 : 1)}, {(2 : 1), (4 : 1), (16 : 1)})

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, [1, 2])
            ({(2 : 1), (4 : 1)}, {(2 : 1), (4 : 1), (16 : 1)})

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: one = QQ(1)
            sage: d.orbit(2, one)
            ({(2 : 1)}, {(2 : 1), (4 : 1)})

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, -2)
            Traceback (most recent call last):
            ...
            ValueError: -2 must be a nonnegative integer

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, x)
            Traceback (most recent call last):
            ...
            TypeError: x is not a constant polynomial

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, [1, 2, 3])
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] must be an integer or list or tuple of two integers

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, [-2, 1])
            Traceback (most recent call last):
            ...
            ValueError: [-2, 1] must contain exactly two nonnegative integers

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: d = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: d.orbit(2, [2, 1])
            Traceback (most recent call last):
            ...
            ValueError: [2, 1] cannot be in descending order
        """
    def specialization(self, assignments):
        """
        Return the specialization of the generators of this dynamical semigroup.

        INPUT:

        - ``assignments`` -- argument for specialization of the generators of
          this dynamical semigroup

        OUTPUT: a dynamical semigroup with the specialization of the generators
        of this dynamical semigroup

        EXAMPLES::

            sage: R.<r> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem([r * x, y], P)
            sage: g = DynamicalSystem([x, r * y], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.specialization({r:2})
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (2*x : y)
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (x : 2*y)

        ::

            sage: R.<r> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem([r * x, y], P)
            sage: g = DynamicalSystem([x, y], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.specialization({r:2})
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (2*x : y)
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (x : y)

        ::

            sage: R.<r,s> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem([r * x, y], P)
            sage: g = DynamicalSystem([s * x, y], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.specialization({r:2, s:3})
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (2*x : y)
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (3*x : y)

        ::

            sage: R.<r,s> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem([r * x, s * y], P)
            sage: g = DynamicalSystem([s * x, r * y], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.specialization({s:3})
            Dynamical semigroup over Projective Space of dimension 1 over
             Univariate Polynomial Ring in r over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over
               Univariate Polynomial Ring in r over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (r*x : 3*y)
              Dynamical System of Projective Space of dimension 1 over
               Univariate Polynomial Ring in r over Rational Field
                Defn: Defined on coordinates by sending (x : y) to (3*x : r*y)
        """
    def __mul__(self, other_dynamical_semigroup):
        """
        Return a new :class:`DynamicalSemigroup` that is the result of multiplying
        this dynamical semigroup with another dynamical semigroup of the same type
        using the * operator.

        Let `f` be a dynamical semigroup with generators `\\{ f_1, f_2, \\dots, f_m \\}`
        and `g` be a dynamical semigroup with generators `\\{ g_1, g_2, \\dots, g_n \\}`.
        The product `f * g` has generators
        `\\{ f_i(g_j) : 1 \\leq i \\leq m, 1 \\leq j \\leq n \\}`.

        INPUT:

        - ``other_dynamical_semigroup`` -- a dynamical semigroup

        OUTPUT: :class:`DynamicalSemigroup`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x^10, y^10], P)
            sage: f = DynamicalSemigroup(f1)
            sage: f*f
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field defined by 1 dynamical system:
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^100 : y^100)

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem_affine(x^10, A)
            sage: f = DynamicalSemigroup(f1)
            sage: f*f
            Dynamical semigroup over Affine Space of dimension 1 over Rational Field defined by 1 dynamical system:
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to
                    (x^100)

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x^2 + x * y, y^2 + x * y], P)
            sage: g1 = DynamicalSystem([x^3 + x^2 * y, y^3 + x * y^2], P)
            sage: f = DynamicalSemigroup(f1)
            sage: g = DynamicalSemigroup(g1)
            sage: f*g
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field defined by 1 dynamical system:
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^6 + 2*x^5*y + 2*x^4*y^2 + 2*x^3*y^3 + x^2*y^4 : x^4*y^2 + 2*x^3*y^3 + 2*x^2*y^4 + 2*x*y^5 + y^6)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x^2 + x * y, y^2 + x * y], P)
            sage: f2 = DynamicalSystem([x^2 - x * y, y^2 - x * y], P)
            sage: g1 = DynamicalSystem([x^3 + x^2 * y, y^3 + x * y^2], P)
            sage: g2 = DynamicalSystem([x^3 - x^2 * y, y^3 - x * y^2], P)
            sage: f = DynamicalSemigroup((f1, f2))
            sage: g = DynamicalSemigroup((g1, g2))
            sage: f*g
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field defined by 2 dynamical systems:
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^6 + 2*x^5*y + 2*x^4*y^2 + 2*x^3*y^3 + x^2*y^4 : x^4*y^2 + 2*x^3*y^3 + 2*x^2*y^4 + 2*x*y^5 + y^6)
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^6 - 2*x^5*y + 2*x^3*y^3 - x^2*y^4 : -x^4*y^2 + 2*x^3*y^3 - 2*x*y^5 + y^6)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x^2 + x * y, y^2 - x * y], P)
            sage: g1 = DynamicalSystem([x^3 - x^2 * y, y^3 + x * y^2], P)
            sage: f = DynamicalSemigroup(f1)
            sage: g = DynamicalSemigroup(g1)
            sage: f*g == g*f
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x^2 + x * y, y^2 + x * y], P)
            sage: g1 = DynamicalSystem([x^3 + x^2 * y, y^3 + x * y^2], P)
            sage: h1 = DynamicalSystem([x^4 + x^3 * y, y^4 + x * y^3], P)
            sage: f = DynamicalSemigroup(f1)
            sage: g = DynamicalSemigroup(g1)
            sage: h = DynamicalSemigroup(h1)
            sage: (f*g)*h == f*(g*h)
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x, y], P)
            sage: f = DynamicalSemigroup(f1)
            sage: f*1
            Traceback (most recent call last):
            ...
            TypeError: can only multiply dynamical semigroups with other dynamical semigroups of the same type

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: A.<z> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem_projective([x, y], P)
            sage: g1 = DynamicalSystem_affine(z, A)
            sage: f = DynamicalSemigroup_projective(f1)
            sage: g = DynamicalSemigroup_affine(g1)
            sage: f*g
            Traceback (most recent call last):
            ...
            TypeError: can only multiply dynamical semigroups with other dynamical semigroups of the same type

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: Q.<z,w> = ProjectiveSpace(RR, 1)
            sage: f1 = DynamicalSystem([x, y], P)
            sage: g1 = DynamicalSystem([z, w], Q)
            sage: f = DynamicalSemigroup(f1)
            sage: g = DynamicalSemigroup(g1)
            sage: f*g
            Traceback (most recent call last):
            ...
            ValueError: left dynamical semigroup's domain must equal right dynamical semigroup's codomain

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: Q.<z,w> = ProjectiveSpace(QQ, 1)
            sage: f1 = DynamicalSystem([x, y], P)
            sage: g1 = DynamicalSystem([z, w], Q)
            sage: f = DynamicalSemigroup(f1)
            sage: g = DynamicalSemigroup(g1)
            sage: f*g
            Traceback (most recent call last):
            ...
            ValueError: left dynamical semigroup's domain must equal right dynamical semigroup's codomain
        """
    def __pow__(self, n):
        """
        Return a new dynamical semigroup that is this dynamical semigroup with itself ``n`` times.
        If ``n`` is zero, return a dynamical semigroup with the identity map.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: :class:`DynamicalSemigroup`

        EXAMPLES::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem(x^2, A)
            sage: d = DynamicalSemigroup(f)
            sage: d^2
            Dynamical semigroup over Affine Space of dimension 1 over Rational Field defined by 1 dynamical system:
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to
                    (x^4)

        ::

            sage: A.<x, y, z, w, t, u ,v> = AffineSpace(QQ, 7)
            sage: f = DynamicalSystem([t + u, v - w, x + y, z^2, u * t, v^2 - w^2, x * y * z], A)
            sage: d = DynamicalSemigroup(f)
            sage: d^0
            Dynamical semigroup over Affine Space of dimension 7 over Rational Field defined by 1 dynamical system:
            Dynamical System of Affine Space of dimension 7 over Rational Field
              Defn: Defined on coordinates by sending (x, y, z, w, t, u, v) to
                    (x, y, z, w, t, u, v)

        TESTS::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: d = DynamicalSemigroup(f)
            sage: d*d == d^2
            True

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: d = DynamicalSemigroup(f)
            sage: d^3 * d^2 == d^(3 + 2)
            True

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: d = DynamicalSemigroup(f)
            sage: (d^3)^2 == d^(3 * 2)
            True

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: g1 = DynamicalSystem(x^3 + x - 1, A)
            sage: g2 = DynamicalSystem(x^2 - x + 1, A)
            sage: f = DynamicalSemigroup((f1, f2))
            sage: g = DynamicalSemigroup((g1, g2))
            sage: (f * g) ^ 2 == f^2 * g^2
            False

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: g1 = DynamicalSystem(x^3 + x - 1, A)
            sage: g2 = DynamicalSystem(x^2 - x + 1, A)
            sage: f = DynamicalSemigroup((f1, f2))
            sage: g = DynamicalSemigroup((g1, g2))
            sage: f * g^0 == f
            True

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: g1 = DynamicalSystem(x^3 + x - 1, A)
            sage: g2 = DynamicalSystem(x^2 - x + 1, A)
            sage: f = DynamicalSemigroup((f1, f2))
            sage: g = DynamicalSemigroup((g1, g2))
            sage: g * f^0 == g
            True

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: d = DynamicalSemigroup((f1, f2))
            sage: d^1.5
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f1 = DynamicalSystem(x^2 + 1, A)
            sage: f2 = DynamicalSystem(x^3 - 1, A)
            sage: d = DynamicalSemigroup((f1, f2))
            sage: d^(-1)
            Traceback (most recent call last):
            ...
            ValueError: -1 must be a nonnegative integer

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem(x^2, A)
            sage: d = DynamicalSemigroup(f)
            sage: two = RR(2)
            sage: d^two
            Dynamical semigroup over Affine Space of dimension 1 over Rational Field defined by 1 dynamical system:
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to
                    (x^4)
        """
    def __eq__(self, other):
        """
        Return whether two dynamical semigroups are equal.

        OUTPUT:

        A boolean that is ``True`` if and only if the generators of the two
        dynamical semigroups are equal as sets and no generator is of degree 1.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^2, y^2], [x^3, y^3]))
            sage: g = DynamicalSemigroup(([x^2, y^2], [x^3, y^3]))
            sage: f == g
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^2, y^2], [x^2, y^2]))
            sage: g = DynamicalSemigroup(([x^2, y^2], [x^2, y^2], [x^2, y^2]))
            sage: f == g
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^3, y^3], [x^2, y^2]))
            sage: g = DynamicalSemigroup(([x^2, y^2], [x^3, y^3]))
            sage: f == g
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x^3, y^3], [x^2, y^2]))
            sage: g = DynamicalSemigroup(([x^2, y^2], [y^3, x^3]))
            sage: f == g
            False

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: f == 1
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSemigroup(([x, y], [x^2, y^2]))
            sage: g = DynamicalSemigroup(([x^2, y^2], [x^3, y^3]))
            sage: f == g
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compare dynamical semigroups with at least one generator of degree 1
        """

class DynamicalSemigroup_projective(DynamicalSemigroup):
    """
    A dynamical semigroup defined by a multiple dynamical systems on projective space.

    INPUT:

    - ``ds_data`` -- list or tuple of dynamical systems or objects that define
      dynamical systems over projective space

    OUTPUT: :class:`DynamicalSemigroup_projective`

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: DynamicalSemigroup_projective(([x, y], [x^2, y^2]))
        Dynamical semigroup over Projective Space of dimension 1 over
         Rational Field defined by 2 dynamical systems:
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x : y)
          Dynamical System of Projective Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x : y) to (x^2 : y^2)
    """
    @staticmethod
    def __classcall_private__(cls, ds_data): ...
    def dehomogenize(self, n):
        """
        Return a new :class:`DynamicalSemigroup_projective` with the dehomogenization at ``n`` of
        the generators of this dynamical semigroup.

        INPUT:

        - ``n`` -- tuple of nonnegative integers; if `n` is an integer,
          then the two values of the tuple are assumed to be the same

        OUTPUT: :class:`DynamicalSemigroup_affine`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x, y], P)
            sage: g = DynamicalSystem([x^2, y^2], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.dehomogenize(0)
            Dynamical semigroup over Affine Space of dimension 1 over
             Rational Field defined by 2 dynamical systems:
              Dynamical System of Affine Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (y) to (y)
              Dynamical System of Affine Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (y) to (y^2)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x, y], P)
            sage: g = DynamicalSystem([x^2, y^2], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.dehomogenize(1)
            Dynamical semigroup over Affine Space of dimension 1 over
             Rational Field defined by 2 dynamical systems:
              Dynamical System of Affine Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x) to (x)
              Dynamical System of Affine Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x) to (x^2)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x, y], P)
            sage: g = DynamicalSystem([x^2, y^2], P)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.dehomogenize((1, 0))
            Traceback (most recent call last):
            ...
            ValueError: Scheme morphism:
              From: Affine Space of dimension 1 over Rational Field
              To:   Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to (1/x)
            is not a `DynamicalSystem_affine` object
        """

class DynamicalSemigroup_projective_field(DynamicalSemigroup_projective): ...
class DynamicalSemigroup_projective_finite_field(DynamicalSemigroup_projective_field): ...

class DynamicalSemigroup_affine(DynamicalSemigroup):
    """
    A dynamical semigroup defined by multiple dynamical systems on affine space.

    INPUT:

    - ``ds_data`` -- list or tuple of dynamical systems or objects that define dynamical systems
      over affine space

    OUTPUT: :class:`DynamicalSemigroup_affine`

    EXAMPLES::

        sage: A.<x> = AffineSpace(QQ, 1)
        sage: f = DynamicalSystem(x, A)
        sage: g = DynamicalSystem(x^2, A)
        sage: DynamicalSemigroup_affine((f, g))
        Dynamical semigroup over Affine Space of dimension 1 over
         Rational Field defined by 2 dynamical systems:
          Dynamical System of Affine Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x) to (x)
          Dynamical System of Affine Space of dimension 1 over Rational Field
            Defn: Defined on coordinates by sending (x) to (x^2)
    """
    @staticmethod
    def __classcall_private__(cls, ds_data): ...
    def homogenize(self, n):
        """
        Return a new :class:`DynamicalSemigroup_projective` with the homogenization at ``n`` of
        the generators of this dynamical semigroup.

        INPUT:

        - ``n`` -- tuple of nonnegative integers; if `n` is an integer,
          then the two values of the tuple are assumed to be the same

        OUTPUT: :class:`DynamicalSemigroup_projective`

        EXAMPLES::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem(x + 1, A)
            sage: g = DynamicalSystem(x^2, A)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.homogenize(1)
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x0 : x1) to (x0 + x1 : x1)
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x0 : x1) to (x0^2 : x1^2)

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem(x + 1, A)
            sage: g = DynamicalSystem(x^2, A)
            sage: d = DynamicalSemigroup((f, g))
            sage: d.homogenize((1, 0))
            Dynamical semigroup over Projective Space of dimension 1 over Rational Field
             defined by 2 dynamical systems:
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x0 : x1) to (x1 : x0 + x1)
              Dynamical System of Projective Space of dimension 1 over Rational Field
                Defn: Defined on coordinates by sending (x0 : x1) to (x1^2 : x0^2)
        """

class DynamicalSemigroup_affine_field(DynamicalSemigroup_affine): ...
class DynamicalSemigroup_affine_finite_field(DynamicalSemigroup_affine_field): ...
