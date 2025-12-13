from sage.ext.fast_callable import fast_callable as fast_callable
from sage.functions.log import exp as exp, log as log
from sage.functions.other import ceil as ceil, floor as floor
from sage.misc.flatten import flatten as flatten
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.real_mpfr import RealField as RealField
from sage.rings.semirings.non_negative_integer_semiring import NN as NN

def subexpressions_list(f, pars=None):
    """
    Construct the lists with the intermediate steps on the evaluation of the
    function.

    INPUT:

    - ``f`` -- a symbolic function of several components

    - ``pars`` -- list of the parameters that appear in the function
      this should be the symbolic constants that appear in f but are not
      arguments

    OUTPUT:

    - a list of the intermediate subexpressions that appear in the evaluation
      of f.

    - a list with the operations used to construct each of the subexpressions.
      each element of this list is a tuple, formed by a string describing the
      operation made, and the operands.

    For the trigonometric functions, some extra expressions will be added.
    These extra expressions will be used later to compute their derivatives.

    EXAMPLES::

        sage: from sage.interfaces.tides import subexpressions_list
        sage: var('x,y')
        (x, y)
        sage: f(x,y) = [x^2+y, cos(x)/log(y)]
        sage: subexpressions_list(f)
        ([x^2, x^2 + y, sin(x), cos(x), log(y), cos(x)/log(y)],
        [('mul', x, x),
        ('add', y, x^2),
        ('sin', x),
        ('cos', x),
        ('log', y),
        ('div', log(y), cos(x))])

    ::

        sage: f(a)=[cos(a), arctan(a)]
        sage: from sage.interfaces.tides import subexpressions_list
        sage: subexpressions_list(f)
        ([sin(a), cos(a), a^2, a^2 + 1, arctan(a)],
        [('sin', a), ('cos', a), ('mul', a, a), ('add', 1, a^2), ('atan', a)])

    ::

        sage: from sage.interfaces.tides import subexpressions_list
        sage: var('s,b,r')
        (s, b, r)
        sage: f(t,x,y,z)= [s*(y-x),x*(r-z)-y,x*y-b*z]
        sage: subexpressions_list(f,[s,b,r])
        ([-y,
        x - y,
        s*(x - y),
        -s*(x - y),
        -z,
        r - z,
        (r - z)*x,
        -y,
        (r - z)*x - y,
        x*y,
        b*z,
        -b*z,
        x*y - b*z],
        [('mul', -1, y),
        ('add', -y, x),
        ('mul', x - y, s),
        ('mul', -1, s*(x - y)),
        ('mul', -1, z),
        ('add', -z, r),
        ('mul', x, r - z),
        ('mul', -1, y),
        ('add', -y, (r - z)*x),
        ('mul', y, x),
        ('mul', z, b),
        ('mul', -1, b*z),
        ('add', -b*z, x*y)])

    ::

        sage: var('x, y')
        (x, y)
        sage: f(x,y)=[exp(x^2+sin(y))]
        sage: from sage.interfaces.tides import *
        sage: subexpressions_list(f)
        ([x^2, sin(y), cos(y), x^2 + sin(y), e^(x^2 + sin(y))],
        [('mul', x, x),
        ('sin', y),
        ('cos', y),
        ('add', sin(y), x^2),
        ('exp', x^2 + sin(y))])
    """
def remove_repeated(l1, l2) -> None:
    """
    Given two lists, remove the repeated elements in l1, and the elements
    in l2 that are on the same position.
    positions.

    EXAMPLES::

        sage: from sage.interfaces.tides import (subexpressions_list, remove_repeated)
        sage: f(a)=[1 + a^2, arcsin(a)]
        sage: l1, l2 = subexpressions_list(f)
        sage: l1, l2
        ([a^2, a^2 + 1, a^2, -a^2, -a^2 + 1, sqrt(-a^2 + 1), arcsin(a)],
        [('mul', a, a),
        ('add', 1, a^2),
        ('mul', a, a),
        ('mul', -1, a^2),
        ('add', 1, -a^2),
        ('pow', -a^2 + 1, 0.5),
        ('asin', a)])
        sage: remove_repeated(l1, l2)
        sage: l1, l2
        ([a^2, a^2 + 1, -a^2, -a^2 + 1, sqrt(-a^2 + 1), arcsin(a)],
        [('mul', a, a),
        ('add', 1, a^2),
        ('mul', -1, a^2),
        ('add', 1, -a^2),
        ('pow', -a^2 + 1, 0.5),
        ('asin', a)])
    """
