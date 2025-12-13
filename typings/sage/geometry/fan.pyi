from collections.abc import Callable, Container
from sage.geometry.cone import Cone as Cone, ConvexRationalPolyhedralCone as ConvexRationalPolyhedralCone, IntegralRayCollection as IntegralRayCollection, normalize_rays as normalize_rays
from sage.geometry.point_collection import PointCollection as PointCollection
from sage.geometry.toric_lattice import ToricLattice as ToricLattice, ToricLattice_generic as ToricLattice_generic
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.timing import walltime as walltime
from sage.modules.free_module import span as span
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

def is_Fan(x) -> bool:
    """
    Check if ``x`` is a Fan.

    INPUT:

    - ``x`` -- anything

    OUTPUT: ``True`` if ``x`` is a fan and ``False`` otherwise

    EXAMPLES::

        sage: from sage.geometry.fan import is_Fan
        sage: is_Fan(1)
        doctest:warning...
        DeprecationWarning: The function is_Fan is deprecated; use 'isinstance(..., RationalPolyhedralFan)' instead.
        See https://github.com/sagemath/sage/issues/38126 for details.
        False
        sage: fan = toric_varieties.P2().fan(); fan                                     # needs palp
        Rational polyhedral fan in 2-d lattice N
        sage: is_Fan(fan)                                                               # needs palp
        True
    """
def Fan(cones, rays=None, lattice=None, check: bool = True, normalize: bool = True, is_complete=None, virtual_rays=None, discard_faces: bool = False, allow_arrangement: bool = False):
    '''
    Construct a rational polyhedral fan.

    .. NOTE::

        Approximate time to construct a fan consisting of `n` cones is `n^2/5`
        seconds. That is half an hour for 100 cones. This time can be
        significantly reduced in the future, but it is still likely to be
        `\\sim n^2` (with, say, `/500` instead of `/5`). If you know that your
        input does form a valid fan, use ``check=False`` option to skip
        consistency checks.

    INPUT:

    - ``cones`` -- list of either
      :class:`Cone<sage.geometry.cone.ConvexRationalPolyhedralCone>` objects
      or lists of integers interpreted as indices of generating rays in
      ``rays``. These must be only **maximal** cones of the fan, unless
      ``discard_faces=True`` or ``allow_arrangement=True`` option is specified;

    - ``rays`` -- list of rays given as list or vectors convertible to the
      rational extension of ``lattice``. If ``cones`` are given by
      :class:`Cone<sage.geometry.cone.ConvexRationalPolyhedralCone>` objects
      ``rays`` may be determined automatically. You still may give them
      explicitly to ensure a particular order of rays in the fan. In this case
      you must list all rays that appear in ``cones``. You can give "extra"
      ones if it is convenient (e.g. if you have a big list of rays for
      several fans), but all "extra" rays will be discarded;

    - ``lattice`` -- :class:`ToricLattice
      <sage.geometry.toric_lattice.ToricLatticeFactory>`, `\\ZZ^n`, or any
      other object that behaves like these. If not specified, an attempt will
      be made to determine an appropriate toric lattice automatically;

    - ``check`` -- by default the input data will be checked for correctness
      (e.g. that intersection of any two given cones is a face of each),
      unless ``allow_arrangement=True`` option is specified. If you
      know for sure that the input is correct, you may significantly decrease
      construction time using ``check=False`` option;

    - ``normalize`` -- you can further speed up construction using
      ``normalize=False`` option. In this case ``cones`` must be a list of
      **sorted** :class:`tuples` and ``rays`` must be immutable primitive
      vectors in ``lattice``. In general, you should not use this option, it
      is designed for code optimization and does not give as drastic
      improvement in speed as the previous one;

    - ``is_complete`` -- every fan can determine on its own if it is complete
      or not, however it can take quite a bit of time for "big" fans with many
      generating cones. On the other hand, in some situations it is known in
      advance that a certain fan is complete. In this case you can pass
      ``is_complete=True`` option to speed up some computations. You may also
      pass ``is_complete=False`` option, although it is less likely to be
      beneficial. Of course, passing a wrong value can compromise the
      integrity of data structures of the fan and lead to wrong results, so
      you should be very careful if you decide to use this option;

    - ``virtual_rays`` -- (optional, computed automatically if needed) a list of
      ray generators to be used for :meth:`virtual_rays`;

    - ``discard_faces`` -- by default, the fan constructor expects the list of
      **maximal** cones, unless ``allow_arrangement=True`` option is specified.
      If you provide "extra" ones and leave ``allow_arrangement=False`` (default)
      and ``check=True`` (default), an exception will be raised.
      If you provide "extra" cones and set ``allow_arrangement=False`` (default)
      and ``check=False``, you may get wrong results as assumptions on internal
      data structures will be invalid. If you want the fan constructor to
      select the maximal cones from the given input, you may provide
      ``discard_faces=True`` option (it works both for ``check=True`` and
      ``check=False``).

    - ``allow_arrangement`` -- by default (``allow_arrangement=False``),
      the fan constructor expects that the intersection of any two given cones is
      a face of each. If ``allow_arrangement=True`` option is specified, then
      construct a rational polyhedralfan from the cone arrangement, so that the
      union of the cones in the polyhedral fan equals to the union of the given
      cones, and each given cone is the union of some cones in the polyhedral fan.

    OUTPUT: a :class:`fan <RationalPolyhedralFan>`

    .. SEEALSO::

        In 2 dimensions you can cyclically order the rays. Hence the
        rays determine a unique maximal fan without having to specify
        the cones, and you can use :func:`Fan2d` to construct this
        fan from just the rays.

    EXAMPLES:

    Let\'s construct a fan corresponding to the projective plane in several
    ways::

        sage: cone1 = Cone([(1,0), (0,1)])
        sage: cone2 = Cone([(0,1), (-1,-1)])
        sage: cone3 = Cone([(-1,-1), (1,0)])
        sage: P2 = Fan([cone1, cone2, cone2])
        Traceback (most recent call last):
        ...
        ValueError: you have provided 3 cones, but only 2 of them are maximal!
        Use discard_faces=True if you indeed need to construct a fan from
        these cones.

    Oops! There was a typo and ``cone2`` was listed twice as a generating cone
    of the fan. If it was intentional (e.g. the list of cones was generated
    automatically and it is possible that it contains repetitions or faces of
    other cones), use ``discard_faces=True`` option::

        sage: P2 = Fan([cone1, cone2, cone2], discard_faces=True)
        sage: P2.ngenerating_cones()
        2

    However, in this case it was definitely a typo, since the fan of
    `\\mathbb{P}^2` has 3 maximal cones::

        sage: P2 = Fan([cone1, cone2, cone3])
        sage: P2.ngenerating_cones()
        3

    Looks better. An alternative way is ::

        sage: rays = [(1,0), (0,1), (-1,-1)]
        sage: cones = [(0,1), (1,2), (2,0)]
        sage: P2a = Fan(cones, rays)
        sage: P2a.ngenerating_cones()
        3
        sage: P2 == P2a
        False

    That may seem wrong, but it is not::

        sage: P2.is_equivalent(P2a)
        True

    See :meth:`~RationalPolyhedralFan.is_equivalent` for details.

    Yet another way to construct this fan is ::

        sage: P2b = Fan(cones, rays, check=False)
        sage: P2b.ngenerating_cones()
        3
        sage: P2a == P2b
        True

    If you try the above examples, you are likely to notice the difference in
    speed, so when you are sure that everything is correct, it is a good idea
    to use ``check=False`` option. On the other hand, it is usually **NOT** a
    good idea to use ``normalize=False`` option::

        sage: P2c = Fan(cones, rays, check=False, normalize=False)
        Traceback (most recent call last):
        ...
        AttributeError: \'tuple\' object has no attribute \'parent\'...

    Yet another way is to use functions :func:`FaceFan` and :func:`NormalFan`
    to construct fans from :class:`lattice polytopes
    <sage.geometry.lattice_polytope.LatticePolytopeClass>`.

    We have not yet used ``lattice`` argument, since if was determined
    automatically::

        sage: P2.lattice()
        2-d lattice N
        sage: P2b.lattice()
        2-d lattice N

    However, it is necessary to specify it explicitly if you want to construct
    a fan without rays or cones::

        sage: Fan([], [])
        Traceback (most recent call last):
        ...
        ValueError: you must specify the lattice
        when you construct a fan without rays and cones!
        sage: F = Fan([], [], lattice=ToricLattice(2, "L"))
        sage: F
        Rational polyhedral fan in 2-d lattice L
        sage: F.lattice_dim()
        2
        sage: F.dim()
        0

    In the following examples, we test the ``allow_arrangement=True`` option.
    See :issue:`25122`.

    The intersection of the two cones is not a face of each. Therefore,
    they do not belong to the same rational polyhedral fan::

        sage: c1 = Cone([(-2,-1,1), (-2,1,1), (2,1,1), (2,-1,1)])
        sage: c2 = Cone([(-1,-2,1), (-1,2,1), (1,2,1), (1,-2,1)])
        sage: c1.intersection(c2).is_face_of(c1)
        False
        sage: c1.intersection(c2).is_face_of(c2)
        False
        sage: Fan([c1, c2])
        Traceback (most recent call last):
        ...
        ValueError: these cones cannot belong to the same fan!
        ...

    Let\'s construct the fan using ``allow_arrangement=True`` option::

        sage: fan = Fan([c1, c2], allow_arrangement=True)
        sage: fan.ngenerating_cones()
        5

    Another example where cone c2 is inside cone c1::

        sage: c1 = Cone([(4, 0, 0), (0, 4, 0), (0, 0, 4)])
        sage: c2 = Cone([(2, 1, 1), (1, 2, 1), (1, 1, 2)])
        sage: fan = Fan([c1, c2], allow_arrangement=True)
        sage: fan.ngenerating_cones()
        7
        sage: fan.plot()                                                                # needs sage.plot
        Graphics3d Object

    Cones of different dimension::

        sage: c1 = Cone([(1,0), (0,1)])
        sage: c2 = Cone([(2,1)])
        sage: c3 = Cone([(-1,-2)])
        sage: fan = Fan([c1, c2, c3], allow_arrangement=True)
        sage: for cone in sorted(fan.generating_cones()): print(sorted(cone.rays()))
        [N(-1, -2)]
        [N(0, 1), N(1, 2)]
        [N(1, 0), N(2, 1)]
        [N(1, 2), N(2, 1)]

    A 3-d cone and a 1-d cone::

        sage: c3 = Cone([[0, 1, 1], [1, 0, 1], [0, -1, 1], [-1, 0, 1]])
        sage: c1 = Cone([[0, 0, 1]])
        sage: fan1 = Fan([c1, c3], allow_arrangement=True)
        sage: fan1.plot()                                                               # needs sage.plot
        Graphics3d Object

    A 3-d cone and two 2-d cones::

        sage: c2v = Cone([[0, 1, 1], [0, -1, 1]])
        sage: c2h = Cone([[1, 0, 1], [-1, 0, 1]])
        sage: fan2 = Fan([c2v, c2h, c3], allow_arrangement=True)
        sage: fan2.is_simplicial()
        True
        sage: fan2.is_equivalent(fan1)
        True
    '''
