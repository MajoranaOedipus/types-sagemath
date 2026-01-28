from __future__ import annotations
from mpmath.calculus.approximation import chebyfit
from mpmath.calculus.approximation import fourier
from mpmath.calculus.approximation import fourierval
from mpmath.calculus.differentiation import diff
from mpmath.calculus.differentiation import difference
from mpmath.calculus.differentiation import differint
from mpmath.calculus.differentiation import diffs
from mpmath.calculus.differentiation import diffs_exp
from mpmath.calculus.differentiation import diffs_prod
from mpmath.calculus.differentiation import diffun
from mpmath.calculus.differentiation import pade
from mpmath.calculus.differentiation import taylor
from mpmath.calculus.extrapolation import cohen_alt
from mpmath.calculus.extrapolation import levin
from mpmath.calculus.extrapolation import limit
from mpmath.calculus.extrapolation import nprod
from mpmath.calculus.extrapolation import nsum
from mpmath.calculus.extrapolation import richardson
from mpmath.calculus.extrapolation import shanks
from mpmath.calculus.extrapolation import sumap
from mpmath.calculus.extrapolation import sumem
from mpmath.calculus.inverselaplace.LaplaceTransformInversionMethods import invertlaplace
from mpmath.calculus.inverselaplace.LaplaceTransformInversionMethods import invlapdehoog
from mpmath.calculus.inverselaplace.LaplaceTransformInversionMethods import invlapstehfest
from mpmath.calculus.inverselaplace.LaplaceTransformInversionMethods import invlaptalbot
from mpmath.calculus.odes import odefun
from mpmath.calculus.optimization import findroot
from mpmath.calculus.optimization import jacobian
from mpmath.calculus.optimization import multiplicity
from mpmath.calculus.polynomials import polyroots
from mpmath.calculus.polynomials import polyval
from mpmath.calculus.quadrature.QuadratureMethods import quad
from mpmath.calculus.quadrature.QuadratureMethods import quadgl
from mpmath.calculus.quadrature.QuadratureMethods import quadosc
from mpmath.calculus.quadrature.QuadratureMethods import quadsubdiv
from mpmath.calculus.quadrature.QuadratureMethods import quadts
from mpmath.ctx_base.StandardBaseContext import almosteq
from mpmath.ctx_base.StandardBaseContext import arange
from mpmath.ctx_base.StandardBaseContext import chop
from mpmath.ctx_base.StandardBaseContext import linspace
from mpmath.ctx_base.StandardBaseContext import maxcalls
from mpmath.ctx_base.StandardBaseContext import memoize
from mpmath.ctx_base.StandardBaseContext import nprint
from mpmath.ctx_base.StandardBaseContext import power
from mpmath.ctx_fp import FPContext
from mpmath.ctx_iv import MPIntervalContext
from mpmath.ctx_iv.MPIntervalContext import _mpi as mpi
from mpmath.ctx_mp import MPContext
from mpmath.ctx_mp.MPContext import absmax
from mpmath.ctx_mp.MPContext import absmin
from mpmath.ctx_mp.MPContext import atan2
from mpmath.ctx_mp.MPContext import autoprec
from mpmath.ctx_mp.MPContext import bernoulli
from mpmath.ctx_mp.MPContext import cos_sin
from mpmath.ctx_mp.MPContext import cospi_sinpi
from mpmath.ctx_mp.MPContext import extradps
from mpmath.ctx_mp.MPContext import extraprec
from mpmath.ctx_mp.MPContext import fadd
from mpmath.ctx_mp.MPContext import fdiv
from mpmath.ctx_mp.MPContext import fmul
from mpmath.ctx_mp.MPContext import fneg
from mpmath.ctx_mp.MPContext import fprod
from mpmath.ctx_mp.MPContext import fraction
from mpmath.ctx_mp.MPContext import frexp
from mpmath.ctx_mp.MPContext import fsub
from mpmath.ctx_mp.MPContext import hypot
from mpmath.ctx_mp.MPContext import isfinite
from mpmath.ctx_mp.MPContext import isnan
from mpmath.ctx_mp.MPContext import ldexp
from mpmath.ctx_mp.MPContext import nint_distance
from mpmath.ctx_mp.MPContext import nstr
from mpmath.ctx_mp.MPContext import psi as polygamma
from mpmath.ctx_mp.MPContext import psi
from mpmath.ctx_mp.MPContext import rand
from mpmath.ctx_mp.MPContext import workdps
from mpmath.ctx_mp.MPContext import workprec
from mpmath.ctx_mp_python.PythonMPContext import convert as mpmathify
from mpmath.ctx_mp_python.PythonMPContext import convert
from mpmath.ctx_mp_python.PythonMPContext import fdot
from mpmath.ctx_mp_python.PythonMPContext import fsum
from mpmath.ctx_mp_python.PythonMPContext import isinf
from mpmath.ctx_mp_python.PythonMPContext import isint
from mpmath.ctx_mp_python.PythonMPContext import isnormal
from mpmath.ctx_mp_python.PythonMPContext import mag
from mpmath.ctx_mp_python.PythonMPContext import make_mpc
from mpmath.ctx_mp_python.PythonMPContext import make_mpf
from mpmath.ctx_mp_python import mpc
from mpmath.ctx_mp_python import mpf
from mpmath.functions.bessel import airyai
from mpmath.functions.bessel import airyaizero
from mpmath.functions.bessel import airybi
from mpmath.functions.bessel import airybizero
from mpmath.functions.bessel import angerj
from mpmath.functions.bessel import bei
from mpmath.functions.bessel import ber
from mpmath.functions.bessel import besseli
from mpmath.functions.bessel import besselj
from mpmath.functions.bessel import besseljzero
from mpmath.functions.bessel import besselyzero
from mpmath.functions.bessel import hyperu
from mpmath.functions.bessel import j0
from mpmath.functions.bessel import j1
from mpmath.functions.bessel import kei
from mpmath.functions.bessel import ker
from mpmath.functions.bessel import lommels1
from mpmath.functions.bessel import lommels2
from mpmath.functions.bessel import scorergi
from mpmath.functions.bessel import scorerhi
from mpmath.functions.bessel import struveh
from mpmath.functions.bessel import struvel
from mpmath.functions.bessel import webere
from mpmath.functions.elliptic import ellipfun
from mpmath.functions.elliptic import elliprc
from mpmath.functions.elliptic import elliprd
from mpmath.functions.elliptic import elliprf
from mpmath.functions.elliptic import elliprg
from mpmath.functions.elliptic import elliprj
from mpmath.functions.expintegrals import ci
from mpmath.functions.expintegrals import erf
from mpmath.functions.expintegrals import erfc
from mpmath.functions.expintegrals import gammainc
from mpmath.functions.expintegrals import si
from mpmath.functions.factorials import beta
from mpmath.functions.factorials import binomial
from mpmath.functions.factorials import ff
from mpmath.functions.factorials import gammaprod
from mpmath.functions.factorials import rf
from mpmath.functions.factorials import superfac
from mpmath.functions.functions import agm
from mpmath.functions.functions import arg as phase
from mpmath.functions.functions import arg
from mpmath.functions.functions import conj
from mpmath.functions.functions import degrees
from mpmath.functions.functions import fabs
from mpmath.functions.functions import fmod
from mpmath.functions.functions import im
from mpmath.functions.functions import lambertw
from mpmath.functions.functions import log
from mpmath.functions.functions import log10
from mpmath.functions.functions import mangoldt
from mpmath.functions.functions import polar
from mpmath.functions.functions import radians
from mpmath.functions.functions import re
from mpmath.functions.functions import root as nthroot
from mpmath.functions.functions import root
from mpmath.functions.functions import sign
from mpmath.functions.functions import stirling1
from mpmath.functions.functions import stirling2
from mpmath.functions.functions import unitroots
from mpmath.functions.hypergeometric import appellf2
from mpmath.functions.hypergeometric import appellf3
from mpmath.functions.hypergeometric import appellf4
from mpmath.functions.hypergeometric import bihyper
from mpmath.functions.hypergeometric import hyp0f1
from mpmath.functions.hypergeometric import hyp1f1
from mpmath.functions.hypergeometric import hyp1f2
from mpmath.functions.hypergeometric import hyp2f0
from mpmath.functions.hypergeometric import hyp2f1
from mpmath.functions.hypergeometric import hyp2f2
from mpmath.functions.hypergeometric import hyp2f3
from mpmath.functions.hypergeometric import hyp3f2
from mpmath.functions.hypergeometric import hyper
from mpmath.functions.hypergeometric import hyper2d
from mpmath.functions.hypergeometric import hypercomb
from mpmath.functions.hypergeometric import meijerg
from mpmath.functions.orthogonal import hermite
from mpmath.functions.orthogonal import legenp
from mpmath.functions.orthogonal import legenq
from mpmath.functions.orthogonal import pcfd
from mpmath.functions.orthogonal import pcfu
from mpmath.functions.orthogonal import pcfv
from mpmath.functions.orthogonal import pcfw
from mpmath.functions.orthogonal import spherharm
from mpmath.functions.qfunctions import qhyper
from mpmath.functions.qfunctions import qp
from mpmath.functions.theta import jtheta
from mpmath.functions.zeta import altzeta
from mpmath.functions.zeta import dirichlet
from mpmath.functions.zeta import eulernum
from mpmath.functions.zeta import primepi
from mpmath.functions.zeta import secondzeta
from mpmath.functions.zeta import stieltjes
from mpmath.functions.zeta import zeta
from mpmath.functions.zeta import zeta as hurwitz
from mpmath.functions.zetazeros import nzeros
from mpmath.functions.zetazeros import zetazero
from mpmath.identification import findpoly
from mpmath.identification import identify
from mpmath.identification import pslq
from mpmath.libmp.gammazeta import bernfrac
from mpmath.matrices.calculus.MatrixCalculusMethods import cosm
from mpmath.matrices.calculus.MatrixCalculusMethods import expm
from mpmath.matrices.calculus.MatrixCalculusMethods import logm
from mpmath.matrices.calculus.MatrixCalculusMethods import powm
from mpmath.matrices.calculus.MatrixCalculusMethods import sinm
from mpmath.matrices.calculus.MatrixCalculusMethods import sqrtm
from mpmath.matrices.eigen import eig
from mpmath.matrices.eigen import eig_sort
from mpmath.matrices.eigen import hessenberg
from mpmath.matrices.eigen import schur
from mpmath.matrices.eigen_symmetric import eigh
from mpmath.matrices.eigen_symmetric import eighe
from mpmath.matrices.eigen_symmetric import eigsy
from mpmath.matrices.eigen_symmetric import gauss_quadrature
from mpmath.matrices.eigen_symmetric import svd
from mpmath.matrices.eigen_symmetric import svd_c
from mpmath.matrices.eigen_symmetric import svd_r
from mpmath.matrices.linalg.LinearAlgebraMethods import cholesky
from mpmath.matrices.linalg.LinearAlgebraMethods import cholesky_solve
from mpmath.matrices.linalg.LinearAlgebraMethods import cond
from mpmath.matrices.linalg.LinearAlgebraMethods import det
from mpmath.matrices.linalg.LinearAlgebraMethods import inverse
from mpmath.matrices.linalg.LinearAlgebraMethods import lu
from mpmath.matrices.linalg.LinearAlgebraMethods import lu_solve
from mpmath.matrices.linalg.LinearAlgebraMethods import qr
from mpmath.matrices.linalg.LinearAlgebraMethods import qr_solve
from mpmath.matrices.linalg.LinearAlgebraMethods import residual
from mpmath.matrices.linalg.LinearAlgebraMethods import unitvector
from mpmath.matrices.matrices.MatrixMethods import diag
from mpmath.matrices.matrices.MatrixMethods import extend
from mpmath.matrices.matrices.MatrixMethods import eye
from mpmath.matrices.matrices.MatrixMethods import hilbert
from mpmath.matrices.matrices.MatrixMethods import mnorm
from mpmath.matrices.matrices.MatrixMethods import norm
from mpmath.matrices.matrices.MatrixMethods import ones
from mpmath.matrices.matrices.MatrixMethods import randmatrix
from mpmath.matrices.matrices.MatrixMethods import swap_row
from mpmath.matrices.matrices.MatrixMethods import zeros
from mpmath.matrices.matrices import matrix
from mpmath.usertools import monitor
from mpmath.usertools import timing
from mpmath.visualization import cplot
from mpmath.visualization import plot
from mpmath.visualization import splot
from . import calculus
from . import ctx_base
from . import ctx_fp
from . import ctx_iv
from . import ctx_mp
from . import ctx_mp_python
from . import function_docs
from . import functions
from . import identification
from . import libmp
from . import math2
from . import matrices
from . import rational
from . import usertools
from . import visualization
__all__: list[str] = ['FPContext', 'MPContext', 'MPIntervalContext', 'absmax', 'absmin', 'agm', 'airyai', 'airyaizero', 'airybi', 'airybizero', 'almosteq', 'altzeta', 'angerj', 'apery', 'appellf2', 'appellf3', 'appellf4', 'arange', 'arg', 'atan2', 'autoprec', 'bei', 'ber', 'bernfrac', 'bernoulli', 'besseli', 'besselj', 'besseljzero', 'besselyzero', 'beta', 'bihyper', 'binomial', 'calculus', 'catalan', 'chebyfit', 'cholesky', 'cholesky_solve', 'chop', 'ci', 'cohen_alt', 'cond', 'conj', 'convert', 'cos_sin', 'cosm', 'cospi_sinpi', 'cplot', 'ctx_base', 'ctx_fp', 'ctx_iv', 'ctx_mp', 'ctx_mp_python', 'degree', 'degrees', 'det', 'diag', 'diff', 'difference', 'differint', 'diffs', 'diffs_exp', 'diffs_prod', 'diffun', 'dirichlet', 'doctests', 'e', 'eig', 'eig_sort', 'eigh', 'eighe', 'eigsy', 'ellipfun', 'elliprc', 'elliprd', 'elliprf', 'elliprg', 'elliprj', 'eps', 'erf', 'erfc', 'euler', 'eulernum', 'expm', 'extend', 'extradps', 'extraprec', 'eye', 'fabs', 'fadd', 'fdiv', 'fdot', 'ff', 'findpoly', 'findroot', 'fmod', 'fmul', 'fneg', 'fourier', 'fourierval', 'fp', 'fprod', 'fraction', 'frexp', 'fsub', 'fsum', 'function_docs', 'functions', 'gammainc', 'gammaprod', 'gauss_quadrature', 'glaisher', 'hermite', 'hessenberg', 'hilbert', 'hurwitz', 'hyp0f1', 'hyp1f1', 'hyp1f2', 'hyp2f0', 'hyp2f1', 'hyp2f2', 'hyp2f3', 'hyp3f2', 'hyper', 'hyper2d', 'hypercomb', 'hyperu', 'hypot', 'identification', 'identify', 'im', 'inf', 'inverse', 'invertlaplace', 'invlapdehoog', 'invlapstehfest', 'invlaptalbot', 'isfinite', 'isinf', 'isint', 'isnan', 'isnormal', 'iv', 'j', 'j0', 'j1', 'jacobian', 'jtheta', 'kei', 'ker', 'khinchin', 'lambertw', 'ldexp', 'legenp', 'legenq', 'levin', 'libmp', 'limit', 'linspace', 'ln10', 'ln2', 'log', 'log10', 'logm', 'lommels1', 'lommels2', 'lu', 'lu_solve', 'mag', 'make_mpc', 'make_mpf', 'mangoldt', 'math2', 'matrices', 'matrix', 'maxcalls', 'meijerg', 'memoize', 'mertens', 'mnorm', 'monitor', 'mp', 'mpc', 'mpf', 'mpi', 'mpmathify', 'multiplicity', 'nan', 'ninf', 'nint_distance', 'norm', 'nprint', 'nprod', 'nstr', 'nsum', 'nthroot', 'nzeros', 'odefun', 'ones', 'pade', 'pcfd', 'pcfu', 'pcfv', 'pcfw', 'phase', 'phi', 'pi', 'plot', 'polar', 'polygamma', 'polyroots', 'polyval', 'power', 'powm', 'primepi', 'psi', 'pslq', 'qhyper', 'qp', 'qr', 'qr_solve', 'quad', 'quadgl', 'quadosc', 'quadsubdiv', 'quadts', 'radians', 'rand', 'randmatrix', 'rational', 're', 'residual', 'rf', 'richardson', 'root', 'runtests', 'schur', 'scorergi', 'scorerhi', 'secondzeta', 'shanks', 'si', 'sign', 'sinm', 'spherharm', 'splot', 'sqrtm', 'stieltjes', 'stirling1', 'stirling2', 'struveh', 'struvel', 'sumap', 'sumem', 'superfac', 'svd', 'svd_c', 'svd_r', 'swap_row', 'taylor', 'timing', 'twinprime', 'unitroots', 'unitvector', 'usertools', 'visualization', 'webere', 'workdps', 'workprec', 'zeros', 'zeta', 'zetazero']
def doctests(filter = list()):
    ...
