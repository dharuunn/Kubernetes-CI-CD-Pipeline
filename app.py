def calculate_bill(price, quantity, discount_percentage=0.0):
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percentage / 100)
    return subtotal - discount_amount
def main():
    print("=== Shopping Bill Calculator (With Discount) ===")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        discount = float(input("Enter discount percentage (0-100): "))        
        if price < 0 or quantity < 0 or not (0 <= discount <= 100):
            print("Invalid value constraints. Please verify your entries.")
            return  
        final_total = calculate_bill(price, quantity, discount)
        print(f"Total Bill (After Discount): ${final_total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
if __name__ == "__main__":
    main()
