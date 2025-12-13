from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.pager import pager as pager
from sage.misc.superseded import deprecation as deprecation
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.structure.sage_object import SageObject as SageObject

class TachyonRT(SageObject):
    """
    The Tachyon Ray Tracer.

    Usage:
    ``tachyon_rt(model, outfile='sage.png', verbose=1, block=True, extra_opts='')``

    INPUT:

    - ``model`` -- string that describes a 3d model in
      the Tachyon modeling format. Type ``sage.interfaces.tachyon?`` for a
      description of this format.

    - ``outfile`` -- (default: ``'sage.png'``) output filename;
      the extension of the filename determines the type. Supported types
      include:

      - ``tga`` -- 24-bit (uncompressed)

      - ``bmp`` -- 24-bit Windows BMP (uncompressed)

      - ``ppm`` -- 24-bit PPM (uncompressed)

      - ``rgb`` -- 24-bit SGI RGB (uncompressed)

      - ``png`` -- 24-bit PNG (compressed, lossless)

    - ``verbose`` -- integer; (default: 1)

      - ``0`` -- silent

      - ``1`` -- some output

      - ``2`` -- very verbose output

    - ``block`` -- boolean (default: ``True``); if ``False``, run the
      rendering command in the background

    - ``extra_opts`` -- passed directly to tachyon command
      line. Use ``tachyon_rt.usage()`` to see some of the possibilities

    OUTPUT: some text may be displayed onscreen

    - The file outfile is created.

    EXAMPLES:

    .. automethod:: __call__
    """
    def __call__(self, model, outfile: str = 'sage.png', verbose: int = 1, extra_opts: str = '') -> None:
        """
        This executes the tachyon program, given a scene file input.

        INPUT:

        - ``model`` -- string; the tachyon model

        - ``outfile`` -- string (default: ``'sage.png'``); the filename
          to save the model to

        - ``verbose`` -- 0, 1, (default) or 2; the verbosity level

        - ``extra_opts`` -- string (default: empty string); extra
          options that will be appended to the tachyon commandline

        EXAMPLES::

            sage: from sage.interfaces.tachyon import TachyonRT
            sage: tgen = Tachyon()
            sage: tgen.texture('t1')
            sage: tgen.sphere((0,0,0),1,'t1')
            sage: tgen.str()[30:40]
            'resolution'
            sage: t = TachyonRT()
            sage: import os
            sage: t(tgen.str(), outfile=os.devnull)
            tachyon ...
            Tachyon Parallel/Multiprocessor Ray Tracer...

        TESTS::

            sage: from sage.env import SAGE_EXTCODE
            sage: filename = os.path.join(SAGE_EXTCODE, 'doctest', 'invalid', 'syntax_error.tachyon')
            sage: with open(filename, 'r') as f:
            ....:     syntax_error = f.read()
            sage: t(syntax_error, outfile=os.devnull)
            Traceback (most recent call last):
            ...
            RuntimeError: Tachyon Parallel/Multiprocessor Ray Tracer...
            ...
            Parser failed due to an input file syntax error.
            Aborting render.
        """
    def usage(self, use_pager: bool = True) -> None:
        """
        Return the basic description of using the Tachyon raytracer (simply
        what is returned by running tachyon with no input).  The output is
        paged unless ``use_pager=False``.

        TESTS::

            sage: from sage.interfaces.tachyon import TachyonRT
            sage: t = TachyonRT()
            sage: t.usage(use_pager=False)
            ...
              tachyon modelfile [options]...
            <BLANKLINE>
            Model file formats supported:
              filename.dat ...
        """
    @cached_method
    def version(self):
        """
        Return the version of the Tachyon raytracer being used.

        TESTS::

            sage: tachyon_rt.version()  # random
            0.98.9
            sage: tachyon_rt.version() >= '0.98.9'
            True
        """
    def help(self, use_pager: bool = True) -> None:
        """
        Deprecated: type 'sage.interfaces.tachyon?' for help.

        TESTS::

            sage: from sage.interfaces.tachyon import TachyonRT
            sage: t = TachyonRT()
            sage: t.help(use_pager=False)
            doctest:...: DeprecationWarning: type 'sage.interfaces.tachyon?' for help
            See https://github.com/sagemath/sage/issues/34066 for details.
        """

tachyon_rt: Incomplete
