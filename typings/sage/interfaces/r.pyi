r"""
Interfaces to R

This is the reference to the Sagemath R interface, usable from any
Sage program.

The %r interface creating an R cell in the sage
notebook is described in the Notebook manual.

The %R and %%R interface creating an R line or an R cell in the
Jupyter notebook are briefly described at the end of this page. This
documentation will be expanded and placed in the Jupyter notebook
manual when this manual exists.

The following examples try to follow "An Introduction to R" which can
be found at http://cran.r-project.org/doc/manuals/R-intro.html .

EXAMPLES:

Simple manipulations; numbers and vectors

The simplest data structure in R is the numeric vector which
consists of an ordered collection of numbers.  To create a
vector named `x` using the R interface in Sage, you pass the
R interpreter object a list or tuple of numbers::

    sage: x = r([10.4,5.6,3.1,6.4,21.7]); x
    [1] 10.4  5.6  3.1  6.4 21.7

You can invert elements of a vector x in R by using the
invert operator or by doing 1/x::

    sage: ~x
    [1] 0.09615385 0.17857143 0.32258065 0.15625000 0.04608295
    sage: 1/x
    [1] 0.09615385 0.17857143 0.32258065 0.15625000 0.04608295

The following assignment creates a vector `y` with 11 entries which
consists of two copies of `x` with a 0 in between::

    sage: y = r([x,0,x]); y
    [1] 10.4  5.6  3.1  6.4 21.7  0.0 10.4  5.6  3.1  6.4 21.7

Vector Arithmetic

The following command generates a new vector `v` of length 11 constructed
by adding together (element by element) `2x` repeated 2.2 times, `y`
repeated just once, and 1 repeated 11 times::

    sage: v = 2*x+y+1; v
    [1] 32.2 17.8 10.3 20.2 66.1 21.8 22.6 12.8 16.9 50.8 43.5

One can compute the sum of the elements of an R vector in the following
two ways::

    sage: sum(x)
    [1] 47.2
    sage: x.sum()
    [1] 47.2

One can calculate the sample variance of a list of numbers::

    sage: ((x-x.mean())^2/(x.length()-1)).sum()
    [1] 53.853
    sage: x.var()
    [1] 53.853

    sage: x.sort()
    [1] 3.1  5.6  6.4 10.4 21.7
    sage: x.min()
    [1] 3.1
    sage: x.max()
    [1] 21.7
    sage: x
    [1] 10.4  5.6  3.1  6.4 21.7

    sage: r(-17).sqrt()
    [1] NaN
    sage: r('-17+0i').sqrt()
    [1] 0+4.123106i

Generating an arithmetic sequence::

    sage: r('1:10')
    [1] 1  2  3  4  5  6  7  8  9 10

Because ``from`` is a keyword in Python, it can't be used
as a keyword argument.  Instead, ``from_`` can be passed, and
R will recognize it as the correct thing::

    sage: r.seq(length=10, from_=-1, by=.2)
    [1] -1.0 -0.8 -0.6 -0.4 -0.2  0.0  0.2  0.4  0.6  0.8

    sage: x = r([10.4,5.6,3.1,6.4,21.7])
    sage: x.rep(2)
    [1] 10.4  5.6  3.1  6.4 21.7 10.4  5.6  3.1  6.4 21.7
    sage: x.rep(times=2)
    [1] 10.4  5.6  3.1  6.4 21.7 10.4  5.6  3.1  6.4 21.7
    sage: x.rep(each=2)
    [1] 10.4 10.4  5.6  5.6  3.1  3.1  6.4  6.4 21.7 21.7

Missing Values::

    sage: na = r('NA')
    sage: z = r([1,2,3,na])
    sage: z
    [1]  1  2  3 NA
    sage: ind = r.is_na(z)
    sage: ind
    [1] FALSE FALSE FALSE  TRUE
    sage: zero = r(0)
    sage: zero / zero
    [1] NaN
    sage: inf = r('Inf')
    sage: inf-inf
    [1] NaN
    sage: r.is_na(inf)
    [1] FALSE
    sage: r.is_na(inf-inf)
    [1] TRUE
    sage: r.is_na(zero/zero)
    [1] TRUE
    sage: r.is_na(na)
    [1] TRUE
    sage: r.is_nan(inf-inf)
    [1] TRUE
    sage: r.is_nan(zero/zero)
    [1] TRUE
    sage: r.is_nan(na)
    [1] FALSE


Character Vectors::

    sage: labs = r.paste('c("X","Y")', '1:10', sep='""'); labs
    [1] "X1"  "Y2"  "X3"  "Y4"  "X5"  "Y6"  "X7"  "Y8"  "X9"  "Y10"


Index vectors; selecting and modifying subsets of a data set::

    sage: na = r('NA')
    sage: x = r([10.4,5.6,3.1,6.4,21.7,na]); x
    [1] 10.4  5.6  3.1  6.4 21.7   NA
    sage: x['!is.na(self)']
    [1] 10.4  5.6  3.1  6.4 21.7

    sage: x = r([10.4,5.6,3.1,6.4,21.7,na]); x
    [1] 10.4  5.6  3.1  6.4 21.7   NA
    sage: (x+1)['(!is.na(self)) & self>0']
    [1] 11.4  6.6  4.1  7.4 22.7
    sage: x = r([10.4,-2,3.1,-0.5,21.7,na]); x
    [1] 10.4 -2.0  3.1 -0.5 21.7   NA
    sage: (x+1)['(!is.na(self)) & self>0']
    [1] 11.4  4.1  0.5 22.7

Distributions::

    sage: r.options(width='60')
    $width
    [1] 80

    sage: rr = r.dnorm(r.seq(-3,3,0.1))
    sage: rr
     [1] 0.004431848 0.005952532 0.007915452 0.010420935
     [5] 0.013582969 0.017528300 0.022394530 0.028327038
     [9] 0.035474593 0.043983596 0.053990967 0.065615815
    [13] 0.078950158 0.094049077 0.110920835 0.129517596
    [17] 0.149727466 0.171368592 0.194186055 0.217852177
    [21] 0.241970725 0.266085250 0.289691553 0.312253933
    [25] 0.333224603 0.352065327 0.368270140 0.381387815
    [29] 0.391042694 0.396952547 0.398942280 0.396952547
    [33] 0.391042694 0.381387815 0.368270140 0.352065327
    [37] 0.333224603 0.312253933 0.289691553 0.266085250
    [41] 0.241970725 0.217852177 0.194186055 0.171368592
    [45] 0.149727466 0.129517596 0.110920835 0.094049077
    [49] 0.078950158 0.065615815 0.053990967 0.043983596
    [53] 0.035474593 0.028327038 0.022394530 0.017528300
    [57] 0.013582969 0.010420935 0.007915452 0.005952532
    [61] 0.004431848

Convert R Data Structures to Python/Sage::

    sage: rr = r.dnorm(r.seq(-3,3,0.1))
    sage: sum(rr._sage_())
    9.9772125168981...

Or you get a dictionary to be able to access all the information::

    sage: rs = r.summary(r.c(1,4,3,4,3,2,5,1))
    sage: rs
       Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
      1.000   1.750   3.000   2.875   4.000   5.000
      sage: d = rs._sage_()
      sage: d['DATA']
      [1, 1.75, 3, 2.875, 4, 5]
      sage: d['_Names']
      ['Min.', '1st Qu.', 'Median', 'Mean', '3rd Qu.', 'Max.']
      sage: d['_r_class']
      ['summaryDefault', 'table']

It is also possible to access the plotting capabilities of R
through Sage.  For more information see the documentation of
r.plot() or r.png().

THE JUPYTER NOTEBOOK INTERFACE (work in progress).

The %r interface described in the Sage notebook manual is not useful
in the Jupyter notebook : it creates a inferior R interpreter which
cannot be escaped.

The RPy2 library allows the creation of an R cell in the Jupyter
notebook analogous to the %r escape in command line or %r cell in a
Sage notebook.

The interface is loaded by a cell containing the sole code:

"%load_ext rpy2.ipython"

After execution of this code, the %R and %%R magics are available:

- %R allows the execution of a single line of R code. Data exchange is
   possible via the -i and -o options. Do "%R?" in a standalone cell
   to get the documentation.

- %%R allows the execution in R of the whole text of a cell, with
    similar options (do "%%R?" in a standalone cell for
    documentation).

A few important points must be noted:

- The R interpreter launched by this interface IS (currently)
  DIFFERENT from the R interpreter used br other r... functions.

- Data exchanged via the -i and -o options have a format DIFFERENT
  from the format used by the r... functions (RPy2 mostly uses arrays,
  and bugs the user to use the pandas Python package).

- R graphics are (beautifully) displayed in output cells, but are not
  directly importable. You have to save them as .png, .pdf or .svg
  files and import them in Sage for further use.

In its current incarnation, this interface is mostly useful to
statisticians needing Sage for a few symbolic computations but mostly
using R for applied work.

AUTHORS:

- Mike Hansen (2007-11-01)
- William Stein (2008-04-19)
- Harald Schilly (2008-03-20)
- Mike Hansen (2008-04-19)
- Emmanuel Charpentier (2015-12-12, RPy2 interface)
"""