def runtests():
    """
    
    Run all mpmath tests and print output.
    """
__version__: str = '1.3.0'
apery: ctx_mp_python.constant  # value = <Apery's constant: 1.20206~>
catalan: ctx_mp_python.constant  # value = <Catalan's constant: 0.915966~>
degree: ctx_mp_python.constant  # value = <1 deg = pi / 180: 0.0174533~>
e: ctx_mp_python.constant  # value = <e = exp(1): 2.71828~>
eps: ctx_mp_python.constant  # value = <epsilon of working precision: 2.22045e-16~>
euler: ctx_mp_python.constant  # value = <Euler's constant: 0.577216~>
fp: ctx_fp.FPContext  # value = <mpmath.ctx_fp.FPContext object>
glaisher: ctx_mp_python.constant  # value = <Glaisher's constant: 1.28243~>
inf: ctx_mp_python.mpf  # value = mpf('+inf')
iv: ctx_iv.MPIntervalContext  # value = <mpmath.ctx_iv.MPIntervalContext object>
j: ctx_mp_python.mpc  # value = mpc(real='0.0', imag='1.0')
khinchin: ctx_mp_python.constant  # value = <Khinchin's constant: 2.68545~>
ln10: ctx_mp_python.constant  # value = <ln(10): 2.30259~>
ln2: ctx_mp_python.constant  # value = <ln(2): 0.693147~>
mertens: ctx_mp_python.constant  # value = <Mertens' constant: 0.261497~>
mp: ctx_mp.MPContext  # value = <mpmath.ctx_mp.MPContext object>
nan: ctx_mp_python.mpf  # value = mpf('nan')
ninf: ctx_mp_python.mpf  # value = mpf('-inf')
phi: ctx_mp_python.constant  # value = <Golden ratio phi: 1.61803~>
pi: ctx_mp_python.constant  # value = <pi: 3.14159~>
twinprime: ctx_mp_python.constant  # value = <Twin prime constant: 0.660162~>
_ctx_mp = ctx_mp
