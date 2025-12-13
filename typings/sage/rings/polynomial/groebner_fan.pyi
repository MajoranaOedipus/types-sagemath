from .multi_polynomial_ideal import MPolynomialIdeal as MPolynomialIdeal
from .polynomial_ring_constructor import PolynomialRing as PolynomialRing
from _typeshed import Incomplete
from sage.geometry.fan import Fan as Fan
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.interfaces.gfan import gfan as gfan
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from typing import Iterator

def prefix_check(str_list) -> bool:
    """
    Check if any strings in a list are prefixes of another string in
    the list.

    EXAMPLES::

        sage: from sage.rings.polynomial.groebner_fan import prefix_check
        sage: prefix_check(['z1','z1z1'])
        False
        sage: prefix_check(['z1','zz1'])
        True
    """
def max_degree(list_of_polys) -> float:
    """
    Compute the maximum degree of a list of polynomials.

    EXAMPLES::

        sage: from sage.rings.polynomial.groebner_fan import max_degree
        sage: R.<x,y> = PolynomialRing(QQ,2)
        sage: p_list = [x^2-y,x*y^10-x]
        sage: max_degree(p_list)
        11.0
    """

class PolyhedralCone(SageObject):
    cone_dict: Incomplete
    def __init__(self, gfan_polyhedral_cone, ring=...) -> None:
        """
        Convert polymake/gfan data on a polyhedral cone into a sage class.

        Currently (18-03-2008) needs a lot of work.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.facets()
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        """
    def facets(self) -> list:
        """
        Return the inward facet normals of the Groebner cone.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.facets()
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        """
    def ambient_dim(self):
        """
        Return the ambient dimension of the Groebner cone.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.ambient_dim()
            3
        """
    def dim(self):
        """
        Return the dimension of the Groebner cone.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.dim()
            3
        """
    def lineality_dim(self):
        """
        Return the lineality dimension of the Groebner cone. This is
        just the difference between the ambient dimension and the dimension
        of the cone.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.lineality_dim()
            0
        """
    def relative_interior_point(self):
        """
        Return a point in the relative interior of the Groebner cone.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf[0].groebner_cone()
            sage: a.relative_interior_point()
            [1, 1, 1]
        """

