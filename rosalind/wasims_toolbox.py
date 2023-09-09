# Name: Wasim Sandhu
# Date Created: 09-08-2023
# Description: Collection of functions authored for
# various Rosalind problems and commonly reused

def read_fasta(sequences: str=None, file_path: str=None) -> dict:
    
    """
    Returns sequences in FASTA format as dictionary 
    with key-value pairs of name to sequence.
    
    Args:
        sequences (str): Sequences in FASTA format
        file_path (str): Path to FASTA file
    
    Returns:
        dict: Key-value pairs of name to sequence
    """

    reads = {}
    
    if sequences is not None:
        lines = sequences.splitlines()
        
    elif file_path is not None:
        with open(file_path, "r") as file:
            lines = file.read().splitlines()
            
    else:
        raise Exception("Error: No FASTA sequences given")
    
    last_line = lines[-1]
    
    for line in lines:
        if not line.startswith(">"):
            reads[read] += line
            continue
        
        if line == last_line:
            break
        
        read = line.replace(">", "")
        reads[read] = ""

    return reads
    

def get_reads(fasta_file: str) -> dict:
    """(Deprecated) Reads sequences from FASTA file"""
    return read_fasta(file_path=fasta_file)


def generate_profile_matrix(reads: list) -> dict:

    """
    Generates profile matrix with shape 4 x n for 
    collection of DNA strands with length n.

    Args:
        reads (dict): Dictionary with key-value pairs of
        read titles and DNA strands from a FASTA file.

    Returns:
        dict: 4 x n profile matrix for given DNA strands.
    """
    
    profile_matrix = {
        "A": [0 for nt in reads[0]],
        "C": [0 for nt in reads[0]],
        "G": [0 for nt in reads[0]],
        "T": [0 for nt in reads[0]]
    }
    
    for index in range(len(reads[0])):
        for read in reads:
            profile_matrix[read[index]][index] += 1
    
    return profile_matrix


def get_consensus(profile_matrix: dict) -> str:
    
    """Returns first consensus strand found from the given profile matrix.

    Args:
        profile_matrix (dict): Profile matrix of dimension 4 x n,
        with nucleotide occurrences in each strand of length n.

    Returns:
        str: Consensus strand
    """
    
    consensus_strand = ""
    length = len(profile_matrix["A"])
    
    for index in range(length):
        nt = "-"
        max = 0
        for key in profile_matrix.keys():
            occurrences = profile_matrix[key][index]
            if occurrences > max:
                max = occurrences
                nt = key
        consensus_strand += nt
    
    return consensus_strand