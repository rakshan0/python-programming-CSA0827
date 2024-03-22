from itertools import combinations

def find_combinations(digits):
    # Convert digits string to a list of integers
    digits_list = [int(d) for d in digits]

    # Find all combinations of 3 digits
    digit_combinations = list(combinations(digits_list, 3))

    return digit_combinations

# Example usage
input_digits = "123"
combinations_result = find_combinations(input_digits)
print("All combinations of 3 digits:", combinations_result)
