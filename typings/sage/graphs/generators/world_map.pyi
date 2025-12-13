from sage.graphs.graph import Graph as Graph

def AfricaMap(continental: bool = False, year: int = 2018):
    '''
    Return African states as a graph of common border.

    "African state" here is defined as an independent state having the capital
    city in Africa. The graph has an edge between those countries that have
    common *land* border.

    INPUT:

    - ``continental`` -- boolean (default: ``False``); whether to only return
      states in the continental Africa or all African states

    - ``year`` -- integer (default: 2018); reserved for future use

    EXAMPLES::

        sage: Africa = graphs.AfricaMap(); Africa
        Africa Map: Graph on 54 vertices
        sage: sorted(Africa.neighbors(\'Libya\'))
        [\'Algeria\', \'Chad\', \'Egypt\', \'Niger\', \'Sudan\', \'Tunisia\']

        sage: cont_Africa = graphs.AfricaMap(continental=True)
        sage: cont_Africa.order()
        48
        sage: \'Madagaskar\' in cont_Africa
        False

    TESTS::

        sage: Africa.plot()                     # long time                             # needs sage.plot
        Graphics object consisting of 159 graphics primitives
    '''
def EuropeMap(continental: bool = False, year: int = 2018):
    '''
    Return European states as a graph of common border.

    "European state" here is defined as an independent state having the capital
    city in Europe. The graph has an edge between those countries that have
    common *land* border.

    INPUT:

    - ``continental`` -- boolean (default: ``False``); whether to only return
      states in the continental Europe or all European states

    - ``year`` -- integer (default: 2018); reserved for future use

    EXAMPLES::

        sage: Europe = graphs.EuropeMap(); Europe
        Europe Map: Graph on 44 vertices
        sage: Europe.neighbors(\'Ireland\')
        [\'United Kingdom\']

        sage: cont_Europe = graphs.EuropeMap(continental=True)
        sage: cont_Europe.order()
        40
        sage: \'Iceland\' in cont_Europe
        False
    '''
def USAMap(continental: bool = False):
    """
    Return states of USA as a graph of common border.

    The graph has an edge between those states that have common *land* border
    line or point. Hence for example Colorado and Arizona are marked as
    neighbors, but Michigan and Minnesota are not.

    INPUT:

    - ``continental`` -- boolean (default: ``False``); whether to exclude Alaska
      and Hawaii

    EXAMPLES:

    How many states are neighbor's neighbor for Pennsylvania::

        sage: USA = graphs.USAMap()
        sage: distance = USA.shortest_path_lengths('Pennsylvania')
        sage: len([n2 for n2, d in distance.items() if d == 2])
        7

    Diameter for continental USA::

        sage: USAcont = graphs.USAMap(continental=True)
        sage: USAcont.diameter()
        11
    """
def WorldMap():
    '''
    Return the Graph of all the countries, in which two countries are adjacent
    in the graph if they have a common boundary.

    This graph has been built from the data available
    in The CIA World Factbook [CIA]_ (2009-08-21).

    The returned graph ``G`` has a member ``G.gps_coordinates`` equal to a
    dictionary containing the GPS coordinates of each country\'s capital city.

    EXAMPLES::

        sage: g = graphs.WorldMap()
        sage: g.has_edge("France", "Italy")
        True
        sage: g.gps_coordinates["Bolivia"]
        [[17, \'S\'], [65, \'W\']]
        sage: g.connected_component_containing_vertex(\'Ireland\', sort=True)
        [\'Ireland\', \'United Kingdom\']

    TESTS:

    :issue:`24488`::

        sage: \'Iceland\' in graphs.WorldMap()
        True
    '''
