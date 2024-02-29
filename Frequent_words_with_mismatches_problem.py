from itertools import product

def generate_kmers_with_mismatches(kmer, d):
    bases = 'ACGT'
    kmers_with_mismatches = []

    # Generate all possible combinations of bases with up to d mismatches
    for indices in product(range(len(kmer)), repeat=d):
        for replacements in product(bases, repeat=d):
            modified_kmer = list(kmer)
            for index, replacement in zip(indices, replacements):
                modified_kmer[index] = replacement
            kmers_with_mismatches.append(''.join(modified_kmer))

    return set(kmers_with_mismatches)

def frequent_kmers_with_mismatches(text, k, d):
    frequent_kmers = {}
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmers_with_mismatches = generate_kmers_with_mismatches(kmer, d)
        
        for modified_kmer in kmers_with_mismatches:
            if modified_kmer not in frequent_kmers:
                frequent_kmers[modified_kmer] = 1
            else:
                frequent_kmers[modified_kmer] += 1

    max_frequency = max(frequent_kmers.values())

    return [kmer for kmer, frequency in frequent_kmers.items() if frequency == max_frequency]

# Example usage:
text = "TCTCTGCTCTTTGCTAAAAAAAAATGCTAAAAAATCTCTTTGCTCTTTGCTTCTCTCTCTCTCTGCTTCTTGCTAAATGCTTGCTCTTAAACTTCTTAAATCTCTCTCTGCTAAACTTTCTTGCTCTTTCTCTGCTTCTCTCTCCTTAAATCTCTCTTGCTAAATGCTTCTTCTTCTCCTTTCTAAAAAATGCTTGCTTCTCTCTCAAATCTCTGCTTGCTTGCTCTTTCTCAAATCTTCTAAAAAAAAACTTAAATCTCCTTCTTTCTCAAACTTCTTTGCTTCTCTCTCCTTCTTTGCTTCTCCTTAAATCTCCTTTCTTCTCTGCTTCTCTCTTCTAAATCTTCTCTGCT"
k = 6
d = 3

result = frequent_kmers_with_mismatches(text, k, d)

#text = "ACGTTGCATGTCGCATGATGCATGAGAGCT" 
# k = 4 
# d = 1 
# print(result) 
# for this the output will be ['ATGT', 'GATG', 'ATGC']. to obtain the result without ' ' , and [ ] following is the program

print(" ".join(map(str, result)))