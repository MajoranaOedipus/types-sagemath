"""
This file gathers together all the tables in Sage.

    * ConwayPolynomials() -- database of selected Conway polynomials.

    * CremonaDatabase() - Cremona's tables of elliptic curves and related data.

    * findstat -- The FindStat database (https://www.findstat.org/).

    * JonesDatabase() -- returns the John Jones table of number fields
      with bounded ramification and degree <= 6.

    * oeis -- The On-Line Encyclopedia of Integer Sequences (https://oeis.org/).

    * SloaneEncyclopedia -- Local copy of Sloane On-Line Encyclopedia of
      Integer Sequences.

    * SteinWatkinsAllData() and SteinWatkinsPrimeData() - The
      Stein-Watkins tables of elliptic curves and related data.

    * SymbolicData() -- many benchmark and testing ideals

EXAMPLES::

    sage: ConwayPolynomials()
    Frank Lübeck's database of Conway polynomials

    sage: CremonaDatabase()
    Cremona's database of elliptic curves with conductor...

    sage: JonesDatabase()
    John Jones's table of number fields with bounded ramification and degree <= 6

    sage: oeis
    The On-Line Encyclopedia of Integer Sequences (https://oeis.org/)

    sage: SymbolicData() # optional - database_symbolic_data
    SymbolicData with ... ideals
"""
from sage.databases.db_class_polynomials import HilbertClassPolynomialDatabase as HilbertClassPolynomialDatabase
from sage.databases.db_modular_polynomials import AtkinModularCorrespondenceDatabase as AtkinModularCorrespondenceDatabase, AtkinModularPolynomialDatabase as AtkinModularPolynomialDatabase, ClassicalModularPolynomialDatabase as ClassicalModularPolynomialDatabase, DedekindEtaModularCorrespondenceDatabase as DedekindEtaModularCorrespondenceDatabase, DedekindEtaModularPolynomialDatabase as DedekindEtaModularPolynomialDatabase
from sage.databases.sql_db import SQLDatabase as SQLDatabase, SQLQuery as SQLQuery

from sage.databases.conway import ConwayPolynomials as ConwayPolynomials
from sage.databases.cremona import CremonaDatabase as CremonaDatabase
from sage.databases.jones import JonesDatabase as JonesDatabase
from sage.databases.stein_watkins import (
    SteinWatkinsAllData as SteinWatkinsAllData,
    SteinWatkinsPrimeData as SteinWatkinsPrimeData,
)
from sage.databases.sloane import SloaneEncyclopedia as SloaneEncyclopedia
from sage.databases.oeis import oeis as oeis
from sage.databases.symbolic_data import SymbolicData as SymbolicData
from sage.databases.odlyzko import zeta_zeros as zeta_zeros
from sage.databases.cunningham_tables import cunningham_prime_factors as cunningham_prime_factors
from sage.databases.findstat import (
    findstat as findstat,
    findmap as findmap,
)
