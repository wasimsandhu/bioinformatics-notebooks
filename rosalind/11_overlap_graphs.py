import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Overlap Graphs](https://rosalind.info/problems/grph/)

        ### Background
        A graph whose nodes have all been labeled can be represented by an **adjacency list**, in which each row of the list contains the two node labels corresponding to a unique edge.

        A **directed graph** (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail `v` and head `w` is represented by `(v,w)` (but not by `(w,v)`). A directed loop is a directed edge of the form `(v,v)`.

        For a collection of strings and a positive integer `k`, the **overlap graph** for the strings is a directed graph `O_k` in which each string is represented by a node, and string `s` is connected to string `t` with a directed edge when there is a length `k` suffix of s that matches a length `k` prefix of `t`, as long as `s != t`; we demand `s != t` to prevent directed loops in the overlap graph (although directed cycles may be present).

        ### Problem
        **Given:** A collection of DNA strings in FASTA format having total length at most 10 kbp.

        **Return:** The adjacency list corresponding to `O_3`. You may return edges in any order.

        ### Example
        Input:
        ```
        >Rosalind_0498
        AAATAAA
        >Rosalind_2391
        AAATTTT
        >Rosalind_2323
        TTTTCCC
        >Rosalind_0442
        AAATCCC
        >Rosalind_5013
        GGGTGGG
        ```

        Output:
        ```
        Rosalind_0498 Rosalind_2391
        Rosalind_0498 Rosalind_0442
        Rosalind_2391 Rosalind_2323
        ```
        """
    )
    return


@app.cell
def __():
    from utils import get_reads

    def get_adjacency_list(fasta_file: str) -> list:
        """
        Creates overlap graph using collection of DNA strands
        and returns adjacency list corresponding to O_3, where
        each strand is connected to another via directed edge
        where prefix of strand 1 == suffix of strand 2.

        Args:
            fasta_file (str): Path to FASTA file

        Returns:
            list: Each nested list corresponds to a directed edge.
        """

        adjacency_list = []
        reads = get_reads(fasta_file)

        for title1, read1 in reads.items():
            for title2, read2 in reads.items():
                if read1[-3:] == read2[:3] and read1 != read2:
                    adjacency_list.append([title1, title2])

        return adjacency_list
    return get_adjacency_list, get_reads


@app.cell
def __(get_adjacency_list):
    expected = [
        [">Rosalind_0498", ">Rosalind_2391"],
        [">Rosalind_0498", ">Rosalind_0442"],
        [">Rosalind_2391", ">Rosalind_2323"],
    ]
    actual = get_adjacency_list("./rosalind/sample_datasets/11_collection_01.txt")
    for edge in expected:
        assert edge in actual
    return actual, edge, expected


@app.cell
def __(get_adjacency_list):
    def print_adjacency_list(adjacency_list: list):
        """For answering Rosalind problem."""
        for edge in adjacency_list:
            print(edge[0], edge[1])

    _adjacency_list = get_adjacency_list("./rosalind/sample_datasets/11_collection_01.txt")
    print_adjacency_list(_adjacency_list)
    return (print_adjacency_list,)


@app.cell
def __(get_adjacency_list, print_adjacency_list):
    _adjacency_list = get_adjacency_list("./rosalind/sample_datasets/11_collection_02.txt")
    print_adjacency_list(_adjacency_list)
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
