def loot_scanner(chest):
    print("You found:")
    print(chest)

loot_scanner("dragon egg")


# Way 1: Directly
loot_scanner("sword")

# Way 2: Variable
item = "sword"
loot_scanner(item)

# Way 3: From input
item = input("What did you find? ")
loot_scanner(item)

# Way 4: Loop through a list
loot_bag = ["sword", "gold", "potion"]
for item in loot_bag:
    loot_scanner(item)