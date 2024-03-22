import networkx as nx


def _helper_name_to_node_id(graph):

    name_to_node_id = {data["name"]: node_id for node_id, data in graph.nodes(data=True)}

    return name_to_node_id


def create_subgraph(graph: nx.graph, node: str, edges_away=1):

    single_source_shortest_path = nx.single_source_shortest_path(graph, node, cutoff=edges_away)
    nodes = list(single_source_shortest_path.keys())
    subgraph = nx.subgraph(graph, node)

    return subgraph

def create_subgraph_between_nodes(graph, node_1: str, node_2: str):
    try:
        shortest_path = nx.shortest_path(graph, node_1, node_2, method="djikstra")
    except nx.NetworkxNoPath:
        print(f"No path between {node_1} and {node_2} in the graph.")
        return None, None

    subgraph = nx.subgraph(graph, shortest_path)

    return subgraph

def create_subgraph_from_shortest_paths(graph, nodes):

    paths = list()

    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2:
                try:
                    shortest_path = nx.shortest_path(graph, node, weight="weight")
                    paths.append(shortest_path)
                except nx.NetworkxNoPath:
                    print(f"No path between {node1} and {node2} in the graph.")
                    continue
    nodes_for_subgraph = list(set([node for path in paths for node in path]))

    subgraph = nx.subgraph(graph, nodes_for_subgraph)

    return subgraph



def create_graph(
    schema_structure: dict,
) -> nx.Graph:
    """Create a graph from a schema structure.

    Args:
        schema_structure (dict): The schema structure.

    Returns:
        nx.Graph: The graph.
    """

    relationships = {}
    node_attributes = {}

    node_type_weights = {
        "database": 1000,
        "schema": 100,
        "table": 10,
        "column": 1,
    }

    def _add_relationship(node: dict, neighbour: dict):
        """Add a relationship to the graph.

        Args:
            node (dict): The node.
            neighbour (dict): The neighbour.
        """

        node_id = node['id']
        neighbour_id = neighbour['id']

        if node_id not in relationships:
            relationships[node_id] = {}

        if neighbour_id in relationships[node_id]:
            return

        node_type = node['type']
        weight = node_type_weights.get(node_type)

        relationships[node_id][neighbour_id] = weight

    def _traverse(node: dict):
        """Traverse the graph.

        Args:
            node (dict): The node.
        """

        node_id = node['id']
        node_type = node['type']
        node_name = node['name']
        node_parent = node['parent']
        node_colour = node['colour']

        node_attributes[node_id] = {
                "name": node_name,
                "type": node_type,
                "parent": node_parent,
                "colour": node_colour,
        }

        for neighbour in node["nodes"].values():
            for table in schema_structure[table]["nodes"].values():
                if node["name"] == column["name"]:
                    _add_relationship(node, column)

    for node in schema_structure.keys():
        _traverse(schema_structure[node])

    graph = nx.from_dict_of_dicts(relationships)
    nx.set_node_attributes(graph, node_attributes)

    return graph









frin bokeh.plotting import figure, show, from_networkx
from bokeh.models import Circle, MultiLine

def plot_graph(graph):
    pos = nx.spring_layout(graph)
    networkx_graph = from_networkx(graph, pos=pos, scale=10, center=(0, 0))

    plot = figure(
        title="Graph",
        tooltips=[
            ("Index", "@index"),
            ("Name", "@name"),
            ("Type", "@type"),
            ("Parent", "@parent"),
        ],
        tools="pan, wheel_zoom, reset, save",
        x_range=(-1.1, 1.1),
        y_range=(-1.1, 1.1),
    )

    networkx_graph.node_renderer.glyph = Circle(size=15, fill_color="lightblue")
    networkx_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

    plot.renderers.append(networkx_graph)

    show(plot)
