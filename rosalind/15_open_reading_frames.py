import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Open Reading Frames](https://rosalind.info/problems/orf/)

        ### Background
        Three immediate wrinkles of complexity arise when we try to pass directly from DNA to proteins.

        First, not all DNA will be transcribed into RNA: so-called junk DNA appears to have no practical purpose for cellular function. 

        Second, we can begin translation at any position along a strand of RNA, meaning that any substring of a DNA string can serve as a template for translation, as long as it begins with a start codon, ends with a stop codon, and has no other stop codons in the middle.

        As a result, the same RNA string can actually be translated in three different ways, depending on how we group triplets of symbols into codons. For example, ...AUGCUGAC... can be translated as ...AUGCUG..., ...UGCUGA..., and ...GCUGAC..., which will typically produce wildly different protein strings.

        ### Open Reading Frames
        Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

        An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

        ### Problem
        **Given:** A DNA string `s` of length at most 1 kbp in FASTA format.

        **Return:** Every distinct candidate protein string that can be translated from ORFs of `s`. Strings can be returned in any order.

        ### Example
        Input:
        ```
        >Rosalind_99
        AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
        ```

        Output:
        ```
        MLLGSFRLIPKETLIQVAGSSPCNLS
        M
        MGMTPRLGLESLLE
        MTPRLGLESLLE
        ```
        """
    )
    return


@app.cell
def __():
    from wasims_toolbox import ProteinToolbox, reverse_complement

    def protein_candidates(dna_strand: str) -> list:
        """
        Returns a list of every possible protein that may be
        translated from the open reading frames in the given strand.

        Args:
            dna_strand (str): DNA string of length at most 1 kbp.

        Returns:
            list: Every distinct candidate protein string that can be
            translated from open reading frames in the given DNA strand.
        """

        # Initialize toolbox
        toolbox = ProteinToolbox()

        # Get complementary strand
        complement = reverse_complement(dna_strand)

        # Transcribe into mRNA strands
        rna = dna_strand.replace("T", "U")
        rna_comp = complement.replace("T", "U")

        # Find start codons
        start_codons = [i for i in range(len(rna)) if rna[i : i + 3] == "AUG"]
        comp_start_codons = [
            i for i in range(len(rna_comp)) if rna_comp[i : i + 3] == "AUG"
        ]

        # Find open reading frames
        frames = [rna[start:] for start in start_codons]
        frames += [rna_comp[start:] for start in comp_start_codons]

        # Get translation of each open reading frame
        candidates = []

        for orf in frames:
            protein = ""
            stop_reached = False

            for i in range(0, len(orf), 3):
                if i + 2 >= len(orf):
                    break

                amino_acid = toolbox.translate_codon(orf[i : i + 3])

                if amino_acid == "Stop":
                    stop_reached = True
                    break

                protein += amino_acid

            if stop_reached:
                candidates.append(protein)

        return list(set(candidates))

    return ProteinToolbox, protein_candidates, reverse_complement


@app.cell
def __(protein_candidates):
    import ipytest

    ipytest.autoconfig()

    def test_case_1():
        dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
        candidates = protein_candidates(dna)
        expected = ["MLLGSFRLIPKETLIQVAGSSPCNLS", "M", "MGMTPRLGLESLLE", "MTPRLGLESLLE"]
        for candidate in candidates:
            assert candidate in expected

    ipytest.run()
    return ipytest, test_case_1


@app.cell
def __(protein_candidates):
    dna = "TACACTCAGGAGTGCACTTGGATCTCACTGGCTCCCCACGCGCTGTAATCCCGCGACATCACCCGTGGCAGGTAGGGTGGCTGGCCCATCAGTACCTACTGTAAATCGACCCGTCTAGCTAAGCCTTGGGTTGTTTCTAGGCCGATAGGATACTCCCTGGCCGTGGCAAACTTATATCCGATGACTAAGCGTGCCCAGGCCATGTCTTTTCACTTCACGTTGCAAATATACATGGCGGATCGCCCGCTGTCTCAATCGAAAGGTTACTAAGGCTGTGAGTATTGGTTTCCTACACGCTTTTTTAAGCACGCTTCACAAAGTGGTACGAGTAGAGAGCGACGCCTTGCAGAGCTGGTGTCTATTGAGTCAAAGCGGTTTCTCAGGTATATTCTGCCGACACACCTTGCCTTTATCTTTCAACACCCGAGAGACGAATGAGTCAATCACATGTTTAGCTAAACATGTGATTGACTCATACACGTCAGAACGACCGATATCTAGCCTCAGCTGTGACCTGACTCCTACATAGTTTGGAACCAGCGGTCATCTCACCCTATTAAATAGGCCTTGGCGTTCCTTTTCTGCCGTTATATGACTGTGGTTATACGACCACACACTAACCTAGATCTCCAGCACTGTGCATGCGCGGTGATGAGTATTCACCCGCATGACGACCGACAACCCCCTGGACTATGCAGGAGGTTTGCAATTGATATCTGGCTAAAGGTGATTAATCGCACCTGACCCAATCCGCGTGCCCCCTTAAAGCCCTCATTCCTGGGTGGCTCAGACTCACTGACGGAGCGTGACTGGATGATGTCGGGCGATACTTCACAGTGCAACATGTTAAATCCTAACCTCCAGGTTGTCGTATTGCTTACCTTCAGAACTGACTTGTGGACAGGGACCT"
    solution = protein_candidates(dna)
    for candidate in solution:
        print(candidate)
    return candidate, dna, solution


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
