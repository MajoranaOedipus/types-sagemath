from .graded_ring_element import FormsRingElement as FormsRingElement

class FormsElement(FormsRingElement):
    """
    (Hecke) modular forms.
    """
    def __init__(self, parent, rat) -> None:
        '''
        An element of a space of (Hecke) modular forms.

        INPUT:

        - ``parent`` -- a modular form space

        - ``rat`` -- a rational function which corresponds to a
          modular form in the modular form space

        OUTPUT:

        A (Hecke) modular form element corresponding to the given rational function
        with the given parent space.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: (x,y,z,d)=var("x,y,z,d")
            sage: MF = ModularForms(n=5, k=20/3, ep=1)
            sage: MF.default_prec(3)
            sage: el = MF(x^5*d-y^2*d)
            sage: el
            q - 9/(200*d)*q^2 + O(q^3)
            sage: el.rat()
            x^5*d - y^2*d
            sage: el.parent()
            ModularForms(n=5, k=20/3, ep=1) over Integer Ring
            sage: el.rat().parent()
            Fraction Field of Multivariate Polynomial Ring in x, y, z, d over Integer Ring

            sage: subspace = MF.subspace([MF.gen(1)])
            sage: ss_el = subspace(x^5*d-y^2*d)
            sage: ss_el == el
            True
            sage: ss_el.parent()
            Subspace of dimension 1 of ModularForms(n=5, k=20/3, ep=1) over Integer Ring
        '''
    def coordinate_vector(self):
        """
        Return the coordinate vector of ``self`` with
        respect to ``self.parent().gens()``.

        .. NOTE::

            This uses the corresponding function of the
            parent. If the parent has not defined a coordinate
            vector function or a module for coordinate vectors
            then an exception is raised by the parent
            (default implementation).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.gen(0).coordinate_vector().parent()
            Vector space of dimension 3 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: MF.gen(0).coordinate_vector()
            (1, 0, 0)
            sage: subspace = MF.subspace([MF.gen(0), MF.gen(2)])
            sage: subspace.gen(0).coordinate_vector().parent()
            Vector space of dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: subspace.gen(0).coordinate_vector()
            (1, 0)
            sage: subspace.gen(0).coordinate_vector() == subspace.coordinate_vector(subspace.gen(0))
            True
        """
    def ambient_coordinate_vector(self):
        """
        Return the coordinate vector of ``self`` with
        respect to ``self.parent().ambient_space().gens()``.

        The returned coordinate vector is an element
        of ``self.parent().module()``.

        .. NOTE::

            This uses the corresponding function of the
            parent. If the parent has not defined a coordinate
            vector function or an ambient module for
            coordinate vectors then an exception is raised
            by the parent (default implementation).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.gen(0).ambient_coordinate_vector().parent()
            Vector space of dimension 3 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: MF.gen(0).ambient_coordinate_vector()
            (1, 0, 0)
            sage: subspace = MF.subspace([MF.gen(0), MF.gen(2)])
            sage: subspace.gen(0).ambient_coordinate_vector().parent()
            Vector space of degree 3 and dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            Basis matrix:
            [1 0 0]
            [0 0 1]
            sage: subspace.gen(0).ambient_coordinate_vector()
            (1, 0, 0)
            sage: subspace.gen(0).ambient_coordinate_vector() == subspace.ambient_coordinate_vector(subspace.gen(0))
            True
        """
    def lseries(self, num_prec=None, max_imaginary_part: int = 0, max_asymp_coeffs: int = 40):
        """
        Return the `L`-series of ``self`` if ``self`` is modular and holomorphic.

        This relies on the (pari) based function ``Dokchitser``.

        INPUT:

        - ``num_prec`` -- integer denoting the to-be-used numerical precision.
          If integer ``num_prec=None`` (default) the default
          numerical precision of the parent of ``self`` is used.

        - ``max_imaginary_part`` -- a real number (default: 0), indicating up
          to which imaginary part the `L`-series is going to be studied

        - ``max_asymp_coeffs`` -- integer (default: 40)

        OUTPUT:

        An interface to Tim Dokchitser's program for computing `L`-series, namely
        the series given by the Fourier coefficients of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform.eis_series import eisenstein_series_lseries
            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: f = ModularForms(n=3, k=4).E4()/240
            sage: L = f.lseries()
            sage: L
            L-series associated to the modular form 1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + O(q^5)
            sage: L.conductor
            1
            sage: L(1).prec()
            53
            sage: L.check_functional_equation() < 2^(-50)
            True
            sage: L(1)
            -0.0304484570583...
            sage: abs(L(1) - eisenstein_series_lseries(4)(1)) < 2^(-53)
            True
            sage: L.derivative(1, 1)
            -0.0504570844798...
            sage: L.derivative(1, 2)/2
            -0.0350657360354...
            sage: L.taylor_series(1, 3)
            -0.0304484570583... - 0.0504570844798...*z - 0.0350657360354...*z^2 + O(z^3)
            sage: coeffs = f.q_expansion_vector(min_exp=0, max_exp=20, fix_d=True)
            sage: sum([coeffs[k] * ZZ(k)^(-10) for k in range(1,len(coeffs))]).n(53)
            1.00935215408...
            sage: L(10)
            1.00935215649...

            sage: f = ModularForms(n=6, k=4).E4()
            sage: L = f.lseries(num_prec=200)
            sage: L.conductor
            3
            sage: L.check_functional_equation() < 2^(-180)
            True
            sage: L(1)
            -2.92305187760575399490414692523085855811204642031749788...
            sage: L(1).prec()
            200
            sage: coeffs = f.q_expansion_vector(min_exp=0, max_exp=20, fix_d=True)
            sage: sum([coeffs[k] * ZZ(k)^(-10) for k in range(1,len(coeffs))]).n(53)
            24.2281438789...
            sage: L(10).n(53)
            24.2281439447...

            sage: f = ModularForms(n=8, k=6, ep=-1).E6()
            sage: L = f.lseries()
            sage: L.check_functional_equation() < 2^(-45)
            True
            sage: L.taylor_series(3, 3)
            0.000000000000... + 0.867197036668...*z + 0.261129628199...*z^2 + O(z^3)
            sage: coeffs = f.q_expansion_vector(min_exp=0, max_exp=20, fix_d=True)
            sage: sum([coeffs[k]*k^(-10) for k in range(1,len(coeffs))]).n(53)
            -13.0290002560...
            sage: L(10).n(53)
            -13.0290184579...

            sage: # long time
            sage: f = (ModularForms(n=17, k=24).Delta()^2)
            sage: L = f.lseries()
            sage: L.check_functional_equation() < 2^(-50)
            True
            sage: L.taylor_series(12, 3)
            0.000683924755280... - 0.000875942285963...*z + 0.000647618966023...*z^2 + O(z^3)
            sage: coeffs = f.q_expansion_vector(min_exp=0, max_exp=20, fix_d=True)
            sage: sum([coeffs[k]*k^(-30) for k in range(1,len(coeffs))]).n(53)
            9.31562890589...e-10
            sage: L(30).n(53)
            9.31562890589...e-10

            sage: f = ModularForms(n=infinity, k=2, ep=-1).f_i()
            sage: L = f.lseries()
            sage: L.check_functional_equation() < 2^(-50)
            True
            sage: L.taylor_series(1, 3)
            0.000000000000... + 5.76543616701...*z + 9.92776715593...*z^2 + O(z^3)
            sage: coeffs = f.q_expansion_vector(min_exp=0, max_exp=20, fix_d=True)
            sage: sum([coeffs[k] * ZZ(k)^(-10) for k in range(1,len(coeffs))]).n(53)
            -23.9781792831...
            sage: L(10).n(53)
            -23.9781792831...
        """
