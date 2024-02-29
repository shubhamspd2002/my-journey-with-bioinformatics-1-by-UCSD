def hamming_distance(pattern, text):
    return sum(1 for i in range(len(text) - len(pattern) + 1) if text[i:i+len(pattern)] != pattern)

def median_string(k, dna):
    distance = float('inf')
    pattern = ""

    for i in range(len(dna[0]) - k + 1):
        current_pattern = dna[0][i:i+k]
        current_distance = sum(min(hamming_distance(current_pattern, seq[i:i+k]) for seq in dna) for i in range(len(dna[0]) - k + 1))

        if current_distance < distance:
            distance = current_distance
            pattern = current_pattern

    return pattern

# New example usage with the provided dataset
k = 7
dna = [
"CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",

"GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",

"GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"
]

result = median_string(k, dna)
print(result)