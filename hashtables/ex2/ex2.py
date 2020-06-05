#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    Hash each ticket: source as key and destination as value
    """
    route = [None] * length
    trips = {}

    for ticket in tickets:
        if ticket.source == 'NONE':
            start = ticket
        
        trips[ticket.source] = ticket.destination

    route[0] = start.destination

    for i in range(1, length):
        source = route[i - 1]

        route[i] = trips[source]

    return route