from . import Executable as Executable, FeatureTestResult as FeatureTestResult
from .join_feature import JoinFeature as JoinFeature

class Magick(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``magick`` or the deprecated ``convert``.

    EXAMPLES::

        sage: from sage.features.imagemagick import Magick
        sage: Magick().is_present()  # optional - imagemagick
        FeatureTestResult('magick', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.imagemagick import Magick
            sage: isinstance(Magick(), Magick)
            True
        """
    def is_functional(self):
        """
        Return whether command ``magick`` or ``convert`` in the path is functional.

        EXAMPLES::

            sage: from sage.features.imagemagick import Magick
            sage: Magick().is_functional()   # optional - imagemagick
            FeatureTestResult('magick', True)
        """

class ImageMagick(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of
    :ref:`ImageMagick <spkg_imagemagick>`

    Currently, only the availability of the :class:`magick` (or :class:`convert`) program is checked.

    EXAMPLES::

        sage: from sage.features.imagemagick import ImageMagick
        sage: ImageMagick().is_present()  # optional - imagemagick
        FeatureTestResult('imagemagick', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.imagemagick import ImageMagick
            sage: isinstance(ImageMagick(), ImageMagick)
            True
        """

def all_features(): ...
