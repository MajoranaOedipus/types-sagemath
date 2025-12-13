from _typeshed import Incomplete
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.modules import Modules as Modules
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.module import Module as Module
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent

class OverconvergentDistributions_factory(UniqueFactory):
    """
    Create a space of distributions.

    INPUT:

    - ``k`` -- nonnegative integer
    - ``p`` -- prime number or ``None``
    - ``prec_cap`` -- positive integer or ``None``
    - ``base`` -- ring or ``None``
    - ``character`` -- a Dirichlet character or ``None``
    - ``adjuster`` -- ``None`` or callable that turns 2 x 2 matrices into a 4-tuple
    - ``act_on_left`` -- boolean (default: ``False``)
    - ``dettwist`` -- integer or ``None`` (interpreted as 0)
    - ``act_padic`` -- whether monoid should allow `p`-adic coefficients
    - ``implementation`` -- string (default: ``None``); either ``None`` (for
      automatic), ``'long'``, or ``'vector'``

    EXAMPLES::

        sage: D = OverconvergentDistributions(3, 11, 20)
        sage: D
        Space of 11-adic distributions with k=3 action and precision cap 20
        sage: v = D([1,0,0,0,0])
        sage: v.act_right([2,1,0,1])
        (8 + O(11^5), 4 + O(11^4), 2 + O(11^3), 1 + O(11^2), 6 + O(11))

    ::

        sage: D = OverconvergentDistributions(3, 11, 20, dettwist=1)
        sage: v = D([1,0,0,0,0])
        sage: v.act_right([2,1,0,1])
        (5 + 11 + O(11^5), 8 + O(11^4), 4 + O(11^3), 2 + O(11^2), 1 + O(11))
    """
    def create_key(self, k, p=None, prec_cap=None, base=None, character=None, adjuster=None, act_on_left: bool = False, dettwist=None, act_padic: bool = False, implementation=None):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
            sage: OverconvergentDistributions(20, 3, 10)              # indirect doctest
            Space of 3-adic distributions with k=20 action and precision cap 10
            sage: TestSuite(OverconvergentDistributions).run()
        """
    def create_object(self, version, key):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: OverconvergentDistributions(0, 7, 5)              # indirect doctest
            Space of 7-adic distributions with k=0 action and precision cap 5
        """

class Symk_factory(UniqueFactory):
    """
    Create the space of polynomial distributions of degree `k`
    (stored as a sequence of `k + 1` moments).

    INPUT:

    - ``k`` -- integer; the degree (degree `k` corresponds to weight `k + 2`
      modular forms)
    - ``base`` -- ring (default: ``None``); the base ring (``None`` is
      interpreted as `\\QQ`)
    - ``character`` -- Dirichlet character or ``None`` (default: ``None``)
    - ``adjuster`` -- ``None`` or a callable that turns `2 \\times 2` matrices
      into a 4-tuple (default: ``None``)
    - ``act_on_left`` -- boolean (default: ``False``); whether to have the
      group acting on the left rather than the right
    - ``dettwist`` -- integer or ``None``; power of determinant to twist by

    EXAMPLES::

        sage: D = Symk(4)
        sage: loads(dumps(D)) is D
        True
        sage: loads(dumps(D)) == D
        True
        sage: from sage.modular.pollack_stevens.distributions import Symk
        sage: Symk(5)
        Sym^5 Q^2
        sage: Symk(5, RR)
        Sym^5 (Real Field with 53 bits of precision)^2
        sage: Symk(5, oo.parent()) # don't do this
        Sym^5 (The Infinity Ring)^2
        sage: Symk(5, act_on_left = True)
        Sym^5 Q^2

    The ``dettwist`` attribute::

        sage: V = Symk(6)
        sage: v = V([1,0,0,0,0,0,0])
        sage: v.act_right([2,1,0,1])
        (64, 32, 16, 8, 4, 2, 1)
        sage: V = Symk(6, dettwist=-1)
        sage: v = V([1,0,0,0,0,0,0])
        sage: v.act_right([2,1,0,1])
        (32, 16, 8, 4, 2, 1, 1/2)
    """
    def create_key(self, k, base=None, character=None, adjuster=None, act_on_left: bool = False, dettwist=None, act_padic: bool = False, implementation=None):
        """
        Sanitize input.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import Symk
            sage: Symk(6) # indirect doctest
            Sym^6 Q^2

            sage: V = Symk(6, Qp(7))
            sage: TestSuite(V).run()
        """
    def create_object(self, version, key):
        """
        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import Symk
            sage: Symk(6) # indirect doctest
            Sym^6 Q^2
        """

