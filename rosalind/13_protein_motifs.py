import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Finding a Protein Motif]()

        ### Background
        A structural and functional unit of the protein is a **protein domain**: in terms of the protein's primary structure, the domain is an interval of amino acids that can evolve and function independently.

        Just like species, proteins can evolve, forming homologous groups called protein families. Proteins from one family usually have the same set of domains, performing similar functions; see Figure 1.

        A component of a domain essential for its function is called a **motif**, a term that in general has the same meaning as it does in nucleic acids, although many other terms are also used (blocks, signatures, fingerprints, etc.) Usually protein motifs are evolutionarily conservative, meaning that they appear without much change in different species.

        Proteins are identified in different labs around the world and gathered into freely accessible databases. A central repository for protein data is **[UniProt](https://www.uniprot.org/)**, which provides detailed protein annotation, including function description, domain structure, and post-translational modifications. UniProt also supports protein similarity search, taxonomy analysis, and literature citations.

        ### UniProt
        To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

        You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
        ```
        http://www.uniprot.org/uniprot/uniprot_id
        ```

        Alternatively, you can obtain a protein sequence in FASTA format by following
        ```
        http://www.uniprot.org/uniprot/uniprot_id.fasta
        ```

        For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

        ### Problem
        **Given:** At most 15 UniProt Protein Database access IDs.

        **Return:** For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

        ### Example
        Input:
        ```
        A2Z669
        B5ZC00
        P07204_TRBM_HUMAN
        P20840_SAG1_YEAST
        ```

        Output:
        ```
        B5ZC00
        85 118 142 306 395
        P07204_TRBM_HUMAN
        47 115 116 382 409
        P20840_SAG1_YEAST
        79 109 135 248 306 348 364 402 485 501 614
        ```
        """
    )
    return


@app.cell
def __(access_id):
    import requests
    from wasims_toolbox import read_fasta

    def get_protein_sequence(access_id: str) -> dict:
        """
        Returns protein sequence from given UniProt access ID
        as dictionary with key-value pairs of name to sequence.

        Args:
            access_id (str): UniProt Protein Database access ID

        Returns:
            dict: Protein name and sequence
        """
        response = requests.get(f"https://rest.uniprot.org/uniprotkb/{access_id}.fasta")
        protein = read_fasta(sequences=response.text)
        return protein

    proteins = {}
    access_ids = ["B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
    for _access_id in access_ids:
        _protein = get_protein_sequence(access_id.split("_")[0])
        proteins.update(_protein)
    proteins
    return access_ids, get_protein_sequence, proteins, read_fasta, requests


@app.cell
def __(proteins):
    def find_n_glycosylation_motifs(protein: str) -> list:
        """
        Returns locations of N-glycosylation motif for
        the given protein using UniProt access ID.

        Args:
            protein (str): Protein sequence

        Returns:
            list: Positions in the protein chain where the
            N-glycosylation motif occurs.
        """
        locations = []
        amino_acids = [
            "A",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "K",
            "L",
            "M",
            "N",
            "Q",
            "R",
            "S",
            "T",
            "V",
            "W",
            "Y",
        ]
        motifs = [f"N{aa1}S{aa2}" for aa1 in amino_acids for aa2 in amino_acids]
        motifs = motifs + [
            f"N{aa1}T{aa2}" for aa1 in amino_acids for aa2 in amino_acids
        ]
        for motif in motifs:
            locations = locations + [
                i + 1 for i in range(len(protein)) if protein.startswith(motif, i)
            ]
        return sorted(locations)

    motif_locations = []
    for _protein in proteins.values():
        motif_locations.append(find_n_glycosylation_motifs(_protein))
    motif_locations
    return find_n_glycosylation_motifs, motif_locations


@app.cell
def __(access_ids, motif_locations):
    def print_solution(access_ids: list, motif_locations: list):
        """Print solution to Rosalind problem."""

        for index, locations in enumerate(motif_locations):
            if len(locations) == 0:
                continue
            locations = [str(loc) for loc in locations]
            print(access_ids[index])
            print(str.join(" ", locations))

    print_solution(access_ids, motif_locations)
    return (print_solution,)


@app.cell
def __(find_n_glycosylation_motifs, proteins):
    import ipytest

    ipytest.autoconfig()

    def test_case():
        expected = [
            [85, 118, 142, 306, 395],
            [47, 115, 116, 382, 409],
            [79, 109, 135, 248, 306, 348, 364, 402, 485, 501, 614],
        ]
        actual = []
        for protein in proteins.values():
            actual.append(find_n_glycosylation_motifs(protein))
        assert actual == expected

    ipytest.run()
    return ipytest, test_case


@app.cell
def __(access_id, find_n_glycosylation_motifs, get_protein_sequence):
    access_ids_1 = [
        "P01047_KNL2_BOVIN",
        "B5FPF2",
        "P81824_PABJ_BOTJA",
        "A9QYR8",
        "A1USX4",
        "Q8WW18",
        "O08537_ESR2_MOUSE",
        "Q50228",
        "P04233_HG2A_HUMAN",
        "P11831_SRF_HUMAN",
        "Q9QSP4",
        "P00740_FA9_HUMAN",
    ]
    proteins_1 = {}
    for _access_id in access_ids_1:
        _protein = get_protein_sequence(access_id.split("_")[0])
        proteins_1.update(_protein)
        print(_protein)
    motif_locations_1 = []
    for _protein in proteins_1.values():
        motif_locations_1.append(find_n_glycosylation_motifs(_protein))
    print(motif_locations_1)
    return access_ids_1, motif_locations_1, proteins_1


@app.cell
def __(access_ids_1, motif_locations_1, print_solution):
    print_solution(access_ids_1, motif_locations_1)
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
