from _typeshed import Incomplete
from sage.misc.pager import pager as pager

class POVRay:
    """
    POV-Ray The Persistence of Vision Ray Tracer

    INPUT:

    - ``pov_file`` -- complete path to the .pov file you want to be rendered
    - ``outfile`` -- the filename you want to save your result to
    - ``**kwargs`` -- additionally keyword arguments you want to pass to POVRay

    OUTPUT: image is written to the file you specified in outfile

    EXAMPLES:

    AUTHOR:

    Sage interface written by Yi Qiang (yqiang _atNOSPAM_ gmail.com)

    POVRay: http://www.povray.org
    """
    def __call__(self, pov_file, outfile: str = 'sage.ppm', block: bool = True, **kwargs): ...
    def usage(self) -> None: ...

povray: Incomplete