OverconvergentDistributions: Incomplete
Symk: Incomplete

class OverconvergentDistributions_abstract(Module):
    """
    Parent object for distributions. Not to be used directly, see derived
    classes :class:`Symk_class` and :class:`OverconvergentDistributions_class`.

    INPUT:

    - ``k`` -- integer; `k` is the usual modular forms weight minus 2
    - ``p`` -- ``None`` or prime
    - ``prec_cap`` -- ``None`` or positive integer
    - ``base`` -- ``None`` or the base ring over which to construct the distributions
    - ``character`` -- ``None`` or Dirichlet character
    - ``adjuster`` -- ``None`` or a way to specify the action among different conventions
    - ``act_on_left`` -- boolean (default: ``False``)
    - ``dettwist`` -- ``None`` or integer (twist by determinant); ignored for Symk spaces
    - ``act_padic`` -- boolean (default: ``False``); if ``True``, will allow
      action by `p`-adic matrices
    - ``implementation`` -- string (default: ``None``); either automatic (if ``None``),
      ``'vector'`` or ``'long'``

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
        sage: OverconvergentDistributions(2, 17, 100)
        Space of 17-adic distributions with k=2 action and precision cap 100

        sage: D = OverconvergentDistributions(2, 3, 5); D
        Space of 3-adic distributions with k=2 action and precision cap 5
        sage: type(D)
        <class 'sage.modular.pollack_stevens.distributions.OverconvergentDistributions_class_with_category'>
    """
    Element: Incomplete
    def __init__(self, k, p=None, prec_cap=None, base=None, character=None, adjuster=None, act_on_left: bool = False, dettwist=None, act_padic: bool = False, implementation=None) -> None:
        """
        See ``OverconvergentDistributions_abstract`` for full documentation.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
            sage: D = OverconvergentDistributions(2, 3, 5); D
            Space of 3-adic distributions with k=2 action and precision cap 5
            sage: type(D)
            <class 'sage.modular.pollack_stevens.distributions.OverconvergentDistributions_class_with_category'>

        `p` must be a prime, but `p=6` below, which is not prime::

            sage: OverconvergentDistributions(k=0, p=6, prec_cap=10)
            Traceback (most recent call last):
            ...
            ValueError: p must be prime
        """
    def acting_matrix(self, g, M):
        """
        Return the matrix for the action of `g` on ``self``, truncated to
        the first `M` moments.

        EXAMPLES::

            sage: V = Symk(3)
            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: V.acting_matrix(Sigma0(1)([3,4,0,1]), 4)
            [27 36 48 64]
            [ 0  9 24 48]
            [ 0  0  3 12]
            [ 0  0  0  1]

            sage: from sage.modular.btquotients.pautomorphicform import _btquot_adjuster
            sage: V = Symk(3, adjuster = _btquot_adjuster())
            sage: from sage.modular.pollack_stevens.sigma0 import Sigma0
            sage: V.acting_matrix(Sigma0(1)([3,4,0,1]), 4)
            [  1   4  16  64]
            [  0   3  24 144]
            [  0   0   9 108]
            [  0   0   0  27]
        """
    def prime(self):
        """
        Return prime `p` such that this is a space of `p`-adic distributions.

        In case this space is Symk of a non-padic field, we return 0.

        OUTPUT: a prime or 0

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7); D
            Space of 7-adic distributions with k=0 action and precision cap 20
            sage: D.prime()
            7
            sage: D = Symk(4, base=GF(7)); D
            Sym^4 (Finite Field of size 7)^2
            sage: D.prime()
            0

        But Symk of a `p`-adic field does work::

            sage: D = Symk(4, base=Qp(7)); D
            Sym^4 Q_7^2
            sage: D.prime()
            7
            sage: D.is_symk()
            True
        """
    def weight(self):
        """
        Return the weight of this distribution space.

        The standard caveat applies, namely that the weight of `Sym^k`
        is defined to be `k`, not `k+2`.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7); D
            Space of 7-adic distributions with k=0 action and precision cap 20
            sage: D.weight()
            0
            sage: OverconvergentDistributions(389, 7).weight()
            389
        """
    def precision_cap(self):
        """
        Return the precision cap on distributions.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 10); D
            Space of 7-adic distributions with k=0 action and precision cap 10
            sage: D.precision_cap()
            10
            sage: D = Symk(389, base=QQ); D
            Sym^389 Q^2
            sage: D.precision_cap()
            390
        """
    def lift(self, p=None, M=None, new_base_ring=None):
        """
        Return distribution space that contains lifts with given ``p``,
        precision cap ``M``, and base ring ``new_base_ring``.

        INPUT:

        - ``p`` -- prime or ``None``
        - ``M`` -- nonnegative integer or ``None``
        - ``new_base_ring`` -- ring or ``None``

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = Symk(0, Qp(7)); D
            Sym^0 Q_7^2
            sage: D.lift(M=20)
            Space of 7-adic distributions with k=0 action and precision cap 20
            sage: D.lift(p=7, M=10)
            Space of 7-adic distributions with k=0 action and precision cap 10
            sage: D.lift(p=7, M=10, new_base_ring=QpCR(7,15)).base_ring()
            7-adic Field with capped relative precision 15
        """
    @cached_method
    def approx_module(self, M=None):
        """
        Return the `M`-th approximation module, or if `M` is not specified,
        return the largest approximation module.

        INPUT:

        - ``M`` -- ``None`` or nonnegative integer that is at most the
          precision cap

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
            sage: D = OverconvergentDistributions(0, 5, 10)
            sage: D.approx_module()
            Ambient free module of rank 10 over the principal ideal domain 5-adic Ring with capped absolute precision 10
            sage: D.approx_module(1)
            Ambient free module of rank 1 over the principal ideal domain 5-adic Ring with capped absolute precision 10
            sage: D.approx_module(0)
            Ambient free module of rank 0 over the principal ideal domain 5-adic Ring with capped absolute precision 10

        Note that ``M`` must be at most the precision cap, and must be nonnegative::

            sage: D.approx_module(11)
            Traceback (most recent call last):
            ...
            ValueError: M (=11) must be less than or equal to the precision cap (=10)
            sage: D.approx_module(-1)
            Traceback (most recent call last):
            ...
            ValueError: rank (=-1) must be nonnegative
        """
    def random_element(self, M=None, **args):
        """
        Return a random element of the `M`-th approximation module with
        nonnegative valuation.

        INPUT:

        - ``M`` -- ``None`` or a nonnegative integer

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
            sage: D = OverconvergentDistributions(0, 5, 10)
            sage: D.random_element()
            (..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
            sage: D.random_element(0)
            ()
            sage: D.random_element(5)
            (..., ..., ..., ..., ...)
            sage: D.random_element(-1)
            Traceback (most recent call last):
            ...
            ValueError: rank (=-1) must be nonnegative
            sage: D.random_element(11)
            Traceback (most recent call last):
            ...
            ValueError: M (=11) must be less than or equal to the precision cap (=10)
        """
    def clear_cache(self) -> None:
        """
        Clear some caches that are created only for speed purposes.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 10)
            sage: D.clear_cache()
        """
    @cached_method
    def basis(self, M=None):
        """
        Return a basis for this space of distributions.

        INPUT:

        - ``M`` -- (default: ``None``) if not ``None``, specifies the ``M``-th
          approximation module, in case that this makes sense

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 4); D
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D.basis()
            [(1 + O(7^4), O(7^3), O(7^2), O(7)),
             (O(7^4), 1 + O(7^3), O(7^2), O(7)),
             (O(7^4), O(7^3), 1 + O(7^2), O(7)),
             (O(7^4), O(7^3), O(7^2), 1 + O(7))]
            sage: D.basis(2)
            [(1 + O(7^2), O(7)), (O(7^2), 1 + O(7))]
            sage: D = Symk(3, base=QQ); D
            Sym^3 Q^2
            sage: D.basis()
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
            sage: D.basis(2)
            Traceback (most recent call last):
            ...
            ValueError: Sym^k objects do not support approximation modules
        """

