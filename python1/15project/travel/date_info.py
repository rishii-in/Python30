from datetime import datetime
def date_time():
    print("\n===================================")
    print("           Date and Time             ")
    print("======================================")
    print()
    now = datetime.now()
    print(f"Today Date : {now.strftime('%A %d-%m-%Y')}")
    print(f"Current Time : {now.strftime('%I:%M:%S %p')}")
    print()
