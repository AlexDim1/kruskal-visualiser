import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

from kruskal.UnionFind import UnionFind


class KruskalVisualiser:

    def visualise_kruskal(self, graph: dict, animation_delay=2):
        # Convert the graph to an edge list
        edges = self.__graph_to_edge_list(graph)
        edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight

        # Map nodes to indices for Union-Find
        nodes = list(graph.keys())
        node_to_index = {node: i for i, node in enumerate(nodes)}

        uf = UnionFind(len(nodes))
        mst = []

        G, pos = self.__initialise_nx_graph(graph)

        # Plot the initial graph
        self.__visualise_graph(G, pos, animation_delay)

        total_weight = 0

        for edge in edges:
            a, b, weight = edge
            if uf.union(node_to_index[a], node_to_index[b]):
                print(f"Added edge ({a}, {b}) with weight {weight} to MST.")
                mst.append(edge)
                total_weight += weight

                # Visualize the current state of the MST
                self.__visualise_mst(G, pos, mst, a, b, weight, animation_delay)
            else:
                print(f"Skipped edge ({a}, {b}) to avoid cycle.")

        plt.show()

        return mst, total_weight

    @staticmethod
    def __visualise_graph(graph: Graph,
                          layout: dict,
                          animation_delay=2):
        plt.clf()
        nx.draw(graph, layout, with_labels=True, node_color="lightblue", edge_color="gray")
        nx.draw_networkx_edge_labels(graph, layout,
                                     edge_labels={(u, v): d["weight"] for u, v, d in graph.edges(data=True)})
        if animation_delay > 0:
            plt.pause(animation_delay)

        plt.show()

    @staticmethod
    def __visualise_mst(graph: Graph,
                        layout: dict,
                        mst,
                        a,
                        b,
                        weight,
                        animation_delay=2):
        mst_edges = [(e[0], e[1]) for e in mst]

        connected_nodes = set()
        for edge in mst_edges:
            connected_nodes.update(edge)

        edge_colors = ["red" if (a, b) in mst_edges or (b, a) in mst_edges else "gray" for a, b in graph.edges()]
        nx.draw(graph, layout, with_labels=True, node_color="lightblue", edge_color=edge_colors,
                width=[2 if color == "red" else 1 for color in edge_colors])
        nx.draw_networkx_edge_labels(graph, layout,
                                     edge_labels={(u, v): d["weight"] for u, v, d in graph.edges(data=True)})
        nx.draw_networkx_nodes(graph, layout, nodelist=list(connected_nodes), node_color='green')
        plt.title(f"Step: Added Edge ({a}, {b}) with Weight {weight}")
        if animation_delay > 0:
            plt.pause(animation_delay)

    @staticmethod
    def __initialise_nx_graph(neighbour_matrix: dict):
        g = nx.Graph()
        for node, neighbors in neighbour_matrix.items():
            for neighbor, weight in neighbors:
                g.add_edge(node, neighbor, weight=weight)
        layout = nx.spring_layout(g, iterations=100, seed=865)
        return g, layout

    @staticmethod
    def __graph_to_edge_list(graph):
        edges = set()
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors:
                edges.add((min(node, neighbor), max(node, neighbor), weight))
        return list(edges)

