'''Построить РНК'''


def dna_to_rna(dna):
    replacement_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
    rna = ''.join(replacement_dict.get(base, base) for base in dna)
    return rna


rna_output = dna_to_rna(str(input()))
print("result:", rna_output)
