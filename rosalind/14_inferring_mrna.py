import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Inferring mRNA from Protein](https://rosalind.info/problems/mrna/)

        When researchers discover a new protein, they would like to infer the strand of mRNA from which this protein could have been translated, thus allowing them to locate genes associated with this protein on the genome.

        Unfortunately, although any RNA string can be translated into a unique protein string, reversing the process yields a huge number of possible RNA strings from a single protein string because most amino acids correspond to multiple RNA codons (see the RNA Codon Table).

        Because of memory considerations, most data formats that are built into languages have upper bounds on how large an integer can be: in some versions of Python, an "int" variable may be required to be no larger than 2<sup>31</sup> − 1, or 2,147,483,647. As a result, to deal with very large numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers without actually having to store large numbers.

        ### Background
        For positive integers `a` and `n`, a modulo `n` (written `a mod n` in shorthand) is the remainder when `a` is divided by `n`. For example, `29 mod 11 = 7` because `29 = 11 × 2 + 7`.

        **Modular arithmetic** is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that `a` and `b` are congruent modulo `n` if `a mod n = b mod n`; in this case, we use the notation `a ≡ b mod n`.

        Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn , then a+c≡b+dmodn and a×c≡b×dmodn . To check your understanding of these rules, you may wish to verify these relationships for a=29 , b=73 , c=10 , d=32 , and n=11 .

        As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

        ### Problem
        **Given:** A protein string of length at most 1000 aa.

        **Return:** The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

        ### Example
        Input:
        ```
        MA
        ```

        Output:
        ```
        12
        ```
        """
    )
    return


@app.cell
def __():
    from utils import ProteinToolbox

    def rna_combinations_modulo_million(protein: str):
        toolbox = ProteinToolbox()
        combinations = len(toolbox.get_codons("Stop"))

        for amino_acid in protein:
            amino_acid_codons = len(toolbox.get_codons(amino_acid))
            combinations = (combinations * amino_acid_codons) % 1000000

        return combinations
    return ProteinToolbox, rna_combinations_modulo_million


@app.cell
def __(rna_combinations_modulo_million):
    expected = 12
    actual = rna_combinations_modulo_million("MA")
    assert actual == expected
    return actual, expected


@app.cell
def __(rna_combinations_modulo_million):
    protein = "MTRGCKWAYHDGVSQMYMGCWEIEKNTLIAGLAAWGMRDVITQSTARMIPGSVDSPRYLRYHVRKHIVENDFNQYQSKFQDCNWKQFDTWHDWYLSNHQPNLVLTNAKCHGPFEQWWLKINTRPTDCMIEFGINVIEDDKSARGLSTRFWHWEGILNCTHDIDTYIYDASECNPTPYKCTRVRAKKLKCWQKPMKTNEEKWAYIAINYCQHDGKCQWRLTPLFSKSETALFWDEYCQFSHEMGVKAFRGSPNWAQQLQMHSQRCMNACGIDIERMRTWMQCYRSSWHFDCRFSHQWEWYESHLFWIRELRTVTHGFHFMWAYFRWENMASGGTYAIPHEFHPECYQWWAPTGPMGNMKRWRPRKIYMFRASEKRMDCRQLLWQVKVFMPLDNPLFVCTPRHGFESYRCPSDDANANNMGTDVNSLKYTEYNDIWWVQPFYNVCSLVFWTVLKYGYAMCFNCWHIPPKFPIWCYLKKCMGHYFWHMDFNNVVCSSHGPFIWDKSRTREMNRYCKEWDNPWEAYPTPMFRVSPYQHGITSPRIRCFRAMALLKDYVHIWFCYNCDGRTGWNTPPDIPQDWPPHLVQPIWYLREDEQQKNKKATWYDNVKQHRKQIVMFIWKYYYDEPLNAEPYWNQASEEKAHCDKIAEEDYIMGYVCDCEKTRKSTAAWIISRYVGVTMCPIGSTFGRHNYFDKYILQWLGVVSMWVGFHHHEFFAFPSKKKLANDQRFAVFFWLSKCGHCTCYQYYQENDTWHWMWNLDCLKVTAFPWATTTHISCEKDRCSFIEEETAQMNAMDGWSYQYRSIFLHKGYYPLCSKCADCEPLHRKEYDHHVTKNQDFMQWKRWHNNFQRGTPRRSSWWSRHCAHQLECDSMCKIPTIVIPVAFVHGLGKNQVMSESGIVCEQCPMWHWHSHPESNTIWGMQRHTIHKGPVYSHGWGAHPSMAGYDIIYKSPYMTYWVCWTQIYSFDFTPTFESPSHNALPMVHHEYSHTFMVPTWD"
    combinations = rna_combinations_modulo_million(protein)
    combinations
    return combinations, protein


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
