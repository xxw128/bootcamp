import bioinfo_dicts as bd

def one_to_three(seq):
    """
    Converts a protein sequence using one-letter abbrev to
    one using three-letter abbrev.
    """

    #convert sequence to upper case
    seq = seq.upper()

    #do the conversion, but check each AA is valid first
    aa_list = []
    for amino_acid in seq:
        if amino_acid not in bd.aa.keys():
            raise RuntimeError(amino_acid + ' is not valid amino acid.')
        aa_list += [bd.aa[amino_acid],  '-']

    return ''.join(aa_list[:-1])
