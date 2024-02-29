#this program is to to find the positions in the given genome at which the pattern occurs 
#


pattern = "ATAT"
genome = ""

def find_pattern_positions(pattern, genome):
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)

    return positions

result = find_pattern_positions(pattern, genome)
print(" ".join(map(str, result)))