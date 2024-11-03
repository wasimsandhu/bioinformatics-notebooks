import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Genome Assembly as Shortest Superstring](https://rosalind.info/problems/long/)

        ### Background
        Recall from “Computing GC Content” that almost all humans share approximately 99.9% of the same nucleotides on the genome. Thus, if we know only a few complete genomes from the species, then we already possess an important key to unlocking the species genome.

        Determining an organism's complete genome (called genome sequencing) forms a central task of bioinformatics. Unfortunately, we still don't possess the microscope technology to zoom into the nucleotide level and determine the sequence of a genome's nucleotides, one at a time. However, researchers can apply chemical methods to generate and identify much smaller snippets of DNA, called reads.

        After obtaining a large collection of reads from multiple copies of the same genome, the aim is to reconstruct the desired genome from these small pieces of DNA; this process is called fragment assembly. **Fragment assembly** works by blasting many copies of the same genome into smaller, identifiable reads, which are then used to computationally assemble one copy of the genome.

        ### Problem
        For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a **superstring**.

        By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

        **Given:** At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

        > The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

        **Return:** A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

        ### Example
        Input:
        ```
        >Rosalind_56
        ATTAGACCTG
        >Rosalind_57
        CCTGCCGGAA
        >Rosalind_58
        AGACCTGCCG
        >Rosalind_59
        GCCGGAATAC
        ```

        Output:
        ```
        ATTAGACCTGCCGGAATAC
        ```
        """
    )
    return


@app.cell
def __():
    from wasims_toolbox import read_fasta
    from itertools import combinations

    def shortest_superstring(fasta_file: str) -> str:
        """
        Constructs shortest superstring from a collection of reads,
        which serves as a candidate chromosome.

        For the given dataset, there must exist a unique way to reconstruct
        the entire chromosome from these reads by gluing together pairs of
        reads that overlap by more than half their length.

        Args:
            fasta_file (str): Path to FASTA file containing reads
            from the same strand of a single linear chromosome.

        Returns:
            str: Shortest superstring containing all of the given
            reads, corresponding to a reconstructed chromosome.
        """

        checked = set()
        glued = 0

        # Get reads from FASTA file
        reads = read_fasta(file_path=fasta_file)
        reads = list(reads.values())

        # Combine reads that overlap by over half their length
        while len(reads) != 1:
            read_combinations = combinations(reads, 2)
            glued_count = glued

            for read_pair in read_combinations:
                if read_pair in checked:
                    continue

                index = 0
                glue = True

                while read_pair[0][index:] != read_pair[1][:-index]:
                    index += 1
                    if index == len(read_pair[0]):
                        glue = False
                        break

                if glue:
                    glued_read = read_pair[0] + read_pair[1][-index:]
                    reads.append(glued_read)
                    glued += 1

                    reads.remove(read_pair[0])
                    reads.remove(read_pair[1])
                    break

                checked.add(read_pair)

            if glued_count == glued:
                break

        # Superstring is always at end of list
        superstring = reads.pop(-1)

        # If any unglued reads remaining, append to superstring
        for read in reads:
            if read not in superstring:
                superstring += read

        return superstring

    result = shortest_superstring("./sample_datasets/20_collection_01.txt")
    result
    return combinations, read_fasta, result, shortest_superstring


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
    #     result = shortest_superstring("./sample_datasets/20_collection_01.txt")
    #     answer = "ATTAGACCTGCCGGAATAC"
    #     assert result == answer
    return


@app.cell
def __():
    # result = shortest_superstring("./sample_datasets/20_collection_02.txt")
    # print(result)
    # print(len(result))
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
