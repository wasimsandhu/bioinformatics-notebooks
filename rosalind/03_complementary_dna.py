import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Complementing a Strand of DNA](https://rosalind.info/problems/revc/)

        ### Background
        Watson and Crick's proposal:
        1. The DNA molecule is made up of two strands, running in opposite directions.
        1. Each base bonds to a base in the opposite strand.
        1. The two strands are twisted together into a long spiral staircase structure called a double helix.

        In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

        The reverse complement of a DNA string `s` is the string `c`, formed by reversing the symbols of `s`, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

        ### Problem
        Given: A DNA string `s` of length at most 1000 bp.

        Return: The reverse complement `c` of `s`.

        ### Example
        ```
        Input: AAAACCCGGT
        Output: ACCGGGTTTT
        ```
        """
    )
    return


@app.cell
def __():
    def reverse_complement(dna: str) -> str:
        """Returns the reverse complement of a given DNA strand."""

        complements = {"A": "T", "T": "A", "G": "C", "C": "G"}

        complementary_stand = ""

        for nt in reversed(dna):
            complementary_stand += complements[nt]

        return complementary_stand
    return (reverse_complement,)


@app.cell
def __(reverse_complement):
    actual = reverse_complement("AAAACCCGGT")
    expected = "ACCGGGTTTT"
    assert actual == expected
    return actual, expected


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
