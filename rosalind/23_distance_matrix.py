import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Creating a Distance Matrix](https://rosalind.info/problems/pdst/)

        ### Background
        For two strings s<sub>1</sub> and s<sub>2</sub> of equal length, the p-distance between them – denoted d<sub>p</sub>(s<sub>1</sub>, s<sub>2</sub>) – is the proportion of corresponding symbols that differ between s<sub>1</sub> and s<sub>2</sub>.

        For a general distance function `d` on `n` taxa (taxa are often represented by genetic strings), we may encode the distances between pairs of taxa via a distance matrix `D` in which D<sub>i,j</sub> = d(s<sub>i</sub>, s<sub>j</sub>).

        ### Problem
        **Given:** A collection of n (n ≤ 10) DNA strings of equal length (at most 1 kbp).

        **Return:** The matrix `D` corresponding to the p-distance d<sub>p</sub> on the given strings.

        ### Examples
        Input:
        ```
        >Rosalind_9499
        TTTCCATTTA
        >Rosalind_0942
        GATTCATTTC
        >Rosalind_6568
        TTTCCATTTT
        >Rosalind_1833
        GTTCCATTTA
        ```

        Output:
        ```
        0.00000 0.40000 0.10000 0.10000
        0.40000 0.00000 0.40000 0.30000
        0.10000 0.40000 0.00000 0.20000
        0.10000 0.30000 0.20000 0.00000
        ```
        """
    )
    return


@app.cell
def __():
    from utils import read_fasta

    def distance_matrix(fasta_file: str):
        """Generates distance matrix for given reads in FASTA format."""

        distance_matrix = []
        reads = read_fasta(file_path=fasta_file).values()
        checked = set()

        def hamming_distance(read1, read2):
            """Calculate Hamming distance between two reads."""
            result = 0

            for index in range(len(read1)):
                if read1[index] != read2[index]:
                    result += 1

            return round(result / len(read1), 3)

        def calculated(read1, read2):
            """Memoization."""
            return (read1, read2) not in checked and (read2, read1) not in checked

        for i, read1 in enumerate(reads):
            distance_matrix.append([])

            for j, read2 in enumerate(reads):
                distance_matrix[i].append(0)

                if calculated(read1, read2):
                    distance_matrix[i][j] = hamming_distance(read1, read2)

        return distance_matrix
    return distance_matrix, read_fasta


@app.cell
def __():
    def print_distance_matrix(matrix: list):
        """Prints distance matrix for Rosalind input."""
        for row in matrix:
            print("\t".join([str(x) for x in row]))
    return (print_distance_matrix,)


@app.cell
def __(distance_matrix, print_distance_matrix):
    matrix = distance_matrix("./rosalind/sample_datasets/23_collection.txt")
    print_distance_matrix(matrix)
    return (matrix,)


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
