import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Finding a Shared Motif](https://rosalind.info/problems/lcsm/)

        ### Background
        A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring.

        For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

        Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

        ### Problem
        **Given:** A collection of `k` (where `k` ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

        **Return:** A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

        ### Example
        Input:
        ```
        >Rosalind_1
        GATTACA
        >Rosalind_2
        TAGACCA
        >Rosalind_3
        ATACA
        ```

        Output:
        ```
        AC
        ```
        """
    )
    return


@app.cell
def __():
    from wasims_toolbox import get_reads

    def find_motif(fasta_file: str):
        """
        Searches for longest motif in collection of DNA strands.
        Agnostic to multiple motifs; will only return a single result.
        """

        motif = ""
        reads = get_reads(fasta_file)

        for read in reads.values():
            # Initial condition
            if motif == "":
                motif = read
                continue

            # If current motif is not in read, shorten it
            if motif not in read:
                segment = motif
                segments = []

                # Brute force: test all substrings of current motif
                # until a match to the current read is found
                for i in range(len(segment)):
                    for j in range(i + 1, len(segment) + 1):
                        if segment[i:j] in read:
                            segments.append(segment[i:j])

                motif = max(segments, key=len)

        return motif

    motif = find_motif("./sample_datasets/12_collection.txt")
    motif
    return find_motif, get_reads, motif


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
