# Ask user for number of obstacles
print("How many obstacles should I avoid?")
obstacles_to_avoid = int(input())

# Declare a control variable
obstacles_avoided = 0

# Avoid obstacles
print()

while obstacles_avoided < obstacles_to_avoid:
    print("Avoiding...", end="")
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided.")