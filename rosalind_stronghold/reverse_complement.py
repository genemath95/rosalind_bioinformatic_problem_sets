dna_seq = open('rosalind_revc.txt', 'r').read()
test = 'AAAACCCGGT'

def reverse_complement(seq):
    comp = ""
    result = ""
    for i in seq:
        if i == 'A':
            comp = comp + 'T'
        elif i == 'C':
            comp = comp + 'G'
        elif i == 'T':
            comp = comp + 'A'
        elif i == 'G':
            comp = comp + 'C'
    for i in range(len(comp) - 1, -1, -1):
        result += comp[i]
    print(result)

reverse_complement(dna_seq)


