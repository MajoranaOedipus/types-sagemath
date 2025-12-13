from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.sage_object import SageObject as SageObject

INNER_HTML_TEMPLATE: str
IFRAME_TEMPLATE: str
OUTER_HTML_TEMPLATE: Incomplete

class JSMolHtml(SageObject):
    def __init__(self, jmol, path_to_jsmol=None, width: str = '100%', height: str = '100%') -> None:
        """
        INPUT:

        - ``jmol`` -- 3-d graphics or
          :class:`sage.repl.rich_output.output_graphics3d.OutputSceneJmol`
          instance. The 3-d scene to show.

        - ``path_to_jsmol`` -- string (default:
          ``'/nbextensions/jupyter-jsmol/jsmol'``). The path (relative or absolute)
          where ``JSmol.min.js`` is served on the web server.

        - ``width`` -- integer or string (default:
          ``'100%'``). The width of the JSmol applet using CSS
          dimensions.

        - ``height`` -- integer or string (default:
          ``'100%'``). The height of the JSmol applet using CSS
          dimensions.

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: JSMolHtml(sphere(), width=500, height=300)                            # needs sage.plot
            JSmol Window 500x300
        """
    @cached_method
    def script(self):
        '''
        Return the JMol script file.

        This method extracts the Jmol script from the Jmol spt file (a
        zip archive) and inlines meshes.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: jsmol = JSMolHtml(OutputSceneJmol.example(), width=500, height=300)
            sage: jsmol.script()
            \'data "model list"\\n10\\nempt...aliasdisplay on;\\n\'
        '''
    def js_script(self):
        '''
        The :meth:`script` as Javascript string.

        Since the many shortcomings of Javascript include multi-line
        strings, this actually returns Javascript code to reassemble
        the script from a list of strings.

        OUTPUT:

        String. Javascript code that evaluates to :meth:`script` as
        Javascript string.

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: jsmol = JSMolHtml(OutputSceneJmol.example(), width=500, height=300)
            sage: print(jsmol.js_script())
            [
              \'data "model list"\',
              ...
              \'isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;\',
            ].join(\'\\n\');
        '''
    def inner_html(self):
        """
        Return a HTML document containing a JSmol applet.

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: jmol = JSMolHtml(OutputSceneJmol.example(), width=500, height=300)
            sage: print(jmol.inner_html())
            <html>
            <head>
              <style>
                * {
                  margin: 0;
                  padding: 0;
                    ...
            </html>
        """
    def iframe(self):
        '''
        Return HTML iframe.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: jmol = JSMolHtml(OutputSceneJmol.example())
            sage: print(jmol.iframe())
            <iframe srcdoc="
            ...
            </iframe>
        '''
    def outer_html(self):
        '''
        Return a HTML document containing an iframe with a JSmol applet.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.display.jsmol_iframe import JSMolHtml
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: jmol = JSMolHtml(OutputSceneJmol.example(), width=500, height=300)
            sage: print(jmol.outer_html())
            <html>
            <head>
              <title>JSmol 3D Scene</title>
            </head>
            </body>
            <BLANKLINE>
            <iframe srcdoc="
                    ...
            </html>
        '''
