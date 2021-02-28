codon_table = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
               'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
               'TAT': 'Y', 'TAC': 'Y', 'TGT': 'C', 'TGC': 'C',
               'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L',
               'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
               'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q',
               'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
               'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
               'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T',
               'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
               'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R',
               'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V',
               'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A',
               'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E',
               'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
               'GGG': 'G', 'TAA': '-', 'TAG': '-', 'TGA': '-',
}

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
    return result

def translate(mrna):
    protein = ''
    for i in range(0, len(mrna), 3):
        try:
            codon = mrna[i:i+3]
            if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                protein += codon_table[codon]
                break
            else:
                #print(codon)
                protein += codon_table[codon]
        except:
            pass
    if protein[-1] != '-':
        return('gay')
    else:
        protein = protein[0:len(protein)-1]
        return(protein)

def orf(seq):
    output = ''
    list = []
    for i in range(0, len(seq), 1):
        scan = seq[i:i+3]
        if scan == 'ATG':
            #output = output + str(i+1) + ' '
            temp = seq[i:]
            if translate(temp) == 'gay' or translate(temp) in list:
                pass
            else:
                list.append(translate(temp))
        else:
            pass
    rev = reverse_complement(seq)
    for i in range(0, len(rev), 1):
        scan = rev[i:i+3]
        if scan == 'ATG':
            #output = output + str(i+1) + ' '
            temp = rev[i:]
            if translate(temp) == 'gay' or translate(temp) in list:
                pass
            else:
                list.append(translate(temp))
        else:
            pass
    print("\n".join(list))

#orf('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
orf('CCTGCCATGCAGGCAGCTAATCAACTCTGAGGTGTCAGCCACATCGACAACATACGAACTTTGACGTGTTGCGGATTCCTTGCACTGATCTGGGGCCTCTCATGTAGAACTGATTTACCCCGCACATCAGACCTTCTATCATTCCACTTAACGGAGCTGCGGAAGACGGGTGAGTATGACTTCGCTGAGCGAGTGAGAAACCACCACTATCCACACTCGGACCAGCATCCCAAGCTAGGTCGATGCGCCCGTCACTGGAAACTCATCATGACTGACACGCACTTATGAGGGAGTGACTAGTTCAGCTGTCGTCTTCTGGTGCTCGTAATTCTGAAGTGTGCCGCGGGTACTCCAGGCCCCAGGTGACGACCAGAGTCCTCCTTGAGTACCGTTTAACATGCCAATGCTTTATATGCATTGAAGCTAAGCGCAGCCTTTATAGCTATAAAGGCTGCGCTTAGCTTCAATGCATTACTGCGAACGTAAAGGCCAAGTCAGCCCTTCTGCTTCTAGATAGTGTAGACCGTATGTACTGCTCTTTTACTGACACAAATCCACATTGTCAGGGTTCGTCGAGCCAAAATCCCGAATATAATCCGCTATCTTCACTAAAATGCGTAATGACACTCATCCCACTCTCGGAACTTGGTTCGTGGACAGGGGGGTGACAGACTATAGGTAGGATGCTCCGACCAAGCTCCCGGACTATGCGCCAACAAGTTTTATTGGGTACGCTCCTGTTTTGGAGGAAGGGGGGACATTAGTTGCTTGGCAGTGTAAGGGTCGCCGGTCCAGATAATGCGGCCGCCAGCCCGTTAAGTAAAAAAACTCACAACCGTGTCGTGGGCTCCAAGTCATAAATCCTGTTGCGAAAAGCATAGCAT')

data = open('rosalind_prot.txt', 'r').read()

#translate('TAAAGCCATGTAGCTAACTCAGGTTACATGGGGATGAC')




