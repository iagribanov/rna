def to_rna(dna_strand):
    dna_strand = dna_strand.replace('A','U').replace('G','K').replace('C','O').replace('T','A')
    dna_strand=dna_strand.replace('K','C').replace('O','G')
    return dna_strand
