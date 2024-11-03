import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### [Counting Nucleotides](https://rosalind.info/problems/dna/)

        **Given:** A DNA string `s` of length at most 1000 nt.

        **Return:** Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in `s`.
        """
    )
    return


@app.cell
def __():
    def count_nucleotides(dna: str):
        """Counts nucleotide occurences for a given DNA string"""
        return f'{dna.count("A")} {dna.count("C")} {dna.count("G")} { dna.count("T")}'
    return (count_nucleotides,)


@app.cell
def __(count_nucleotides):
    _dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    output = count_nucleotides(_dna_string)
    assert output == "20 12 17 21"
    return (output,)


@app.cell
def __(count_nucleotides):
    _dna_string = "GGTCAATCTACGGTGAAATAGGTCGAAGTAACAACGGAATTGATCAATACCCATCTATCCTGAAGTGGCGCGGTAGATGACGAAAATTCGGTCGGACCCGCAACCCTTTGAGGACCCCAACACTGTCGTAGGAAGGCTGCTGCAACGATGTTGCACTTGACCACCGGCGCCTTAAGCCACCATATTTATACTATTGCATGCTACGAGGTGGTGAGAGACCGCTTGTAGTCCCCATATAGGCAGCTTAAACTGACAGTACTCAAATACTACCAAGTATCCCGTAGATTCCCAGGGGACAATGCGTTAGAAAGAAATAAAGGTCATACTATAAGGTCCACGTTCGTATTACTGGTGTCACCCACACTTGACCTGGTGGTAATGTGTCTTGCGCTGGTACGGAGATAACCCGCAGCGCTTCGACAAAAGACACAGTGCCAACCGAAGGTCATAGATTAGCTGCATCCTTATGGATACGCTCTGGGACGGTTAATAGAATGATAAAGGACGAACCCTTACACCAGCTGGGATGGTCCCGAAGTAAACATTCATCTGAGGTTATCGTTCAATTCTCCGCACTACAGGCGAACAATGTGCGAAAGGTATAAAGACATACACTCATTCTAGCACCCTGGACGTAACACACGTGGATTCGTCTAGATATTCCTCATGCTCGTACCCCACAATTTAAGGAGTTGCCCAGAGGATTAGCATCTCAGATTTCAACAAGGATGTTCCCCTTTAGTATTTATATATCGAGTTAGCGCTGAGTTTTTGATTCGAATCGTATGGTCACTGGCTCAACCGTGTGTTCTGTAGCAGGCCTTGACTATGCAAAAGGGGTAGCTGCGTGCTGACGCTCAATATATAACAATCGTAATTCCGTGGCGCGATTGAATGGACCTTGATCTA"
    count_nucleotides(_dna_string)
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
