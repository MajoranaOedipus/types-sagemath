from docutils.transforms import Transform

default_role: str

def process_docstring_aliases(app, what, name, obj, options, docstringlines) -> None:
    """
    Change the docstrings for aliases to point to the original object.
    """
def process_directives(app, what, name, obj, options, docstringlines) -> None:
    """
    Remove 'nodetex' and other directives from the first line of any
    docstring where they appear.
    """
def process_docstring_cython(app, what, name, obj, options, docstringlines) -> None:
    """
    Remove Cython's filename and location embedding.
    """
def process_docstring_module_title(app, what, name, obj, options, docstringlines) -> None:
    """
    Removes the first line from the beginning of the module's docstring.  This
    corresponds to the title of the module's documentation page.
    """
def process_dollars(app, what, name, obj, options, docstringlines) -> None:
    """
    Replace dollar signs with backticks.

    See sage.misc.sagedoc.process_dollars for more information.
    """
def process_inherited(app, what, name, obj, options, docstringlines) -> None:
    """
    If we're including inherited members, omit their docstrings.
    """
def skip_TESTS_block(app, what, name, obj, options, docstringlines) -> None:
    '''
    Skip blocks labeled "TESTS:".

    See sage.misc.sagedoc.skip_TESTS_block for more information.
    '''

class SagemathTransform(Transform):
    '''
    Transform for code-blocks.

    This allows Sphinx to treat code-blocks with prompt "sage:" as
    associated with the pycon lexer, and in particular, to change
    "<BLANKLINE>" to a blank line.
    '''
    default_priority: int
    def apply(self) -> None: ...

def setup(app) -> None: ...