def FaceFan(polytope, lattice=None):
    """
    Construct the face fan of the given rational ``polytope``.

    INPUT:

    - ``polytope`` -- a :func:`polytope
      <sage.geometry.polyhedron.constructor.Polyhedron>` over `\\QQ` or
      a :class:`lattice polytope
      <sage.geometry.lattice_polytope.LatticePolytopeClass>`. A (not
      necessarily full-dimensional) polytope containing the origin in
      its :meth:`relative interior
      <sage.geometry.polyhedron.base.Polyhedron_base.relative_interior_contains>`.

    - ``lattice`` -- :class:`ToricLattice
      <sage.geometry.toric_lattice.ToricLatticeFactory>`, `\\ZZ^n`, or any
      other object that behaves like these. If not specified, an attempt will
      be made to determine an appropriate toric lattice automatically.

    OUTPUT: :class:`rational polyhedral fan <RationalPolyhedralFan>`

    See also :func:`NormalFan`.

    EXAMPLES:

    Let's construct the fan corresponding to the product of two projective
    lines::

        sage: diamond = lattice_polytope.cross_polytope(2)
        sage: P1xP1 = FaceFan(diamond)
        sage: P1xP1.rays()
        M( 1,  0),
        M( 0,  1),
        M(-1,  0),
        M( 0, -1)
        in 2-d lattice M
        sage: for cone in P1xP1: print(cone.rays())
        M(-1,  0),
        M( 0, -1)
        in 2-d lattice M
        M( 0, 1),
        M(-1, 0)
        in 2-d lattice M
        M(1, 0),
        M(0, 1)
        in 2-d lattice M
        M(1,  0),
        M(0, -1)
        in 2-d lattice M

    TESTS::

        sage: cuboctahed = polytopes.cuboctahedron()
        sage: FaceFan(cuboctahed)
        Rational polyhedral fan in 3-d lattice M
        sage: cuboctahed.is_lattice_polytope(), cuboctahed.dilation(1/2).is_lattice_polytope()
        (True, False)
        sage: fan1 = FaceFan(cuboctahed)
        sage: fan2 = FaceFan(cuboctahed.dilation(2).lattice_polytope())
        sage: fan1.is_equivalent(fan2)
        True

        sage: ray = Polyhedron(vertices=[(-1,-1)], rays=[(1,1)])
        sage: FaceFan(ray)
        Traceback (most recent call last):
        ...
        ValueError: face fans are defined only for
        polytopes containing the origin as an interior point!

        sage: interval_in_QQ2 = Polyhedron([(0,-1), (0,+1)])
        sage: FaceFan(interval_in_QQ2).generating_cones()
        (1-d cone of Rational polyhedral fan in 2-d lattice M,
         1-d cone of Rational polyhedral fan in 2-d lattice M)

        sage: FaceFan(Polyhedron([(-1,0), (1,0), (0,1)])) # origin on facet
        Traceback (most recent call last):
        ...
        ValueError: face fans are defined only for
        polytopes containing the origin as an interior point!
    """
def NormalFan(polytope, lattice=None):
    """
    Construct the normal fan of the given rational ``polytope``.

    This returns the inner normal fan. For the outer normal fan, use
    ``NormalFan(-P)``.

    INPUT:

    - ``polytope`` -- a full-dimensional :func:`polytope
      <sage.geometry.polyhedron.constructor.Polyhedron>` over `\\QQ`
      or:class:`lattice polytope
      <sage.geometry.lattice_polytope.LatticePolytopeClass>`.

    - ``lattice`` -- :class:`ToricLattice
      <sage.geometry.toric_lattice.ToricLatticeFactory>`, `\\ZZ^n`, or any
      other object that behaves like these. If not specified, an attempt will
      be made to determine an appropriate toric lattice automatically.

    OUTPUT: :class:`rational polyhedral fan <RationalPolyhedralFan>`

    See also :func:`FaceFan`.

    EXAMPLES:

    Let's construct the fan corresponding to the product of two projective
    lines::

        sage: square = LatticePolytope([(1,1), (-1,1), (-1,-1), (1,-1)])
        sage: P1xP1 = NormalFan(square)
        sage: P1xP1.rays()
        N( 1,  0),
        N( 0,  1),
        N(-1,  0),
        N( 0, -1)
        in 2-d lattice N
        sage: for cone in P1xP1: print(cone.rays())
        N(-1,  0),
        N( 0, -1)
        in 2-d lattice N
        N(1,  0),
        N(0, -1)
        in 2-d lattice N
        N(1, 0),
        N(0, 1)
        in 2-d lattice N
        N( 0, 1),
        N(-1, 0)
        in 2-d lattice N

        sage: cuboctahed = polytopes.cuboctahedron()
        sage: NormalFan(cuboctahed)
        Rational polyhedral fan in 3-d lattice N

    TESTS::

        sage: cuboctahed.is_lattice_polytope(), cuboctahed.dilation(1/2).is_lattice_polytope()
        (True, False)
        sage: fan1 = NormalFan(cuboctahed)
        sage: fan2 = NormalFan(cuboctahed.dilation(2).lattice_polytope())
        sage: fan1.is_equivalent(fan2)
        True
    """
def Fan2d(rays, lattice=None):
    """
    Construct the maximal 2-d fan with given ``rays``.

    In two dimensions we can uniquely construct a fan from just rays,
    just by cyclically ordering the rays and constructing as many
    cones as possible. This is why we implement a special constructor
    for this case.

    INPUT:

    - ``rays`` -- list of rays given as list or vectors convertible to
      the rational extension of ``lattice``. Duplicate rays are
      removed without changing the ordering of the remaining rays.

    - ``lattice`` -- :class:`ToricLattice
      <sage.geometry.toric_lattice.ToricLatticeFactory>`, `\\ZZ^n`, or any
      other object that behaves like these. If not specified, an attempt will
      be made to determine an appropriate toric lattice automatically.

    EXAMPLES::

        sage: Fan2d([(0,1), (1,0)])
        Rational polyhedral fan in 2-d lattice N
        sage: Fan2d([], lattice=ToricLattice(2, 'myN'))
        Rational polyhedral fan in 2-d lattice myN

    The ray order is as specified, even if it is not the cyclic order::

        sage: fan1 = Fan2d([(0,1), (1,0)])
        sage: fan1.rays()
        N(0, 1),
        N(1, 0)
        in 2-d lattice N

        sage: fan2 = Fan2d([(1,0), (0,1)])
        sage: fan2.rays()
        N(1, 0),
        N(0, 1)
        in 2-d lattice N

        sage: fan1 == fan2, fan1.is_equivalent(fan2)
        (False, True)

        sage: fan = Fan2d([(1,1), (-1,-1), (1,-1), (-1,1)])
        sage: [cone.ambient_ray_indices() for cone in fan]
        [(2, 1), (1, 3), (3, 0), (0, 2)]
        sage: fan.is_complete()
        True

    TESTS::

        sage: Fan2d([(0,1), (0,1)]).generating_cones()
        (1-d cone of Rational polyhedral fan in 2-d lattice N,)

        sage: Fan2d([(1,1), (-1,-1)]).generating_cones()
        (1-d cone of Rational polyhedral fan in 2-d lattice N,
         1-d cone of Rational polyhedral fan in 2-d lattice N)

        sage: Fan2d([])
        Traceback (most recent call last):
        ...
        ValueError: you must specify a 2-dimensional lattice
        when you construct a fan without rays.

        sage: Fan2d([(3,4)]).rays()
        N(3, 4)
        in 2-d lattice N

        sage: Fan2d([(0,1,0)])
        Traceback (most recent call last):
        ...
        ValueError: the lattice must be 2-dimensional.

        sage: Fan2d([(0,1), (1,0), (0,0)])
        Traceback (most recent call last):
        ...
        ValueError: only nonzero vectors define rays

        sage: Fan2d([(0, -2), (2, -10), (1, -3), (2, -9), (2, -12), (1, 1),
        ....:        (2, 1), (1, -5), (0, -6), (1, -7), (0, 1), (2, -4),
        ....:        (2, -2), (1, -9), (1, -8), (2, -6), (0, -1), (0, -3),
        ....:        (2, -11), (2, -8), (1, 0), (0, -5), (1, -4), (2, 0),
        ....:        (1, -6), (2, -7), (2, -5), (-1, -3), (1, -1), (1, -2),
        ....:        (0, -4), (2, -3), (2, -1)]).cone_lattice()
        Finite lattice containing 44 elements with distinguished linear extension

        sage: Fan2d([(1,1)]).is_complete()
        False
        sage: Fan2d([(1,1), (-1,-1)]).is_complete()
        False
        sage: Fan2d([(1,0), (0,1)]).is_complete()
        False
    """

