import marimo

__generated_with = "0.9.6"
app = marimo.App(app_title="COVID-19 Variant Analysis")


@app.cell(hide_code=True)
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


@app.cell(disabled=True)
def __(global_pairwise_align_nucleotide, sequences, warnings):
    # Deprecating SSW in scikit-bio https://github.com/scikit-bio/scikit-bio/issues/1814
    # Use https://github.com/jeffdaily/parasail-python
    with warnings.catch_warnings(action="ignore"):
        global_pairwise_align_nucleotide(sequences[0], sequences[2])
    return


@app.cell
def __(
    StringIO,
    df_variants,
    mo,
    ncbi_api_base_url,
    reference_fasta,
    requests,
    skbio,
):
    def get_fasta(ncbi_id: str):
        return requests.get(
            f"{ncbi_api_base_url}?db=nuccore&id={ncbi_id}&rettype=fasta&retmode=text"
        ).text


    def parse_sequence(fasta_str: str):
        fasta_io = StringIO(fasta_str)
        sequence = next(
            skbio.read(fasta_io, format="fasta", constructor=skbio.DNA)
        )
        return sequence


    @mo.cache
    def get_sequences():
        sequences = []

        for id in df_variants["NCBI ID"].tolist():
            if id == "Reference":
                _fasta = requests.get(reference_fasta).text
            else:
                _fasta = get_fasta(id)
            _sequence = parse_sequence(_fasta)
            sequences.append(_sequence)

        return sequences
    return get_fasta, get_sequences, parse_sequence


@app.cell
def __():
    ncbi_api_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    reference_fasta = (
        "https://viralzone.expasy.org/resources/Coronav/Wuhan-Hu-1%5Fgenome.fasta"
    )
    return ncbi_api_base_url, reference_fasta


@app.cell
def __():
    import requests
    import warnings
    import marimo as mo
    import pandas as pd
    import skbio
    from skbio import DNA, TabularMSA
    from skbio.alignment import global_pairwise_align_nucleotide
    from io import StringIO
    return (
        DNA,
        StringIO,
        TabularMSA,
        global_pairwise_align_nucleotide,
        mo,
        pd,
        requests,
        skbio,
        warnings,
    )


if __name__ == "__main__":
    app.run()
