import itertools

# Function to compute the hamming distance between two strings
def hamming_distance(p, q):
    return sum(el1 != el2 for el1, el2 in zip(p, q))

# Function to find all possible k-mers
def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for x in nucleotides:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood

# Function to find the reverse complement of a DNA sequence
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna[::-1])

# Function to find the most frequent patterns with mismatches and reverse complements
def frequent_words_with_mismatches_and_rc(text, k, d):
    patterns = {}
    n = len(text)
    for i in range(n - k + 1):
        sequence = text[i:i+k]
        f
d = 1
result = frequent_words_with_mismatches_and_rc(genome, k, d)
print(result)or neighbor in neighbors(sequence, d):
    
        patterns[neighbor] = patterns.get(neighbor, 0) + 1
            patterns[reverse_complement(neighbor)] = patterns.get(reverse_complement(neighbor), 0) + 1
    max_count = max(patterns.values())
    return [pattern for pattern, count in patterns.items() if count == max_count]

# File path
file_path = r'C:\Users\Ameen\Downloads\sequence.txt'

# Read the genome sequence from the file
with open(file_path, 'r') as f:
    genome = ''.join(line.strip() for line in f if not line.startswith('>'))

# Find the most frequent patterns with mismatches and reverse complements
k = 4

#the results was ['GCCG', 'CGGC'] for entire genome of Salmonella enterica. the link for the entire genome is https://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt


