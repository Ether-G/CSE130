# 1. Name:
#      Benjamin Black
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if a player can build a hotel on Pennsylvania Avenue
#      in Monopoly based on various game conditions including property ownership,
#      current buildings, available pieces, and funds.
# 4. What was the hardest part? Be as specific as possible.
#      Configuring OBS again, I am travelling this week so I recorded and did this project in a McDonalds.
# 5. How long did it take for you to complete the assignment?
#       ~ 90 mins - 2 hours

def get_valid_building_input(prompt):
    """Get and validate building input (0-5)"""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 5:
                return value
            print("Please enter a number between 0 and 5")
        except ValueError:
            print("Please enter a valid number")

def get_valid_cash_input():
    """Get and validate cash input"""
    while True:
        try:
            value = int(input("How much cash do you have to spend? "))
            if value >= 0:
                return value
            print("Please enter a non-negative amount")
        except ValueError:
            print("Please enter a valid number")

def get_valid_pieces_input(prompt):
    """Get and validate pieces input"""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter a non-negative number")
        except ValueError:
            print("Please enter a valid number")

def main():
    # First check if player owns all properties
    owns_all = input("Do you own all the green properties? (y/n) ").lower()
    if owns_all != 'y':
        print("\nYou cannot purchase a hotel until you own")
        print("         all the properties of a given color group.")
        return

    # Get current buildings on properties
    pa = get_valid_building_input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
    
    # If PA already has a hotel, no need to continue
    if pa == 5:
        print("\nYou cannot purchase a hotel if the property already has one.")
        return

    # Get buildings on other properties
    pc = get_valid_building_input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
    nc = get_valid_building_input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")

    # Check for hotel swaps first
    if pc == 5 and pa == 4:
        print("\nSwap Pacific's hotel with Pennsylvania's 4 houses.")
        return
    if nc == 5 and pa == 4:
        print("\nSwap North Carolina's hotel with Pennsylvania's 4 houses.")
        return

    # Get available pieces and cash $$
    houses = get_valid_pieces_input("How many houses are there to purchase? ")
    hotels = get_valid_pieces_input("How many hotels are there to purchase? ")
    cash = get_valid_cash_input()

    # Check if hotel is available
    if hotels < 1:
        print("\nThere are not enough hotels available for purchase at this time.")
        return

    # Calculate needed houses and cost
    houses_needed = 0
    if pc < 4:
        houses_needed += (4 - pc)
    if nc < 4:
        houses_needed += (4 - nc)
    if pa < 4:
        houses_needed += (4 - pa)

    # Check if enough houses are available
    if houses < houses_needed:
        print("\nThere are not enough houses available for purchase at this time.")
        return

    # Calculate total
    total_cost = 200 + (houses_needed * 200)

    # Enough MONEY???
    if cash < total_cost:
        print("\nYou do not have sufficient funds to purchase a hotel at this time.")
        return

    # Display the message
    if houses_needed == 0:
        print(f"\nThis will cost ${total_cost}.")
        print("         Purchase 1 hotel and 0 house(s).")
        print("         Put 1 hotel on Pennsylvania and return any houses to the bank.")
    elif pc < 4 and nc < 4:
        print(f"\nThis will cost ${total_cost}.")
        print(f"         Purchase 1 hotel and {houses_needed} house(s).")
        print("         Put 1 hotel on Pennsylvania and return any houses to the bank.")
        print(f"         Put {4 - nc} house(s) on North Carolina.")
        print(f"         Put {4 - pc} house(s) on Pacific.")
    elif pc < 4:
        print(f"\nThis will cost ${total_cost}.")
        print(f"         Purchase 1 hotel and {houses_needed} house(s).")
        print("         Put 1 hotel on Pennsylvania and return any houses to the bank.")
        print(f"         Put {4 - pc} house(s) on Pacific.")
    elif nc < 4:
        print(f"\nThis will cost ${total_cost}.")
        print(f"         Purchase 1 hotel and {houses_needed} house(s).")
        print("         Put 1 hotel on Pennsylvania and return any houses to the bank.")
        print(f"         Put {4 - nc} house(s) on North Carolina.")

if __name__ == "__main__":
    main()