def calculate_price(loaves):
    regular_price = loaves * 185 
    discount = regular_price * 0.6  
    total_price = regular_price - discount
    return regular_price, discount, total_price


loaves = int(input("Enter the number of loaves of day-old bread: "))


regular_price, discount, total_price = calculate_price(loaves)


print(f"Regular Price: {regular_price:.2f} rupees")
print(f"Discount: {discount:.2f} rupees")
print(f"Total Price: {total_price:.2f} rupees")
