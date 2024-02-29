import math

def countMotifPercent(motifs):
    count = {}
    columns = []
    for i in range(len(motifs[0])):
        columns.append([motif[i] for motif in motifs])
    for i in range(len(columns)):
        count[i] = {'A': columns[i].count('A')/len(columns[i]), 'C': columns[i].count('C')/len(columns[i]), 'G': columns[i].count('G')/len(columns[i]), 'T': columns[i].count('T')/len(columns[i])}

    return count

def motifEntropy(motifs):
    entropy = 0
    percents = countMotifPercent(motifs)
    for i in range(len(percents)):
        for nucleotide in percents[i]:
            if percents[i][nucleotide] != 0:
                entropy += percents[i][nucleotide] * math.log2(percents[i][nucleotide])
    return -entropy

# Example motif matrix
motif_matrix = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]

# Calculate and print the entropy
entropy_score = motifEntropy(motif_matrix)
print("Motif Entropy:", entropy_score)
 