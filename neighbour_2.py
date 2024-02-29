#here neighbour has been modified to generate all k-mers of Hamming distance exactly d from Pattern. That means give output of neighbours of 
#kmer with hamming distance exactly 2. i.e there has to be 2 mismatching nucleotides
def loop_count():
    successful_runs = 0
    while(True):
        successful_runs += 1
        return successful_runs
    
    
def neighbors(pattern, d):
    
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) == d:
            for nucleotide in 'ACGT':
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
        loop_count
         
    return neighborhood

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# Example usage:
pattern = "TGCAT"
d = 2


result = neighbors(pattern, d)
count = loop_count()

print(" ".join(map(str, result)), pattern) #note that the pattern string itself is also a neighbour of pattern 

print("the total number of neighbours are: ", count)

#ask mayur how to get loop count of the def neighbours(pattern, d) function