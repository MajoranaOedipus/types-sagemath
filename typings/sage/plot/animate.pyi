from . import plot as plot
from _typeshed import Incomplete
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.temporary_file import tmp_dir as tmp_dir, tmp_filename as tmp_filename
from sage.structure.sage_object import SageObject as SageObject

def animate(frames, **kwds):
    '''
    Animate a list of frames by creating a
    :class:`sage.plot.animate.Animation` object.

    EXAMPLES::

        sage: t = SR.var("t")
        sage: a = animate((cos(c*pi*t) for c in sxrange(1, 2, .2)))
        sage: a.show()              # long time  # optional -- ImageMagick

    See also :mod:`sage.plot.animate` for more examples.
    '''

class Animation(WithEqualityById, SageObject):
    '''
    Return an animation of a sequence of plots of objects.

    INPUT:

    - ``v`` -- iterable of Sage objects; these should preferably be
      graphics objects, but if they aren\'t, then :meth:`make_image` is
      called on them.

    - ``xmin``, ``xmax``, ``ymin``, ``ymax`` -- the ranges of the x and y axes

    - ``**kwds`` -- all additional inputs are passed onto the rendering
      command. E.g., use ``figsize`` to adjust the resolution and aspect
      ratio.

    EXAMPLES::

        sage: x = SR.var("x")
        sage: a = animate([sin(x + float(k)) for k in srange(0, 2*pi, 0.3)],
        ....:             xmin=0, xmax=2*pi, figsize=[2,1])
        sage: print(a)
        Animation with 21 frames
        sage: print(a[:5])
        Animation with 5 frames
        sage: a.show()              # long time  # optional -- ImageMagick
        sage: a[:5].show()          # long time  # optional -- ImageMagick

    The :meth:`show` method takes arguments to specify the
    delay between frames (measured in hundredths of a second, default
    value 20) and the number of iterations (default: 0, which
    means to iterate forever). To iterate 4 times with half a second
    between each frame::

        sage: a.show(delay=50, iterations=4)  # long time  # optional -- ImageMagick

    An animation of drawing a parabola::

        sage: step = 0.1
        sage: L = Graphics()
        sage: v = []
        sage: for i in srange(0, 1, step):
        ....:     L += line([(i,i^2),(i+step,(i+step)^2)], rgbcolor=(1,0,0), thickness=2)
        ....:     v.append(L)
        sage: a = animate(v, xmin=0, ymin=0)
        sage: a.show()              # long time  # optional -- ImageMagick
        sage: show(L)

    TESTS:

    This illustrates that :issue:`2066` is fixed (setting axes
    ranges when an endpoint is 0)::

        sage: animate([plot(sin, -1,1)], xmin=0, ymin=0)._kwds[\'xmin\']
        0

    We check that :issue:`7981` is fixed::

        sage: x = SR.var("x")
        sage: a = animate([plot(sin(x + float(k)), (0, 2*pi), ymin=-5, ymax=5)
        ....:              for k in srange(0,2*pi,0.3)])
        sage: a.show()              # long time  # optional -- ImageMagick

    Do not convert input iterator to a list, but ensure that
    the frame count is known after rendering the frames::

        sage: x = SR.var("x")
        sage: a = animate((plot(x^p, (x,0,2)) for p in sxrange(1,2,.1)))
        sage: str(a)
        \'Animation with unknown number of frames\'
        sage: a.png()    # long time
        \'.../\'
        sage: len(a)     # long time
        10
        sage: a._frames
        <generator object ...

        sage: from sage.plot.animate import Animation
        sage: hash(Animation())  # random
        140658972348064
    '''
    def __init__(self, v=None, **kwds) -> None:
        '''
        Return an animation of a sequence of plots of objects.  See
        documentation of :func:`animate` for more details and
        examples.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)],  # indirect doctest
            ....:                xmin=0, xmax=2*pi, figsize=[2,1])
            sage: print(a)
            Animation with 21 frames
            sage: a.show()          # long time  # optional -- ImageMagick
        '''
    def __getitem__(self, i):
        """
        Get a frame from an animation or
        slice this animation returning a subanimation.

        EXAMPLES::

            sage: a = animate([circle((i,-i), 1-1/(i+1), hue=i/10) for i in srange(0,2,0.2)],
            ....:               xmin=0,ymin=-2,xmax=2,ymax=0,figsize=[2,2])
            sage: print(a)
            Animation with 10 frames
            sage: a.show()          # long time  # optional -- ImageMagick
            sage: frame2 = a[2]     # indirect doctest
            sage: frame2.show()
            sage: print(a[3:7])     # indirect doctest
            Animation with 4 frames
            sage: a[3:7].show()     # long time  # optional -- ImageMagick
        """
    def __add__(self, other):
        """
        Add two animations. This has the effect of superimposing the two
        animations frame-by-frame.

        EXAMPLES::

            sage: a = animate([line([(0,0),(1,i)],hue=0/3) for i in range(2)],
            ....:             xmin=0, ymin=0, xmax=1, ymax=1,
            ....:             figsize=[1,1], axes=False)
            sage: print(a)
            Animation with 2 frames
            sage: a.show()        # optional -- ImageMagick
            sage: b = animate([line([(0,0),(i,1)],hue=2/3) for i in range(2)],
            ....:             xmin=0, ymin=0, xmax=1, ymax=1,
            ....:             figsize=[1,1], axes=False)
            sage: print(b)
            Animation with 2 frames
            sage: b.show()        # optional -- ImageMagick
            sage: s = a+b         # indirect doctest
            sage: print(s)
            Animation with 2 frames
            sage: len(a), len(b)
            (2, 2)
            sage: len(s)
            2
            sage: s.show()        # optional -- ImageMagick
        """
    def __mul__(self, other):
        """
        Multiply two animations. This has the effect of appending the two
        animations (the second comes after the first).

        EXAMPLES::

            sage: a = animate([line([(0,0),(1,i)],hue=0/3) for i in range(2)],
            ....:             xmin=0, ymin=0, xmax=1, ymax=1,
            ....:             figsize=[1,1], axes=False)
            sage: print(a)
            Animation with 2 frames
            sage: a.show()             # optional -- ImageMagick
            sage: b = animate([line([(0,0),(i,1)],hue=2/3) for i in range(2)],
            ....:             xmin=0, ymin=0, xmax=1, ymax=1,
            ....:             figsize=[1,1], axes=False)
            sage: print(b)
            Animation with 2 frames
            sage: b.show()             # optional -- ImageMagick
            sage: p = a*b              # indirect doctest
            sage: len(a), len(b)
            (2, 2)
            sage: len(p)
            4
            sage: print(p)
            Animation with 4 frames
            sage: p.show()             # optional -- ImageMagick
        """
    def __len__(self) -> int:
        """
        Length of ``self``.

        EXAMPLES::

            sage: a = animate([circle((i,0),1,thickness=20*i) for i in srange(0,2,0.4)],
            ....:                xmin=0, ymin=-1, xmax=3, ymax=1, figsize=[2,1], axes=False)
            sage: len(a)
            5
        """
    def make_image(self, frame, filename, **kwds) -> None:
        '''
        Given a frame which has no ``save_image()`` method, make a graphics
        object and save it as an image with the given filename.  By default, this is
        :meth:`sage.plot.plot.plot`.  To make animations of other objects,
        override this method in a subclass.

        EXAMPLES::

            sage: from sage.plot.animate import Animation
            sage: class MyAnimation(Animation):
            ....:    def make_image(self, frame, filename, **kwds):
            ....:        P = parametric_plot(frame[0], frame[1], **frame[2])
            ....:        P.save_image(filename, **kwds)

            sage: t = SR.var("t")
            sage: x = lambda t: cos(t)
            sage: y = lambda n,t: sin(t)/n
            sage: B = MyAnimation([([x(t), y(i+1,t)], (t,0,1),
            ....:                   {\'color\':Color((1,0,i/4)), \'aspect_ratio\':1, \'ymax\':1})
            ....:                  for i in range(4)])

            sage: d = B.png(); v = os.listdir(d); v.sort(); v  # long time
            [\'00000000.png\', \'00000001.png\', \'00000002.png\', \'00000003.png\']
            sage: B.show()  # not tested

            sage: class MyAnimation(Animation):
            ....:    def make_image(self, frame, filename, **kwds):
            ....:        G = frame.plot()
            ....:        G.set_axes_range(floor(G.xmin()), ceil(G.xmax()),
            ....:                         floor(G.ymin()), ceil(G.ymax()))
            ....:        G.save_image(filename, **kwds)

            sage: B = MyAnimation([graphs.CompleteGraph(n)
            ....:                  for n in range(7,11)], figsize=5)
            sage: d = B.png()
            sage: v = os.listdir(d); v.sort(); v
            [\'00000000.png\', \'00000001.png\', \'00000002.png\', \'00000003.png\']
            sage: B.show()  # not tested
        '''
    def png(self, dir=None):
        '''
        Render PNG images of the frames in this animation, saving them
        in ``dir``.  Return the absolute path to that directory.  If
        the frames have been previously rendered and ``dir`` is
        ``None``, just return the directory in which they are stored.

        When ``dir`` is other than ``None``, force re-rendering of
        frames.

        INPUT:

        - ``dir`` -- (default: ``None``) directory in which to store frames; in
          this case, a temporary directory will be created for storing the frames

        OUTPUT: absolute path to the directory containing the PNG images

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([plot(x^2 + n) for n in range(4)], ymin=0, ymax=4)
            sage: d = a.png(); v = os.listdir(d); v.sort(); v  # long time
            [\'00000000.png\', \'00000001.png\', \'00000002.png\', \'00000003.png\']
        '''
    def graphics_array(self, ncols: int = 3):
        '''
        Return a :class:`sage.plot.multigraphics.GraphicsArray` with plots of the
        frames of this animation, using the given number of columns.
        The frames must be acceptable inputs for
        :class:`sage.plot.multigraphics.GraphicsArray`.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: E = EllipticCurve(\'37a\')
            sage: v = [E.change_ring(GF(p)).plot(pointsize=30)
            ....:      for p in [97, 101, 103]]
            sage: a = animate(v, xmin=0, ymin=0, axes=False)
            sage: print(a)
            Animation with 3 frames
            sage: a.show()                      # optional -- ImageMagick

        Modify the default arrangement of array::

            sage: g = a.graphics_array(); print(g)                                      # needs sage.schemes
            Graphics Array of size 1 x 3
            sage: g.show(figsize=[6,3])                                                 # needs sage.schemes

        Specify different arrangement of array and save it with a given file name::

            sage: g = a.graphics_array(ncols=2); print(g)                               # needs sage.schemes
            Graphics Array of size 2 x 2
            sage: f = tmp_filename(ext=\'.png\'); print(f)                                # needs sage.schemes
            ...png
            sage: g.save(f)                                                             # needs sage.schemes

        Frames can be specified as a generator too; it is internally converted to a list::

            sage: t = SR.var("t")
            sage: b = animate((plot(sin(c*pi*t)) for c in sxrange(1,2,.2)))
            sage: g = b.graphics_array()
            sage: print(g)
            Graphics Array of size 2 x 3
        '''
    def gif(self, delay: int = 20, savefile=None, iterations: int = 0, show_path: bool = False, use_ffmpeg: bool = False) -> None:
        '''
        Return an animated gif composed from rendering the graphics
        objects in ``self``.

        This method will only work if either (a) the ImageMagick
        software suite is installed, i.e., you have the ``magick/convert``
        command or (b) ``ffmpeg`` is installed.  See the web sites of
        ImageMagick_ and FFmpeg_ for more details.  By default, this
        produces the gif using Imagemagick if it is present.  If this
        can\'t find ImageMagick or if ``use_ffmpeg`` is True, then it
        uses ``ffmpeg`` instead.

        INPUT:

        - ``delay`` -- (default: 20) delay in hundredths of a
          second between frames

        - ``savefile`` -- file that the animated gif gets saved
          to

        - ``iterations`` -- integer (default: 0); number of
          iterations of animation. If 0, loop forever.

        - ``show_path`` -- boolean (default: ``False``); if True,
          print the path to the saved file

        - ``use_ffmpeg`` -- boolean (default: ``False``); if ``True``, use
          \'ffmpeg\' by default instead of ImageMagick

        If ``savefile`` is not specified: in notebook mode, display the
        animation; otherwise, save it to a default file name.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k))
            ....:              for k in srange(0,2*pi,0.7)],
            ....:             xmin=0, xmax=2*pi, ymin=-1, ymax=1, figsize=[2,1])
            sage: td = tmp_dir()
            sage: a.gif()              # not tested
            sage: a.gif(savefile=td + \'my_animation.gif\',               # long time  # optional -- ImageMagick
            ....:       delay=35, iterations=3)
            sage: with open(td + \'my_animation.gif\', \'rb\') as f:        # long time  # optional -- ImageMagick
            ....:     print(b\'GIF8\' in f.read())
            True
            sage: a.gif(savefile=td + \'my_animation.gif\',               # long time  # optional -- ImageMagick
            ....:       show_path=True)
            Animation saved to .../my_animation.gif.
            sage: a.gif(savefile=td + \'my_animation_2.gif\',             # long time  # optional -- FFmpeg
            ....:       show_path=True, use_ffmpeg=True)
            Animation saved to .../my_animation_2.gif.

        .. NOTE::

           If neither ffmpeg nor ImageMagick is installed, you will
           get an error message like this::

              Error: Neither ImageMagick nor ffmpeg appears to be installed. Saving an
              animation to a GIF file or displaying an animation requires one of these
              packages, so please install one of them and try again.

              See www.imagemagick.org and www.ffmpeg.org for more information.
        '''
    def show(self, delay=None, iterations=None, **kwds) -> None:
        '''
        Show this animation immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        INPUT:

        - ``delay`` -- (default: 20) delay in hundredths of a
          second between frames

        - ``iterations`` -- integer (default: 0); number of
          iterations of animation. If 0, loop forever.

        - ``format`` -- (default: gif) format to use for output.
          Currently supported formats are: gif,
          ogg, webm, mp4, flash, matroska, avi, wmv, quicktime.

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        .. NOTE::

           Currently this is done using an animated gif, though this
           could change in the future. This requires that either
           ffmpeg or the ImageMagick suite (in particular, the
           ``magick/convert`` command) is installed.

        See also the :meth:`ffmpeg` method.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k))
            ....:              for k in srange(0,2*pi,0.7)],
            ....:             xmin=0, xmax=2*pi, figsize=[2,1])
            sage: a.show()                              # long time  # optional -- ImageMagick

        The preceding will loop the animation forever. If you want to show
        only three iterations instead::

            sage: a.show(iterations=3)                  # long time  # optional -- ImageMagick

        To put a half-second delay between frames::

            sage: a.show(delay=50)                      # long time  # optional -- ImageMagick

        You can also make use of the HTML5 video element in the Sage notebook::

            sage: # long time, optional -- FFmpeg
            sage: a.show(format=\'ogg\')
            sage: a.show(format=\'webm\')
            sage: a.show(format=\'mp4\')
            sage: a.show(format=\'webm\', iterations=1)

        Other backends may support other file formats as well::

            sage: # long time, optional -- FFmpeg
            sage: a.show(format=\'flash\')
            sage: a.show(format=\'matroska\')
            sage: a.show(format=\'avi\')
            sage: a.show(format=\'wmv\')
            sage: a.show(format=\'quicktime\')

        TESTS:

        Use of positional parameters is discouraged, will likely get
        deprecated, but should still work for the time being::

            sage: a.show(50, 3)                         # long time  # optional -- ImageMagick

        .. NOTE::

           If you don\'t have ffmpeg or ImageMagick installed, you will
           get an error message like this::

              Error: Neither ImageMagick nor ffmpeg appears to be installed. Saving an
              animation to a GIF file or displaying an animation requires one of these
              packages, so please install one of them and try again.

              See www.imagemagick.org and www.ffmpeg.org for more information.
        '''
    def ffmpeg(self, savefile=None, show_path: bool = False, output_format=None, ffmpeg_options: str = '', delay=None, iterations: int = 0, pix_fmt: str = 'rgb24') -> None:
        '''
        Return a movie showing an animation composed from rendering
        the frames in ``self``.

        This method will only work if ``ffmpeg`` is installed.  See
        https://www.ffmpeg.org for information about ``ffmpeg``.

        INPUT:

        - ``savefile`` -- file that the mpeg gets saved to

        .. warning::

            This will overwrite ``savefile`` if it already exists.

        - ``show_path`` -- boolean (default: ``False``); if ``True``,
          print the path to the saved file

        - ``output_format`` -- string (default: ``None``); format and
          suffix to use for the video.  This may be ``\'mpg\'``, ``\'mpeg\'``,
          ``\'avi\'``, ``\'gif\'``, or any other format that ``ffmpeg`` can handle.
          If this is ``None`` and the user specifies ``savefile`` with a
          suffix, say ``savefile=\'animation.avi\'``, try to determine the
          format (``\'avi\'`` in this case) from that file name.  If no file
          is specified or if the suffix cannot be determined, ``\'mpg\'`` is
          used.

        - ``ffmpeg_options`` -- string (default: ``\'\'``); this string is
          passed directly to ffmpeg

        - ``delay`` -- integer (default: ``None``); delay in hundredths of a
          second between frames.  The framerate is 100/delay.
          This is not supported for mpeg files: for mpegs, the frame
          rate is always 25 fps.

        - ``iterations`` -- integer (default: 0); number of iterations
          of animation. If 0, loop forever.  This is only supported
          for animated gif output and requires ``ffmpeg`` version 0.9 or
          later.  For older versions, set ``iterations=None``.

        - ``pix_fmt`` -- string (default: ``\'rgb24\'``); used only for gif
          output.  Different values such as \'rgb8\' or \'pal8\' may be
          necessary depending on how ffmpeg was installed.  Set
          ``pix_fmt=None`` to disable this option.

        If ``savefile`` is not specified: in notebook mode, display
        the animation; otherwise, save it to a default file name.  Use
        :func:`sage.misc.verbose.set_verbose` with ``level=1`` to see
        additional output.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k))
            ....:              for k in srange(0, 2*pi, 0.7)],
            ....:             xmin=0, xmax=2*pi, ymin=-1, ymax=1, figsize=[2,1])
            sage: td = tmp_dir()
            sage: a.ffmpeg(savefile=td + \'new.mpg\')                  # long time  # optional -- FFmpeg
            sage: a.ffmpeg(savefile=td + \'new.avi\')                  # long time  # optional -- FFmpeg
            sage: a.ffmpeg(savefile=td + \'new.gif\')                  # long time  # optional -- FFmpeg
            sage: a.ffmpeg(savefile=td + \'new.mpg\', show_path=True)  # long time  # optional -- FFmpeg
            Animation saved to .../new.mpg.

        .. NOTE::

           If ffmpeg is not installed, you will get an error message
           like this::

              FeatureNotPresentError: ffmpeg is not available.
              Executable \'ffmpeg\' not found on PATH.
              Further installation instructions might be available at https://www.ffmpeg.org/.

        TESTS::

            sage: a.ffmpeg(output_format=\'gif\',delay=30,iterations=5)  # long time  # optional -- FFmpeg
        '''
    def apng(self, savefile=None, show_path: bool = False, delay: int = 20, iterations: int = 0) -> None:
        '''
        Create an animated PNG composed from rendering the graphics
        objects in ``self``. Return the absolute path to that file.

        Notice that not all web browsers are capable of displaying APNG
        files, though they should still present the first frame of the
        animation as a fallback.

        The generated file is not optimized, so it may be quite large.

        Input:

        - ``delay`` -- (default: 20) delay in hundredths of a
          second between frames

        - ``savefile`` -- file that the animated gif gets saved
          to

        - ``iterations`` -- integer (default: 0); number of
          iterations of animation. If 0, loop forever.

        - ``show_path`` -- boolean (default: ``False``); if True,
          print the path to the saved file

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k))
            ....:              for k in srange(0,2*pi,0.7)],
            ....:             xmin=0, xmax=2*pi, figsize=[2,1])
            sage: dir = tmp_dir()
            sage: a.apng(show_path=True)  # long time
            Animation saved to ....png.
            sage: a.apng(savefile=dir + \'my_animation.png\', delay=35, iterations=3)  # long time
            sage: a.apng(savefile=dir + \'my_animation.png\', show_path=True)  # long time
            Animation saved to .../my_animation.png.

        If the individual frames have different sizes, an error will be raised::

            sage: a = animate([plot(sin(x), (x, 0, k))
            ....:              for k in range(1,4)],
            ....:             ymin=-1, ymax=1, aspect_ratio=1, figsize=[2,1])
            sage: a.apng()  # long time
            Traceback (most recent call last):
            ...
            ValueError: Chunk IHDR mismatch

        TESTS::

            sage: a = animate([])
            sage: a.apng(show_path=True)
            Animation saved to file ....png.
        '''
    def save(self, filename=None, show_path: bool = False, use_ffmpeg: bool = False, **kwds) -> None:
        '''
        Save this animation.

        INPUT:

        - ``filename`` -- (default: ``None``) name of save file

        - ``show_path`` -- boolean (default: ``False``); if True,
          print the path to the saved file

        - ``use_ffmpeg`` -- boolean (default: ``False``); if ``True``, use
          \'ffmpeg\' by default instead of ImageMagick when creating GIF files

        If filename is ``None``, then in notebook mode, display the
        animation; otherwise, save the animation to a GIF file. If
        filename ends in \'.html\', save an :meth:`interactive` version of
        the animation to an HTML file that uses the Three.js viewer.  If
        filename ends in \'.sobj\', save to an sobj file.  Otherwise,
        try to determine the format from the filename extension
        (\'.mpg\', \'.gif\', \'.avi\', etc.).  If the format cannot be
        determined, default to GIF.

        For GIF files, either ffmpeg or the ImageMagick suite must be
        installed.  For other movie formats, ffmpeg must be installed.
        sobj and HTML files can be saved with no extra software installed.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: a = animate([sin(x + float(k))
            ....:              for k in srange(0, 2*pi, 0.7)],
            ....:             xmin=0, xmax=2*pi, ymin=-1, ymax=1, figsize=[2,1])
            sage: td = tmp_dir()
            sage: a.save()         # not tested
            sage: a.save(td + \'wave.gif\')                   # long time  # optional -- ImageMagick
            sage: a.save(td + \'wave.gif\', show_path=True)   # long time  # optional -- ImageMagick
            Animation saved to file .../wave.gif.
            sage: a.save(td + \'wave.avi\', show_path=True)   # long time  # optional -- FFmpeg
            Animation saved to file .../wave.avi.
            sage: a.save(td + \'wave0.sobj\')
            sage: a.save(td + \'wave1.sobj\', show_path=True)
            Animation saved to file .../wave1.sobj.
            sage: a.save(td + \'wave0.html\', online=True)
            sage: a.save(td + \'wave1.html\', show_path=True, online=True)
            Animation saved to file .../wave1.html.

        TESTS:

        Ensure that we can pass delay and iteration count to the saved
        GIF image (see :issue:`18176`)::

            sage: # long time, optional -- ImageMagick
            sage: a.save(td + \'wave.gif\')
            sage: with open(td + \'wave.gif\', \'rb\') as f:
            ....:     print(b\'GIF8\' in f.read())
            True
            sage: with open(td + \'wave.gif\', \'rb\') as f:
            ....:     print(b\'!\\xff\\x0bNETSCAPE2.0\\x03\\x01\\x00\\x00\\x00\' in f.read())
            True
            sage: a.save(td + \'wave.gif\', delay=35)
            sage: with open(td + \'wave.gif\', \'rb\') as f:
            ....:     print(b\'GIF8\' in f.read())
            True
            sage: a.save(td + \'wave.gif\', iterations=3)
            sage: with open(td + \'wave.gif\', \'rb\') as f:
            ....:     print(b\'!\\xff\\x0bNETSCAPE2.0\\x03\\x01\\x00\\x00\\x00\' in f.read())
            False
            sage: with open(td + \'wave.gif\', \'rb\') as f:
            ....:      check1 = b\'!\\xff\\x0bNETSCAPE2.0\\x03\\x01\\x02\\x00\\x00\'
            ....:      check2 = b\'!\\xff\\x0bNETSCAPE2.0\\x03\\x01\\x03\\x00\\x00\'
            ....:      data = f.read()
            ....:      print(check1 in data or check2 in data)
            True
        '''
    def interactive(self, **kwds):
        '''
        Create an interactive depiction of the animation.

        INPUT:

        - ``**kwds`` -- any of the viewing options accepted by show() are valid
          as keyword arguments to this function and they will behave in the same
          way. Those that are animation-related and recognized by the Three.js
          viewer are: ``animate``, ``animation_controls``, ``auto_play``,
          ``delay``, and ``loop``.

        OUTPUT: a 3D graphics object which, by default, will use the Three.js viewer

        EXAMPLES::

            sage: x = SR.var("x")
            sage: frames = [point3d((sin(x), cos(x), x))
            ....:           for x in (0, pi/16, .., 2*pi)]
            sage: animate(frames).interactive(online=True)
            Graphics3d Object

        Works with frames that are 2D or 3D graphics objects or convertible to
        2D or 3D graphics objects via a ``plot`` or ``plot3d`` method::

            sage: frames = [dodecahedron(), circle(center=(0, 0), radius=1), x^2]
            sage: animate(frames).interactive(online=True, delay=100)
            Graphics3d Object

        .. SEEALSO::

            :ref:`threejs_viewer`
        '''