class Cone_of_fan(ConvexRationalPolyhedralCone):
    '''
    Construct a cone belonging to a fan.

    .. WARNING::

        This class does not check that the input defines a valid cone of a
        fan. You must not construct objects of this class directly.

    In addition to all of the properties of "regular" :class:`cones
    <sage.geometry.cone.ConvexRationalPolyhedralCone>`, such cones know their
    relation to the fan.

    INPUT:

    - ``ambient`` -- fan whose cone is constructed

    - ``ambient_ray_indices`` -- increasing list or tuple of integers, indices
      of rays of ``ambient`` generating this cone

    OUTPUT: cone of ``ambient``

    EXAMPLES:

    The intended way to get objects of this class is the following::

        sage: # needs palp
        sage: fan = toric_varieties.P1xP1().fan()
        sage: cone = fan.generating_cone(0); cone
        2-d cone of Rational polyhedral fan in 2-d lattice N
        sage: cone.ambient_ray_indices()
        (0, 2)
        sage: cone.star_generator_indices()
        (0,)
    '''
    def __init__(self, ambient, ambient_ray_indices) -> None:
        """
        See :class:`Cone_of_Fan` for documentation.

        TESTS:

        The following code is likely to construct an invalid object, we just
        test that creation of cones of fans is working::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: cone = sage.geometry.fan.Cone_of_fan(fan, (0,)); cone                 # needs palp
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: TestSuite(cone).run()                                                 # needs palp
        """
    def star_generator_indices(self):
        '''
        Return indices of generating cones of the "ambient fan" containing
        ``self``.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()                                       # needs palp
            sage: cone = P1xP1.fan().generating_cone(0)                                 # needs palp
            sage: cone.star_generator_indices()                                         # needs palp
            (0,)

        TESTS:

        A mistake in this function used to cause the problem reported in
        :issue:`9782`. We check that now everything is working smoothly::

            sage: f = Fan([(0, 2, 4),
            ....:          (0, 4, 5),
            ....:          (0, 3, 5),
            ....:          (0, 1, 3),
            ....:          (0, 1, 2),
            ....:          (2, 4, 6),
            ....:          (4, 5, 6),
            ....:          (3, 5, 6),
            ....:          (1, 3, 6),
            ....:          (1, 2, 6)],
            ....:         [(-1, 0, 0),
            ....:          (0, -1, 0),
            ....:          (0, 0, -1),
            ....:          (0, 0, 1),
            ....:          (0, 1, 2),
            ....:          (0, 1, 3),
            ....:          (1, 0, 4)])
            sage: f.is_complete()
            True
            sage: X = ToricVariety(f)
            sage: X.fan().is_complete()
            True
        '''
    def star_generators(self):
        '''
        Return indices of generating cones of the "ambient fan" containing
        ``self``.

        OUTPUT: increasing :class:`tuple` of integers

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()                                       # needs palp
            sage: cone = P1xP1.fan().generating_cone(0)                                 # needs palp
            sage: cone.star_generators()                                                # needs palp
            (2-d cone of Rational polyhedral fan in 2-d lattice N,)
        '''

