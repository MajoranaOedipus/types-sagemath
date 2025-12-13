from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.element import Element as Element, parent as parent
from sage.structure.parent_base import ParentWithBase as ParentWithBase
from sage.structure.richcmp import rich_to_bool as rich_to_bool
from sage.structure.sage_object import SageObject as SageObject

class AsciiArtString(str): ...

class Interface(WithEqualityById, ParentWithBase):
    """
    Interface interface object.

    .. NOTE::

        Two interfaces compare equal if and only if they are identical
        objects (this is a critical constraint so that caching of
        representations of objects in interfaces works
        correctly). Otherwise they are never equal.
    """
    def __init__(self, name) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Maxima() == maxima
            False
            sage: maxima == maxima
            True

            sage: Maxima() != maxima
            True
            sage: maxima != maxima
            False
        """
    def name(self, new_name=None): ...
    def get_seed(self):
        """
        Return the seed used to set the random number generator in
        this interface.

        The seed is initialized as ``None`` but should be set when the
        interface starts.

        EXAMPLES::

            sage: s = Singular()
            sage: s.set_seed(107)
            107
            sage: s.get_seed()
            107
        """
    def rand_seed(self):
        '''
        Return a random seed that can be put into ``set_seed`` function
        for any interpreter.

        This should be overridden if the particular interface needs
        something other than a small positive integer.

        EXAMPLES::

            sage: from sage.interfaces.interface import Interface
            sage: i = Interface("")
            sage: i.rand_seed() # random
            318491487

            sage: s = Singular()
            sage: s.rand_seed() # random
            365260051
        '''
    def set_seed(self, seed=None) -> None:
        '''
        Set the random seed for the interpreter and return the new
        value of the seed.

        This is dependent on which interpreter so must be implemented
        in each separately. For examples see gap.py or singular.py.

        If seed is ``None`` then should generate a random seed.

        EXAMPLES::

            sage: s = Singular()
            sage: s.set_seed(1)
            1
            sage: [s.random(1,10) for i in range(5)]
            [8, 10, 4, 9, 1]

            sage: from sage.interfaces.interface import Interface
            sage: i = Interface("")
            sage: i.set_seed()
            Traceback (most recent call last):
            ...
            NotImplementedError: This interpreter did not implement a set_seed function
        '''
    def interact(self) -> None:
        """
        This allows you to interactively interact with the child
        interpreter.

        Press :kbd:`Ctrl` + :kbd:`D` or type 'quit' or 'exit' to exit and
        return to Sage.

        .. NOTE::

           This is completely different than the console() member
           function. The console function opens a new copy of the
           child interpreter, whereas the interact function gives you
           interactive access to the interpreter that is being used by
           Sage. Use sage(xxx) or interpretername(xxx) to pull objects
           in from sage to the interpreter.
        """
    def cputime(self) -> float:
        """
        CPU time since this process started running.
        """
    def read(self, filename) -> None:
        """
        EXAMPLES::

            sage: filename = tmp_filename()
            sage: f = open(filename, 'w')
            sage: _ = f.write('x = 2\\n')
            sage: f.close()
            sage: octave.read(filename)  # optional - octave
            sage: octave.get('x')        # optional - octave
            ' 2'
            sage: import os
            sage: os.unlink(filename)
        """
    def eval(self, code, **kwds) -> None:
        """
        Evaluate code in an interface.

        This method needs to be implemented in sub-classes.

        Note that it is not always to be expected that
        it returns a non-empty string. In contrast,
        :meth:`get` is supposed to return the result of applying
        a print command to the object so that the output is easier
        to parse.

        Likewise, the method :meth:`_eval_line` for evaluation of a single
        line, often makes sense to be overridden.
        """
    def execute(self, *args, **kwds): ...
    def __call__(self, x, name=None):
        """
        Create a new object in ``self`` from ``x``.

        The object ``X`` returned can be used like any Sage object, and
        wraps an object in ``self``.  The standard arithmetic operators
        work.  Moreover if ``foo`` is a function then::

            ``X.foo(y,z,...)``

        calls ``foo(X, y, z, ...)`` and returns the corresponding object.

        EXAMPLES::

            sage: gp(2)
            2
            sage: gp('2')
            2
            sage: a = gp(2); gp(a) is a
            True

        TESTS:

        Check conversion of Booleans (:issue:`28705`)::

            sage: giac(True)  # needs giac
            true
            sage: maxima(True)
            true
        """
    def new(self, code): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var):
        """
        Get the value of the variable var.

        Note that this needs to be overridden in some interfaces,
        namely when getting the string representation of an object
        requires an explicit print command.
        """
    def get_using_file(self, var):
        """
        Return the string representation of the variable var in self,
        possibly using a file. Use this if var has a huge string
        representation, since it may be way faster.

        .. warning::

           In fact unless a special derived class implements this, it
           will *not* be any faster. This is the case for this class
           if you're reading it through introspection and seeing this.
        """
    def clear(self, var) -> None:
        """
        Clear the variable named var.
        """
    def function_call(self, function, args=None, kwds=None):
        """
        EXAMPLES::

            sage: maxima.quad_qags(x, x, 0, 1, epsrel=1e-4)
            [0.5,5.5511151231257...e-15,21,0]
            sage: maxima.function_call('quad_qags', [x, x, 0, 1], {'epsrel':'1e-4'})
            [0.5,5.5511151231257...e-15,21,0]
        """
    def call(self, function_name, *args, **kwds): ...
    def __getattr__(self, attrname):
        """
        TESTS::

            sage: from sage.structure.parent_base import ParentWithBase
            sage: from sage.interfaces.singular import singular
            sage: ParentWithBase.__getattribute__(singular, '_coerce_map_from_')
            <bound method Singular._coerce_map_from_ of Singular>
        """
    def console(self) -> None: ...
    def help(self, s): ...

class InterfaceFunction(SageObject):
    """
    Interface function.
    """
    def __init__(self, parent, name) -> None: ...
    def __call__(self, *args, **kwds): ...

class InterfaceFunctionElement(SageObject):
    """
    Interface function element.
    """
    def __init__(self, obj, name) -> None: ...
    def __call__(self, *args, **kwds): ...
    def help(self) -> None: ...

def is_InterfaceElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`InterfaceElement`.

    EXAMPLES::

        sage: from sage.interfaces.interface import is_InterfaceElement
        sage: is_InterfaceElement(2)
        doctest:...: DeprecationWarning: the function is_InterfaceElement is deprecated; use isinstance(x, sage.interfaces.abc.InterfaceElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
    """

