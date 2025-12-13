from sage.quadratic_forms.quadratic_form__mass__Conway_Sloane_masses import conway_cross_product_doubled_power as conway_cross_product_doubled_power, conway_diagonal_factor as conway_diagonal_factor, conway_mass as conway_mass, conway_octane_of_this_unimodular_Jordan_block_at_2 as conway_octane_of_this_unimodular_Jordan_block_at_2, conway_p_mass as conway_p_mass, conway_species_list_at_2 as conway_species_list_at_2, conway_species_list_at_odd_prime as conway_species_list_at_odd_prime, conway_standard_mass as conway_standard_mass, conway_standard_p_mass as conway_standard_p_mass, conway_type_factor as conway_type_factor, is_even as is_even, is_odd as is_odd, parity as parity
from sage.quadratic_forms.quadratic_form__mass__Siegel_densities import Kitaoka_mass_at_2 as Kitaoka_mass_at_2, Pall_mass_density_at_odd_prime as Pall_mass_density_at_odd_prime, Watson_mass_at_2 as Watson_mass_at_2, mass__by_Siegel_densities as mass__by_Siegel_densities, mass_at_two_by_counting_mod_power as mass_at_two_by_counting_mod_power

def shimura_mass__maximal(self) -> None:
    """
    Use Shimura's exact mass formula to compute the mass of a maximal
    quadratic lattice. This works for any totally real number field,
    but has a small technical restriction when `n` is odd.

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.shimura_mass__maximal()
    """
def GHY_mass__maximal(self) -> None:
    """
    Use the GHY formula to compute the mass of a (maximal?) quadratic
    lattice. This works for any number field.

    REFERENCES:

    See [GHY, Prop 7.4 and 7.5, p121] and [GY, Thrm 10.20, p25].

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.GHY_mass__maximal()
    """
