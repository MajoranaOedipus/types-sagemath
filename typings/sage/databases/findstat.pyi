from _typeshed import Incomplete
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.alternating_sign_matrix import AlternatingSignMatrices as AlternatingSignMatrices, AlternatingSignMatrix as AlternatingSignMatrix
from sage.combinat.binary_tree import BinaryTree as BinaryTree, BinaryTrees as BinaryTrees
from sage.combinat.colored_permutations import SignedPermutation as SignedPermutation, SignedPermutations as SignedPermutations
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.core import Core as Core, Cores as Cores
from sage.combinat.decorated_permutation import DecoratedPermutation as DecoratedPermutation, DecoratedPermutations as DecoratedPermutations
from sage.combinat.dyck_word import DyckWord as DyckWord, DyckWords as DyckWords
from sage.combinat.gelfand_tsetlin_patterns import GelfandTsetlinPattern as GelfandTsetlinPattern, GelfandTsetlinPatterns as GelfandTsetlinPatterns
from sage.combinat.ordered_tree import OrderedTree as OrderedTree, OrderedTrees as OrderedTrees
from sage.combinat.parking_functions import ParkingFunction as ParkingFunction, ParkingFunctions as ParkingFunctions
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.perfect_matching import PerfectMatching as PerfectMatching, PerfectMatchings as PerfectMatchings
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.combinat.plane_partition import PlanePartition as PlanePartition
from sage.combinat.posets.lattices import FiniteLatticePoset as FiniteLatticePoset, LatticePoset as LatticePoset
from sage.combinat.posets.poset_examples import Posets as Posets
from sage.combinat.posets.posets import FinitePoset as FinitePoset, Poset as Poset
from sage.combinat.root_system.cartan_type import CartanType as CartanType, CartanType_abstract as CartanType_abstract
from sage.combinat.set_partition import SetPartition as SetPartition, SetPartitions as SetPartitions
from sage.combinat.set_partition_ordered import OrderedSetPartition as OrderedSetPartition, OrderedSetPartitions as OrderedSetPartitions
from sage.combinat.skew_partition import SkewPartition as SkewPartition, SkewPartitions as SkewPartitions
from sage.combinat.tableau import SemistandardTableau as SemistandardTableau, SemistandardTableaux as SemistandardTableaux, StandardTableau as StandardTableau, StandardTableaux as StandardTableaux
from sage.combinat.words.abstract_word import Word_class as Word_class
from sage.combinat.words.word import Word as Word
from sage.combinat.words.words import Words as Words
from sage.databases.oeis import FancyTuple as FancyTuple
from sage.graphs.graph import Graph as Graph
from sage.graphs.graph_generators import graphs as graphs
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_list import lazy_list as lazy_list
from sage.misc.verbose import verbose as verbose
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import NamedTuple

FINDSTAT_URL: str
FINDSTAT_API: Incomplete
FINDSTAT_API_COLLECTIONS: Incomplete
FINDSTAT_API_STATISTICS: Incomplete
FINDSTAT_API_MAPS: Incomplete
FINDSTAT_URL_LOGIN: Incomplete
FINDSTAT_URL_COLLECTIONS: Incomplete
FINDSTAT_URL_STATISTICS: Incomplete
FINDSTAT_URL_EDIT_STATISTIC: Incomplete
FINDSTAT_URL_NEW_STATISTIC: Incomplete
FINDSTAT_URL_MAPS: Incomplete
FINDSTAT_URL_EDIT_MAP: Incomplete
FINDSTAT_URL_NEW_MAP: Incomplete
FINDSTAT_MAX_VALUES: int
FINDSTAT_MIN_VALUES: int
FINDSTAT_DEFAULT_DEPTH: int
FINDSTAT_MAX_SUBMISSION_VALUES: int
FINDSTAT_SEPARATOR_NAME: str
FINDSTAT_VALUE_SEPARATOR: str
FINDSTAT_MAP_SEPARATOR: str
FINDSTAT_STATISTIC_REGEXP: str
FINDSTAT_MAP_REGEXP: str
FINDSTAT_COLLECTION_REGEXP: str
FINDSTAT_STATISTIC_PADDED_IDENTIFIER: str
FINDSTAT_MAP_PADDED_IDENTIFIER: str
FINDSTAT_COLLECTION_PADDED_IDENTIFIER: str
FINDSTAT_POST_HEADER: str
FINDSTAT_NEWSTATISTIC_FORM_HEADER: str
FINDSTAT_NEWMAP_FORM_HEADER: str
FINDSTAT_FORM_FORMAT: str
FINDSTAT_FORM_FOOTER: str

class FindStat(UniqueRepresentation, SageObject):
    """
    The Combinatorial Statistic Finder.

    :class:`FindStat` is a class preserving user information.
    """
    def __init__(self) -> None:
        """
        Initialize the database.

        TESTS::

            sage: findstat()
            The Combinatorial Statistic Finder (https://www.findstat.org/)
        """
    def browse(self) -> None:
        """
        Open the FindStat web page in a browser.

        EXAMPLES::

            sage: findstat().browse()                                           # optional -- webbrowser
        """
    def set_user(self, name=None, email=None) -> None:
        """
        Set the user for the session.

        INPUT:

        - ``name`` -- the name of the user

        - ``email`` -- an email address of the user

        This information is used when submitting a statistic with
        :meth:`FindStatStatistic.submit`.

        EXAMPLES::

            sage: findstat().set_user(name='Anonymous', email='invalid@org')

        .. NOTE::

            It is usually more convenient to login into the FindStat
            web page using the :meth:`login` method.
        """
    def user_name(self):
        """
        Return the user name used for submissions.

        EXAMPLES::

            sage: findstat().set_user(name='Anonymous', email='invalid@org')
            sage: findstat().user_name()
            'Anonymous'
        """
    def user_email(self):
        """
        Return the user name used for submissions.

        EXAMPLES::

            sage: findstat().set_user(name='Anonymous', email='invalid@org')
            sage: findstat().user_email()
            'invalid@org'
        """
    def login(self) -> None:
        """
        Open the FindStat login page in a browser.

        EXAMPLES::

            sage: findstat().login()                                            # optional -- webbrowser
        """

