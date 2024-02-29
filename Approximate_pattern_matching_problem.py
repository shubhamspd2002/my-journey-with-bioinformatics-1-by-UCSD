
def hamming_distance(str1, str2):
    # Calculate the Hamming distance between two strings of equal length
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))
 

def approximate_pattern_matching(pattern, text, d):
    positions = [] 
    count = 0                                       # Iterate through each substring of the text with the same length as the pattern
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]

        # Check if the Hamming distance is at most d
        if hamming_distance(pattern, substring) <= d:
            positions.append(i)   
            
            count += 1     
            
        
    print(count)  
    return positions
 
 

# Example usage:
pattern = "CCATA"
text = "GATCAATCCGGAACCATAAATGAAATTTCCAGCTTGGGCGGCCGTGGTGCGGGTTGACAGGCTGATGGATATCGAGGCTAGGCGGCCATAGTTCCGACTGCAATTCTAAGGCCAAGATTATGCCGATAGGTGGATATATCGGAGGATTTTCGAGTAATCTTTATGTCAGGTCCTCGTCGCATTTCCCAGATTCAAATTCTCTCTCCACGTCCCCCTCGTACGCTGATGCAACATTCCGAACCTGACCAAGTGAGCAGCTAGCGTGCATCAGAGCCCGTTGGACTAAGGCGGGCTAACGGCTAGTTCTTGGGCCATCGCGAGTTCTTCGAGGAACCGGTCCCCT"
d = 3


#in the following program you wil get OP in [ ] with numbers seperated by spaces
# result = approximate_pattern_matching(pattern, text, d)
# print(result)

# but to print only numbers seperated by spaces, following is the program:

result = approximate_pattern_matching(pattern, text, d)

print(" ".join(map(str, result))) 





