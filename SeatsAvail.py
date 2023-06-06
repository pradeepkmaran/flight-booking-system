import General

def checkSeats(flight):
    seatsAvail = []
    for i in General.flights:
        if i == flight:
            seatsAvail.append([i, General.flights[i]["Seats"]])
    return seatsAvail