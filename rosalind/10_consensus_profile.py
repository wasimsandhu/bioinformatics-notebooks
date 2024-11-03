import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Consensus and Profile](https://rosalind.info/problems/cons/)

        ### Background
        Say that we have a collection of DNA strings, all having the same length `n`. Their profile matrix is a `4 × n` matrix `P` in which `P(1,j)` represents the number of times that 'A' occurs in the `j`th position of one of the strings, `P(2,j)` represents the number of times that 'C' occurs in the `j`th position, and so on (see below).

        **DNA strands**
        ```
        A T C C A G C T
        G G G C A A C T
        A T G G A T C T
        A A G C A A C C
        T T G G A A C T
        A T G C C A T T
        A T G G C A C T
        ```

        **Profile**
        ```
        A   5 1 0 0 5 5 0 0
        C   0 0 1 4 2 0 6 1
        G   1 1 6 3 0 1 0 0
        T   1 5 0 0 0 1 1 6
        ```

        A consensus string `c` is a string of length `n` formed from our collection by taking the most common symbol at each position; the `j`th symbol of `c` therefore corresponds to the symbol having the maximum value in the `j`th column of the profile matrix. 

        **Consensus**
        ```
        A T G C A A C T
        ```

        Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

        ### Problem
        **Given:** A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

        **Return:** A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
        """
    )
    return


@app.cell
def __():
    from utils import get_reads
    _reads = get_reads("./rosalind/sample_datasets/10_collection_01.txt")
    collection = [read for read in _reads.values()]
    collection
    return collection, get_reads


@app.cell
def __(collection):
    def generate_profile_matrix(reads: list) -> dict:
        """
        Generates profile matrix with shape 4 x n for
        collection of DNA strands with length n.

        Args:
            reads (dict): Dictionary with key-value pairs of
            read titles and DNA strands from a FASTA file.

        Returns:
            dict: 4 x n profile matrix for given DNA strands.
        """
        profile_matrix = {
            "A": [0 for nt in reads[0]],
            "C": [0 for nt in reads[0]],
            "G": [0 for nt in reads[0]],
            "T": [0 for nt in reads[0]],
        }
        for index in range(len(reads[0])):
            for read in reads:
                profile_matrix[read[index]][index] = (
                    profile_matrix[read[index]][index] + 1
                )
        return profile_matrix

    profile_matrix = generate_profile_matrix(collection)
    profile_matrix
    return generate_profile_matrix, profile_matrix


@app.cell
def __(profile_matrix):
    def get_consensus(profile_matrix: dict) -> str:
        """Returns first consensus strand found from the given profile matrix.

        Args:
            profile_matrix (dict): Profile matrix of dimension 4 x n,
            with nucleotide occurrences in each strand of length n.

        Returns:
            str: Consensus strand
        """
        consensus_strand = ""
        length = len(profile_matrix["A"])
        for index in range(length):
            nt = "-"
            max = 0
            for key in profile_matrix.keys():
                occurrences = profile_matrix[key][index]
                if occurrences > max:
                    max = occurrences
                    nt = key
            consensus_strand = consensus_strand + nt
        return consensus_strand

    _consensus = get_consensus(profile_matrix)
    _consensus
    return (get_consensus,)


@app.cell
def __(generate_profile_matrix, get_consensus, get_reads):
    _reads = get_reads("./rosalind/sample_datasets/10_collection_01.txt")
    collection_1 = [read for read in _reads.values()]
    profile_matrix_1 = generate_profile_matrix(collection_1)
    _consensus = get_consensus(profile_matrix_1)

    expected = {
        ">Rosalind_1": "ATCCAGCT",
        ">Rosalind_2": "GGGCAACT",
        ">Rosalind_3": "ATGGATCT",
        ">Rosalind_4": "AAGCAACC",
        ">Rosalind_5": "TTGGAACT",
        ">Rosalind_6": "ATGCCATT",
        ">Rosalind_7": "ATGGCACT",
    }
    assert _reads == expected

    expected = {
        "A": [5, 1, 0, 0, 5, 5, 0, 0],
        "C": [0, 0, 1, 4, 2, 0, 6, 1],
        "G": [1, 1, 6, 3, 0, 1, 0, 0],
        "T": [1, 5, 0, 0, 0, 1, 1, 6],
    }
    assert profile_matrix_1 == expected

    assert _consensus == "ATGCAACT"
    return collection_1, expected, profile_matrix_1


@app.cell
def __(generate_profile_matrix, get_consensus, get_reads):
    _reads = get_reads("./rosalind/sample_datasets/10_collection_02.txt")
    collection_2 = [read for read in _reads.values()]
    profile_matrix_2 = generate_profile_matrix(collection_2)
    _consensus = get_consensus(profile_matrix_2)
    _consensus
    return collection_2, profile_matrix_2


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
