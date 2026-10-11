from travel import activities
def trip():
    dest=input("enter destination:").title()
    days=int(input("enter no of days:"))
    nights=int(input("enter no of nights:"))
    t_dist=int(input("enter transport distance:"))
    t_cost=int(input("enter transport cost per km:"))
    h_cost=int(input("enter hotel cost per night:"))
    f_cost=int(input("enter food cost per day:"))

    def calculate_transport_cost(t_dist,t_cost):
        return t_dist*t_cost
    def calculate_hotel_cost(nights,h_cost):
        return nights*h_cost
    def calculate_food_cost(days, f_cost):
        return days*f_cost
    total_budget=(t_dist*t_cost)+(nights*h_cost)+(days*f_cost)

    print("\n======================================")
    print("         Trip Summary          ")
    print("======================================")
    print()
    print(f"{'Destination':<15}: {dest}")
    print(f"{'Days':<15}: {days}")
    print(f"{'Nights':<15}: {nights}")
    print()
    print(f"{'Transport Cost':<15}: ₹{calculate_transport_cost(t_dist,t_cost)}")
    print(f"{'Hotel cost:':<15}: ₹{calculate_hotel_cost(nights,h_cost)}")
    print(f"{'Food cost:':<15}: ₹{calculate_food_cost(days, f_cost)}")
    print()
    print(f"{'Total Trip cost':<15}: ₹{total_budget}")
    print()
    print(f"{'Recommended Activity':<15}: {activities.get_random_activity()}")
    print("=============================================")