import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Computing GC Content](https://rosalind.info/problems/gc/)

        ### Background
        The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

        DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

        In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

        ### Problem
        **Given:** At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

        **Return:** The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

        ### Example
        Input:

        ```
        >Rosalind_6404
        CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
        TCCCACTAATAATTCTGAGG
        >Rosalind_5959
        CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
        ATATCCATTTGTCAGCAGACACGC
        >Rosalind_0808
        CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
        TGGGAACCTGCGGGCAGTAGGTGGAAT
        ```

        Output:

        ```
        Rosalind_0808
        60.919540
        ```
        """
    )
    return


@app.cell
def __():
    def get_max_gc_content(data_file: str):
        """Returns DNA strand with highest GC content in a given FASTA file."""
        dna_strand = ""
        max_gc_content = 0
        with open(data_file, "r") as file:
            lines = file.read().splitlines()
            gc_count = 0
            total_nt = 0
            curr_strand = ""
            for index, line in enumerate(lines):
                if index == 0:
                    curr_strand = line.replace(">", "")
                    continue
                if not line.startswith(">Rosalind"):
                    gc_count = gc_count + line.count("G") + line.count("C")
                    total_nt = total_nt + len(line)
                    if not line == lines[-1]:
                        continue
                gc_content = gc_count / total_nt * 100
                if gc_content > max_gc_content:
                    dna_strand = curr_strand
                    max_gc_content = round(gc_content, 6)
                curr_strand = line.replace(">", "")
                gc_count, total_nt = (0, 0)
        return (dna_strand, max_gc_content)

    return (get_max_gc_content,)


@app.cell
def __(get_max_gc_content):
    dna_strand, gc_content = get_max_gc_content("./sample_datasets/05_sample_01.txt")
    print(dna_strand)
    print(gc_content)
    return dna_strand, gc_content


@app.cell
def __(get_max_gc_content):
    dna_strand_1, gc_content_1 = get_max_gc_content(
        "./sample_datasets/05_sample_02.txt"
    )
    print(dna_strand_1)
    print(gc_content_1)
    return dna_strand_1, gc_content_1


@app.cell
def __(mo):
    mo.md(
        r"""
        ### More information
        Why would we want to calculate GC content? Why does GC content even matter?

        At the prokaryotic level, GC content correlates coding-sequence length, correlates with certain secondary RNA structures, and there is also a noted bias towards low GC content in stop codons (TAG, TAA, and TGA). These are just to name a few situations where rich GC regions and GC poor regions correlate with functional significance.

        Long coding regions in vertebrates and prokaryotes are significantly correlated with GC content; long coding regions tend to be GC-rich where as short coding regions tend to be GC poor. Since codons are biased towards being AT rich, mutations in AT rich regions can likely lead to the generation of stop codons. Whereas in GC regions, many such mutations might be required to spontaneously lead to stop codons.

        Therefore, conserved regions across organisms are likely GC rich.
        """
    )
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