class PolyhedralFan(SageObject):
    fan_dict: Incomplete
    def __init__(self, gfan_polyhedral_fan, parameter_indices=None) -> None:
        """
        Convert polymake/gfan data on a polyhedral fan into a sage class.

        INPUT:

        - ``gfan_polyhedral_fan`` -- output from gfan of a polyhedral fan

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: i2 = ideal(x*z + 6*y*z - z^2, x*y + 6*x*z + y*z - z^2, y^2 + x*z + y*z)
            sage: gf2 = i2.groebner_fan(verbose=False)
            sage: pf = gf2.polyhedralfan()
            sage: pf.rays()
            [[-1, 0, 1], [-1, 1, 0], [1, -2, 1], [1, 1, -2], [2, -1, -1]]
        """
    def ambient_dim(self):
        """
        Return the ambient dimension of the Groebner fan.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf.polyhedralfan()
            sage: a.ambient_dim()
            3
        """
    def dim(self):
        """
        Return the dimension of the Groebner fan.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf.polyhedralfan()
            sage: a.dim()
            3
        """
    def lineality_dim(self):
        """
        Return the lineality dimension of the fan. This is the
        dimension of the largest subspace contained in the fan.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-2]).groebner_fan()
            sage: a = gf.polyhedralfan()
            sage: a.lineality_dim()
            0
        """
    def rays(self) -> list:
        """
        A list of rays of the polyhedral fan.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: i2 = ideal(x*z + 6*y*z - z^2, x*y + 6*x*z + y*z - z^2, y^2 + x*z + y*z)
            sage: gf2 = i2.groebner_fan(verbose=False)
            sage: pf = gf2.polyhedralfan()
            sage: pf.rays()
            [[-1, 0, 1], [-1, 1, 0], [1, -2, 1], [1, 1, -2], [2, -1, -1]]
        """
    def cones(self) -> dict:
        """
        A dictionary of cones in which the keys are the cone dimensions.

        For each dimension, the value is a list of the cones,
        where each element consists of a list of ray indices.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 1+x+y+x*y
            sage: I = R.ideal([f+z*f, 2*f+z*f, 3*f+z^2*f])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: PF.cones()
            {1: [[0], [1], [2], [3], [4], [5]], 2: [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [4, 5]]}
        """
    def maximal_cones(self) -> dict:
        """
        A dictionary of the maximal cones in which the keys are the
        cone dimensions.

        For each dimension, the value is a list of
        the maximal cones, where each element consists of a list of ray indices.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 1+x+y+x*y
            sage: I = R.ideal([f+z*f, 2*f+z*f, 3*f+z^2*f])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: PF.maximal_cones()
            {2: [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [4, 5]]}
        """
    def f_vector(self) -> list:
        """
        The f-vector of the fan.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 1+x+y+x*y
            sage: I = R.ideal([f+z*f, 2*f+z*f, 3*f+z^2*f])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: PF.f_vector()
            [1, 6, 12]
        """
    def is_simplicial(self) -> bool:
        """
        Whether the fan is simplicial or not.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 1+x+y+x*y
            sage: I = R.ideal([f+z*f, 2*f+z*f, 3*f+z^2*f])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: PF.is_simplicial()
            True
        """
    def to_RationalPolyhedralFan(self):
        """
        Convert to the RationalPolyhedralFan class, which is more actively
        maintained.

        While the information in each class is essentially the
        same, the methods and implementation are different.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 1+x+y+x*y
            sage: I = R.ideal([f+z*f, 2*f+z*f, 3*f+z^2*f])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: fan = PF.to_RationalPolyhedralFan()
            sage: [tuple(q.facet_normals()) for q in fan]
            [(M(0, -1, 0), M(-1, 0, 0)), (M(0, 0, -1), M(-1, 0, 0)), (M(0, 0, 1), M(-1, 0, 0)), (M(0, 1, 0), M(-1, 0, 0)), (M(0, 0, -1), M(0, -1, 0)), (M(0, 0, 1), M(0, -1, 0)), (M(0, 1, 0), M(0, 0, -1)), (M(0, 1, 0), M(0, 0, 1)), (M(1, 0, 0), M(0, -1, 0)), (M(1, 0, 0), M(0, 0, -1)), (M(1, 0, 0), M(0, 0, 1)), (M(1, 0, 0), M(0, 1, 0))]

        Here we use the RationalPolyhedralFan's Gale_transform method on a tropical
        prevariety.

        .. link

        ::

            sage: fan.Gale_transform()
            [ 1  0  0  0  0  1 -2]
            [ 0  1  0  0  1  0 -2]
            [ 0  0  1  1  0  0 -2]
        """

class InitialForm(SageObject):
    def __init__(self, cone, rays, initial_forms) -> None:
        """
        A system of initial forms from a polynomial system.

        To each form is associated a cone and a list of
        polynomials (the initial form system itself).

        This class is intended for internal use inside of the
        :class:`TropicalPrevariety` class.

        EXAMPLES::

            sage: from sage.rings.polynomial.groebner_fan import InitialForm
            sage: R.<x,y> = QQ[]
            sage: inform = InitialForm([0], [[-1, 0]], [y^2 - 1, y^2 - 2, y^2 - 3])
            sage: inform._cone
            [0]
        """
    def cone(self):
        """
        The cone associated with the initial form system.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([(x+y)^2-1,(x+y)^2-2,(x+y)^2-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: pfi0 = PF.initial_form_systems()[0]
            sage: pfi0.cone()
            [0]
        """
    def rays(self):
        """
        The rays of the cone associated with the initial form system.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([(x+y)^2-1,(x+y)^2-2,(x+y)^2-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: pfi0 = PF.initial_form_systems()[0]
            sage: pfi0.rays()
            [[-1, 0]]
        """
    def internal_ray(self):
        """
        A ray internal to the cone associated with the initial form
        system.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([(x+y)^2-1,(x+y)^2-2,(x+y)^2-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: pfi0 = PF.initial_form_systems()[0]
            sage: pfi0.internal_ray()
            (-1, 0)
        """
    def initial_forms(self):
        """
        The initial forms (polynomials).

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([(x+y)^2-1,(x+y)^2-2,(x+y)^2-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: pfi0 = PF.initial_form_systems()[0]
            sage: pfi0.initial_forms()
            [y^2 - 1, y^2 - 2, y^2 - 3]
        """