def findstat(query=None, values=None, distribution=None, domain=None, depth=..., max_values=...):
    '''
    Return matching statistics.

    INPUT:

    One of the following:

    - an integer or a string representing a valid FindStat identifier
      (e.g. 45 or \'St000045\').  The keyword arguments ``depth`` and
      ``max_values`` are ignored, ``values`` and ``distribution``
      must be ``None``.

    - a list of pairs of the form ``(object, value)``, or a
      dictionary from Sage objects to integer values.  The keyword
      arguments ``depth`` and ``max_values`` are passed to the
      finder, ``values`` and ``distribution`` must be ``None``.

    - a list of pairs of the form (list of objects, list of values),
      or a single pair of the form (list of objects, list of values).
      In each pair there should be as many objects as values.  The
      keyword arguments ``depth`` and ``max_values`` are passed to
      the finder.

    - a collection and a list of pairs of the form (string, value),
      or a dictionary from strings to integer values.  The keyword
      arguments ``depth`` and ``max_values`` are passed to the
      finder.  This should only be used if the collection is not yet
      supported.

    - a collection and a callable.  The callable is used to generate
      ``max_values`` ``(object, value)`` pairs.  The number of terms
      generated may also be controlled by passing an iterable
      collection, such as ``Permutations(3)``.  The keyword arguments
      ``depth`` and ``max_values`` are passed to the finder.

    OUTPUT: an instance of a :class:`FindStatStatistic`, represented by

    - the FindStat identifier together with its name, or

    - a list of triples, each consisting of

        - the statistic

        - a list of strings naming certain maps

        - a number which says how many of the values submitted agree
          with the values in the database, when applying the maps in
          the given order to the object and then computing the
          statistic on the result.

    EXAMPLES:

    A particular statistic can be retrieved by its St-identifier or
    number::

        sage: findstat(\'St000041\')                                              # optional -- internet
        St000041: The number of nestings of a perfect matching.

        sage: findstat(51)                                                      # optional -- internet
        St000051: The size of the left subtree of a binary tree.

        sage: findstat(\'St000042oMp00116\')                                      # optional -- internet
        St000042oMp00116

    The database can be searched by providing a list of pairs::

        sage: l = [m for n in range(1, 4) for m in PerfectMatchings(2*n)]
        sage: findstat([(m, m.number_of_nestings()) for m in l], depth=0)       # optional -- internet
        0: St000041 (quality [100, 100])

    or a dictionary::

        sage: findstat({m: m.number_of_nestings() for m in l}, depth=0)         # optional -- internet
        0: St000041 (quality [100, 100])

    Note however, that the results of these two queries need not
    compare equal, because we compare queries by the data
    sent, and the ordering of the data might be different.

    Another possibility is to send a collection and a function.  In
    this case, the function is applied to the first few objects of
    the collection::

        sage: findstat("Perfect Matchings", lambda m: m.number_of_nestings(), depth=0)    # optional -- internet
        0: St000041 (quality [20, 100])

    To search for a distribution, send a list of lists, or a single pair::

        sage: PM = PerfectMatchings(10); findstat((PM, [m.number_of_nestings() for m in PM]), depth=0) # optional -- internet
        0: St000042 (quality [100, 100])
        1: St000041 (quality [9, 100])

    Alternatively, specify the ``distribution`` parameter::

        sage: findstat(12, distribution=lambda m: m.number_of_nestings(), depth=0) # optional -- internet
        0: St000041 (quality [100, 100])
        1: St000042 (quality [100, 100])

    Note that there is a limit, ``FINDSTAT_MAX_VALUES``, on the number
    of elements that may be submitted to FindStat, which is currently
    1000.  Therefore, the interface tries to truncate queries
    appropriately, but this may be impossible, especially with
    distribution searches::

        sage: PM = PerfectMatchings(12); PM.cardinality()                       # optional -- internet
        10395
        sage: findstat((PM, [1 for m in PM]))                                   # optional -- internet
        Traceback (most recent call last):
        ...
        ValueError: E016: The statistic finder was unable to perform a search on your data. The following errors have occured:
        <BLANKLINE>
        You passed too few elements (0 < 3) to FindStat!

    Finally, we can also retrieve all statistics with a given domain::

        sage: findstat("Cc0024")                                                # optional -- internet
        Set of combinatorial statistics with domain Cc0024: Binary words in FindStat

        sage: findstat(domain=\'Cores\')                                          # optional -- internet
        Set of combinatorial statistics with domain Cc0013: Cores in FindStat

    TESTS::

        sage: findstat("Permutations", lambda x: 1, depth=\'x\')                  # optional -- internet
        Traceback (most recent call last):
        ...
        ValueError: E021: Depth should be a nonnegative integer at most 9, but is x.

        sage: findstat("Permutations", lambda x: 1, depth=100)                  # optional -- internet
        Traceback (most recent call last):
        ...
        ValueError: E021: Depth should be a nonnegative integer at most 9, but is 100.

        sage: S = Permutation
        sage: findstat([(S([1,2]), 1), ([S([1,3,2]), S([1,2])], [2,3])])        # optional -- internet
        Traceback (most recent call last):
        ...
        ValueError: FindStat expects that every object occurs at most once: [1, 2]

    Check that values which can be converted to integers are supported::

        sage: findstat([(m, m.number_of_nestings()/1) for m in PerfectMatchings(10)], depth=0) # optional -- internet
        0: St000041 (quality [9, 100])

    Check that ``None`` values are omitted::

        sage: findstat("graphs", lambda g: g.diameter() if g.is_connected() else None, max_values=100, depth=0) # optional -- internet
        0: St000259 (quality [100, 100])
    '''
def findmap(*args, **kwargs):
    '''
    Return matching maps.

    INPUT:

    Valid keywords are: ``domain``, ``codomain``, ``values``,
    ``distribution``, ``depth`` and ``max_values``. They have the
    following meanings:

    - ``depth`` -- nonnegative integer (default: ``FINDSTAT_DEFAULT_DEPTH``);
      specifying how many maps to apply to generate the given map

    - ``max_values`` -- integer (default: ``FINDSTAT_MAX_VALUES``); specifying
      how many values are sent to the finder

    - ``domain``, ``codomain`` -- integer or string of the form
      ``Cc1234``, designates the domain and codomain of the sought
      for maps

    - ``values``, ``distribution`` -- data specifying the values or
      distribution of values of the sought for maps.  The keyword
      arguments ``depth`` and ``max_values`` are passed to the
      finder.  The data may be specified in one of the following
      forms:

        - a list of pairs of the form ``(object, value)``, or a
          dictionary from Sage objects to Sage objects.

        - a list of pairs of the form ``(list of objects, list of
          values)``, or a single pair of the form ``(list of objects,
          list of values)``.  In each pair there should be as many
          objects as values.

        - a callable.  In this case, the domain must be specified,
          also.  The callable is then used to generate ``max_values``
          ``(object, value)`` pairs.

          The number of terms generated may also be controlled by
          passing an iterable collection, such as
          ``Permutations(3)``.

    ``findmap`` also accepts at most three positional arguments as
    follows:

    - a single positional argument, if none of ``domain``,
      ``codomain``, ``values`` or ``distribution`` are specified, is
      interpreted as a FindStat map identifier.  If further arguments
      are given and it is a string, it is interpreted as a domain.
      If all this fails, it is interpreted as the specification of
      values.

    - if two positional arguments are given, the first is interpreted
      as domain, and the second either as codomain or the
      specification of values.

    - if three positional arguments are given, the first two are
      interpreted as domain and codomain, and the third as the
      specification of values.

    OUTPUT:

    An instance of a :class:`FindStatMap`, :class:`FindStatMapQuery`
    or :class:`FindStatMaps`.

    EXAMPLES:

    A particular map can be retrieved by its Mp-identifier or
    number::

        sage: findmap(\'Mp00062\')                                                # optional -- internet
        Mp00062: Lehmer-code to major-code bijection

        sage: findmap(62)                                                       # optional -- internet
        Mp00062: Lehmer-code to major-code bijection

        sage: findmap("Mp00099oMp00127")                                        # optional -- internet
        Mp00099oMp00127

    The database can be searched by providing a list of pairs::

        sage: l = [pi for n in range(5) for pi in Permutations(n)]
        sage: findmap([(pi, pi.complement().increasing_tree_shape()) for pi in l], depth=2) # optional -- internet
        0: Mp00061oMp00069 (quality [...])

    or a dictionary::

        sage: findmap({pi: pi.complement().increasing_tree_shape() for pi in l}, depth=2) # optional -- internet
        0: Mp00061oMp00069 (quality [...])

    Note however, that the results of these two queries need not
    compare equal, because we compare queries by the data
    sent, and the ordering of the data might be different.

    Another possibility is to send a collection and a function.  In
    this case, the function is applied to the first few objects of
    the collection::

        sage: findmap("Permutations", lambda pi: pi.increasing_tree_shape(), depth=1)     # optional -- internet
        0: Mp00061 (quality [100])

    In rare cases, it may not be possible to guess the codomain of a
    map, in which case it can be provided as second argument or
    keyword argument::

        sage: findmap("Dyck paths", "Perfect matchings", lambda D: [(a+1, b) for a,b in D.tunnels()]) # optional -- internet
        0: Mp00146 (quality [100])

        sage: findmap("Dyck paths", "Set partitions", lambda D: [(a+1, b) for a,b in D.tunnels()]) # optional -- internet
        0: Mp00092oMp00146 (quality [...])

    Finally, we can also retrieve all maps with a given domain or codomain::

        sage: findmap("Cc0024")                                                 # optional -- internet
        Set of combinatorial maps with domain Cc0024: Binary words used by FindStat

        sage: findmap(codomain=\'Cores\')                                         # optional -- internet
        Set of combinatorial maps with codomain Cc0013: Cores used by FindStat
    '''

