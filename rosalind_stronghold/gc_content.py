"""fasta = open('rosalind_gc.txt', 'r')

# print(fasta.readlines())

numLines = 0
i = 0

with open('rosalind_gc.txt', 'r') as file:
    for line in file:
        #print(i)
        #print(line)
        #i += 1
        numLines += 1

seq_name = []
seq_dna = []
seq_temp = ''

with open('rosalind_gc.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            seq_dna.append(seq_temp)
            if seq_temp:
                seq_dna.append(seq_temp)
            break
        else:
            line = line.upper()
        if all([k == k.upper() for k in file]):
            seq_temp = seq_temp + line
seq_dna.append(seq_temp)

gc_list = []

for i in seq_dna:
    c = 0
    for k in i:
        if k == 'G' or k == 'C':
            c += 1
    gc_content = float(c)/len(i) * 100
    gc_list.append(gc_content)

gc_highest = max(gc_list)


# print(seq_name)
print(seq_dna)
# print(gc_list)
# print(gc_highest)

def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results[label] = bases

    return results

def gc_content(s):
    n = len(s)
    m = 0

    for c in s:
        if c == 'G' or c == 'C':
            m += 1

    return 100 * (float(m) / n)

if __name__ == "__main__":
    large_dataset = open('rosalind_gc.txt').read()

    results = parse_fasta(large_dataset)
    results = dict([(k, gc_content(v)) for k, v in results.items()])

    highest_k = None
    highest_v = 0

    for k, v in results.items():
        if v > highest_v:
            highest_k = k
            highest_v = v

    print(highest_k)
    print('%f%%' % highest_v)


f = open('rosalind_gc.txt', 'r')

max_gc_name = ''
max_gc_content = 0
"""""

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()
