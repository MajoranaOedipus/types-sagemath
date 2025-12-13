from sage.structure.sage_object import SageObject as SageObject

class Image(SageObject):
    def __init__(self, mode, size, color: str = 'white') -> None:
        """
        Create a new image with the given mode and size.

        INPUT:

        - ``mode`` -- string. The mode to use for the new image. Valid
          options are:

              * ``'1'`` (1-bit pixels, black and white, stored with
                one pixel per byte)

              * ``'L'`` (8-bit pixels, black and white)

              * ``'P'`` (8-bit pixels, mapped to any other mode using
                a color palette)

              * ``'RGB'`` (3x8-bit pixels, true color)

              * ``'RGBA'`` (4x8-bit pixels, true color with
                transparency mask)

              * ``'CMYK'`` (4x8-bit pixels, color separation)

              * ``'YCbCr'`` (3x8-bit pixels, color video format)

              * ``'LAB'`` (3x8-bit pixels, the L*a*b color space)

              * ``'HSV'`` (3x8-bit pixels, Hue, Saturation, Value
                color space)

              * ``'I'`` (32-bit signed integer pixels)

              * ``'F'`` (32-bit floating point pixels)

        - ``size`` -- 2-tuple, containing (width, height) in pixels

        - ``color`` -- string, numeric or tuple of numeric. What colour to use
          for the image. Default is black.  If given, this should be a
          a tuple with one value per band. When creating RGB images,
          you can also use colour strings as supported by the
          ImageColor module.  If the colour is None, the image is not
          initialised.

        OUTPUT: a new :class:`Image` object

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: Image('P', (16, 16), 13)
            16x16px 8-bit Color image
        """
    @property
    def pil(self):
        """
        Access the wrapped PIL(low) Image.

        OUTPUT: the underlying ``PIL.Image.Image object``

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('RGB', (16, 16), 'white')
            sage: img.pil
            <PIL.Image.Image image mode=RGB size=16x16...>
        """
    def pixels(self):
        """
        Return the pixel map.

        OUTPUT:

        The PIL PixelAccess object that allows you to get/set the
        pixel data.

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('RGB', (16, 16), 'white')
            sage: img.pixels()
            <PixelAccess object at 0x...>
        """
    def mode(self):
        """
        Return the color mode.

        OUTPUT: string; as given when constructing the image

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('YCbCr', (16, 16), 'white')
            sage: img.mode()
            'YCbCr'
        """
    def width(self):
        """
        Return the horizontal dimension in pixels.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('1', (12, 34), 'white')
            sage: img.width()
            12
            sage: img.height()
            34
        """
    def height(self):
        """
        Return the vertical dimension in pixels.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('1', (12, 34), 'white')
            sage: img.width()
            12
            sage: img.height()
            34
        """
    def save(self, filename) -> None:
        """
        Save the bitmap image.

        INPUT:

        - ``filename`` -- string; the filename to save as. The given
          extension automatically determines the image file type

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('P', (12, 34), 13)
            sage: filename = tmp_filename(ext='.png')
            sage: img.save(filename)
            sage: with open(filename, 'rb') as f:
            ....:     f.read(4) == b'\\x89PNG'
            True
        """
    def show(self) -> None:
        """
        Show this image immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES::

            sage: from sage.repl.image import Image
            sage: img = Image('1', (12, 34), 'white')
            sage: img.show()
        """