class FindStatFunction(SageObject):
    """
    A class providing the common methods of :class:`FindStatMap` and
    :class:`FindStatStatistic`.

    This class provides methods to access and modify properties of a
    single statistic or map of the FindStat database.
    """
    def __init__(self, id, data=None, function=None) -> None:
        '''
        Initialize a statistic or map.

        INPUT:

        - ``id`` -- a padded identifier, with number 0 reserved for new
          statistics or maps.

        - ``data`` -- dictionary with "Description", "Code", etc.

        - ``function`` -- (optional) a callable implementing the
          statistic or map, or ``None``

        ``data`` should be provided if and only if ``id`` refers to a
        new statistic or map (with identifier 0).

        TESTS::

            sage: from sage.databases.findstat import FindStatFunction, FindStatCollection
            sage: FindStatFunction("St000000",                                  # optional -- internet
            ....:                  data={"Bibliography": {},
            ....:                        "Code": "",
            ....:                        "Description" : "",
            ....:                        "Domain": FindStatCollection(1),
            ....:                        "Name": "a new statistic",
            ....:                        "References": "",
            ....:                        "SageCode": ""})
            St000000: a new statistic
        '''
    def __call__(self, elt):
        '''
        Apply the function to a given element.

        EXAMPLES::

            sage: s = lambda g: g.diameter() if g.is_connected() else None
            sage: q = findstat("graphs", s, max_values=100)                     # optional -- internet
            sage: q(graphs.PetersenGraph().copy(immutable=True))                # optional -- internet
            2
        '''
    def reset(self) -> None:
        '''
        Discard all modification of the statistic or map.

        EXAMPLES::

            sage: s = findmap(62)                                               # optional -- internet
            sage: s.set_name(u"Möbius"); s                                      # optional -- internet
            Mp00062(modified): Möbius
            sage: s.reset(); s                                                  # optional -- internet
            Mp00062: Lehmer-code to major-code bijection

        TESTS:

        Check that new statistics and maps cannot be reset::

            sage: # optional - internet
            sage: q = findstat([(d, randint(1, 1000)) for d in DyckWords(4)])
            sage: q.set_description("Random values on Dyck paths.")
            sage: print(q.description())
            Random values on Dyck paths.
            sage: q.reset()
            Traceback (most recent call last):
            ...
            ValueError: cannot reset values of St000000: a new statistic on Dyck paths
        '''
    def id(self):
        """
        Return the FindStat identifier of the statistic or map.

        OUTPUT: the FindStat identifier of the statistic or map, as an integer

        EXAMPLES::

            sage: findstat(51).id()                                             # optional -- internet
            51
        """
    def id_str(self):
        """
        Return the FindStat identifier of the statistic or map.

        OUTPUT: the FindStat identifier of the statistic or map, as a string

        EXAMPLES::

            sage: findstat(51).id_str()                                         # optional -- internet
            'St000051'
        """
    def domain(self):
        """
        Return the FindStat domain of the statistic or map.

        OUTPUT:

        The domain of the statistic or map as an instance of
        :class:`FindStatCollection`.

        EXAMPLES::

            sage: findstat(51).domain()                                         # optional -- internet
            Cc0010: Binary trees

            sage: findmap(62).domain()                                          # optional -- internet
            Cc0001: Permutations
        """
    def description(self):
        """
        Return the description of the statistic or map.

        OUTPUT: string; for statistics, the first line is used as name

        EXAMPLES::

            sage: print(findstat(51).description())                             # optional -- internet
            The size of the left subtree of a binary tree.
        """
    def set_description(self, value) -> None:
        '''
        Set the description of the statistic or map.

        INPUT:

        - ``value`` -- string; for statistics, this is the name of the
          statistic followed by its description on a separate line

        This information is used when submitting the statistic or map with
        :meth:`submit`.

        EXAMPLES::

            sage: q = findstat([(d, randint(1, 1000)) for d in DyckWords(4)])             # optional -- internet
            sage: q.set_description("Random values on Dyck paths.\\nNot for submission.")  # optional -- internet
            sage: print(q.description())                                                  # optional -- internet
            Random values on Dyck paths.
            Not for submission.
        '''
    def name(self):
        """
        Return the name of the statistic or map.

        OUTPUT:

        A string.  For statistics, this is just the first line of the
        description.

        EXAMPLES::

            sage: findstat(51).name()                                           # optional -- internet
            'The size of the left subtree of a binary tree.'
        """
    def references(self):
        """
        Return the references associated with the statistic or map.

        OUTPUT:

        An instance of :class:`sage.databases.oeis.FancyTuple`, each
        item corresponds to a reference.

        EXAMPLES::

            sage: findstat(41).references()                                     # optional -- internet
            0: [1]  de Médicis, A., Viennot, X. G., Moments des $q$-polynômes de Laguerre et la bijection de Foata-Zeilberger [[MathSciNet:1288802]]
            1: [2]  Simion, R., Stanton, D., Octabasic Laguerre polynomials and permutation statistics [[MathSciNet:1418763]]
        """
    def references_raw(self):
        """
        Return the unrendered references associated with the statistic or map.

        EXAMPLES::

            sage: print(findstat(41).references_raw())                          # optional -- internet
            [1]  [[MathSciNet:1288802]]
            [2]  [[MathSciNet:1418763]]
        """
    def set_references_raw(self, value) -> None:
        '''
        Set the references associated with the statistic or map.

        INPUT:

        - ``value`` -- string; each reference should be on a single line, and
          consist of one or more links to the same item

        FindStat will automatically resolve the links, if possible.
        A complete list of supported services can be found at
        <https://findstat.org/NewStatistic>.

        This information is used when submitting the statistic with
        :meth:`submit`.

        EXAMPLES::

            sage: q = findstat([(d, randint(1, 1000)) for d in DyckWords(4)])   # optional -- internet
            sage: q.set_references_raw("[[arXiv:1102.4226]]\\n[[oeis:A000001]]") # optional -- internet
            sage: q.references()                                                # optional -- internet
            0: [[arXiv:1102.4226]]
            1: [[oeis:A000001]]
        '''
    def sage_code(self):
        """
        Return the Sage code associated with the statistic or map.

        OUTPUT: an empty string or a string of the form::

            def statistic(x):
                ...

        or::

            def mapping(x):
                ...

        EXAMPLES::

            sage: print(findstat(51).sage_code())                               # optional -- internet
            def statistic(T):
                return T[0].node_number()
        """
    def set_sage_code(self, value) -> None:
        '''
        Set the code associated with the statistic or map.

        INPUT:

        - ``value`` -- string; SageMath code producing the values of the
          statistic or map

        Contributors are encouraged to submit code for statistics
        using :meth:`FindStatStatistic.set_code`.  Modifying the
        "verified" SageMath code using this method is restricted to
        members of the FindStatCrew, for all other contributors this
        method has no effect.

        EXAMPLES::

            sage: q = findstat([(d, randint(1,1000)) for d in DyckWords(4)])              # optional -- internet
            sage: q.set_sage_code("def statistic(x):\\n    return randint(1, 1000)")        # optional -- internet
            sage: print(q.sage_code())                                                    # optional -- internet
            def statistic(x):
                return randint(1,1000)
        '''

