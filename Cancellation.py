import General, Booking

#passengers = General.passengers
flights = General.flights
passengers = General.passengers
            

def cancel():
    ticketId = int(input("Enter ticket Id: "))
    if ticketId in passengers:
        bookedFl = passengers[ticketId]["Flight"]
        refundPercent = flights[bookedFl]["Refund"]
        refundAmount = refundPercent/100*flights[bookedFl]["Cost"] if refundPercent>0 else "Non Refundable"
        print()
        print("Flight Name", "Source","Destination", "Cost", "Refund Amount", sep="\t\t")
        for k in flights:
            if bookedFl == k:
                print(k, flights[k]["Source"], flights[k]["Destination"], flights[k]["Cost"], refundAmount, sep="\t\t")
        for i in Booking.tickets:
            if i[0] == ticketId:
                Booking.tickets.remove(i)
        del General.passengers[ticketId]
        print("\nTICKET %d CANCELLED\n"%ticketId)
        General.flights[bookedFl]["Seats"] += 1
        if refundAmount != "Non Refundable":
            print("Rs. %d refunded\n"%refundAmount)

    else:
        print("Invalid ticket Id")
    
