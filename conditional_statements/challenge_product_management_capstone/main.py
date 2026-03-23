# Input variables
days_until_expiration = 7  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if days_until_expiration <= 3 and product_type == "Perishable" and stock_level > 50:
    print("30% discount applied")

elif days_until_expiration in range(4,6) and product_type == "Perishable" and stock_level > 50:
    print("20% discount applied")

elif days_until_expiration >= 7 and product_type == "Perishable" and stock_level <=50:
    print("10% discount applied")

else:
    product_type != "Perishable"
    print("No discount available for non-perishable items.")