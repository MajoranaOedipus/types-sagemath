from _typeshed import Incomplete
from enum import Enum
from sage.algebras.hecke_algebras.cubic_hecke_base_ring import CubicHeckeExtensionRing as CubicHeckeExtensionRing
from sage.matrix.constructor import matrix as matrix
from sage.misc.persist import load as load
from sage.misc.temporary_file import atomic_write as atomic_write
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

def simplify(mat):
    """
    Convert a matrix to a dictionary consisting of flat Python objects.

    INPUT:

    - ``mat`` -- matrix to be converted into a ``dict``

    OUTPUT:

    A ``dict`` from which ``mat`` can be reconstructed via
    element construction. The values of the dictionary may be
    dictionaries of tuples of integers or strings.

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import simplify
        sage: import sage.algebras.hecke_algebras.cubic_hecke_base_ring as chbr
        sage: ER.<a, b, c> = chbr.CubicHeckeExtensionRing()
        sage: mat = matrix(ER, [[2*a, -3], [c, 4*b*~c]]); mat
        [     2*a       -3]
        [       c 4*b*c^-1]
        sage: simplify(mat)
        {(0, 0): {(1, 0, 0): {0: 2}},
         (0, 1): {(0, 0, 0): {0: -3}},
         (1, 0): {(0, 0, 1): {0: 1}},
         (1, 1): {(0, 1, -1): {0: 4}}}
        sage: mat == matrix(ER, _)
        True
        sage: F = ER.fraction_field()
        sage: matf = mat.change_ring(F)
        sage: simplify(matf)
        {(0, 0): '2*a', (0, 1): '-3', (1, 0): 'c', (1, 1): '4*b/c'}
        sage: matf == matrix(F, _)
        True
    """

class CubicHeckeDataSection(Enum):
    """
    Enum for the different sections of the database.

    The following choices are possible:

    - ``basis`` -- list of basis elements
    - ``reg_left_reprs`` -- data for the left regular representation
    - ``reg_right_reprs`` -- data for the right regular representation
    - ``irr_reprs`` -- data for the split irreducible representations
    - ``markov_tr_cfs`` -- data for the coefficients of the formal Markov traces

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
        sage: cha_db = CubicHeckeDataBase()
        sage: cha_db.section
        <enum 'CubicHeckeDataSection'>
    """
    basis = 'basis'
    regular_left = 'regular_left'
    regular_right = 'regular_right'
    split_irred = 'split_irred'
    markov_tr_cfs = 'markov_tr_cfs'

