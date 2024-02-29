def find_clumps(text, k, L, t):
    patterns = []
    n = len(text)
    
    for i in range(n - L + 1):
        window = text[i:i+L]
        freq_map = frequency_table(window, k)
        
        for s in freq_map:
            if freq_map[s] >= t:
                patterns.append(s)
    
    # Remove duplicates from Patterns
    patterns = list(set(patterns))
    
    return patterns

def frequency_table(s, k):
    freq_map = {}
    n = len(s)
    
    for i in range(n - k + 1):
        kmer = s[i:i+k]
        if kmer in freq_map:
            freq_map[kmer] += 1
        else:
            freq_map[kmer] = 1
    
    return freq_map

# Example usage:
text = "GGGACCCCCCCTATTGGTT"
L = 500
t = 3
k = 9

result = find_clumps(text, k, L, t)
print(result)