class RationalPolyhedralFan(IntegralRayCollection, Callable, Container):
    '''
    Create a rational polyhedral fan.

    .. WARNING::

        This class does not perform any checks of correctness of input nor
        does it convert input into the standard representation. Use
        :func:`Fan` to construct fans from "raw data" or :func:`FaceFan` and
        :func:`NormalFan` to get fans associated to polytopes.

    Fans are immutable, but they cache most of the returned values.

    INPUT:

    - ``cones`` -- list of generating cones of the fan, each cone given as a
      list of indices of its generating rays in ``rays``;

    - ``rays`` -- list of immutable primitive vectors in ``lattice``
      consisting of exactly the rays of the fan (i.e. no "extra" ones);

    - ``lattice`` -- :class:`ToricLattice
      <sage.geometry.toric_lattice.ToricLatticeFactory>`, `\\ZZ^n`, or any
      other object that behaves like these. If ``None``, it will be determined
      as :func:`parent` of the first ray. Of course, this cannot be done if
      there are no rays, so in this case you must give an appropriate
      ``lattice`` directly;

    - ``is_complete`` -- if given, must be ``True`` or ``False`` depending on
      whether this fan is complete or not. By default, it will be determined
      automatically if necessary;

    - ``virtual_rays`` -- if given, must be a list of immutable primitive
      vectors in ``lattice``, see :meth:`virtual_rays` for details. By default,
      it will be determined automatically if necessary.

    OUTPUT:

    rational polyhedral fan
    '''
    def __init__(self, cones, rays, lattice, is_complete=None, virtual_rays=None) -> None:
        """
        See :class:`RationalPolyhedralFan` for documentation.

        TESTS::

            sage: v = vector([0,1])
            sage: v.set_immutable()
            sage: f = sage.geometry.fan.RationalPolyhedralFan(
            ....:                       [(0,)], [v], None)
            sage: f.rays()
            (0, 1)
            in Ambient free module of rank 2
            over the principal ideal domain Integer Ring
            sage: TestSuite(f).run()
            sage: f = Fan([(0,)], [(0,1)])
            sage: TestSuite(f).run()
        """
    def __call__(self, dim=None, codim=None):
        '''
        Return the specified cones of ``self``.

        .. NOTE::

            "Direct call" syntax is a synonym for :meth:`cones` method except
            that in the case of no input parameters this function returns
            just ``self``.

        INPUT:

        - ``dim`` -- dimension of the requested cones

        - ``codim`` -- codimension of the requested cones

        OUTPUT:

        cones of ``self`` of the specified (co)dimension if it was given,
        otherwise ``self``

        TESTS::

            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan(1)
            (1-d cone of Rational polyhedral fan in 2-d lattice N,
             1-d cone of Rational polyhedral fan in 2-d lattice N,
             1-d cone of Rational polyhedral fan in 2-d lattice N)
            sage: fan(2)
            (2-d cone of Rational polyhedral fan in 2-d lattice N,)
            sage: fan(dim=2)
            (2-d cone of Rational polyhedral fan in 2-d lattice N,)
            sage: fan(codim=2)
            (0-d cone of Rational polyhedral fan in 2-d lattice N,)
            sage: fan(dim=1, codim=1)
            Traceback (most recent call last):
            ...
            ValueError: dimension and codimension
            cannot be specified together!
            sage: fan() is fan
            True
        '''
    def __richcmp__(self, right, op):
        """
        Compare ``self`` and ``right``.

        INPUT:

        - ``right`` -- anything

        OUTPUT: boolean

        There is equality if ``right`` is also a fan, their rays are
        the same and stored in the same order, and their generating
        cones are the same and stored in the same order.

        TESTS::

            sage: f1 = Fan(cones=[(0,1), (1,2)],
            ....:          rays=[(1,0), (0,1), (-1, 0)],
            ....:          check=False)
            sage: f2 = Fan(cones=[(1,2), (0,1)],
            ....:          rays=[(1,0), (0,1), (-1, 0)],
            ....:          check=False)
            sage: f3 = Fan(cones=[(1,2), (0,1)],
            ....:          rays=[(1,0), (0,1), (-1, 0)],
            ....:          check=False)
            sage: f1 > f2
            True
            sage: f2 < f1
            True
            sage: f2 == f3
            True
            sage: f2 is f3
            False
        """
    def __contains__(self, cone) -> bool:
        '''
        Check if ``cone`` is equivalent to a cone of the fan.

        See :meth:`_contains` (which is called by this function) for
        documentation.

        TESTS::

            sage: cone1 = Cone([(0,-1), (1,0)])
            sage: cone2 = Cone([(1,0), (0,1)])
            sage: f = Fan([cone1, cone2])
            sage: f.generating_cone(0) in f
            True
            sage: cone1 in f
            True
            sage: (1,1) in f    # not a cone
            False
            sage: "Ceci n\'est pas un cone" in f
            False
        '''
    def __iter__(self):
        """
        Return an iterator over generating cones of ``self``.

        OUTPUT: iterator

        TESTS::

            sage: f = Fan(cones=[(0,1), (1,2)],
            ....:         rays=[(1,0), (0,1), (-1, 0)],
            ....:         check=False)
            sage: for cone in f: print(cone.rays())
            N(1, 0),
            N(0, 1)
            in 2-d lattice N
            N( 0, 1),
            N(-1, 0)
            in 2-d lattice N
        """
    def support_contains(self, *args):
        """
        Check if a point is contained in the support of the fan.

        The support of a fan is the union of all cones of the fan. If
        you want to know whether the fan contains a given cone, you
        should use :meth:`contains` instead.

        INPUT:

        - ``*args`` -- an element of ``self.lattice()`` or something
          that can be converted to it (for example, a list of
          coordinates).

        OUTPUT:

        ``True`` if ``point`` is contained in the support of the
        fan, ``False`` otherwise

        TESTS::

            sage: cone1 = Cone([(0,-1), (1,0)])
            sage: cone2 = Cone([(1,0), (0,1)])
            sage: f = Fan([cone1, cone2])

        We check if some points are in this fan::

            sage: f.support_contains(f.lattice()(1,0))
            True
            sage: f.support_contains(cone1)    # a cone is not a point of the lattice
            False
            sage: f.support_contains((1,0))
            True
            sage: f.support_contains(1,1)
            True
            sage: f.support_contains((-1,0))
            False
            sage: f.support_contains(f.lattice().dual()(1,0))  # random output (warning)
            False
            sage: f.support_contains(f.lattice().dual()(1,0))
            False
            sage: f.support_contains(1)
            False
            sage: f.support_contains(0)   # 0 converts to the origin in the lattice
            True
            sage: f.support_contains(1/2, sqrt(3))                                      # needs sage.symbolic
            True
            sage: f.support_contains(-1/2, sqrt(3))                                     # needs sage.symbolic
            False
        """
    def cartesian_product(self, other, lattice=None):
        """
        Return the Cartesian product of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a :class:`rational polyhedral fan
          <sage.geometry.fan.RationalPolyhedralFan>`;

        - ``lattice`` -- (optional) the ambient lattice for the
          Cartesian product fan. By default, the direct sum of the
          ambient lattices of ``self`` and ``other`` is constructed.

        OUTPUT:

        a :class:`fan <RationalPolyhedralFan>` whose cones are all pairwise
        Cartesian products of the cones of ``self`` and ``other``

        EXAMPLES::

            sage: K = ToricLattice(1, 'K')
            sage: fan1 = Fan([[0],[1]], [(1,),(-1,)], lattice=K)
            sage: L = ToricLattice(2, 'L')
            sage: fan2 = Fan(rays=[(1,0), (0,1), (-1,-1)],
            ....:            cones=[[0,1], [1,2], [2,0]], lattice=L)
            sage: fan1.cartesian_product(fan2)
            Rational polyhedral fan in 3-d lattice K+L
            sage: _.ngenerating_cones()
            6
        """
    def __neg__(self):
        """
        Return the fan where each cone is replaced by the opposite cone.

        EXAMPLES::

            sage: c0 = Cone([(1,1),(0,1)])
            sage: c1 = Cone([(1,1),(1,0)])
            sage: F = Fan([c0, c1]); F
            Rational polyhedral fan in 2-d lattice N
            sage: G = -F; G  # indirect doctest
            Rational polyhedral fan in 2-d lattice N
            sage: -G==F
            True
            sage: G.rays()
            N( 0, -1),
            N(-1,  0),
            N(-1, -1)
            in 2-d lattice N
        """
    def common_refinement(self, other):
        """
        Return the common refinement of this fan and ``other``.

        INPUT:

        - ``other`` -- a :class:`fan <RationalPolyhedralFan>` in the same
          :meth:`lattice` and with the same support as this fan

        OUTPUT: a :class:`fan <RationalPolyhedralFan>`

        EXAMPLES:

        Refining a fan with itself gives itself::

            sage: F0 = Fan2d([(1,0), (0,1), (-1,0), (0,-1)])
            sage: F0.common_refinement(F0) == F0
            True

        A more complex example with complete fans::

            sage: F1 = Fan([[0],[1]], [(1,),(-1,)])
            sage: F2 = Fan2d([(1,0), (1,1), (0,1), (-1,0), (0,-1)])
            sage: F3 = F2.cartesian_product(F1)
            sage: F4 = F1.cartesian_product(F2)
            sage: FF = F3.common_refinement(F4)
            sage: F3.ngenerating_cones()
            10
            sage: F4.ngenerating_cones()
            10
            sage: FF.ngenerating_cones()
            13

        An example with two non-complete fans with the same support::

            sage: F5 = Fan2d([(1,0), (1,2), (0,1)])
            sage: F6 = Fan2d([(1,0), (2,1), (0,1)])
            sage: F5.common_refinement(F6).ngenerating_cones()
            3

        Both fans must live in the same lattice::

            sage: F0.common_refinement(F1)
            Traceback (most recent call last):
            ...
            ValueError: the fans are not in the same lattice
        """
    def cone_containing(self, *points):
        """
        Return the smallest cone of ``self`` containing all given points.

        INPUT:

        - either one or more indices of rays of ``self``, or one or more
          objects representing points of the ambient space of ``self``, or a
          list of such objects (you CANNOT give a list of indices).

        OUTPUT:

        A :class:`cone of fan <Cone_of_fan>` whose ambient fan is
        ``self``

        .. NOTE::

            We think of the origin as of the smallest cone containing no rays
            at all. If there is no ray in ``self`` that contains all ``rays``,
            a :exc:`ValueError` exception will be raised.

        EXAMPLES::

            sage: cone1 = Cone([(0,-1), (1,0)])
            sage: cone2 = Cone([(1,0), (0,1)])
            sage: f = Fan([cone1, cone2])
            sage: f.rays()
            N(0, -1),
            N(0,  1),
            N(1,  0)
            in 2-d lattice N
            sage: f.cone_containing(0)  # ray index
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing(0, 1) # ray indices
            Traceback (most recent call last):
            ...
            ValueError: there is no cone in
            Rational polyhedral fan in 2-d lattice N
            containing all of the given rays! Ray indices: [0, 1]
            sage: f.cone_containing(0, 2) # ray indices
            2-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing((0,1))  # point
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing([(0,1)]) # point
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing((1,1))
            2-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing((1,1), (1,0))
            2-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing()
            0-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing((0,0))
            0-d cone of Rational polyhedral fan in 2-d lattice N
            sage: f.cone_containing((-1,1))
            Traceback (most recent call last):
            ...
            ValueError: there is no cone in
            Rational polyhedral fan in 2-d lattice N
            containing all of the given points! Points: [N(-1, 1)]

        TESTS::

            sage: fan = Fan(cones=[(0,1,2,3), (0,1,4)],
            ....:           rays=[(1,1,1), (1,-1,1), (1,-1,-1), (1,1,-1), (0,0,1)])
            sage: fan.cone_containing(0).rays()
            N(1, 1, 1)
            in 3-d lattice N
        """
    def cone_lattice(self):
        '''
        Return the cone lattice of ``self``.

        This lattice will have the origin as the bottom (we do not include the
        empty set as a cone) and the fan itself as the top.

        OUTPUT:

        :class:`finite poset <sage.combinat.posets.posets.FinitePoset` of
        :class:`cones of fan<Cone_of_fan>`, behaving like "regular" cones,
        but also containing the information about their relation to this
        fan, namely, the contained rays and containing generating cones. The
        top of the lattice will be this fan itself (*which is not a*
        :class:`cone of fan<Cone_of_fan>`).

        See also :meth:`cones`.

        EXAMPLES:

        Cone lattices can be computed for arbitrary fans::

            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.rays()
            N(-1, 0),
            N( 0, 1),
            N( 1, 0)
            in 2-d lattice N
            sage: for cone in fan: print(cone.ambient_ray_indices())
            (1, 2)
            (0,)
            sage: L = fan.cone_lattice()
            sage: L
            Finite poset containing 6 elements with distinguished linear extension

        These 6 elements are the origin, three rays, one two-dimensional
        cone, and the fan itself\\ . Since we do add the fan itself as the
        largest face, you should be a little bit careful with this last
        element::

            sage: for face in L: print(face.ambient_ray_indices())
            Traceback (most recent call last):
            ...
            AttributeError: \'RationalPolyhedralFan\'
            object has no attribute \'ambient_ray_indices\'
            sage: L.top()
            Rational polyhedral fan in 2-d lattice N

        For example, you can do ::

            sage: for l in L.level_sets()[:-1]:
            ....:     print([f.ambient_ray_indices() for f in l])
            [()]
            [(0,), (1,), (2,)]
            [(1, 2)]

        If the fan is complete, its cone lattice is atomic and coatomic and
        can (and will!) be computed in a much more efficient way, but the
        interface is exactly the same::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: L = fan.cone_lattice()                                                # needs palp
            sage: for l in L.level_sets()[:-1]:                                         # needs palp
            ....:     print([f.ambient_ray_indices() for f in l])
            [()]
            [(0,), (1,), (2,), (3,)]
            [(0, 2), (1, 2), (1, 3), (0, 3)]

        Let\'s also consider the cone lattice of a fan generated by a single
        cone::

            sage: fan = Fan([cone1])
            sage: L = fan.cone_lattice()
            sage: L
            Finite poset containing 5 elements with distinguished linear extension

        Here these 5 elements correspond to the origin, two rays, one
        generating cone of dimension two, and the whole fan. While this single
        cone "is" the whole fan, it is consistent and convenient to
        distinguish them in the cone lattice.
        '''
    def f_vector(self) -> tuple:
        """
        Return the f-vector of the fan.

        This is the tuple `(f_0, f_1, \\ldots, f_d)`
        where `f_i` is the number of cones of dimension `i`.

        EXAMPLES::

            sage: F = ClusterAlgebra(['A',2]).cluster_fan()
            sage: F.f_vector()
            (1, 5, 5)
        """
    def cones(self, dim=None, codim=None):
        '''
        Return the specified cones of ``self``.

        INPUT:

        - ``dim`` -- dimension of the requested cones

        - ``codim`` -- codimension of the requested cones

        .. NOTE::

            You can specify at most one input parameter.

        OUTPUT:

        :class:`tuple` of cones of ``self`` of the specified (co)dimension,
        if either ``dim`` or ``codim`` is given. Otherwise :class:`tuple` of
        such tuples for all existing dimensions.

        EXAMPLES::

            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan(dim=0)
            (0-d cone of Rational polyhedral fan in 2-d lattice N,)
            sage: fan(codim=2)
            (0-d cone of Rational polyhedral fan in 2-d lattice N,)
            sage: for cone in fan.cones(1): cone.ray(0)
            N(-1, 0)
            N(0, 1)
            N(1, 0)
            sage: fan.cones(2)
            (2-d cone of Rational polyhedral fan in 2-d lattice N,)

        You cannot specify both dimension and codimension, even if they
        "agree"::

            sage: fan(dim=1, codim=1)
            Traceback (most recent call last):
            ...
            ValueError: dimension and codimension
            cannot be specified together!

        But it is OK to ask for cones of too high or low (co)dimension::

            sage: fan(-1)
            ()
            sage: fan(3)
            ()
            sage: fan(codim=4)
            ()
        '''
    def contains(self, cone) -> bool:
        """
        Check if a given ``cone`` is equivalent to a cone of the fan.

        INPUT:

        - ``cone`` -- anything

        OUTPUT:

        ``False`` if ``cone`` is not a cone or if ``cone`` is not
        equivalent to a cone of the fan, ``True`` otherwise

        .. NOTE::

            Recall that a fan is a (finite) collection of cones. A
            cone is contained in a fan if it is equivalent to one of
            the cones of the fan. In particular, it is possible that
            all rays of the cone are in the fan, but the cone itself
            is not.

            If you want to know whether a point is in the support of
            the fan, you should use :meth:`support_contains`.

        EXAMPLES:

        We first construct a simple fan::

            sage: cone1 = Cone([(0,-1), (1,0)])
            sage: cone2 = Cone([(1,0), (0,1)])
            sage: f = Fan([cone1, cone2])

        Now we check if some cones are in this fan. First, we make sure that
        the order of rays of the input cone does not matter (``check=False``
        option ensures that rays of these cones will be listed exactly as they
        are given)::

            sage: f.contains(Cone([(1,0), (0,1)], check=False))
            True
            sage: f.contains(Cone([(0,1), (1,0)], check=False))
            True

        Now we check that a non-generating cone is in our fan::

            sage: f.contains(Cone([(1,0)]))
            True
            sage: Cone([(1,0)]) in f   # equivalent to the previous command
            True

        Finally, we test some cones which are not in this fan::

            sage: f.contains(Cone([(1,1)]))
            False
            sage: f.contains(Cone([(1,0), (-0,1)]))
            True

        A point is not a cone::

            sage: n = f.lattice()(1,1); n
            N(1, 1)
            sage: f.contains(n)
            False
        """
    def embed(self, cone):
        '''
        Return the cone equivalent to the given one, but sitting in ``self``.

        You may need to use this method before calling methods of ``cone`` that
        depend on the ambient structure, such as
        :meth:`~sage.geometry.cone.ConvexRationalPolyhedralCone.ambient_ray_indices`
        or
        :meth:`~sage.geometry.cone.ConvexRationalPolyhedralCone.facet_of`. The
        cone returned by this method will have ``self`` as ambient. If ``cone``
        does not represent a valid cone of ``self``, :exc:`ValueError`
        exception is raised.

        .. NOTE::

            This method is very quick if ``self`` is already the ambient
            structure of ``cone``, so you can use without extra checks and
            performance hit even if ``cone`` is likely to sit in ``self`` but
            in principle may not.

        INPUT:

        - ``cone`` -- a :class:`cone
          <sage.geometry.cone.ConvexRationalPolyhedralCone>`

        OUTPUT:

        a :class:`cone of fan <Cone_of_fan>`, equivalent to ``cone`` but
        sitting inside ``self``

        EXAMPLES:

        Let\'s take a 3-d fan generated by a cone on 4 rays::

            sage: f = Fan([Cone([(1,0,1), (0,1,1), (-1,0,1), (0,-1,1)])])

        Then any ray generates a 1-d cone of this fan, but if you construct
        such a cone directly, it will not "sit" inside the fan::

            sage: ray = Cone([(0,-1,1)])
            sage: ray
            1-d cone in 3-d lattice N
            sage: ray.ambient_ray_indices()
            (0,)
            sage: ray.adjacent()
            ()
            sage: ray.ambient()
            1-d cone in 3-d lattice N

        If we want to operate with this ray as a part of the fan, we need to
        embed it first::

            sage: e_ray = f.embed(ray)
            sage: e_ray
            1-d cone of Rational polyhedral fan in 3-d lattice N
            sage: e_ray.rays()
            N(0, -1, 1)
            in 3-d lattice N
            sage: e_ray is ray
            False
            sage: e_ray.is_equivalent(ray)
            True
            sage: e_ray.ambient_ray_indices()
            (3,)
            sage: e_ray.adjacent()
            (1-d cone of Rational polyhedral fan in 3-d lattice N,
             1-d cone of Rational polyhedral fan in 3-d lattice N)
            sage: e_ray.ambient()
            Rational polyhedral fan in 3-d lattice N

        Not every cone can be embedded into a fixed fan::

            sage: f.embed(Cone([(0,0,1)]))
            Traceback (most recent call last):
            ...
            ValueError: 1-d cone in 3-d lattice N does not belong
            to Rational polyhedral fan in 3-d lattice N!
            sage: f.embed(Cone([(1,0,1), (-1,0,1)]))
            Traceback (most recent call last):
            ...
            ValueError: 2-d cone in 3-d lattice N does not belong
            to Rational polyhedral fan in 3-d lattice N!
        '''
    @cached_method
    def Gale_transform(self):
        """
        Return the Gale transform of ``self``.

        OUTPUT: a matrix over `ZZ`

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.Gale_transform()                                                  # needs palp
            [ 1  1  0  0 -2]
            [ 0  0  1  1 -2]
            sage: _.base_ring()                                                         # needs palp
            Integer Ring
        """
    def is_polytopal(self) -> bool:
        """
        Check if ``self`` is the normal fan of a polytope.

        A rational polyhedral fan is *polytopal* if it is the normal fan of a
        polytope. This is also called *regular*, or provides a *coherent*
        subdivision or leads to a *projective* toric variety.

        OUTPUT: ``True`` if ``self`` is polytopal and ``False`` otherwise

        EXAMPLES:

        This is the mother of all examples (see Section 7.1.1 in
        [DLRS2010]_)::

            sage: def mother(epsilon=0):
            ....:     rays = [(4-epsilon,epsilon,0),(0,4-epsilon,epsilon),(epsilon,0,4-epsilon),(2,1,1),(1,2,1),(1,1,2),(-1,-1,-1)]
            ....:     L = [(0,1,4),(0,3,4),(1,2,5),(1,4,5),(0,2,3),(2,3,5),(3,4,5),(6,0,1),(6,1,2),(6,2,0)]
            ....:     S1 = [Cone([rays[i] for i in indices]) for indices in L]
            ....:     return Fan(S1)

        When epsilon=0, it is not polytopal::

            sage: epsilon = 0
            sage: mother(epsilon).is_polytopal()
            False

        Doing a slight perturbation makes the same subdivision polytopal::

            sage: epsilon = 1/2
            sage: mother(epsilon).is_polytopal()
            True

        TESTS::

            sage: cone = Cone([(1,1), (2,1)])
            sage: F = Fan([cone])
            sage: F.is_polytopal()
            Traceback (most recent call last):
            ...
            ValueError: to be polytopal, the fan should be complete

        .. SEEALSO::

            :meth:`is_projective`.
        """
    def generating_cone(self, n):
        """
        Return the ``n``-th generating cone of ``self``.

        INPUT:

        - ``n`` -- integer; the index of a generating cone

        OUTPUT: :class:`cone of fan<Cone_of_fan>`

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.generating_cone(0)                                                # needs palp
            2-d cone of Rational polyhedral fan in 2-d lattice N
        """
    def generating_cones(self):
        """
        Return generating cones of ``self``.

        OUTPUT: :class:`tuple` of :class:`cones of fan<Cone_of_fan>`

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.generating_cones()                                                # needs palp
            (2-d cone of Rational polyhedral fan in 2-d lattice N,
             2-d cone of Rational polyhedral fan in 2-d lattice N,
             2-d cone of Rational polyhedral fan in 2-d lattice N,
             2-d cone of Rational polyhedral fan in 2-d lattice N)
            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.generating_cones()
            (2-d cone of Rational polyhedral fan in 2-d lattice N,
             1-d cone of Rational polyhedral fan in 2-d lattice N)
        """
    @cached_method
    def vertex_graph(self):
        """
        Return the graph of 1- and 2-cones.

        OUTPUT:

        An edge-colored graph. The vertices correspond to the 1-cones
        (i.e. rays) of
        the fan. Two vertices are joined by an edge iff the rays span
        a 2-cone of the fan. The edges are colored by pairs of
        integers that classify the 2-cones up to `GL(2,\\ZZ)`
        transformation, see
        :func:`~sage.geometry.cone.classify_cone_2d`.

        EXAMPLES::

            sage: # needs palp
            sage: dP8 = toric_varieties.dP8()
            sage: g = dP8.fan().vertex_graph(); g
            Graph on 4 vertices
            sage: set(dP8.fan(1)) == set(g.vertices(sort=False))
            True
            sage: g.edge_labels()  # all edge labels the same since every cone is smooth
            [(1, 0), (1, 0), (1, 0), (1, 0)]

            sage: g = toric_varieties.Cube_deformation(10).fan().vertex_graph()
            sage: g.automorphism_group().order()                                        # needs sage.groups
            48
            sage: g.automorphism_group(edge_labels=True).order()                        # needs sage.groups
            4
        """
    def is_complete(self) -> bool:
        """
        Check if ``self`` is complete.

        A rational polyhedral fan is *complete* if its cones fill the whole
        space.

        OUTPUT: ``True`` if ``self`` is complete and ``False`` otherwise

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.is_complete()                                                     # needs palp
            True
            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.is_complete()
            False
        """
    def is_equivalent(self, other) -> bool:
        '''
        Check if ``self`` is "mathematically" the same as ``other``.

        INPUT:

        - ``other`` -- fan

        OUTPUT:

        ``True`` if ``self`` and ``other`` define the same fans as
        collections of equivalent cones in the same lattice, ``False``
        otherwise.

        There are three different equivalences between fans `F_1` and `F_2`
        in the same lattice:

        #. They have the same rays in the same order and the same generating
           cones in the same order.
           This is tested by ``F1 == F2``.
        #. They have the same rays and the same generating cones without
           taking into account any order.
           This is tested by ``F1.is_equivalent(F2)``.
        #. They are in the same orbit of `GL(n,\\ZZ)` (and, therefore,
           correspond to isomorphic toric varieties).
           This is tested by ``F1.is_isomorphic(F2)``.

        Note that :meth:`virtual_rays` are included into consideration for all
        of the above equivalences.

        EXAMPLES::

            sage: fan1 = Fan(cones=[(0,1), (1,2)],
            ....:            rays=[(1,0), (0,1), (-1,-1)],
            ....:            check=False)
            sage: fan2 = Fan(cones=[(2,1), (0,2)],
            ....:            rays=[(1,0), (-1,-1), (0,1)],
            ....:            check=False)
            sage: fan3 = Fan(cones=[(0,1), (1,2)],
            ....:            rays=[(1,0), (0,1), (-1,1)],
            ....:            check=False)
            sage: fan1 == fan2
            False
            sage: fan1.is_equivalent(fan2)
            True
            sage: fan1 == fan3
            False
            sage: fan1.is_equivalent(fan3)
            False
        '''
    def is_isomorphic(self, other) -> bool:
        '''
        Check if ``self`` is in the same `GL(n, \\ZZ)`-orbit as ``other``.

        There are three different equivalences between fans `F_1` and `F_2`
        in the same lattice:

        #. They have the same rays in the same order and the same generating
           cones in the same order.
           This is tested by ``F1 == F2``.
        #. They have the same rays and the same generating cones without
           taking into account any order.
           This is tested by ``F1.is_equivalent(F2)``.
        #. They are in the same orbit of `GL(n,\\ZZ)` (and, therefore,
           correspond to isomorphic toric varieties).
           This is tested by ``F1.is_isomorphic(F2)``.

        Note that :meth:`virtual_rays` are included into consideration for all
        of the above equivalences.

        INPUT:

        - ``other`` -- a :class:`fan <RationalPolyhedralFan>`

        OUTPUT:

        ``True`` if ``self`` and ``other`` are in the same
        `GL(n, \\ZZ)`-orbit, ``False`` otherwise

        .. SEEALSO::

            If you want to obtain the actual fan isomorphism, use
            :meth:`isomorphism`.

        EXAMPLES:

        Here we pick an `SL(2,\\ZZ)` matrix ``m`` and then verify that
        the image fan is isomorphic::

            sage: rays = ((1, 1), (0, 1), (-1, -1), (1, 0))
            sage: cones = [(0,1), (1,2), (2,3), (3,0)]
            sage: fan1 = Fan(cones, rays)
            sage: m = matrix([[-2,3], [1,-1]])
            sage: fan2 = Fan(cones, [vector(r)*m for r in rays])
            sage: fan1.is_isomorphic(fan2)
            True
            sage: fan1.is_equivalent(fan2)
            False
            sage: fan1 == fan2
            False

        These fans are "mirrors" of each other::

            sage: fan1 = Fan(cones=[(0,1), (1,2)],
            ....:            rays=[(1,0), (0,1), (-1,-1)],
            ....:            check=False)
            sage: fan2 = Fan(cones=[(0,1), (1,2)],
            ....:            rays=[(1,0), (0,-1), (-1,1)],
            ....:            check=False)
            sage: fan1 == fan2
            False
            sage: fan1.is_equivalent(fan2)
            False
            sage: fan1.is_isomorphic(fan2)
            True
            sage: fan1.is_isomorphic(fan1)
            True
        '''
    def isomorphism(self, other):
        """
        Return a fan isomorphism from ``self`` to ``other``.

        INPUT:

        - ``other`` -- fan

        OUTPUT:

        A fan isomorphism. If no such isomorphism exists, a
        :class:`~sage.geometry.fan_isomorphism.FanNotIsomorphicError`
        is raised.

        EXAMPLES::

            sage: rays = ((1, 1), (0, 1), (-1, -1), (3, 1))
            sage: cones = [(0,1), (1,2), (2,3), (3,0)]
            sage: fan1 = Fan(cones, rays)
            sage: m = matrix([[-2,3], [1,-1]])
            sage: fan2 = Fan(cones, [vector(r)*m for r in rays])

            sage: fan1.isomorphism(fan2)
            Fan morphism defined by the matrix
            [-2  3]
            [ 1 -1]
            Domain fan: Rational polyhedral fan in 2-d lattice N
            Codomain fan: Rational polyhedral fan in 2-d lattice N

            sage: fan2.isomorphism(fan1)
            Fan morphism defined by the matrix
            [1 3]
            [1 2]
            Domain fan: Rational polyhedral fan in 2-d lattice N
            Codomain fan: Rational polyhedral fan in 2-d lattice N

            sage: fan1.isomorphism(toric_varieties.P2().fan())                          # needs palp
            Traceback (most recent call last):
            ...
            FanNotIsomorphicError
        """
    def is_simplicial(self) -> bool:
        """
        Check if ``self`` is simplicial.

        A rational polyhedral fan is **simplicial** if all of its cones are,
        i.e. primitive vectors along generating rays of every cone form a part
        of a *rational* basis of the ambient space.

        OUTPUT: ``True`` if ``self`` is simplicial and ``False`` otherwise

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.is_simplicial()                                                   # needs palp
            True
            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.is_simplicial()
            True

        In fact, any fan in a two-dimensional ambient space is simplicial.
        This is no longer the case in dimension three::

            sage: fan = NormalFan(lattice_polytope.cross_polytope(3))
            sage: fan.is_simplicial()
            False
            sage: fan.generating_cone(0).nrays()
            4
        """
    @cached_method
    def is_smooth(self, codim=None) -> bool:
        """
        Check if ``self`` is smooth.

        A rational polyhedral fan is **smooth** if all of its cones
        are, i.e. primitive vectors along generating rays of every
        cone form a part of an *integral* basis of the ambient
        space. In this case the corresponding toric variety is smooth.

        A fan in an `n`-dimensional lattice is smooth up to codimension `c`
        if all cones of codimension greater than or equal to `c` are smooth,
        i.e. if all cones of dimension less than or equal to `n-c` are smooth.
        In this case the singular set of the corresponding toric variety is of
        dimension less than `c`.

        INPUT:

        - ``codim`` -- codimension in which smoothness has to be checked, by
          default complete smoothness will be checked

        OUTPUT:

        ``True`` if ``self`` is smooth (in codimension ``codim``, if it was
        given) and ``False`` otherwise.

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.is_smooth()                                                       # needs palp
            True
            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.is_smooth()
            True
            sage: fan = NormalFan(lattice_polytope.cross_polytope(2))
            sage: fan.is_smooth()
            False
            sage: fan.is_smooth(codim=1)
            True
            sage: fan.generating_cone(0).rays()
            N(-1, -1),
            N(-1,  1)
            in 2-d lattice N
            sage: fan.generating_cone(0).rays().matrix().det()
            -2
        """
    def make_simplicial(self, **kwds):
        """
        Construct a simplicial fan subdividing ``self``.

        It is a synonym for :meth:`subdivide` with ``make_simplicial=True``
        option.

        INPUT:

        - this functions accepts only keyword arguments. See :meth:`subdivide`
          for documentation.

        OUTPUT:

        :class:`rational polyhedral fan
        <sage.geometry.fan.RationalPolyhedralFan>`

        EXAMPLES::

            sage: fan = NormalFan(lattice_polytope.cross_polytope(3))
            sage: fan.is_simplicial()
            False
            sage: fan.ngenerating_cones()
            6
            sage: new_fan = fan.make_simplicial()
            sage: new_fan.is_simplicial()
            True
            sage: new_fan.ngenerating_cones()
            12
        """
    def ngenerating_cones(self):
        """
        Return the number of generating cones of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: fan = toric_varieties.P1xP1().fan()                                   # needs palp
            sage: fan.ngenerating_cones()                                               # needs palp
            4
            sage: cone1 = Cone([(1,0), (0,1)])
            sage: cone2 = Cone([(-1,0)])
            sage: fan = Fan([cone1, cone2])
            sage: fan.ngenerating_cones()
            2
        """
    def plot(self, **options):
        """
        Plot ``self``.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        EXAMPLES::

            sage: fan = toric_varieties.dP6().fan()                                     # needs palp
            sage: fan.plot()                                                            # needs palp sage.plot
            Graphics object consisting of 31 graphics primitives
        """
    def subdivide(self, new_rays=None, make_simplicial: bool = False, algorithm: str = 'default', verbose: bool = False):
        '''
        Construct a new fan subdividing ``self``.

        INPUT:

        - ``new_rays`` -- list of new rays to be added during subdivision, each
          ray must be a list or a vector. May be empty or ``None`` (default);

        - ``make_simplicial`` -- if ``True``, the returned fan is guaranteed to
          be simplicial, default is ``False``;

        - ``algorithm`` -- string with the name of the algorithm used for
          subdivision. Currently there is only one available algorithm called
          "default";

        - ``verbose`` -- if ``True``, some timing information may be printed
          during the process of subdivision

        OUTPUT:

        :class:`rational polyhedral fan
        <sage.geometry.fan.RationalPolyhedralFan>`

        Currently the "default" algorithm corresponds to iterative stellar
        subdivision for each ray in ``new_rays``.

        EXAMPLES::

            sage: fan = NormalFan(lattice_polytope.cross_polytope(3))
            sage: fan.is_simplicial()
            False
            sage: fan.ngenerating_cones()
            6
            sage: fan.nrays()
            8
            sage: new_fan = fan.subdivide(new_rays=[(1,0,0)])
            sage: new_fan.is_simplicial()
            False
            sage: new_fan.ngenerating_cones()
            9
            sage: new_fan.nrays()
            9

        TESTS:

        We check that :issue:`11902` is fixed::

            sage: fan = toric_varieties.P2().fan()                                      # needs palp
            sage: fan.subdivide(new_rays=[(0,0)])                                       # needs palp
            Traceback (most recent call last):
            ...
            ValueError: the origin cannot be used for fan subdivision!
        '''
    def virtual_rays(self, *args):
        '''
        Return (some of the) virtual rays of ``self``.

        Let `N` be the `D`-dimensional
        :meth:`~sage.geometry.cone.IntegralRayCollection.lattice`
        of a `d`-dimensional fan `\\Sigma` in `N_\\RR`. Then the corresponding
        toric variety is of the form `X \\times (\\CC^*)^{D-d}`. The actual
        :meth:`~sage.geometry.cone.IntegralRayCollection.rays` of `\\Sigma`
        give a canonical choice of homogeneous coordinates on `X`. This function
        returns an arbitrary but fixed choice of virtual rays corresponding to a
        (non-canonical) choice of homogeneous coordinates on the torus factor.
        Combinatorially primitive integral generators of virtual rays span the
        `D-d` dimensions of `N_\\QQ` "missed" by the actual rays. (In general
        addition of virtual rays is not sufficient to span `N` over `\\ZZ`.)

        .. NOTE::

            You may use a particular choice of virtual rays by passing optional
            argument ``virtual_rays`` to the :func:`Fan` constructor.

        INPUT:

        - ``ray_list`` -- list of integers; the indices of the
          requested virtual rays. If not specified, all virtual rays of ``self``
          will be returned.

        OUTPUT:

        a :class:`~sage.geometry.point_collection.PointCollection` of
        primitive integral ray generators. Usually (if the fan is
        full-dimensional) this will be empty.

        EXAMPLES::

            sage: f = Fan([Cone([(1,0,1,0), (0,1,1,0)])])
            sage: f.virtual_rays()
            N(1, 0, 0, 0),
            N(0, 0, 0, 1)
            in 4-d lattice N

            sage: f.rays()
            N(1, 0, 1, 0),
            N(0, 1, 1, 0)
            in 4-d lattice N

            sage: f.virtual_rays([0])
            N(1, 0, 0, 0)
            in 4-d lattice N

        You can also give virtual ray indices directly, without
        packing them into a list::

            sage: f.virtual_rays(0)
            N(1, 0, 0, 0)
            in 4-d lattice N

        Make sure that :issue:`16344` is fixed and one can compute
        the virtual rays of fans in non-saturated lattices::

            sage: N = ToricLattice(1)
            sage: B = N.submodule([(2,)]).basis()
            sage: f = Fan([Cone([B[0]])])
            sage: len(f.virtual_rays())
            0

        TESTS::

            sage: N = ToricLattice(4)
            sage: for i in range(10):
            ....:      c = Cone([N.random_element() for j in range(i//2)], lattice=N)
            ....:      if not c.is_strictly_convex():
            ....:          continue
            ....:      f = Fan([c])
            ....:      assert matrix(f.rays() + f.virtual_rays()).rank() == 4
            ....:      assert f.dim() + len(f.virtual_rays()) == 4
        '''
    def primitive_collections(self):
        """
        Return the primitive collections.

        OUTPUT:

        Return the subsets `\\{i_1,\\dots,i_k\\} \\subset \\{ 1,\\dots,n\\}`
        such that

        * The points `\\{p_{i_1},\\dots,p_{i_k}\\}` do not span a cone of
          the fan.

        * If you remove any one `p_{i_j}` from the set, then they do
          span a cone of the fan.

        .. NOTE::

            By replacing the multiindices `\\{i_1,\\dots,i_k\\}` of each
            primitive collection with the monomials `x_{i_1}\\cdots
            x_{i_k}` one generates the Stanley-Reisner ideal in
            `\\ZZ[x_1,\\dots]`.

        REFERENCES:

        - [Bat1991]_

        EXAMPLES::

            sage: fan = Fan([[0,1,3], [3,4], [2,0], [1,2,4]],
            ....:           [(-3, -2, 1), (0, 0, 1), (3, -2, 1), (-1, -1, 1), (1, -1, 1)])
            sage: fan.primitive_collections()
            [frozenset({0, 4}),
             frozenset({2, 3}),
             frozenset({0, 1, 2}),
             frozenset({1, 3, 4})]
        """
    def Stanley_Reisner_ideal(self, ring):
        """
        Return the Stanley-Reisner ideal.

        INPUT:

        - A polynomial ring in ``self.nrays()`` variables.

        OUTPUT: the Stanley-Reisner ideal in the given polynomial ring

        EXAMPLES::

            sage: fan = Fan([[0,1,3], [3,4], [2,0], [1,2,4]],
            ....:           [(-3, -2, 1), (0, 0, 1), (3, -2, 1), (-1, -1, 1), (1, -1, 1)])
            sage: fan.Stanley_Reisner_ideal(PolynomialRing(QQ, 5, 'A, B, C, D, E'))
            Ideal (A*E, C*D, A*B*C, B*D*E) of
             Multivariate Polynomial Ring in A, B, C, D, E over Rational Field
        """
    def linear_equivalence_ideal(self, ring):
        """
        Return the ideal generated by linear relations.

        INPUT:

        - A polynomial ring in ``self.nrays()`` variables.

        OUTPUT:

        Return the ideal, in the given ``ring``, generated by the
        linear relations of the rays. In toric geometry, this
        corresponds to rational equivalence of divisors.

        EXAMPLES::

            sage: fan = Fan([[0,1,3],[3,4],[2,0],[1,2,4]],
            ....:           [(-3, -2, 1), (0, 0, 1), (3, -2, 1), (-1, -1, 1), (1, -1, 1)])
            sage: fan.linear_equivalence_ideal(PolynomialRing(QQ, 5, 'A, B, C, D, E'))
            Ideal (-3*A + 3*C - D + E, -2*A - 2*C - D - E, A + B + C + D + E) of
             Multivariate Polynomial Ring in A, B, C, D, E over Rational Field
        """
    def oriented_boundary(self, cone):
        '''
        Return the facets bounding ``cone`` with their induced
        orientation.

        INPUT:

        - ``cone`` -- a cone of the fan or the whole fan

        OUTPUT:

        The boundary cones of ``cone`` as a formal linear combination
        of cones with coefficients `\\pm 1`. Each summand is a facet of
        ``cone`` and the coefficient indicates whether their (chosen)
        orientation agrees or disagrees with the "outward normal
        first" boundary orientation. Note that the orientation of any
        individual cone is arbitrary. This method once and for all
        picks orientations for all cones and then computes the
        boundaries relative to that chosen orientation.

        If ``cone`` is the fan itself, the generating cones with their
        orientation relative to the ambient space are returned.

        See :meth:`complex` for the associated chain complex. If you
        do not require the orientation, use :meth:`cone.facets()
        <sage.geometry.cone.ConvexRationalPolyhedralCone.facets>`
        instead.

        EXAMPLES::

            sage: # needs palp
            sage: fan = toric_varieties.P(3).fan()
            sage: cone = fan(2)[0]
            sage: bdry = fan.oriented_boundary(cone);  bdry
            -1-d cone of Rational polyhedral fan in 3-d lattice N
            + 1-d cone of Rational polyhedral fan in 3-d lattice N
            sage: bdry[0]
            (-1, 1-d cone of Rational polyhedral fan in 3-d lattice N)
            sage: bdry[1]
            (1, 1-d cone of Rational polyhedral fan in 3-d lattice N)
            sage: fan.oriented_boundary(bdry[0][1])
            -0-d cone of Rational polyhedral fan in 3-d lattice N
            sage: fan.oriented_boundary(bdry[1][1])
            -0-d cone of Rational polyhedral fan in 3-d lattice N

        If you pass the fan itself, this method returns the
        orientation of the generating cones which is determined by the
        order of the rays in :meth:`cone.ray_basis()
        <sage.geometry.cone.IntegralRayCollection.ray_basis>` ::

            sage: fan.oriented_boundary(fan)                                            # needs palp
            -3-d cone of Rational polyhedral fan in 3-d lattice N
            + 3-d cone of Rational polyhedral fan in 3-d lattice N
            - 3-d cone of Rational polyhedral fan in 3-d lattice N
            + 3-d cone of Rational polyhedral fan in 3-d lattice N
            sage: [cone.rays().basis().matrix().det()                                   # needs palp
            ....:  for cone in fan.generating_cones()]
            [-1, 1, -1, 1]

        A non-full dimensional fan::

            sage: cone = Cone([(4,5)])
            sage: fan = Fan([cone])
            sage: fan.oriented_boundary(cone)
            0-d cone of Rational polyhedral fan in 2-d lattice N
            sage: fan.oriented_boundary(fan)
            1-d cone of Rational polyhedral fan in 2-d lattice N

        TESTS::

            sage: fan = toric_varieties.P2().fan()                                      # needs palp
            sage: trivial_cone = fan(0)[0]                                              # needs palp
            sage: fan.oriented_boundary(trivial_cone)                                   # needs palp
            0
        '''
    def toric_variety(self, *args, **kwds):
        """
        Return the associated toric variety.

        INPUT:

        Same arguments as :func:`~sage.schemes.toric.variety.ToricVariety`.

        OUTPUT: a toric variety

        This is equivalent to the command ``ToricVariety(self)`` and
        is provided only as a convenient alternative method to go from the
        fan to the associated toric variety.

        EXAMPLES::

            sage: Fan([Cone([(1,0)]), Cone([(0,1)])]).toric_variety()
            2-d toric variety covered by 2 affine patches
        """
    def complex(self, base_ring=..., extended: bool = False):
        """
        Return the chain complex of the fan.

        To a `d`-dimensional fan `\\Sigma`, one can canonically
        associate a chain complex `K^\\bullet`

        .. MATH::

            0 \\longrightarrow
            \\ZZ^{\\Sigma(d)} \\longrightarrow
            \\ZZ^{\\Sigma(d-1)} \\longrightarrow
            \\cdots \\longrightarrow
            \\ZZ^{\\Sigma(0)} \\longrightarrow
            0

        where the leftmost nonzero entry is in degree `0` and the
        rightmost entry in degree `d`. See [Kly1990]_, eq. (3.2). This
        complex computes the homology of `|\\Sigma|\\subset N_\\RR` with
        arbitrary support,

        .. MATH::

            H_i(K) = H_{d-i}(|\\Sigma|, \\ZZ)_{\\text{non-cpct}}

        For a complete fan, this is just the non-compactly supported
        homology of `\\RR^d`. In this case, `H_0(K)=\\ZZ` and `0` in all
        nonzero degrees.

        For a complete fan, there is an extended chain complex

        .. MATH::

            0 \\longrightarrow
            \\ZZ \\longrightarrow
            \\ZZ^{\\Sigma(d)} \\longrightarrow
            \\ZZ^{\\Sigma(d-1)} \\longrightarrow
            \\cdots \\longrightarrow
            \\ZZ^{\\Sigma(0)} \\longrightarrow
            0

        where we take the first `\\ZZ` term to be in degree -1. This
        complex is an exact sequence, that is, all homology groups
        vanish.

        The orientation of each cone is chosen as in
        :meth:`oriented_boundary`.

        INPUT:

        - ``extended`` -- boolean (default: ``False``); whether to
          construct the extended complex, that is, including the
          `\\ZZ`-term at degree -1 or not

        - ``base_ring`` -- a ring (default: ``ZZ``); the ring to use
          instead of `\\ZZ`

        OUTPUT:

        The complex associated to the fan as a :class:`ChainComplex
        <sage.homology.chain_complex.ChainComplex>`. This raises a
        :exc:`ValueError` if the extended complex is requested for a
        non-complete fan.

        EXAMPLES::

            sage: # needs palp
            sage: fan = toric_varieties.P(3).fan()
            sage: K_normal = fan.complex(); K_normal
            Chain complex with at most 4 nonzero terms over Integer Ring
            sage: K_normal.homology()
            {0: Z, 1: 0, 2: 0, 3: 0}
            sage: K_extended = fan.complex(extended=True); K_extended
            Chain complex with at most 5 nonzero terms over Integer Ring
            sage: K_extended.homology()
            {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0}

        Homology computations are much faster over `\\QQ` if you do not
        care about the torsion coefficients::

            sage: toric_varieties.P2_123().fan().complex(extended=True,                 # needs palp
            ....:                                        base_ring=QQ)
            Chain complex with at most 4 nonzero terms over Rational Field
            sage: _.homology()                                                          # needs palp
            {-1: Vector space of dimension 0 over Rational Field,
             0: Vector space of dimension 0 over Rational Field,
             1: Vector space of dimension 0 over Rational Field,
             2: Vector space of dimension 0 over Rational Field}

        The extended complex is only defined for complete fans::

            sage: fan = Fan([Cone([(1,0)])])
            sage: fan.is_complete()
            False
            sage: fan.complex(extended=True)
            Traceback (most recent call last):
            ...
            ValueError: The extended complex is only defined for complete fans!

        The definition of the complex does not refer to the ambient
        space of the fan, so it does not distinguish a fan from the
        same fan embedded in a subspace::

            sage: K1 = Fan([Cone([(-1,)]), Cone([(1,)])]).complex()
            sage: K2 = Fan([Cone([(-1,0,0)]), Cone([(1,0,0)])]).complex()
            sage: K1 == K2
            True

        Things get more complicated for non-complete fans::

            sage: fan = Fan([Cone([(1,1,1)]),
            ....:            Cone([(1,0,0), (0,1,0)]),
            ....:            Cone([(-1,0,0), (0,-1,0), (0,0,-1)])])
            sage: fan.complex().homology()
            {0: 0, 1: 0, 2: Z x Z, 3: 0}
            sage: fan = Fan([Cone([(1,0,0), (0,1,0)]),
            ....:            Cone([(-1,0,0), (0,-1,0), (0,0,-1)])])
            sage: fan.complex().homology()
            {0: 0, 1: 0, 2: Z, 3: 0}
            sage: fan = Fan([Cone([(-1,0,0), (0,-1,0), (0,0,-1)])])
            sage: fan.complex().homology()
            {0: 0, 1: 0, 2: 0, 3: 0}
        """

def discard_faces(cones):
    """
    Return the cones of the given list which are not faces of each other.

    INPUT:

    - ``cones`` -- list of
      :class:`cones <sage.geometry.cone.ConvexRationalPolyhedralCone>`

    OUTPUT:

    a list of
    :class:`cones <sage.geometry.cone.ConvexRationalPolyhedralCone>`,
    sorted by dimension in decreasing order

    EXAMPLES:

    Consider all cones of a fan::

        sage: Sigma = toric_varieties.P2().fan()                                        # needs palp
        sage: cones = flatten(Sigma.cones())                                            # needs palp
        sage: len(cones)                                                                # needs palp
        7

    Most of them are not necessary to generate this fan::

        sage: from sage.geometry.fan import discard_faces
        sage: len(discard_faces(cones))                                                 # needs palp
        3
        sage: Sigma.ngenerating_cones()                                                 # needs palp
        3
    """