class FindStatCombinatorialStatistic(SageObject):
    """
    A class providing methods to retrieve the first terms of a statistic.

    This class provides methods applicable to instances of
    :class:`FindStatStatistic`, :class:`FindStatCompoundStatistic`
    and :class:`FindStatStatisticQuery`.
    """
    def __init__(self) -> None:
        """
        Initialize the combinatorial statistic.

        TESTS::

            sage: from sage.databases.findstat import FindStatCombinatorialStatistic
            sage: FindStatCombinatorialStatistic()
            <sage.databases.findstat.FindStatCombinatorialStatistic object at 0x...>
        """
    def first_terms(self):
        """
        Return the first terms of the (compound) statistic as a
        dictionary.

        OUTPUT:

        A dictionary from Sage objects representing an element of the
        appropriate collection to integers.

        This method is overridden in :class:`FindStatStatisticQuery`.

        EXAMPLES::

            sage: findstat(41).first_terms()[PerfectMatching([(1,6),(2,5),(3,4)])]        # optional -- internet
            3
        """
    def first_terms_str(self, max_values=...):
        '''
        Return the first terms of the statistic in the format needed
        for a FindStat query.

        OUTPUT:

        A string, where each line is of the form ``object => value``,
        where ``object`` is the string representation of an element
        of the appropriate collection as used by FindStat and value
        is an integer.

        EXAMPLES::

            sage: print(findstat(41).first_terms_str(max_values=4))             # optional -- internet
            [(1,2)] => 0
            [(1,2),(3,4)] => 0
            [(1,3),(2,4)] => 0
            [(1,4),(2,3)] => 1

        TESTS:

        Check that no more terms than asked for are computed::

            sage: st = cached_function(lambda d: randint(1,1000))
            sage: s = findstat("Dyck paths", st, max_values=100, depth=0)       # optional -- internet
            sage: len(st.cache)                                                 # optional -- internet
            100
            sage: _ = s.first_terms_str(max_values=100)                         # optional -- internet
            sage: len(st.cache)                                                 # optional -- internet
            100
        '''
    def generating_functions(self, style: str = 'polynomial', max_values=...):
        '''
        Return the generating functions of the statistic as a dictionary.

        The keys of this dictionary are the levels for which the
        generating function of the statistic can be computed from
        the known data.  Each value represents a generating function
        for one level, as a polynomial, as a dictionary, or as a list
        of coefficients.

        INPUT:

        - ``style`` -- string (default: ``\'polynomial\'``); can be
          ``\'polynomial\'``, ``\'dictionary\'``, or ``\'list\'``

        OUTPUT:

        - if ``style`` is ``\'polynomial\'``, the generating function is
          returned as a polynomial

        - if ``style`` is ``\'dictionary\'``, the generating function is
          returned as a dictionary representing the monomials of the
          generating function

        - if ``style`` is ``\'list\'``, the generating function is
          returned as a list of coefficients of the generating
          function.  In this case, leading and trailing zeros are
          omitted.

        EXAMPLES::

            sage: st = findstat(41)                                             # optional -- internet
            sage: st.generating_functions()                                     # optional -- internet
            {2: 1,
             4: q + 2,
             6: q^3 + 3*q^2 + 6*q + 5,
             8: q^6 + 4*q^5 + 10*q^4 + 20*q^3 + 28*q^2 + 28*q + 14}

            sage: st.generating_functions(style=\'dictionary\')                   # optional -- internet
            {2: {0: 1},
             4: {0: 2, 1: 1},
             6: {0: 5, 1: 6, 2: 3, 3: 1},
             8: {0: 14, 1: 28, 2: 28, 3: 20, 4: 10, 5: 4, 6: 1}}

            sage: st.generating_functions(style=\'list\')                         # optional -- internet
            {2: [1], 4: [2, 1], 6: [5, 6, 3, 1], 8: [14, 28, 28, 20, 10, 4, 1]}

        TESTS::

            sage: st = findstat(41)                                             # optional -- internet
            sage: st.generating_functions(max_values=19)                        # optional -- internet
            {2: 1, 4: q + 2, 6: q^3 + 3*q^2 + 6*q + 5}

            sage: st = findstat("graphs", lambda G: G.size(), max_values=100)   # optional -- internet
            sage: st.generating_functions(max_values=18)                        # optional -- internet
            {1: 1,
             2: q + 1,
             3: q^3 + q^2 + q + 1,
             4: q^6 + q^5 + 2*q^4 + 3*q^3 + 2*q^2 + q + 1}
            sage: st.generating_functions(max_values=1252)                      # optional -- internet
            {1: 1,
             2: q + 1,
             3: q^3 + q^2 + q + 1,
             4: q^6 + q^5 + 2*q^4 + 3*q^3 + 2*q^2 + q + 1,
             5: q^10 + q^9 + 2*q^8 + 4*q^7 + 6*q^6 + 6*q^5 + 6*q^4 + 4*q^3 + 2*q^2 + q + 1,
             6: q^15 + q^14 + 2*q^13 + 5*q^12 + 9*q^11 + 15*q^10 + 21*q^9 + 24*q^8 + 24*q^7 + 21*q^6 + 15*q^5 + 9*q^4 + 5*q^3 + 2*q^2 + q + 1,
             7: q^21 + q^20 + 2*q^19 + 5*q^18 + 10*q^17 + 21*q^16 + 41*q^15 + 65*q^14 + 97*q^13 + 131*q^12 + 148*q^11 + 148*q^10 + 131*q^9 + 97*q^8 + 65*q^7 + 41*q^6 + 21*q^5 + 10*q^4 + 5*q^3 + 2*q^2 + q + 1}
        '''
    def oeis_search(self, search_size: int = 32, verbose: bool = True):
        '''
        Search the OEIS for the generating function of the statistic.

        INPUT:

        - ``search_size`` -- (default: 32) the number of integers in the
          sequence. If this is chosen too big, the OEIS result may be
          corrupted.

        - ``verbose`` -- boolean (default: ``True``); if ``True``, some
          information about the search are printed

        OUTPUT: a tuple of OEIS sequences, see
        :meth:`sage.databases.oeis.OEIS.find_by_description` for more
        information

        EXAMPLES::

            sage: st = findstat(41)                                             # optional -- internet

            sage: st.oeis_search()                                              # optional -- internet
            Searching the OEIS for "1  2,1  5,6,3,1  14,28,28,20,10,4,1"
            0: A067311: Triangle read by rows: T(n,k) gives number of ways of arranging n chords on a circle with k simple intersections ...
        '''

class FindStatStatistic(Element, FindStatFunction, FindStatCombinatorialStatistic, metaclass=InheritComparisonClasscallMetaclass):
    """
    A FindStat statistic.

    :class:`FindStatStatistic` is a class representing a
    combinatorial statistic available in the FindStat database.

    This class provides methods to inspect and update various
    properties of these statistics.

    EXAMPLES::

        sage: from sage.databases.findstat import FindStatStatistic
        sage: FindStatStatistic(41)                                             # optional -- internet
        St000041: The number of nestings of a perfect matching.

    .. SEEALSO::

        :class:`FindStatStatistics`
    """
    @staticmethod
    def __classcall_private__(cls, entry):
        '''
        Retrieve a statistic from the database.

        TESTS::

            sage: from sage.databases.findstat import FindStatStatistic
            sage: FindStatStatistic("abcdefgh")                                 # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: the value \'abcdefgh\' is not a valid FindStat statistic identifier
        '''
    def __init__(self, parent, id) -> None:
        """
        Initialize a FindStat statistic from an identifier.

        INPUT:

        - ``parent`` -- :class:`FindStatStatistics`

        - ``id`` -- the (padded) FindStat identifier of the statistic

        EXAMPLES::

            sage: findstat(41)                                                  # optional -- internet, indirect doctest
            St000041: The number of nestings of a perfect matching.
        """
    def __call__(self, elt):
        '''
        Apply the statistic to a given element.

        EXAMPLES::

            sage: s = lambda g: g.diameter() if g.is_connected() else None
            sage: q = findstat("graphs", s, max_values=100)                     # optional -- internet
            sage: q(graphs.PetersenGraph().copy(immutable=True))                # optional -- internet
            2
        '''
    def __reduce__(self):
        """
        Return a function and its arguments needed to create the
        statistic.

        TESTS::

            sage: from sage.databases.findstat import FindStatStatistic
            sage: c = FindStatStatistic(41)                                     # optional -- internet
            sage: loads(dumps(c)) == c                                          # optional -- internet
            True
        """
    def set_first_terms(self, values) -> None:
        """
        Update the first terms of the statistic.

        INPUT:

        - ``values`` -- list of pairs of the form ``(object, value)`` where
          ``object`` is a Sage object representing an element of the
          appropriate collection and ``value`` is an integer

        This information is used when submitting the statistic with
        :meth:`submit`.

        .. WARNING::

            This method cannot check whether the given values are
            actually correct.  Moreover, it does not even perform any
            sanity checks.

        TESTS::

            sage: s = findstat(41)                                              # optional -- internet
            sage: l = [([(1,2)], 1), ([(1,2),(3,4)], 7), ([(1,3),(2,4)], 8), ([(1,4),(2,3)], 3)]
            sage: s.set_first_terms(l)                                          # optional -- internet
            sage: print(s.first_terms_str())                                    # optional -- internet
            [(1, 2)] => 1
            [(1, 2), (3, 4)] => 7
            [(1, 3), (2, 4)] => 8
            [(1, 4), (2, 3)] => 3
            sage: s.reset()                                                     # optional -- internet
        """
    def code(self):
        """
        Return the code associated with the statistic or map.

        OUTPUT: string

        Contributors are encouraged to submit Sage code in the form::

            def statistic(x):
                ...

        but the string may also contain code for other computer
        algebra systems.

        EXAMPLES::

            sage: print(findstat(41).code())                                    # optional -- internet
            def statistic(x):
                return len(x.nestings())

            sage: print(findstat(118).code())                                   # optional -- internet
            (* in Mathematica *)
            tree = {{{{}, {}}, {{}, {}}}, {{{}, {}}, {{}, {}}}};
            Count[tree, {{___}, {{___}, {{___}, {___}}}}, {0, Infinity}]
        """
    def set_code(self, value) -> None:
        '''
        Set the code associated with the statistic.

        INPUT:

        - ``value`` -- string; code producing the values of the statistic

        Contributors are encouraged to submit SageMath code in the form::

            def statistic(x):
                ...

        However, code for any other platform is accepted also.

        This information is used when submitting the statistic with
        :meth:`submit`.

        EXAMPLES::

            sage: q = findstat([(d, randint(1,1000)) for d in DyckWords(4)])    # optional -- internet
            sage: q.set_code("def statistic(x):\\n    return randint(1,1000)")   # optional -- internet
            sage: print(q.code())                                               # optional -- internet
            def statistic(x):
                return randint(1,1000)
        '''
    def browse(self) -> None:
        """
        Open the FindStat web page of the statistic in a browser.

        EXAMPLES::

            sage: findstat(41).browse()                                         # optional -- webbrowser
        """
    def submit(self, max_values=...) -> None:
        '''
        Open the FindStat web page for editing the statistic or
        submitting a new statistic in a browser.

        TESTS::

            sage: s = findstat([(d, randint(1,1000)) for d in DyckWords(4)])    # optional -- internet
            sage: s.set_description(u"Möbius")                                  # optional -- internet
            sage: s.submit()                                                    # optional -- webbrowser
        '''
    edit = submit
    def __hash__(self):
        """
        Return a hash value for the statistic.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMaps
            sage: list(FindStatMaps(domain=1, codomain=10))                     # optional -- internet
            [Mp00061: to increasing tree, Mp00072: binary search tree: left to right]
        """
    def info(self) -> None:
        '''
        Print a detailed description of the statistic.

        EXAMPLES::

            sage: findstat("St000042").info()                                   # optional -- internet
                St000042: The number of crossings of a perfect matching.
        '''

