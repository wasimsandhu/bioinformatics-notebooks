import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [RNA Splicing](https://rosalind.info/problems/splc/)

        ### Background
        In the nucleus, an enzyme called RNA polymerase (RNAP) initiates transcription by breaking the bonds joining complementary bases of DNA.

        It then creates a molecule called precursor mRNA, or pre-mRNA, by using one of the two strands of DNA as a template strand: moving down the template strand, when RNAP encounters the next nucleotide, it adds the complementary base to the growing RNA strand, with the provision that uracil must be used in place of thymine.

        A pre-mRNA is first chopped into smaller segments called introns and exons; for the purposes of protein translation, the introns are thrown out, and the exons are glued together sequentially to produce a final strand of mRNA.

        This cutting and pasting process is called splicing, and it is facilitated by a collection of RNA and proteins called a **spliceosome**.

        The fact that the spliceosome is made of RNA and proteins despite regulating the splicing of RNA to create proteins is just one manifestation of a molecular chicken-and-egg scenario that has yet to be fully resolved.

        ### Problem
        After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

        **Given:** A DNA string `s` (of length at most 1 kbp) and a collection of substrings of `s` acting as introns. All strings are given in FASTA format.

        **Return:** A protein string resulting from transcribing and translating the exons of `s`. (Note: Only one solution will exist for the dataset provided.)

        ### Example
        Input:
        ```
        >Rosalind_10
        ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
        >Rosalind_12
        ATCGGTCGAA
        >Rosalind_15
        ATCGGTCGAGCGTGT
        ```

        Output:
        ```
        MVYIADKQHVASREAYGHMFKVCA
        ```
        """
    )
    return


@app.cell
def __():
    def remove_introns(dna_strand: str, introns: list) -> str:
        """
        Removes introns and returns exons in given DNA strand.

        Args:
            dna_strand (str): DNA strand of length at most 1 kbp.
            introns (list): List of introns found in DNA strand.

        Returns:
            str: Gene coding region i.e. exons derived from DNA strand.
        """

        for intron in introns:
            dna_strand = dna_strand.replace(intron, "")

        return dna_strand
    return (remove_introns,)


@app.cell
def __(remove_introns):
    from utils import read_fasta, ProteinToolbox

    def translate_exons(fasta_file: str) -> str:
        dna_collection = read_fasta(file_path=fasta_file)
        dna_collection = list(dna_collection.values())
        dna_strand, introns = (dna_collection[0], dna_collection[1:])
        coding_strand = remove_introns(dna_strand, introns)
        mrna_strand = coding_strand.replace("T", "U")
        return ProteinToolbox().translate(mrna_strand)

    _solution = translate_exons("./rosalind/sample_datasets/18_collection_01.txt")
    assert _solution == "MVYIADKQHVASREAYGHMFKVCA"
    print(_solution)
    return ProteinToolbox, read_fasta, translate_exons


@app.cell
def __(translate_exons):
    _solution = translate_exons("./rosalind/sample_datasets/18_collection_02.txt")
    print(_solution)
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
