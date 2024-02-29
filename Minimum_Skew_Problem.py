def min_skew(genome):
    skew_values = [0]
    min_skew_value = float('inf')
    min_skew_positions = []

    
    for i in range(1, len(genome) + 1):
        skew_values.append(skew_values[i-1] + (1 if genome[i-1] == 'G' else (-1 if genome[i-1] == 'C' else 0)))
        
       
        if skew_values[i] < min_skew_value:
            min_skew_value = skew_values[i]
            min_skew_positions = [i]
        elif skew_values[i] == min_skew_value:
            min_skew_positions.append(i)

    return min_skew_positions


genome = "GGACCCCGCCCCCCTTGGC"
result = min_skew(genome)

print(result)

#find a  way to remove the [ ] and , in output and just keep space between the numbers