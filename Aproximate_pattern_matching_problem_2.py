#this code is just to get the count of the number of pattern occuring in text with at the most 3 nucleotides mismatch
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def approximate_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern_prime = text[i:i + len(pattern)]
        if hamming_distance(pattern, pattern_prime) <= d:
            count += 1
    return count
s1 = "GGGCCGTTGGT"
s2 = "GGACCGTTGAC"
text = "GATCAATCCGGAACCATAAATGAAATTTCCAGCTTGGGCGGCCGTGGTGCGGGTTGACAGGCTGATGGATATCGAGGCTAGGCGGCCATAGTTCCGACTGCAATTCTAAGGCCAAGATTATGCCGATAGGTGGATATATCGGAGGATTTTCGAGTAATCTTTATGTCAGGTCCTCGTCGCATTTCCCAGATTCAAATTCTCTCTCCACGTCCCCCTCGTACGCTGATGCAACATTCCGAACCTGACCAAGTGAGCAGCTAGCGTGCATCAGAGCCCGTTGGACTAAGGCGGGCTAACGGCTAGTTCTTGGGCCATCGCGAGTTCTTCGAGGAACCGGTCCCCT"
pattern = "CCATA"
d = 3

result = approximate_pattern_count(text, pattern, d)

print(result)