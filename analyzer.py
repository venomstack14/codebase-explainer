import networkx as nx

def build_dependency_graph(parsed_data):
    G = nx.DiGraph()

    for file, details in parsed_data.items():
        G.add_node(file)

        for imp in details["imports"]:
            if imp:
                G.add_edge(file, imp)

    return G