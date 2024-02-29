genome = "GCATACACTTCCCAGTAGGTACTG"
count = 0
loop_count = 0
print(count, end=" ")

for nucleotide in genome:
    if nucleotide == 'C':
        count -= 1
        print(count, end=" ")
    elif nucleotide == 'G':
        count += 1
        print(count, end=" ")
    else:
        print(count, end=" ")

    loop_count += 1
#Output a newline for better readability
print()

print(loop_count)