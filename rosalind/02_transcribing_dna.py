import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Transcribing DNA into RNA](https://rosalind.info/problems/rna/)

        ### Background
        An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

        Given a DNA string `t` corresponding to a coding strand, its transcribed RNA string `u` is formed by replacing all occurrences of 'T' in `t` with 'U' in `u`.

        ### Problem
        **Given:** A DNA string `t` having length at most 1000 nt.

        **Return:** The transcribed RNA string of `t`.

        ### Example
        Input:
        ```
        GATGGAACTTGACTACGTAAATT
        ```

        Output:
        ```
        GAUGGAACUUGACUACGUAAAUU
        ```
        """
    )
    return


@app.cell
def __():
    def transcribe(dna: str) -> str:
        """Transcribes DNA coding strand into RNA."""
        return dna.replace("T", "U")
    return (transcribe,)


@app.cell
def __(transcribe):
    expected = "GAUGGAACUUGACUACGUAAAUU"
    actual = transcribe("GATGGAACTTGACTACGTAAATT")
    assert actual == expected
    return actual, expected


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
