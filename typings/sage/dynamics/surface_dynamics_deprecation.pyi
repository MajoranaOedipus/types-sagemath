deprecation_msg: str

def surface_dynamics_deprecation(name) -> None:
    '''
    TESTS::

        sage: from sage.dynamics.surface_dynamics_deprecation import surface_dynamics_deprecation
        sage: surface_dynamics_deprecation("HeYhEy")
        doctest:...: DeprecationWarning: HeYhEy is deprecated and will be removed from Sage.
        You are advised to install the surface_dynamics package via:
            sage -pip install surface_dynamics
        If you do not have write access to the Sage installation you can
        alternatively do
            sage -pip install surface_dynamics --user
        The package surface_dynamics subsumes all flat surface related
        computation that are currently available in Sage. See more
        information at
            http://www.labri.fr/perso/vdelecro/surface-dynamics/latest/
        See https://github.com/sagemath/sage/issues/20695 for details.
    '''