def verts_for_normal(normal, poly) -> list:
    """
    Return the exponents of the vertices of a Newton polytope
    that make up the supporting hyperplane for the given outward
    normal.

    EXAMPLES::

        sage: from sage.rings.polynomial.groebner_fan import verts_for_normal
        sage: R.<x,y,z> = PolynomialRing(QQ,3)
        sage: f1 = x*y*z - 1
        sage: f2 = f1*(x^2 + y^2 + 1)
        sage: verts_for_normal([1,1,1],f2)
        [(3, 1, 1), (1, 3, 1)]
    """

class TropicalPrevariety(PolyhedralFan):
    def __init__(self, gfan_polyhedral_fan, polynomial_system, poly_ring, parameters=None) -> None:
        """
        This class is a subclass of the PolyhedralFan class,
        with some additional methods for tropical prevarieties.

        INPUT:

        - ``gfan_polyhedral_fan`` -- output from ``gfan`` of a polyhedral fan
        - ``polynomial_system`` -- list of polynomials
        - ``poly_ring`` -- the polynomial ring of the list of polynomials
        - ``parameters`` -- (optional) list of variables to be considered
          as parameters

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: I = R.ideal([(x+y+z)^2-1,(x+y+z)-x,(x+y+z)-3])
            sage: GF = I.groebner_fan()
            sage: TI = GF.tropical_intersection()
            sage: TI._polynomial_system
            [x^2 + 2*x*y + y^2 + 2*x*z + 2*y*z + z^2 - 1, y + z, x + y + z - 3]
        """
    def initial_form_systems(self) -> list:
        """
        Return a list of systems of initial forms for each cone
        in the tropical prevariety.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([(x+y)^2-1,(x+y)^2-2,(x+y)^2-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: pfi = PF.initial_form_systems()
            sage: for q in pfi:
            ....:     print(q.initial_forms())
            [y^2 - 1, y^2 - 2, y^2 - 3]
            [x^2 - 1, x^2 - 2, x^2 - 3]
            [x^2 + 2*x*y + y^2, x^2 + 2*x*y + y^2, x^2 + 2*x*y + y^2]
        """

def ring_to_gfan_format(input_ring) -> str:
    """
    Convert a ring to gfan's format.

    EXAMPLES::

        sage: R.<w,x,y,z> = QQ[]
        sage: from sage.rings.polynomial.groebner_fan import ring_to_gfan_format
        sage: ring_to_gfan_format(R)
        'Q[w, x, y, z]'
        sage: R2.<x,y> = GF(2)[]
        sage: ring_to_gfan_format(R2)
        'Z/2Z[x, y]'
    """
