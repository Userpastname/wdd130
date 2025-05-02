items = input("what is the number of manufactured items?: ")
box_size = input("what is the number of items the user will pack per box?: ")

items = int(items)
box_size = int(box_size)

boxes = items%box_size

boxers = items-boxes

no_of_boxes = int(boxers/box_size)+1

print(f"For {items} items, packing {box_size} items in each box, you will need {round(no_of_boxes,0)} boxes.")