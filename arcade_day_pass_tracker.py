"""Arcade Day Pass Tracker challenge solution."""

customer_name = input("Enter your name: ")
passes = int(input("Enter the number of passes: "))
tokens_per_pass = 12
price_per_pass = 43.4
tokens_required = 5

# Calculations
total_tokens = passes * tokens_per_pass
total_cost = passes * price_per_pass
games_available = total_tokens // tokens_required

# Summary
print("\n--- Arcade Day Pass Summary ---")
print(f"Customer name: {customer_name}")
print(f"Passes bought: {passes}")
print(f"Total tokens: {total_tokens}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Games available: {games_available}")
