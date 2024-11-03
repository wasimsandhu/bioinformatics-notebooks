import marimo

__generated_with = "0.9.8"
app = marimo.App(width="columns", app_title="COVID-19 Variant Analysis")


@app.cell(column=0, hide_code=True)
def __(pd):
    # SARS-CoV-2 variants - ViralZone https://viralzone.expasy.org/9556
    df_variants = pd.DataFrame(
        [
            {
                "Lineage": "Reference",
                "Emergence": "China, Dec 2019",
                "Phenotype": "Reference for variants",
                "NCBI ID": "Reference",
            },
            {
                "Lineage": "Alpha",
                "Emergence": "UK, Sep 2020",
                "Phenotype": "Increased transmissibility: 29%",
                "NCBI ID": "MZ344997.1",
            },
            {
                "Lineage": "Beta",
                "Emergence": "South Africa, Aug 2020",
                "Phenotype": "Increased transmissibility: 25%",
                "NCBI ID": "MW598419.1",
            },
            {
                "Lineage": "Delta",
                "Emergence": "India, Dec 2020",
                "Phenotype": "Increased transmissibility: 97%",
                "NCBI ID": "MZ009823",
            },
            {
                "Lineage": "Omicron BA.1",
                "Emergence": "South Africa, Dec 2021",
                "Phenotype": "Less pathogenic than previous variants",
                "NCBI ID": "OL672836.1",
            },
        ]
    )
    df_variants
    return (df_variants,)


@app.cell
def __(get_sequences):
    sequences = get_sequences()
    sequences
    return (sequences,)


@app.cell
def __(align, sequences):
    matrix = align.SubstitutionMatrix.std_nucleotide_matrix()
    alignments = align.align_optimal(
        sequences[0],
        sequences[2],
        matrix,
        gap_penalty=(-10, -1),
        terminal_penalty=False,
    )
    return alignments, matrix


@app.cell
def __(alignments):
    alignments
    return


@app.cell
def __(alignments, graphics, matrix, plt):
    fig = plt.figure(figsize=(8.0, 2.5))
    ax = fig.add_subplot(111)
    graphics.plot_alignment_similarity_based(
        ax,
        alignments[0],
        matrix=matrix,
        labels=["Reference", "Beta variant"],
        show_numbers=True,
        show_line_position=True,
    )
    fig.tight_layout()
    plt.show()
    return ax, fig


@app.cell(column=1)
def __():
    import requests
    import warnings
    import marimo as mo
    import pandas as pd
    from io import StringIO
    import matplotlib.pyplot as plt
    import biotite.database.entrez as entrez
    import biotite.sequence as seq
    import biotite.sequence.align as align
    import biotite.sequence.graphics as graphics
    import biotite.sequence.io.fasta as fasta

    return (
        StringIO,
        align,
        entrez,
        fasta,
        graphics,
        mo,
        pd,
        plt,
        requests,
        seq,
        warnings,
    )


@app.cell
def __(
    StringIO,
    df_variants,
    entrez,
    fasta,
    mo,
    reference_fasta,
    requests,
    seq,
):
    @mo.cache
    def get_sequences():
        sequences = []

        for id in df_variants["NCBI ID"].tolist():
            if id == "Reference":
                fasta_str = requests.get(reference_fasta).text
                fasta_io = StringIO(fasta_str)
                fasta_file = seq.io.fasta.FastaFile.read(fasta_io)
            else:
                fasta_file = fasta.FastaFile.read(
                    entrez.fetch_single_file([id], None, "nuccore", "fasta")
                )

            for name, sequence in fasta_file.items():
                _sequence = seq.NucleotideSequence(sequence)
                sequences.append(_sequence)

        return sequences

    return (get_sequences,)


@app.cell
def __():
    # CONSTANTS
    reference_fasta = (
        "https://viralzone.expasy.org/resources/Coronav/Wuhan-Hu-1%5Fgenome.fasta"
    )
    return (reference_fasta,)


if __name__ == "__main__":
    app.run()