def remove_constants(l1, l2) -> None:
    """
    Given two lists, remove the entries in the first that are real constants,
    and also the corresponding elements in the second one.

    EXAMPLES::

        sage: from sage.interfaces.tides import subexpressions_list, remove_constants
        sage: f(a)=[1+cos(7)*a]
        sage: l1, l2 = subexpressions_list(f)
        sage: l1, l2
        ([sin(7), cos(7), a*cos(7), a*cos(7) + 1],
        [('sin', 7), ('cos', 7), ('mul', cos(7), a), ('add', 1, a*cos(7))])
        sage: remove_constants(l1,l2)
        sage: l1, l2
        ([a*cos(7), a*cos(7) + 1], [('mul', cos(7), a), ('add', 1, a*cos(7))])
    """
def genfiles_mintides(integrator, driver, f, ics, initial, final, delta, tolrel: float = 1e-16, tolabs: float = 1e-16, output: str = '') -> None:
    '''
    Generate the needed files for the min_tides library.

    INPUT:

    - ``integrator`` -- the name of the integrator file

    - ``driver`` -- the name of the driver file

    - ``f`` -- the function that determines the differential equation

    - ``ics`` -- list or tuple with the initial conditions

    - ``initial`` -- the initial time for the integration

    - ``final`` -- the final time for the integration

    - ``delta`` -- the step of the output

    - ``tolrel`` -- the relative tolerance

    - ``tolabs`` -- the absolute tolerance

    - ``output`` -- the name of the file that the compiled integrator will write to

    This function creates two files, integrator and driver, that can be used
    later with the min_tides library [TIDES]_.


    TESTS::

        sage: from sage.interfaces.tides import genfiles_mintides
        sage: import os
        sage: import shutil
        sage: from sage.misc.temporary_file import tmp_dir
        sage: tempdir = tmp_dir()
        sage: intfile = os.path.join(tempdir, \'integrator.c\')
        sage: drfile = os.path.join(tempdir ,\'driver.c\')
        sage: var(\'t,x,y,X,Y\')
        (t, x, y, X, Y)
        sage: f(t,x,y,X,Y)=[X, Y, -x/(x^2+y^2)^(3/2), -y/(x^2+y^2)^(3/2)]
        sage: genfiles_mintides(intfile, drfile, f, [1,0, 0, 0.2], 0, 10, 0.1, output = \'out\')
        sage: fileint = open(intfile)
        sage: l = fileint.readlines()
        sage: fileint.close()
        sage: l[5]
        \'    #include "minc_tides.h"\\n\'
        sage: l[15]
        \'    double XX[TT+1][MO+1];\\n\'
        sage: l[25]
        \'\\n\'
        sage: l[35]
        \'\\t\\tXX[1][i+1] = XX[3][i] / (i+1.0);\\n\'
        sage: filedr = open(drfile)
        sage: l = filedr.readlines()
        sage: filedr.close()
        sage: l[6]
        \'    #include "minc_tides.h"\\n\'
        sage: l[15]
        \'    double tolrel, tolabs, tini, tend, dt;\\n\'
        sage: l[25]
        \'\\ttolrel = 9.9999999999999998e-17 ;\\n\'
        sage: shutil.rmtree(tempdir)

    Check that issue :issue:`17179` is fixed (handle expressions like `\\\\pi`)::

        sage: from sage.interfaces.tides import genfiles_mintides
        sage: import os
        sage: import shutil
        sage: from sage.misc.temporary_file import tmp_dir
        sage: tempdir = tmp_dir()
        sage: intfile = os.path.join(tempdir, \'integrator.c\')
        sage: drfile = os.path.join(tempdir ,\'driver.c\')
        sage: var(\'t,x,y,X,Y\')
        (t, x, y, X, Y)
        sage: f(t,x,y,X,Y)=[X, Y, -x/(x^2+y^2)^(3/2), -y/(x^2+y^2)^(3/2)]
        sage: genfiles_mintides(intfile, drfile, f, [pi, 0, 0, 0.2], 0, 10, 0.1, output = \'out\')
        sage: fileint = open(intfile)
        sage: l = fileint.readlines()
        sage: fileint.close()
        sage: l[30]
        \'\\t\\tXX[8][i] = pow_mc_c(XX[7],-1.5000000000000000,XX[8], i);\\n\'
        sage: filedr = open(drfile)
        sage: l = filedr.readlines()
        sage: filedr.close()
        sage: l[18]
        \'    \\tv[0] = 3.1415926535897931 ; \\n\'
        sage: shutil.rmtree(tempdir)
    '''
