from _typeshed import Incomplete
from enum import Enum
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.persist import load as load, save as save
from sage.misc.verbose import verbose as verbose
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

columns_white_list: Incomplete
columns_black_list: Incomplete

class KnotInfoColumnTypes(Enum):
    """
    Enum class to specify if a column from the table of knots and links provided
    at the web-pages `KnotInfo <https://knotinfo.math.indiana.edu/>`__ and
    `LinkInfo <https://linkinfo.sitehost.iu.edu>`__.  is used for knots only,
    links only or both.

    EXAMPLES::

        sage: from sage.databases.knotinfo_db import KnotInfoColumnTypes
        sage: [col_type for col_type in KnotInfoColumnTypes]
        [<KnotInfoColumnTypes.OnlyKnots: 'K'>,
        <KnotInfoColumnTypes.OnlyLinks: 'L'>,
        <KnotInfoColumnTypes.KnotsAndLinks: 'B'>]
    """
    OnlyKnots = 'K'
    OnlyLinks = 'L'
    KnotsAndLinks = 'B'

class KnotInfoColumns(Enum):
    """
    Enum class to select a column from the table of knots and links provided
    at the web-pages `KnotInfo <https://knotinfo.math.indiana.edu/>`__ and
    `LinkInfo <https://linkinfo.sitehost.iu.edu>`__.

    EXAMPLES::

        sage: from sage.databases.knotinfo_db import KnotInfoDataBase
        sage: ki_db = KnotInfoDataBase()
        sage: cols = ki_db.columns(); cols
        <enum 'Columns'>
        sage: from sage.databases.knotinfo_db import KnotInfoColumns
        sage: isinstance(cols.name, KnotInfoColumns)
        True

        sage: def only_links(c):
        ....:     return c.column_type() == c.types.OnlyLinks
        sage: [c.column_name() for c in cols if only_links(c)]  # optional - database_knotinfo
        ['Name - Unoriented',
         'Orientation',
         'Unoriented Rank',
         'PD Notation (vector)',
         'PD Notation (KnotTheory)',
         'Braid Notation',
         'Quasipositive Braid',
         'Multivariable Alexander Polynomial',
         'HOMFLYPT Polynomial',
         'Khovanov Polynomial',
         'Unoriented',
         'Arc Notation',
         'Linking Matrix',
         'Rolfsen Name',
         'Components',
         'DT code',
         'Splitting Number',
         'Nullity',
         'Unlinking Number',
         'Weak Splitting Number']
    """
    @property
    def types(self):
        """
        Return :class:`KnotInfoColumnTypes` to be used for checks.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: cols = ki_db.columns()
            sage: cols.dt_code.column_type() == cols.dt_code.types.OnlyLinks
            True
        """
    def column_name(self):
        """
        Return the name of ``self`` displayed on the KnotInfo web-page.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: cols = ki_db.columns()
            sage: cols.dt_code.column_name()
            'DT code'
        """
    def column_type(self):
        """
        Return the type of ``self``. That is an instance of ``Enum``
        :class:`KnotInfoColumnTypes`.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: cols = ki_db.columns()
            sage: cols.homfly_polynomial.column_type()
            <KnotInfoColumnTypes.OnlyKnots: 'K'>
            sage: cols.homflypt_polynomial.column_type()
            <KnotInfoColumnTypes.OnlyLinks: 'L'>
            sage: cols.name.column_type()
            <KnotInfoColumnTypes.KnotsAndLinks: 'B'>
        """
    def description_webpage(self, new: int = 0, autoraise: bool = True):
        """
        Launch the description page of ``self`` in the standard web browser.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: cols = ki_db.columns()
            sage: cols.pd_notation.description_webpage()            # not tested
            True
            sage: cols.homflypt_polynomial.description_webpage()    # not tested
            True
        """

class KnotInfoFilename(Enum):
    """
    Enum for the different data files. The following choices are possible:

    - ``knots`` -- contains the data from KnotInfo
    - ``links`` -- contains the data for proper links from LinkInfo

    Examples::

        sage: from sage.databases.knotinfo_db import KnotInfoDataBase
        sage: ki_db = KnotInfoDataBase()
        sage: ki_db.filename
        <enum 'KnotInfoFilename'>
    """
    def url(self):
        """
        Return the URL to download the data from the web-page.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.url()
            'https://knotinfo.math.indiana.edu/'
        """
    def excel(self):
        """
        Return the Excel-file name to download the data from the web-page.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.excel()
            'knotinfo_data_complete.xls'
        """
    def csv(self):
        """
        Return the file name under which the data from the web-page
        are stored as csv file.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.csv()
            'knotinfo_data_complete.csv'
        """
    def num_knots(self, version):
        """
        Return the file name under which the number of knots is stored
        in an sobj-file.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.num_knots('21.7')
            'num_knots_21.7.sobj'
        """
    def sobj_row(self):
        """
        Return the file name under which the row-data of the csv-File
        is stored as python dictionary in a sobj-file.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.sobj_row()
            'row_dict.sobj'
        """
    def sobj_column(self):
        """
        Return the file name under which the column-data of the csv-File
        is stored as python dictionary in a sobj-file.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.sobj_column()
            'column_dict.sobj'
        """
    def sobj_data(self, column):
        """
        Return the file name under which the data of the given
        column is stored as python list in a sobj-file.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.sobj_data(ki_db.columns().braid_notation)
            'knotinfo_braid_notation'
        """
    def description_url(self, column):
        """
        Return the url of the description page of the given column.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.description_url(ki_db.columns().braid_notation)
            'https://knotinfo.math.indiana.edu/descriptions/braid_notation.html'
        """
    def diagram_url(self, fname, single: bool = False):
        """
        Return the url of the diagram page of the given link.

        Examples::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.knots.diagram_url('3_1-50.png')
            'https://knotinfo.math.indiana.edu/diagram_display.php?3_1-50.png'
            sage: ki_db.filename.knots.diagram_url('3_1', single=True)
            'https://knotinfo.math.indiana.edu/diagrams/3_1'
        """
    knots = ['https://knotinfo.math.indiana.edu/', 'knotinfo_data_complete']
    links = ['https://linkinfo.sitehost.iu.edu/', 'linkinfo_data_complete']

