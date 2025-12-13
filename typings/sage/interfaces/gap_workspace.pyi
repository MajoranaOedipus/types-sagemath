from sage.env import DOT_SAGE as DOT_SAGE, GAP_ROOT_PATHS as GAP_ROOT_PATHS, HOSTNAME as HOSTNAME

def gap_workspace_file(system: str = 'gap', name: str = 'workspace', dir=None):
    '''
    Return the filename for the GAP workspace.

    INPUT:

    - ``system`` -- the name of the system, either ``\'gap\'`` or
      ``\'libgap\'``

    - ``name`` -- the kind of workspace, usually ``\'workspace\'`` but
      the library interface also uses other files

    - ``dir`` -- the directory where the workspaces should be stored
      By default, this is ``DOT_SAGE/gap``

    EXAMPLES::

        sage: from sage.interfaces.gap_workspace import gap_workspace_file
        sage: gap_workspace_file("foo", "bar", "/somewhere")
        \'/somewhere/foo-bar-...\'

    TESTS::

        sage: from sage.env import DOT_SAGE
        sage: D = gap_workspace_file()
        sage: D.startswith(os.path.join(DOT_SAGE, "gap", "gap-workspace-"))
        True

    Check that the name generated is independent of the session::

        sage: from subprocess import Popen, PIPE
        sage: import sys
        sage: cmd = \'import sage.all, sage.interfaces.gap_workspace; print(sage.interfaces.gap_workspace.gap_workspace_file())\'
        sage: name1 = Popen([sys.executable, \'-c\', cmd], stdout=PIPE).communicate()[0]
        sage: name2 = Popen([sys.executable, \'-c\', cmd], stdout=PIPE).communicate()[0]
        sage: assert name1 == name2
    '''
def prepare_workspace_dir(dir=None):
    '''
    Create and clean up the directory for GAP workspaces.

    INPUT:

    - ``dir`` -- the directory where the workspaces should be stored
      By default, this is ``DOT_SAGE/gap``

    OUTPUT: the actual workspace directory

    EXAMPLES::

        sage: from sage.interfaces.gap_workspace import prepare_workspace_dir
        sage: prepare_workspace_dir()
        \'.../gap\'

    TESTS::

        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     prepare_workspace_dir(os.path.join(d, "new"))
        \'.../new\'
    '''