class FindStatStatistics(UniqueRepresentation, Parent):
    '''
    The class of FindStat statistics.

    The elements of this class are combinatorial statistics currently
    in FindStat.

    EXAMPLES:

    We can print a list of the first few statistics currently in
    FindStat in a given domain::

        sage: from sage.databases.findstat import FindStatStatistics
        sage: for st, _ in zip(FindStatStatistics("Perfect Matchings"), range(3)):        # optional -- internet
        ....:     print("    " + st.name())
        The number of nestings of a perfect matching.
        The number of crossings of a perfect matching.
        The number of crossings plus two-nestings of a perfect matching.
    '''
    def __init__(self, domain=None) -> None:
        """
        TESTS::

            sage: from sage.databases.findstat import FindStatStatistics
            sage: M = FindStatStatistics()                                      # optional -- internet
            sage: TestSuite(M).run()                                            # optional -- internet
        """
    def __iter__(self):
        '''
        Return an iterator over all FindStat statistics.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatStatistics
            sage: next(iter(FindStatStatistics("Perfect Matchings")))           # optional -- internet
            St000041: The number of nestings of a perfect matching.
        '''
    Element = FindStatStatistic

class FindStatStatisticQuery(FindStatStatistic):
    """
    A class representing a query for FindStat (compound) statistics.
    """
    def __init__(self, data=None, values_of=None, distribution_of=None, domain=None, known_terms=None, function=None, depth=..., debug: bool = False) -> None:
        """
        Initialize a query for FindStat (compound) statistics.

        INPUT:

        - ``data`` -- (optional), a list of pairs ``(objects,
          values)``, where ``objects`` and ``values`` are all lists
          of the same length, the former are elements in the FindStat
          collection, the latter are integers

        - ``known_terms`` -- (optional), a lazy list in the same format
          as ``data``, which agrees with ``data``, and may be used
          for submission

        - ``values_of`` -- (optional), anything accepted by
          :class:`FindStatCompoundStatistic`

        - ``distribution_of`` -- (optional), anything accepted by
          :class:`FindStatCompoundStatistic`

        - ``domain`` -- (optional), anything accepted by
          :class:`FindStatCollection`

        - ``depth`` -- (optional), the number of maps to apply before
          applying the statistic


        Only one of ``data``, ``values_of`` and ``distribution_of``
        may be provided.  The parameter ``domain`` must be provided
        if and only if ``data`` is provided, or ``values_of`` or
        ``distribution_of`` are given as a function.

        The parameter ``known_terms`` is only allowed, if ``data`` is
        provided.  It defaults to ``data``.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatStatisticQuery
            sage: data = [[[m], [m.number_of_nestings()]] for n in range(5) for m in PerfectMatchings(2*n)]
            sage: FindStatStatisticQuery(domain=12, data=data, depth=1)         # optional -- internet
            0: St000041 (quality [99, 100])
            1: St000041oMp00113 (quality [99, 100])
            2: St000042oMp00116 (quality [99, 100])
            ...
        """
    def first_terms(self, max_values=...):
        """
        Return the pairs of the known terms which contain singletons as a dictionary.

        EXAMPLES::

             sage: PM = PerfectMatchings
             sage: l = [(PM(2*n), [m.number_of_nestings() for m in PM(2*n)]) for n in range(5)]
             sage: r = findstat(l, depth=0); r                                  # optional -- internet
             0: St000041 (quality [99, 100])
             1: St000042 (quality [99, 100])
             sage: r.first_terms()                                              # optional -- internet
             {[]: 0, [(1, 2)]: 0}
        """
    def __getitem__(self, i):
        """
        Return the `t`-th result in the query.

        EXAMPLES::

            sage: PM = PerfectMatchings
            sage: data = [(m, m.number_of_nestings()) for n in range(6) for m in PM(2*n)]
            sage: r = findstat(data, depth=1)                                   # optional -- internet
            sage: r[1]                                                          # optional -- internet
            St000041 (quality [20, 100])
        """
    def __len__(self) -> int:
        """
        Return the number of results in the query.

        EXAMPLES::

            sage: r = findstat(Permutations, lambda pi: pi.saliances()[0], depth=1)       # optional -- internet
            sage: len(r) > 4                                                              # optional -- internet
            True
        """

class FindStatCompoundStatistic(Element, FindStatCombinatorialStatistic):
    def __init__(self, id, domain=None, check: bool = True) -> None:
        '''
        Initialize a compound statistic.

        A compound statistic is a sequence of maps followed by a statistic.

        INPUT:

        - ``id`` -- a padded identifier

        - ``domain`` -- (optional), the domain of the compound statistic

        - ``check`` -- whether to check that domains and codomains fit

        If the domain is given and ``check`` is ``False``, it is not
        fetched from FindStat.

        TESTS::

            sage: findstat("St000041oMp00127")                                  # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: the statistic St000041: The number of nestings of a perfect matching. cannot be composed with the map Mp00127
        '''
    def domain(self):
        '''
        Return the domain of the compound statistic.

        EXAMPLES::

            sage: findstat("St000042oMp00116").domain()                         # optional -- internet
            Cc0012: Perfect matchings
        '''
    def __call__(self, elt):
        '''
        Apply the compound statistic to the given element.

        Note that this is only possible if execution of code is
        enabled, by setting the attribute ``_function`` of each map
        and the statistic to ``True``.

        EXAMPLES::

            sage: findstat("St000042oMp00116")(PerfectMatching([(1,2)]))        # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: execution of verified code provided by FindStat is not enabled for Mp00116: Kasraoui-Zeng
        '''
    def id_str(self):
        '''
        Return the padded identifier of the compound statistic.

        EXAMPLES::

            sage: findstat("St000042oMp00116").id_str()                         # optional -- internet
            \'St000042oMp00116\'
        '''
    def statistic(self):
        '''
        Return the statistic of the compound statistic.

        EXAMPLES::

            sage: findstat("St000041oMp00116").statistic()                      # optional -- internet
            St000041: The number of nestings of a perfect matching.
        '''
    def compound_map(self):
        '''
        Return the compound map which is part of the compound statistic.

        EXAMPLES::

            sage: findstat("St000051oMp00061oMp00069").compound_map()           # optional -- internet
            Mp00061oMp00069
        '''
    def browse(self) -> None:
        '''
        Open the FindStat web page of the compound statistic in a browser.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCompoundStatistic
            sage: FindStatCompoundStatistic("St000042oMp00116").browse()        # optional -- webbrowser
        '''
    def info(self) -> None:
        '''
        Print a detailed description of the compound statistic.

        EXAMPLES::

            sage: findstat("St000042oMp00116").info()                           # optional -- internet
                Mp00116: Kasraoui-Zeng: Perfect matchings -> Perfect matchings
                St000042: The number of crossings of a perfect matching.
        '''

class FindStatMatchingStatistic(FindStatCompoundStatistic):
    def __init__(self, matching_statistic, offset, quality, domain=None) -> None:
        '''
        Initialize a FindStat statistic match.

        INPUT:

        - ``matching_statistic`` -- a compound statistic identifier

        - ``offset`` -- the offset of the values, as provided by FindStat

        - ``quality`` -- the quality of the match, as provided by FindStat

        - ``domain`` -- (optional) the domain of the compound statistic

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingStatistic
            sage: FindStatMatchingStatistic("St000042oMp00116", 1, [17, 83])    # optional -- internet
            St000042oMp00116 with offset 1 (quality [17, 83])
        '''
    def offset(self):
        '''
        Return the offset which has to be added to each value of the
        compound statistic to obtain the desired value.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingStatistic
            sage: r = FindStatMatchingStatistic("St000042oMp00116", 1, [17, 83])          # optional -- internet
            sage: r.offset()                                                    # optional -- internet
            1
        '''
    def quality(self):
        '''
        Return the quality of the match, as provided by FindStat.

        The quality of a statistic match is a pair of percentages
        `(q_a, q_d)`, where `q_a` is the percentage of ``(object,
        value)`` pairs that are in the database among those which
        were sent to FindStat, and `q_d` is the percentage of
        ``(object, value)`` pairs with distinct values in the
        database among those which were sent to FindStat.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingStatistic
            sage: r = FindStatMatchingStatistic("St000042oMp00116", 1, [17, 83])          # optional -- internet
            sage: r.quality()                                                   # optional -- internet
            [17, 83]
        '''
    def info(self) -> None:
        '''
        Print a detailed explanation of the match.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingStatistic
            sage: r = FindStatMatchingStatistic("St000042oMp00116", 1, [17, 83])          # optional -- internet
            sage: r.info()                                                      # optional -- internet
            after adding 1 to every value
            and applying
                Mp00116: Kasraoui-Zeng: Perfect matchings -> Perfect matchings
            to the objects (see `.compound_map()` for details)
            <BLANKLINE>
            your input matches
                St000042: The number of crossings of a perfect matching.
            <BLANKLINE>
            among the values you sent, 17 percent are actually in the database,
            among the distinct values you sent, 83 percent are actually in the database

            sage: r = FindStatMatchingStatistic("St000042", 1, [17, 83])        # optional -- internet
            sage: r.info()                                                      # optional -- internet
            after adding 1 to every value
            <BLANKLINE>
            your input matches
                St000042: The number of crossings of a perfect matching.
            <BLANKLINE>
            among the values you sent, 17 percent are actually in the database,
            among the distinct values you sent, 83 percent are actually in the database
        '''

