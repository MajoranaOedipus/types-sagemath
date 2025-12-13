from _typeshed import Incomplete
from sage.repl.prompts import SagePrompts as SagePrompts

SAGE_EXTENSION: str

class SageIpythonConfiguration:
    def colors(self):
        """
        Return the IPython color palette.

        This returns ``'nocolor'`` during doctests to avoid ANSI escape
        sequences.

        EXAMPLES::

            sage: from sage.repl.configuration import sage_ipython_config
            sage: sage_ipython_config.simple_prompt()
            True
        """
    def simple_prompt(self):
        """
        Return whether to use the simple prompt.

        This returns ``True`` during doctests to avoid ANSI escape sequences.

        EXAMPLES::

            sage: from sage.repl.configuration import sage_ipython_config
            sage: sage_ipython_config.simple_prompt()
            True
        """
    def term_title(self):
        """
        Return whether to set the terminal title.

        This returns false during doctests to avoid ANSI escape sequences.

        EXAMPLES::

            sage: from sage.repl.configuration import sage_ipython_config
            sage: sage_ipython_config.term_title()
            False
        """
    def default(self):
        """
        Return a new default configuration object.

        EXAMPLES::

            sage: from sage.repl.configuration import sage_ipython_config
            sage: conf = sage_ipython_config.default()
            sage: type(conf)
            <class 'traitlets.config.loader.Config'>
            sage: 'InteractiveShell' in conf
            True
        """
    def copy(self):
        """
        Return a copy of the current configuration.

        EXAMPLES::

            sage: from sage.repl.configuration import sage_ipython_config
            sage: conf = sage_ipython_config.copy()
            sage: type(conf)
            <class 'traitlets.config.loader.Config'>
            sage: 'InteractiveShell' in conf
            True
        """

sage_ipython_config: Incomplete