from sage.env import DOT_SAGE as DOT_SAGE
from sage.features import PythonModule as PythonModule
from sage.interfaces.interface import Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunction as InterfaceFunction, InterfaceFunctionElement as InterfaceFunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import parent as parent

rpy2_feature: PythonModule
COMMANDS_CACHE: str
RRepositoryURL: str
RFilteredPackages: list[str]
RBaseCommands: list[str]

class R(ExtraTabCompletion, Interface):
    def __init__(self, maxread=None, logfile=None, init_list_length: int = 1024, seed=None) -> None:
        """
        An interface to the R interpreter.

        R is a comprehensive collection of methods for statistics,
        modelling, bioinformatics, data analysis and much more.
        For more details, see http://www.r-project.org/about.html

        Resources:

        * http://r-project.org/ provides more information about R.
        * http://rseek.org/ R's own search engine.

        EXAMPLES::

             sage: r.summary(r.c(1,2,3,111,2,3,2,3,2,5,4))
             Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
             1.00    2.00    3.00   12.55    3.50  111.00

        TESTS::

            sage: from sage.interfaces.r import r
            sage: r == loads(dumps(r))
            True
        """
    def set_seed(self, seed=None):
        '''
        Set the seed for R interpreter.

        The seed should be an integer.

        EXAMPLES::

            sage: r = R()
            sage: r.set_seed(1)
            1
            sage: r.sample("1:10", 5) # random
            [1] 3 4 5 7 2
        '''
    def png(self, *args, **kwds):
        '''
        Create an R PNG device.

        This should primarily be used to save an R graphic to a custom file.  Note
        that when using this in the notebook, one must plot in the same cell that
        one creates the device.  See r.plot() documentation for more information
        about plotting via R in Sage.

        These examples won\'t work on the many platforms where R still gets
        built without graphics support.

        EXAMPLES::

            sage: filename = tmp_filename() + \'.png\'
            sage: r.png(filename=\'"%s"\'%filename)               # optional - rgraphics
            NULL
            sage: x = r([1,2,3])
            sage: y = r([4,5,6])
            sage: r.plot(x,y)                                   # optional - rgraphics
            null device
                      1
            sage: import os; os.unlink(filename)                # optional - rgraphics

        We want to make sure that we actually can view R graphics, which happens
        differently on different platforms::

            sage: s = r.eval(\'capabilities("png")\')   # should be on Linux and Solaris
            sage: t = r.eval(\'capabilities("aqua")\')  # should be on all supported Mac versions
            sage: "TRUE" in s+t                                 # optional - rgraphics
            True
        '''
    def convert_r_list(self, l):
        '''
        Convert an R list to a Python list.

        EXAMPLES::

            sage: s = \'c(".GlobalEnv", "package:stats", "package:graphics", "package:grDevices", \\n"package:utils", "package:datasets", "package:methods", "Autoloads", \\n"package:base")\'
            sage: r.convert_r_list(s)
            [\'.GlobalEnv\',
             \'package:stats\',
             \'package:graphics\',
             \'package:grDevices\',
             \'package:utils\',
             \'package:datasets\',
             \'package:methods\',
             \'Autoloads\',
             \'package:base\']
        '''
    def install_packages(self, package_name) -> None:
        """
        Install an R package into Sage's R installation.

        EXAMPLES::

            sage: r.install_packages('aaMI')       # not tested
            ...
            R is free software and comes with ABSOLUTELY NO WARRANTY.
            You are welcome to redistribute it under certain conditions.
            Type 'license()' or 'licence()' for distribution details.
            ...
            Please restart Sage in order to use 'aaMI'.
        """
    def __reduce__(self):
        """
        Used in serializing an R interface.

        EXAMPLES::

            sage: from sage.interfaces.r import r
            sage: rlr, t = r.__reduce__()
            sage: rlr(*t)
            R Interpreter
        """
    def __getattr__(self, attrname):
        """
        Called when you get an attribute of the R interface.  This
        manufactures an R function, which is a Python function that
        can then be called with various inputs.

        EXAMPLES::

            sage: c = r.c; c
            c
            sage: type(c)
            <class 'sage.interfaces.r.RFunction'>
        """
    def read(self, filename) -> None:
        """
        Read filename into the R interpreter by calling R's source function on a
        read-only file connection.

        EXAMPLES::

            sage: filename = tmp_filename()
            sage: f = open(filename, 'w')
            sage: _ = f.write('a <- 2+2\\n')
            sage: f.close()
            sage: r.read(filename)
            sage: r.get('a')
            '[1] 4'
        """
    def source(self, s):
        '''
        Display the R source (if possible) about the function named s.

        INPUT:

        - ``s`` -- string representing the function whose source code you want to see

        OUTPUT: string; source code

        EXAMPLES::

            sage: print(r.source("c"))
            function (...)  .Primitive("c")
        '''
    def version(self):
        """
        Return the version of R currently running.

        OUTPUT: tuple of ints; string

        EXAMPLES::

            sage: r.version()                   # not tested
            ((3, 0, 1), 'R version 3.0.1 (2013-05-16)')
            sage: rint, rstr = r.version()
            sage: rint[0] >= 3
            True
            sage: rstr.startswith('R version')
            True
        """
    def library(self, library_name) -> None:
        """
        Load the library library_name into the R interpreter.

        This function raises an :exc:`ImportError` if the given library
        is not known.

        INPUT:

        - ``library_name`` -- string

        EXAMPLES::

            sage: r.library('grid')
            sage: 'grid' in r.eval('(.packages())')
            True
            sage: r.library('foobar')
            Traceback (most recent call last):
            ...
            ImportError: ...
        """
    require = library
    def available_packages(self):
        """
        Return a list of all available R package names.

        This list is not necessarily sorted.

        OUTPUT: list of strings

        .. NOTE::

            This requires an internet connection. The CRAN server is
            that is checked is defined at the top of sage/interfaces/r.py.

        EXAMPLES::

            sage: ap = r.available_packages()                   # optional - internet
            sage: len(ap) > 20                                  # optional - internet
            True
        """
    def help(self, command):
        """
        Return help string for a given command.

        INPUT:

        - ``command`` -- string

        OUTPUT: HelpExpression; a subclass of string whose ``__repr__``
        method is ``__str__``, so it prints nicely

        EXAMPLES::

            sage: r.help('c')
            title
            -----
            <BLANKLINE>
            Combine Values into a Vector or List
            <BLANKLINE>
            name
            ----
            <BLANKLINE>
            c
            ...
        """
    def console(self) -> None:
        """
        Run the R console as a separate new R process.

        EXAMPLES::

            sage: r.console()                    # not tested
                R version 2.6.1 (2007-11-26)
                Copyright (C) 2007 The R Foundation for Statistical Computing
                ISBN 3-900051-07-0
                ...
        """
    def function_call(self, function, args=None, kwds=None):
        """
        Return the result of calling an R function, with given args and keyword args.

        OUTPUT: RElement; an object in R

        EXAMPLES::

            sage: r.function_call('length', args=[ [1,2,3] ])
            [1] 3
        """
    def call(self, function_name, *args, **kwds):
        """
        This is an alias for :meth:`function_call`.

        EXAMPLES::

            sage: r.call('length', [1,2,3])
            [1] 3
        """
    def set(self, var, value) -> None:
        """
        Set the variable var in R to what the string value evaluates to in R.

        INPUT:

        - ``var`` -- string
        - ``value`` -- string

        EXAMPLES::

            sage: r.set('a', '2 + 3')
            sage: r.get('a')
            '[1] 5'
        """
    def get(self, var):
        """
        Return the string representation of the variable var.

        INPUT:

        - ``var`` -- string

        OUTPUT: string

        EXAMPLES::

            sage: r.set('a', 2)
            sage: r.get('a')
            '[1] 2'
        """
    def na(self):
        """
        Return the NA in R.

        OUTPUT: RElement; an element of R

        EXAMPLES::

            sage: r.na()
            [1] NA
        """
    def completions(self, s):
        """
        Return all commands names that complete the command starting with the
        string s.   This is like typing s[Ctrl-T] in the R interpreter.

        INPUT:

        - ``s`` -- string

        OUTPUT: list of strings

        EXAMPLES::

            sage: dummy = r._tab_completion(use_disk_cache=False)  # clean doctest
            sage: 'testInheritedMethods' in r.completions('tes')
            True
        """
    def plot(self, *args, **kwds):
        '''
        The R plot function.  Type r.help(\'plot\') for much more extensive
        documentation about this function.  See also below for a brief
        introduction to more plotting with R.

        If one simply wants to view an R graphic, using this function is
        is sufficient (because it calls dev.off() to turn off the device).

        However, if one wants to save the graphic to a specific file, it
        should be used as in the example below to write the output.

        EXAMPLES:

        This example saves a plot to the standard R output, usually a
        filename like ``Rplot001.png`` - from the command line, in the
        current directory, and in the cell directory in the
        notebook. We use a temporary directory in this example while
        doctesting this example, but you should use something
        persistent in your own code::

            sage: from tempfile import TemporaryDirectory
            sage: with TemporaryDirectory() as d:               # optional - rgraphics
            ....:     _ = r.setwd(d)
            ....:     r.plot("1:10")
            null device
                      1

        To save to a specific file name, one should use :meth:`png` to set
        the output device to that file.  If this is done in the notebook, it
        must be done in the same cell as the plot itself::

            sage: filename = tmp_filename() + \'.png\'
            sage: r.png(filename=\'"%s"\'%filename)               # optional - rgraphics
            NULL
            sage: x = r([1,2,3])
            sage: y = r([4,5,6])
            sage: r.plot(x,y)                                   # optional - rgraphics
            null device
                      1
            sage: import os; os.unlink(filename)                # optional - rgraphics

        Please note that for more extensive use of R\'s plotting
        capabilities (such as the lattices package), it is advisable
        to either use an interactive plotting device or to use the
        notebook.  The following examples are not tested, because they
        differ depending on operating system::

            sage: # not tested
            sage: r.X11()
            sage: r.quartz()
            sage: r.hist("rnorm(100)")
            sage: r.library("lattice")
            sage: r.histogram(x = \'~ wt | cyl\', data=\'mtcars\')
            sage: r.dev_off()

        In the notebook, one can use r.png() to open the device, but
        would need to use the following since R lattice graphics do
        not automatically print away from the command line::

            sage: filename = tmp_filename() + \'.png\'  # not needed in notebook, used for doctesting
            sage: r.png(filename=\'"%s"\'%filename)               # optional - rgraphics
            NULL
            sage: r.library("lattice")
            sage: r("print(histogram(~wt | cyl, data=mtcars))")         # optional - rgraphics
            sage: import os; os.unlink(filename)                # optional - rgraphics
        '''
    def eval(self, code, *args, **kwds):
        """
        Evaluates a command inside the R interpreter and returns the output
        as a string.

        EXAMPLES::

            sage: r.eval('1+1')
            '[1] 2'
        """
    def __getitem__(self, s):
        """
        Return the RFunction with name s.

        INPUT:

        - ``s`` -- string

        OUTPUT: RFunction; the R function that in R has name s

        EXAMPLES::

            sage: r['as.data.frame']
            as.data.frame
            sage: r['print']
            print
        """
    def chdir(self, dir) -> None:
        """
        Changes the working directory to ``dir``.

        INPUT:

        - ``dir`` -- the directory to change to

        EXAMPLES::

            sage: import tempfile
            sage: tmpdir = tempfile.mkdtemp()
            sage: r.chdir(tmpdir)

        Check that ``tmpdir`` and ``r.getwd()`` refer to the same
        directory.  We need to use ``realpath()`` in case ``$TMPDIR``
        (by default ``/tmp``) is a symbolic link (see :issue:`10264`).

        ::

            sage: os.path.realpath(tmpdir) == sageobj(r.getwd())  # known bug (issue #9970)
            True
        """