class FindStatCombinatorialMap(SageObject):
    """
    A class serving as common ancestor of :class:`FindStatStatistic`
    and :class:`FindStatCompoundStatistic`.
    """

class FindStatMap(Element, FindStatFunction, FindStatCombinatorialMap, metaclass=InheritComparisonClasscallMetaclass):
    """
    A FindStat map.

    :class:`FindStatMap` is a class representing a combinatorial
    map available in the FindStat database.

    This class provides methods to inspect various properties of
    these maps, in particular :meth:`code`.

    EXAMPLES::

        sage: from sage.databases.findstat import FindStatMap
        sage: FindStatMap(116)                                                  # optional -- internet
        Mp00116: Kasraoui-Zeng

    .. SEEALSO::

        :class:`FindStatMaps`
    """
    @staticmethod
    def __classcall_private__(cls, entry):
        '''
        Retrieve a map from the database.

        TESTS::

            sage: from sage.databases.findstat import FindStatMap
            sage: FindStatMap("abcdefgh")                                       # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: the value \'abcdefgh\' is not a valid FindStat map identifier
        '''
    def __init__(self, parent, id) -> None:
        """
        Initialize the map.

        This should only be called in
        :meth:`FindStatMaps()._element_constructor_` via
        :meth:`FindStatMaps().element_class`.

        INPUT:

        - ``parent`` -- :class:`FindStatMaps`

        - ``id`` -- the (padded) FindStat identifier of the statistic

        TESTS::

            sage: from sage.databases.findstat import FindStatMap
            sage: FindStatMap(116).parent()                                     # optional -- internet
            Set of combinatorial maps used by FindStat
        """
    def __reduce__(self):
        """
        Return a function and its arguments needed to create the map.

        TESTS::

            sage: from sage.databases.findstat import FindStatMap
            sage: c = FindStatMap(116)                                          # optional -- internet
            sage: loads(dumps(c)) == c                                          # optional -- internet
            True
        """
    def browse(self) -> None:
        """
        Open the FindStat web page of the map in a browser.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMap
            sage: FindStatMap(116).browse()                                     # optional -- webbrowser
        """
    def submit(self) -> None:
        '''
        Open the FindStat web page for editing the map in a browser.

        TESTS::

            sage: s = findmap(62)                                               # optional -- internet
            sage: s.set_name(u"Möbius")                                         # optional -- internet
            sage: s.submit()                                                    # optional -- webbrowser
            sage: s.reset()                                                     # optional -- internet
        '''
    edit = submit
    def __hash__(self):
        """
        Return a hash value for the map.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMaps
            sage: sorted(list(FindStatMaps(domain=1, codomain=10)))             # optional -- internet, indirect doctest
            [Mp00061: to increasing tree, Mp00072: binary search tree: left to right]
        """
    def codomain(self):
        """
        Return the FindStat collection which is the codomain of the map.

        OUTPUT: the codomain of the map as a :class:`FindStatCollection`

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMap               # optional -- internet
            sage: FindStatMap(27).codomain()                                    # optional -- internet
            Cc0002: Integer partitions
        """
    def properties_raw(self):
        """
        Return the properties of the map.

        OUTPUT: the properties as a string

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMap               # optional -- internet
            sage: FindStatMap(61).properties_raw()                              # optional -- internet
            'surjective, graded'
        """
    def set_properties_raw(self, value) -> None:
        """
        Set the properties of the map.

        EXAMPLES::

            sage: # optional - internet
            sage: from sage.databases.findstat import FindStatMap
            sage: FindStatMap(61).set_properties_raw('surjective')
            sage: FindStatMap(61).properties_raw()
            'surjective'
            sage: FindStatMap(61)
            Mp00061(modified): to increasing tree
            sage: FindStatMap(61).reset()
            sage: FindStatMap(61)
            Mp00061: to increasing tree
        """
    def set_name(self, value) -> None:
        '''
        Set the name of the map.

        INPUT:

        - ``value`` -- string; the new name of the map

        This information is used when submitting the map with
        :meth:`submit`.

        TESTS::

            sage: s = findmap(62)                                               # optional -- internet
            sage: s.set_name(u"Möbius"); s                                      # optional -- internet
            Mp00062(modified): Möbius
            sage: s.reset(); s                                                  # optional -- internet
            Mp00062: Lehmer-code to major-code bijection
        '''
    def info(self) -> None:
        '''
        Print a detailed description of the map.

        EXAMPLES::

            sage: findmap("Mp00116").info()                                     # optional -- internet
                Mp00116: Kasraoui-Zeng: Perfect matchings -> Perfect matchings
        '''

class FindStatMaps(UniqueRepresentation, Parent):
    '''
    The class of FindStat maps.

    The elements of this class are combinatorial maps currently in
    FindStat.

    EXAMPLES:

    We can print a sample map for each domain and codomain::

        sage: from sage.databases.findstat import FindStatCollections, FindStatMaps
        sage: ccs = sorted(FindStatCollections())[:3]                           # optional -- internet
        sage: for cc_dom in ccs:                                                # optional -- internet
        ....:     for cc_codom in ccs:
        ....:         print(cc_dom.name(style=\'plural\') + " -> " + cc_codom.name(style=\'plural\'))
        ....:         try:
        ....:             print("    " + next(iter(FindStatMaps(cc_dom, cc_codom))).name())
        ....:         except StopIteration:
        ....:             pass
        Permutations -> Permutations
            Lehmer-code to major-code bijection
        Permutations -> Integer partitions
            Robinson-Schensted tableau shape
        Permutations -> Dyck paths
            left-to-right-maxima to Dyck path
        Integer partitions -> Permutations
        Integer partitions -> Integer partitions
            conjugate
        Integer partitions -> Dyck paths
            to Dyck path
        Dyck paths -> Permutations
            to non-crossing permutation
        Dyck paths -> Integer partitions
            to partition
        Dyck paths -> Dyck paths
            reverse
    '''
    def __init__(self, domain=None, codomain=None) -> None:
        """
        TESTS::

            sage: from sage.databases.findstat import FindStatMaps
            sage: M = FindStatMaps()                                            # optional -- internet
            sage: TestSuite(M).run()                                            # optional -- internet
        """
    def __iter__(self):
        """
        Return an iterator over all FindStat maps.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMaps
            sage: next(iter(FindStatMaps(domain=1, codomain=10)))               # optional -- internet
            Mp00061: to increasing tree
        """
    Element = FindStatMap

class FindStatMapQuery(FindStatMap):
    """
    A class representing a query for FindStat (compound) maps.
    """
    def __init__(self, data=None, values_of=None, distribution_of=None, domain=None, codomain=None, known_terms=None, function=None, depth=..., debug: bool = False) -> None:
        """
        Initialize a query for FindStat (compound) maps.

        INPUT:

        - ``data`` -- (optional), a list of pairs ``(objects,
          values)``, where ``objects`` and ``values`` are all lists
          of the same length, the former are elements in the domain
          and the latter in the codomain

        - ``known_terms`` -- (optional), a lazy list in the same format
          as ``data``, which agrees with ``data``, and may be used
          for submission

        - ``values_of`` -- (optional), anything accepted by
          :class:`FindStatCompoundStatistic`

        - ``distribution_of`` -- (optional), anything accepted by
          :class:`FindStatCompoundStatistic`

        - ``domain``, ``codomain`` -- (optional), anything accepted by
          :class:`FindStatCollection`

        - ``depth`` -- (optional), the number of maps to apply before
          applying the statistic

        - ``function`` -- (optional), a callable producing the terms

        Only one of ``data``, ``values_of`` and ``distribution_of``
        may be provided.  The parameter ``domain`` must be provided
        if and only if ``data`` is provided, or ``values_of`` or
        ``distribution_of`` are given as a function.

        The parameter ``known_terms`` is only allowed, if ``data`` is
        provided.  It defaults to ``data``.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMapQuery
            sage: data = [[[pi], [pi.complement().increasing_tree_shape()]] for pi in Permutations(4)]
            sage: FindStatMapQuery(domain=1, codomain=10, data=data)            # optional -- internet
            0: Mp00061oMp00069 (quality [100])
        """
    def __getitem__(self, i):
        """
        Return the `i`-th result in the query.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMapQuery
            sage: data = [[[pi],[pi.complement().increasing_tree_shape()]] for pi in Permutations(4)]
            sage: r = FindStatMapQuery(domain=1, codomain=10, data=data)        # optional -- internet
            sage: r[0]                                                          # optional -- internet
            Mp00061oMp00069 (quality [100])
        """
    def __len__(self) -> int:
        '''
        Return the number of results in the query.

        EXAMPLES::

            sage: r = findmap("Permutations", lambda pi: pi.descents_composition())       # optional -- internet
            sage: len(r) > 0                                                              # optional -- internet
            True
        '''

