from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.rings.cc import CC as CC
from sage.rings.integer import Integer as Integer
from sage.rings.real_mpfr import RR as RR

def get_solution_dicts(output_file_contents, input_ring, get_failures: bool = True):
    """
    Return a list of dictionaries of variable:value (key:value)
    pairs.  Only used internally; see the solution_dict function in
    the PHC_Object class definition for details.

    INPUT:

    - ``output_file_contents`` -- phc solution output as a string
    - ``input_ring`` -- a PolynomialRing that variable names can be coerced into

    OUTPUT: list of dictionaries of solutions

    EXAMPLES::

        sage: from sage.interfaces.phc import *
        sage: R2.<x1,x2> = PolynomialRing(QQ,2)
        sage: test_sys = [(x1-1)^5-x2, (x2-1)^5-1]
        sage: sol = phc.blackbox(test_sys, R2)             # optional -- phc
        sage: test = get_solution_dicts(sol.output_file_contents,R2)  # optional -- phc
        sage: str(sum([q[x1].real() for q in test]))[0:4]  # optional -- phc
        '25.0'
    """
def get_classified_solution_dicts(output_file_contents, input_ring, get_failures: bool = True):
    """
    Return a dictionary of lists of dictionaries of variable:value (key:value)
    pairs.  Only used internally; see the classified_solution_dict function in
    the PHC_Object class definition for details.

    INPUT:

    - ``output_file_contents`` -- phc solution output as a string
    - ``input_ring`` -- a PolynomialRing that variable names can be coerced into

    OUTPUT: a dictionary of lists if dictionaries of solutions, classifies by type

    EXAMPLES::

        sage: from sage.interfaces.phc import *
        sage: R2.<x1,x2> = PolynomialRing(QQ,2)
        sage: test_sys = [(x1-2)^5-x2, (x2-1)^5-1]
        sage: sol = phc.blackbox(test_sys, R2)          # optional -- phc
        sage: sol_classes = get_classified_solution_dicts(sol.output_file_contents,R2)  # optional -- phc
        sage: len(sol_classes['real'])            # optional -- phc
        1
    """
def get_variable_list(output_file_contents):
    """
    Return the variables, as strings, in the order in which PHCpack has processed them.

    EXAMPLES::

        sage: from sage.interfaces.phc import *
        sage: R2.<x1,x2> = PolynomialRing(QQ,2)
        sage: test_sys = [(x1-2)^5-x2, (x2-1)^5-1]
        sage: sol = phc.blackbox(test_sys, R2)             # optional -- phc
        sage: get_variable_list(sol.output_file_contents)  # optional -- phc
        ['x1', 'x2']
    """

