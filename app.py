def calculate_bill(price, quantity):
    return price * quantity
def main():
    print("=== Shopping Bill Calculator ===")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        if price < 0 or quantity < 0:
            print("Price and quantity must be positive values.")
            return        
        total = calculate_bill(price, quantity)
        print(f"Total Bill: ${total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
if __name__ == "__main__":
    main()
    