#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    connections = {}
    for ticket in tickets:
        connections[ticket.source] = ticket.destination

    route = []
    source = "NONE"
    for i in range(length):
        dest = connections[source]
        route.append(dest)
        source = dest

    return route
