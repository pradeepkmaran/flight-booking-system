import General

def checkFlights(source, dest):
    availFlights = ()
    for i in General.flights:
        if General.flights[i]["Source"] == source and General.flights[i]["Destination"] == dest:
            if General.flights[i]["Seats"] > 0:
                availFlights += (i,)
    return availFlights