def ideal_to_gfan_format(input_ring, polys) -> str:
    '''
    Return the ideal in gfan\'s notation.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: polys = [x^2*y - z, y^2*z - x, z^2*x - y]
            sage: from sage.rings.polynomial.groebner_fan import ideal_to_gfan_format
            sage: ideal_to_gfan_format(R, polys)
            \'Q[x, y, z]{x^2*y-z,y^2*z-x,x*z^2-y}\'

        TESTS:

        Test that :issue:`20146` is fixed::

            sage: P = PolynomialRing(QQ,"x11,x12,x13,x14,x15,x21,x22,x23,x24,x25,x31,x32,x33,x34,x35"); x = P.gens(); M = Matrix(3,x)
            sage: I = P.ideal(M.minors(2))
            sage: ideal_to_gfan_format(P,I.gens())
            \'Q[x11, x12, x13, x14, x15, x21, x22, x23, x24, x25, x31, x32, x33, x34, x35]{-x12*x21+x11*x22,-x13*x21+x11*x23,-x14*x21+x11*x24,-x15*x21+x11*x25,-x13*x22+x12*x23,-x14*x22+x12*x24,-x15*x22+x12*x25,-x14*x23+x13*x24,-x15*x23+x13*x25,-x15*x24+x14*x25,-x12*x31+x11*x32,-x13*x31+x11*x33,-x14*x31+x11*x34,-x15*x31+x11*x35,-x13*x32+x12*x33,-x14*x32+x12*x34,-x15*x32+x12*x35,-x14*x33+x13*x34,-x15*x33+x13*x35,-x15*x34+x14*x35,-x22*x31+x21*x32,-x23*x31+x21*x33,-x24*x31+x21*x34,-x25*x31+x21*x35,-x23*x32+x22*x33,-x24*x32+x22*x34,-x25*x32+x22*x35,-x24*x33+x23*x34,-x25*x33+x23*x35,-x25*x34+x24*x35}\'
    '''

