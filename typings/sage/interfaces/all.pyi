from sage.interfaces.maxima import maxima as maxima
from sage.interfaces.sage0 import (
    sage0 as sage0,
    sage0_version as sage0_version,
    Sage as Sage,
)
from sage.interfaces.axiom import Axiom as Axiom, axiom as axiom
from sage.interfaces.ecm import ECM as ECM, ecm as ecm
from sage.interfaces.four_ti_2 import four_ti_2 as four_ti_2
from sage.interfaces.fricas import FriCAS as FriCAS, fricas as fricas
from sage.interfaces.frobby import frobby as frobby
from sage.interfaces.gap import (
    gap as gap,
    gap_reset_workspace as gap_reset_workspace,
    Gap as Gap,
)
from sage.interfaces.gap3 import (
    gap3 as gap3,
    gap3_version as gap3_version,
    Gap3 as Gap3,
)
from sage.interfaces.genus2reduction import (
    genus2reduction as genus2reduction,
    Genus2reduction as Genus2reduction,
)
from sage.interfaces.gfan import gfan as gfan, Gfan as Gfan
from sage.interfaces.giac import giac as giac, Giac as Giac
from sage.interfaces.gnuplot import gnuplot as gnuplot
from sage.interfaces.gp import gp as gp, gp_version as gp_version, Gp as Gp
from sage.interfaces.kash import (
    kash as kash,
    kash_version as kash_version,
    Kash as Kash,
)
# from sage.interfaces.khoca import khoca as khoca, Khoca as Khoca
from sage.interfaces.lie import lie as lie, LiE as LiE
from sage.interfaces.lisp import lisp as lisp, Lisp as Lisp
from sage.interfaces.macaulay2 import macaulay2 as macaulay2, Macaulay2 as Macaulay2
from sage.interfaces.magma import magma as magma, Magma as Magma
from sage.interfaces.magma_free import magma_free as magma_free
from sage.interfaces.maple import maple as maple, Maple as Maple
from sage.interfaces.mathematica import (
    mathematica as mathematica,
    Mathematica as Mathematica,
)
from sage.interfaces.mathics import mathics as mathics, Mathics as Mathics
from sage.interfaces.matlab import (
    matlab as matlab,
    matlab_version as matlab_version,
    Matlab as Matlab,
)
from sage.interfaces.mupad import mupad as mupad, Mupad as Mupad  # NOT functional yet
from sage.interfaces.mwrank import mwrank as mwrank, Mwrank as Mwrank
from sage.interfaces.octave import octave as octave, Octave as Octave
from sage.interfaces.polymake import polymake as polymake
from sage.interfaces.povray import povray as povray
from sage.interfaces.psage import PSage as PSage
from sage.interfaces.qepcad import (
    qepcad as qepcad,
    qepcad_version as qepcad_version,
    qepcad_formula as qepcad_formula,
)
from sage.interfaces.r import r as r, R as R, r_version as r_version
from sage.interfaces.read_data import read_data as read_data
from sage.interfaces.regina import regina as regina, Regina as Regina
from sage.interfaces.scilab import scilab as scilab
from sage.interfaces.singular import (
    singular as singular,
    singular_version as singular_version,
    Singular as Singular,
)
from sage.interfaces.tachyon import tachyon_rt as tachyon_rt

interfaces = [
    "gap",
    "gap3",
    "giac",
    "gp",
    "mathematica",
    "gnuplot",
    "kash",
    "magma",
    "macaulay2",
    "maple",
    "maxima",
    "mathematica",
    "mwrank",
    "octave",
    "r",
    "singular",
    "sage0",
    "sage",
]
