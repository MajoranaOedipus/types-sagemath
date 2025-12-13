from sage.categories.morphism import Morphism as Morphism
from sage.geometry.cone import Cone as Cone
from sage.geometry.fan import Fan as Fan
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism, SchemeMorphism_point as SchemeMorphism_point, SchemeMorphism_polynomial as SchemeMorphism_polynomial
from sage.schemes.generic.scheme import Scheme as Scheme
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence

class SchemeMorphism_point_toric_field(SchemeMorphism_point, Morphism):
    """
    A point of a toric variety determined by homogeneous coordinates
    in a field.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    - ``X`` -- toric variety or subscheme of a toric variety

    - ``coordinates`` -- list of coordinates in the base field of ``X``

    - ``check`` -- if ``True`` (default), the input will be checked for
      correctness

    OUTPUT: a :class:`SchemeMorphism_point_toric_field`

    TESTS::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1(1,2,3,4)
        [1 : 2 : 3 : 4]
    """
    def __init__(self, X, coordinates, check: bool = True) -> None:
        """
        See :class:`SchemeMorphism_point_toric_field` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1(1,2,3,4)
            [1 : 2 : 3 : 4]
        """

class SchemeMorphism_polynomial_toric_variety(SchemeMorphism_polynomial, Morphism):
    """
    A morphism determined by homogeneous polynomials.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    Same as for
    :class:`~sage.schemes.toric.morphism.SchemeMorphism_polynomial`.

    OUTPUT: a :class:`~sage.schemes.toric.morphism.SchemeMorphism_polynomial_toric_variety`

    TESTS::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1.inject_variables()
        Defining s, t, x, y
        sage: P1 = P1xP1.subscheme(s - t)
        sage: H = P1xP1.Hom(P1)
        sage: import sage.schemes.toric.morphism as MOR
        sage: MOR.SchemeMorphism_polynomial_toric_variety(H, [s, s, x, y])
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   Closed subscheme of 2-d CPR-Fano toric variety
                covered by 4 affine patches defined by:
          s - t
          Defn: Defined on coordinates by sending [s : t : x : y] to
                [s : s : x : y]
    """
    def __init__(self, parent, polynomials, check: bool = True) -> None:
        """
        See :class:`SchemeMorphism_polynomial_toric_variety` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.inject_variables()
            Defining s, t, x, y
            sage: P1 = P1xP1.subscheme(s - t)
            sage: H = P1xP1.Hom(P1)
            sage: import sage.schemes.toric.morphism as MOR
            sage: MOR.SchemeMorphism_polynomial_toric_variety(H, [s, s, x, y])
            Scheme morphism:
              From: 2-d CPR-Fano toric variety covered by 4 affine patches
              To:   Closed subscheme of 2-d CPR-Fano toric variety
                    covered by 4 affine patches defined by:
              s - t
              Defn: Defined on coordinates by sending [s : t : x : y] to
                    [s : s : x : y]
        """
    def as_fan_morphism(self) -> None:
        """
        Express the morphism as a map defined by a fan morphism.

        OUTPUT: a :class:`SchemeMorphism_polynomial_toric_variety`

        This raises a :exc:`TypeError` if the morphism cannot be written
        in such a way.

        EXAMPLES::

            sage: A1.<z> = toric_varieties.A1()
            sage: P1 = toric_varieties.P1()
            sage: patch = A1.hom([1,z], P1)
            sage: patch.as_fan_morphism()
            Traceback (most recent call last):
            ...
            NotImplementedError: expressing toric morphisms as fan morphisms is
            not implemented yet
        """

