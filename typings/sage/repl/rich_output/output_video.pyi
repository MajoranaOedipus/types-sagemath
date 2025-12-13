from _typeshed import Incomplete
from sage.repl.rich_output.buffer import OutputBuffer as OutputBuffer
from sage.repl.rich_output.output_basic import OutputBase as OutputBase

class OutputVideoBase(OutputBase):
    video: Incomplete
    loop: Incomplete
    def __init__(self, video, loop: bool = True) -> None:
        """
        Abstract base class for rich video output.

        INPUT:

        - ``video`` -- :class:`~sage.repl.rich_output.buffer.OutputBuffer`;
          the video data
        - ``loop`` -- boolean; whether to repeat the video in an endless loop

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputVideoOgg
            sage: OutputVideoOgg.example()  # indirect doctest
            OutputVideoOgg container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample video output container.

        This static method is meant for doctests, so they can easily
        construct an example.  The method is implemented in the abstract
        :class:`OutputVideoBase` class, but should get invoked on a
        concrete subclass for which an actual example can exist.

        OUTPUT: an instance of the class on which this method is called

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputVideoOgg
            sage: OutputVideoOgg.example()
            OutputVideoOgg container
            sage: OutputVideoOgg.example().video
            buffer containing 5612 bytes
            sage: OutputVideoOgg.example().ext
            '.ogv'
            sage: OutputVideoOgg.example().mimetype
            'video/ogg'
        """
    def html_fragment(self, url, link_attrs: str = ''):
        '''
        Construct a HTML fragment for embedding this video.

        INPUT:

        - ``url`` -- string; the URL where the data of this video can be found

        - ``link_attrs`` -- string; can be used to style the fallback link
          which is presented to the user if the video is not supported

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputVideoOgg
            sage: print(OutputVideoOgg.example().html_fragment
            ....:       (\'foo\', \'class="bar"\').replace(\'><\',\'>\\n<\'))
            <video autoplay="autoplay" controls="controls" loop="loop">
            <source src="foo" type="video/ogg" />
            <p>
            <a target="_new" href="foo" class="bar">Download video/ogg video</a>
            </p>
            </video>
        '''

class OutputVideoOgg(OutputVideoBase):
    """
    Ogg video, Ogg Theora in particular.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoOgg
        sage: OutputVideoOgg.example()
        OutputVideoOgg container
    """
    ext: str
    mimetype: str

class OutputVideoWebM(OutputVideoBase):
    """
    WebM video.

    The video can be encoded using VP8, VP9 or an even more recent codec.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoWebM
        sage: OutputVideoWebM.example()
        OutputVideoWebM container
    """
    ext: str
    mimetype: str

class OutputVideoMp4(OutputVideoBase):
    """
    MPEG 4 video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoMp4
        sage: OutputVideoMp4.example()
        OutputVideoMp4 container
    """
    ext: str
    mimetype: str

class OutputVideoFlash(OutputVideoBase):
    """
    Flash video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoFlash
        sage: OutputVideoFlash.example()
        OutputVideoFlash container
    """
    ext: str
    mimetype: str

class OutputVideoMatroska(OutputVideoBase):
    """
    Matroska Video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoMatroska
        sage: OutputVideoMatroska.example()
        OutputVideoMatroska container
    """
    ext: str
    mimetype: str

class OutputVideoAvi(OutputVideoBase):
    """
    AVI video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoAvi
        sage: OutputVideoAvi.example()
        OutputVideoAvi container
    """
    ext: str
    mimetype: str

class OutputVideoWmv(OutputVideoBase):
    """
    Windows Media Video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoWmv
        sage: OutputVideoWmv.example()
        OutputVideoWmv container
    """
    ext: str
    mimetype: str

class OutputVideoQuicktime(OutputVideoBase):
    """
    Quicktime video.

    EXAMPLES::

        sage: from sage.repl.rich_output.output_catalog import OutputVideoQuicktime
        sage: OutputVideoQuicktime.example()
        OutputVideoQuicktime container
    """
    ext: str
    mimetype: str
