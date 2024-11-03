import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Calculating Protein Mass](https://rosalind.info/problems/prtm/)

        ### Background
        When two amino acids link together, they form a peptide bond, which releases a molecule of water. Thus, after a series of amino acids have been linked together into a polypeptide, every pair of adjacent amino acids has lost one molecule of water, meaning that a polypeptide containing `n` amino acids has had `n − 1` water molecules removed.

        More generally, a residue is a molecule from which a water molecule has been removed; every amino acid in a protein are residues except the leftmost and the rightmost ones. These outermost amino acids are special in that one has an "unstarted" peptide bond, and the other has an "unfinished" peptide bond. Between them, the two molecules have a single "extra" molecule of water (see the atoms marked in blue in Figure 2). 

        **Thus, the mass of a protein is the sum of masses of all its residues plus the mass of a single water molecule.**

        There are two standard ways of computing the mass of a residue by summing the masses of its individual atoms. Its monoisotopic mass is computed by using the principal (most abundant) isotope of each atom in the amino acid, whereas its average mass is taken by taking the average mass of each atom in the molecule (over all naturally appearing isotopes).

        Many applications in proteomics rely on mass spectrometry, an analytical chemical technique used to determine the mass, elemental composition, and structure of molecules. In mass spectrometry, monoisotopic mass is used more often than average mass, and so all amino acid masses are assumed to be monoisotopic unless otherwise stated.

        The standard unit used in mass spectrometry for measuring mass is the atomic mass unit, which is also called the dalton (Da) and is defined as one twelfth of the mass of a neutral atom of carbon-12. The mass of a protein is the sum of the monoisotopic masses of its amino acid residues plus the mass of a single water molecule (whose monoisotopic mass is 18.01056 Da).

        In the following several problems on applications of mass spectrometry, we avoid the complication of having to distinguish between residues and non-residues by only considering peptides excised from the middle of the protein. This is a relatively safe assumption because in practice, peptide analysis is often performed in tandem mass spectrometry. In this special class of mass spectrometry, a protein is first divided into peptides, which are then broken into ions for mass analysis.

        ### Problem
        The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

        **Given:** A protein string `P` of length at most 1000 aa.

        **Return:** The total weight of `P`.

        ### Example
        Input:
        ```
        SKADYEK
        ```

        Output:
        ```
        821.392
        ```
        """
    )
    return


@app.cell
def __():
    from utils import ProteinToolbox

    def calculate_protein_mass(protein: str) -> float:
        """Returns mass (in Daltons) of the given polypeptide chain."""

        mass = 0
        toolbox = ProteinToolbox()

        for amino_acid in protein:
            mass += toolbox.monoisotopic_mass_table[amino_acid]

        return mass
    return ProteinToolbox, calculate_protein_mass


@app.cell
def __(calculate_protein_mass):
    actual = calculate_protein_mass("SKADYEK")
    expected = 821.392
    assert round(actual, 3) == expected
    return actual, expected


@app.cell
def __(calculate_protein_mass):
    protein = "TFAYKWQYGEYMWDCMHWHQWRTWMLWQRCSSQMKDSPPEINASTIIVSPRTDQLTGIMQIIEKWHPNVCQDYRAGCDFKKCVFKIYLNLPTSNTQNMMTMKRKESFPCTDRKARDHATRWNMRYDSWWACHHVCIDWKHWETMKEQKHPNMQDNYGETQLFKHEYKWGQANCKFCSHGIEQSWRMVFGPYIPGHFYIASQALKVTREECSQTCTEKGWGFWKTWKICAKTSCYQICHWTMVTWSNYDVRCFSCLLLTEMKLYLFHVQPQWYETYGCRFDYQIYIHMGGLPWCTSPGGGPNQDLFDAEGFNPDISWNISFHYICNPYRTLTNPSPIFQMYFGKYIDAFGIDTNLHVVESPFAIWWNQWGWPIMKVHVQISWHEKQDRKDPQFHKQNNRTERNKRLYFSMSKRWVVMMFGEMDHGKNILGFDHDYVSFMANMPKYSRHYGHHTDNVGQNFEKKSNCRIWGCEYLAWIEYHWNTRVAVKQKVHALICSYIFQFIILFKNESICWVHSIMAPLAIDWQTTQIPWAGVAWTIVIAQASTRWGIYGHAAWRYHCMTMSYGELQNSWMIKYWFIAKCHHNPWQCKSWHICQRMPHIPEHQLAMEHTTCASHTICSKREACPNKHIQSSKNHQAFGSHVLMLCAHMFMYFMSLVYDPGMRTKYYSICTAFVWKWVMTLLEQCRCENAACKLHEYDLINPIAYWFAPIRTCTHNWNDLLGCKELSNYRTDSNRMGEPYTLNQPVTENPGKVVTTLLYTVGRIAKTDPAHYAIWPVHDIKCLKTAISSTNHGRPMNARHQDWHDQKKIWSSEPNPRFDDRRPPNNDPPYHYNHFDDHDQSHQLSCREGANPKIGKWINHMEMCDQLFHNHIVTPRLLQVGMIQAAHQTCIMSTSMPKIDNYFKVYFQHSHNEKRMINPAEIDKPGW"
    mass = calculate_protein_mass(protein)
    round(mass, 3)
    return mass, protein


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
