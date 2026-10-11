from travel import budget,t_budget,activities,date_info

while True:
    print("\n======================================")
    print("        Smart Travel Planner          ")
    print("=======================================")
    print()
    print("1.Plan My Trip")
    print("2.Calculate Travel Budget")
    print("3.Get Random Activity")
    print("4.Show Current Date and Time")
    print("5.Exit")
    print()
    ch=int(input("Enter your Choice:"))

    if ch==1:
        print()
        budget.trip()
    elif ch==2:
        print()
        t_budget.travel_budget()
    elif ch==3:
        print()
        activities.recommended()
    elif ch==4:
        print()
        date_info.date_time()
    elif ch==5:
        print()
        print("Thank you for using Smart Travel Planner!")
        print("Have a safe journey! ✈️\n")
        break
    else:
        print()
        print("Invalid choice !!")