class InterfaceElement(Element):
    """
    Interface element.
    """
    def __init__(self, parent, value, is_name: bool = False, name=None) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int:
        """
        Call self.sage() and return the length of that sage object.

        This approach is inefficient - each interface should override
        this method with one that calls the external program's length
        function.

        EXAMPLES::

            sage: len(gp([1,2,3]))
            3

        AUTHORS:

        - Felix Lawrence (2009-08-21)
        """
    def __reduce__(self):
        '''
        The default linearisation is to return ``self``\'s parent,
        which will then get the items returned by :meth:`_reduce`
        as arguments to reconstruct the element.

        EXAMPLES::

            sage: G = gap.SymmetricGroup(6)
            sage: loads(dumps(G)) == G     # indirect doctest
            True
            sage: y = gap(34)
            sage: loads(dumps(y))
            34
            sage: type(_)
            <class \'sage.interfaces.gap.GapElement\'>
            sage: y = singular(34)
            sage: loads(dumps(y))
            34
            sage: type(_)
            <class \'sage.interfaces.singular.SingularElement\'>
            sage: G = gap.PolynomialRing(QQ, [\'x\'])
            sage: loads(dumps(G))
            PolynomialRing( Rationals, ["x"] )
            sage: S = singular.ring(0, (\'x\'))
            sage: loads(dumps(S))
            polynomial ring, over a field, global ordering
            // coefficients: QQ...
            // number of vars : 1
            //        block   1 : ordering lp
            //                  : names    x
            //        block   2 : ordering C

        Here are further examples of pickling of interface elements::

            sage: loads(dumps(gp(\'"abc"\')))
            abc
            sage: loads(dumps(gp([1,2,3])))
            [1, 2, 3]
            sage: loads(dumps(pari(\'"abc"\')))
            "abc"
            sage: loads(dumps(pari([1,2,3])))
            [1, 2, 3]
            sage: loads(dumps(r(\'"abc"\')))                                        # optional - rpy2
            [1] "abc"
            sage: loads(dumps(r([1,2,3])))                                        # optional - rpy2
            [1] 1 2 3
            sage: loads(dumps(maxima([1,2,3])))
            [1,2,3]

        Unfortunately, strings in maxima can\'t be pickled yet::

            sage: loads(dumps(maxima(\'"abc"\')))
            Traceback (most recent call last):
            ...
            TypeError: unable to make sense of Maxima expression \'"abc"\' in Sage
        '''
    def __call__(self, *args): ...
    def __contains__(self, x) -> bool: ...
    def __hash__(self):
        """
        Return the hash of ``self``. This is a default implementation of hash
        which just takes the hash of the string of ``self``.
        """
    def is_string(self):
        """
        Tell whether this element is a string.

        By default, the answer is negative.
        """
    def __del__(self) -> None: ...
    def sage(self, *args, **kwds):
        '''
        Attempt to return a Sage version of this object.

        This method does nothing more than calling :meth:`_sage_`,
        simply forwarding any additional arguments.

        EXAMPLES::

            sage: gp(1/2).sage()
            1/2
            sage: _.parent()
            Rational Field
            sage: singular.lib("matrix")
            sage: R = singular.ring(0, \'(x,y,z)\', \'dp\')
            sage: singular.matrix(2,2).sage()
            [0 0]
            [0 0]
        '''
    def __getattr__(self, attrname): ...
    def get_using_file(self):
        """
        Return this element's string representation using a file. Use this
        if ``self`` has a huge string representation. It'll be way faster.

        EXAMPLES::

            sage: a = maxima(str(2^1000))
            sage: a.get_using_file()
            '10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376'
        """
    def hasattr(self, attrname):
        """
        Return whether the given attribute is already defined by this
        object, and in particular is not dynamically generated.

        EXAMPLES::

            sage: m = maxima('2')
            sage: m.hasattr('integral')
            True
            sage: m.hasattr('gcd')
            False
        """
    def attribute(self, attrname):
        """
        If this wraps the object x in the system, this returns the object
        x.attrname. This is useful for some systems that have object
        oriented attribute access notation.

        EXAMPLES::

            sage: g = gap('SO(1,4,7)')
            sage: k = g.InvariantQuadraticForm()
            sage: k.attribute('matrix')
            [ [ 0*Z(7), Z(7)^0, 0*Z(7), 0*Z(7) ], [ 0*Z(7), 0*Z(7), 0*Z(7), 0*Z(7) ],
              [ 0*Z(7), 0*Z(7), Z(7), 0*Z(7) ], [ 0*Z(7), 0*Z(7), 0*Z(7), Z(7)^0 ] ]

        ::

            sage: e = gp('ellinit([0,-1,1,-10,-20])')
            sage: e.attribute('j')
            -122023936/161051
        """
    def __getitem__(self, n): ...
    def __int__(self) -> int:
        """
        EXAMPLES::

            sage: int(maxima('1'))
            1
            sage: type(_)
            <... 'int'>
        """
    def bool(self):
        """
        Convert this element to a boolean.

        EXAMPLES::

            sage: singular(0).bool()
            False
            sage: singular(1).bool()
            True
        """
    def __bool__(self) -> bool:
        '''
        Return whether this element is not ``False``.

        .. NOTE::

            This method needs to be overridden if the subprocess would
            not return a string representation of a boolean value unless
            an explicit print command is used.

        EXAMPLES::

            sage: bool(maxima(0))
            False
            sage: bool(maxima(1))
            True

        TESTS:

        By default this returns ``True`` for elements that are considered to be
        not ``False`` by the interface (:issue:`28705`)::

            sage: bool(giac(\'"a"\'))  # needs giac
            True
        '''
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: m = maxima('1/2')
            sage: m.__float__()
            0.5
            sage: float(m)
            0.5
        """
    def name(self, new_name=None):
        """
        Return the name of ``self``. If ``new_name`` is passed in, then this
        function returns a new object identical to ``self`` whose name is
        ``new_name``.

        Note that this can overwrite existing variables in the system.

        EXAMPLES::

            sage: # optional - rpy2
            sage: x = r([1,2,3]); x
            [1] 1 2 3
            sage: x.name()
            'sage...'
            sage: x = r([1,2,3]).name('x'); x
            [1] 1 2 3
            sage: x.name()
            'x'

        ::

            sage: s5 = gap.SymmetricGroup(5).name('s5')
            sage: s5
            SymmetricGroup( [ 1 .. 5 ] )
            sage: s5.name()
            's5'
        """
    def gen(self, n): ...
    def __invert__(self):
        """
        EXAMPLES::

            sage: f = maxima('sin(x)')
            sage: ~f
            1/sin(x)
            sage: f = maxima.function('x','sin(x)')
            sage: ~f
            1/sin(x)
        """
    def __pow__(self, n):
        """
        EXAMPLES::

            sage: a = maxima('2')
            sage: a^(3/4)
            2^(3/4)

        ::

            sage: f = maxima.function('x','sin(x)')
            sage: g = maxima('-cos(x)')
            sage: f^g
            1/sin(x)^cos(x)

        ::

            sage: f = maxima.function('x','sin(x)')
            sage: g = maxima('-cos(x)') # not a function
            sage: g^f
            (-cos(x))^sin(x)
        """
