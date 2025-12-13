def sphinxify(docstring, format: str = 'html'):
    '''
    Run Sphinx on a ``docstring``, and output the processed documentation.

    INPUT:

    - ``docstring`` -- string; a ReST-formatted docstring

    - ``format`` -- string (default: ``\'html\'``); either ``\'html\'`` or
      ``\'text\'``

    OUTPUT:

    - ``string`` -- Sphinx-processed documentation, in either HTML or
      plain text format, depending on the value of ``format``

    EXAMPLES::

        sage: from sage.misc.sphinxify import sphinxify
        sage: sphinxify(\'A test\')
        \'<div class="docstring">\\n    \\n  <p>A test</p>\\n\\n\\n</div>\'
        sage: sphinxify(\'**Testing**\\n`monospace`\')
        \'<div class="docstring"...<strong>Testing</strong>\\n<span class="math...</p>\\n\\n\\n</div>\'
        sage: sphinxify(\'`x=y`\')
        \'<div class="docstring">\\n    \\n  <p><span class="math notranslate nohighlight">x=y</span></p>\\n\\n\\n</div>\'
        sage: sphinxify(\'`x=y`\', format=\'text\')
        \'x=y\\n\'
        sage: sphinxify(\':math:`x=y`\', format=\'text\')
        \'x=y\\n\'

    TESTS::

        sage: n = len(sys.path)
        sage: _ = sphinxify(\'A test\')
        sage: assert n == len(sys.path)
    '''
