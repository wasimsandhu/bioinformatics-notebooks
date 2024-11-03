import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Completing a Tree]()

        ### Background
        An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart.

        In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

        ### Problem
        **Given:** A positive integer `n`, where `n ≤ 1000`, and an adjacency list corresponding to a graph on `n` nodes that contains no cycles.

        **Return:** The minimum number of edges that can be added to the graph to produce a tree.

        ### Example
        Input:
        ```
        10
        1 2
        2 8
        4 10
        5 9
        6 10
        7 9
        ```

        Output:
        ```
        3
        ```
        """
    )
    return


@app.cell
def __():
    def min_edges_needed(file_path: str) -> int:
        """
        Returns the minimum number of edges needed to
        construct a tree from the given adjacency list.

        The minimum number of edges is going to be n - 1,
        where n is the number of nodes in the graph.

        The given adjacency list provides us a list of nodes
        that are connected in the graph, but does not give
        us the unconnected "lonely" nodes.

        By subtracting the minimum edges (n - 1) from the
        given number of edges, we determine the remaining
        number of edges needed. :)
        """

        with open(file_path, "r") as file:
            lines = file.read().splitlines()

        total_nodes = int(lines[0])
        given_edges = len(lines[1:])
        min_edges = total_nodes - 1

        return min_edges - given_edges

    return (min_edges_needed,)


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
