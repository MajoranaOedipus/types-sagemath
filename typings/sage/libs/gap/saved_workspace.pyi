from sage.env import GAP_ROOT_PATHS as GAP_ROOT_PATHS
from sage.interfaces.gap_workspace import gap_workspace_file as gap_workspace_file

def timestamp():
    """
    Return a time stamp for (lib)gap.

    OUTPUT:

    Float. Unix timestamp of the most recently changed GAP/LibGAP file(s). In particular, the
    timestamp increases whenever a gap package is added.

    EXAMPLES::

        sage: from sage.libs.gap.saved_workspace import timestamp
        sage: timestamp()   # random output
        1406642467.25684
        sage: type(timestamp())
        <... 'float'>
    """
def workspace(name: str = 'workspace'):
    """
    Return the filename of the gap workspace and whether it is up to date.

    INPUT:

    - ``name`` -- string; a name that will become part of the
      workspace filename

    OUTPUT:

    Pair consisting of a string and a boolean. The string is the
    filename of the saved libgap workspace (or that it should have if
    it doesn't exist). The boolean is whether the workspace is
    up-to-date. You may use the workspace file only if the boolean is
    ``True``.

    EXAMPLES::

        sage: from sage.libs.gap.saved_workspace import workspace
        sage: ws, up_to_date = workspace()
        sage: ws
        '/.../gap/libgap-workspace-...'
        sage: isinstance(up_to_date, bool)
        True
    """
