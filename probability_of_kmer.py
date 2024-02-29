def calculate_probability(kmer, profile):

    probability = 1.0

    nucleotides = {'A', 'C', 'G', 'T'}

 

    for i, nucleotide in enumerate(kmer):

        probability *= profile[nucleotide][i]

 

    return probability

 

# Define the profile matrix as a dictionary

profile = {

    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],

    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],

    'G': [0.0, 0.0, 1, 1, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]

}

 

# Example k-mer

kmer = "TCGGGGATTTCC"

 

# Calculate the probability

probability = calculate_probability(kmer, profile)

 

print(f"Pr({kmer} | Profile) = {probability}") 