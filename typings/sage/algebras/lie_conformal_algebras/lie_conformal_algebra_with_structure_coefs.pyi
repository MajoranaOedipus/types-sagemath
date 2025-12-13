from .finitely_freely_generated_lca import FinitelyFreelyGeneratedLCA as FinitelyFreelyGeneratedLCA
from .lie_conformal_algebra_element import LCAStructureCoefficientsElement as LCAStructureCoefficientsElement
from sage.arith.misc import binomial as binomial
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators, standardize_names_index_set as standardize_names_index_set

class LieConformalAlgebraWithStructureCoefficients(FinitelyFreelyGeneratedLCA):
    """
    A Lie conformal algebra with a set of specified structure
    coefficients.

    INPUT:

    - ``R`` -- a ring (default: ``None``); the base ring of this Lie
      conformal algebra. Behaviour is undefined if it is not a field
      of characteristic zero.

    - ``s_coeff`` -- dictionary (default: ``None``);
      a dictionary containing the `\\lambda` brackets of the
      generators of this Lie conformal algebra. The family encodes a
      dictionary whose keys
      are pairs of either names or indices of the generators
      and the values are themselves dictionaries. For a pair of
      generators `a` and `b`, the value of ``s_coeff[('a','b')]`` is
      a dictionary whose keys are positive integer numbers and the
      corresponding value for the key `j` is a dictionary itself
      representing the `j`-th product `a_{(j)}b`.
      Thus, for a positive integer number `j`, the value of
      ``s_coeff[('a','b')][j]`` is a dictionary whose entries are
      pairs ``('c',n)`` where ``'c'`` is the name of a generator
      and `n` is a positive number. The value for this key is the
      coefficient of `\\frac{T^{n}}{n!} c` in `a_{(j)}b`. For example
      the ``s_coeff`` for the *Virasoro* Lie conformal algebra is::

            {('L','L'):{0:{('L',1):1}, 1:{('L',0):2}, 3:{('C',0):1/2}}}


      Do not include central elements in this dictionary. Also, if
      the key ``('a','b')`` is present, there is no need to include
      ``('b','a')`` as it is defined by skew-symmetry.
      Any missing pair (besides the ones
      defined by skew-symmetry) is assumed to have vanishing
      `\\lambda`-bracket.

    - ``names`` -- tuple of strings (default: ``None``); the list of
      names for generators of this Lie conformal algebra. Do not
      include central elements in this list.

    - ``central_elements`` -- tuple of strings (default: ``None``);
      a list of names for central elements of this Lie conformal algebra

    - ``index_set`` -- enumerated set (default: ``None``);
      an indexing set for the generators of this Lie
      conformal algebra. Do not include central elements in this
      list.

    - ``parity`` -- tuple of `0` or `1` (default: tuple of `0`);
      a tuple specifying the parity of each non-central generator

    EXAMPLES:

    - We construct the `\\beta-\\gamma` system by directly giving the
      `\\lambda`-brackets of the generators::

        sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
        sage: V = LieConformalAlgebra(QQ, betagamma_dict, names=('a','b'),
        ....:         weights=(1,0), central_elements=('K',))
        sage: V.category()
        Category of H-graded finitely generated Lie conformal algebras
        with basis over Rational Field
        sage: V.inject_variables()
        Defining a, b, K
        sage: a.bracket(b)
        {0: -K}

    - We construct the centerless Virasoro Lie conformal algebra::

        sage: virdict =  {('L','L'):{0:{('L',1):1}, 1:{('L',0): 2}}}
        sage: R = LieConformalAlgebra(QQbar, virdict, names='L')
        sage: R.inject_variables()
        Defining L
        sage: L.bracket(L)
        {0: TL, 1: 2*L}

    - The construction checks that skew-symmetry is violated::

        sage: wrongdict =  {('L','L'):{0:{('L',1):2}, 1:{('L',0): 2}}}
        sage: LieConformalAlgebra(QQbar, wrongdict, names='L')
        Traceback (most recent call last):
        ...
        ValueError: two distinct values given for one and the same bracket. Skew-symmetry is not satisfied?
    """
    def __init__(self, R, s_coeff, index_set=None, central_elements=None, category=None, element_class=None, prefix=None, names=None, latex_names=None, parity=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.NeveuSchwarz(QQ)
            sage: TestSuite(V).run()
        """
    def structure_coefficients(self):
        """
        The structure coefficients of this Lie conformal algebra.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(AA)
            sage: Vir.structure_coefficients()
            Finite family {('L', 'L'): ((0, TL), (1, 2*L), (3, 1/2*C))}

            sage: lie_conformal_algebras.NeveuSchwarz(QQ).structure_coefficients()
            Finite family {('G', 'G'): ((0, 2*L), (2, 2/3*C)),
            ('G', 'L'): ((0, 1/2*TG), (1, 3/2*G)),
            ('L', 'G'): ((0, TG), (1, 3/2*G)),
            ('L', 'L'): ((0, TL), (1, 2*L), (3, 1/2*C))}
        """