class FindStatCompoundMap(Element, FindStatCombinatorialMap):
    def __init__(self, id, domain=None, codomain=None, check: bool = True) -> None:
        '''
        Initialize a compound statistic.

        INPUT:

        - ``id`` -- a padded identifier

        - ``domain`` -- (optional), the domain of the compound map

        - ``codomain`` -- (optional), the codomain of the compound map

        - ``check`` -- whether to check that domains and codomains fit

        If domain and codomain are given and ``check`` is ``False``,
        they are not fetched from FindStat.

        If ``id`` is the empty string, ``domain`` must be provided,
        and the identity map on this collection is returned.

        TESTS::

            sage: findmap("Mp00146oMp00127").domain()                           # optional -- internet
            Cc0001: Permutations

            sage: findmap("Mp00146oMp00127").codomain()                         # optional -- internet
            Cc0012: Perfect matchings

            sage: findmap("Mp00127oMp00146")                                    # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: the sequence of maps [Mp00146: to tunnel matching, Mp00127: left-to-right-maxima to Dyck path] cannot be composed
        '''
    def domain(self):
        '''
        Return the domain of the compound map.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127").domain()                           # optional -- internet
            Cc0001: Permutations
        '''
    def codomain(self):
        '''
        Return the codomain of the compound map.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127").codomain()                         # optional -- internet
            Cc0005: Dyck paths
        '''
    def __call__(self, elt):
        '''
        Apply the compound map to the given element.

        Note that this is only possible if execution of code is
        enabled, by setting the attribute ``_function`` of each map
        to ``True``.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127")(Permutation([1,3,2]))              # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: execution of verified code provided by FindStat is not enabled for Mp00127: left-to-right-maxima to Dyck path
        '''
    def __getitem__(self, i):
        '''
        Return the `i`-th map in the compound map.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127")[1]                                 # optional -- internet
            Mp00099: bounce path
        '''
    def id_str(self):
        '''
        Return the padded identifier of the compound map.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127").id_str()                           # optional -- internet
            \'Mp00099oMp00127\'
        '''
    def maps(self):
        '''
        Return the maps occurring in the compound map as a list.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127").maps()                             # optional -- internet
            [Mp00127: left-to-right-maxima to Dyck path, Mp00099: bounce path]
        '''
    def __len__(self) -> int:
        '''
        Return the number of maps occurring in the compound map.

        .. WARNING::

            Do not confuse this with the number of results in a query.

        EXAMPLES::

            sage: len(findmap("Mp00099oMp00127"))                               # optional -- internet
            2
        '''
    def browse(self) -> None:
        """
        Open the FindStat web page of the compound map in a browser.

        EXAMPLES::

            sage: findmap(62).browse()                                          # optional -- webbrowser
        """
    def info(self) -> None:
        '''
        Print a detailed explanation of the compound map.

        EXAMPLES::

            sage: findmap("Mp00099oMp00127").info()                             # optional -- internet
                Mp00127: left-to-right-maxima to Dyck path: Permutations -> Dyck paths
                Mp00099: bounce path: Dyck paths -> Dyck paths
        '''

class FindStatMatchingMap(FindStatCompoundMap):
    def __init__(self, matching_map, quality, domain=None, codomain=None) -> None:
        '''
        Initialize a FindStat map match.

        INPUT:

        - ``matching_map`` -- a compound map identifier

        - ``quality`` -- the quality of the match, as provided by FindStat

        - ``domain`` -- (optional) the domain of the compound map

        - ``codomain`` -- (optional), the codomain of the compound map

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingMap
            sage: FindStatMatchingMap("Mp00099oMp00127", [83])                  # optional -- internet
            Mp00099oMp00127 (quality [83])
        '''
    def quality(self):
        '''
        Return the quality of the match, as provided by FindStat.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingMap
            sage: FindStatMatchingMap("Mp00099oMp00127", [83]).quality()        # optional -- internet
            [83]
        '''
    def info(self) -> None:
        '''
        Print a detailed explanation of the match.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatMatchingMap
            sage: FindStatMatchingMap("Mp00099oMp00127", [83]).info()           # optional -- internet
            your input matches
                Mp00127: left-to-right-maxima to Dyck path: Permutations -> Dyck paths
                Mp00099: bounce path: Dyck paths -> Dyck paths
            <BLANKLINE>
            among the values you sent, 83 percent are actually in the database
        '''

