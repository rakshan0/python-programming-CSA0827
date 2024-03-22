def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    
    for num in l:
        if num % 2 == 0:  
            even_sum += num ** 2
        else:
            odd_sum += num ** 2
    
    return [odd_sum, even_sum]


elements = int(input("Enter the number of elements: "))
input_list = []
for _ in range(elements):
    num = int(input("Enter the element: "))
    input_list.append(num)


result = sumsquare(input_list)
print("Output:")
print(result)
