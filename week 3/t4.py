# Ask user for phrase
print("Please enter a phrase?")
phrase = input()

# Declare a control variable
hellos = 0

# Display hi
print()

while hellos < len(phrase):
    print("Hi ", end="")
    hellos = hellos + 1