import General, FlightAvail, SeatsAvail
import random

tickets = []

def updateSeats(flight, seats):
    for f in General.flights:
        if f == flight:
            General.flights[flight]["Seats"] -= seats

def generateTicket(flight, passengers):
    global tickets
    for p in passengers:
        ticketId = random.randint(100000, 999999)
        while ticketId in General.passengers:
            ticketId = random.randint(100000, 999999)
        name = p[0]
        age = p[1]
        phone = p[2]
        tickets.append([ticketId, name, flight, age, phone])
        print()
        print("-"*50)
        print("Ticket Generated")
        print("\nTicket Id:", ticketId)
        print("Name:", name)
        print("-"*50)
        General.passengers[ticketId] = {"Name":name, "Flight":flight, "Age":age, "PhoneNo":phone}
    updateSeats(flight, len(passengers))
   



def getPassengerInfo():
    passengersInfo = []
    global n
    n = int(input("Enter no. of passengers: "))
    for i in range(n):
        name = input("\nEnter name: ")
        age = int(input("Enter age: "))
        phoneNo = int(input("Enter phone No: "))
        passengersInfo.append([name, age, phoneNo])
    return passengersInfo



def paymentProcess(flight):
    global n
    flInfo = General.flights[flight]
    print("-"*80)
    print("Flight\t\tDeparture\t\tArrival\t\tCost\n")
    print(flight, flInfo["Departure"], flInfo["Arrival"], flInfo["Cost"], sep="\t\t")
    print("-"*80)
    print()
    passengers = getPassengerInfo()
    amount = int(input("\nPay amount: "))
    if amount>flInfo["Cost"]*n:
        balanceAmount = amount - flInfo["Cost"]
        print("Rs.%d returned as balance\n"%balanceAmount)
        generateTicket(flight, passengers)
    elif amount == flInfo["Cost"]*n:
        generateTicket(flight, passengers)
    else:
        amountRequired = (flInfo["Cost"]*n) - amount
        while amountRequired>0:
            print("Rs. %d more required"%amountRequired)
            amountEnterred = int(input("Enter remaining amount: "))
            amountRequired -= amountEnterred
            if(amountRequired<0):
                print("Rs. %d is return."%-amountRequired)
                generateTicket(flight, passengers)
                break
        else:
            print("Rs. %d is return."%-amountRequired)
            generateTicket(flight, passengers)
        print()
        

def bookFlight():
    source = input("Enter source: ")
    dest = input("Enter destination: ")
    p_flights = FlightAvail.checkFlights(source, dest)
    flights = []
    for i in p_flights:
        if SeatsAvail.checkSeats(i)[0][1] > 0:
            flights.append(i)
    print("-------------------------------Flights Available-----------------------------\n")
    print("Flight\t\tDeparture Time\t\tArrival Time\tSeats\t\tCost\n")
    for i in flights:
        print(i, General.flights[i]["Departure"], General.flights[i]["Arrival"], General.flights[i]["Seats"], General.flights[i]["Cost"], sep="\t\t")
    print("\n-----------------------------------------------------------------------------")
    fl = input("\nEnter flight name that you want to travel: ")
    while fl not in General.flights:
        print("Invalid flight name")
        fl = input("\nEnter flight name that you want to travel: " )
    print()
    paymentProcess(fl)