class Symk_class(OverconvergentDistributions_abstract):
    def __init__(self, k, base, character, adjuster, act_on_left, dettwist, act_padic, implementation) -> None:
        """
        EXAMPLES::

            sage: D = sage.modular.pollack_stevens.distributions.Symk(4); D
            Sym^4 Q^2
            sage: TestSuite(D).run() # indirect doctest
        """
    def is_symk(self) -> bool:
        """
        Whether or not this distributions space is `Sym^k(R)` for some ring `R`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(4, 17, 10); D
            Space of 17-adic distributions with k=4 action and precision cap 10
            sage: D.is_symk()
            False
            sage: D = Symk(4); D
            Sym^4 Q^2
            sage: D.is_symk()
            True
            sage: D = Symk(4, base=GF(7)); D
            Sym^4 (Finite Field of size 7)^2
            sage: D.is_symk()
            True
        """
    def change_ring(self, new_base_ring):
        """
        Return a Symk with the same `k` but a different base ring.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 4); D
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D.base_ring()
            7-adic Ring with capped absolute precision 4
            sage: D2 = D.change_ring(QpCR(7)); D2
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D2.base_ring()
            7-adic Field with capped relative precision 20
        """
    def base_extend(self, new_base_ring):
        """
        Extend scalars to a new base ring.

        EXAMPLES::

            sage: Symk(3).base_extend(Qp(3))
            Sym^3 Q_3^2
        """

