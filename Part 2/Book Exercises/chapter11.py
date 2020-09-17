# Exercise 1

    # Situation 1

classrooms = [{"name": "C01", "info": "no computers, no whiteboard"}, {"name": "D06", "info": "no mini-whiteboards, 25x computer, 6x laptop"}]

for classroom in classrooms:
    print("=" * 50)
    for key, value in classroom.items():
        print(f"{key}: {value}")
    print("=" * 50)

    # Situation 2

online_shop = [
                {"category": "dairy", "items": ["skimmed milk", "semi-skimmed milk", "yoghurt", "cheese", "long-life milk"]}, 
                {"category": "bakery", "items": ["tiger bread", "seedless bread", "chocolate muffin", "butter croissant", "strawberry pancake"]}
            ]

for category in online_shop:
    print("=" * 50)
    for key, value in category.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"- {item}")
        else:
            print(f"{key}: {value}")
    print("=" * 50)