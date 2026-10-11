import random 
l1=["Beach Visit", "Mountain Trek", "City Tour",
 "Local Food Tour", "Museum Visit", "Shopping"]
def get_random_activity():
    return random.choice(l1)
def recommended():
    print()
    print("===============================")
    print("       Travel Activity         ")
    print("================================")
    print()
    print("Recommended Activity:")
    print(random.choice(l1))
    print()
    print("Enjoy your Trip!\n")