class SchemeMorphism_orbit_closure_toric_variety(SchemeMorphism, Morphism):
    """
    The embedding of an orbit closure.

    INPUT:

    - ``parent`` -- the parent homset

    - ``defining_cone`` -- the defining cone

    - ``ray_map`` -- dictionary ``{ambient ray generator: orbit ray
      generator}``. Note that the image of the ambient ray generator
      is not necessarily primitive.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.toric.variety.ToricVariety_field.orbit_closure`
        method of :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: H = P1xP1.fan(1)[0]
        sage: V = P1xP1.orbit_closure(H)
        sage: V.embedding_morphism()
        Scheme morphism:
          From: 1-d toric variety covered by 2 affine patches
          To:   2-d CPR-Fano toric variety covered by 4 affine patches
          Defn: Defined by embedding the torus closure associated to the 1-d
                cone of Rational polyhedral fan in 2-d lattice N.

    TESTS::

        sage: V.embedding_morphism()._reverse_ray_map()
        {N(-1): 3, N(1): 2}
        sage: V.embedding_morphism()._defining_cone
        1-d cone of Rational polyhedral fan in 2-d lattice N
    """
    def __init__(self, parent, defining_cone, ray_map) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P1 = P2.orbit_closure(P2.fan(1)[0])
            sage: P1.embedding_morphism()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined by embedding the torus closure associated to the 1-d cone
                    of Rational polyhedral fan in 2-d lattice N.
        """
    def defining_cone(self):
        """
        Return the cone corresponding to the torus orbit.

        OUTPUT: a cone of the fan of the ambient toric variety

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: cone = P2.fan(1)[0]
            sage: P1 = P2.orbit_closure(cone)
            sage: P1.embedding_morphism().defining_cone()
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: _ is cone
            True
        """
    def as_polynomial_map(self):
        """
        Express the morphism via homogeneous polynomials.

        OUTPUT: a :class:`SchemeMorphism_polynomial_toric_variety`

        This raises a :exc:`TypeError` if the morphism cannot be
        written in terms of homogeneous polynomials.

        The defining polynomials are not necessarily unique. There are
        choices if multiple ambient space ray generators project to
        the same orbit ray generator, and one such choice is made
        implicitly. The orbit embedding can be written as a polynomial
        map if and only if each primitive orbit ray generator is the
        image of at least one primitive ray generator of the ambient
        toric variety.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: V = P2.orbit_closure(P2.fan(1)[0]);  V
            1-d toric variety covered by 2 affine patches
            sage: V.embedding_morphism().as_polynomial_map()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to [0 : z1 : z0]

        If the toric variety is singular, then some orbit closure
        embeddings cannot be written with homogeneous polynomials::

            sage: P2_112 = toric_varieties.P2_112()
            sage: P1 = P2_112.orbit_closure(Cone([(1,0)]))
            sage: P1.embedding_morphism().as_polynomial_map()
            Traceback (most recent call last):
            ...
            TypeError: the embedding cannot be written with homogeneous polynomials
        """
    def pullback_divisor(self, divisor):
        """
        Pull back a toric divisor.

        INPUT:

        - ``divisor`` -- a torus-invariant `\\QQ`-Cartier divisor on the
          codomain of the embedding map

        OUTPUT:

        A divisor on the domain of the embedding map (the orbit
        closure) that is isomorphic to the pull-back divisor `f^*(D)`
        but with possibly different linearization.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P1 = P2.orbit_closure(P2.fan(1)[0])
            sage: f = P1.embedding_morphism()
            sage: D = P2.divisor([1,2,3]); D
            V(x) + 2*V(y) + 3*V(z)
            sage: f.pullback_divisor(D)
            4*V(z0) + 2*V(z1)
        """

class SchemeMorphism_fan_toric_variety(SchemeMorphism, Morphism):
    """
    Construct a morphism determined by a fan morphism.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    - ``parent`` -- Hom-set whose domain and codomain are toric varieties

    - ``fan_morphism`` -- a morphism of fans whose domain and codomain
      fans equal the fans of the domain and codomain in the ``parent``
      Hom-set.

    - ``check`` -- boolean (default: ``True``); whether to
      check the input for consistency

    .. WARNING::

        A fibration is a dominant morphism; if you are interested in
        these then you have to make sure that your fan morphism is
        dominant. For example, this can be achieved by
        :meth:`factoring the morphism
        <sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety.factor>`. See
        :class:`SchemeMorphism_fan_toric_variety_dominant` for
        additional functionality for fibrations.

    OUTPUT: a :class:`~sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety`

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1 = toric_varieties.P1()
        sage: f = P1.hom(matrix([[1,0]]), P1xP1);  f
        Scheme morphism:
          From: 1-d CPR-Fano toric variety covered by 2 affine patches
          To:   2-d CPR-Fano toric variety covered by 4 affine patches
          Defn: Defined by sending Rational polyhedral fan in 1-d lattice N
                to Rational polyhedral fan in 2-d lattice N.
        sage: type(f)
        <class 'sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety'>

    Slightly more explicit construction::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1 = toric_varieties.P1()
        sage: hom_set = P1xP1.Hom(P1)
        sage: fm = FanMorphism(matrix(ZZ, [[1],[0]]), P1xP1.fan(), P1.fan())
        sage: hom_set(fm)
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 1-d lattice N.

        sage: P1xP1.hom(fm, P1)
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 1-d lattice N.
    """
    def __init__(self, parent, fan_morphism, check: bool = True) -> None:
        """
        See :class:`SchemeMorphism_polynomial_toric_variety` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: hom_set = P1xP1.Hom(P1)
            sage: fan_morphism = FanMorphism(matrix(ZZ, [[1],[0]]), P1xP1.fan(), P1.fan())
            sage: from sage.schemes.toric.morphism import SchemeMorphism_fan_toric_variety
            sage: SchemeMorphism_fan_toric_variety(hom_set, fan_morphism)
            Scheme morphism:
              From: 2-d CPR-Fano toric variety covered by 4 affine patches
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                    to Rational polyhedral fan in 1-d lattice N.
        """
    def factor(self):
        '''
        Factor ``self`` into injective * birational * surjective morphisms.

        OUTPUT:

        - a triple of toric morphisms `(\\phi_i, \\phi_b, \\phi_s)`, such that
          `\\phi_s` is surjective, `\\phi_b` is birational, `\\phi_i` is injective,
          and ``self`` is equal to `\\phi_i \\circ \\phi_b \\circ \\phi_s`.

        The intermediate varieties are universal in the following sense. Let
        ``self`` map `X` to `X\'` and let `X_s`, `X_i` sit in between, that is,

        .. MATH::

            X
            \\twoheadrightarrow
            X_s
            \\to
            X_i
            \\hookrightarrow
            X\'.

        Then any toric morphism from `X` coinciding with ``self`` on the maximal
        torus factors through `X_s` and any toric morphism into `X\'` coinciding
        with ``self`` on the maximal torus factors through `X_i`. In particular,
        `X_i` is the closure of the image of ``self`` in `X\'`.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.factor`
        for a description of the toric algorithm.

        EXAMPLES:

        We map an affine plane into a projective 3-space in such a way, that it
        becomes "a double cover of a chart of the blow up of one of the
        coordinate planes"::

            sage: A2 = toric_varieties.A2()
            sage: P3 = toric_varieties.P(3)
            sage: m = matrix([(2,0,0), (1,1,0)])
            sage: phi = A2.hom(m, P3)
            sage: phi.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   3-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [x : y] to
                    [x^2*y : y : 1 : 1]

            sage: phi.is_surjective(), phi.is_birational(), phi.is_injective()
            (False, False, False)
            sage: phi_i, phi_b, phi_s = phi.factor()
            sage: phi_s.is_surjective(), phi_b.is_birational(), phi_i.is_injective()
            (True, True, True)
            sage: prod(phi.factor()) == phi
            True

        Double cover (surjective)::

            sage: phi_s.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d affine toric variety
              Defn: Defined on coordinates by sending [x : y] to [x^2 : y]

        Blowup chart (birational)::

            sage: phi_b.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d toric variety covered by 3 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to [1 : z1 : z0*z1]

        Coordinate plane inclusion (injective)::

            sage: phi_i.as_polynomial_map()
            Scheme morphism:
              From: 2-d toric variety covered by 3 affine patches
              To:   3-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [z0 : z1 : z2] to [z2 : z1 : z0 : z0]
        '''
    def fan_morphism(self):
        """
        Return the defining fan morphism.

        OUTPUT: a :class:`~sage.geometry.fan_morphism.FanMorphism`

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: f = P1xP1.hom(matrix([[1],[0]]), P1)
            sage: f.fan_morphism()
            Fan morphism defined by the matrix
            [1]
            [0]
            Domain fan: Rational polyhedral fan in 2-d lattice N
            Codomain fan: Rational polyhedral fan in 1-d lattice N
        """
    def as_polynomial_map(self):
        """
        Express the morphism via homogeneous polynomials.

        OUTPUT: a :class:`SchemeMorphism_polynomial_toric_variety`

        This raises a :exc:`TypeError` if the morphism cannot be written
        in terms of homogeneous polynomials.

        EXAMPLES::

            sage: A1 = toric_varieties.A1()
            sage: square = A1.hom(matrix([[2]]), A1)
            sage: square.as_polynomial_map()
            Scheme endomorphism of 1-d affine toric variety
              Defn: Defined on coordinates by sending [z] to [z^2]

            sage: P1 = toric_varieties.P1()
            sage: patch = A1.hom(matrix([[1]]), P1)
            sage: patch.as_polynomial_map()
            Scheme morphism:
              From: 1-d affine toric variety
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined on coordinates by sending [z] to [z : 1]
        """
    def is_bundle(self):
        """
        Check if ``self`` is a bundle.

        See :meth:`~sage.geometry.fan_morphism.FanMorphism.is_bundle`
        for fan morphisms for details.

        OUTPUT: ``True`` if ``self`` is a bundle, ``False`` otherwise

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_bundle()
            True
        """
    def is_fibration(self):
        """
        Check if ``self`` is a fibration.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_fibration`
        for fan morphisms for details.

        OUTPUT: ``True`` if ``self`` is a fibration, ``False`` otherwise

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_fibration()
            True
        """
    def is_injective(self):
        """
        Check if ``self`` is injective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_injective`
        for fan morphisms for a description of the toric algorithm.

        OUTPUT: boolean; whether ``self`` is injective

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_injective()
            False

            sage: X = toric_varieties.A(2)
            sage: m = identity_matrix(2)
            sage: f = X.hom(m, X)
            sage: f.is_injective()
            True

            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: f = Y.hom(m, X)
            sage: f.is_injective()
            False
        """
    def is_surjective(self):
        """
        Check if ``self`` is surjective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_surjective`
        for fan morphisms for a description of the toric algorithm.

        OUTPUT: boolean; whether ``self`` is surjective

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_surjective()
            True

            sage: X = toric_varieties.A(2)
            sage: m = identity_matrix(2)
            sage: f = X.hom(m, X)
            sage: f.is_surjective()
            True

            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: f = Y.hom(m, X)
            sage: f.is_surjective()
            False
        """
    def is_birational(self):
        """
        Check if ``self`` is birational.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_birational`
        for fan morphisms for a description of the toric algorithm.

        OUTPUT: boolean; whether ``self`` is birational

        EXAMPLES::

            sage: dP8 = toric_varieties.dP8()
            sage: P2 = toric_varieties.P2()
            sage: dP8.hom(identity_matrix(2), P2).is_birational()
            True

            sage: X = toric_varieties.A(2)
            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: m = identity_matrix(2)
            sage: f = Y.hom(m, X)
            sage: f.is_birational()
            True
        """
    def is_dominant(self):
        """
        Return whether ``self`` is dominant.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_dominant`
        for fan morphisms for a description of the toric algorithm.

        OUTPUT: boolean; whether ``self`` is a dominant scheme morphism

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: A1 = toric_varieties.A1()
            sage: phi = A1.hom(identity_matrix(1), P1);  phi
            Scheme morphism:
              From: 1-d affine toric variety
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined by sending Rational polyhedral fan in 1-d lattice N
                    to Rational polyhedral fan in 1-d lattice N.
            sage: phi.is_dominant()
            True
            sage: phi.is_surjective()
            False
        """
    def pullback_divisor(self, divisor):
        """
        Pull back a toric divisor.

        INPUT:

        - ``divisor`` -- a torus-invariant `\\QQ`-Cartier divisor on the
          codomain of ``self``

        OUTPUT: the pull-back divisor `f^*(D)`

        EXAMPLES::

            sage: A2_Z2 = toric_varieties.A2_Z2()
            sage: A2 = toric_varieties.A2()
            sage: f = A2.hom(matrix([[1,0], [1,2]]), A2_Z2)
            sage: f.pullback_divisor(A2_Z2.divisor(0))
            V(x)

            sage: A1 = toric_varieties.A1()
            sage: square = A1.hom(matrix([[2]]), A1)
            sage: D = A1.divisor(0);  D
            V(z)
            sage: square.pullback_divisor(D)
            2*V(z)
        """

class SchemeMorphism_fan_toric_variety_dominant(SchemeMorphism_fan_toric_variety):
    """
    Construct a morphism determined by a dominant fan morphism.

    A dominant morphism is one that is surjective onto a dense
    subset. In the context of toric morphisms, this means that it is
    onto the big torus orbit.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    See :class:`SchemeMorphism_fan_toric_variety`. The given fan
    morphism :meth:`must be dominant
    <sage.geometry.fan_morphism.FanMorphism.is_dominant>`.

    OUTPUT: a :class:`~sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety_dominant`

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: dP8 = toric_varieties.dP8()
        sage: f = dP8.hom(identity_matrix(2), P2);  f
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   2-d CPR-Fano toric variety covered by 3 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 2-d lattice N.
        sage: type(f)
        <class 'sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety_dominant'>
    """
    @cached_method
    def fiber_generic(self):
        '''
        Return the generic fiber.

        OUTPUT:

        - a tuple `(X, n)`, where `X` is a :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>` with the
          embedding morphism into domain of ``self`` and `n` is an integer.

        The fiber over the base point with homogeneous coordinates
        `[1:1:\\cdots:1]` consists of `n` disjoint toric varieties isomorphic to
        `X`. Note that fibers of a dominant toric morphism are isomorphic over
        all points of a fixed torus orbit of its codomain, in particular over
        all points of the maximal torus, so it makes sense to talk about "the
        generic" fiber.

        The embedding of `X` is a toric morphism with
        the :meth:`~sage.geometry.fan_morphism.FanMorphism.domain_fan`
        being the
        :meth:`~sage.geometry.fan_morphism.FanMorphism.kernel_fan` of
        the defining fan morphism. By contrast, embeddings of fiber components
        over lower-dimensional torus orbits of the image are not toric
        morphisms. Use :meth:`fiber_component` for the latter
        (non-generic) fibers.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fiber = P1xP1.hom(matrix([[1],[0]]), P1).fiber_generic()
            sage: fiber
            (1-d toric variety covered by 2 affine patches, 1)
            sage: f = fiber[0].embedding_morphism();  f
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined by sending Rational polyhedral fan in Sublattice <N(0, 1)> to
                    Rational polyhedral fan in 2-d lattice N.
            sage: f.as_polynomial_map()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to [1 : 1 : z0 : z1]

            sage: A1 = toric_varieties.A1()
            sage: fan = Fan([(0,1,2)], [(1,1,0), (1,0,1), (1,-1,-1)])
            sage: fan = fan.subdivide(new_rays=[(1,0,0)])
            sage: f = ToricVariety(fan).hom(matrix([[1],[0],[0]]), A1)
            sage: f.fiber_generic()
            (2-d affine toric variety, 1)
            sage: _[0].fan().generating_cones()
            (0-d cone of Rational polyhedral fan in Sublattice <N(0, 1, 0), N(0, 0, 1)>,)
        '''
    def fiber_component(self, domain_cone, multiplicity: bool = False):
        """
        Return a fiber component corresponding to ``domain_cone``.

        INPUT:

        - ``domain_cone`` -- a cone of the domain fan of ``self``

        - ``multiplicity`` -- boolean (default: ``False``); whether to return
          the number of fiber components corresponding to ``domain_cone`` as well

        OUTPUT:

        - either `X` or a tuple `(X, n)`, where `X` is a :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>` with the
          embedding morphism into domain of ``self`` and `n` is an integer.

        Let `\\phi: \\Sigma \\to \\Sigma'` be the :class:`fan morphism
        <sage.geometry.fan_morphism.FanMorphism>` corresponding to
        ``self``. Let `\\sigma \\in \\Sigma` and `\\sigma' \\in \\Sigma'` be
        the :meth:`~sage.geometry.fan_morphism.FanMorphism.image_cone`
        of `\\sigma`.  The fiber over any point of the torus orbit corresponding
        to `\\sigma'` consists of `n` isomorphic connected components with each
        component being a union of toric varieties intersecting along
        their torus invariant subvarieties. The latter correspond to
        :meth:`~sage.geometry.fan_morphism.FanMorphism.preimage_cones` of
        `\\sigma'` and `X` is one of the `n` components corresponding to
        `\\sigma`. The irreducible components correspond to
        :meth:`~sage.geometry.fan_morphism.FanMorphism.primitive_preimage_cones`.

        EXAMPLES::

            sage: polytope = LatticePolytope(
            ....:     [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ....:      (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope)
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0], [1,0], [0,0], [0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
            sage: ffm = fibration.fan_morphism()
            sage: primitive_cones = ffm.primitive_preimage_cones(P2.fan(1)[0])
            sage: primitive_cone = primitive_cones[0]
            sage: fibration.fiber_component(primitive_cone)
            2-d toric variety covered by 4 affine patches
            sage: fibration.fiber_component(primitive_cone, True)
            (2-d toric variety covered by 4 affine patches, 1)

            sage: for primitive_cone in primitive_cones:
            ....:     print(fibration.fiber_component(primitive_cone))
            2-d toric variety covered by 4 affine patches
            2-d toric variety covered by 3 affine patches
            2-d toric variety covered by 3 affine patches
        """
    @cached_method
    def fiber_dimension(self, codomain_cone):
        """
        Return the dimension of the fiber over a particular torus
        orbit in the base.

        INPUT:

        - ``codomain_cone`` -- a cone `\\sigma` of the codomain,
          specifying a torus orbit `O(\\sigma)`

        OUTPUT:

        An integer. The dimension of the fiber over the torus orbit
        corresponding to ``codomain_cone``. If the fiber is the empty
        set, ``-1`` is returned. Note that all fibers over this torus
        orbit are isomorphic, and therefore have the same dimension.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: f = P1xP1.hom(matrix([[1],[0]]), P1)
            sage: f.fiber_dimension(P1.fan(0)[0])
            1
            sage: f.fiber_dimension(P1.fan(1)[0])
            1
            sage: f.fiber_dimension(P1.fan(1)[1])
            1

        Here is a more complicated example that is not a flat fibration::

            sage: A2_Z2 = toric_varieties.A2_Z2()
            sage: O2_P1 = A2_Z2.resolve(new_rays=[(1,1)])
            sage: blowup = O2_P1.hom(identity_matrix(2), A2_Z2)
            sage: blowup.fiber_dimension(A2_Z2.fan(0)[0])
            0
            sage: blowup.fiber_dimension(A2_Z2.fan(1)[0])
            0
            sage: blowup.fiber_dimension(A2_Z2.fan(2)[0])
            1

        This corresponds to the three different fibers::

            sage: blowup.fiber_generic()
            (0-d affine toric variety, 1)
            sage: blowup.fiber_component(Cone([(1,0)]))
            0-d affine toric variety
            sage: blowup.fiber_component(Cone([(1,1)]))
            1-d toric variety covered by 2 affine patches
        """
    def fiber_graph(self, codomain_cone):
        """
        Return the fiber over a given torus orbit in the codomain.

        INPUT:

        - ``codomain_cone`` -- a cone `\\sigma` of the codomain,
          specifying a torus orbit `O(\\sigma)`

        OUTPUT:

        A graph whose nodes are the irreducible components of a connected
        component of the fiber over a point of `O(\\sigma)`. If two irreducible
        components intersect, the
        corresponding nodes of the graph are joined by an edge. Note that
        irreducible components do not have to be of the same dimension.

        .. SEEALSO::

            :meth:`~SchemeMorphism_fan_toric_variety_dominant.fiber_component`.

        EXAMPLES::

            sage: polytope = Polyhedron(
            ....:     [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ....:      (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope, lattice=ToricLattice(4))

            sage: P2 = toric_varieties.P2()
            sage: proj34 = block_matrix(2, 1, [zero_matrix(2,2),
            ....:                              identity_matrix(2)])
            sage: fm = FanMorphism(proj34, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)

            sage: fibration.fiber_graph(P2.fan(0)[0])
            Graph on 1 vertex
            sage: for c1 in P2.fan(1):
            ....:     fibration.fiber_graph(c1)
            Graph on 1 vertex
            Graph on 1 vertex
            Graph on 4 vertices

            sage: fibration.fiber_graph(P2.fan(1)[2]).get_vertices()
            {0: 2-d toric variety covered by 4 affine patches,
             1: 2-d toric variety covered by 3 affine patches,
             2: 2-d toric variety covered by 3 affine patches,
             3: 2-d toric variety covered by 4 affine patches}

            sage: fibration
            Scheme morphism:
              From: 4-d toric variety covered by 18 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined by sending Rational polyhedral fan in 4-d lattice N
                    to Rational polyhedral fan in 2-d lattice N.
        """

class SchemeMorphism_fan_fiber_component_toric_variety(SchemeMorphism):
    """
    The embedding of a fiber component of a toric morphism.

    Note that the embedding map of a fiber component of a toric morphism is
    itself not a toric morphism!

    INPUT:

    - ``toric_morphism`` -- a toric morphism; the toric morphism whose
      fiber component we are describing

    - ``defining_cone`` -- a cone of the fan of the domain of
      ``toric_morphism``; see
      :meth:`~SchemeMorphism_fan_toric_variety_dominant.fiber_component` for
      details

    EXAMPLES::

        sage: polytope = Polyhedron(
        ....:     [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
        ....:      (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
        sage: coarse_fan = FaceFan(polytope, lattice=ToricLattice(4))
        sage: P2 = toric_varieties.P2()
        sage: proj24 = matrix([[0,0],[1,0],[0,0],[0,1]])
        sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
        sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
        sage: ffm = fibration.fan_morphism()
        sage: primitive_cones = ffm.primitive_preimage_cones(P2.fan(1)[0])
        sage: primitive_cone = primitive_cones[0]
        sage: fiber_component = fibration.fiber_component(primitive_cone)
        sage: fiber_component
        2-d toric variety covered by 4 affine patches
        sage: fiber_component.embedding_morphism()
        Scheme morphism:
          From: 2-d toric variety covered by 4 affine patches
          To:   4-d toric variety covered by 23 affine patches
          Defn: Defined by embedding a fiber component corresponding to
                1-d cone of Rational polyhedral fan in 4-d lattice N.
        sage: fiber_component.embedding_morphism().as_polynomial_map()
        Scheme morphism:
          From: 2-d toric variety covered by 4 affine patches
          To:   4-d toric variety covered by 23 affine patches
          Defn: Defined on coordinates by sending [z0 : z1 : z2 : z3] to
                [1 : 1 : 1 : 1 : z2 : 0 : 1 : z3 : 1 : 1 : 1 : z1 : z0 : 1 : 1]
        sage: type(fiber_component.embedding_morphism())
        <class 'sage.schemes.toric.morphism.SchemeMorphism_fan_fiber_component_toric_variety'>
    """
    def __init__(self, toric_morphism, defining_cone) -> None:
        """
        The Python constructor.

        TESTS::

            sage: polytope = Polyhedron(
            ....:     [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ....:      (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope, lattice=ToricLattice(4))
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0], [1,0], [0,0], [0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
            sage: primitive_cone = Cone([(-1, 2, -1, 0)])
            sage: fibration.fiber_component(primitive_cone).embedding_morphism()
            Scheme morphism:
              From: 2-d toric variety covered by 3 affine patches
              To:   4-d toric variety covered by 23 affine patches
              Defn: Defined by embedding a fiber component corresponding to
                    1-d cone of Rational polyhedral fan in 4-d lattice N.
        """
    def as_polynomial_map(self):
        """
        Express the embedding morphism via homogeneous polynomials.

        OUTPUT: a :class:`SchemeMorphism_polynomial_toric_variety`

        This raises a :exc:`ValueError` if the morphism cannot be
        written in terms of homogeneous polynomials.

        EXAMPLES::

            sage: polytope = Polyhedron(
            ....:     [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ....:      (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope, lattice=ToricLattice(4))
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0], [1,0], [0,0], [0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)

            sage: primitive_cone = Cone([(0, 1, 0, 0)])
            sage: f = fibration.fiber_component(primitive_cone).embedding_morphism()
            sage: f.as_polynomial_map()
            Scheme morphism:
              From: 2-d toric variety covered by 4 affine patches
              To:   4-d toric variety covered by 23 affine patches
              Defn: Defined on coordinates by sending [z0 : z1 : z2 : z3] to
                    [1 : 1 : 1 : 1 : z2 : 0 : 1 : z3 : 1 : 1 : 1 : z1 : z0 : 1 : 1]

            sage: primitive_cone = Cone([(-1, 2, -1, 0)])
            sage: f = fibration.fiber_component(primitive_cone).embedding_morphism()
            sage: f.as_polynomial_map()
            Traceback (most recent call last):
            ...
            ValueError: the morphism cannot be written using homogeneous polynomials
        """
    def defining_cone(self):
        """
        Return the cone corresponding to the fiber torus orbit.

        OUTPUT: a cone of the fan of the total space of the toric fibration

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fc = P1xP1.hom(matrix([[1],[0]]), P1).fiber_component(Cone([(1,0)]))
            sage: f = fc.embedding_morphism()
            sage: f.defining_cone().rays()
            N(1, 0)
            in 2-d lattice N
            sage: f.base_cone().rays()
            N(1)
            in 1-d lattice N
        """
    def base_cone(self):
        """
        Return the base cone `\\sigma`.

        The fiber is constant over the base orbit closure `V(\\sigma)`.

        OUTPUT: a cone of the base of the toric fibration

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fc = P1xP1.hom(matrix([[1],[0]]), P1).fiber_component(Cone([(1,0)]))
            sage: f = fc.embedding_morphism()
            sage: f.defining_cone().rays()
            N(1, 0)
            in 2-d lattice N
            sage: f.base_cone().rays()
            N(1)
            in 1-d lattice N
        """
    def pullback_divisor(self, divisor):
        """
        Pull back a toric divisor.

        INPUT:

        - ``divisor`` -- a torus-invariant `\\QQ`-Cartier divisor on the
          codomain of the embedding map

        OUTPUT:

        A divisor on the domain of the embedding map (irreducible
        component of a fiber of a toric morphism) that is isomorphic
        to the pull-back divisor `f^*(D)` but with possibly different
        linearization.

        EXAMPLES::

            sage: A1 = toric_varieties.A1()
            sage: fan = Fan([(0,1,2)], [(1,1,0),(1,0,1),(1,-1,-1)]).subdivide(new_rays=[(1,0,0)])
            sage: f = ToricVariety(fan).hom(matrix([[1],[0],[0]]), A1)
            sage: D = f.domain().divisor([1,1,3,4]); D
            V(z0) + V(z1) + 3*V(z2) + 4*V(z3)
            sage: fc = f.fiber_component(Cone([(1,1,0)]))
            sage: fc.embedding_morphism().pullback_divisor(D)
            4*V(z0) + V(z1) + 4*V(z2)
            sage: fc = f.fiber_component(Cone([(1,0,0)]))
            sage: fc.embedding_morphism().pullback_divisor(D)
            -V(z0) - 3*V(z1) - 3*V(z2)
        """
