from . import Feature as Feature, FeatureTestResult as FeatureTestResult

class JoinFeature(Feature):
    '''
    Join of several :class:`~sage.features.Feature` instances.

    This creates a new feature as the union of the given features. Typically
    these are executables of an SPKG. For an example, see
    :class:`~sage.features.rubiks.Rubiks`.

    Furthermore, this can be the union of a single feature. This is used to map
    the given feature to a more convenient name to be used in ``optional`` tags
    of doctests. Thus you can equip a feature such as a
    :class:`~sage.features.PythonModule` with a tag name that differs from the
    systematic tag name. As an example for this use case, see
    :class:`~sage.features.meataxe.Meataxe`.

    EXAMPLES::

        sage: from sage.features import Executable
        sage: from sage.features.join_feature import JoinFeature
        sage: F = JoinFeature("shell-boolean",
        ....:                 (Executable(\'shell-true\', \'true\'),
        ....:                  Executable(\'shell-false\', \'false\')))
        sage: F.is_present()
        FeatureTestResult(\'shell-boolean\', True)
        sage: F = JoinFeature("asdfghjkl",
        ....:                 (Executable(\'shell-true\', \'true\'),
        ....:                  Executable(\'xxyyyy\', \'xxyyyy-does-not-exist\')))
        sage: F.is_present()
        FeatureTestResult(\'xxyyyy\', False)
    '''
    def __init__(self, name, features, spkg=None, url=None, description=None, type=None, **kwds) -> None:
        '''
        TESTS:

        The empty join feature is present::

            sage: from sage.features.join_feature import JoinFeature
            sage: JoinFeature("empty", ()).is_present()
            FeatureTestResult(\'empty\', True)
        '''
    def hide(self) -> None:
        """
        Hide this feature and all its joined features.

        EXAMPLES::

            sage: from sage.features.sagemath import sage__groups
            sage: f = sage__groups()
            sage: f.hide()
            sage: f._features[0].is_present()
            FeatureTestResult('sage.groups.perm_gps.permgroup', False)

            sage: f.require()
            Traceback (most recent call last):
            ...
            FeatureNotPresentError: sage.groups is not available.
            Feature `sage.groups` is hidden.
            Use method `unhide` to make it available again.
        """
    def unhide(self) -> None:
        """
        Revert what :meth:`hide` did.

        EXAMPLES::

            sage: from sage.features.sagemath import sage__groups
            sage: f = sage__groups()
            sage: f.hide()
            sage: f.is_present()
            FeatureTestResult('sage.groups', False)
            sage: f._features[0].is_present()
            FeatureTestResult('sage.groups.perm_gps.permgroup', False)

            sage: f.unhide()
            sage: f.is_present()    # optional sage.groups
            FeatureTestResult('sage.groups', True)
            sage: f._features[0].is_present() # optional sage.groups
            FeatureTestResult('sage.groups.perm_gps.permgroup', True)
        """
