def entropy(probabilities):

    """   

    :param probabilities: A list of probabilities.

    :return: O value gives entropy.

    """

    ent = 0

    for p in probabilities:

        if p > 0:

            ent -= p * math.log2(p)

    return ent

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

 

 

nucleotide_counts = {nucleotide: [] for nucleotide in "ACGT"}

 

for column in zip(*motif_matrix):

    for nucleotide in "ACGT":

        count = column.count(nucleotide) / len(column)

        nucleotide_counts[nucleotide].append(count)

 

column_entropies = []

for nucleotide in "ACGT":

    ent = entropy(nucleotide_counts[nucleotide])

    column_entropies.append(ent)

 

total_entropy = sum(column_entropies)

 

print("Entropia total:", total_entropy)

 



