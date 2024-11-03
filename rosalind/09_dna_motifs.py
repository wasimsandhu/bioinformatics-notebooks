import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Finding DNA Motifs](https://rosalind.info/problems/subs/)

        ### Background
        Given two strings, `t` is a substring of `s` if it is contained as a contiguous collection of symbols in `s` (as a result, t must be no longer than `s`).

        The position of a symbol in a string is the total number of symbols found to its left, including itself e.g., the positions of all occurrences of `U` in `AUGCUUCAGAAAGGUCUUACG` are 2, 5, 6, 15, 17, and 18. The symbol at position `i` of `s` is denoted by `s[i]` .

        A substring of `s` can be represented as `s[j:k]` , where `j` and `k` represent the starting and ending positions of the substring in `s`. For example, if `s` = `AUGCUUCAGAAAGGUCUUACG`, then `s[2:5]` = `UGCU`.

        The location of a substring `s[j:k]` is its beginning position `j`; note that `t` will have multiple locations in `s` if it occurs more than once as a substring of `s`.

        ### Problem
        Input:
        ```
        GATATATGCATATACTT
        ATAT
        ```

        Output:
        ```
        2 4 10
        ```
        """
    )
    return


@app.cell
def __():
    def find_motif(dna: str, motif: str):
        """Finds and returns indices of motif in given DNA strand."""

        index = 0
        indices = []

        while True:
            try:
                motif_index = dna.index(motif, index) + 1
                indices.append(str(motif_index))
                index = motif_index
            except:
                break

        return " ".join(indices)
    return (find_motif,)


@app.cell
def __(find_motif):
    actual = find_motif("GATATATGCATATACTT", "ATAT")
    expected = "2 4 10"
    assert actual == expected
    return actual, expected


@app.cell
def __(find_motif):
    dna_strand = "TTTCCGGGTTCACAAGGTTCACGGGTTCACGGTTCACATTATTTCGGTTCACGGTTCACGGGTTCACGGAGCAAACTGGTTCACGCGGTTCACAGGTTCACGGTTCACAAGGTTCACCTTTGTGGTTCACCAGCAATTATCGGTTCACCCGGTTCACAGGTTCACGACGGGGGGTTCACGGTTCACGGTTCACCCAGGATGGTTCACGGTTCACTACGGGTTCACAGGTTCACATACTCGCGGTTCACGGTTCACCTCCCACCTTGGTTCACGGTTCACGGTTCACTACCACTGTGTGGTTCACAGGTTCACGGTTCACTGGTTCACAGCAAAGGTTCACGGTTCACGGTTCACACGGTTCACGGTTCACGGTTCACGGTTCACGGTTCACGATCGGTTCACCGGTTCACATGGTTCACACCGGTTCACGGGTTCACGGAGGTTCACGGGTTCACCGGTTCACGTAGTATCAGGTTCACCGGTTCACGGTTCACGGTTCACTGGTTCACGGGGTTCACGGTTCACTGGTTCACGCACTTCAAGGTTCACGGGTTCACTACTAGGTTCACGGGTTCACGCGGTTCACTCGACGGTTCACGCGCTGGCGGTTCACGGTTCACACGGTTCACTCTGGTTCACCAGGTTCACTTGGTTCACGGTTCACAGGTTCACGCCCACGGGGCGGTTCACCGGGTTCACAAAGCGGTTCACGACGTCTAGAGTCGGTTCACGGTTCACATGGGTTCACATTTCGGTTCACGGGTCGGGTTCACGGTTCACGGTTCACGTAGGTTCACGGTTCACCGGTTCACAGGATCGGTTCACGGGTTCACTGGGTTCACGGTTCACGCCGGGTTCACCGGTTCACGGTTCACAGGTTCACGGTTCACAAGGTTCACAGGTTCACGGTTCACTGGTTCACATGGTAGGGTTCACTCCATTACAGGTTCACTGGTTCACGATTTGCCGGTTCAC"
    motif = "GGTTCACGG"
    find_motif(dna_strand, motif)
    return dna_strand, motif


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
