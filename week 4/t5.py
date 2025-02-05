# The function with a single parameter named 'plan'
def escape_by(plan):
    # Determine which message to display
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure about that plan!")

# Calls to the function
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")