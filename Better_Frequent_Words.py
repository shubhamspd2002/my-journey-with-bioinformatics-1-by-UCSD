"""
following is the pseudocode for the better frequent words program:


    FrequentWordsWithMismatches(Text, k, d)
    Patterns ← an array of strings of length 0
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n - k
        Pattern ← Text(i, k)
        neighborhood ← Neighbors(Pattern, d)
        for j ← 0 to |neighborhood| - 1
            neighbor ← neighborhood[j]
            if freqMap[neighbor] doesn't exist
                freqMap[neighbor] ← 1
            else
                freqMap[neighbor] ← freqMap[neighbor] + 1
    m ← MaxMap(freqMap)
    for every key Pattern in freqMap
        if freqMap[Pattern] = m
            append Pattern to Patterns
    return Patterns
    
    try to find the differences between this program and  Frequent_words_with_mismatches_problem.py program because both give the same output 
    but this program runs way faster than Frequent_words_with_mismatches_problem.py for the same data
"""
from collections import defaultdict

def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = Neighbors(pattern[1:], d)
    
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    
    return neighborhood

def HammingDistance(p, q):
    return sum(pi != qi for pi, qi in zip(p, q))

def MaxMap(freqMap):
    return max(freqMap.values())

def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = defaultdict(int)
    n = len(Text)

    for i in range(n - k + 1):
        Pattern = Text[i:i+k]
        neighborhood = Neighbors(Pattern, d)

        for neighbor in neighborhood:
            freqMap[neighbor] += 1

    m = MaxMap(freqMap)

    for pattern in freqMap:
        if freqMap[pattern] == m:
            Patterns.append(pattern)

    return Patterns

# Example usage:
Text = "TCTCTGCTCTTTGCTAAAAAAAAATGCTAAAAAATCTCTTTGCTCTTTGCTTCTCTCTCTCTCTGCTTCTTGCTAAATGCTTGCTCTTAAACTTCTTAAATCTCTCTCTGCTAAACTTTCTTGCTCTTTCTCTGCTTCTCTCTCCTTAAATCTCTCTTGCTAAATGCTTCTTCTTCTCCTTTCTAAAAAATGCTTGCTTCTCTCTCAAATCTCTGCTTGCTTGCTCTTTCTCAAATCTTCTAAAAAAAAACTTAAATCTCCTTCTTTCTCAAACTTCTTTGCTTCTCTCTCCTTCTTTGCTTCTCCTTAAATCTCCTTTCTTCTCTGCTTCTCTCTTCTAAATCTTCTCTGCT"
k = 6
d = 3

result = FrequentWordsWithMismatches(Text, k, d)

print(result) #OP with [ ] , and ' '

print(" ".join(map(str, result))) #OP without [ ] , and ' '

#try and compile with text as salmonella enterica genome at link https://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt and d = 1, k = 9. see if u get OP as 