class CubicHeckeDataBase(SageObject):
    """
    Database interface for
    :class:`~sage.algebras.hecke_algebras.cubic_hecke_algebras.CubicHeckeAlgebra`

    The original data are obtained from `Ivan Marin's web page
    <http://www.lamfa.u-picardie.fr/marin/representationH4-en.html>`__

    The data needed to work with the cubic Hecke algebras on less than 4 strands
    is completely contained in this module. Data needed for the larger algebras
    can be installed as an optional Sage package which comes as a ``pip`` installable
    `Python wrapper <https://pypi.org/project/database-cubic-hecke/>`__ of
    Ivan Marin's data. For more information see the `corresponding repository
    <https://github.com/soehms/database_cubic_hecke>`__.

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
        sage: cha_db = CubicHeckeDataBase()
        sage: cha_db._feature
        Feature('database_cubic_hecke')
    """
    section = CubicHeckeDataSection
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
            sage: cha_db = CubicHeckeDataBase()
            sage: cha_db._data_library
            {}
        """
    def version(self):
        """
        Return the current version of the database.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
            sage: cha_db = CubicHeckeDataBase()
            sage: cha_db.version() > '2022.1.1'   # optional - database_cubic_hecke
            True
        """
    def demo_version(self):
        """
        Return whether the cubic Hecke database is installed completely or
        just the demo version is used.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.demo_version()       # optional - database_knotinfo
            False
        """
    def read(self, section, variables=None, nstrands: int = 4):
        """
        Access various static data libraries.

        INPUT:

        - ``section`` -- instance of enum :class:`CubicHeckeDataSection`
          to select the data to be read in

        OUTPUT: a dictionary containing the data corresponding to the section

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
            sage: cha_db = CubicHeckeDataBase()
            sage: basis = cha_db.read(cha_db.section.basis, nstrands=3)
            sage: len(basis)
            24
        """
    def read_matrix_representation(self, representation_type, gen_ind, nstrands, ring_of_definition):
        """
        Return the matrix representations from the database.

        INPUT:

        - ``representation_type`` -- an element of
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_matrix_rep.RepresentationType`
          specifying the type of the representation

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeDataBase
            sage: CHA3 = algebras.CubicHecke(2)
            sage: GER = CHA3.extension_ring(generic=True)
            sage: cha_db = CHA3._database
            sage: rt = CHA3.repr_type
            sage: m1 =cha_db.read_matrix_representation(rt.SplitIrredMarin, 1, 3, GER)
            sage: len(m1)
            7
            sage: GBR = CHA3.base_ring(generic=True)
            sage: m1rl = cha_db.read_matrix_representation(rt.RegularLeft, 1, 3, GBR)
            sage: m1rl[0].dimensions()
            (24, 24)
        """

class MarkovTraceModuleBasis(Enum):
    """
    Enum for the basis elements for the Markov trace module.

    The choice of the basis elements doesn't have a systematically background
    apart from generating the submodule of maximal rank in the module of linear
    forms on the cubic Hecke algebra for which the Markov trace condition with
    respect to its cubic Hecke subalgebras hold. The number of crossings in
    the corresponding links is chosen as minimal as possible.

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
        sage: MarkovTraceModuleBasis.K92.description()
        'knot 9_34'
    """
    def __gt__(self, other):
        """
        Implement comparison of different items in order to have ``sorted`` work.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: sorted(MarkovTraceModuleBasis)
            [U1, U2, U3, K4, U4, K4U, K6, K7, K91, K92]
        """
    def strands(self):
        """
        Return the number of strands of the minimal braid representative
        of the link corresponding to ``self``.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.K7.strands()
            4
        """
    def braid_tietze(self, strands_embed=None):
        """
        Return the Tietze representation of the braid corresponding to this basis
        element.

        INPUT:

        - ``strands_embed`` -- (optional) the number of strands of the braid
          if strands should be added

        OUTPUT: a tuple representing the braid in Tietze form

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U2.braid_tietze()
            ()
            sage: MarkovTraceModuleBasis.U2.braid_tietze(strands_embed=4)
            (2, 3)
        """
    def writhe(self):
        """
        Return the writhe of the link corresponding to this basis element.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.K4.writhe()
            0
            sage: MarkovTraceModuleBasis.K6.writhe()
            1
        """
    def description(self):
        """
        Return a description of the link corresponding to this basis element.

        In the case of knots it refers to the naming according to
        `KnotInfo <https://knotinfo.math.indiana.edu/>`__.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U3.description()
            'three unlinks'
        """
    def link(self):
        """
        Return the :class:`Link` that represents this basis element.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U1.link()
            Link with 1 component represented by 0 crossings
            sage: MarkovTraceModuleBasis.K4.link()
            Link with 1 component represented by 4 crossings
        """
    def regular_homfly_polynomial(self):
        """
        Return the regular variant of the HOMFLY-PT polynomial of the link that
        represents this basis element.

        This is the HOMFLY-PT polynomial renormalized by the writhe factor
        such that it is an invariant of regular isotopy.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U1.regular_homfly_polynomial()
            1
            sage: u2 = MarkovTraceModuleBasis.U2.regular_homfly_polynomial(); u2
            -L*M^-1 - L^-1*M^-1
            sage: u2**2 == MarkovTraceModuleBasis.U3.regular_homfly_polynomial()
            True
            sage: u2**3 == MarkovTraceModuleBasis.U4.regular_homfly_polynomial()
            True
        """
    def regular_kauffman_polynomial(self):
        """
        Return the regular variant of the Kauffman polynomial of the link that
        represents this basis element.

        This is the Kauffman polynomial renormalized by the writhe factor
        such that it is an invariant of regular isotopy.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U1.regular_homfly_polynomial()
            1
            sage: u2 = MarkovTraceModuleBasis.U2.regular_kauffman_polynomial(); u2
            a*z^-1 - 1 + a^-1*z^-1
            sage: u2**2 == MarkovTraceModuleBasis.U3.regular_kauffman_polynomial()
            True
            sage: u2**3 == MarkovTraceModuleBasis.U4.regular_kauffman_polynomial()
            True
        """
    def links_gould_polynomial(self):
        """
        Return the Links-Gould polynomial of the link that represents this
        basis element.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import MarkovTraceModuleBasis
            sage: MarkovTraceModuleBasis.U1.links_gould_polynomial()
            1
            sage: MarkovTraceModuleBasis.U2.links_gould_polynomial()
            0
            sage: MarkovTraceModuleBasis.K4.links_gould_polynomial()
            2*t0*t1 - 3*t0 - 3*t1 + t0*t1^-1 + 7 + t0^-1*t1
            - 3*t1^-1 - 3*t0^-1 + 2*t0^-1*t1^-1
        """
    U1 = ['one unlink', 1, (), []]
    U2 = ['two unlinks', 2, (), [[3, 1, 4, 2], [4, 1, 3, 2]]]
    U3 = ['three unlinks', 3, (), [[3, 7, 4, 8], [4, 7, 5, 8], [5, 1, 6, 2], [6, 1, 3, 2]]]
    U4 = ['four unlinks', 4, (), [[3, 9, 4, 10], [4, 9, 5, 10], [5, 11, 6, 12], [6, 11, 7, 12], [7, 1, 8, 2], [8, 1, 3, 2]]]
    K4U = ['knot 4_1 plus one unlink', 4, (1, -2, 1, -2), [[3, 8, 4, 9], [9, 7, 10, 6], [7, 4, 8, 5], [5, 11, 6, 10], [11, 1, 12, 2], [12, 1, 3, 2]]]
    K4 = ['knot 4_1', 3, (1, -2, 1, -2), None]
    K6 = ['knot 6_1', 4, (1, 1, 2, -1, -3, 2, -3), None]
    K7 = ['knot 7_4', 4, (1, 1, 2, -1, 2, 2, 3, -2, 3), None]
    K91 = ['knot 9_29', 4, (1, -2, -2, 3, -2, 1, -2, 3, -2), None]
    K92 = ['knot 9_34', 4, (-1, 2, -1, 2, -3, 2, -1, 2, -3), None]

kauffman: Incomplete
links_gould: Incomplete

class CubicHeckeFileCache(SageObject):
    """
    A class to cache calculations of
    :class:`~sage.algebras.hecke_algebras.cubic_hecke_algebras.CubicHeckeAlgebra`
    in the local file system.
    """
    class section(Enum):
        """
        Enum for the different sections of file cache.

        The following choices are possible:

        - ``matrix_representations`` -- file cache for representation matrices
          of basis elements
        - ``braid_images`` -- file cache for images of braids
        - ``basis_extensions`` -- file cache for a dynamical growing basis used
          in the case of cubic Hecke algebras on more than 4 strands
        - ``markov_trace`` -- file cache for intermediate results of long
          calculations in order to recover the results already obtained by
          previous attempts of calculation until the corresponding intermediate
          step

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: CHA2 = algebras.CubicHecke(2)
            sage: cha_fc = CubicHeckeFileCache(CHA2)
            sage: cha_fc.section
            <enum 'section'>
        """
        def filename(self, nstrands=None):
            """
            Return the file name under which the data of this file cache section
            is stored as an sobj-file.

            INPUT:

            - ``nstrands`` -- (optional) :class:`Integer`; number of strands of
              the underlying braid group if the data file depends on it

            EXAMPLES::

                sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
                sage: CHA2 = algebras.CubicHecke(2)
                sage: cha_fc = CubicHeckeFileCache(CHA2)
                sage: cha_fc.section.matrix_representations.filename(2)
                'matrix_representations_2.sobj'
                sage: cha_fc.section.braid_images.filename(2)
                'braid_images_2.sobj'
            """
        matrix_representations = 'matrix_representations'
        braid_images = 'braid_images'
        basis_extensions = 'basis_extensions'
        markov_trace = 'markov_trace'
    def __init__(self, num_strands) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``num_strands`` -- integer giving the number of strands of the
          corresponding cubic Hecke algebra

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: cha_fc = CubicHeckeFileCache(2)
            sage: cha_fc._file_cache_path.endswith('cubic_hecke')
            True
        """
    def reset_library(self, section=None) -> None:
        """
        Reset the file cache corresponding to the specified ``section``.

        INPUT:

        - ``section`` -- an element of :class:`CubicHeckeFileCache.section`
          to select the section of the file cache or ``None`` (default)
          meaning all sections

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: cha2_fc = CubicHeckeFileCache(2)
            sage: cha2_fc.reset_library(cha2_fc.section.braid_images)
            sage: cha2_fc.read(cha2_fc.section.braid_images)
            {}
            sage: cha2_fc.reset_library(cha2_fc.section.matrix_representations)
            sage: data_mat = cha2_fc.read(cha2_fc.section.matrix_representations)
            sage: len(data_mat.keys())
            4
        """
    def is_empty(self, section=None):
        """
        Return ``True`` if the cache of the given ``section`` is empty.

        INPUT:

        - ``section`` -- an element of :class:`CubicHeckeFileCache.section`
          to select the section of the file cache or ``None`` (default)
          meaning all sections

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: cha2_fc = CubicHeckeFileCache(2)
            sage: cha2_fc.reset_library()
            sage: cha2_fc.is_empty()
            True
        """
    def write(self, section=None) -> None:
        """
        Write data from memory to the file system.

        INPUT:

        - ``section`` -- an element of :class:`CubicHeckeFileCache.section`
          specifying the section where the corresponding cached data belong to;
          if omitted, the data of all sections is written to the file system

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: cha2_fc = CubicHeckeFileCache(2)
            sage: cha2_fc.reset_library(cha2_fc.section.braid_images)
            sage: cha2_fc.write(cha2_fc.section.braid_images)
        """
    def read(self, section):
        """
        Read data into memory from the file system.

        INPUT:

        - ``section`` -- an element of :class:`CubicHeckeFileCache.section`
          specifying the section where the corresponding cached data belong to

        OUTPUT:

        Dictionary containing the data library corresponding to the section
        of file cache

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: cha2_fc = CubicHeckeFileCache(2)
            sage: cha2_fc.reset_library(cha2_fc.section.braid_images)
            sage: cha2_fc.read(cha2_fc.section.braid_images)
            {}
        """
    def read_matrix_representation(self, representation_type, monomial_tietze, ring_of_definition):
        """
        Return the matrix representations of the given monomial (in Tietze form)
        if it has been stored in the file cache before.
        INPUT:

        - ``representation_type`` -- an element of
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_matrix_rep.RepresentationType`
          specifying the type of the representation
        - ``monomial_tietze`` -- tuple representing the braid in Tietze form
        - ``ring_of_definition`` -- instance of
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_base_ring.CubicHeckeRingOfDefinition`
          respectively
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_base_ring.CubicHeckeExtensionRing`
          depending on whether ``representation_type`` is split or not

        OUTPUT:

        Dictionary containing all matrix representations of ``self`` of the
        given ``representation_type`` which have been stored in the file cache.
        Otherwise ``None`` is returned.

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: R = CHA2.base_ring(generic=True)
            sage: cha_fc = CHA2._filecache
            sage: g, = CHA2.gens(); gt = g.Tietze()
            sage: rt = CHA2.repr_type
            sage: g.matrix(representation_type=rt.RegularLeft)
            [ 0 -v  1]
            [ 1  u  0]
            [ 0  w  0]
            sage: [_] == cha_fc.read_matrix_representation(rt.RegularLeft, gt, R)
            True
            sage: cha_fc.reset_library(cha_fc.section.matrix_representations)
            sage: cha_fc.write(cha_fc.section.matrix_representations)
            sage: cha_fc.read_matrix_representation(rt.RegularLeft, gt, R) == None
            True
        """
    def write_matrix_representation(self, representation_type, monomial_tietze, matrix_list) -> None:
        """
        Write the matrix representation of a monomial to the file cache.

        INPUT:

        - ``representation_type`` -- an element of
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_matrix_rep.RepresentationType`
          specifying the type of the representation
        - ``monomial_tietze`` -- tuple representing the braid in Tietze form
        - ``matrix_list`` -- list of matrices corresponding to the irreducible
          representations

        EXAMPLES::

            sage: CHA2 = algebras.CubicHecke(2)
            sage: R = CHA2.base_ring(generic=True)
            sage: cha_fc = CHA2._filecache
            sage: g, = CHA2.gens(); gi = ~g; git = gi.Tietze()
            sage: rt = CHA2.repr_type
            sage: m = gi.matrix(representation_type=rt.RegularRight)
            sage: cha_fc.read_matrix_representation(rt.RegularRight, git, R)
            [
            [     0      1 (-u)/w]
            [     0      0    1/w]
            [     1      0    v/w]
            ]
            sage: CHA2.reset_filecache(cha_fc.section.matrix_representations)
            sage: cha_fc.read_matrix_representation(rt.RegularLeft, git, R) == None
            True
            sage: cha_fc.write_matrix_representation(rt.RegularRight, git, [m])
            sage: [m] == cha_fc.read_matrix_representation(rt.RegularRight, git, R)
            True
        """
    def read_braid_image(self, braid_tietze, ring_of_definition):
        """
        Return the list of pre calculated braid images from file cache.

        INPUT:

        - ``braid_tietze`` -- tuple representing the braid in Tietze form
        - ``ring_of_definition`` -- a
          :class:`~sage.algebras.hecke_algebras.cubic_hecke_base_ring.CubicHeckeRingOfDefinition`

        OUTPUT:

        A dictionary containing the pre calculated braid image of the given
        braid.

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: CHA2 = algebras.CubicHecke(2)
            sage: ring_of_definition = CHA2.base_ring(generic=True)
            sage: cha_fc = CubicHeckeFileCache(2)
            sage: B2 = BraidGroup(2)
            sage: b, = B2.gens(); b2 = b**2
            sage: cha_fc.is_empty(CubicHeckeFileCache.section.braid_images)
            True
            sage: b2_img = CHA2(b2); b2_img
            w*c^-1 + u*c - v
            sage: cha_fc.write_braid_image(b2.Tietze(), b2_img.to_vector())
            sage: cha_fc.read_braid_image(b2.Tietze(), ring_of_definition)
            (-v, u, w)
        """
    def write_braid_image(self, braid_tietze, braid_image_vect) -> None:
        """
        Write the braid image of the given braid to the file cache.

        INPUT:

        - ``braid_tietze`` -- tuple representing the braid in Tietze form
        - ``braid_image_vect`` -- image of the given braid as a vector with
          respect to the basis of the cubic Hecke algebra

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: CHA2 = algebras.CubicHecke(2)
            sage: ring_of_definition = CHA2.base_ring(generic=True)
            sage: cha_fc = CubicHeckeFileCache(2)
            sage: B2 = BraidGroup(2)
            sage: b, = B2.gens(); b3 = b**3
            sage: b3_img = CHA2(b3); b3_img
            u*w*c^-1 + (u^2-v)*c - (u*v-w)
            sage: cha_fc.write_braid_image(b3.Tietze(), b3_img.to_vector())
            sage: cha_fc.read_braid_image(b3.Tietze(), ring_of_definition)
            (-u*v + w, u^2 - v, u*w)
            sage: cha_fc.reset_library(CubicHeckeFileCache.section.braid_images)
            sage: cha_fc.write(CubicHeckeFileCache.section.braid_images)
            sage: cha_fc.is_empty(CubicHeckeFileCache.section.braid_images)
            True
        """
    def update_basis_extensions(self, new_basis_extensions) -> None:
        """
        Update the file cache for basis extensions for cubic Hecke algebras on
        more than 4 strands according to the given ``new_basis_extensions``.

        INPUT:

        - ``new_basis_extensions`` -- list of additional (to the static basis)
          basis elements which should replace the former such list in the file

        EXAMPLES::

            sage: from sage.databases.cubic_hecke_db import CubicHeckeFileCache
            sage: CHA2 = algebras.CubicHecke(2)
            sage: cha_fc = CubicHeckeFileCache(2)
            sage: cha_fc.is_empty(CubicHeckeFileCache.section.basis_extensions)
            True
            sage: cha_fc.update_basis_extensions([(1,), (-1,)])
            sage: cha_fc.read(CubicHeckeFileCache.section.basis_extensions)
            [(1,), (-1,)]
            sage: cha_fc.reset_library(CubicHeckeFileCache.section.basis_extensions)
            sage: cha_fc.write(CubicHeckeFileCache.section.basis_extensions)
            sage: cha_fc.is_empty(CubicHeckeFileCache.section.basis_extensions)
            True
        """

