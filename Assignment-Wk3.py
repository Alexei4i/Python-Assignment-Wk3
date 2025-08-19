# 1
def calculate_discount(price , discount_percent):
    price = float(price)
        
    discount = discount_percent / 100
    discount_amount = price * discount

    discount_price = price - discount_amount
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        return discount_price
    else:
        return price
# 2
price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(price, discount_percent)
# Output the final price
print(f"The final price after discount is: ${final_price}")