class GroebnerFan(SageObject):
    def __init__(self, I, is_groebner_basis: bool = False, symmetry=None, verbose: bool = False) -> None:
        """
        This class is used to access capabilities of the program ``Gfan``.

        In addition to computing Groebner fans, ``Gfan`` can compute
        other things in tropical geometry such as tropical prevarieties.

        INPUT:

        - ``I`` -- ideal in a multivariate polynomial ring

        - ``is_groebner_basis`` -- boolean (default: ``False``); if
          ``True``, then I.gens() must be a Groebner basis with respect to the
          standard degree lexicographic term order

        - ``symmetry`` -- (default: ``None``) if not ``None``, describes
          symmetries of the ideal

        - ``verbose`` -- (default: ``False``) if ``True``, printout
          useful info during computations

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: I = R.ideal([x^2*y - z, y^2*z - x, z^2*x - y])
            sage: G = I.groebner_fan(); G
            Groebner fan of the ideal:
            Ideal (x^2*y - z, y^2*z - x, x*z^2 - y) of Multivariate Polynomial Ring in x, y, z over Rational Field

        Here is an example of the use of the tropical_intersection command, and then using the RationalPolyhedralFan
        class to compute the Stanley-Reisner ideal of the tropical prevariety::

            sage: R.<x,y,z> = QQ[]
            sage: I = R.ideal([(x+y+z)^3-1,(x+y+z)^3-x,(x+y+z)-3])
            sage: GF = I.groebner_fan()
            sage: PF = GF.tropical_intersection()
            sage: PF.rays()
            [[-1, 0, 0], [0, -1, 0], [0, 0, -1], [1, 1, 1]]
            sage: RPF = PF.to_RationalPolyhedralFan()
            sage: RPF.Stanley_Reisner_ideal(PolynomialRing(QQ,4,'A, B, C, D'))
            Ideal (A*B, A*C, B*C*D) of Multivariate Polynomial Ring in A, B, C, D over Rational Field
        """
    def __eq__(self, right) -> bool:
        """
        Test equality of Groebner fan objects.

        EXAMPLES::

            sage: R.<q,u> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([q^2-u,u^2-q]).groebner_fan()
            sage: gf2 = R.ideal([u^2-q,q^2-u]).groebner_fan()
            sage: gf.__eq__(gf2)
            True
        """
    def ideal(self):
        """
        Return the ideal the was used to define this Groebner fan.

        EXAMPLES::

            sage: R.<x1,x2> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([x1^3-x2,x2^3-2*x1-2]).groebner_fan()
            sage: gf.ideal()
            Ideal (x1^3 - x2, x2^3 - 2*x1 - 2) of Multivariate Polynomial Ring in x1, x2 over Rational Field
        """
    def weight_vectors(self) -> list:
        """
        Return the weight vectors corresponding to the reduced Groebner
        bases.

        EXAMPLES::

            sage: r3.<x,y,z> = PolynomialRing(QQ,3)
            sage: g = r3.ideal([x^3+y,y^3-z,z^2-x]).groebner_fan()
            sage: g.weight_vectors()
            [(3, 7, 1), (5, 1, 2), (7, 1, 4), (5, 1, 4), (1, 1, 1), (1, 4, 8), (1, 4, 10)]
            sage: r4.<x,y,z,w> = PolynomialRing(QQ,4)
            sage: g4 = r4.ideal([x^3+y,y^3-z,z^2-x,z^3 - w]).groebner_fan()
            sage: len(g4.weight_vectors())
            23
        """
    def ring(self):
        """
        Return the multivariate polynomial ring.

        EXAMPLES::

            sage: R.<x1,x2> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([x1^3-x2,x2^3-x1-2]).groebner_fan()
            sage: gf.ring()
            Multivariate Polynomial Ring in x1, x2 over Rational Field
        """
    def characteristic(self):
        """
        Return the characteristic of the base ring.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: i1 = ideal(x*z + 6*y*z - z^2, x*y + 6*x*z + y*z - z^2, y^2 + x*z + y*z)
            sage: gf = i1.groebner_fan()
            sage: gf.characteristic()
            0
        """
    @cached_method
    def reduced_groebner_bases(self):
        """
        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
            sage: G = R.ideal([x^2*y - z, y^2*z - x, z^2*x - y]).groebner_fan()
            sage: X = G.reduced_groebner_bases()
            sage: len(X)
            33
            sage: X[0]
            [z^15 - z, x - z^9, y - z^11]
            sage: X[0].ideal()
            Ideal (z^15 - z, x - z^9, y - z^11) of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: X[:5]
            [[z^15 - z, x - z^9, y - z^11],
            [y^2 - z^8, x - z^9, y*z^4 - z, -y + z^11],
            [y^3 - z^5, x - y^2*z, y^2*z^3 - y, y*z^4 - z, -y^2 + z^8],
            [y^4 - z^2, x - y^2*z, y^2*z^3 - y, y*z^4 - z, -y^3 + z^5],
            [y^9 - z, y^6*z - y, x - y^2*z, -y^4 + z^2]]
            sage: R3.<x,y,z> = PolynomialRing(GF(2477),3)
            sage: gf = R3.ideal([300*x^3-y,y^2-z,z^2-12]).groebner_fan()
            sage: gf.reduced_groebner_bases()
            [[z^2 - 12, y^2 - z, x^3 + 933*y],
            [y^4 - 12, x^3 + 933*y, -y^2 + z],
            [x^6 - 1062*z, z^2 - 12, -300*x^3 + y],
            [x^12 + 200, -300*x^3 + y, -828*x^6 + z]]
        """
    def gfan(self, cmd: str = 'bases', I=None, format=None):
        """
        Return the ``gfan`` output as a string given an input ``cmd``.

        The default is to produce the list of reduced Groebner bases
        in ``gfan`` format.

        INPUT:

        - ``cmd`` -- string (default: ``'bases'``); GFan command
        - ``I`` -- ideal (default: ``None``)
        - ``format`` -- boolean (default: ``None``); deprecated

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([x^3-y,y^3-x-1]).groebner_fan()
            sage: gf.gfan()
            'Q[x,y]\\n{{\\ny^9-1-y+3*y^3-3*y^6,\\nx+1-y^3}\\n,\\n{\\nx^3-y,\\ny^3-1-x}\\n,\\n{\\nx^9-1-x,\\ny-x^3}\\n}\\n'
        """
    def __iter__(self) -> Iterator:
        """
        Return an iterator for the reduced Groebner bases.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([x^3-y,y^3-x-1]).groebner_fan()
            sage: a = gf.__iter__()
            sage: next(a)
            [y^9 - 3*y^6 + 3*y^3 - y - 1, -y^3 + x + 1]
        """
    def __getitem__(self, i):
        """
        Get a reduced groebner basis.

        EXAMPLES::

            sage: R4.<w1,w2,w3,w4> = PolynomialRing(QQ,4)
            sage: gf = R4.ideal([w1^2-w2,w2^3-1,2*w3-w4^2,w4^2-w1]).groebner_fan()
            sage: gf[0]
            [w4^12 - 1, -w4^4 + w2, -w4^2 + w1, -1/2*w4^2 + w3]
        """
    @cached_method
    def buchberger(self):
        """
        Return a lexicographic reduced Groebner basis for the ideal.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: G = R.ideal([x - z^3, y^2 - x + x^2 - z^3*x]).groebner_fan()
            sage: G.buchberger()
            [-z^3 + y^2, -z^3 + x]
        """
    @cached_method
    def polyhedralfan(self):
        """
        Return a polyhedral fan object corresponding to the reduced
        Groebner bases.

        EXAMPLES::

            sage: R3.<x,y,z> = PolynomialRing(QQ,3)
            sage: gf = R3.ideal([x^8-y^4,y^4-z^2,z^2-1]).groebner_fan()
            sage: pf = gf.polyhedralfan()
            sage: pf.rays()
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        """
    @cached_method
    def homogeneity_space(self):
        """
        Return the homogeneity space of a the list of polynomials that
        define this Groebner fan.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: H = G.homogeneity_space()
        """
    def render(self, file=None, larger: bool = False, shift: int = 0, rgbcolor=(0, 0, 0), polyfill: bool = True, scale_colors: bool = True):
        """
        Render a Groebner fan as sage graphics or save as an xfig file.

        More precisely, the output is a drawing of the Groebner fan
        intersected with a triangle. The corners of the triangle are
        (1,0,0) to the right, (0,1,0) to the left and (0,0,1) at the top.
        If there are more than three variables in the ring we extend these
        coordinates with zeros.

        INPUT:

        - ``file`` -- a filename if you prefer the output
          saved to a file; this will be in xfig format

        - ``shift`` -- shift the positions of the variables in
          the drawing. For example, with shift=1, the corners will be b
          (right), c (left), and d (top). The shifting is done modulo the
          number of variables in the polynomial ring. The default is 0.

        - ``larger`` -- boolean (default: ``False``); if ``True``, make
          the triangle larger so that the shape of the Groebner region
          appears. Affects the xfig file but probably not the sage graphics (?).

        - ``rgbcolor`` -- this will not affect the saved xfig
          file, only the sage graphics produced

        - ``polyfill`` -- whether or not to fill the cones with
          a color determined by the highest degree in each reduced Groebner
          basis for that cone

        - ``scale_colors`` -- if ``True``, this will normalize
          color values to try to maximize the range

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x,z]).groebner_fan()
            sage: test_render = G.render()                                              # needs sage.plot

        ::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: G = R.ideal([x^2*y - z, y^2*z - x, z^2*x - y]).groebner_fan()
            sage: test_render = G.render(larger=True)                                   # needs sage.plot

        TESTS:

        Testing the case where the number of generators is < 3. Currently,
        this should raise a :exc:`NotImplementedError`.

        ::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan().render()              # needs sage.plot
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def render3d(self, verbose: bool = False):
        """
        For a Groebner fan of an ideal in a ring with four variables, this
        function intersects the fan with the standard simplex perpendicular
        to (1,1,1,1), creating a 3d polytope, which is then projected into
        3 dimensions. The edges of this projected polytope are returned as
        lines.

        EXAMPLES::

            sage: R4.<w,x,y,z> = PolynomialRing(QQ,4)
            sage: gf = R4.ideal([w^2-x,x^2-y,y^2-z,z^2-x]).groebner_fan()
            sage: three_d = gf.render3d()                                               # needs sage.plot

        TESTS:

        Now test the case where the number of generators is not 4. Currently,
        this should raise a :exc:`NotImplementedError` error.

        ::

            sage: P.<a,b,c> = PolynomialRing(QQ, 3, order='lex')
            sage: sage.rings.ideal.Katsura(P, 3).groebner_fan().render3d()              # needs sage.plot
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def dimension_of_homogeneity_space(self):
        """
        Return the dimension of the homogeneity space.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G.dimension_of_homogeneity_space()
            0
        """
    def maximal_total_degree_of_a_groebner_basis(self):
        """
        Return the maximal total degree of any Groebner basis.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G.maximal_total_degree_of_a_groebner_basis()
            4
        """
    def minimal_total_degree_of_a_groebner_basis(self):
        """
        Return the minimal total degree of any Groebner basis.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G.minimal_total_degree_of_a_groebner_basis()
            2
        """
    def number_of_reduced_groebner_bases(self):
        """
        Return the number of reduced Groebner bases.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G.number_of_reduced_groebner_bases()
            3
        """
    def number_of_variables(self):
        """
        Return the number of variables.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G.number_of_variables()
            2

        ::

            sage: R = PolynomialRing(QQ,'x',10)
            sage: R.inject_variables(globals())
            Defining x0, x1, x2, x3, x4, x5, x6, x7, x8, x9
            sage: G = ideal([x0 - x9, sum(R.gens())]).groebner_fan()
            sage: G.number_of_variables()
            10
        """
    @cached_method
    def tropical_basis(self, check: bool = True, verbose: bool = False):
        """
        Return a tropical basis for the tropical curve associated to this
        ideal.

        INPUT:

        - ``check`` -- boolean (default: ``True``); if ``True`` raises a
          :exc:`ValueError` exception if this ideal does not define a tropical
          curve (i.e., the condition that R/I has dimension equal to 1 + the
          dimension of the homogeneity space is not satisfied)

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3, order='lex')
            sage: G = R.ideal([y^3-3*x^2, z^3-x-y-2*y^3+2*x^2]).groebner_fan()
            sage: G
            Groebner fan of the ideal:
            Ideal (-3*x^2 + y^3, 2*x^2 - x - 2*y^3 - y + z^3) of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: G.tropical_basis()
            [-3*x^2 + y^3, 2*x^2 - x - 2*y^3 - y + z^3, 3/4*x + y^3 + 3/4*y - 3/4*z^3]
        """
    def interactive(self, *args, **kwds) -> None:
        '''
        See the documentation for self[0].interactive().

        This does not work with the notebook.

        EXAMPLES::

            sage: print("This is not easily doc-testable; please write a good one!")
            This is not easily doc-testable; please write a good one!
        '''
    @cached_method
    def tropical_intersection(self, parameters=None, symmetry_generators=None, *args, **kwds):
        """
        Return information about the tropical intersection of the
        polynomials defining the ideal.

        This is the common refinement of the outward-pointing normal
        fans of the Newton polytopes of the generators of the
        ideal. Note that some people use the inward-pointing normal
        fans.

        INPUT:

        - ``parameters`` -- (optional) tuple of variables to be
          considered as parameters
        - ``symmetry_generators`` -- (optional) generators of the symmetry group

        OUTPUT: a TropicalPrevariety object

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: I = R.ideal(x*z + 6*y*z - z^2, x*y + 6*x*z + y*z - z^2, y^2 + x*z + y*z)
            sage: gf = I.groebner_fan()
            sage: pf = gf.tropical_intersection()
            sage: pf.rays()
            [[-2, 1, 1]]

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: f1 = x*y*z - 1
            sage: f2 = f1*(x^2 + y^2 + z^2)
            sage: f3 = f2*(x + y + z - 1)
            sage: I = R.ideal([f1,f2,f3])
            sage: gf = I.groebner_fan()
            sage: pf = gf.tropical_intersection(symmetry_generators = '(1,2,0),(1,0,2)')
            sage: pf.rays()
            [[-2, 1, 1], [1, -2, 1], [1, 1, -2]]

            sage: R.<x,y,z> = QQ[]
            sage: I = R.ideal([(x+y+z)^2-1,(x+y+z)-x,(x+y+z)-3])
            sage: GF = I.groebner_fan()
            sage: TI = GF.tropical_intersection()
            sage: TI.rays()
            [[-1, 0, 0], [0, -1, -1], [1, 1, 1]]
            sage: GF = I.groebner_fan()
            sage: TI = GF.tropical_intersection(parameters=(y,))
            sage: TI.rays()
            [[-1, 0, 0]]
        """
    def mixed_volume(self):
        """
        Return the mixed volume of the generators of this ideal.

        This is not really an ideal property, it can depend on the
        generators used.

        The generators must give a square system (as many polynomials
        as variables).

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: example_ideal = R.ideal([x^2-y-1,y^2-z-1,z^2-x-1])
            sage: gf = example_ideal.groebner_fan()
            sage: mv = gf.mixed_volume()
            sage: mv
            8

            sage: R2.<x,y> = QQ[]
            sage: g1 = 1 - x + x^7*y^3 + 2*x^8*y^4
            sage: g2 = 2 + y + 3*x^7*y^3 + x^8*y^4
            sage: example2 = R2.ideal([g1,g2])
            sage: example2.groebner_fan().mixed_volume()
            15
        """

