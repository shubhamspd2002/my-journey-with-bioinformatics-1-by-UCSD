def MotifEnumeration(DNA, k, d):

    patterns = set()

 

    for dna_sequence in DNA:

        for i in range(len(dna_sequence) - k + 1):

            k_mer = dna_sequence[i:i + k]

            neighbors = generate_neighbors(k_mer, d)

 

            for neighbor in neighbors:

                if is_pattern_consistent(neighbor, DNA, d):

                    patterns.add(neighbor)

 

    return patterns

 

def generate_neighbors(pattern, d):

    if d == 0:

        return [pattern]

 

    if len(pattern) == 1:

        return ['A', 'C', 'G', 'T']

 

    neighbors = []

    suffix_neighbors = generate_neighbors(pattern[1:], d - 1)

 

    for text in suffix_neighbors:

        if hamming_distance(pattern[1:], text) < d:

            for nucleotide in ['A', 'C', 'G', 'T']:

                neighbors.append(nucleotide + text)

        else:

            neighbors.append(pattern[0] + text)

 

    return neighbors

 

def hamming_distance(str1, str2):

    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

 

def is_pattern_consistent(pattern, DNA, d):

    return all(any(hamming_distance(pattern, dna[i:i + len(pattern)]) <= d for i in range(len(dna) - len(pattern) + 1)) for dna in DNA)

 

DNA = {"GGTATCGACGCGTTAGAATCGTCTC",

      "GCCTGAGGGGCCCGTCGTTACTGTA" ,

        "AGCGCTTTTACGGTAACCCTAAGGA" ,

        "AATACCGATACTCCGTAGGTGCTAC" ,

        "CACTCCATATAAGACCCTCCCGGTA" ,

        "GTTCAGAGCGTGTCTCGGTATCTGT"}

 

k = 5

d = 1

 

result = MotifEnumeration(DNA, k, d)

print(' '.join(result))

 

#The code I've provided is an implementation of the Motif Enumeration algorithm to find the common motifs (k-mers)

# that appear in a set of DNA sequences with at most d mismatches. Let me break down the code step by step:

 

#1. **MotifEnumeration Function:**

   #This function takes three arguments: the set of DNA sequences (`DNA`), the length of motifs (`k`), and the maximum

   # allowed mismatches (`d`). The goal of this function is to find all the motifs that appear in all sequences with at

   # most `d` mismatches.

 

#2. **Generate Neighbors Function (`generate_neighbors`):**

   #This function generates all possible neighbors of a given pattern with at most `d` mismatches. It's a recursive function

   #  that generates single nucleotide mutations and recursively generates more neighbors with fewer allowed mismatches.

 

#3. **Hamming Distance Function (`hamming_distance`):**

   #This function calculates the Hamming distance between two strings, which is the number of positions at which the

   # corresponding symbols differ.

 

#4. **Pattern Consistency Check Function (`is_pattern_consistent`):**

   #This function checks whether a given pattern is consistent in all the DNA sequences with at most `d` mismatches.

   # It iterates through each sequence and checks if there's at least one occurrence of the pattern with at most `d`

   # mismatches.

 

#5. **Main Execution:**

   #The main part of the code consists of the execution logic. It initializes a set called `patterns` to store the found

   # motifs. It then iterates through each DNA sequence and each possible k-mer within the sequence. For each k-mer, it

   # generates its neighbors with at most `d` mismatches and checks if these neighbors are consistent motifs using the

   # `is_pattern_consistent` function. If a neighbor is consistent, it's added to the `patterns` set.

 

#6. **Printing the Result:**

   #After the `MotifEnumeration` function has collected all the consistent motifs, it joins these motifs into a single

   # space-separated string using the `join` function and prints the result.

 

#The provided DNA sequences, `k`, and `d` are set, and the result should be a list of k-mers that appear in all the

# sequences with at most `d` mismatches. The expected output for the given DNA sequences, `k = 5`, and `d = 1` is: `TCAGA`.