class APngAssembler:
    '''
    Build an APNG_ (Animated PNG) from a sequence of PNG files.
    This is used by the :meth:`sage.plot.animate.Animation.apng` method.

    This code is quite simple; it does little more than copying chunks
    from input PNG files to the output file. There is no optimization
    involved. This does not depend on external programs or libraries.

    INPUT:

    - ``out`` -- a file opened for binary writing to which the data
      will be written

    - ``num_frames`` -- the number of frames in the animation

    - ``num_plays`` -- how often to iterate, 0 means infinitely

    - ``delay`` -- numerator of the delay fraction in seconds

    - ``delay_denominator`` -- denominator of the delay in seconds

    EXAMPLES::

        sage: from sage.plot.animate import APngAssembler
        sage: x = SR.var("x")
        sage: def assembleAPNG():
        ....:     a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.7)],
        ....:                 xmin=0, xmax=2*pi, figsize=[2,1])
        ....:     pngdir = a.png()
        ....:     outfile = sage.misc.temporary_file.tmp_filename(ext=\'.png\')
        ....:     with open(outfile, "wb") as f:
        ....:         apng = APngAssembler(f, len(a))
        ....:         for i in range(len(a)):
        ....:             png = os.path.join(pngdir, "{:08d}.png".format(i))
        ....:             apng.add_frame(png, delay=10*i + 10)
        ....:     return outfile
        sage: assembleAPNG()  # long time
        \'...png\'
    '''
    magic: bytes
    mustmatch: Incomplete
    out: Incomplete
    num_frames: Incomplete
    num_plays: Incomplete
    default_delay_numerator: Incomplete
    default_delay_denominator: Incomplete
    def __init__(self, out, num_frames, num_plays: int = 0, delay: int = 200, delay_denominator: int = 100) -> None:
        """
        Initialize for creation of an APNG file.
        """
    delay_numerator: Incomplete
    delay_denominator: Incomplete
    def add_frame(self, pngfile, delay=None, delay_denominator=None) -> None:
        '''
        Add a single frame to the APNG file.

        INPUT:

        - ``pngfile`` -- file name of the PNG file with data for this frame

        - ``delay`` -- numerator of the delay fraction in seconds

        - ``delay_denominator`` -- denominator of the delay in seconds

        If the delay is not specified, the default from the constructor
        applies.

        TESTS::

            sage: from sage.plot.animate import APngAssembler
            sage: from io import BytesIO
            sage: buf = BytesIO()
            sage: apng = APngAssembler(buf, 2)
            sage: fn = APngAssembler._testData("input1", True)
            sage: apng.add_frame(fn, delay=0x567, delay_denominator=0x1234)
            sage: fn = APngAssembler._testData("input2", True)
            sage: apng.add_frame(fn)
            sage: len(buf.getvalue())
            217
            sage: buf.getvalue() == APngAssembler._testData("anim12", False)
            True
            sage: apng.add_frame(fn)
            Traceback (most recent call last):
            ...
            RuntimeError: Already reached the declared number of frames
        '''
    def set_default(self, pngfile) -> None:
        '''
        Add a default image for the APNG file.

        This image is used as a fallback in case some application does
        not understand the APNG format.  This method must be called
        prior to any calls to the ``add_frame`` method, if it is called
        at all.  If it is not called, then the first frame of the
        animation will be the default.

        INPUT:

        - ``pngfile`` -- file name of the PNG file with data
          for the default image

        TESTS::

            sage: from sage.plot.animate import APngAssembler
            sage: from io import BytesIO
            sage: buf = BytesIO()
            sage: apng = APngAssembler(buf, 1)
            sage: fn = APngAssembler._testData("input1", True)
            sage: apng.set_default(fn)
            sage: fn = APngAssembler._testData("input2", True)
            sage: apng.add_frame(fn, delay=0x567, delay_denominator=0x1234)
            sage: len(buf.getvalue())
            179
            sage: buf.getvalue() == APngAssembler._testData("still1anim2", False)
            True
            sage: apng.add_frame(fn)
            Traceback (most recent call last):
            ...
            RuntimeError: Already reached the declared number of frames
        '''
