from KruskalVisualiser import KruskalVisualiser


def main():
    graph = {
        'A': [('B', 2), ('C', 4), ('D', 7)],
        'B': [('A', 2), ('E', 3)],
        'C': [('A', 4), ('D', 2), ('F', 5)],
        'D': [('A', 7), ('C', 2), ('E', 6), ('G', 8)],
        'E': [('B', 3), ('D', 6), ('G', 4)],
        'F': [('C', 5), ('G', 3), ('H', 6)],
        'G': [('E', 4), ('F', 3), ('H', 2), ('D', 8)],
        'H': [('F', 6), ('G', 2)]
    }

    animation_delay = 1  # секунди

    visualiser = KruskalVisualiser()
    mst, total_weight = visualiser.visualise_kruskal(graph, animation_delay=animation_delay)

    print("Minimum Spanning Tree:", mst)
    print("Total weight of MST:", total_weight)


if __name__ == "__main__":
    main()
