from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.repl.rich_output.buffer import OutputBuffer as OutputBuffer
from sage.repl.rich_output.output_basic import OutputBase as OutputBase

class OutputImagePng(OutputBase):
    png: Incomplete
    def __init__(self, png) -> None:
        """
        PNG Image.

        .. NOTE::

            Every backend that is capable of displaying any kind of
            graphics is supposed to support the PNG format at least.

        INPUT:

        - ``png`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          PNG image data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImagePng
            sage: OutputImagePng.example()  # indirect doctest
            OutputImagePng container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample PNG output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImagePng`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImagePng
            sage: OutputImagePng.example()
            OutputImagePng container
            sage: OutputImagePng.example().png
            buffer containing 608 bytes
            sage: OutputImagePng.example().png.get().startswith(b'\\x89PNG')
            True
        """

class OutputImageGif(OutputBase):
    gif: Incomplete
    def __init__(self, gif) -> None:
        """
        GIF Image (possibly animated).

        INPUT:

        - ``gif`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          GIF image data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageGif
            sage: OutputImageGif.example()   # indirect doctest
            OutputImageGif container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample GIF output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImageGif`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageGif
            sage: OutputImageGif.example()
            OutputImageGif container
            sage: OutputImageGif.example().gif
            buffer containing 408 bytes
            sage: OutputImageGif.example().gif.get().startswith(b'GIF89a')
            True
        """
    def html_fragment(self):
        '''
        Return a self-contained HTML fragment displaying the image.

        This is a workaround for the Jupyter notebook which doesn\'t support GIF directly.

        OUTPUT: string. HTML fragment for displaying the GIF image

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageGif
            sage: OutputImageGif.example().html_fragment()
            \'<img src="data:image/gif;base64,R0lGODl...zd3t/g4eLj5OVDQQA7"/>\'
        '''

class OutputImageJpg(OutputBase):
    jpg: Incomplete
    def __init__(self, jpg) -> None:
        """
        JPEG Image.

        INPUT:

        - ``jpg`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          JPEG image data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageJpg
            sage: OutputImageJpg.example()   # indirect doctest
            OutputImageJpg container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample JPEG output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImageJpg`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageJpg
            sage: OutputImageJpg.example()
            OutputImageJpg container
            sage: OutputImageJpg.example().jpg
            buffer containing 978 bytes
            sage: OutputImageJpg.example().jpg.get().startswith(b'\\xff\\xd8\\xff\\xe0\\x00\\x10JFIF')
            True
        """

class OutputImageSvg(OutputBase):
    svg: Incomplete
    def __init__(self, svg) -> None:
        """
        SVG Image.

        INPUT:

        - ``svg`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          SVG image data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageSvg
            sage: OutputImageSvg.example()   # indirect doctest
            OutputImageSvg container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample SVG output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImageSvg`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageSvg
            sage: OutputImageSvg.example()
            OutputImageSvg container
            sage: OutputImageSvg.example().svg
            buffer containing 1422 bytes
            sage: b'</svg>' in OutputImageSvg.example().svg.get()
            True
        """

class OutputImagePdf(OutputBase):
    pdf: Incomplete
    def __init__(self, pdf) -> None:
        """
        PDF Image.

        INPUT:

        - ``pdf`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          PDF data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImagePdf
            sage: OutputImagePdf.example()   # indirect doctest
            OutputImagePdf container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample PDF output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImagePdf`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImagePdf
            sage: OutputImagePdf.example()
            OutputImagePdf container
            sage: OutputImagePdf.example().pdf
            buffer containing 4285 bytes
            sage: OutputImagePdf.example().pdf.get().startswith(b'%PDF-1.4')
            True
        """

class OutputImageDvi(OutputBase):
    dvi: Incomplete
    def __init__(self, dvi) -> None:
        """
        DVI Image.

        INPUT:

        - ``dvi`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          DVI data.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageDvi
            sage: OutputImageDvi.example()     # indirect doctest
            OutputImageDvi container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample DVI output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputImageDvi`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputImageDvi
            sage: OutputImageDvi.example()
            OutputImageDvi container
            sage: OutputImageDvi.example().dvi
            buffer containing 212 bytes
            sage: b'TeX output' in OutputImageDvi.example().dvi.get()
            True
        """