class KnotInfoDataBase(SageObject, UniqueRepresentation):
    """
    Database interface to KnotInfo.

    The original data are obtained from KnotInfo web-page (URL see the example
    below). In order to have these data installed during the build process as
    a sage-package they are converted as csv files into a tarball. This tarball
    has been created using the method :meth:`create_spkg_tarball`.

    EXAMPLES::

        sage: from sage.databases.knotinfo_db import KnotInfoDataBase
        sage: ki_db = KnotInfoDataBase()
        sage: ki_db.filename.knots
        <KnotInfoFilename.knots: ['https://knotinfo.math.indiana.edu/',
                                  'knotinfo_data_complete']>
    """
    filename = KnotInfoFilename
    def __init__(self, install: bool = False) -> None:
        """
        Python constructor.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.filename.links
            <KnotInfoFilename.links: ['https://linkinfo.sitehost.iu.edu/',
                                      'linkinfo_data_complete']>
        """
    def create_filecache(self, force: bool = False) -> None:
        """
        Create the internal files containing the database.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if set to ``True`` the
          existing file-cache is overwritten

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.create_filecache()    # optional - database_knotinfo
        """
    def version(self):
        """
        Return the version of the database currently installed on the device.

        .. NOTE::

            The development of the original databases on the KnotInfo and
            LinkInfo web-pages is in a continuous flow. The installed version
            can be behind the current available state of these databases. Every
            month a cronjob on the
            `GitHub repository <https://github.com/soehms/database_knotinfo/>`__
            searches for differences and creates a new release on
            `PyPI <https://pypi.org/project/database-knotinfo/>`__ in case of
            success.

            If you note that your version is behind the version on PyPI
            and would like to have Sage working with that release you should
            first try to upgrade using ``sage -i database_knotinfo``. If this
            is not successful even though you are on the latest Sage release
            please create an issue for that in the GitHub repository.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.version()   >= '2021.10.1'   # optional database_knotinfo
            True
        """
    def demo_version(self):
        """
        Return whether the KnotInfo databases are installed completely or
        just the demo version is used.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.demo_version()       # optional - database_knotinfo
            False
        """
    def knot_list(self):
        """
        Return the KnotInfo table rows as Python list.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: len(ki_db.knot_list())  # not tested (just used on installation)
        """
    def link_list(self):
        """
        Return the LinkInfo table rows as Python list.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: len(ki_db.link_list())  # not tested (just used on installation)
        """
    @cached_method
    def columns(self):
        """
        Return the columns ot the database table as instances of enum class
        :class:`KnotInfoColumns`.

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: cols = ki_db.columns()
            sage: [col.column_name() for col in cols if col.name.startswith('pd')]   # optional - database_knotinfo
            ['PD Notation', 'PD Notation (vector)', 'PD Notation (KnotTheory)']
        """
    @cached_method
    def read_column_dict(self):
        """
        Read the dictionary for the column names from the according sobj-file.

        OUTPUT: a Python dictionary containing the column names and types

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: len(ki_db.read_column_dict()) > 120       # optional - database_knotinfo
            True
        """
    @cached_method
    def read_row_dict(self):
        """
        Read the dictionary for the row names that is the knot and link names
        from the according sobj-file

        OUTPUT:

        A python dictionary containing the names of the knots and links
        together with their table index and the corresponding number of
        components

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.read_row_dict()['K7_1']
            [8, 1]
        """
    @cached_method
    def row_names(self):
        """
        Return a dictionary to obtain the original name to a row_dict key.

        OUTPUT: a Python dictionary containing the names of the knots and links
        together with their original names from the database

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.row_names()['K7_1']      # optional - database_knotinfo
            '7_1'
        """
    def read_num_knots(self):
        """
        Read the number of knots contained in the database (without
        proper links) from the according sobj-file.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
            sage: ki_db.read_num_knots()              # optional - database_knotinfo
            12966
        """
    @cached_method
    def read(self, column):
        """
        Access a column of KnotInfo / LinkInfo.

        INPUT:

        - ``column`` -- instance of enum :class:`KnotInfoColumns`
          to select the data to be read in

        OUTPUT: a Python list containing the data corresponding to the column

        EXAMPLES::

            sage: from sage.databases.knotinfo_db import KnotInfoDataBase
            sage: ki_db = KnotInfoDataBase()
        """

column_demo_sample: Incomplete
row_demo_sample: Incomplete
db: Incomplete
dc: Incomplete
data_demo_sample: Incomplete