class PHC_Object:
    output_file_contents: Incomplete
    input_ring: Incomplete
    def __init__(self, output_file_contents, input_ring) -> None:
        """
        A container for data from the PHCpack program - lists of float
        solutions, etc.  Currently the file contents are kept as a string;
        for really large outputs this would be bad.

        INPUT:

        - ``output_file_contents`` -- the string output of PHCpack
        - ``input_ring`` -- for coercion of the variables into the desired ring

        EXAMPLES::

            sage: from sage.interfaces.phc import phc
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [(x-1)^2+(y-1)-1, x^2+y^2-1]
            sage: sol = phc.blackbox(start_sys, R2)  # optional -- phc
            sage: str(sum([x[0] for x in sol.solutions()]).real())[0:3]  # optional -- phc
            '2.0'
        """
    def save_as_start(self, start_filename=None, sol_filter: str = ''):
        """
        Save a solution as a phcpack start file.  The usual output is
        just as a string, but it can be saved to a file as well.  Even
        if saved to a file, it still returns the output string.

        EXAMPLES::

            sage: from sage.interfaces.phc import phc
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [x^3-y^2,y^5-1]
            sage: sol = phc.blackbox(start_sys, R2)  # optional -- phc
            sage: start_save = sol.save_as_start()   # optional -- phc
            sage: end_sys = [x^7-2,y^5-x^2]          # optional -- phc
            sage: sol = phc.start_from(start_save, end_sys, R2)  # optional -- phc
            sage: len(sol.solutions())               # optional -- phc
            15
        """
    def classified_solution_dicts(self):
        """
        Return a dictionary of lists of dictionaries of solutions.

        Its not as crazy as it sounds; the keys are the types of solutions as
        classified by phcpack: regular vs. singular, complex vs. real

        INPUT:

        - None

        OUTPUT: a dictionary of lists of dictionaries of solutions

        EXAMPLES::

            sage: from sage.interfaces.phc import phc
            sage: R.<x,y> = PolynomialRing(CC,2)
            sage: p_sys = [x^10-y,y^2-1]
            sage: sol = phc.blackbox(p_sys,R)         # optional -- phc
            sage: classifieds = sol.classified_solution_dicts()          # optional -- phc
            sage: str(sum([q[y] for q in classifieds['real']]))[0:3]     # optional -- phc
            '2.0'
        """
    def solution_dicts(self, get_failures: bool = False):
        """
        Return a list of solutions in dictionary form: variable:value.

        INPUT:

        - ``self`` -- for access to self_out_file_contents, the string
          of raw PHCpack output
        - ``get_failures`` -- boolean (default: ``False``); the default
          is to not process failed homotopies.  These either lie on
          positive-dimensional components or at infinity.

        OUTPUT:

        - solution_dicts: a list of dictionaries.  Each dictionary
          element is of the form variable:value, where the variable
          is an element of the input_ring, and the value is in
          ComplexField.

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: fs = [x^2-1,y^2-x,z^2-y]
            sage: sol = phc.blackbox(fs,R)          # optional -- phc
            sage: s_list = sol.solution_dicts()     # optional -- phc
            sage: s_list.sort()                     # optional -- phc
            sage: s_list[0]                         # optional -- phc
            {y: 1.00000000000000, z: -1.00000000000000, x: 1.00000000000000}
        """
    def solutions(self, get_failures: bool = False):
        """
        Return a list of solutions in the ComplexField.

        Use the variable_list function to get the order of variables used by
        PHCpack, which is usually different than the term order of the
        input_ring.

        INPUT:

        - ``self`` -- for access to self_out_file_contents, the string
          of raw PHCpack output
        - ``get_failures`` -- boolean (default: ``False``); the default
          is to not process failed homotopies.  These either lie on
          positive-dimensional components or at infinity.

        OUTPUT: solutions: a list of lists of ComplexField-valued solutions

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x1,x2> = PolynomialRing(QQ,2)
            sage: test_sys = [x1^5-x1*x2^2-1, x2^5-x1*x2-1]
            sage: sol = phc.blackbox(test_sys, R2)          # optional -- phc
            sage: len(sol.solutions())                      # optional -- phc
            25
        """
    def variable_list(self):
        """
        Return the variables, as strings, in the order in which
        PHCpack has processed them.

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x1,x2> = PolynomialRing(QQ,2)
            sage: test_sys = [x1^5-x1*x2^2-1, x2^5-x1*x2-1]
            sage: sol = phc.blackbox(test_sys, R2)          # optional -- phc
            sage: sol.variable_list()                       # optional -- phc
            ['x1', 'x2']
        """

