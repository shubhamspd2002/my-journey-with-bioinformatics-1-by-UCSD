#So you want to loop through 2 lists comparing each index to its comparative index and return the number of differences.
# Python has a function called zip() that u can find helpful in this situation. 
# It can take 2 (or more) iterables and return a tuple of each index aggregate until the shorter runs out. 
# For example string1 = 'GGG' and string2 ='GGA' then zip(string1, string2) returns (('G','G'),('G','G'),('G','A')).



genome_1 = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'

genome_2 = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'

if len(genome_1) != len(genome_2):
    
    print("the number of nucleotides do not match")
    
else: 
    
    
    def hamming(genome_1, genome_2):

        if len(genome_1) == len (genome_2):
        
            count = 0

        for n, j in zip(genome_1, genome_2):

                    if n != j:

                             count += 1

                    else:

                              pass
        
        return count
    
    hamming_distance = hamming(genome_1, genome_2)

    print(hamming_distance)  

#if u put 1 additional nucleuotide in any DNA string, it will give op as "the number of nucleotides do not match"
#the op of this program is 829. That means that there are 829 mismatches in both the genomes or kmers