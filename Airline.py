import Booking, Cancellation

while(True):
    print("\n===================AIRLINE RESERVATION SYSTEM=================\n")
    print("1. Book flights for trip")
    print("2. Cancel your trip\n")

    print("Enter -1 to exit airline reservation system\n")

    resp = int(input("What do you want to do?(1/2/-1): "))
    if resp == 1:
        Booking.bookFlight()
    elif resp == 2:
        Cancellation.cancel()
    elif resp == -1:
        print("\n**************EXITTING AIRLINE RESERVATION SYSTEM***************")
        break
    else:
        print("Invalid Input")