class ReducedGroebnerBasis(SageObject, list):
    def __init__(self, groebner_fan, gens, gfan_gens) -> None:
        """
        A class for representing reduced Groebner bases as produced by
        ``gfan``.

        INPUT:

        - ``groebner_fan`` -- a GroebnerFan object from an ideal

        - ``gens`` -- the generators of the ideal

        - ``gfan_gens`` -- the generators as a gfan string

        EXAMPLES::

            sage: R.<a,b> = PolynomialRing(QQ,2)
            sage: gf = R.ideal([a^2-b^2,b-a-1]).groebner_fan()
            sage: from sage.rings.polynomial.groebner_fan import ReducedGroebnerBasis
            sage: ReducedGroebnerBasis(gf,gf[0],gf[0]._gfan_gens())
            [b - 1/2, a + 1/2]
        """
    def interactive(self, latex: bool = False, flippable: bool = False, wall: bool = False, inequalities: bool = False, weight: bool = False) -> None:
        """
        Do an interactive walk of the Groebner fan starting at this reduced
        Groebner basis.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: G[0].interactive()      # not tested
            Initializing gfan interactive mode
            *********************************************
            *     Press control-C to return to Sage     *
            *********************************************
            ....
        """
    def groebner_cone(self, restrict: bool = False):
        """
        Return defining inequalities for the full-dimensional Groebner cone
        associated to this marked minimal reduced Groebner basis.

        INPUT:

        - ``restrict`` -- boolean (default: ``False``); if ``True``, add
          an inequality for each coordinate, so that the cone is restricted
          to the positive orthant

        OUTPUT: tuple of integer vectors

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
            sage: poly_cone = G[1].groebner_cone()
            sage: poly_cone.facets()
            [[-1, 2], [1, -1]]
            sage: [g.groebner_cone().facets() for g in G]
            [[[0, 1], [1, -2]], [[-1, 2], [1, -1]], [[-1, 1], [1, 0]]]
            sage: G[1].groebner_cone(restrict=True).facets()
            [[-1, 2], [1, -1]]
        """
    def ideal(self):
        """
        Return the ideal generated by this basis.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: G = R.ideal([x - z^3, y^2 - 13*x]).groebner_fan()
            sage: G[0].ideal()
            Ideal (-13*z^3 + y^2, -z^3 + x) of Multivariate Polynomial Ring in x, y, z over Rational Field
        """