class RElement(ExtraTabCompletion, InterfaceElement):
    def tilde(self, x):
        """
        The tilde regression operator in R.

        EXAMPLES::

            sage: x = r([1,2,3,4,5])
            sage: y = r([3,5,7,9,11])
            sage: a = r.lm( y.tilde(x) ) # lm( y ~ x )
            sage: d = a._sage_()
            sage: d['DATA']['coefficients']['DATA'][1]
            2
        """
    stat_model = tilde
    def is_string(self):
        '''
        Tell whether this element is a string.

        EXAMPLES::

            sage: r(\'"abc"\').is_string()
            True
            sage: r([1,2,3]).is_string()
            False
        '''
    def __len__(self) -> int:
        """
        Return the length of this object.

        OUTPUT: integer

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: len(x)
            5
        """
    def __getattr__(self, attrname):
        """
        Return attribute of this object, which is an R function with this object
        as the first input.

        INPUT:

        - ``attrname`` -- string

        OUTPUT: RFunctionElement

        EXAMPLES::

            sage: x = r([1,2,3])
            sage: length = x.length
            sage: type(length)
            <class 'sage.interfaces.r.RFunctionElement'>
            sage: length()
            [1] 3
        """
    def __getitem__(self, n):
        """
        Return element(s) of ``self``.

        INPUT:

        - ``n`` -- integer, a tuple, a string that makes sense to R, or an
          RElement

        OUTPUT: RElement

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x[0]
            numeric(0)
            sage: x[1]
            [1] 10.4
            sage: x[-1]
            [1] 5.6  3.1  6.4 21.7
            sage: x[-2]
            [1] 10.4  3.1  6.4 21.7
            sage: x[-3]
            [1] 10.4  5.6  6.4 21.7
            sage: x['c(2,3)']
            [1]  5.6 3.1
            sage: key = r.c(2,3)
            sage: x[key]
            [1]  5.6 3.1
            sage: m = r.array('1:3',r.c(2,4,2))
            sage: m
            , , 1
                 [,1] [,2] [,3] [,4]
            [1,]    1    3    2    1
            [2,]    2    1    3    2
            , , 2
                 [,1] [,2] [,3] [,4]
            [1,]    3    2    1    3
            [2,]    1    3    2    1
            sage: m[1,2,2]
            [1] 2
            sage: m[1,r.c(1,2),1]
            [1] 1 3
        """
    def __bool__(self) -> bool:
        """
        Implement ``bool(self)``.

        .. NOTE::

            bool(self) will only return ``True`` if ``self == 0`` contains a
            FALSE in its representation.

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: bool(x)
            True
            sage: y = r([0,0,0,0])
            sage: bool(y)
            False
            sage: bool(r(0))
            False
            sage: bool(r(1))
            True
        """
    def __eq__(self, other):
        """
        Equality testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES:

        Notice that comparison is term by term and returns an R element. ::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x == 10.4
            [1] TRUE FALSE FALSE FALSE FALSE
        """
    def __lt__(self, other):
        """
        Less than testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES:

        Notice that comparison is term by term and returns an R element. ::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x < 7
            [1] FALSE  TRUE  TRUE  TRUE FALSE
        """
    def __gt__(self, other):
        """
        Greater than testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES:

        Notice that comparison is term by term and returns an R element. ::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x > 8
            [1] TRUE FALSE FALSE FALSE  TRUE
        """
    def __le__(self, other):
        """
        Less than or equal testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x <= 10.4
            [1] TRUE  TRUE  TRUE  TRUE FALSE
        """
    def __ge__(self, other):
        """
        Greater than or equal testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x >= 10.4
            [1] TRUE FALSE FALSE FALSE  TRUE
        """
    def __ne__(self, other):
        """
        Not equal testing term by term.

        INPUT:

        - ``other`` -- RElement

        OUTPUT: RElement; an R element (not a bool!)

        EXAMPLES::

            sage: x = r([10.4,5.6,3.1,6.4,21.7])
            sage: x != 10.4
            [1] FALSE  TRUE  TRUE  TRUE  TRUE
        """
    def dot_product(self, other):
        """
        Implement the notation ``self . other``.

        INPUT:

        - ``self``, ``other`` -- R elements

        OUTPUT: R element

        EXAMPLES::

            sage: c = r.c(1,2,3,4)
            sage: c.dot_product(c.t())
                 [,1] [,2] [,3] [,4]
            [1,]    1    2    3    4
            [2,]    2    4    6    8
            [3,]    3    6    9   12
            [4,]    4    8   12   16

            sage: v = r([3,-1,8])
            sage: v.dot_product(v)
                 [,1]
            [1,]   74
        """

