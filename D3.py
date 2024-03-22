def digit_square_sum(num):
    
    sum_squares = 0
    while num > 0:
        digit = num % 10
        sum_squares += digit ** 2
        num //= 10
    return sum_squares

def is_happy(n):
    visited = set()
    
    while n != 1 and n not in visited:
        visited.add(n)
        n = digit_square_sum(n)
    
    return n == 1


number = int(input("Enter a number to check if it's happy: "))
result = is_happy(number)
print("Is the number happy?", result)
