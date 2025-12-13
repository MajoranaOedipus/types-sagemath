from _typeshed import Incomplete

edit_template: Incomplete
template_defaults: Incomplete

def file_and_line(obj):
    """
    Look up source file and line number of ``obj``.

    If the file lies in the Sage library, the path name of the
    corresponding file in the current branch (i.e., the file that gets
    copied into the Sage library upon running 'sage -br').  Note that
    the first line of a file is considered to be 1 rather than 0
    because most editors think that this is the case.

    AUTHORS:

    - Nils Bruin (2007-10-03)
    - Simon King (2011-05): Use :mod:`~sage.misc.sageinspect` to get the file
      and the line.

    EXAMPLES::

        sage: import sage.misc.edit_module as edit_module
        sage: edit_module.file_and_line(sage.cpython)
        ('...sage/cpython/__init__.py', 0)

    The following tests against a bug that was fixed in :issue:`11298`::

        sage: edit_module.file_and_line(x)                                              # needs sage.symbolic
        ('...sage/symbolic/expression...pyx', ...)
    """
def template_fields(template):
    '''
    Given a String.Template object, returns the fields.

    AUTHOR:

    Nils Bruin (2007-10-22)

    EXAMPLES::

        sage: from sage.misc.edit_module import template_fields
        sage: from string import Template
        sage: t = Template("Template ${one} with ${two} and ${three}")
        sage: sorted(template_fields(t))
        [\'one\', \'three\', \'two\']
    '''
def set_edit_template(template_string) -> None:
    '''
    Set the default edit template string.

    It should reference ``${file}`` and ``${line}``. This routine normally
    needs to be called prior to using \'edit\'. However, if the editor
    set in the shell variable :envvar:`EDITOR` is known, then the system will
    substitute an appropriate template for you. See
    edit_module.template_defaults for the recognised templates.

    AUTHOR:

    Nils Bruin (2007-10-03)

    EXAMPLES::

        sage: from sage.misc.edit_module import set_edit_template
        sage: set_edit_template("echo EDIT ${file}:${line}")
        sage: edit(sage)      # not tested
        EDIT /usr/local/sage/src/sage/__init__.py:1
    '''
def set_editor(editor_name, opts: str = '') -> None:
    """
    Set the editor to be used by the edit command by basic editor name.

    Currently, the system only knows appropriate call strings for a
    limited number of editors. If you want to use another editor, you
    should set the whole edit template via :func:`set_edit_template`.

    AUTHOR:

    Nils Bruin (2007-10-05)

    EXAMPLES::

        sage: from sage.misc.edit_module import set_editor
        sage: set_editor('vi')
        sage: sage.misc.edit_module.edit_template.template
        'vi -c ${line} ${file}'
    """
def edit(obj, editor=None, bg=None) -> None:
    '''nodetex
    Open source code of ``obj`` in editor of your choice.

    INPUT:

    - editor -- string (default: ``None``); if given, use specified editor.
      Choice is stored for next time.

    AUTHOR:

    Nils Bruin (2007-10-03)

    EXAMPLES:

    This is a typical example of how to use this routine::

        # make some object obj
        sage: edit(obj)    # not tested

    Now for more details and customization::

        sage: import sage.misc.edit_module as m
        sage: m.set_edit_template("vi -c ${line} ${file}")

    In fact, since ``vi`` is a well-known editor, you could also just use::

        sage: m.set_editor("vi")

    To illustrate::

        sage: m.edit_template.template
        \'vi -c ${line} ${file}\'

    And if your environment variable :envvar:`EDITOR` is set to a recognised
    editor, you would not have to set anything.

    To edit the source of an object, just type something like::

        sage: edit(edit)           # not tested
    '''
def edit_devel(self, filename, linenum) -> None:
    """
    This function is for internal use and is called by IPython when you use
    the IPython commands ``%edit`` or ``%ed``.

    This hook calls the default implementation, but changes the filename for
    files that appear to be from the sage library: if the filename begins with
    'SAGE_LOCAL/lib/python.../site-packages', it replaces this by
    'SAGE_ROOT/src'.

    EXAMPLES::

        sage: %edit gcd         # indirect doctest, not tested
        sage: %ed gcd           # indirect doctest, not tested

    The above should open your favorite editor (as stored in the environment
    variable :envvar:`EDITOR`) with the file in which gcd is defined, and when your
    editor supports it, also at the line in which gcd is defined.
    """