class RFunctionElement(InterfaceFunctionElement):
    def __reduce__(self) -> None:
        """
        EXAMPLES::

            sage: a = r([1,2,3])
            sage: a.mean
            mean
            sage: dumps(a.mean)
            Traceback (most recent call last):
            ...
            NotImplementedError: pickling of R element methods is not yet supported
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: a = r([1,2,3])
            sage: length = a.length
            sage: length()
            [1] 3
        """

class RFunction(InterfaceFunction):
    def __init__(self, parent, name, r_name=None) -> None:
        """
        A Function in the R interface.

        INPUT:

        - ``parent`` -- the R interface
        - ``name`` -- the name of the function for Python
        - ``r_name`` -- the name of the function in R itself (which can have dots in it)

        EXAMPLES::

            sage: length = r.length
            sage: type(length)
            <class 'sage.interfaces.r.RFunction'>
            sage: loads(dumps(length))
            length
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: r.mean == loads(dumps(r.mean))
            True
            sage: r.mean == r.lr
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: r.mean != loads(dumps(r.mean))
            False
            sage: r.mean != r.lr
            True
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: length = r.length
            sage: length([1,2,3])
            [1] 3
        """

def is_RElement(x):
    """
    Return ``True`` if x is an element in an R interface.

    INPUT:

    - ``x`` -- object

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.interfaces.r import is_RElement
        sage: is_RElement(2)
        doctest:...: DeprecationWarning: the function is_RElement is deprecated; use isinstance(x, sage.interfaces.abc.RElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_RElement(r(2))
        True
    """

r: R

def reduce_load_R():
    """
    Used for reconstructing a copy of the R interpreter from a pickle.

    EXAMPLES::

        sage: from sage.interfaces.r import reduce_load_R
        sage: reduce_load_R()
        R Interpreter
    """
def r_console() -> None:
    """
    Spawn a new R command-line session.

    EXAMPLES::

        sage: r.console()                    # not tested
            R version 2.6.1 (2007-11-26)
            Copyright (C) 2007 The R Foundation for Statistical Computing
            ISBN 3-900051-07-0
            ...
    """
def r_version():
    """
    Return the R version.

    EXAMPLES::

        sage: r_version()                       # not tested
        ((3, 0, 1), 'R version 3.0.1 (2013-05-16)')
        sage: rint, rstr = r_version()
        sage: rint[0] >= 3
        True
        sage: rstr.startswith('R version')
        True
    """

class HelpExpression(str):
    """
    Used to improve printing of output of r.help.
    """
