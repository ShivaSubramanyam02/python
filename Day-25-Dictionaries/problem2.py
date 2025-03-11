inventory = {
    "pen": 10,
    "pencil": 0,
    "eraser": 5,
    "notebook": 0
}

empty_dict = {}

for key,value in inventory.items():
    if value > 0:
        empty_dict[key] = value
        
print(empty_dict)