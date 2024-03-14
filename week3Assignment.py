# Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) and the 
# discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; 
# otherwise, return the original price.
# Using the calculate_discount function, 
# prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, 
# print the original price.

"""price = int(input("Please enter the original price: "))
calculate_discount = int(input("Enter discount applied. It should be between 1-100: "))"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Corrected the comparison
        discPrice = price * (1 - discount_percent / 100)
        return discPrice
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print("No discount applied. Original price:", original_price)
else:
    print("Final price after applying the discount:", final_price)