class FindStatCollection(Element, metaclass=InheritComparisonClasscallMetaclass):
    '''
    A FindStat collection.

    :class:`FindStatCollection` is a class representing a
    combinatorial collection available in the FindStat database.

    Its main use is to allow easy specification of the combinatorial
    collection when using :class:`findstat<FindStat>`.  It also
    provides methods to quickly access its FindStat web page
    (:meth:`browse`), check whether a particular element is actually
    in the range considered by FindStat (:meth:`in_range`), etc.

    INPUT:

    One of the following:

    - a string eg. \'Dyck paths\' or \'DyckPaths\', case-insensitive, or

    - an integer designating the FindStat id of the collection, or

    - a Sage object belonging to a collection, or

    - an iterable producing a Sage object belonging to a collection.

    EXAMPLES::

        sage: from sage.databases.findstat import FindStatCollection
        sage: FindStatCollection("Dyck paths")                                  # optional -- internet
        Cc0005: Dyck paths

        sage: FindStatCollection(5)                                             # optional -- internet
        Cc0005: Dyck paths

        sage: FindStatCollection(DyckWord([1,0,1,0]))                           # optional -- internet
        Cc0005: Dyck paths

        sage: FindStatCollection(DyckWords(2))                                  # optional -- internet
        a subset of Cc0005: Dyck paths

        sage: FindStatCollection(DyckWords)                                     # optional -- internet
        Cc0005: Dyck paths

    .. SEEALSO::

        :class:`FindStatCollections`
    '''
    @staticmethod
    def __classcall_private__(cls, entry):
        """
        Retrieve a collection from the database.

        TESTS::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection(0)                                         # optional -- internet
            Traceback (most recent call last):
            ...
            ValueError: could not find FindStat collection for 0
        """
    def __init__(self, parent, id, data, sageconstructor_overridden) -> None:
        """
        Initialize the collection.

        This should only be called in
        :meth:`FindStatCollections()._element_constructor_` via
        :meth:`FindStatCollections().element_class`.

        INPUT:

        - ``parent`` -- :class:`FindStatCollections`

        - ``id`` -- the (padded) FindStat identifier of the collection

        - ``data`` -- dictionary containing the properties of the
          collection, such as its name, the corresponding class in
          sage, and so on.

        - ``sageconstructor_overridden`` -- either ``None`` or an
          iterable which yields a subset of the elements of the
          collection.

        TESTS::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection(5).parent()                                # optional -- internet
            Set of combinatorial collections used by FindStat
        """
    def __reduce__(self):
        '''
        Return a function and its arguments needed to create the
        collection.

        TESTS::

            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("Permutations")                        # optional -- internet
            sage: loads(dumps(c)) == c                                          # optional -- internet
            True
        '''
    def __hash__(self):
        """
        Return a hash value for the collection.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollections
            sage: set(FindStatCollections())           # optional -- internet
            {Cc0001: Permutations,
             Cc0002: Integer partitions,
             ...
        """
    def is_supported(self):
        """
        Check whether the collection is fully supported by the interface.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection(1).is_supported()                          # optional -- internet
            True

            sage: FindStatCollection(24).is_supported()                         # optional -- internet, random
            False
        """
    def elements_on_level(self, level):
        '''
        Return an iterable over the elements on the given level.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection("Perfect Matchings").elements_on_level(4)  # optional -- internet
            Perfect matchings of {1, 2, 3, 4}
        '''
    def element_level(self, element):
        '''
        Return the level of an element.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: cc = FindStatCollection("Perfect Matchings")                  # optional -- internet
            sage: cc.element_level(PerfectMatching([[1,2],[3,4],[5,6]]))        # optional -- internet
            6
        '''
    def is_element(self, element):
        '''
        Return whether the element belongs to the collection.

        If the collection is not yet supported, return whether element is a string.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: cc = FindStatCollection("Perfect Matchings")                  # optional -- internet
            sage: cc.is_element(PerfectMatching([[1,2],[3,4],[5,6]]))           # optional -- internet
            True

            sage: cc.is_element(SetPartition([[1,2],[3,4],[5,6]]))              # optional -- internet
            False
        '''
    def levels_with_sizes(self):
        '''
        Return a dictionary from levels to level sizes.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: cc = FindStatCollection("Perfect Matchings")                  # optional -- internet
            sage: cc.levels_with_sizes()                                        # optional -- internet
            {2: 1, 4: 3, 6: 15, 8: 105, 10: 945}
        '''
    def in_range(self, element):
        '''
        Check whether an element of the collection is in FindStat\'s precomputed range.

        INPUT:

        - ``element`` -- a Sage object that belongs to the collection

        OUTPUT: ``True``, if ``element`` is used by the FindStat search
        engine, and ``False`` if it is ignored

        EXAMPLES::

            sage: # optional - internet
            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("GelfandTsetlinPatterns")
            sage: c.in_range(GelfandTsetlinPattern([[2, 1], [1]]))
            True
            sage: c.in_range(GelfandTsetlinPattern([[3, 1], [1]]))
            True
            sage: c.in_range(GelfandTsetlinPattern([[7, 1], [1]]))
            False

        TESTS::

            sage: from sage.databases.findstat import FindStatCollections
            sage: l = FindStatCollections()                                     # optional -- internet
            sage: long = [14, 20]
            sage: for c in sorted(l):                                           # optional -- internet
            ....:     if c.id() not in long and c.is_supported():
            ....:         f = c.first_terms(lambda x: 1)
            ....:         print("{} {} {}".format(c, len(list(f)), all(c.in_range(e) for e, _ in f)))
            Cc0001: Permutations 5913 True
            Cc0002: Integer partitions 1211 True
            Cc0005: Dyck paths 2055 True
            Cc0006: Integer compositions 1023 True
            Cc0007: Standard tableaux 1115 True
            Cc0009: Set partitions 1155 True
            Cc0010: Binary trees 2055 True
            Cc0012: Perfect matchings 1069 True
            Cc0013: Cores 100 True
            Cc0017: Alternating sign matrices 7917 True
            Cc0018: Gelfand-Tsetlin patterns 1409 True
            Cc0019: Semistandard tableaux 2374 True
            Cc0021: Ordered trees 2056 True
            Cc0022: Finite Cartan types 31 True
            Cc0023: Parking functions 18248 True
            Cc0024: Binary words 1022 True
            Cc0025: Plane partitions 1123 True
            Cc0026: Decorated permutations 2371 True
            Cc0027: Signed permutations 4282 True
            Cc0028: Skew partitions 1250 True
            Cc0029: Lattices 1378 True
            Cc0030: Ordered set partitions 5316 True
        '''
    def first_terms(self, function, level=None):
        '''
        Compute the first few terms of the given function, possibly
        restricted to a level, as a lazy list.

        INPUT:

        - ``function`` -- a callable

        - ``level`` -- (optional), the level to restrict to

        OUTPUT:

        A lazy list of pairs of the form ``(object, value)``.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("GelfandTsetlinPatterns")              # optional -- internet
            sage: c.first_terms(lambda x: 1)[:10].list()                        # optional -- internet
            [([[1, 0], [0]], 1),
             ([[1, 0], [1]], 1),
             ([[2, 0], [0]], 1),
             ([[2, 0], [1]], 1),
             ([[2, 0], [2]], 1),
             ([[1, 1], [1]], 1),
             ([[1, 0, 0], [0, 0], [0]], 1),
             ([[1, 0, 0], [1, 0], [0]], 1),
             ([[1, 0, 0], [1, 0], [1]], 1),
             ([[3, 0], [0]], 1)]
        '''
    def id(self):
        '''
        Return the FindStat identifier of the collection.

        OUTPUT: the FindStat identifier of the collection as an integer

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("GelfandTsetlinPatterns")              # optional -- internet
            sage: c.id()                                                        # optional -- internet
            18
        '''
    def id_str(self):
        '''
        Return the FindStat identifier of the collection.

        OUTPUT: the FindStat identifier of the collection as a string

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("GelfandTsetlinPatterns")              # optional -- internet
            sage: c.id_str()                                                    # optional -- internet
            \'Cc0018\'
        '''
    def browse(self) -> None:
        '''
        Open the FindStat web page of the collection in a browser.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection("Permutations").browse()                   # optional -- webbrowser
        '''
    def to_string(self):
        '''
        Return a function that returns a FindStat representation given an
        object.

        If the collection is not yet supported, return the identity.

        OUTPUT:

        The function that produces the string representation as
        needed by the FindStat search webpage.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: p = Poset((range(3), [[0, 1], [1, 2]]))                       # optional -- internet
            sage: c = FindStatCollection("Posets")                              # optional -- internet
            sage: c.to_string()(p)                                              # optional -- internet
            \'([(0, 1), (1, 2)], 3)\'
        '''
    def from_string(self):
        '''
        Return a function that returns the object given a FindStat
        representation.

        OUTPUT:

        The function that produces the Sage object given its FindStat
        representation as a string.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: c = FindStatCollection("Posets")                              # optional -- internet
            sage: p = c.from_string()(\'([(0, 2), (2, 1)], 3)\')                  # optional -- internet
            sage: p.cover_relations()                                           # optional -- internet
            [[0, 2], [2, 1]]

            sage: c = FindStatCollection("Binary Words")                        # optional -- internet
            sage: w = c.from_string()(\'010101\')                                 # optional -- internet
            sage: w in c._data["Code"].elements_on_level(6)                     # optional -- internet
            True
        '''
    def name(self, style: str = 'singular'):
        '''
        Return the name of the FindStat collection.

        INPUT:

        - ``style`` -- string (default: ``\'singular\'``); can be
          ``\'singular\'``, or ``\'plural\'``

        OUTPUT: the name of the FindStat collection, in singular or in plural

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollection
            sage: FindStatCollection("Binary trees").name()                     # optional -- internet
            \'Binary tree\'

            sage: FindStatCollection("Binary trees").name(style=\'plural\')       # optional -- internet
            \'Binary trees\'
        '''

class _SupportedFindStatCollection(NamedTuple):
    string_to_element: Incomplete
    element_to_string: Incomplete
    elements_on_level: Incomplete
    element_level: Incomplete
    is_element: Incomplete

class FindStatCollections(UniqueRepresentation, Parent):
    """
    The class of FindStat collections.

    The elements of this class are combinatorial collections in
    FindStat as of January 2020.  If a new collection was added to the
    web service since then, the dictionary ``_SupportedFindStatCollections``
    in this module has to be updated accordingly.

    EXAMPLES::

        sage: from sage.databases.findstat import FindStatCollections
        sage: sorted(c for c in FindStatCollections() if c.is_supported())      # optional -- internet
        [Cc0001: Permutations,
         Cc0002: Integer partitions,
         Cc0005: Dyck paths,
         Cc0006: Integer compositions,
         Cc0007: Standard tableaux,
         Cc0009: Set partitions,
         Cc0010: Binary trees,
         Cc0012: Perfect matchings,
         Cc0013: Cores,
         Cc0014: Posets,
         Cc0017: Alternating sign matrices,
         Cc0018: Gelfand-Tsetlin patterns,
         Cc0019: Semistandard tableaux,
         Cc0020: Graphs,
         Cc0021: Ordered trees,
         Cc0022: Finite Cartan types,
         Cc0023: Parking functions,
         Cc0024: Binary words,
         Cc0025: Plane partitions,
         Cc0026: Decorated permutations,
         Cc0027: Signed permutations,
         Cc0028: Skew partitions,
         Cc0029: Lattices,
         Cc0030: Ordered set partitions]
    """
    def __init__(self) -> None:
        """
        Fetch the collections from FindStat.

        TESTS::

            sage: from sage.databases.findstat import FindStatCollections
            sage: C = FindStatCollections()                                     # optional -- internet
            sage: TestSuite(C).run()                                            # optional -- internet
        """
    def __iter__(self):
        """
        Return an iterator over all FindStat collections.

        EXAMPLES::

            sage: from sage.databases.findstat import FindStatCollections
            sage: sorted(FindStatCollections())[0]                              # optional -- internet
            Cc0001: Permutations
        """
    Element = FindStatCollection
