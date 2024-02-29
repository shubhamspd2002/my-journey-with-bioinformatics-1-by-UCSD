
# Example usage:
n = int(input("Enter a positive integer n: "))


def recursive_gauss_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_gauss_sum(n - 1)

result = recursive_gauss_sum(n)

print(f"The sum of the first {n} integers is: {result}")