func_name: str
var_decl: str
var_doc_input: str
var_doc_decl: str
template: str
doc: Incomplete

def create_demo_data(filename: str = 'demo_data.py'):
    """
    Generate code for the functions inserted below to access the
    small cases of less than 4 strands as demonstration cases.

    The code is written to a file with the given name from where
    it can be copied into this source file (in case a change is needed).

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import create_demo_data
        sage: create_demo_data()   # not tested
    """
def read_basis(num_strands: int = 3):
    """
    Return precomputed data of Ivan Marin.

    This code was generated by :func:`create_demo_data`, please do not edit.

    INPUT:

    - ``num_strands`` -- integer; number of strands of the cubic Hecke algebra

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import read_basis
        sage: read_basis(2)
        [[], [1], [-1]]
    """
def read_irr(variables, num_strands: int = 3):
    """
    Return precomputed data of Ivan Marin.

    This code was generated by :func:`create_demo_data`, please do not edit.

    INPUT:

    - ``variables`` -- tuple containing the indeterminates of the representation
    - ``num_strands`` -- integer; number of strands of the cubic Hecke algebra

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import read_irr
        sage: L.<a, b, c, j> = LaurentPolynomialRing(ZZ)
        sage: read_irr((a, b, c, j), 2)
        ([1, 1, 1],
        [[{(0, 0): a}], [{(0, 0): c}], [{(0, 0): b}]],
        [[{(0, 0): a^-1}], [{(0, 0): c^-1}], [{(0, 0): b^-1}]])
    """
