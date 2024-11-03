import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Locating Restriction Enzymes](https://rosalind.info/problems/revp/)

        ### Background
        To defend itself, the bacterium must either obfuscate its cellular functions so that the phage cannot infiltrate it, or better yet, go on the counterattack by calling in the air force. Specifically, the bacterium employs aerial scouts called restriction enzymes, which operate by cutting through viral DNA to cripple the phage. But what kind of DNA are restriction enzymes looking for?

        The restriction enzyme is a homodimer, which means that it is composed of two identical substructures. Each of these structures separates from the restriction enzyme in order to bind to and cut one strand of the phage DNA molecule; both substructures are pre-programmed with the same target string containing 4 to 12 nucleotides to search for within the phage DNA.

        The chance that both strands of phage DNA will be cut (thus crippling the phage) is greater if the target is located on both strands of phage DNA, as close to each other as possible. By extension, the best chance of disarming the phage occurs when the two target copies appear directly across from each other along the phage DNA, a phenomenon that occurs precisely when the target is equal to its own reverse complement. Eons of evolution have made sure that most restriction enzyme targets now have this form.

        ### Problem
        A DNA string is a **reverse palindrome** if it is equal to its reverse complement. For instance, `GCATGC` is a reverse palindrome because its reverse complement is `GCATGC`.

        **Given:** A DNA string of length at most 1 kbp in FASTA format.

        **Return:** The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

        ### Examples
        Input:
        ```
        >Rosalind_24
        TCAATGCATGCGGGTCTATATGCAT
        ```

        Output:
        ```
        4 6
        5 4
        6 6
        7 4
        17 4
        18 4
        20 6
        21 4
        ```
        """
    )
    return


@app.cell
def __():
    def find_reverse_palindromes(dna_strand: str) -> dict:
        """
        Returns the position and sequence of every reverse palindrome
        in the given DNA strand having a length between 4 and 12.

        Args:
            dna_strand (str): DNA strand of length at most 1kbp.

        Returns:
            dict: Position and sequence of every reverse palindrome.
        """

        comp = {"A": "T", "T": "A", "G": "C", "C": "G"}

        reverse_palindromes = {}

        # Iterate over DNA strand
        for start in range(len(dna_strand)):
            # Get every subsequence of length 4-12
            for length in range(4, 13, 2):
                # Indexing
                end = start + length
                if end > len(dna_strand):
                    break

                # Check outer nucleotides before comparing
                if dna_strand[start] != comp[dna_strand[end - 1]]:
                    continue

                # Start from the middle and see if not reverse palindromic
                candidate = dna_strand[start:end]
                center = len(candidate) // 2
                palindromic = True

                left, right = 1, 0
                while left <= center and right <= center:
                    if candidate[center - left] != comp[candidate[center + right]]:
                        palindromic = False
                        break
                    left += 1
                    right += 1

                # If sequence equals its reverse palindrome, save sequence
                if palindromic:
                    reverse_palindromes[start + 1] = candidate

        return reverse_palindromes

    return (find_reverse_palindromes,)


@app.cell
def __(dna_strand, find_reverse_palindromes):
    import ipytest

    ipytest.autoconfig()
    _dna_strand = "TCAATGCATGCGGGTCTATATGCAT"
    _reverse_palindromes = find_reverse_palindromes(dna_strand)
    _reverse_palindromes
    return (ipytest,)


@app.cell
def __():
    # magic command not supported in marimo; please file an issue to add support
    # %%ipytest
    #
    # def test_case_1():
    #
    #     solution = {
    #         4: 6,
    #         5: 4,
    #         6: 6,
    #         7: 4,
    #         17: 4,
    #         18: 4,
    #         20: 6,
    #         21: 4,
    #     }
    #
    #     dna_strand = "TCAATGCATGCGGGTCTATATGCAT"
    #     reverse_palindromes = find_reverse_palindromes(dna_strand)
    #
    #     for position, sequence in reverse_palindromes.items():
    #         assert solution[position] == len(sequence)
    return


@app.cell
def __(dna_strand, find_reverse_palindromes):
    _dna_strand = "ATATCTGGCTACGTCTTTTTACCTGTTTGACAACCGGCCTCCTTACGAAGTACCCATTGAAGCGTTGAGTGCACGTTGCTCGTCGCGCTCTGCGGAGAAACGCGTGGGGCCATGACATACAAGCGAATCCTGTCTCCGCCGCGCTCGGGCCGTGAAGTCGTTTGATACGCCTCTAGGATCAATGATCCGAGGCGCCGTGACTTGGCAACTGAGTAATCCCTACACGTCGCTGCCAAACCTTCCGCTAGGCTGCATGTACTGCAGGCCCATCCATATTATGCCGACTGCCCGGTAAAAGCCACTAGATCAACGGATTTTCTGACTGCCGCTGTCGAGGGCTAAGAACTTGATCAGGGACCGGACACGAATTACTAACACCGCGGTCCTGTAAGACAACATTGGCGCCCAACTCCACGAGGCCGCGTCACGGAGAAGCTTCTCGGTTTGTTGCAGGGAACTCCGTACGTGAATTATTGCCCGTTCGGGTTAGTGCGGGAAGACGACTTCCATCATTATTGAGGAGACTCCACGTGCATCGAAGAAGCGCGGCGAATGCTCGCGACCCTACCCCCTGCTCAATGTAGTTTCGGAGCCGTCCTTGCCGGACGTAATTGGTCATCAGCCTGTGCCACTCGCGTATTCGCTCATGAATCCCGACTATTGTAGCCGAATTAGTAACGGCTGTCTTGTTAGAGGAAACAACGGTGCCTCAGTCTATTGCGTTCGCGTTGCACTGAAAGGCCCTCATAAAGGCTTACCAGCCTGATCCGGTCGCAGGCGAAGAAAGCACGGCCGCGTGTCGCTACAAAATTCCCGCGGGCACGTGGCCGACTTCACACTCGTTAAATGTAATCAGGCGCTGGCTGTATA"
    _reverse_palindromes = find_reverse_palindromes(dna_strand)
    for position, sequence in _reverse_palindromes.items():
        print(position, len(sequence))
    return position, sequence


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
