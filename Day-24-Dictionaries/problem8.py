inventory = {
    "pen": 10,
    "pencil": 0,
    "eraser": 5,
    "notebook": 0
}

cleared_inventory = {}

for key,value in inventory.items():
    if value >0:
        cleared_inventory[key] = value

print(cleared_inventory)