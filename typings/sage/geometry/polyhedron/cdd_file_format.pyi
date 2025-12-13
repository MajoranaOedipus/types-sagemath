def cdd_Vrepresentation(cdd_type, vertices, rays, lines, file_output=None):
    """
    Return a string containing the V-representation in cddlib's ext format.

    INPUT:

    - ``file_output`` -- string (optional); a filename to which the
      representation should be written. If set to ``None`` (default),
      representation is returned as a string.

    .. NOTE::

        If there is no vertex given, then the origin will be implicitly
        added. You cannot write the empty V-representation (which cdd would
        refuse to process).

    EXAMPLES::

        sage: from sage.geometry.polyhedron.cdd_file_format import cdd_Vrepresentation
        sage: print(cdd_Vrepresentation('rational', [[0,0]], [[1,0]], [[0,1]]))
        V-representation
        linearity 1 1
        begin
          3 3 rational
          0 0 1
          0 1 0
          1 0 0
        end

    TESTS::

        sage: from sage.misc.temporary_file import tmp_filename
        sage: filename = tmp_filename(ext='.ext')
        sage: cdd_Vrepresentation('rational', [[0,0]], [[1,0]], [[0,1]], file_output=filename)
    """
def cdd_Hrepresentation(cdd_type, ieqs, eqns, file_output=None):
    """
    Return a string containing the H-representation in cddlib's ine format.

    INPUT:

    - ``file_output`` -- string (optional); a filename to which the
      representation should be written. If set to ``None`` (default),
      representation is returned as a string.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.cdd_file_format import cdd_Hrepresentation
        sage: cdd_Hrepresentation('rational', None, [[0,1]])
        'H-representation\\nlinearity 1 1\\nbegin\\n 1 2 rational\\n 0 1\\nend\\n'

    TESTS::

        sage: from sage.misc.temporary_file import tmp_filename
        sage: filename = tmp_filename(ext='.ine')
        sage: cdd_Hrepresentation('rational', None, [[0,1]], file_output=filename)
    """
