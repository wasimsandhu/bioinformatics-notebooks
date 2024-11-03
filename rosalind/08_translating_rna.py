import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Translating RNA into Protein](https://rosalind.info/problems/prot/)

        ### Background
        The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

        The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

        ### Problem
        Given: An RNA string `s` corresponding to a strand of mRNA (of length at most 10 kbp).

        Return: The protein string encoded by `s`.

        ### Example
        Input:
        ```
        AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
        ```

        Output:
        ```
        MAMAPRTEINSTRING
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __():
    codon_dictionary = {
        "UUU": "F",
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "UAU": "Y",
        "UAC": "Y",
        "UAA": "Stop",
        "UAG": "Stop",
        "UGU": "C",
        "UGC": "C",
        "UGA": "Stop",
        "UGG": "W",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGU": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }


    def translation(rna: str):
        """Translates mRNA (genetic string) into polypeptide (protein string)."""

        codons = [rna[index : index + 3] for index in range(0, len(rna), 3)]
        protein = [codon_dictionary[codon] for codon in codons]
        protein.remove("Stop")
        return "".join(protein)
    return codon_dictionary, translation


@app.cell
def __(translation):
    _rna_strand = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    actual = translation(_rna_strand)
    expected = "MAMAPRTEINSTRING"
    assert actual == expected
    return actual, expected


@app.cell
def __(translation):
    with open("./rosalind/sample_datasets/08_mRNA_strand.txt") as file:
        rna_strand = file.readline()
        print(translation(rna_strand))
    return file, rna_strand


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