class PHC:
    """
    A class to interface with PHCpack, for computing numerical
    homotopies and root counts.

    EXAMPLES::

        sage: from sage.interfaces.phc import phc
        sage: R.<x,y> = PolynomialRing(CDF,2)
        sage: testsys = [x^2 + 1, x*y - 1]
        sage: phc.mixed_volume(testsys)        # optional -- phc
        2
        sage: v = phc.blackbox(testsys, R)     # optional -- phc
        sage: sols = v.solutions()             # optional -- phc
        sage: sols.sort()                      # optional -- phc
        sage: sols                             # optional -- phc
        [[-1.00000000000000*I, 1.00000000000000*I], [1.00000000000000*I, -1.00000000000000*I]]
        sage: sol_dict = v.solution_dicts()    # optional -- phc
        sage: x_sols_from_dict = [d[x] for d in sol_dict]    # optional -- phc
        sage: x_sols_from_dict.sort(); x_sols_from_dict      # optional -- phc
        [-1.00000000000000*I, 1.00000000000000*I]
        sage: residuals = [[test_equation.change_ring(CDF).subs(sol) for test_equation in testsys] for sol in v.solution_dicts()]  # optional -- phc
        sage: residuals                        # optional -- phc
        [[0, 0], [0, 0]]
    """
    def path_track(self, start_sys, end_sys, input_ring, c_skew: float = 0.001, saved_start=None):
        """
        This function computes homotopy paths between the solutions of
        ``start_sys`` and ``end_sys``.

        INPUT:

        - ``start_sys`` -- a square polynomial system, given as a list of
          polynomials
        - ``end_sys`` -- same type as ``start_sys``
        - ``input_ring`` -- for coercion of the variables into the desired ring
        - ``c_skew`` -- (optional) the imaginary part of homotopy multiplier;
          nonzero values are often necessary to avoid intermediate path
          collisions
        - ``saved_start`` -- (optional) a phc output file; if not given, start
          system solutions are computed via the ``phc.blackbox`` function

        OUTPUT: list of paths as dictionaries, with the keys variables and
        t-values on the path

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [x^6-y^2,y^5-1]
            sage: sol = phc.blackbox(start_sys, R2)        # optional -- phc
            sage: start_save = sol.save_as_start()         # optional -- phc
            sage: end_sys = [x^7-2,y^5-x^2]                # optional -- phc
            sage: sol_paths = phc.path_track(start_sys, end_sys, R2, saved_start = start_save)  # optional -- phc
            sage: len(sol_paths)        # optional -- phc
            30
        """
    def plot_paths_2d(self, start_sys, end_sys, input_ring, c_skew: float = 0.001, endpoints: bool = True, saved_start=None, rand_colors: bool = False):
        """
        Return a graphics object of solution paths in the complex plane.

        INPUT:

        - ``start_sys`` -- a square polynomial system, given as a list of
          polynomials
        - ``end_sys`` -- same type as start_sys
        - ``input_ring`` -- for coercion of the variables into the desired ring
        - ``c_skew`` -- (optional) the imaginary part of homotopy multiplier;
          nonzero values are often necessary to avoid intermediate path
          collisions
        - ``endpoints`` -- (optional) whether to draw in the ends of paths as
          points
        - ``saved_start`` -- (optional) a phc output file; if not given, start
          system solutions are computed via the ``phc.blackbox`` function

        OUTPUT: lines and points of solution paths

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: from sage.structure.sage_object import SageObject
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [x^5-y^2,y^5-1]
            sage: sol = phc.blackbox(start_sys, R2)    # optional -- phc
            sage: start_save = sol.save_as_start()     # optional -- phc
            sage: end_sys = [x^5-25,y^5-x^2]           # optional -- phc
            sage: testing = phc.plot_paths_2d(start_sys, end_sys, R2)  # optional -- phc
            sage: type(testing)                        # optional -- phc (normally use plot here)
            <class 'sage.plot.graphics.Graphics'>
        """
    def mixed_volume(self, polys, verbose: bool = False):
        """
        Compute the mixed volume of the polynomial system given by the input polys.

        INPUT:

        - ``polys`` -- list of multivariate polynomials (elements of a multivariate
          polynomial ring).
        - ``verbose`` -- print lots of verbose information about what this function does

        OUTPUT: the mixed volume

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x,y,z> = PolynomialRing(QQ,3)
            sage: test_sys = [(x+y+z)^2-1,x^2-x,y^2-1]
            sage: phc.mixed_volume(test_sys)                # optional -- phc
            4
        """
    def start_from(self, start_filename_or_string, polys, input_ring, path_track_file=None, verbose: bool = False):
        """
        This computes solutions starting from a phcpack solution file.

        INPUT:

        - ``start_filename_or_string`` -- the filename for a phcpack start system,
          or the contents of such a file as a string.  Variable names must match
          the inputring variables.  The value of the homotopy variable t should
          be 1, not 0.
        - ``polys`` -- list of multivariate polynomials (elements of a multivariate
          polynomial ring).
        - input_ring: for coercion of the variables into the desired ring.
        - path_track_file: whether to save path-tracking information
        - ``verbose`` -- print lots of verbose information about what this function does

        OUTPUT: a solution in the form of a PHCObject

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [x^6-y^2,y^5-1]
            sage: sol = phc.blackbox(start_sys, R2)        # optional -- phc
            sage: start_save = sol.save_as_start()         # optional -- phc
            sage: end_sys = [x^7-2,y^5-x^2]                # optional -- phc
            sage: sol = phc.start_from(start_save, end_sys, R2)  # optional -- phc
            sage: len(sol.solutions())                     # optional -- phc
            30
        """
    def blackbox(self, polys, input_ring, verbose: bool = False):
        """
        Return as a string the result of running PHC with the given polynomials
        under blackbox mode (the '-b' option).

        INPUT:

        - ``polys`` -- list of multivariate polynomials (elements of a multivariate
          polynomial ring).
        - ``input_ring`` -- for coercion of the variables into the desired ring
        - ``verbose`` -- print lots of verbose information about what this function does

        OUTPUT: a PHC_Object object containing the phcpack output string

        EXAMPLES::

            sage: from sage.interfaces.phc import *
            sage: R2.<x,y> = PolynomialRing(QQ,2)
            sage: start_sys = [x^6-y^2,y^5-1]
            sage: sol = phc.blackbox(start_sys, R2)        # optional -- phc
            sage: len(sol.solutions())                     # optional -- phc
            30
        """

phc: Incomplete
