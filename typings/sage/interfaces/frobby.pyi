from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.misc_c import prod as prod

class Frobby:
    def __call__(self, action, input=None, options=[], verbose: bool = False):
        '''
        This function calls Frobby as a command line program using streams
        for input and output. Strings passed as part of the command get
        broken up at whitespace. This is not done to the data passed
        via the streams.

        INPUT:

        - ``action`` -- string telling Frobby what to do
        - ``input`` -- ``None`` or string that is passed to Frobby as standard in
        - ``options`` -- list of options without the dash in front
        - ``verbose`` -- boolean (default: ``False``); print detailed information

        OUTPUT: string; what Frobby wrote to the standard output stream

        EXAMPLES:

        We compute the lcm of an ideal provided in Monos format. ::

            sage: frobby("analyze", input="vars x,y,z;[x^2,x*y];", # optional - frobby
            ....:     options=["lcm", "iformat monos", "oformat 4ti2"])
            \' 2 1 0\\n\\n2 generators\\n3 variables\\n\'


        We get an exception if frobby reports an error. ::

            sage: frobby("do_dishes") # optional - frobby
            Traceback (most recent call last):
            ...
            RuntimeError: Frobby reported an error:
            ERROR: No action has the prefix "do_dishes".

        AUTHOR:

        - Bjarke Hammersholt Roune (2008-04-27)
        '''
    def alexander_dual(self, monomial_ideal):
        """
        This function computes the Alexander dual of the passed-in
        monomial ideal. This ideal is the one corresponding to the
        simplicial complex whose faces are the complements of the
        nonfaces of the simplicial complex corresponding to the input
        ideal.

        INPUT:

        - ``monomial_ideal`` -- the monomial ideal to decompose

        OUTPUT: the monomial corresponding to the Alexander dual

        EXAMPLES:

        This is a simple example of computing irreducible decomposition. ::

            sage: # optional - frobby
            sage: (a, b, c, d) = QQ['a,b,c,d'].gens()
            sage: id = ideal(a * b, b * c, c * d, d * a)
            sage: alexander_dual = frobby.alexander_dual(id)
            sage: true_alexander_dual = ideal(b * d, a * c)
            sage: alexander_dual == true_alexander_dual # use sets to ignore order
            True

        We see how it is much faster to compute this with frobby than the built-in
        procedure for simplicial complexes::

            sage: # optional - frobby
            sage: t=simplicial_complexes.PoincareHomologyThreeSphere()
            sage: R=PolynomialRing(QQ,16,'x')
            sage: I=R.ideal([prod([R.gen(i-1) for i in a]) for a in t.facets()])
            sage: len(frobby.alexander_dual(I).gens())
            643
        """
    def hilbert(self, monomial_ideal):
        """
        Compute the multigraded Hilbert-Poincaré series of the input
        ideal. Use the -univariate option to get the univariate series.

        The Hilbert-Poincaré series of a monomial ideal is the sum of all
        monomials not in the ideal. This sum can be written as a (finite)
        rational function with `(x_1-1)(x_2-1)...(x_n-1)` in the denominator,
        assuming the variables of the ring are `x_1,x2,...,x_n`. This action
        computes the polynomial in the numerator of this fraction.

        INPUT:

        - ``monomial_ideal`` -- a monomial ideal

        OUTPUT:

        A polynomial in the same ring as the ideal.

        EXAMPLES::

            sage: R.<d,b,c>=QQ[] # optional - frobby
            sage: I=[d*b*c,b^2*c,b^10,d^10]*R # optional - frobby
            sage: frobby.hilbert(I) # optional - frobby
            d^10*b^10*c + d^10*b^10 + d^10*b*c + b^10*c + d^10 + b^10 + d*b^2*c + d*b*c + b^2*c + 1
        """
    def associated_primes(self, monomial_ideal):
        """
        This function computes the associated primes of the passed-in
        monomial ideal.

        INPUT:

        - ``monomial_ideal`` -- the monomial ideal to decompose

        OUTPUT:

        A list of the associated primes of the monomial ideal. These ideals
        are constructed in the same ring as monomial_ideal is.

        EXAMPLES::

            sage: R.<d,b,c>=QQ[] # optional - frobby
            sage: I=[d*b*c,b^2*c,b^10,d^10]*R # optional - frobby
            sage: frobby.associated_primes(I)   # optional - frobby
            [Ideal (d, b) of Multivariate Polynomial Ring in d, b, c over Rational Field,
            Ideal (d, b, c) of Multivariate Polynomial Ring in d, b, c over Rational Field]
        """
    def dimension(self, monomial_ideal):
        """
        This function computes the dimension of the passed-in
        monomial ideal.

        INPUT:

        - ``monomial_ideal`` -- the monomial ideal to decompose

        OUTPUT: the dimension of the zero set of the ideal

        EXAMPLES::

            sage: R.<d,b,c>=QQ[] # optional - frobby
            sage: I=[d*b*c,b^2*c,b^10,d^10]*R # optional - frobby
            sage: frobby.dimension(I)   # optional - frobby
            1
        """
    def irreducible_decomposition(self, monomial_ideal):
        """
        This function computes the irreducible decomposition of the passed-in
        monomial ideal. I.e. it computes the unique minimal list of
        irreducible monomial ideals whose intersection equals monomial_ideal.

        INPUT:

        - ``monomial_ideal`` -- the monomial ideal to decompose

        OUTPUT:

        A list of the unique irredundant irreducible components of
        monomial_ideal. These ideals are constructed in the same ring
        as monomial_ideal is.

        EXAMPLES:

        This is a simple example of computing irreducible decomposition. ::

            sage: # optional - frobby
            sage: (x, y, z) = QQ['x,y,z'].gens()
            sage: id = ideal(x ** 2, y ** 2, x * z, y * z)
            sage: decom = frobby.irreducible_decomposition(id)
            sage: true_decom = [ideal(x, y), ideal(x ** 2, y ** 2, z)]
            sage: set(decom) == set(true_decom) # use sets to ignore order
            True

        We now try the special case of the zero ideal in different rings.

        We should also try PolynomialRing(QQ, names=[]), but it has a bug
        which makes that impossible (see :issue:`3028`). ::

            sage: # optional - frobby
            sage: rings = [ZZ['x'], CC['x,y']]
            sage: allOK = True
            sage: for ring in rings:
            ....:     id0 = ring.ideal(0)
            ....:     decom0 = frobby.irreducible_decomposition(id0)
            ....:     allOK = allOK and decom0 == [id0]
            sage: allOK
            True

        Finally, we try the ideal that is all of the ring in different
        rings. ::

            sage: # optional - frobby
            sage: rings = [ZZ['x'], CC['x,y']]
            sage: allOK = True
            sage: for ring in rings:
            ....:     id1 = ring.ideal(1)
            ....:     decom1 = frobby.irreducible_decomposition(id1)
            ....:     allOK = allOK and decom1 == [id1]
            sage: allOK
            True
        """

frobby: Incomplete
