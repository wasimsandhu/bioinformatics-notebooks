import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Perfect Matchings and RNA Secondary Structures](https://rosalind.info/problems/pmch/)

        ### Intro to RNA Folding
        Because RNA is single-stranded, you may have wondered if the cytosine and guanine bases bond to each other like in DNA. The answer is yes, as do adenine and uracil, and the resulting base pairs define the secondary structure of the RNA molecule.

        In the greater three-dimensional world, the base pairing interactions of an RNA molecule cause it to twist around on itself in a process called RNA folding. When two complementary intervals of bases located close to each other on the strand bond to each other, they form a structure called a hairpin loop (or stem loop).

        ![](https://rosalind.info/media/problems/pmch/hairpin_loop.thumb.png)

        The same RNA molecule may base pair differently at different points in time, thus adopting many different secondary structures. Our eventual goal is to classify which of these structures are practically feasible, and which are not. To this end, we will ask natural combinatorial questions about the number of possible different RNA secondary structures. 

        In this problem, we will first consider the (impractical) simplified case in which every nucleotide forms part of a base pair in the RNA molecule.

        ### Background
        A **matching** in a graph `G` is a collection of edges of G, no two of which include the same node.

        ![](https://rosalind.info/media/problems/pmch/matching.thumb.png)

        <sub><sup>Three matchings (highlighted in red) shown in three different graphs. Basically, they are edges that don't share nodes.</sup></sub>

        If G contains an even number of nodes – say `2n` – then a matching on `G` is perfect if it contains `n` edges, which is clearly the maximum possible.

        ![](https://rosalind.info/media/problems/pmch/perfect_matching.thumb.png)

        <sub><sup>A graph containing 10 nodes; the five edges forming a perfect matching on these nodes are highlighted in red.</sup><sub>

        First, let `K_n` denote the complete graph on `2n` labeled nodes, in which every node is connected to every other node with an edge, and let pn denote the total number of perfect matchings in `K_n` . For a given node `x`, there are `2n − 1` ways to join `x` to the other nodes in the graph, after which point we must form a perfect matching on the remaining `2n − 2` nodes.

        This reasoning provides us with the recurrence relation `p_n = (2n − 1) * p_n − 1`.

        Using the fact that `p_1` is `1`, this recurrence relation implies the closed equation `p_n = (2n − 1)(2n − 3)(2n − 5) ⋯ (3)(1)`.

        ### Problem
        Given an RNA string `s = s_1, ..., s_n` , a bonding graph for `s` is formed as follows.

        1. First, assign each symbol of `s` to a node, and arrange these nodes in order around a circle, connecting them with edges called adjacency edges.

        1. Second, form all possible edges {A, U} and {C, G}, called basepair edges; we will represent basepair edges with dashed edges.

        ![](https://rosalind.info/media/problems/pmch/bonding_graph.thumb.png)

        <sub><sup>The bonding graph for the RNA string s = UAGCGUGAUCAC.</sup><sub>

        Note that a matching contained in the basepair edges will represent one possibility for base pairing interactions in `s`. For such a matching to exist, `s` must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

        ![](https://rosalind.info/media/problems/pmch/bonding_crossing.thumb.png)

        <sub><sup>A perfect matching on the basepair edges is highlighted in red and represents a candidate secondary structure for the RNA strand.</sup><sub>

        **Given:** An RNA string `s` of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

        **Return:** The total possible number of perfect matchings of basepair edges in the bonding graph of `s`.

        ### Examples
        Input:
        ```
        >Rosalind_23
        AGCUAGUCAU
        ```

        Output:
        ```
        12
        ```
        """
    )
    return


@app.cell
def __():
    def total_perfect_matchings(s: str) -> int:
        """Returns total possible number of perfect matchings
        of basepair edges in the bonding graph of s."""

        graph = {}

        base_pair = {"A": "U", "U": "A", "C": "G", "G": "C"}

        def is_base_pair(nt_1: str, nt_2: str) -> bool:
            nt_1, nt_2 = nt_1[0], nt_2[0]
            return base_pair[nt_1] == nt_2 or base_pair[nt_2] == nt_1

        # First, assign each symbol of s to a node
        for index, char in enumerate(s):
            key = f"{char}{index}"
            graph[key] = []

        # Second, form all possible edges {A, U} and {C, G}, called basepair edges
        for source in graph:
            for target in graph:
                if is_base_pair(source, target):
                    graph[source].append(target)

        # Finally, count all matchings
        matchings = 0

        for node1 in graph:
            for node2 in graph[node1]:
                if node1 not in graph[node2]:
                    continue

                is_matching = True

                for x in graph[node1]:
                    if x in graph[node2]:
                        is_matching = False
                        break

                if is_matching:
                    print("Node 1:", node1, graph[node1])
                    print("Node 2:", node2, graph[node2], "\n")
                    matchings += 1
                    break

        return matchings

    total_perfect_matchings("UAGCGUGAUCAC")
    return (total_perfect_matchings,)


@app.cell
def __():
    import ipytest

    ipytest.autoconfig()
    return (ipytest,)


@app.cell
def __():
    # magic command not supported in marimo; please file an issue to add support
    # %%ipytest
    #
    # def test_case_1():
    #     assert total_perfect_matchings("UAGCGUGAUCAC") == 6
    #
    # def test_case_2():
    #     assert total_perfect_matchings("AGCUAGUCAU") == 12
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