class OverconvergentDistributions_class(OverconvergentDistributions_abstract):
    """
    The class of overconvergent distributions.

    This class represents the module of finite approximation modules, which are finite-dimensional
    spaces with a `\\Sigma_0(N)` action which approximate the module of overconvergent distributions.
    There is a specialization map to the finite-dimensional Symk module as well.

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions
        sage: D = OverconvergentDistributions(0, 5, 10)
        sage: TestSuite(D).run()
    """
    def is_symk(self) -> bool:
        """
        Whether or not this distributions space is `Sym^k(R)` for some ring `R`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(4, 17, 10); D
            Space of 17-adic distributions with k=4 action and precision cap 10
            sage: D.is_symk()
            False
            sage: D = Symk(4); D
            Sym^4 Q^2
            sage: D.is_symk()
            True
            sage: D = Symk(4, base=GF(7)); D
            Sym^4 (Finite Field of size 7)^2
            sage: D.is_symk()
            True
        """
    def change_ring(self, new_base_ring):
        """
        Return space of distributions like this one, but with the base ring changed.

        INPUT:

        - ``new_base_ring`` -- a ring over which the distribution can be coerced

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 4); D
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D.base_ring()
            7-adic Ring with capped absolute precision 4
            sage: D2 = D.change_ring(QpCR(7)); D2
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D2.base_ring()
            7-adic Field with capped relative precision 20
        """
    def specialize(self, new_base_ring=None):
        """
        Return distribution space got by specializing to `Sym^k`, over
        the ``new_base_ring``.  If ``new_base_ring`` is not given, use current
        ``base_ring``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import OverconvergentDistributions, Symk
            sage: D = OverconvergentDistributions(0, 7, 4); D
            Space of 7-adic distributions with k=0 action and precision cap 4
            sage: D.is_symk()
            False
            sage: D2 = D.specialize(); D2
            Sym^0 Z_7^2
            sage: D2.is_symk()
            True
            sage: D2 = D.specialize(QQ); D2
            Sym^0 Q^2
        """
