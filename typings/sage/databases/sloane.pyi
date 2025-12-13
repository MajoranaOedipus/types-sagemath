from _typeshed import Incomplete
from sage.env import SAGE_SHARE as SAGE_SHARE
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ

class SloaneEncyclopediaClass:
    """
    A local copy of the Sloane Online Encyclopedia of Integer Sequences
    that contains only the sequence numbers and the sequences
    themselves.
    """
    __file_names__: Incomplete
    __loaded__: bool
    __loaded_names__: bool
    def __init__(self) -> None:
        """
        Initialize the database but do not load any of the data.
        """
    def __iter__(self):
        """
        Return an iterator through the encyclopedia. Elements are of the
        form [number, sequence].
        """
    def __getitem__(self, N):
        """
        Return sequence N in the encyclopedia. If sequence N does not
        exist, return ``[]``.

        INPUT:

        - ``N`` -- integer

        OUTPUT: list
        """
    def __len__(self) -> int:
        """
        Return the number of sequences in the encyclopedia.
        """
    def is_installed(self):
        """
        Check if a local copy of the encyclopedia is installed.

        EXAMPLES::

            sage: SloaneEncyclopedia.is_installed()  # optional - sloane_database
            True
        """
    def find(self, seq, maxresults: int = 30):
        """
        Return a list of all sequences which have seq as a subsequence, up
        to maxresults results. Sequences are returned in the form (number,
        list).

        INPUT:

        - ``seq`` -- list

        - ``maxresults`` -- integer

        OUTPUT: list of 2-tuples (i, v), where v is a sequence with seq as
        a subsequence.
        """
    def install(self, oeis_url: str = 'https://oeis.org/stripped.gz', names_url: str = 'https://oeis.org/names.gz', overwrite: bool = False) -> None:
        """
        Download and install the online encyclopedia, raising an IOError if
        either step fails.

        INPUT:

        - ``oeis_url`` -- string (default: ``'https://oeis.org...'``)
          The URL of the stripped.gz encyclopedia file

        - ``names_url`` -- string (default: ``'https://oeis.org...'``)
          The URL of the names.gz encyclopedia file.  If you do not want to
          download this file, set names_url=None.

        - ``overwrite`` -- boolean (default: ``False``); if the encyclopedia is
          already installed and overwrite=True, download and install the latest
          version over the installed one
        """
    def install_from_gz(self, stripped_file, names_file, overwrite: bool = False) -> None:
        """
        Install the online encyclopedia from a local stripped.gz file.

        INPUT:

        - ``stripped_file`` -- string; the name of the stripped.gz OEIS file

        - ``names_file`` -- string; the name of the names.gz OEIS file, or
          None if the user does not want it installed

        - ``overwrite`` -- boolean (default: ``False``); if the encyclopedia is
          already installed and ``overwrite=True``, install 'filename' over the
          old encyclopedia
        """
    __data__: Incomplete
    def load(self) -> None:
        """
        Load the entire encyclopedia into memory from a file. This is done
        automatically if the user tries to perform a lookup or a search.
        """
    def sequence_name(self, N):
        """
        Return the name of sequence ``N`` in the encyclopedia.

        If sequence ``N`` does not exist, return ``''``.  If the names
        database is not installed, raise an :exc:`IOError`.

        INPUT:

        - ``N`` -- integer

        OUTPUT: string

        EXAMPLES::

            sage: SloaneEncyclopedia.sequence_name(1) # optional - sloane_database
            'Number of groups of order n.'
        """
    def unload(self) -> None:
        """
        Remove the database from memory.
        """

SloaneEncyclopedia: Incomplete

def copy_gz_file(gz_source, bz_destination) -> None:
    """
    Decompress a gzipped file and install the bzipped version.

    This is used by SloaneEncyclopedia.install_from_gz to install
    several gzipped OEIS database files.

    INPUT:

    - ``gz_source`` -- string; the name of the gzipped file

    - ``bz_destination`` -- string; the name of the newly compressed file
    """
