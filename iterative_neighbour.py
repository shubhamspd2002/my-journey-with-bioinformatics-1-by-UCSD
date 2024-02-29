#to implement an iterative version of Neighbors instead, shown below. This gives the same op as neighbour.py file. Try and find the difference
#in their run time and algorithm

def iterative_neighbors(pattern, d):
    neighborhood = {pattern}

    for j in range(1, d + 1):
        current_neighbors = set()
        for pattern_prime in neighborhood:
            current_neighbors.update(immediate_neighbors(pattern_prime))
        
        neighborhood.update(current_neighbors)
    
    return neighborhood

def immediate_neighbors(pattern):
    neighbors = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in 'ACGT':
            if nucleotide != symbol:
                neighbor = pattern[:i] + nucleotide + pattern[i+1:]
                neighbors.add(neighbor)
    
    return neighbors

# Example usage:
pattern = "ACG"
d = 1
result = iterative_neighbors(pattern, d)

print(result)