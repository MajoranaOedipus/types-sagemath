from sage.env import sage_data_paths as sage_data_paths
from sage.features import PythonModule as PythonModule, StaticFile as StaticFile

class DatabaseCremona(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of :ref:`John Cremona's
    database of elliptic curves <spkg_database_cremona_ellcurve>`.

    INPUT:

    - ``name`` -- either ``'cremona'`` (the default) for the full large
      database or ``'cremona_mini'`` for the small database

    EXAMPLES::

        sage: from sage.features.databases import DatabaseCremona
        sage: DatabaseCremona('cremona_mini', type='standard').is_present()
        FeatureTestResult('database_cremona_mini_ellcurve', True)
        sage: DatabaseCremona().is_present()                                    # optional - database_cremona_ellcurve
        FeatureTestResult('database_cremona_ellcurve', True)
    """
    def __init__(self, name: str = 'cremona', spkg: str = 'database_cremona_ellcurve', type: str = 'optional') -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseCremona
            sage: isinstance(DatabaseCremona(), DatabaseCremona)
            True
        """

class DatabaseEllcurves(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    William Stein's database of interesting curves.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseEllcurves
        sage: bool(DatabaseEllcurves().is_present())  # optional - database_ellcurves
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseEllcurves
            sage: isinstance(DatabaseEllcurves(), DatabaseEllcurves)
            True
        """

class DatabaseGraphs(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    the graphs database.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseGraphs
        sage: bool(DatabaseGraphs().is_present())  # optional - database_graphs
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseGraphs
            sage: isinstance(DatabaseGraphs(), DatabaseGraphs)
            True
        """

class DatabaseJones(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    :ref:`John Jones's tables of number fields <spkg_database_jones_numfield>`.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseJones
        sage: bool(DatabaseJones().is_present())  # optional - database_jones_numfield
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseJones
            sage: isinstance(DatabaseJones(), DatabaseJones)
            True
        """

class DatabaseKnotInfo(PythonModule):
    """
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`package providing the KnotInfo and LinkInfo databases <spkg_database_knotinfo>`.

    The homes of these databases are the
    web-pages `KnotInfo <https://knotinfo.math.indiana.edu/>`__ and
    `LinkInfo <https://linkinfo.sitehost.iu.edu>`__.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseKnotInfo
        sage: DatabaseKnotInfo().is_present()  # optional - database_knotinfo
        FeatureTestResult('database_knotinfo', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseKnotInfo
            sage: isinstance(DatabaseKnotInfo(), DatabaseKnotInfo)
            True
        """

class DatabaseMatroids(PythonModule):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    :ref:`Yoshitake Matsumoto's Database of Matroids <spkg_matroid_database>`.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseMatroids
        sage: DatabaseMatroids().is_present()                                           # optional - matroid_database
        FeatureTestResult('matroid_database', True)

    REFERENCES:

    [Mat2012]_
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseMatroids
            sage: isinstance(DatabaseMatroids(), DatabaseMatroids)
            True
        """

class DatabaseCubicHecke(PythonModule):
    """
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`Cubic Hecke algebra database package <spkg_database_cubic_hecke>`.

    The home of this database is the
    web-page `Cubic Hecke algebra on 4 strands <http://www.lamfa.u-picardie.fr/marin/representationH4-en.html>`__
    of Ivan Marin.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseCubicHecke
        sage: DatabaseCubicHecke().is_present()  # optional - database_cubic_hecke
        FeatureTestResult('database_cubic_hecke', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseCubicHecke
            sage: isinstance(DatabaseCubicHecke(), DatabaseCubicHecke)
            True
        """

class DatabaseReflexivePolytopes(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`PALP databases of reflexive three-dimensional <spkg_polytopes_db>`
    and :ref:`four-dimensional lattice polytopes <spkg_polytopes_db_4d>`.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseReflexivePolytopes
        sage: bool(DatabaseReflexivePolytopes().is_present())                   # optional - polytopes_db
        True
        sage: bool(DatabaseReflexivePolytopes('polytopes_db_4d').is_present())  # optional - polytopes_db_4d
        True
    """
    def __init__(self, name: str = 'polytopes_db') -> None:
        """
        TESTS::

            sage: from sage.features.databases import DatabaseReflexivePolytopes
            sage: isinstance(DatabaseReflexivePolytopes(), DatabaseReflexivePolytopes)
            True
            sage: DatabaseReflexivePolytopes().filename
            'Full3d'
            sage: DatabaseReflexivePolytopes('polytopes_db_4d').filename
            'Hodge4d'
        """

def all_features(): ...