def genfiles_mpfr(integrator, driver, f, ics, initial, final, delta, parameters=None, parameter_values=None, dig: int = 20, tolrel: float = 1e-16, tolabs: float = 1e-16, output: str = '') -> None:
    '''
        Generate the needed files for the mpfr module of the tides library.

    INPUT:

    - ``integrator`` -- the name of the integrator file

    - ``driver`` -- the name of the driver file

    - ``f`` -- the function that determines the differential equation

    - ``ics`` -- list or tuple with the initial conditions

    - ``initial`` -- the initial time for the integration

    - ``final`` -- the final time for the integration

    - ``delta`` -- the step of the output

    - ``parameters`` -- the variables inside the function that should be treated
      as parameters

    - ``parameter_values`` -- the values of the parameters for the particular
      initial value problem

    - ``dig`` -- the number of digits of precision that will be used in the integration

    - ``tolrel`` -- the relative tolerance

    - ``tolabs`` -- the absolute tolerance

    - ``output`` -- the name of the file that the compiled integrator will write to

    This function creates two files, integrator and driver, that can be used
    later with the tides library ([TIDES]_).


    TESTS::

        sage: from tempfile import mkdtemp
        sage: from sage.interfaces.tides import genfiles_mpfr
        sage: import os
        sage: import shutil
        sage: from sage.misc.temporary_file import tmp_dir
        sage: tempdir = tmp_dir()
        sage: intfile = os.path.join(tempdir, \'integrator.c\')
        sage: drfile = os.path.join(tempdir ,\'driver.c\')
        sage: var(\'t,x,y,X,Y\')
        (t, x, y, X, Y)
        sage: f(t,x,y,X,Y)=[X, Y, -x/(x^2+y^2)^(3/2), -y/(x^2+y^2)^(3/2)]
        sage: genfiles_mpfr(intfile, drfile, f, [1,0, 0, 0.2], 0, 10, 0.1, output = \'out\', dig = 50)
        sage: fileint = open(intfile)
        sage: l = fileint.readlines()
        sage: fileint.close()
        sage: l[5]
        \'    #include "mp_tides.h"\\n\'
        sage: l[15]
        \'\\tstatic int PARAMETERS = 0;\\n\'
        sage: l[25]
        \'\\t\\tmpfrts_var_t(itd, link[5], var[3], i);\\n\'
        sage: l[30]
        \'\\t\\tmpfrts_pow_t_c(itd, link[2], "-1.500000000000000000000000000000000000000000000000000", link[3], i);\\n\'
        sage: l[35]
        \'\\n\'
        sage: l[36]
        \'    }\\n\'
        sage: l[37]
        \'    write_mp_solution();\\n\'
        sage: filedr = open(drfile)
        sage: l = filedr.readlines()
        sage: filedr.close()
        sage: l[6]
        \'    #include "mpfr.h"\\n\'
        sage: l[16]
        \'    int nfun = 0;\\n\'
        sage: l[26]
        \'\\tmpfr_set_str(v[2], "0.000000000000000000000000000000000000000000000000000", 10, TIDES_RND);\\n\'
        sage: l[30]
        \'\\tmpfr_init2(tolabs, TIDES_PREC); \\n\'
        sage: l[34]
        \'\\tmpfr_init2(tini, TIDES_PREC); \\n\'
        sage: l[40]
        \'\\tmp_tides_delta(function_iteration, NULL, nvar, npar, nfun, v, p, tini, dt, nipt, tolrel, tolabs, NULL, fd);\\n\'
        sage: shutil.rmtree(tempdir)

    Check that issue :issue:`17179` is fixed (handle expressions like `\\\\pi`)::

        sage: from sage.interfaces.tides import genfiles_mpfr
        sage: import os
        sage: import shutil
        sage: from sage.misc.temporary_file import tmp_dir
        sage: tempdir = tmp_dir()
        sage: intfile = os.path.join(tempdir, \'integrator.c\')
        sage: drfile = os.path.join(tempdir ,\'driver.c\')
        sage: var(\'t,x,y,X,Y\')
        (t, x, y, X, Y)
        sage: f(t,x,y,X,Y)=[X, Y, -x/(x^2+y^2)^(3/2), -y/(x^2+y^2)^(3/2)]
        sage: genfiles_mpfr(intfile, drfile, f, [pi, 0, 0, 0.2], 0, 10, 0.1, output = \'out\', dig = 50)
        sage: fileint = open(intfile)
        sage: l = fileint.readlines()
        sage: fileint.close()
        sage: l[30]
        \'\\t\\tmpfrts_pow_t_c(itd, link[2], "-1.500000000000000000000000000000000000000000000000000", link[3], i);\\n\'
        sage: filedr = open(drfile)
        sage: l = filedr.readlines()
        sage: filedr.close()
        sage: l[24]
        \'\\tmpfr_set_str(v[0], "3.141592653589793238462643383279502884197169399375101", 10, TIDES_RND);\\n\'
        sage: shutil.rmtree(tempdir)
    '''