def read_regl(variables, num_strands: int = 3):
    """
    Return precomputed data of Ivan Marin.

    This code was generated by :func:`create_demo_data`, please do not edit.

    INPUT:

    - ``variables`` -- tuple containing the indeterminates of the representation
    - ``num_strands`` -- integer; number of strands of the cubic Hecke algebra

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import read_regl
        sage: L.<u, v, w> = LaurentPolynomialRing(ZZ)
        sage: read_regl((u, v, w), 2)
        ([3],
        [[{(0, 1): -v, (0, 2): 1, (1, 0): 1, (1, 1): u, (2, 1): w}]],
        [[{(0, 1): 1, (0, 2): -u*w^-1, (1, 2): w^-1, (2, 0): 1, (2, 2): v*w^-1}]])
    """
def read_regr(variables, num_strands: int = 3):
    """
    Return precomputed data of Ivan Marin.

    This code was generated by :func:`create_demo_data`, please do not edit.

    INPUT:

    - ``variables`` -- tuple containing the indeterminates of the representation
    - ``num_strands`` -- integer; number of strands of the cubic Hecke algebra

    EXAMPLES::

        sage: from sage.databases.cubic_hecke_db import read_regr
        sage: L.<u, v, w> = LaurentPolynomialRing(ZZ)
        sage: read_regr((u, v, w), 2)
        ([3],
        [[{(0, 1): -v, (0, 2): 1, (1, 0): 1, (1, 1): u, (2, 1): w}]],
        [[{(0, 1): 1, (0, 2): -u*w^-1, (1, 2): w^-1, (2, 0): 1, (2, 2): v*w^-1}]])
    """
def read_markov(bas_ele, variables, num_strands: int = 4):
    """
    Return precomputed Markov trace coefficients.

    This code was generated by ``create_markov_trace_data.py`` (from
    the ``database_cubic_hecke`` repository), please do not edit.

    INPUT:

    - ``bas_ele`` -- an element of :class:`MarkovTraceModuleBasis`
    - ``variables`` -- tuple consisting of the variables used in
      the coefficients
    - ``num_strands`` -- integer (default: 4); the number of strands

    OUTPUT:

    A list of the coefficients. The i'th member corresponds to the i'th
    basis element.

    EXAMPLES::

        sage: # needs sympy
        sage: from sage.databases.cubic_hecke_db import read_markov
        sage: from sympy import var
        sage: u, v, w, s = var('u, v, w, s')
        sage: variables = (u, v, w, s)
        sage: read_markov('U2', variables, num_strands=3)
        [0, s, 1/s, s, 1/s, 0, 0, 0, 0, -s*v, s, s, -s*u/w, -v/s, 1/s,
         0, 0, 0, 0, 1/s, -u/(s*w), -v/s, 0, 0]
    """
