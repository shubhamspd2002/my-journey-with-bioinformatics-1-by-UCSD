#this program is to find the total number of patterns occuring in text with atmost d mismatches.
#it is represented as countd(text, pattern) [d is in subscriprt]

def count_pattern_with_mismatches(sequence, pattern, d):
    count = 0

    # Iterate through the sequence with a sliding window of the pattern length
    for i in range(len(sequence) - len(pattern) + 1):
        mismatch_count = 0

        # Check each position in the pattern
        for j in range(len(pattern)):
            if sequence[i + j] != pattern[j]:
                mismatch_count += 1

            # If the number of mismatches exceeds the allowed threshold, break the inner loop
            if mismatch_count > d:
                break

        # If the total number of mismatches is within the allowed threshold, increment the count
        if mismatch_count <= d:
            count += 1

    return count

# Example usage
sequence = "CGTGACAGTGTATGGGCATCTTT"
pattern = "TGT"
d = 1
result = count_pattern_with_mismatches(sequence, pattern, d)
print(f"Count of occurrences of {pattern} with at most {d} mismatch(es): {result}")
